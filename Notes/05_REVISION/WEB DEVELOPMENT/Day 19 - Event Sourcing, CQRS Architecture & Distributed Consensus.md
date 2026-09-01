---
tags:
- backend
- event-sourcing
- cqrs
- microservices
- architecture
- system-design
- database
date: 2026-08-19
---

# Day 19 - Event Sourcing, CQRS Architecture & Distributed Consensus

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Traditional CRUD vs. Event Sourcing Paradigm

In standard CRUD architectures, database records are modified destructively in-place with UPDATE and DELETE queries. Past states are lost unless stored in separate audit tables.

**Event Sourcing (ES)** models application state as an **immutable, append-only log of domain events**. The current state of any entity (an **Aggregate Root**) is derived at runtime by replaying all historical events from the beginning of time (or from the latest snapshot).

#### Benefits of Event Sourcing:

- **Flawless Audit Trail**: Complete historical ledger of every action and domain reason.

- **Time-Travel Debugging & Temporal Queries**: Reconstruct the exact system state as it existed at any historical timestamp.

- **Append-Only Performance**: High-throughput writes without row-level lock contention.

### 2. CQRS (Command Query Responsibility Segregation)

Event Sourcing pairs naturally with **CQRS**, separating the application into two distinct paths:

[ Client Request ]

│

├───► [ Command / Write Side ] ───► Invariant Validation ───► [ Append to EventStore ]

│ │

│ (Async / CDC Event Bus)

│ │

│ ▼

│ [ Read Model Projections ]

│ │

└───► [ Query / Read Side ] ◄──────────────────────────────────────────┘

1.  **Write Model (Command Side)**:

    - Validates business invariants and rules against the Aggregate.

    - Appends events to the **Event Store** (e.g., PostgreSQL table, EventStoreDB, Apache Kafka).

    - Optimistic concurrency control via expectedVersion checking.

2.  **Read Model (Query Side)**:

    - Asynchronous event handlers (Projections) consume events and update read-optimized materialized views (PostgreSQL tables, Redis caches, Elasticsearch indexes).

    - **Eventual Consistency**: Read replicas update asynchronously within milliseconds of write completion.

### 3. Aggregate Root Implementation & Snapshotting

To prevent slow startup times when an aggregate has thousands of events, a **Snapshot Strategy** persists the hydrated aggregate state every $N$ events (e.g. every 100 events). Rehydration then loads the snapshot and replays only subsequent delta events.

```typescript
// Aggregate State Hydration Pattern
export interface DomainEvent {
eventId: string;
aggregateId: string;
type: string;
payload: any;
version: number;
timestamp: string;
}
export class BankAccountAggregate {
public id: string = "";
public balance: number = 0;
public version: number = 0;
// Replays an event to mutate internal state without validation checks
```

public apply(event: DomainEvent): void {

```javascript
switch (event.type) {
case "AccountOpened":
this.id = event.aggregateId;
this.balance = event.payload.initialDeposit;
break;
case "MoneyDeposited":
this.balance += event.payload.amount;
break;
case "MoneyWithdrawn":
this.balance -= event.payload.amount;
break;
}
this.version = event.version;
}
// Business Invariant Command Validator
```

public withdraw(amount: number): DomainEvent {

```javascript
if (amount <= 0) throw new Error("Withdrawal amount must be positive");
if (this.balance < amount) throw new Error("Insufficient funds");
return {
```

eventId: crypto.randomUUID(),

aggregateId: this.id,

type: "MoneyWithdrawn",

payload: { amount },

version: this.version + 1,

timestamp: new Date().toISOString()

```javascript
};
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Canonical Event Envelope Schema:

```javascript
{
```

"eventId": "e81d4fae-7dec-11d0-a765-00a0c91e6bf6",

"aggregateId": "acc-9921",

"aggregateType": "BankAccount",

"eventType": "MoneyTransferred",

"version": 14,

"payload": {

"recipientId": "acc-1044",

"amount": 250.00,

"currency": "USD"

},

"metadata": {

"userId": "user-881",

"correlationId": "corr-4412",

"causationId": "cmd-1092"

},

"timestamp": "2026-08-19T15:30:00.000Z"

```javascript
}
```

### Event Store PostgreSQL Table Schema:

CREATE TABLE event_store (

event_id UUID PRIMARY KEY,

aggregate_id VARCHAR(64) NOT NULL,

aggregate_type VARCHAR(64) NOT NULL,

event_type VARCHAR(64) NOT NULL,

version INT NOT NULL,

payload JSONB NOT NULL,

metadata JSONB NOT NULL,

created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

UNIQUE (aggregate_id, version) -- Guarantees optimistic concurrency

```javascript
);
```

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Global Banking Ledger & Multi-Model CQRS Architecture)

Design an enterprise-grade Core Banking Transaction Ledger using Event Sourcing and CQRS supporting 10,000 TPS.

**Requirements**:

1.  Detail the Event Store architecture ensuring zero double-spends and atomic balance transfers between accounts.

2.  Design the asynchronous Change Data Capture (CDC) projection pipeline (using Debezium + Kafka) that updates two distinct Read Models:

    - Fast Customer Dashboard in Redis.

    - Full-text Search & Audit History in Elasticsearch.

3.  Define the Snapshotting policy and Disaster Recovery strategy for hydrating cold aggregates.

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **Event-Sourced E-Commerce Order Aggregate & Projection Service** in TypeScript.

**Requirements**:

1.  Implement the OrderAggregate with lifecycle commands:

    - CreateOrder(items)

    - ApplyDiscountCode(code, percent) (fails if order already cancelled or paid)

    - ConfirmPayment(transactionId)

    - CancelOrder(reason) (fails if order already shipped)

2.  Build an EventStore class backed by an in-memory or PostgreSQL database with optimistic locking (expectedVersion) that rejects concurrent writes with ConcurrencyConflictError.

3.  Implement an asynchronous OrderReadModelProjection that processes events and maintains an updated view of active orders.

4.  Include comprehensive unit tests verifying event replay state hydration, optimistic concurrency conflicts, and invalid invariant rejections.
