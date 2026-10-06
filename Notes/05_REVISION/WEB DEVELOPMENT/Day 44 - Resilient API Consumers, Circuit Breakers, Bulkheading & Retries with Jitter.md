---
tags:
  - backend
  - distributed-systems
  - resilience
  - circuit-breaker
  - bulkheading
  - system-design
  - microservices
  - architecture
date: 2026-09-13
---

# Day 44 - Resilient API Consumers, Circuit Breakers, Bulkheading & Retries with Jitter

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Cascading Failure Problem in Distributed Systems

In a microservices architecture, services continually consume external dependencies (databases, third-party payment gateways, fraud scoring APIs, authentication providers).

When a downstream dependency experiences degraded latency (e.g. response time increases from 100ms to 25 seconds):

1.  **Thread / Socket Pool Exhaustion**: Upstream calling services hold connection sockets and Node.js event loop handles open waiting for responses.

2.  **Resource Starvation**: Incoming requests queue up, consuming memory buffers and socket handles until the calling service exhausts memory or file descriptors.

3.  **Cascading Collapse**: Failure ripples backward through API Gateways to frontends, taking down unrelated healthy business services.

```text
┌────────────────────────────────────── Cascading Microservice Failure ──────────────────────────────────────┐
│                                                                                                            │
│   Incoming Users (2,000 req/sec)                                                                           │
│        │                                                                                                   │
│        ▼                                                                                                   │
│   [ Checkout Service ] ─────────────────────────► Exhausts all 100 available HTTP client connections!       │
│        │                                                                                                   │
│        ├──► Sits blocked waiting for slow API... (25s latency per call)                                    │
│        │                                                                                                   │
│        ▼                                                                                                   │
│   [ Third-Party Fraud API ] ──► Experiencing network outage / packet drop!                                 │
│                                                                                                            │
│   Consequence: Checkout crashes ──► API Gateway times out ──► Entire platform offline! 💥                  │
│                                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The 4 Pillars of Resilient Client Architecture

#### 1. Immutable Timeouts: Fail Fast

Never allow an outgoing HTTP call to execute without an explicit, bounded timeout:

```typescript
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 2000); // 2-second timeout

try {
  const res = await fetch('https://api.thirdparty.com/v1/charge', { signal: controller.signal });
} finally {
  clearTimeout(timeoutId);
}
```

#### 2. Exponential Backoff with Full Jitter

Naive retries (e.g. retrying every 1 second) create a **Retry Storm / Thundering Herd**, DDOSing the downstream service just as it attempts recovery.

**Full Jitter** decorrelates retry attempts across distributed callers: \$\$\\text{Sleep Time} = \\text{random}(0, \\min(M, B \\times 2^{\\text{attempt}}))\$\$ Where \$B\$ is the base delay (e.g. 100ms) and \$M\$ is the maximum delay cap (e.g. 10 seconds).

### 3. Circuit Breaker State Machine

The **Circuit Breaker** acts as an automatic electrical breaker protecting your system:

- **CLOSED (Normal)**: Requests pass through to dependency. Tracks failure rate over a rolling time window (e.g. last 50 calls).

- **OPEN (Failing Fast)**: If failure rate exceeds threshold (e.g. \$> 50%\$), the breaker trips immediately. All subsequent requests fail instantly with a cached fallback or error without touching the network!

- **HALF_OPEN (Probing Recovery)**: After a sleep cooldown (e.g. 15s), the breaker allows a single test probe through. If successful, it resets to CLOSED; if it fails, it trips back to OPEN.

```text
┌────────────────────────────────────── Circuit Breaker State Machine ──────────────────────────────────────┐
│                                                                                                           │
│                 ┌──────────────────────────────────────────────────────────┐                              │
│                 │                                                          │                              │
│                 ▼                                                          │ Success Probe                │
│         ┌───────────────┐     Failure Rate > 50% in window         ┌───────────────┐                      │
│         │    CLOSED     │ ───────────────────────────────────────► │     OPEN      │                      │
│         │ (Normal Flow) │                                          │  (Fail Fast)  │                      │
│         └───────────────┘                                          └───────┬───────┘                      │
│                 ▲                                                          │                              │
│                 │                                                          │ Cooldown Expired (15s)       │
│                 │                                                          ▼                              │
│                 │              Probe Failed                        ┌───────────────┐                      │
│                 └───────────────────────────────────────────────── │   HALF_OPEN   │                      │
│                                                                    │ (Single Test) │                      │
│                                                                    └───────────────┘                      │
│                                                                                                           │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4. Bulkheading: Fault Domain Isolation

Named after the watertight compartments in a ship's hull. Even if one compartment is breached, the ship stays afloat.

- Allocate a **dedicated connection pool limit** per dependency (e.g. Max 15 sockets for Fraud API, Max 30 for Payment API, Max 50 for Internal User DB).

- If the Fraud API hangs, only its 15 sockets fill up; the remaining 85 sockets continue serving healthy checkout and user queries.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Resilience Patterns Reference Matrix:

------------------------------------------------------------------------------------ **Pattern**       **Mechanism**        **Primary Danger  **Key Metric to Monitor** Prevented** ----------------- -------------------- ----------------- --------------------------- **Timeout**       AbortController      Hanging socket    http_client_timeout_total exhaustion

**Exponential     \$B \\times 2^a\$   Immediate         Retry distribution Backoff**                              downstream        frequency overload

**Full Jitter**   Uniform random \$(0, Thundering herd   Cluster retry alignment \\text{backoff})\$   retry spikes

**Circuit         State Machine        Cascading         circuit_breaker_state Breaker**         (Closed/Open/Half)   cross-service failure

**Bulkhead**      Concurrency          Resource pool     Active leased sockets per Semaphore            exhaustion        pool ------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Airline Booking Engine Resilient Gateway

Architect a resilient integration gateway for an airline booking platform that consumes 6 legacy Global Distribution Systems (GDS) with erratic latencies (\$50\\text{ms} - 45\\text{s}\$) and frequent downtime:

**Requirements**:

1.  **Multi-Tenant Bulkheading**:

    - Isolates socket and concurrency allocations per GDS provider so a crash in Provider A never slows searches on Provider B.

2.  **Predictive Circuit Breaking**:

    - Automatically opens circuit when p95 latency exceeds 5 seconds or error rate exceeds 20% over a 60-second rolling window.

3.  **Graceful Fallback & Stale Cache Serving**:

    - When a provider circuit opens, returns cached flight schedules flagged with stale: true and a visual indicator rather than failing user searches.

### Problem 2: Production-Grade Resilient HTTP Client in TypeScript

Build an Enterprise **Resilient HTTP Client Wrapper** in TypeScript:

**Requirements**:

1.  **Sliding-Window Circuit Breaker**:

    - Implements states CLOSED, OPEN, HALF_OPEN.

    - Monitors success/failure ratio over a rolling circular buffer of the last 100 requests.

2.  **Semaphore-Based Bulkhead**:

    - Restricts maximum in-flight concurrent requests to \$N\$ (e.g. 10 max concurrent calls). Queues or rejects excess requests immediately with BulkheadCapacityExceededException.

3.  **Full Jitter Exponential Retry Engine**:

    - Automatically retries idempotent idempotent calls on HTTP 502/503/504 or network timeouts using the Full Jitter formula.

    - Attaches telemetry event hooks: onStateChange, onRetry, onCircuitOpen.
