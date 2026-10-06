---
tags:
  - backend
  - distributed-systems
  - temporal
  - workflow-orchestration
  - durable-execution
  - microservices
  - sagas
  - architecture
date: 2026-09-17
---

# Day 48 - Distributed Workflow Orchestration, Temporal.io, Event-Driven Sagas & Durable Execution Engines

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Distributed Failure Dilemma & The Rise of Durable Execution

Modern backend architectures coordinate operations spanning dozens of independent microservices, payment gateways, and third-party APIs. In traditional stateless architectures (Node.js/Express, Lambdas, Celery queues), multi-step business transactions face unavoidable failure modes:

- **Process Crashes Mid-Transaction**: A container running a multi-step onboarding flow is terminated by Kubernetes for an OOM event or node auto-scaling. The local in-memory state is wiped.
- **Zombie / Lost State**: Developers attempt to track transaction state manually by updating a status column in a database (`PENDING_PAYMENT`, `PAYMENT_SUCCESS`, `SENDING_WELCOME_EMAIL`). Under high concurrency, race conditions, missed database updates, and deadlocks emerge.
- **Flaky Ad-hoc Retries**: If step 4 of 5 fails due to a network glitch, standard HTTP retries risk executing side-effects multiple times or requiring complex distributed lock orchestration.

#### The Durable Execution Paradigm (Temporal.io / Cadence)

Durable Execution guarantees that code execution will proceed to completion regardless of server crashes, process kills, network partitions, or database failovers. If a worker hosting your function is unceremoniously killed, another worker automatically reconstructs the exact call stack, variables, and execution state, seamlessly picking up at the exact line of code where the original worker halted!

```text
┌────────────────────────────────────── Temporal Execution Architecture ──────────────────────────────────────┐
│                                                                                                             │
│  Temporal Cluster (Control Plane)                                                                           │
│  ┌─────────────────────────┬─────────────────────────┬─────────────────────────────────────────────────┐   │
│  │ Frontend Service (gRPC) │ Matching Service (Queues│ History Service (Event Sourced Persistence Engine│   │
│  └─────────────────────────┴─────────────────────────┴─────────────────────────────────────────────────┘   │
│                                           │ (gRPC Long-Polling)                                             │
│                                           ▼                                                                 │
│  Application Workers (Your Node.js Microservices)                                                           │
│  ┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Workflow Sandbox: Must be 100% Deterministic!                                                         │  │
│  │ • Orchestrates flow, manages timers, handles Signals/Queries.                                         │  │
│  │ • NO Math.random(), NO Date.now(), NO direct fetch() or DB calls!                                     │  │
│  ├───────────────────────────────────────────────────────────────────────────────────────────────────────┤  │
│  │ Activity Workers: Unconstrained & Non-Deterministic!                                                  │  │
│  │ • Executes API requests, database queries, emails, Stripe transactions.                               │  │
│  │ • Configured with automated exponential backoff retry policies.                                       │  │
│  └───────────────────────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2. Event Sourcing Replay & The Strict Determinism Constraint

How does Temporal achieve durable execution without taking multi-gigabyte memory snapshots of running processes? It utilizes **Event History Replay**:

1. When a Workflow executes an Activity, Temporal records a `WorkflowTaskScheduled` and `ActivityTaskCompleted` event in its append-only History Store.
2. If a worker crashes and restarts, Temporal "replays" the Workflow function from the very beginning.
3. During replay, whenever the Workflow reaches an Activity call that was previously completed, Temporal intercepts the call, skips execution, and immediately returns the cached result from the history log!
4. Execution fast-forwards instantly until it reaches the point of failure.

#### The Cardinal Determinism Rules

Because replay re-runs your workflow code line-by-line, the code must produce the exact same sequence of commands on every run:

- ❌ **Forbidden**: `const id = crypto.randomUUID();` ➔ Replay generates a different ID, causing a non-deterministic history mismatch panic!
- ❌ **Forbidden**: `const timestamp = Date.now();` ➔ Replay gets a newer timestamp.
- ❌ **Forbidden**: `const res = await fetch('https://api.stripe.com/v1/charges');` ➔ Network results can change or fail on replay.
- ✅ **Temporal Pattern**: Call `workflow.uuid4()`, `workflow.now()`, or offload external I/O into an Activity.

```typescript
// workflows/order-fulfillment.workflow.ts
import { proxyActivities, sleep } from '@temporalio/workflow';
import type * as activities from '../activities/fulfillment.activities';

