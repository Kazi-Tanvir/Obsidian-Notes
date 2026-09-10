---
tags:
  - backend
  - security
  - rate-limiting
  - redis
  - system-design
  - api-gateway
  - cloudflare
  - devops
date: 2026-09-06
---

# Day 37 - Rate Limiting at Scale, Token Bucket, Leaky Bucket & Cloudflare WAF Architecture

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Multi-Tier Defense: Why Application-Level Rate Limiting Is Not Enough

Relying solely on rate limiting inside your application code (Express, Fastify, Next.js) is an architectural failure mode. Under a volumetric Layer 7 DDoS attack, parsing TLS, handling TCP handshakes, and executing Node.js middleware for 100,000 requests/second will exhaust CPU and network sockets before rate limiters even evaluate the client.

A production rate-limiting strategy requires **defense-in-depth**:

1. **Edge Tier (Cloudflare WAF / AWS WAF)**: Drops malicious volumetric floods, botnets, and bad IP ranges at edge PoPs before traffic ever touches your origin server.
2. **API Gateway / Reverse Proxy Tier (Kong / Nginx / Envoy)**: Enforces IP-based and client-credential rate limits globally across all upstream microservices.
3. **Application Tier (Node.js \+ Redis)**: Enforces granular, business-logic rate limits (e.g. per-user billing tiers, dynamic cost per endpoint, free vs. premium allowances).

┌────────────────────────────────────── Multi-Tier Rate Limiting Architecture ──────────────────────────────────────┐

│                                                                                                                   │

│   Inbound HTTP Requests (DDoS Attack / Bot Traffic / Legitimate Users)                                            │

│         │                                                                                                         │

│         ▼                                                                                                         │

│  [ Tier 1: Cloudflare WAF / Edge Layer ] ────────► Drops IP reputation anomalies & L7 volumetric floods           │

│         │ (Traffic reduced by 85%)                                                                                │

│         ▼                                                                                                         │

│  [ Tier 2: Envoy / Kong API Gateway ] ───────────► Drops unauthorized traffic & unauthenticated IP floods         │

│         │ (Global rate limits enforced via Redis)                                                                 │

│         ▼                                                                                                         │

│  [ Tier 3: Application Layer (Fastify/Node.js) ] ─► Fine-grained business logic limits (Token Bucket via Redis)   │

│         │                                                                                                         │

│         ▼                                                                                                         │

│   Protected Microservices & Database                                                                              │

│                                                                                                                   │

└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. Algorithmic Deep Dive: Token Bucket vs. Leaky Bucket vs. Sliding Window

#### 1. Token Bucket

- **Mechanism**: A bucket holds up to a maximum capacity of $B$ tokens. Tokens are continuously added at a constant fill rate of $R$ tokens/second. Each request consumes $1$ (or $C$) tokens. If tokens are available, the request passes; otherwise, it is rejected with HTTP 429.
- **Advantage**: Naturally tolerates **bursts** of traffic up to capacity $B$ while maintaining an average rate $R$.
- **Ideal For**: General-purpose REST and GraphQL APIs.

#### 2. Leaky Bucket

- **Mechanism**: Requests enter a FIFO queue of capacity $B$. Requests leak out and are processed at a strictly constant rate $R$. If the queue is full, excess requests leak over the edge and are dropped.
- **Advantage**: Provides **traffic shaping**, producing a perfectly smooth output flow to downstream databases.
- **Ideal For**: Ingestion pipelines, background job queues, and payment gateways.

#### 3. Sliding Window Counter (Memory-Efficient Hybrid)

Instead of keeping individual timestamps in a Redis `ZSET` (which consumes megabytes under high load), the sliding window counter approximates the rate using the current and previous fixed window counts:

$$\\text{Estimated Count} \= \\text{Count}*{\\text{current}} \+ \\text{Count}*{\\text{prev}} \\times (1 - \\text{progress through current window})$$

---

### 3. Distributed Atomic Token Bucket in Redis with Lua

To avoid race conditions and network round-trips across clustered Node.js processes, the entire Token Bucket calculation must execute as an atomic Redis Lua script:

-- token\_bucket.lua

local key \= KEYS[1]

