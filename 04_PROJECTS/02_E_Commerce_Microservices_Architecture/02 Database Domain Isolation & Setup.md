---
tags:
  - architecture
  - microservices
  - database
  - polyglot-persistence
  - prisma
  - mongoose
---

## 🧠 Core Concept: Polyglot Persistence

In a monolithic application, every feature shares a single giant database. If the database crashes, the entire application dies.

In microservices, we follow the "Database-per-Service" pattern. Every service owns its data and chooses the specific type of database that best fits its unique needs (Polyglot Persistence). They never query each other's databases directly.

**The Enterprise Benefit:**

- **Decoupling:** If the Product database goes offline, the Order service can still function independently.
- **Optimization:** You can use SQL for strict relational data and NoSQL for flexible, nested data.
---

## 🐘 1. The Product Service (PostgreSQL + Prisma)

The Product catalog requires strict rules. A product _must_ have a price, it _must_ belong to a category, and those relationships need to be enforced at the database level to prevent bad data. Therefore, we use **PostgreSQL** (Relational SQL) paired with **Prisma ORM**.

### The Shared `product-db` Package

Instead of burying the database connection inside the Express app, it is extracted into `packages/product-db`.

**The Prisma Client Singleton (Best Practice):** In development, Next.js or Node hot-reloads frequently. If we aren't careful, every save creates a new database connection until Postgres crashes with a "Too many connections" error. We solve this by caching the connection on the `globalThis` object.

TypeScript

```ts
// packages/product-db/src/index.ts
import { PrismaClient } from "../generated/prisma";

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };

// Reuse existing connection, or create a new one
export const prisma = globalForPrisma.prisma || new PrismaClient();

if (process.env.NODE_ENV !== "production") {
  globalForPrisma.prisma = prisma;
}

export * from "../generated/prisma"; 
export default prisma;
```

---

## 🍃 2. The Order Service (MongoDB + Mongoose)

Orders are fundamentally different from products. An order is a **historical snapshot** in time.

- If a user buys a $50 shirt today, and the admin changes the price to $60 tomorrow, the historical order receipt _must still say $50_.
    

Because of this, relational databases can be tricky for orders. **MongoDB** (NoSQL) is perfect here. We can embed the exact state of the product directly into the order document.

### The Mongoose Schema Definition

The connection is extracted into `packages/order-db`. Notice how the product details are nested directly inside the order schema, permanently locking in the price at the time of purchase.

TypeScript

```ts
// packages/order-db/src/models/Order.ts
import mongoose, { InferSchemaType, model } from "mongoose";

const OrderSchema = new mongoose.Schema(
  {
    userId: { type: String, required: true },
    email: { type: String, required: true },
    amount: { type: Number, required: true },
    status: { type: String, required: true, enum: ["success", "failed"] },
    products: [
      {
        name: { type: String, required: true },
        quantity: { type: Number, required: true },
        price: { type: Number, required: true }, // The locked-in price snapshot
      },
    ],
  },
  { timestamps: true }
);

export type OrderSchemaType = InferSchemaType<typeof OrderSchema>;
export const Order = model<OrderSchemaType>("Order", OrderSchema);
```

### The Lazy Creation Paradigm

Unlike Prisma (which requires you to run `migrate dev` to build tables manually), MongoDB is "lazy." The `ecommerce-orders` database and the `orders` collection do not exist until the exact moment the server successfully runs `new Order(...).save()` for the very first time.