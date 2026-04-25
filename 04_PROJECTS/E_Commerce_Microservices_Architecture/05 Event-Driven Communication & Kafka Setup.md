---
tags:
  - architecture
  - microservices
  - kafka
  - event-bus
  - pubsub
  - asynchronous
---

## 🧠 Core Concept: Breaking Synchronous Chains

If the Order Service uses a standard `axios.post()` to tell the Product Service to reduce inventory, the two services are now **tightly coupled**.

- If the Product Service is down for maintenance, the HTTP request fails.
- If the request fails, the user's checkout crashes.
- _Result: One broken server takes down the entire application (Cascading Failure)._

**The Solution: A Message Broker (Kafka) via Pub/Sub** Instead of talking directly to each other, microservices communicate asynchronously through an **Event Bus**.

- The Order Service **Publishes** a message: _"An order was just created."_ (It doesn't care who listens, it just drops the message and finishes the user's checkout instantly).
- The Product Service **Subscribes** to that message. When it has free CPU cycles, it reads the message and updates its database. If the Product service is down, Kafka safely holds the message in a queue until the server comes back online.

---

## 🚌 1. The Shared Event Bus Package (`@repo/event-bus`)

Just like our database connections, the Kafka configuration is extracted into a shared Turborepo package so all microservices can use it seamlessly. We use **Upstash** (Serverless Kafka) to avoid the nightmare of hosting Kafka clusters locally.

TypeScript

```ts
// packages/event-bus/src/index.ts
import { Kafka } from "kafkajs";

// 1. Connect to the Upstash Serverless Cluster
export const kafka = new Kafka({
  clientId: "ecommerce-platform",
  brokers: [process.env.UPSTASH_KAFKA_BROKER as string],
  ssl: true,
  sasl: {
    mechanism: "scram-sha-256",
    username: process.env.UPSTASH_KAFKA_USERNAME as string,
    password: process.env.UPSTASH_KAFKA_PASSWORD as string,
  },
});

// 2. Export the Producer (For sending messages)
export const producer = kafka.producer();

// 3. Export a Consumer Factory (For listening to messages)
export const createConsumer = (groupId: string) => {
  return kafka.consumer({ groupId });
};
```

---

## 📤 2. The Producer: Emitting Events (Order Service)

When a user successfully creates an order, we want to broadcast that fact to the rest of the architecture.

Inside the Fastify Order controller, immediately after saving the order to MongoDB, we fire off a message to a specific **Topic** (e.g., `order-created`).

TypeScript

```ts
// apps/order-services/src/routes/order.ts
import { producer } from "@repo/event-bus";

app.post("/", async (request, reply) => {
    const newOrder = new Order(request.body);
    const savedOrder = await newOrder.save();
    
    // Broadcast the event to Kafka!
    await producer.send({
        topic: "order-created",
        messages: [
            {
                // We send the order data as a stringified JSON payload
                value: JSON.stringify({
                    orderId: savedOrder._id,
                    products: savedOrder.products
                })
            }
        ]
    });

    reply.code(201).send(savedOrder);
});
```

---

## 📥 3. The Consumer: Reacting to Events (Product Service)

The Product Service needs to listen for that `order-created` topic so it can adjust its inventory in the PostgreSQL database.

We set this listener up in the `index.ts` file of the Product Service so it starts running the moment the server boots up.

TypeScript

```ts
// apps/product-services/src/index.ts
import { createConsumer } from "@repo/event-bus";
import prisma from "@repo/product-db";

const runKafkaConsumer = async () => {
    // 1. Create a consumer tied to this specific microservice
    const consumer = createConsumer("product-service-group");
    await consumer.connect();

    // 2. Subscribe to the relevant topic
    await consumer.subscribe({ topic: "order-created", fromBeginning: false });

    // 3. Run a continuous loop listening for new messages
    await consumer.run({
        eachMessage: async ({ message }) => {
            if (!message.value) return;
            
            // Parse the incoming data
            const eventData = JSON.parse(message.value.toString());
            
            console.log(`[Kafka] Processing inventory for Order: ${eventData.orderId}`);

            // Update Prisma Database (Decrease Inventory)
            for (const item of eventData.products) {
                // In a real app, you would decrement stock here
                console.log(`Decreasing stock for ${item.name} by ${item.quantity}`);
            }
        }
    });
};

// Start the consumer loop alongside the Express server
runKafkaConsumer().catch(console.error);
```

## ⚠️ Architectural Tradeoff: Eventual Consistency

By using Kafka, we trade **Strong Consistency** for **High Availability**. When the user finishes checkout, the database isn't updated in that exact millisecond. There is a slight delay (milliseconds to seconds) before the Product Service reads the message and updates Postgres. This concept is called **Eventual Consistency**, and it is the backbone of modern scaling.