local capacity \= tonumber(ARGV[1])

local fill\_rate \= tonumber(ARGV[2]) -- tokens per millisecond

local now \= tonumber(ARGV[3])       -- current timestamp in ms

local requested \= tonumber(ARGV[4])  -- tokens requested

local data \= redis.call("HMGET", key, "tokens", "last\_updated")

local tokens \= tonumber(data[1])

local last\_updated \= tonumber(data[2])

if not tokens then

  tokens \= capacity

  last\_updated \= now

else

  -- Calculate tokens accumulated since last request

  local elapsed \= math.max(0, now - last\_updated)

  tokens \= math.min(capacity, tokens \+ (elapsed * fill\_rate))

  last\_updated \= now

end

if tokens >= requested then

  tokens \= tokens - requested

  redis.call("HMSET", key, "tokens", tokens, "last\_updated", last\_updated)

  redis.call("PEXPIRE", key, math.ceil(capacity / fill\_rate))

  return { 1, math.floor(tokens) } -- 1 \= Allowed, remaining tokens

else

  redis.call("HMSET", key, "tokens", tokens, "last\_updated", last\_updated)

  return { 0, math.floor(tokens) } -- 0 \= Blocked

end

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Rate Limiting Algorithms Tradeoff Matrix:

| Algorithm | Memory Consumption | Accuracy | Burst Tolerance | Use Case |
| :---- | :---- | :---- | :---- | :---- |
| **Fixed Window** | $O(1)$ (ultra low) | Low (2x boundary spike) | None | Basic internal rate limiting |
| **Sliding Log** | $O(N)$ (high memory) | $100%$ exact | High | Low-frequency critical endpoints |
| **Sliding Counter** | $O(1)$ (ultra low) | $99%$ approximation | Moderate | Large-scale public APIs |
| **Token Bucket** | $O(1)$ (ultra low) | Very High | **Excellent** | SaaS REST APIs (Standard) |
| **Leaky Bucket** | $O(N)$ (buffer size) | High | None (Smooths) | Asynchronous task ingestion |

### Standard IETF HTTP RateLimit Headers:

When returning responses, follow the standard IETF draft headers:

- `RateLimit-Limit`: Maximum requests permitted in the window (e.g. `100`).
- `RateLimit-Remaining`: Tokens remaining in the current bucket (e.g. `42`).
- `RateLimit-Reset`: Seconds until bucket fully refills (e.g. `14`).
- `Retry-After`: Returned on HTTP 429 indicating seconds to wait before retrying.

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Tiered Rate Limiting for a Public Developer API

Design a global rate-limiting platform for a developer API serving 250,000 requests per second across 3 continents:

**Requirements**:

1. **Tiered Billing Quotas**:
   - Free Tier: 60 req/min, burst up to 10.
   - Pro Tier: 1,200 req/min, burst up to 50.
   - Enterprise: Custom limits with dynamic cost weighting (e.g. simple `GET` \= 1 token, complex AI report generation \= 10 tokens).
2. **Global Edge & Multi-Region Redis Sync**:
   - Clients hitting regional edge gateways (US-East, EU-Central, AP-South) must share rate limit state without paying a 200ms cross-continental latency penalty per request (Local caching with asynchronous batched sync).
3. **Graceful Degradation**:
   - If the Redis cluster experiences a network partition or failover, requests must default to a localized fallback policy without crashing the application.

---

### Problem 2: Production Rate Limiter Middleware in TypeScript

Build a production-grade **Token Bucket Rate Limiter Middleware** in TypeScript for Fastify or Express using `ioredis`:

**Requirements**:

1. **Atomic Lua Execution**:
   - Executes the atomic Redis Lua script above via `redis.evalsha()`.
2. **Dynamic Route Cost**:
   - Middleware accepts a custom cost function: `cost: (req) => number` (e.g. heavy exports consume 5 tokens).
3. **IETF Header Compliance**:
   - Automatically attaches `RateLimit-Limit`, `RateLimit-Remaining`, and `RateLimit-Reset` headers to every response.
   - On limit exhaustion, returns HTTP `429 Too Many Requests` with a JSON error payload and `Retry-After` header.

