---
tags:
  - backend
  - distributed-systems
  - redis
  - concurrency
  - distributed-locking
  - system-design
  - database
date: 2026-09-05
---

# Day 36 - Distributed Locking, Redlock Algorithm, Concurrency Control & Deadlock Prevention

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Distributed Mutual Exclusion Problem

In a clustered environment (e.g. Kubernetes with multiple replicas of a microservice), in-memory process locks (`Mutex` or `synchronized`) fail because each instance operates in its own memory address space.

Without distributed coordination, concurrent requests create severe data anomalies:

- **Race Conditions**: Two workers process payment or allocate the same physical concert seat simultaneously.
- **Lost Updates**: Worker A overwrites Worker B's state without knowing Worker B modified it.
- **Split-Brain**: Network partitions cause two distinct nodes to each believe they hold the lock.

┌───────────────────────────────────── The Distributed Locking Pitfall ─────────────────────────────────────┐

│                                                                                                          │

│   Worker 1 (Instance A)                       Worker 2 (Instance B)                Shared Resource       │

│   ┌─────────────────────┐                     ┌─────────────────────┐              ┌──────────────────┐  │

│   │ 1. Acquire Lock     │                     │                     │              │ Bank Balance     │  │

│   │    (TTL \= 10s)      │                     │                     │              │ $1000            │  │

│   │ 2. Long GC Pause /  │                     │                     │              └────────┬─────────┘  │

│   │    Disk I/O Delay   │                     │                     │                       │            │

│   │    (Stalls for 12s) │                     │                     │                       │            │

│   │   [Lock Expires!]   │                     │ 3. Acquires Lock    │                       │            │

│   │                     │                     │    (Writes $800)    │ ═════════════════════►│ $800       │

│   │ 4. Wakes Up & Writes│                     │                     │                       │            │

│   │    (Writes $900) ───┼─────────────────────┼─────────────────────┼──────────────────────►│ $900       │

│   └─────────────────────┘                     └─────────────────────┘              (Lost Update! 💥)     │

│                                                                                                          │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. Single-Instance Redis Lock & Atomic Lua Release

A single-node Redis distributed lock relies on atomic creation with lease timeouts and unique ownership tokens:

// 1. Acquire Lock: SET key random\_token NX PX ttl\_ms

// NX: Only set if not already existing

// PX: Expire after ttl\_ms milliseconds

const lockAcquired \= await redis.set('lock:order:4401', workerToken, 'PX', 10000, 'NX');

// 2. Safe Release via Atomic Lua Script:

// Prevents Worker 1 from deleting Worker 2's lock if Worker 1 exceeded its lease TTL!

const unlockLuaScript \= `

  if redis.call("get", KEYS[1]) \== ARGV[1] then

    return redis.call("del", KEYS[1])

  else

    return 0

  end

`;

await redis.eval(unlockLuaScript, 1, 'lock:order:4401', workerToken);

---

### 3. Multi-Node Redlock Algorithm & Fencing Tokens

To tolerate single-master Redis node crashes without split-brain locks, Martin Kleppmann and Salvatore Sanfilippo designed the **Redlock Algorithm**:

1. Run $N$ independent Redis master nodes (typically 5 nodes across distinct fault domains).
2. The client records the current start timestamp $T\_1$.
3. Sequentially attempt to acquire the lock on all $N$ instances using the same key and random value, with a per-instance network timeout (e.g. 5-50ms) much smaller than the total lock TTL.
4. The lock is acquired **if and only if** the client obtains a quorum ($Q \\ge \\lfloor N/2 \\rfloor \+ 1$, e.g. 3 of 5\) and the total elapsed time $T\_2 - T\_1$ is less than the lock validity time.
5. If acquisition fails, immediately send unlock commands to all instances.

#### Fencing Tokens for End-to-End Safety:

A distributed lock can never guarantee complete safety against client-side pauses (Stop-the-World GC pauses, page faults). Storage systems must enforce monotonic **Fencing Tokens**:

Client 1 acquires lock ──► Server returns Fencing Token: 31

Client 2 acquires lock ──► Server returns Fencing Token: 32

Client 1 attempts write with Token 31 ──► Database REJECTS (Current token is already 32!)

---

### 4. Background Lock Heartbeat / Watchdog Pattern

To prevent locks from expiring during legitimately long computations, a background daemon periodically extends the lease:

class LockWatchdog {

  #timer;

  constructor(private redis: Redis, private key: string, private token: string, private ttlMs: number) {

    // Renew lease every TTL / 3

    const interval \= Math.floor(ttlMs / 3);

    this.#timer \= setInterval(async () \=> {

      const extendScript \= `

        if redis.call("get", KEYS[1]) \== ARGV[1] then

          return redis.call("pexpire", KEYS[1], ARGV[2])

        else

          return 0

        end

      `;

      const renewed \= await redis.eval(extendScript, 1, key, token, ttlMs);

      if (!renewed) clearInterval(this.#timer);

    }, interval);

  }

  stop() {

    clearInterval(this.#timer);

  }

}

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Concurrency Control Primitives Comparison:

| Strategy | Scope | Latency | Contention Scenario | Tradeoff |
| :---- | :---- | :---- | :---- | :---- |
| **Pessimistic DB Lock** (`SELECT FOR UPDATE`) | Database Level | High | High Contention | Holds database connections, prone to DB deadlocks |
| **Optimistic DB Lock** (`WHERE version = v`) | Database Level | Low | Low Contention | High retry overhead under heavy write collision |
| **Redis Single-Node Lock** | Cluster/Distributed | Ultra-low | High Contention | Master crash before replica sync drops lock |
| **Redlock (5 Masters)** | Distributed (Multi-DC) | Medium | High Contention | Requires consensus across $\\ge 3$ nodes, network sensitive |
| **Fencing Tokens** | Storage Barrier | Low | All Scenarios | Requires database support for monotonic version check |

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: High-Throughput Flash Sale Ticket Reservation

Design a flash sale ticketing engine for an event with 50,000 concurrent fans competing for 5,000 available seats:

**Requirements**:

1. **Concurrency & Locking Tier**:
   - Zero oversell guarantees utilizing Redis distributed locks with sub-second expiration.
   - Idempotent seat reservation tickets using monotonic Fencing Tokens written to PostgreSQL.
2. **Deadlock Prevention Strategy**:
   - For multi-ticket purchases (e.g. buying 4 seats at once), establish an invariant lock acquisition order (lexicographically ordered by `seat_id`) to mathematically eliminate distributed circular wait deadlocks.
3. **Automatic Expiration & Stock Reclaim**:
   - Reserved seats not checked out within 10 minutes are automatically released back to the general inventory via Redis key expiration notifications (`notify-keyspace-events Ex`) or delayed Kafka topics.

---

### Problem 2: Enterprise Distributed Lock Manager in TypeScript

Build a production-ready **Distributed Lock Manager** in TypeScript using ioredis:

**Requirements**:

1. **Atomic Acquisition & Release (`acquireLock`, `releaseLock`)**:
   - Uses `SET key token PX ttl NX` for acquisition.
   - Releases lock exclusively via atomic Lua script checking `token === stored_token`.
2. **Automatic Heartbeat Extension (Watchdog)**:
   - Starts an automated background renewal loop extending the TTL while the critical task is executing.
   - Automatically stops the watchdog and releases the lock upon completion or error.
3. **Execution Wrapper (`withLock`)**:
   - Implements a higher-order wrapper:

     await lockManager.withLock('resource:order:102', 5000, async (fencingToken) \=> {

       // Critical business logic here

     });

   - Handles retry backoff with randomized jitter to prevent lock acquisition stampedes.

