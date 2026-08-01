---
tags:
  - backend
  - api-design
  - http
  - express
  - rest
date: 2026-08-01
---

# Day 1 - Client-Server Architecture & RESTful API Design

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Client-Server Paradigm & HTTP Protocol Evolution

Modern web applications rely on the **Client-Server Architecture**, where clients (browsers, mobile apps, single-page applications) initiate requests to servers that process business logic and return resources.

#### Protocol Hierarchy & Evolution:

- **HTTP/1.1**: Persistent TCP connections, head-of-line blocking, plaintext request/response headers.  
- **HTTP/2**: Binary framing layer, multiplexing over a single TCP connection, header compression (HPACK), server push.  
- **HTTP/3**: Built on **QUIC** (UDP-based protocol), eliminating TCP head-of-line blocking during packet loss, faster connection establishment with TLS 1.3 integration.

#### HTTP Anatomy:

- **Request**: Method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`), URI, Version, Headers (`Authorization`, `Content-Type`, `Accept`), Body.  
- **Response**: Status Code (`1xx`, `2xx`, `3xx`, `4xx`, `5xx`), Headers (`Cache-Control`, `Set-Cookie`, `CORS`), Body (`JSON`, `HTML`, binary).

---

### 2. RESTful API Principles & Idempotency

**REST (Representational State Transfer)** is an architectural style guided by 6 constraints:

1. **Statelessness**: Every request contains all information needed to process it. Server stores no client session context.  
2. **Client-Server**: Separation of concerns between UI/UX and data storage/processing.  
3. **Cacheability**: Responses must define themselves as cacheable or non-cacheable (`Cache-Control`).  
4. **Uniform Interface**: Identification of resources via URIs (`/api/v1/users`), manipulation through representations, self-descriptive messages, HATEOAS.  
5. **Layered System**: Hierarchical layers (proxies, load balancers, gateways) transparent to the client.  
6. **Code on Demand (Optional)**: Executable code returned to client (e.g. JavaScript scripts).

#### Method Idempotency & Safety:

| HTTP Verb | Safe? | Idempotent? | Typical Use Case |
| :---- | :---- | :---- | :---- |
| `GET` | Yes | Yes | Retrieve resource representation |
| `POST` | No | No | Create new resource / process non-idempotent action |
| `PUT` | No | Yes | Replace resource completely or create at specific URI |
| `PATCH` | No | No (usually) | Partial modification of resource |
| `DELETE` | No | Yes | Remove resource |

---

### 3. Production Node.js & Express API Implementation Pattern
```tsx
import express, { Request, Response, NextFunction } from 'express';
const app = express();

app.use(express.json());

// Standard API Response Contract Interface
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

// Controller Implementation Pattern
app.get('/api/v1/products/:id', async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { id } = req.params;
    if (!id || isNaN(Number(id))) {
      return res.status(400).json({ success: false, error: 'Invalid product ID' });
    }

    // Simulated DB Query
    const product = { id: Number(id), name: 'High Performance Server', price: 1299.99 };

    if (!product) {
      return res.status(404).json({ success: false, error: 'Product not found' });
    }

    return res.status(200).json({ success: true, data: product });
  } catch (error) {
    next(error); // Pass to centralized error handler
  }
});

// Centralized Error Handling Middleware
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
  console.error('[API Error]:', err.stack);
  res.status(500).json({ success: false, error: 'Internal Server Error' });
});
```

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### HTTP Status Code Reference

- **200 OK**: Request succeeded.  
- **201 Created**: Resource successfully created (`POST`/`PUT`).  
- **204 No Content**: Action executed successfully, no response body (`DELETE`).  
- **400 Bad Request**: Malformed syntax, invalid payload, or failed validation.  
- **401 Unauthorized**: Missing or invalid authentication token.  
- **403 Forbidden**: Authenticated user lacks permission for resource.  
- **404 Not Found**: Endpoint or resource URI does not exist.  
- **409 Conflict**: State conflict (e.g. duplicate key / email already exists).  
- **422 Unprocessable Entity**: Valid syntax but semantic validation failed.  
- **500 Internal Server Error**: Unhandled server-side exception.  
- **503 Service Unavailable**: Server overloaded or undergoing maintenance.

### RESTful URI Naming Conventions

- Use **plural nouns** for resource collections: `/api/v1/orders`, `/api/v1/users`.  
- Sub-resources reflect relationships: `/api/v1/users/:userId/orders`.  
- Use **hyphens (`-`)** for readability instead of underscores (`_`): `/api/v1/payment-intents`.  
- Never use verbs in resource paths (Anti-pattern: `/api/getUsers`, `/api/createOrder`). Use HTTP verbs instead.

### CLI Testing Commands (`curl`)

```bash
# GET with Headers & Authorization
curl -X GET https://api.example.com/v1/orders \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Accept: application/json"

# POST JSON Payload
curl -X POST https://api.example.com/v1/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Monitor","price":299.99}'
```

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Architecture / Schema & API Contract Design

Design a production-grade RESTful API specification for a **Multi-tenant SaaS E-Commerce Cart & Checkout Service**.

**Requirements**:

1. Define the full HTTP endpoint table (HTTP Verb, Path, Description, Request Headers, Status Codes).  
2. Write JSON Request and Response schemas for:  
   - Adding an item to a cart.  
   - Applying a promo code (handling edge cases like expired code or minimum purchase criteria).  
   - Finalizing checkout (idempotent submission using `Idempotency-Key` header).  
3. Specify how tenant separation (`Tenant-ID`) and authentication token verification are handled architecturally.

---

### Problem 2: End-to-End Code Implementation Challenge

Build an Express/Node.js router module for **User Management** that satisfies the following criteria:

**Requirements**:

1. Implement route handlers for:  
   - `POST /api/v1/users` (Registration with field validation: `email`, `password` min 8 chars, `role`).  
   - `GET /api/v1/users` (Supports query parameters for pagination: `page`, `limit`, and filtering: `role`).  
   - `PATCH /api/v1/users/:id` (Partial update of profile information).  
2. Implement a custom validation middleware that checks input payloads against a schema without letting invalid data reach the handler.  
3. Ensure every error is passed through a global error-handling middleware that returns standardized `{ success: false, error: string, timestamp: string }` response objects.  
4. Provide unit/integration test cases (specifying test inputs and expected status codes).

