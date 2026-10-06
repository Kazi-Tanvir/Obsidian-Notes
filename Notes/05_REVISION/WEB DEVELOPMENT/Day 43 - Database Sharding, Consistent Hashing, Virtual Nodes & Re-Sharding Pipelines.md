---
tags:
  - database
  - sharding
  - consistent-hashing
  - distributed-systems
  - system-design
  - backend
  - scalability
  - postgresql
date: 2026-09-12
---

# Day 43 - Database Sharding, Consistent Hashing, Virtual Nodes & Re-Sharding Pipelines

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Breaking the Single-Primary Bottleneck: Why Shard?

While read replicas and declarative table partitioning (Day 30) scale read queries and improve local index efficiency, all write operations (INSERT, UPDATE, DELETE) still terminate on a single primary database node.

When write throughput exceeds hardware limits (\$> 50,000\$ writes/second) or total database size exceeds multiple terabytes, the database must be **Horizontally Sharded**:

- Data is partitioned across \$N\$ completely independent physical database clusters (shards).

- Each shard owns a mutually exclusive subset of the total dataset.

- Sharding scales **both write capacity and storage capacity linearly**.

```text
┌────────────────────────────────────── Consistent Hashing Ring Topology ──────────────────────────────────────┐
│                                                                                                              │
│                                           Hash Ring: [0 to 2^32 - 1]                                         │
│                                                                                                              │
│                                           Shard A (Node A - vnode 1)                                         │
│                                                     (0)                                                      │
│                                                  ▲       ▲                                                   │
│                                           ┌──────┘       └──────┐                                            │
│                                           │                     │                                            │
│                                    Key "user_42"                │                                            │
│                                (Hashes to 400M)                 │                                            │
│                                           │                     │                                            │
│             Shard C (Node C - vnode 1) ───┤                     ├─── Shard B (Node B - vnode 1)              │
│                  (3,000,000,000)          │                     │            (1,000,000,000)                 │
│                                           │                     │                                            │
│                                           └──────┐       ┌──────┘                                            │
│                                                  ▼       ▼                                                   │
│                                           Shard A (Node A - vnode 2)                                         │
│                                                 (2,000,000,000)                                              │
│                                                                                                              │
│   Routing Rule: Hash the shard key (e.g. user_id). Walk clockwise along the ring.                             │
│                 The first encountered node (or virtual node) owns the data!                                  │
│                                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The Flaw of Modular Hashing vs. Consistent Hashing

#### The Modular Hashing Disaster:

The naive method routes keys using modulus: \$\$\\text{Shard ID} = \\text{hash}(\\text{key}) \\pmod N\$\$

- When \$N = 4\$, adding a 5th shard (\$N = 5\$) changes the result of \$\\text{hash}(\\text{key}) \\pmod N\$ for **over \$80%\$ of all existing keys**.

- Scaling or shrinking the database cluster forces a catastrophic migration of almost the entire database!

#### Consistent Hashing with Virtual Nodes (vnodes):

Consistent hashing maps both **cache/database nodes** and **keys** to a 32-bit circular ring (\$0\$ to \$2^{32}-1\$):

- **Minimal Rebalancing**: Adding or removing a node affects **only \$1/N\$** of the keys (the slice immediately preceding the modified node).

- **Virtual Nodes (vnodes)**: To prevent uneven data clustering (hot spots), each physical node is assigned multiple points on the ring (e.g. 100 to 256 virtual nodes per physical shard). This guarantees uniform statistical load distribution across all physical machines.

```typescript
import crypto from 'node:crypto';
export class ConsistentHashRing {
private ring: Map<number, string> = new Map();
private sortedKeys: number[] = [];
constructor(private virtualNodesPerShard: number = 150) {}
private hash(key: string): number {
return crypto.createHash('md5').update(key).digest().readUInt32BE(0);
}
addShard(shardId: string) {
for (let i = 0; i < this.virtualNodesPerShard; i++) {
const vnodeKey = this.hash(`\${shardId}#vnode_\${i}`);
this.ring.set(vnodeKey, shardId);
this.sortedKeys.push(vnodeKey);
}
this.sortedKeys.sort((a, b) => a - b);
}
getShard(key: string): string {
if (this.sortedKeys.length === 0) throw new Error('No shards available');
const hashVal = this.hash(key);
// Binary search for first node clockwise (>= hashVal)
let low = 0;
let high = this.sortedKeys.length - 1;
if (hashVal > this.sortedKeys[high]) {
// Wrap around ring to first node
return this.ring.get(this.sortedKeys[0])!;
}
while (low <= high) {
const mid = Math.floor((low + high) / 2);
if (this.sortedKeys[mid] >= hashVal) {
if (mid === 0 || this.sortedKeys[mid - 1] < hashVal) {
return this.ring.get(this.sortedKeys[mid])!;
}
high = mid - 1;
} else {
low = mid + 1;
}
}
return this.ring.get(this.sortedKeys[0])!;
}
}
### 3. Shard Key Selection & Cross-Shard Query Mitigation
Choosing the right shard key dictates system performance:
- **Good Shard Key**: High cardinality, uniform distribution, matches the primary query access path (e.g. tenant_id for B2B SaaS, user_id for consumer apps). All data for that tenant/user colocates on the same physical shard.
- **The Scatter-Gather Trap**: If a query does not include the shard key (e.g. SELECT * FROM orders WHERE status = 'PENDING'), the application must query **all \$N\$ shards in parallel**, aggregate results in memory, and sort. This eliminates the benefits of sharding.
## SECTION 2: DOCUMENTATION CHEAT SHEET
### Sharding Topologies Comparison Matrix:
------------------------------------------------------------------------------------------- **Strategy**          **Routing           **Scalability**   **Hot Spot     **Re-Sharding Mechanism**                           Risk**         Overhead** --------------------- ------------------- ----------------- -------------- ---------------- **Directory-Based**   Central lookup      Moderate          Central DB     Low (Update table                                 bottleneck     mapping rows)
**Range-Based**       ID ranges (1-10M,   Low               High (Recent   Complex 10M-20M)                              IDs get all writes)
**Modular Hash**      \$\\text{hash}(k)   High              Low            **Catastrophic \\pmod N\$                                           (\$>80%\$ data move)**
**Consistent          Virtual node        **Unlimited**     **Zero         **Minimal Hashing**             circular ring                         (Uniform       (\$1/N\$ data vnodes)**      move)** -------------------------------------------------------------------------------------------
## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS
### Problem 1: Global Sharded Social Platform Database Architecture
Design a horizontally sharded PostgreSQL database architecture for a social platform with 100M daily active users handling 150,000 writes/second:
**Requirements**:
1.  **Colocated Sharding Strategy**:
    - Select the optimal shard key (user_id).
    - Detail how posts, followers, and likes are structured so that 95% of user profile queries hit a single shard with zero cross-shard joins.
2.  **Global Scatter-Gather Aggregation Tier**:
    - For global queries (e.g. searching posts by hashtag #tech), design a dedicated query aggregator tier using Redis caching and an asynchronous fan-out worker pattern with bounded timeouts.
3.  **Zero-Downtime Re-Sharding Pipeline**:
    - Detail the 4-phase migration plan to expand a cluster from 8 shards to 16 shards using Change Data Capture (CDC via Debezium) and consistent hashing cutover.
### Problem 2: Dynamic Sharded Query Router in TypeScript
Build a production-ready **Sharded Database Router & Pool Manager** in TypeScript:
**Requirements**:
1.  **Consistent Hashing with Virtual Nodes**:
    - Manages a cluster of physical PostgreSQL connection pools using the ConsistentHashRing implementation above (default 150 vnodes/shard).
2.  **Routing Execution Decorator (executeOnShard)**:
    - Inspects the query context to extract the shard key (tenantId).
    - Resolves the target physical shard connection pool and executes the query locally.
3.  **Scatter-Gather Parallel Executor (executeScatterGather)**:
    - Executes cross-shard analytics queries across all physical shards concurrently using Promise.allSettled().
    - Merges and sorts individual shard result arrays in memory, applying global limit and offset.
```
