---
tags:
  - backend
  - fintech
  - payments
  - stripe
  - webhooks
  - idempotency
  - architecture
  - system-design
date: 2026-09-09
---

# Day 40 - Payment Systems, Stripe API Internals, Webhook Idempotency & Reconciliation

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Modern Payment Architecture & Stripe PaymentIntents Lifecycle

Processing real-world payments is an asynchronous, state-machine driven process governed by global banking regulations (PCI-DSS compliance, European PSD2 Strong Customer Authentication - SCA / 3D Secure).

The **Stripe PaymentIntents API** represents the canonical transaction state machine:

1.  requires_payment_method: Client initiates intent; customer provides credit card or payment wallet token.

2.  requires_confirmation: Payment details verified on server; server instructs Stripe to process transaction.

3.  requires_action: Triggered when customer's issuing bank demands biometric or SMS 3D Secure challenge authentication.

4.  processing: Asynchronous payment rails (ACH, SEPA, Boleto) clear funds over 1 to 3 days.

5.  succeeded: Terminal success state; funds captured and ready for product provisioning.

```text
┌────────────────────────────────────── Payment & Webhook Architecture ──────────────────────────────────────┐
│                                                                                                             │
│  Client (Browser/App)           Your Backend (Node.js/Next)                    Stripe Engine                │
│        │                                     │                                       │                      │
│        │── 1. Create Checkout Session ──────►│                                       │                      │
│        │                                     │── 2. Create PaymentIntent ───────────►│                      │
│        │                                     │◄─ 3. Returns Client Secret ───────────│                      │
│        │◄─ 4. Passes Client Secret ──────────│                                       │                      │
│        │                                                                             │                      │
│        │── 5. Submits Card Data Directly to Stripe (PCI Compliant!) ────────────────►│                      │
│        │                                                                             │                      │
│        │   (Never trust client redirect! Asynchronous webhook is source of truth)    │                      │
│        │                                     │                                       │                      │
│        │                                     │◄─ 6. Webhook Event: payment_intent.succeeded ─────────────── │
│        │                                     │      (Cryptographic HMAC signature!)  │                      │
│        │                                     ├───────────────────────────────┐       │                      │
│        │                                     │ Check Idempotency Key in DB   │       │                      │
│        │                                     │ In Double-Entry Ledger        │       │                      │
│        │                                     │ Provision Product Order       │       │                      │
│        │                                     └───────────────────────────────┘       │                      │
│        │                                     │── 7. HTTP 200 OK Ack ────────────────►│                      │
│                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Webhook Delivery Realities & Cryptographic Verification

Webhooks are distributed messages transmitted over the public internet:

1.  **At-Least-Once Delivery**: Network partitions cause Stripe to retry events up to 72 hours. Your server **will** receive duplicate events.

2.  **Out-of-Order Delivery**: A charge.refunded webhook can arrive *before* the payment_intent.succeeded webhook!

3.  **Cryptographic Signature Verification**:

    - Every webhook payload is signed with an HMAC-SHA256 signature passed in the Stripe-Signature header: t=1614555000,v1=5257a869e7ecebeef\...

    - Prevents Man-in-the-Middle spoofing and replay attacks by validating timestamp tolerance (default \$\\le 300\\text{s}\$).

```typescript
import Stripe from 'stripe';
import { Request, Response } from 'express';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export async function stripeWebhookHandler(req: Request, res: Response) {
  const sig = req.headers['stripe-signature'] as string;
  const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET!;
  let event: Stripe.Event;

  try {
    // CRITICAL: Must use the RAW unparsed Buffer, not parsed JSON!
    event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  } catch (err: any) {
    console.error('[Security Violation]: Webhook signature verification failed:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  // Pass to idempotent event processor
  await processWebhookEventIdempotently(event);
  return res.status(200).json({ received: true });
}
```

### 3. Webhook Idempotency & The Double-Entry Ledger Pattern

To guarantee that duplicate webhook deliveries never cause double-crediting or duplicate shipments, architects employ two core fintech patterns:

#### 1. Idempotency Key Deduplication Table:

```sql
CREATE TABLE processed_webhook_events (
  id VARCHAR(255) PRIMARY KEY, -- Stripe event.id (e.g. evt_1N2...)
  event_type VARCHAR(100) NOT NULL,
  processed_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### 2. Dual-Entry Financial Ledger:

Money is never represented as a single mutable balance column. Every monetary transaction is recorded as immutable balanced Debit and Credit line items: \$\$\\sum \\text{Debits} = \\sum \\text{Credits}\$\$

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Stripe Webhook Events & Handling Priorities:

------------------------------------------------------------------------------- **Event Name**                  **Trigger Context**     **Primary Application Action** ------------------------------- ----------------------- ----------------------- payment_intent.succeeded        Single charge           Provision digital successful              access, trigger invoice generation

payment_intent.payment_failed   Card declined / expired Notify user, prompt payment method update

invoice.payment_succeeded       Recurring subscription  Extend subscription billed                  billing period (current_period_end)

invoice.payment_failed          Recurring subscription  Trigger automated failed                  dunning email, grace period countdown

customer.subscription.deleted   Subscription cancelled  Revoke access at period end

charge.refunded                 Funds returned to       Reverse ledger balance, customer                revoke user entitlements -------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Subscription Billing & Dunning Platform

Architect an Enterprise Global Subscription & Recurring Billing Platform for 1,000,000 active subscribers:

**Requirements**:

1.  **SCA 3DS Payment Recovery**:

    - When recurring subscription charges require customer 3D Secure bank authentication, dynamically generate an SCA recovery session link and trigger an urgent automated notification sequence.

2.  **Smart Dunning & Grace Periods**:

    - Implement exponential retry scheduling for soft card declines (insufficient funds) over 14 days before downgrading account status.

3.  **Audit Ledger & Reconciliation**:

    - Reconcile Stripe balance transaction export files (balance_transaction.created) with internal database ledger records to detect currency exchange discrepancies and chargeback fees.

### Problem 2: Production-Grade Stripe Webhook Processor in TypeScript

Build an Enterprise **Stripe Webhook Processing Service** in TypeScript with Prisma and Redis:

**Requirements**:

1.  **Raw Body Cryptographic Verification**:

    - Verifies incoming HMAC-SHA256 signature using stripe.webhooks.constructEvent() with strict 5-minute timestamp tolerance.

2.  **Distributed Lock & Idempotent Database Transaction**:

    - Acquires a Redis lock on event.id to prevent concurrent processing race conditions.

    - Executes an atomic PostgreSQL database transaction that inserts event.id into processed_webhook_events, updates the order status to PAID, and logs immutable ledger credit/debit rows.

3.  **Dead-Letter Queue (DLQ) & Graceful Error Recovery**:

    - If downstream database calls fail, returns HTTP 500 so Stripe re-delivers the event.

    - If an unrecoverable business error occurs, routes event metadata to a Dead-Letter Queue for administrator inspection without crashing the webhook listener.
