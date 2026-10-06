---
tags:
  - backend
  - architecture
  - webhooks
  - event-driven
  - security
  - microservices
  - redis
  - system-design
date: 2026-09-10
---

# Day 41 - Webhook Delivery Systems, Outbound Retry Engines & HMAC Event Broadcasting

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Challenge of Outbound Webhook Delivery

While consuming inbound webhooks requires idempotency and signature verification (Day 40), **building an outbound webhook infrastructure** (acting as the webhook provider like Stripe, GitHub, or Shopify) introduces complex distributed systems challenges:

1.  **Unreliable Consumer Endpoints**: Customers provide HTTP URLs hosted on fragile servers, serverless cold starts, or behind unconfigured firewalls.

2.  **Cascading Timeout & Backpressure**: A slow client taking 29 seconds to respond must never tie up your backend worker threads or database connection pools.

3.  **Internal Denial of Service (Self-Inflicted DoS)**: If 1,000 customers configure webhooks and an event triggers 500,000 webhook dispatches, naive synchronous delivery will crash your outbound networking infrastructure.

4.  **Guaranteed Delivery with Exponential Backoff**: Delivering messages reliably across network outages over a 72-hour period requires an asynchronous, durable event outbox and worker pipeline.

```text
┌────────────────────────────────────── Outbound Webhook Dispatch Topology ──────────────────────────────────────┐
│                                                                                                                 │
│   Primary Application Service (Orders / Billing)                                                                │
│        │                                                                                                        │
│        ▼ (Transactional Outbox)                                                                                 │
│   [ PostgreSQL: webhook_outbox Table ] ──► Atomic insert in same DB transaction as business logic               │
│        │                                                                                                        │
│        ▼ (Debezium CDC / Worker Poll)                                                                           │
│   [ Redis / BullMQ Job Queue ] ──────────► Partitioned by customer_id (Prevents noisy-neighbor lockups)       │
│        │                                                                                                        │
│        ▼                                                                                                        │
│   [ Webhook Worker Pool ]                                                                                       │
│        │                                                                                                        │
│        ├──► 1. Generates HMAC-SHA256 Signature (Timestamped)                                                    │
│        ├──► 2. Sets Strict 5-Second AbortController Timeout                                                     │
│        ├──► 3. Dispatches HTTP POST to Customer Endpoint ────────► Customer Server                              │
│        │                                                                                                        │
│        ├─► Success (2xx) ──► Mark DELIVERED in audit log                                                        │
│        └─► Failure (5xx / Timeout) ──► Reschedule with Exponential Backoff + Jitter                             │
│                                       (1m, 5m, 15m, 1h, 6h, 24h, 72h ──► Dead Letter Queue)                     │
│                                                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Cryptographic Timestamped Signatures: The Modern Standard

To prevent replay attacks and allow consumers to verify authentic origin, every outbound request must transmit:

- X-Webhook-Id: Unique event UUID.

- X-Webhook-Timestamp: Unix timestamp (seconds).

- X-Webhook-Signature: Hex-encoded HMAC-SHA256 signature calculated over \${timestamp}.\${raw_payload} using the customer's shared webhook secret:

```typescript
import crypto from 'node:crypto';

export function signWebhookPayload(payload: string, secret: string, timestamp: number): string {
  const signaturePayload = `${timestamp}.${payload}`;
  const hmac = crypto.createHmac('sha256', secret);
  hmac.update(signaturePayload);
  return `t=${timestamp},v1=${hmac.digest('hex')}`;
}
```

### 3. Circuit Breakers & Endpoint Auto-Disabling

A customer endpoint that persistently fails (e.g. returns 404, 502, or times out 100 consecutive times) wastes massive network resources:

- **Circuit Breaker Policy**: If an endpoint fails \$N\$ consecutive deliveries over 24 hours, the system automatically transitions the endpoint status to SUSPENDED.

- **Administrative Alerting**: Dispatches an email notification to the customer administrator with error logs and a one-click endpoint re-enable button after verifying endpoint health.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Outbound Webhook Delivery State Machine:

----------------------------------------------------------------------- **State**               **Transition            **Next Action** Condition** ----------------------- ----------------------- ----------------------- QUEUED                  Event inserted into     Assigned to worker queue

DELIVERING              Worker dispatches HTTP  Wait for response / POST                    timeout

DELIVERED               Customer returns HTTP   Complete job, log 2xx                     telemetry

RETRYING                Customer returns 4xx /  Calculate exponential 5xx / timeout           backoff delay

FAILED                  Reached max retry limit Route to **Dead Letter (72h)                   Queue (DLQ)**

SUSPENDED               100 consecutive         Auto-disable endpoint, failures                alert customer -----------------------------------------------------------------------

### Exponential Retry Backoff Cadence:

\$\$\\text{Delay}(attempt) = \\min(\\text{base} \\times 2^{attempt} + \\text{jitter}, \\text{max_delay})\$\$

- Attempt 1: Immediate

- Attempt 2: 1 minute

- Attempt 3: 5 minutes

- Attempt 4: 15 minutes

- Attempt 5: 1 hour

- Attempt 6: 6 hours

- Attempt 7: 24 hours

- Terminal: Dead-Letter Queue (DLQ)

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Enterprise Outbound Webhook Delivery Architecture

Architect an Enterprise Outbound Webhook Platform delivering 10,000,000 events/day across 15,000 customer endpoints:

**Requirements**:

1.  **Noisy-Neighbor Protection**:

    - Prevent a single high-volume customer (e.g. generating 2,000 events/sec) from starving other customers' webhook deliveries.

2.  **Private Network / SSRF Protection**:

    - Prevent customers from configuring internal/private IP addresses (127.0.0.1, 10.0.0.0/8, 169.254.169.254 AWS metadata) as their webhook destination.

3.  **Customer Self-Service Delivery Logs**:

    - Store 30 days of delivery attempts (request headers, response codes, response latency, payload preview) queryable via an API dashboard with sub-second response times.

### Problem 2: Resilient Webhook Dispatcher Service in TypeScript

Build a production-ready **Outbound Webhook Dispatcher Service** in TypeScript using BullMQ, Redis, and native fetch:

**Requirements**:

1.  **HMAC-SHA256 Signing & Metadata Headers**:

    - Generates compliant X-Webhook-Id, X-Webhook-Timestamp, and X-Webhook-Signature headers.

2.  **Strict AbortController Timeout**:

    - Enforces an immutable 5-second connection/read timeout per delivery attempt using AbortController.

3.  **Exponential Backoff & Audit Logging**:

    - Retries failed deliveries with exponential backoff and randomized jitter.

    - Logs every attempt with timestamp, HTTP status code, duration in milliseconds, and error traces into an audit store.
