---
tags:
  - backend
  - caching
  - redis
  - cdn
  - cache-stampede
  - performance
  - distributed-systems
  - architecture
date: 2026-09-24
---

# Day 55 - High-Performance Distributed Caching, Cache Stampede Mitigation (XFetch), Multi-Tier CDNs & Cache Invalidation

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Anatomy of a Cache Stampede (Thundering Herd)

In high-throughput distributed architectures, caching serves as the primary shield protecting primary transactional databases (PostgreSQL/MySQL) from query saturation. However, naive caching implementations contain a lethal failure mode: the **Cache Stampede** (or "Thundering Herd"):

- **The Trigger**: A highly popular cache entry (e.g. an e-commerce flash sale catalog receiving \$50,000\\text{ req/sec}\$) expires because its Time-to-Live (TTL) reaches zero, or is evicted under memory pressure.

- **The Collapse**: Within a \$100\\text{ms}\$ window, 5,000 concurrent requests detect a cache miss simultaneously. Every single request executes the expensive database query in parallel.

- **Cascading Outage**: Database CPU surges to 100%, connection pools exhaust, query latencies spike from \$5\\text{ms}\$ to \$30\\text{s}\$, health checks fail, Kubernetes pods crash, and the entire platform collapses.

```text
┌────────────────────────────────────── Cache Stampede Collapse vs. Mitigation ──────────────────────────────────────┐
│                                                                                                                     │
│  Unmitigated Cache Expiration ⚠️:                                                                                   │
│  50,000 req/sec ──► [ Cache MISS ] ──► 50,000 Simultaneous DB Queries! ──► 🚨 Database OOM & Crash!                │
│                                                                                                                     │
│  Mitigated Architecture (XFetch & Singleflight) 🚀:                                                                 │
│  50,000 req/sec ──► [ Singleflight Coalescing ] ──► Exactly 1 Worker Recomputes DB Query! ⚡                        │
│                           │                                                                                         │
│                           └──► 49,999 Waiting Requests Share the Single Returned Result!                            │
│                                                                                                                     │
│  Probabilistic Early Expiration (XFetch):                                                                           │
│  Recomputes hot entries in the background BEFORE the key officially expires! Zero user-facing latency spikes!      │
│                                                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The Three Stampede Defense Strategies

Engineering resilient systems requires combining three distinct defense patterns:

#### Strategy A: Mutex / Distributed Locking (Redlock)

- When a cache miss occurs, the worker attempts to acquire an atomic distributed lock in Redis (SET lock:key token NX EX 5).

- The winner computes the database value and updates the cache; losing workers wait or poll.

- **Drawback**: High lock contention, complex retry loops, and risk of deadlocks if the lock holder crashes.

#### Strategy B: The Singleflight Pattern (Request Coalescing)

- Synchronizes concurrent in-flight requests **within a single Node.js process**.

- If 200 incoming HTTP requests request the same key simultaneously on a worker, Singleflight registers a single active Promise. All 200 requests await that identical Promise, collapsing 200 queries into exactly one database hit.

#### Strategy C: Probabilistic Early Expiration (The XFetch Algorithm)

Introduced by Vattani, Chierichetti, and Lowenstein, **XFetch** uses optimal probabilistic decision theory: Instead of waiting for a key to expire, readers probabilistically trigger background recomputation **before the key expires**. The closer the current time is to the expiration point, and the longer the computation takes (\$\\delta\$), the higher the probability of recomputation:

\$\$\\Delta - \\beta \\cdot \\delta \\cdot \\ln(\\text{random}()) \\le 0\$\$

- \$\\Delta\$: Remaining time until expiration (\$\\text{expiry} - \\text{currentTime}\$).

- \$\\delta\$: Time taken to compute the value on the last calculation.

- \$\\beta\$: Tuning aggressiveness parameter (\$\\beta > 0\$, typically \$1.0\$).

- \$\\text{random}()\$: Uniform random value \$\\in (0, 1]\$.

- **Mathematical Invariant**: If the inequality holds true, the client asynchronously recalculates and extends the cache before any client ever experiences a cache miss!

### 3. Multi-Tier Distributed Caching Topology (L1 / L2 / L3)

Planet-scale architectures do not rely on a single Redis instance; they construct a **hierarchical multi-tier caching topology**:

```text
┌────────────────────────────────────── Multi-Tier Caching Architecture ──────────────────────────────────────┐
│                                                                                                             │
│  Tier 1: In-Memory L1 Process Cache (LRU / TinyLFU inside Node.js Heap)                                      │
│  • Microsecond read latency (<0.01ms), zero network serialization.                                          │
│  • Short TTL (5s - 30s) with stale-while-revalidate.                                                        │
│                                                                                                             │
│  Tier 2: Distributed L2 Cache (Redis Cluster / Dragonfly / KeyDB)                                           │
│  • Shared cluster-wide state, 1ms - 3ms latency over VPC network.                                           │
│  • Stores enriched domain models, serialized JSON/Protobuf, XFetch metadata.                                │
│                                                                                                             │
│  Tier 3: Edge L3 CDN (Cloudflare / Fastly Edge Network)                                                    │
│  • Terminated at 300+ global Anycast edge points of presence (PoPs).                                        │
│  • Serves full HTTP HTML/JSON payloads with sub-20ms TTFB directly to users worldwide.                      │
│                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4. Distributed Cache Invalidation via Surrogate-Keys (Cache-Tags)

