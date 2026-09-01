---
tags:
- backend
- microservices
- system-design
- distributed-systems
- event-sourcing
- grpc
- websockets
- architecture
date: 2026-08-21
---

# Day 21 - Week 3 Review: Microservices, Distributed Systems, Event Sourcing & Real-Time Mesh

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Week 3 Distributed Systems Architecture Topology

Week 3 bridged advanced inter-service transport, distributed data patterns, and real-time client communication into an enterprise-grade microservice architecture:

┌─────────────────────────────────────────┐

│ Client Layer (Web, Mobile) │

└───────────┬─────────────────┬───────────┘

│ (HTTP/REST) │ (WebSockets / SSE)

▼ ▼

┌──────────────────┐ ┌───────────────────┐

│ API Gateway │ │ WebSocket Mesh │

│ (Rate Limiting, │ │ (Redis Pub/Sub │

│ Circuit Breakers)│ │ Multi-Node Hub) │

└───────────┬──────┘ └─────────┬─────────┘

│ │

┌─────────────────────┴───────────────────┴─────────────────────┐

│ (Internal High-Throughput gRPC / Protobuf over HTTP/2) │

▼ ▼

┌─────────────────────────┐ ┌─────────────────────────┐

│ Order Microservice │ │ Payment Microservice │

│ (Saga Orchestration) │ │ (Compensating Actions) │

└────────────┬────────────┘ └────────────┬────────────┘

│ │

▼ (Transactional Outbox + PostgreSQL WAL) ▼ (Outbox CDC)

┌─────────────────────────┐ ┌─────────────────────────┐

│ Debezium CDC Engine │ │ Debezium CDC Engine │

└────────────┬────────────┘ └────────────┬────────────┘

│ │

└─────────────────────────────┬─────────────────────────────────┘

▼ (At-Least-Once Delivery)

┌───────────────────────────┐

│ Apache Kafka Broker │

└─────────────┬─────────────┘

│

▼ (Async Projection Handlers)

┌───────────────────────────┐

│ CQRS Read Models (Redis, │

│ Elasticsearch, Postgres) │

└───────────────────────────┘

### 2. Core Architectural Principles Reviewed

#### 1. Inter-Service Communication (gRPC vs REST vs GraphQL)

- **gRPC / Protocol Buffers**: Compact binary packing over HTTP/2 multiplexed streams; ideal for high-throughput, low-latency microservice meshes with strict deadlining.

- **GraphQL & DataLoader**: Flexible client-driven data graphs with microtask batching and request-scoped memoization to eliminate $N+1$ database calls.

#### 2. Edge Ingress, Gateway Aggregation & Fault Tolerance

- **Distributed Rate Limiting**: Sliding Window Counter algorithms via Redis Lua scripts to prevent noisy-neighbor API abuse.

- **Circuit Breaker State Machine**: CLOSED -> OPEN (fail-fast fallback) -> HALF-OPEN (canary recovery testing) to halt cascading system failure.

#### 3. Real-Time Networking at Scale

- **WebSockets + Redis Pub/Sub**: Horizontal scaling of stateful TCP connections across multi-instance clusters.

- **Connection Health**: Dual-sided ping/pong heartbeats to aggressively prune zombie sockets.

#### 4. Event Sourcing & CQRS

- **Immutable Event Store**: Zero data loss, auditability, and temporal rehydration.

- **Read-Model Projections**: Asynchronous materialized views optimized for read queries without join contention.

#### 5. Distributed Transactions & The Saga Pattern

- **Sagas over 2PC**: Decentralized Choreography or Centralized Orchestration with compensating rollback transactions.

- **Transactional Outbox**: Combining local database mutations and outbox records in a single ACID commit, propagated via Debezium CDC.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Distributed Systems Patterns Comparison Matrix:

| **Pattern / Technology** | **Primary Use Case** | **Key Invariant / Guarantee** | **Fallback / Mitigation** |
| --- | --- | --- | --- |
| **gRPC / Protobuf** | Inter-service East-West communication | Strictly typed schema, binary performance | Deadlines / Timeouts on all RPCs |
| **DataLoader** | GraphQL nested field resolution | Batches $N$ queries into 1 SQL statement    R | quest-scoped lifecycle (no cross-user cache leak) |
| **Circuit Breaker** | Downstream dependency protection | Fails fast when error threshold exceeded | Returns cached data or degraded response |
| **Transactional Outbox** | Eliminating Dual-Write bug | Atomicity between DB state and Kafka event | Debezium CDC ensures at-least-once delivery |
| **Saga Orchestrator** | Multi-service business transactions | Backward compensating transaction rollbacks | Forward idempotent retries + Dead-Letter Queues |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Full-Scale System Design (Real-Time High-Frequency Trading Platform)

Design an enterprise-grade **Real-Time Financial Trading & Portfolio Execution Platform** capable of handling 200k orders/sec with sub-millisecond execution tracking.

**Requirements**:

1.  Detail the Edge Gateway layer with JWT validation, Sliding Window rate limiting, and Circuit Breakers.

2.  Design the internal Order Routing Mesh using gRPC Unary & Server-Streaming RPCs with deadline propagation.

3.  Design the Order Matching Ledger using **Event Sourcing** with a PostgreSQL Write-Ahead Log Event Store and Kafka event dissemination.

4.  Diagram the **CQRS Read Models** (Redis cluster for real-time user portfolios, TimescaleDB for candlestick charting).

5.  Explain the **WebSocket Broadcast Mesh** using Redis Pub/Sub to push real-time order fills to connected trader browsers.

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **Resilient Microservice Gateway & Outbox Dispatcher** in TypeScript:

**Requirements**:

1.  Implement a CircuitBreaker<T> class with configurable failure thresholds (e.g. 5 failures in 10s), timeout resets (5s), and state transitions (CLOSED, OPEN, HALF-OPEN).

2.  Build an API Gateway route handler that routes requests to a mock downstream gRPC microservice wrapped in the Circuit Breaker with a strict $200\text{ms}$ deadline timeout.

3.  If the downstream call succeeds:

    - Commit the order to a database transaction.

    - Insert an event into the outbox_events table in the **same transaction**.

4.  If the Circuit Breaker is OPEN or the downstream service times out:

    - Return a graceful degraded HTTP 503 Service Unavailable with a Retry-After: 5 header without crashing the Node.js event loop.

5.  Include automated unit and integration tests verifying all failure modes, timeouts, and outbox transaction atomicity.
