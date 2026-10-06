---
tags:
  - backend
  - distributed-systems
  - system-design
  - architecture
  - redis
  - database
  - security
  - fintech
date: 2026-09-11
---

# Day 42 - Week 6 Review: Distributed Concurrency, Scalable Rate Limiting, Zero-Downtime Migrations & Resilient Fintech Architectures

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Week 6 Architectural Synthesis: Distributed Coordination & Resilient Systems

Week 6 synthesized the core infrastructure components required to run fault-tolerant, high-concurrency microservices, fintech platforms, and event-driven architectures under heavy production traffic:

```text
┌──────────────────────────────────── Production Distributed Systems Topology ────────────────────────────────────┐
│                                                                                                                 │
│  Inbound Traffic (API Gateway & Edge Tier)                                                                      │
│  • Multi-Tier Rate Limiting: Cloudflare WAF (L7 Floods) ──► Envoy Gateway (Global Quotas)                      │
│  • Edge Dynamic Feature Evaluation (MurmurHash3 Deterministic User Canary Bucketing)                            │
│         │                                                                                                       │
│         ▼                                                                                                       │
│  Application & Concurrency Layer (Node.js / Fastify / Next.js)                                                  │
│  • Distributed Mutual Exclusion: Redis Lua Atomic Locks & Multi-Master Redlock Quorums                          │
│  • Storage-level fencing protection (Monotonic Fencing Tokens)                                                  │
│         │                                                                                                       │
│         ├─────────────────────────────────┬──────────────────────────────────┬──────────────────────────────────┤
│         ▼                                 ▼                                  ▼                                  ▼
│  Database Layer                   Fintech Payment Core               Outbound Webhook Pipeline          Configuration Sync
│  • PostgreSQL 16+                 • Stripe PaymentIntents Lifecycle  • Transactional Outbox (DB)        • Real-Time SSE Stream
│  • Zero-Downtime Expand-Contract  • Double-Entry Bookkeeping Ledger  • Redis/BullMQ Worker Dispatchers  • In-Memory Flag Engine
│  • Safe DDL (`lock_timeout = 2s`) • Cryptographic HMAC-SHA256 Sign.  • Exponential Backoff + Jitter     • Sub-Microsecond Evals
│  • Concurrent Index Creation      • Idempotency Deduplication Tables • Circuit-Breaker Auto-Suspension  • Instant Kill Switches
│                                                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Core Resilient Systems Architectural Pillars

#### 1. Distributed Concurrency & Fencing Tokens

- Single-instance in-memory locks fail across multi-node clusters. Atomic Redis locking (SET key token NX PX ttl) with Lua release scripts guarantees mutual exclusion.

- In multi-datacenter setups, the **Redlock Algorithm** achieves consensus across independent master nodes.

- To eliminate lost update hazards caused by long Garbage Collection pauses or network freezes, databases enforce **Monotonic Fencing Tokens**, rejecting writes from stale lock holders.

#### 2. Multi-Tier Rate Limiting & Traffic Shaping

- Layer 7 DDoS mitigation requires defense-in-depth: Edge WAF drops volumetric floods, Gateways enforce API key limits, and application layers execute **Atomic Token Bucket** scripts in Redis to accommodate natural bursts while enforcing strict continuous replenishment.

#### 3. Zero-Downtime Database Schema Migrations

- Naive DDL migrations acquire ACCESS EXCLUSIVE table locks that queue behind long-running queries, rapidly starving connection pools and triggering cascading 504 outages.

- The **Expand and Contract Pattern** decomposes changes into 5 safe phases across multiple code deployments: Expand schema \$\\rightarrow\$ Dual-write \$\\rightarrow\$ Background backfill \$\\rightarrow\$ Read cutover \$\\rightarrow\$ Contract schema. Always set lock_timeout = '2s' and use CREATE INDEX CONCURRENTLY.

#### 4. High-Integrity Fintech & Asynchronous Event Broadcasting

- Payment states are treated as strict finite state machines. Webhooks are treated as distributed, out-of-order, at-least-once deliveries requiring HMAC-SHA256 signature verification and **Idempotency Deduplication Tables**.

- Money is represented exclusively through an immutable **Double-Entry Bookkeeping Ledger** (\$\\sum \\text{Debits} = \\sum \\text{Credits}\$).

- Outbound event delivery decouples business logic via the **Transactional Outbox Pattern**, using exponential retry queues with randomized jitter and circuit-breaker auto-suspension to protect against slow or dead consumer endpoints.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Distributed Infrastructure Patterns Reference Matrix:

--------------------------------------------------------------------------- **Pattern**           **Primary Problem **Core Primitive  **Guarantees Solved**          / Technology**    Provided** --------------------- ----------------- ----------------- ----------------- **Distributed Lock**  Multi-instance    Redis SET NX PX,  Mutual exclusion race conditions   Redlock           across cluster

**Fencing Token**     Client GC pause   Monotonic DB      Absolute split-brain       version counter   storage-level write isolation

**Token Bucket**      API overuse &     Redis Lua script  Bursty throughput noisy neighbors                     with fixed average rate

**Expand-Contract**   Migration lock    Phased deployment Zero-downtime table starvation  / Dual-write      schema evolution

**Double-Entry        Financial         Balanced          Mathematical Ledger**              corruption &      debit/credit DB   auditability & balance drift     rows              zero data loss

**Transactional       Dual-write        PostgreSQL        Exactly-once Outbox**              message loss      table + Debezium  publish intention / Workers ---------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Full-Scale Architecture: Global Fintech Payment & Webhook Platform

Architect an enterprise-scale global payment processing and outbound webhook broadcasting platform handling \$100M+ in daily transaction volume:

**Requirements**:

1.  **Concurrency & Payment Execution**:

    - High-throughput checkout API with distributed Redis locking, monotonic fencing tokens, and zero double-charge guarantees.

    - Dual-entry ledger schema in PostgreSQL with row-level transaction isolation.

2.  **Outbound Webhook Delivery Engine**:

    - Dispatches up to 20,000,000 webhook events per day across thousands of merchant endpoints.

    - Multi-tenant worker queues with noisy-neighbor isolation, SSRF protection against internal IPs, and an exponential backoff retry scheduler over a 72-hour delivery window.

3.  **Continuous Zero-Downtime Upgrades**:

    - End-to-end strategy for migrating the primary payment table schema while receiving continuous 24/7 transaction traffic with zero failed requests.

### Problem 2: Idempotent Payment Transaction & Webhook Dispatch Gateway in TypeScript

Build an End-to-End **Payment & Webhook Gateway Service** in TypeScript using Prisma and Redis:

**Requirements**:

1.  **Idempotent Payment Processor (processPaymentTransaction)**:

    - Uses an atomic Redis lock on the customer cart ID to prevent double submissions.

    - Executes an atomic PostgreSQL transaction that verifies balance, records balanced Debit/Credit entries in a ledger table, and inserts an event into the webhook_outbox table.

2.  **Outbox Worker Dispatcher (dispatchOutboxEvents)**:

    - Polls and claims un-dispatched events atomically.

    - Computes HMAC-SHA256 signature headers (X-Webhook-Signature).

    - Dispatches HTTP POST with a strict 5-second AbortController timeout.

    - On delivery failure, increments retry count and reschedules with exponential backoff.
