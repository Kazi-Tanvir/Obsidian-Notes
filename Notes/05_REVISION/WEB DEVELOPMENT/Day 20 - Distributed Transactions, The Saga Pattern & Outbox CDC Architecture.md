tags:

- backend

- microservices

- distributed-systems

- saga-pattern

- kafka

- system-design

- database date: 2026-08-20

# Day 20 - Distributed Transactions, The Saga Pattern & Outbox CDC Architecture

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Dual-Write Problem & The Failure of 2-Phase Commit (2PC)

In distributed microservices, a single business workflow often spans multiple independent databases (e.g., Order DB, Payment DB, Inventory DB).

- **The Dual-Write Problem**: Updating a local database and publishing a message to a broker (Kafka/RabbitMQ) in one API call cannot be atomically bound. If the process crashes between the DB commit and the message publish, the system enters an inconsistent state.

- **Why 2PC Fails in Cloud Microservices**: Two-Phase Commit (2PC) relies on distributed locking across coordinators and participants. Network partitions (CAP theorem) cause database connections to hang indefinitely, degrading system availability and throughput.

### 2. The Saga Pattern: Choreography vs. Orchestration

A **Saga** is a sequence of local transactions where each transaction updates data within a single service and publishes an event to trigger the next step. If a step fails, the Saga executes **Compensating Transactions** to undo preceding changes in reverse order.

\[ Happy Path \]:

CreateOrder ──► AuthorizePayment ──► ReserveInventory ──► ShipOrder ──► (Completed)

\[ Failure at Inventory \]:

CreateOrder ──► AuthorizePayment ──► ReserveInventory (FAIL!)

│ │

▼ ▼

RefundPayment ◄───────────────┘

│

▼

CancelOrder

#### Comparison: Choreography vs. Orchestration:

  -------------------------------------------------------------------------------------------------------------------------------------
  **Characteristic**      **Choreography (Event-Driven)**                   **Orchestration (State Machine)**
  ----------------------- ------------------------------------------------- -----------------------------------------------------------
  **Coordination**        Decentralized; services react to domain events    Centralized Saga Orchestrator engine

  **Coupling**            Loosely coupled                                   Orchestrator knows all participating steps

  **Complexity**          Difficult to visualize full workflow trajectory   Clear visibility into execution state and retries

  **Best For**            Simple workflows (2--3 steps)                     Complex enterprise workflows (5+ steps, banking, booking)
  -------------------------------------------------------------------------------------------------------------------------------------

### 3. Transactional Outbox Pattern + Change Data Capture (CDC)

To guarantee that database mutations and event publications occur with \$100%\$ atomicity without distributed locks, we use the **Transactional Outbox Pattern**:

┌──────────────────────────────────────────────┐

│ Service Application │

│ │

│ BEGIN TRANSACTION; │

│ INSERT INTO orders (\...); │

│ INSERT INTO outbox_table (event_payload); │

│ COMMIT; │

└──────────────────────┬───────────────────────┘

│

▼ (PostgreSQL Write-Ahead Log - WAL)

┌──────────────────────────────────────────────┐

│ Debezium CDC / Kafka Connect Engine │

└──────────────────────┬───────────────────────┘

│

▼ (Guaranteed At-Least-Once Delivery)

┌──────────────────────────────────────────────┐

│ Apache Kafka Topic (\'order-events\') │

└──────────────────────────────────────────────┘

1.  Order mutation and event envelope are committed inside the **same local ACID database transaction**.

2.  A Change Data Capture (CDC) tool (e.g. **Debezium**) reads the PostgreSQL WAL (Write-Ahead Log) and pushes events to Apache Kafka without touching application logic.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Outbox Table DDL (PostgreSQL):

CREATE TABLE outbox_events (

id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

aggregate_type VARCHAR(64) NOT NULL,

aggregate_id VARCHAR(64) NOT NULL,

event_type VARCHAR(64) NOT NULL,

payload JSONB NOT NULL,

created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),

processed BOOLEAN DEFAULT FALSE

);

CREATE INDEX idx_outbox_unprocessed ON outbox_events(created_at) WHERE processed = FALSE;

### Saga Orchestrator State Interface:

export enum SagaStatus {

STARTED = \"STARTED\",

COMPENSATING = \"COMPENSATING\",

COMPLETED = \"COMPLETED\",

FAILED = \"FAILED\"

}

export interface SagaStep\<TContext\> {

name: string;

execute: (context: TContext) =\> Promise\<void\>;

compensate: (context: TContext) =\> Promise\<void\>;

}

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Global Travel Booking Saga Architecture)

Design a multi-service travel booking platform (Flights, Hotels, Car Rentals) orchestrating bookings with third-party APIs.

**Requirements**:

1.  Choose between an Orchestrated Saga (using Temporal/Custom Node.js State Machine) vs Choreographed Kafka events, justifying your choice for handling third-party API downtime.

2.  Detail the compensation sequence if Flight Booking succeeds, Hotel Booking succeeds, but Car Rental fails due to credit card authorization limits.

3.  Design the Idempotency Strategy ensuring that compensating requests (e.g. POST /api/v1/hotels/cancel) are safely retried without double-cancelling.

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **Saga Orchestrator Engine** in TypeScript:

**Requirements**:

1.  Implement a generic SagaOrchestrator\<TContext\> class that accepts an array of SagaStep\<TContext\>.

2.  The orchestrator must execute steps sequentially in forward order.

3.  If any step throws an error:

    - Catch the failure and immediately transition to COMPENSATING mode.

    - Execute the corresponding compensate() functions in **reverse order** for all previously completed steps.

    - Record and log step execution duration and compensation errors.

4.  Include mock test cases verifying:

    - Full successful execution trajectory.

    - Mid-pipeline failure at Step 3 triggering rollbacks of Step 2 and Step 1.