// Configure proxy activities with production retry policies
const { chargeCustomer, reserveInventory, dispatchWarehouse, releaseInventory } =
  proxyActivities<typeof activities>({
    startToCloseTimeout: '30 seconds',
    retry: {
      initialInterval: '1 second',
      backoffCoefficient: 2,
      maximumAttempts: 5,
      nonRetryableErrorTypes: ['InvalidCreditCardError'],
    },
  });

export async function processOrderWorkflow(orderId: string, amountCents: number): Promise<string> {
  // Step 1: Charge customer
  const paymentId = await chargeCustomer(orderId, amountCents);

  // Step 2: Reserve inventory with automated Saga rollback compensation
  let inventoryReserved = false;
  try {
    await reserveInventory(orderId);
    inventoryReserved = true;
  } catch (err) {
    // If inventory fails, execute compensation activity (Saga pattern)
    // Temporal guarantees compensation runs even if the worker crashed!
    throw new Error(`Inventory allocation failed: ${err.message}`);
  }

  // Step 3: Durable Timer - Wait 2 hours for fraud review without holding thread or DB connection!
  // Temporal puts workflow to sleep; zero CPU or RAM consumed in cluster!
  await sleep('2 hours');

  // Step 4: Dispatch to warehouse
  const trackingNumber = await dispatchWarehouse(orderId, paymentId);
  return trackingNumber;
}
```

---

### 3. Signals, Queries, and Updates: Human-in-the-Loop Orchestration

Real-world workflows are rarely linear; they require interacting with external actors over days or weeks (e.g. human manager approvals, customer address changes, order cancellations).

```text
┌────────────────────────────────────── Temporal Interactive Channels ──────────────────────────────────────┐
│                                                                                                            │
│  Signal (Async Mutation):                                                                                  │
│  • External service pushes an asynchronous event into a running workflow (e.g. "Customer clicked Cancel"). │
│  • Does not return a value to the caller; buffered into workflow history.                                  │
│                                                                                                            │
│  Query (Synchronous Read-Only Inspection):                                                                 │
│  • External dashboard inspects current workflow internal state (e.g. "What stage of fulfillment is this?").│
│  • Zero state mutations; executes instantly without recording history events.                              │
│                                                                                                            │
│  Update (Synchronous Mutation & Return):                                                                   │
│  • Mutates workflow state and immediately returns validated result to caller in a single round-trip.       │
│                                                                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### TypeScript Implementation of Signals & Queries

```typescript
import { defineSignal, defineQuery, setHandler, condition } from '@temporalio/workflow';

export const cancelOrderSignal = defineSignal<[reason: string]>('cancelOrder');
export const getOrderStatusQuery = defineQuery<string>('getOrderStatus');

export async function orderLifecycleWorkflow(orderId: string): Promise<string> {
  let status = 'AWAITING_PAYMENT';
  let isCancelled = false;
  let cancellationReason = '';

  // Register handlers
  setHandler(cancelOrderSignal, (reason) => {
    isCancelled = true;
    cancellationReason = reason;
  });

  setHandler(getOrderStatusQuery, () => status);

  // Await either payment completion OR cancellation signal within a 24-hour timeout window
  const receivedSignalOrTimeout = await condition(() => isCancelled, '24 hours');

  if (isCancelled) {
    status = 'CANCELLED';
    return `Order cancelled due to: ${cancellationReason}`;
  }

  status = 'PROCESSING';
  // Proceed with shipment...
  return 'Order fulfilled successfully';
}
```

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Temporal TypeScript SDK Architecture & APIs

