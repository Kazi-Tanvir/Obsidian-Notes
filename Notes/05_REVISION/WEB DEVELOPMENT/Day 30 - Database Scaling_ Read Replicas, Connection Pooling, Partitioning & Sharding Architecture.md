---
tags:
- database
- postgresql
- scaling
- connection-pooling
- sharding
- read-replicas
- backend
- system-design
date: 2026-08-30
---

# Day 30 - Database Scaling: Read Replicas, Connection Pooling, Partitioning & Sharding Architecture

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Database Scaling Bottlenecks & Evolution Hierarchy

As relational databases (PostgreSQL, MySQL) scale to tens of millions of records and thousands of queries per second, systems encounter three hard physical limits:

1.  **Connection Exhaustion**: Each PostgreSQL connection forks a dedicated OS backend process consuming 5--10 MB of RAM. 5,000 idle connections alone consume 25--50 GB of memory without executing queries.

2.  **Read vs. Write I/O Contention**: Write locks (EXCLUSIVE LOCK) block read operations, and massive reporting scans degrade transaction throughput.

3.  **Table Bloat & Index Degradation**: B-Tree indexes on single tables exceeding 100M+ rows no longer fit into RAM (shared_buffers), resulting in random disk seeks.

┌────────────────────────────────────── Database Scaling Evolution ──────────────────────────────────────┐

│ │

│ Phase 1: Connection Pooling (PgBouncer / RDS Proxy) ──► Reuses small connection pools (e.g. 50 conns) │

│ │

│ Phase 2: Read/Write Splitting ──► 1 Primary (Writes) + N Read Replicas (WAL Streaming Replication) │

│ │

│ Phase 3: Declarative Partitioning ──► Splits single huge table into Range/Hash partitions in 1 DB │

│ │

│ Phase 4: Horizontal Sharding ──► Distributes distinct rows across multiple independent physical DBs │

│ │

└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Connection Pooling Architecture (PgBouncer & AWS RDS Proxy)

Connection poolers act as a high-performance proxy layer that maintains a persistent pool of server connections while multiplexing thousands of incoming ephemeral client connections.

#### PgBouncer Pooling Modes:

- **Session Pooling (Least aggressive)**: Connection is leased to a client for the entire lifespan of the client session. Safest, but lowest concurrency gain.

- **Transaction Pooling (Recommended for Web APIs)**: Connection is leased only for the duration of a single BEGIN ... COMMIT transaction, then immediately released to the pool.

  - *Constraint*: Cannot use session-level state (e.g. SET timezone, LISTEN/NOTIFY, or un-named prepared statements in older drivers).

- **Statement Pooling (Most aggressive)**: Connection is leased for a single query.

  - *Constraint*: Multi-statement transactions (BEGIN...COMMIT) are prohibited.

### 3. Read/Write Splitting & Read-Your-Own-Writes Consistency

In an asynchronous replication topology, the Primary server writes changes to the **Write-Ahead Log (WAL)** and streams them to Read Replicas.

┌─────────────────┐ Writes (INSERT/UPDATE/DELETE) ┌────────────────────────┐

│ App Server / │ ────────────────────────────────────────► │ Primary PostgreSQL │

│ Prisma Client │ │ (Read/Write) │

└────────┬────────┘ └───────────┬────────────┘

│ │ WAL Streaming

│ Reads (SELECT) ▼ (Async Replication)

│ ──────────────────────────────────────────────────► ┌────────────────────────┐

│ │ Read Replica 1 & 2 │

│ │ (Read-Only) │

└─────────────────────────────────────────────────────┴────────────────────────┘

#### The Replication Lag Trap & Mitigation:

- **The Bug**: A user creates a post (INSERT), is immediately redirected to their profile (SELECT), but queries a lagging Read Replica where the record does not yet exist.

- **Mitigation (Sticky Session / Causal Consistency)**:

  1.  **Write Time Tracking**: When a user performs a write, record a timestamp cookie (e.g. last_write_at = Date.now()).

  2.  **Primary Routing Window**: Route all read queries for that user to the **Primary** database for the next 5 seconds (grace window), after which reads safely return to the Read Replicas.

