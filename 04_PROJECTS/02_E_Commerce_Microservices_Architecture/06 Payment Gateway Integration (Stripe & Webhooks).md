---
tags:
  - architecture
  - microservices
  - stripe
  - payments
  - webhooks
  - asynchronous
  - ngrok
---

## 🧠 Core Concept: The Zero-Trust Payment Flow

In a poorly designed app, the Next.js frontend sends a request like: `POST /pay { amount: 5000 }`. A malicious user can easily intercept this network request, change `5000` to `1`, and buy a $50 item for 1 cent.

**The Microservice Payment Flow:**

1. Next.js sends _only_ the Product IDs and Quantities to the Payment Service.
2. The Payment Service queries the Product Database to get the _true_ prices.
3. The Payment Service creates a secure **Stripe Checkout Session** and returns a URL.
4. The user leaves your site, pays securely on Stripe's servers, and is redirected back.
5. Stripe sends a background **Webhook** to your server confirming the payment actually succeeded.

---

## ⚡ 1. The Hono Framework (Payment Service)

For the Payment Service, the architecture introduces **Hono**, a lightweight, ultrafast web framework (similar to Express but designed for Edge computing and serverless environments).

It is used here because webhook receivers need to be incredibly fast and often run on edge networks (like Cloudflare Workers or Vercel Edge).

TypeScript

```ts
// apps/payment-services/src/index.ts
import { Hono } from "hono";
import { serve } from "@hono/node-server";
import Stripe from "stripe";

const app = new Hono();
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

// Health check
app.get("/", (c) => c.text("Payment Service is running"));

serve({ fetch: app.fetch, port: 8002 });
```

---

## 🛒 2. Creating the Checkout Session

When the user clicks "Checkout", we build a Stripe Session. Notice how we construct the `line_items` array using server-verified data.

TypeScript

```ts
// apps/payment-services/src/routes/checkout.ts
app.post("/create-checkout-session", async (c) => {
    const { products, orderId } = await c.req.json();

    // 1. Build the Stripe line items format
    const lineItems = products.map((item: any) => ({
        price_data: {
            currency: "usd",
            product_data: { name: item.name },
            unit_amount: item.price, // MUST BE IN CENTS!
        },
        quantity: item.quantity,
    }));

    // 2. Create the session
    const session = await stripe.checkout.sessions.create({
        payment_method_types: ["card"],
        line_items: lineItems,
        mode: "payment",
        success_url: `${process.env.CLIENT_URL}/success?session_id={CHECKOUT_SESSION_ID}`,
        cancel_url: `${process.env.CLIENT_URL}/cart`,
        // 3. CRITICAL: Attach your internal Order ID so the webhook knows what to update later
        metadata: {
            orderId: orderId 
        }
    });

    // Return the Stripe URL to the frontend for redirection
    return c.json({ url: session.url });
});
```

---

## 🪝 3. Listening to Stripe Webhooks

When a user pays, Stripe needs to tell your server. However, Stripe cannot send an HTTP POST request to `http://localhost:8002` because your laptop is not on the public internet.

**The Solution: Ngrok** During development, you run `ngrok http 8002` in your terminal. Ngrok creates a secure, public URL (e.g., `https://abc-123.ngrok-free.app`) that tunnels directly to your local Fastify/Hono server. You paste this URL into your Stripe Dashboard.

### The Webhook Receiver

Stripe signs its webhooks cryptographically. Your server must verify this signature to ensure a hacker isn't just sending fake "payment successful" requests.

TypeScript

```ts
// apps/payment-services/src/routes/webhook.ts
import { producer } from "@repo/event-bus";

app.post("/webhook", async (c) => {
    const sig = c.req.header("stripe-signature");
    const rawBody = await c.req.text(); // Stripe requires the RAW body for verification

    let event;
    try {
        // Verify the signature using your Stripe Webhook Secret
        event = stripe.webhooks.constructEvent(rawBody, sig!, process.env.STRIPE_WEBHOOK_SECRET!);
    } catch (err) {
        return c.text(`Webhook Error: ${err.message}`, 400);
    }

    // Handle the specific event we care about
    if (event.type === "checkout.session.completed") {
        const session = event.data.object;
        const orderId = session.metadata?.orderId;

        console.log(`[Stripe] Payment success for Order: ${orderId}`);

        // THE SAGA CONTINUES: Tell Kafka the payment succeeded!
        await producer.send({
            topic: "payment-successful",
            messages: [{ value: JSON.stringify({ orderId, status: "paid" }) }]
        });
    }

    return c.json({ received: true });
});
```

## 🔄 Architectural Workflow (The Saga Pattern)

This completes what is known in microservices as a **Saga**:

1. User clicks "Buy" -> **Order Service** creates an Order (`status: pending`).
2. **Order Service** calls **Payment Service** to generate a Stripe URL.
3. User pays on Stripe.
4. Stripe hits the **Payment Service Webhook**.
5. **Payment Service** fires a Kafka event: `payment-successful`.
6. **Order Service** consumes the event and updates MongoDB (`status: success`).