| Component | Function / Interface | Description & Constraints |
| :--- | :--- | :--- |
| **Workflow** | `export async function myWorkflow()` | Orchestrator function. Must be 100% deterministic. No direct side effects. |
| **Activity** | `export async function myActivity()` | Execution unit. Performs non-deterministic work (HTTP, DB, FS, Stripe). |
| **Proxy** | `proxyActivities<T>(options)` | Creates a typed invocation proxy for activities with timeouts and retry options. |
| **Timer** | `sleep(duration: string \| number)` | Suspends workflow execution durably. Consumes zero CPU/RAM. |
| **Signal** | `defineSignal<Args>(name)` | Async push notification sent to a running workflow. |
| **Query** | `defineQuery<Ret>(name)` | Synchronous read of internal workflow state without modifying history. |
| **Condition** | `condition(() => boolean, timeout)` | Pauses workflow until a state predicate resolves true or timeout elapses. |

### Production Timeout & Retry Configuration

```typescript
const activities = proxyActivities<MyActivities>({
  // Maximum duration an activity can run from start to completion
  startToCloseTimeout: '1 minute',
  // Heartbeat timeout: Detects crashed activity workers quickly
  heartbeatTimeout: '10 seconds',
  retry: {
    initialInterval: '500ms',
    backoffCoefficient: 2.0,      // Exponential backoff
    maximumInterval: '30 seconds', // Cap retry delay
    maximumAttempts: 10,           // Give up after 10 attempts
    nonRetryableErrorTypes: ['ValidationError', 'UnauthorizedError'], // Skip retry for terminal errors
  }
});
```

### Essential Temporal CLI Commands

```bash
# Start local Temporal dev server with Web UI at http://localhost:8233
temporal server start-dev

# Trigger a workflow execution manually via CLI
temporal workflow start   --task-queue order-fulfillment-queue   --type processOrderWorkflow   --workflow-id order-ord-98765   --input '["ord-98765", 14999]'

# Send a Signal to a running workflow
temporal workflow signal   --workflow-id order-ord-98765   --name cancelOrder   --input '"Customer requested cancellation via UI"'

# Query the real-time state of a workflow
temporal workflow query   --workflow-id order-ord-98765   --name getOrderStatus
```

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Multi-Day E-Commerce Order Fulfillment & International Customs Engine

Design an enterprise-grade distributed workflow orchestration architecture for a cross-border retail enterprise (handling 10 million shipments annually):

- **Multi-Day Customs Clearance & Carrier Handshakes**:
  - The fulfillment cycle spans 5 to 14 days across multiple international freight carriers (air cargo, customs broker, local delivery).
  - The engine must handle carrier webhook status callbacks and manual customs inspection holds without consuming active thread resources.
- **Saga Orchestration & Partial Compensations**:
  - If customs rejects an item on Day 4, the workflow must execute targeted compensation actions: issue a partial customer refund (excluding export taxes), return local warehouse inventory, and file an automated carrier insurance claim.
- **High-Volume Worker Partitioning**:
  - Design task queue partitioning strategies to prevent heavy long-running customs workflows from starving high-priority sub-second payment workflows.

---

### Problem 2: Resilient SaaS Subscription Billing & Dunning Workflow in TypeScript

Implement a production-ready Subscription Billing & Dunning Workflow using the Temporal TypeScript SDK:

- **Monthly Recurring Execution with Grace Period**:
  - The workflow runs indefinitely for an active customer, executing once every 30 days (`sleep('30 days')`).
  - Each cycle calls `chargeSubscription(customerId, planId)`.
- **Intelligent Dunning Cycle upon Payment Failure**:
  - If `chargeSubscription` fails, the workflow enters a 7-day Dunning Mode:
    - Retries payment on Day 1, Day 3, and Day 7.
    - Sends reminder emails to the customer after each failure via `sendPaymentReminderEmail()`.
    - Exposes a `paymentMethodUpdated` Signal allowing customers to update their credit card mid-dunning, immediately re-triggering a payment attempt.
- **Workflow Query & Cancellation**:
  - Exposes a `getSubscriptionStatus` Query returning `{ status: 'ACTIVE' | 'DUNNING' | 'TERMINATED', retryCount: number, nextAttemptAt: string }`.
  - Listens for a `cancelSubscription` Signal. If received, immediately terminates billing and calls `downgradeAccountToFree(customerId)`.
