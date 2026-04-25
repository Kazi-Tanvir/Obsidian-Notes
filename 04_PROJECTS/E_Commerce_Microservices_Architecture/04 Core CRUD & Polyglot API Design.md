---
tags:
  - architecture
  - api
  - express
  - fastify
  - prisma
  - mongoose
  - crud
---

## 🧠 Core Concept: The Controller Layer

The Controller layer acts as the brain of an individual microservice. It is responsible for taking an incoming HTTP request, parsing the data, communicating with the database, and returning a formatted JSON response.

Because we are using a **Polyglot Architecture**, the syntax and methodology change depending on which service you are inside.

**The Enterprise Benefit:**

- **Framework Optimization:** Express is used for the Product service due to its massive ecosystem and mature middleware (like Clerk). Fastify is used for the Order service because it is heavily optimized for raw speed and throughput (ideal for high-volume checkout processes).
- **Centralized Error Handling:** Moving away from scattered `try/catch` blocks to a unified global error catcher prevents the server from silently crashing.

---

## 🏗️ 1. The Express + Prisma Pattern (Product Service)

In the Product service, we are dealing with a strict relational catalog. The most complex operation here is **Filtering and Sorting** (e.g., a user searching for "Sneakers under $100, sorted by newest").

### Handling Complex Queries

Instead of fetching all products and filtering them in JavaScript (which is slow and crashes servers), we pass the heavy lifting to the PostgreSQL database using Prisma's query builder.

TypeScript

```ts
// apps/product-services/src/controllers/product.controller.ts
import { Request, Response } from "express";
import prisma from "@repo/product-db";

export const getProducts = async (req: Request, res: Response) => {
  // 1. Extract query parameters from the URL (?category=sneakers&sort=asc)
  const { category, sort, minPrice, maxPrice } = req.query;

  // 2. Build a dynamic Prisma query object
  const query: any = {};
  
  if (category) query.categorySlug = category;
  if (minPrice || maxPrice) {
    query.price = {
      ...(minPrice && { gte: Number(minPrice) }), // Greater than or equal
      ...(maxPrice && { lte: Number(maxPrice) }), // Less than or equal
    };
  }

  // 3. Execute the query
  const products = await prisma.product.findMany({
    where: query,
    orderBy: {
      price: sort === "asc" ? "asc" : "desc", // Default to descending
    },
    include: {
      category: true // JOIN the category table automatically!
    }
  });

  res.status(200).json(products);
};
```

---

## ⚡ 2. The Fastify + Mongoose Pattern (Order Service)

Fastify operates differently than Express. It encapsulates routes inside plugins and has built-in asynchronous error handling.

When a user checks out, we need to save the Mongoose document. Because Fastify is built on modern Promises, the controller logic is incredibly sleek.

TypeScript

```ts
// apps/order-services/src/routes/order.ts
import { FastifyInstance } from "fastify";
import { Order } from "@repo/order-db";

// Fastify routes are wrapped in an exported async function
export default async function orderRoute(app: FastifyInstance) {
  
  app.post("/", async (request, reply) => {
    // 1. request.body is automatically parsed by Fastify
    const data = request.body;

    // 2. Create the snapshot in MongoDB
    const newOrder = new Order(data);
    const savedOrder = await newOrder.save();
    
    // 3. Fastify's reply.send() is much faster than Express res.json()
    reply.code(201).send(savedOrder);
  });

  app.get("/:userId", async (request, reply) => {
    // Fastify uses request.params with explicit generic typing
    const { userId } = request.params as { userId: string };
    
    // Mongoose query
    const orders = await Order.find({ userId }).sort({ createdAt: -1 });
    
    reply.send(orders);
  });
}
```

---

## 🧯 3. Global Error Handling

In a production app, if a database connection drops, a random `try/catch` might swallow the error, leaving the client hanging forever.

To fix this in the Express Product Service, we implement a **Global Error Handler** middleware at the very bottom of our `index.ts` file.

### The Express Error Catcher

This middleware must have exactly 4 arguments `(err, req, res, next)` for Express to recognize it as an error handler.

TypeScript

```ts
// apps/product-services/src/index.ts
import express, { NextFunction, Request, Response } from "express";

const app = express();

// ... [All your other routes go here] ...

// THE GLOBAL ERROR HANDLER (Must be the last app.use!)
app.use((err: any, req: Request, res: Response, next: NextFunction) => {
  const errorStatus = err.status || 500;
  const errorMessage = err.message || "Something went critically wrong!";

  // Log to internal monitoring systems (like Sentry) here
  console.error(`[ERROR] ${req.method} ${req.url} - ${errorMessage}`);

  // Return a safe, formatted error to the client
  res.status(errorStatus).json({
    success: false,
    status: errorStatus,
    message: errorMessage,
    stack: process.env.NODE_ENV === "development" ? err.stack : {} // Hide stack traces in prod!
  });
});
```

**How to use it:** Now, inside any controller, if something breaks, you simply call `next(error)` and it acts as a funnel, sending the error straight to this global catcher.