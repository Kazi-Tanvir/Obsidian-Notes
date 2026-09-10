---
tags:
  - database
  - devops
  - postgresql
  - migrations
  - zero-downtime
  - prisma
  - system-design
  - backend
date: 2026-09-07
---

# Day 38 - Zero-Downtime Database Migrations, Expand-Contract Pattern & Shadow Tables

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Anatomy of Migration Outages: PostgreSQL Lock Contention

In high-throughput web applications handling thousands of queries per second, running naive database schema migrations (`ALTER TABLE ...`) will bring down your service.

The primary culprit is **PostgreSQL Table Locking**:

- An `ALTER TABLE` operation requires an **`ACCESS EXCLUSIVE` lock**.
- An `ACCESS EXCLUSIVE` lock conflicts with **all other locks**, including simple `SELECT` queries.
- Even if the DDL command takes 2 milliseconds to run, if it is queued behind a long-running 10-second `SELECT` statement, **every subsequent query on that table queues behind the migration lock**. Within seconds, your backend connection pool exhausts, returning 500 errors to users.

┌────────────────────────────────────── Lock Queue Contention Scenario ──────────────────────────────────────┐

│                                                                                                              │

│  1. Long-Running Query:                                                                                      │

│     SELECT * FROM orders WHERE ... (Running for 8 seconds, holds ACCESS SHARE lock)                          │

│                                                                                                              │

│  2. Inbound DDL Migration:                                                                                   │

│     ALTER TABLE orders ADD COLUMN status VARCHAR(50); (Requests ACCESS EXCLUSIVE lock)                       │

│     └─► BLOCKED! Must wait for Query 1 to finish.                                                            │

│                                                                                                              │

│  3. Inbound Production Traffic:                                                                              │

│     SELECT / INSERT / UPDATE queries arrive at 2,000 requests/sec.                                            │

│     └─► BLOCKED! Cannot acquire ACCESS SHARE lock because DDL request is pending!                            │

│     └─► Connection pool exhausts ──► Cascading 504 Gateway Timeout Outage! 💥                                │

│                                                                                                              │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. The Expand and Contract (Parallel Run) Pattern

To achieve true zero-downtime migrations when renaming fields, splitting tables, or modifying constraints, architects employ the **Expand and Contract Pattern** across multiple independent deployments:

┌────────────────────────────────────── The 5 Phases of Expand & Contract ──────────────────────────────────────┐

│                                                                                                               │

│  Phase 1: Expand (Database Migration)                                                                         │

│  • Add the new column `new\_status` as nullable without altering `old\_status`.                                 │

│                                                                                                               │

│  Phase 2: Dual-Writing (Application Deployment 1\)                                                             │

│  • Application reads from `old\_status`.                                                                       │

│  • Application writes to BOTH `old\_status` AND `new\_status` on every mutation.                                │

│                                                                                                               │

│  Phase 3: Backfill (Background Worker)                                                                        │

│  • An asynchronous, throttled worker backfills existing historical rows:                                      │

│    `UPDATE orders SET new\_status \= old\_status WHERE new\_status IS NULL LIMIT 1000;`                           │

│                                                                                                               │

│  Phase 4: Read Cutover (Application Deployment 2\)                                                             │

│  • Application switches reading to `new\_status`.                                                              │

│  • Application continues writing to both fields for rollback safety.                                          │

│                                                                                                               │

│  Phase 5: Contract (Application Deployment 3 & Database Migration)                                            │

│  • Application stops writing to `old\_status`.                                                                 │

│  • Safely drop `old\_status` column from the database asynchronously.                                          │

│                                                                                                               │

└───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 3. Safe DDL Rules in PostgreSQL

#### Rule 1: Always Set a Strict `lock_timeout`

Never allow a migration script to wait indefinitely for a lock:

SET lock\_timeout \= '2s';

-- If the lock cannot be acquired within 2 seconds, fail immediately without queueing traffic!

ALTER TABLE users ADD COLUMN phone VARCHAR(20);

#### Rule 2: Non-Blocking Index Creation

Never run plain `CREATE INDEX`. It acquires a `SHARE` lock blocking all table writes:

-- Safe: Builds index in the background without blocking concurrent INSERT/UPDATE/DELETE

CREATE INDEX CONCURRENTLY idx\_users\_email ON users(email);

#### Rule 3: Adding NOT NULL Columns Safely

In PostgreSQL 11+, adding a column with a constant `DEFAULT` does not rewrite the table:

-- Safe in PG 11+ (Metadata update only, instant):

ALTER TABLE orders ADD COLUMN is\_active BOOLEAN NOT NULL DEFAULT true;

-- For complex constraints, add as NOT VALID, then validate separately:

ALTER TABLE orders ADD CONSTRAINT check\_amount\_positive CHECK (amount > 0\) NOT VALID;

-- Validates concurrently without blocking writes:

ALTER TABLE orders VALIDATE CONSTRAINT check\_amount\_positive;

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### PostgreSQL Migration Safety Matrix:

| Operation | Naive Approach (Downtime Risk) | Zero-Downtime Recipe |
| :---- | :---- | :---- |
| **Add Index** | `CREATE INDEX ...` (Blocks writes) | `CREATE INDEX CONCURRENTLY ...` |
| **Drop Index** | `DROP INDEX ...` (Blocks queries) | `DROP INDEX CONCURRENTLY ...` |
| **Add Column** | `ALTER TABLE tbl ADD col ...` | Always set `lock_timeout = '2s';` first |
| **Rename Column** | `ALTER TABLE tbl RENAME COLUMN ...` | **Expand-Contract Pattern** across 3 deployments |
| **Change Type** | `ALTER TABLE tbl ALTER COLUMN col TYPE ...` | Add new column $\\rightarrow$ Dual-write $\\rightarrow$ Backfill $\\rightarrow$ Drop old |
| **Add Foreign Key** | `ADD CONSTRAINT fk REFERENCES ...` | `ADD CONSTRAINT ... NOT VALID;` $\\rightarrow$ `VALIDATE CONSTRAINT` |

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Zero-Downtime Migration of a 500M-Row Ledger Table

Design an end-to-end migration strategy to split a 500-million row monolithic `transactions` table into a normalized ledger structure (`transactions` and `transaction_entries`) receiving 15,000 writes/sec:

**Requirements**:

1. **Zero Data Loss & Zero Downtime**:
   - The application must maintain 99.999% availability with zero query timeouts.
2. **Dual-Writing & CDC Replication**:
   - Specify whether to use application-level dual writing or database triggers / Debezium CDC for stream replication.
3. **Throttled Backfilling with Replica Protection**:
   - Design a backfill strategy that monitors PostgreSQL streaming replication lag and throttles backfill throughput if replica lag exceeds 2 seconds.

---

### Problem 2: Idempotent Chunked Database Backfill Worker in TypeScript

Build a production-grade **Idempotent Chunked Backfill Worker** in TypeScript using Prisma or Kysely:

**Requirements**:

1. **Keyset Pagination (Seek Method)**:
   - Must use keyset pagination (`WHERE id > :last_seen_id ORDER BY id ASC LIMIT :chunk_size`) rather than `OFFSET / LIMIT` to prevent $O(N)$ query degradation on massive tables.
2. **Adaptive Throttling & Sleep**:
   - Dynamically sleeps between chunks (e.g. 50ms - 200ms) to allow concurrent OLTP transactions to clear the database buffer pool.
3. **Crash Recovery & Checkpointing**:
   - Stores progress checkpoint (`last_processed_id`, `rows_updated`, `error_count`) in a Redis key or persistent metadata table so the worker can resume instantly after restarts.