Hardcoding URL-based cache purging (PURGE /products/123) breaks when an item appears across hundreds of category, search, and recommendation pages.

Modern CDNs and edge layers utilize **Surrogate-Keys (Cache-Tags)**:

1.  When generating an HTTP response, the backend emits a Cache-Tag or Surrogate-Key header listing all entity IDs contained in the response:

> Surrogate-Key: product-9812 brand-nike category-shoes

2.  When product-9812 is updated in the database, the backend sends a single purge API call to the CDN:

> curl -X POST https://api.cloudflare.com/\.../purge_cache -d > '{"tags": ["product-9812"]}'

3.  The CDN instantly and atomically purges every cached page containing that tag worldwide in \$<150\\text{ms}\$!

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Redis Core Commands for High-Concurrency Caching:

| **Command** | **Signature** | **Performance / Atomic Guarantee** |
| :--- | :--- | :--- |
| `SET key val EX 3600 NX` | Atomic conditional set | Sets key with 1-hour expiration **only if key does not exist**. Used for distributed mutexes. |
| `MGET key1 key2 ...` | Vectorized read | Collapses multiple network round-trips into a single pipelined socket fetch. |
| `GETEX key EX 3600` | Read and refresh | Retrieves value and updates expiration atomically in a single operation. |
| `PUBLISH cache:invalidate key` | Pub/Sub broadcast | Broadcasts cache eviction events to L1 in-memory caches across all Node.js cluster pods. |

### The XFetch Algorithm in TypeScript:

```typescript
interface CacheEntry<T> {
  value: T;
  delta: number;    // Execution duration in seconds
  expiry: number;   // Epoch timestamp in seconds
}

export function shouldRecomputeXFetch<T>(entry: CacheEntry<T>, beta = 1.0): boolean {
  const now = Date.now() / 1000;
  const deltaRemaining = entry.expiry - now;

  // If already expired, must recompute immediately
  if (deltaRemaining <= 0) return true;

  // XFetch decision rule: Δ - β * δ * ln(rand()) <= 0
  const randomFactor = -Math.log(Math.random());
  return (deltaRemaining - (beta * entry.delta * randomFactor)) <= 0;
}
```

### Edge CDN Cache-Tag Headers:

```http
# Cloudflare Enterprise Cache Tagging
Cache-Tag: entity-user-402, entity-team-99, view-dashboard

# Fastly Surrogate Control
Surrogate-Key: product-543 category-footwear
Surrogate-Control: max-age=86400, stale-while-revalidate=3600
```

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Planetary E-Commerce Product Catalog Caching Layer

Design an enterprise-grade multi-tier caching architecture for a global retail platform (Black Friday scale: 1,000,000 requests/sec, 50,000 products):

**Architectural Requirements**:

1.  **Multi-Tier Latency & Blast-Radius Partitioning**:

    - L1 Node.js process memory cache with TinyLFU eviction.

    - L2 Multi-Region Redis cluster with read replicas.

    - L3 Fastly/Cloudflare CDN with Surrogate-Keys.

2.  **Zero-Downtime Cache Stampede Immunity**:

    - Guarantee that when the highest-traffic product page in the catalog expires during peak flash sales, the primary database receives \$\\le 1\$ query per minute.

    - Combine Singleflight request coalescing with the XFetch early expiration algorithm.

3.  **Automated Event-Driven Invalidation Pipeline**:

    - Integrate Change Data Capture (CDC) via Debezium and Kafka to capture inventory changes directly from PostgreSQL WAL logs.

    - Dispatch targeted edge purges via CDN Cache-Tags within \$<200\\text{ms}\$ of database commit.

### Problem 2: Production-Grade Multi-Tier Caching Engine in TypeScript

Implement a complete, production-ready **Multi-Tier Cache Orchestrator** in TypeScript:

**Requirements**:

1.  **L1 / L2 Hierarchical Routing**:

    - Inspects L1 memory cache (e.g. lru-cache). On hit, returns in \$<0.1\\text{ms}\$.

    - On L1 miss, queries L2 (Redis). If found in L2, populates L1 and returns.

2.  **Built-in Singleflight Coalescing**:

    - Manages an in-memory Map<string, Promise<any>>.

    - If 100 callers invoke getOrCompute('catalog', fetchFromDb) simultaneously, only the first caller triggers fetchFromDb(). The remaining 99 callers await the existing promise.

3.  **XFetch Background Recomputation**:

    - Stores { value, delta, expiry } records in Redis.

    - Evaluates shouldRecomputeXFetch(). If triggered, returns the current cached value immediately to the user while spawning an asynchronous background task to recompute and refresh the cache without blocking the caller.

4.  **Integration Test Suite**:

    - Write concurrent test cases simulating 500 parallel callers, proving that fetchFromDb executes exactly once.
