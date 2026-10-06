---
tags:
  - database
  - distributed-systems
  - replication
  - multi-region
  - raft
  - consensus
  - cockroachdb
  - system-design
  - architecture
date: 2026-09-16
---

# Day 47 - Database Replication Topologies, Multi-Region Architectures & CockroachDB / Spanner Consensus

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Multi-Region Latency & Consistency Dilemma

When web applications serve users across North America, Europe, and Asia, single-region databases introduce inescapable physical latency limits:

- **Speed of Light in Fiber**: Transmitting an electrical packet from London to Singapore and back takes \$\\approx 160\\text{ms}\$ of pure physical transit time, completely independent of software optimizations.

- If a user in Singapore attempts a write to a primary database in us-east-1, the single database round-trip incurs a minimum \$220\\text{ms}\$ delay.

- The **CAP Theorem** dictates that in the presence of a network partition between continents, a distributed database must choose between **Consistency** (reject writes) or **Availability** (accept writes and risk split-brain divergence).

```text
┌────────────────────────────────────── Multi-Region Database Topologies ──────────────────────────────────────┐
│                                                                                                              │
│  Topology A: Single-Primary with Cross-Region Read Replicas                                                  │
│  • US Primary (All Writes) ──► Asynchronously streams WAL to EU & APAC Read Replicas                         │
│  • Latency: Local reads (5ms), but cross-continental writes (250ms+). Risk: Stale reads due to repl lag.     │
│                                                                                                              │
│  Topology B: Multi-Primary (Active-Active Master) ⚠️                                                          │
│  • Both US and EU accept writes independently.                                                               │
│  • Fatal flaw: Write-write conflicts! Requires complex asynchronous conflict resolution (Last-Write-Wins      │
│    causes silent data loss; CRDTs are limited to commutative operations).                                    │
│                                                                                                              │
│  Topology C: Distributed SQL (Google Spanner / CockroachDB / YugabyteDB) 🚀                                  │
│  • Single logical ACID database spanning the globe.                                                          │
│  • Partitions data into contiguous ranges; each range is replicated via Raft Consensus across 3+ regions.   │
│  • Enforces Strict Serializable Transactions using Hybrid Logical Clocks (HLC) or GPS/Atomic TrueTime.      │
│                                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Distributed Consensus via Raft & Multi-Raft Partitioning

In Distributed SQL databases like **CockroachDB**, data is divided into 64MB chunks called **Ranges**. Instead of running a single global consensus cluster (which would bottleneck), CockroachDB uses **Multi-Raft**:

- Every 64MB Range runs its own independent 3-node or 5-node **Raft Consensus Group**.

- One node is elected the **Raft Leader / Leaseholder** for that range.

- Writes to that range require acknowledgment from a quorum (majority: 2 of 3 nodes).

```text
┌────────────────────────────────────── CockroachDB Range Locality ──────────────────────────────────────┐
│                                                                                                        │
│  Range 1 (US Customer Data)                                                                            │
│  • Leaseholder: US-East Node ──► Quorum achieved across US-East + US-Central (Sub-20ms writes! ⚡)     │
│                                                                                                        │
│  Range 2 (EU Customer Data)                                                                            │
│  • Leaseholder: EU-West Node ──► Quorum achieved across EU-West + EU-Central (Sub-15ms writes! ⚡)     │
│                                                                                                        │
│  Cross-Region Write (When User in EU transfers money to US):                                           │
│  • Two-Phase Commit (2PC) coordinated across Raft groups with atomic write intents.                    │
│                                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3. Table Locality Patterns: Regional by Row

CockroachDB allows developers to configure table locality directly via SQL DDL to ensure compliance with data sovereignty regulations (GDPR) and guarantee sub-20ms local latencies:

-- 1. Create a Multi-Region Database

CREATE DATABASE enterprise_fintech PRIMARY REGION "us-east"

REGIONS "us-west", "europe-west";

-- 2. Define Table with Automatic Geo-Partitioning

CREATE TABLE users (

id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

region crdb_region NOT NULL, -- Automatic region enum column

name TEXT NOT NULL,

email TEXT NOT NULL,

balance NUMERIC(12, 2) NOT NULL

) LOCALITY REGIONAL BY ROW;

-- When a user registers in Europe, CockroachDB automatically pins the row's Raft leaseholders

-- to EU data centers! German data never leaves European physical disks!

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Distributed Database Replication Comparison:

---------------------------------------------------------------------------- **Characteristic**   **Primary-Replica   **Active-Active   **Distributed SQL (Postgres)**        (Galera/BDR)**    (CockroachDB)** -------------------- ------------------- ----------------- ----------------- **Isolation Level**  Read Committed /    Read Committed /  **Strict Serializable        Snapshot          Serializable (Global)**

**Write              Single machine      Limited by        **Linearly Scalability**        limit               conflicts         horizontal**

**Multi-Region       High latency        Low latency, high **Fast local Writes**             (cross-ocean)       conflicts         quorum (by row)**

**Failover RPO /     RPO \$> 0\$ (Lag), RPO \$\\approx    **RPO = 0, RTO RTO**                RTO: Minutes        0\$, RTO: Seconds \$< 3\\text{s}\$ (Automatic)**

**Clocks**           NTP (Vulnerable to  NTP               **Hybrid Logical drift)                                Clocks (HLC)** ----------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global High-Availability Banking Ledger

Design a globally distributed core banking platform operating across US, Europe, and Asia serving 50 million accounts:

**Requirements**:

1.  **Zero Data Loss (RPO = 0) with Sub-Second Failover**:

    - The platform must tolerate the complete loss of an entire cloud region (e.g. AWS us-east-1 hurricane outage) without losing a single transaction.

2.  **Strict Serializability without Global Deadlocks**:

    - Prevent double-spending when a card is swiped in London while an automated ACH withdrawal executes in New York simultaneously.

3.  **Data Sovereignty Compliance (GDPR)**:

    - Enforce row-level data residency guarantees ensuring European citizen data is physically stored and backed up exclusively within EU borders.

### Problem 2: Multi-Region Causal Consistency Router in TypeScript

Build an Enterprise **Geo-Aware Multi-Region Database Router** in TypeScript:

**Requirements**:

1.  **Hybrid Logical Clock (HLC) Generator**:

    - Implements a Hybrid Logical Clock producing monotonic { physicalTime: number, logicalCounter: number } timestamps that prevent clock-drift causality violations.

2.  **Region-Aware Query Dispatcher**:

    - Inspects client request metadata (e.g. cf-ipcountry or X-Client-Region).

    - Routes localized reads and writes to regional read/write connection pools.

    - For global transactions requiring cross-region consensus, applies a distributed two-phase commit wrapper with bounded timeout rollbacks.