```typescript
// Advanced Read/Write Router Implementation with Prisma Extension
import { PrismaClient } from '@prisma/client';
const primaryClient = new PrismaClient({ datasourceUrl: process.env.DATABASE_PRIMARY_URL });
const replicaClient = new PrismaClient({ datasourceUrl: process.env.DATABASE_REPLICA_URL });
export function getDatabaseClient(userLastWriteTimestamp?: number) {
const REPLICATION_LAG_TOLERANCE_MS = 3000; // 3-second grace window
if (userLastWriteTimestamp && Date.now() - userLastWriteTimestamp < REPLICATION_LAG_TOLERANCE_MS) {
// User recently wrote data -> Route to Primary to guarantee Read-Your-Own-Writes!
return primaryClient;
}
// Safe to read from replica
return replicaClient;
}
```

### 4. PostgreSQL Declarative Table Partitioning

Partitioning divides a large table into smaller physical child tables while maintaining a single logical table interface.

-- Create Logical Partitioned Table by Range (Time-Series Orders)

CREATE TABLE orders (

order_id UUID NOT NULL,

user_id UUID NOT NULL,

amount DECIMAL(10, 2) NOT NULL,

created_at TIMESTAMPTZ NOT NULL,

PRIMARY KEY (order_id, created_at) -- Partition key must be part of composite primary key

```javascript
) PARTITION BY RANGE (created_at);
```

-- Create Monthly Child Partitions

CREATE TABLE orders_2026_08 PARTITION OF orders

```javascript
FOR VALUES FROM ('2026-08-01 00:00:00+00') TO ('2026-09-01 00:00:00+00');
```

CREATE TABLE orders_2026_09 PARTITION OF orders

```javascript
FOR VALUES FROM ('2026-09-01 00:00:00+00') TO ('2026-10-01 00:00:00+00');
```

-- Partition Pruning in Action:

-- Query optimizer scans ONLY orders_2026_08 child table and skips all other partitions!

EXPLAIN ANALYZE

SELECT * FROM orders

```javascript
WHERE created_at >= '2026-08-15' AND created_at <= '2026-08-20';
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Database Scaling Strategies Comparison:

| **Technique** | **Solves** | **Architectural Complexity** | **Primary Trade-Off** |
| --- | --- | --- | --- |
| **Connection Pooling** | Connection exhaustion & RAM bloat | Low (Drop-in proxy) | No session-level state in transaction pooling |
| **Read Replicas** | High read query volume | Medium | Replication lag & eventual consistency |
| **Table Partitioning** | Giant table index bloat & slow VACUUM | Medium | Composite primary keys required on partition key |
| **Horizontal Sharding** | CPU/Disk/Write limits on single server | High | Cross-shard joins & distributed transactions |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: High-Scale IoT Fleet Telemetry Database Architecture

Design a high-scale PostgreSQL database architecture for an IoT telemetry fleet streaming 50,000 sensor readings per second:

**Requirements**:

1.  Detail the storage architecture:

    - **Declarative Partitioning Strategy**: Range partitioning by day/week combined with Hash sub-partitioning by device_id.

    - **Automated Partition Lifecycle**: Retention policies to compress and archive partitions older than 90 days into S3 Parquet cold storage.

    - **Connection Tier**: Sizing and tuning PgBouncer in transaction mode for 10,000 concurrent ingestion workers.

<!-- -->

1.  Formulate a failover and disaster recovery strategy: Automated Primary-to-Replica promotion with zero data loss using Patroni / AWS Aurora Global Database.

### Problem 2: End-to-End Dynamic Read/Write Database Router in TypeScript

Build an enterprise **Database Context Router with Read-Your-Own-Writes Consistency**:

**Requirements**:

1.  **Query Router (DatabaseRouter)**:

    - Manages a Primary connection pool and an array of Read Replica connection pools with round-robin load balancing.

    - Automatically inspects incoming SQL statements or ORM operations:

      - Routes INSERT, UPDATE, DELETE, BEGIN transactions to the Primary.

      - Routes standalone SELECT queries to Read Replicas.

2.  **Session Consistency Guard (ReadYourOwnWritesGuard)**:

    - Accepts a context object { userId: string; lastWriteTimestamp?: number }.

    - If Date.now() - lastWriteTimestamp < 5000, forces SELECT queries to the Primary.

    - Emits an updated X-Last-Write-Timestamp header upon successful mutating transactions.

3.  Include test suites verifying:

    - Write operations correctly target Primary.

    - Normal reads load balance across Read Replicas.

    - Post-write read operations within the 5s window are pinned to Primary.
