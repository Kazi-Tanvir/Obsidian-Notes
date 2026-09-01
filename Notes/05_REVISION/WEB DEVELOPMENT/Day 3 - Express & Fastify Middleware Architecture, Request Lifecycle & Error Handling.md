---
tags:
- backend
- nodejs
- express
- fastify
- middleware
- api-design
date: 2026-08-03
---

# Day 3 - Express & Fastify Middleware Architecture, Request Lifecycle & Error Handling

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Express Middleware Stack & Chain of Responsibility

In Express.js, request handling is structured as a pipeline of **middleware functions** following the *Chain of Responsibility* design pattern. A middleware function receives (req, res, next) and can:

- Execute any application logic.

- Modify the req (Request) or res (Response) objects (e.g. attaching req.user).

- Terminate the request-response cycle by sending a response (res.json(...)).

- Call next() to pass control to the next middleware in the stack.

- Call next(err) to bypass normal route handlers and trigger error-handling middleware.

```typescript
// Express Custom Middleware & Error Pipeline
import express, { Request, Response, NextFunction } from 'express';
const app = express();
// Custom Context Enrichment Middleware
interface AuthenticatedRequest extends Request {
user?: { id: string; role: string };
correlationId?: string;
}
const correlationIdMiddleware = (req: AuthenticatedRequest, res: Response, next: NextFunction) => {
req.correlationId = (req.headers['x-correlation-id'] as string) || `corr_${Date.now()}`;
res.setHeader('X-Correlation-ID', req.correlationId);
next();
};
app.use(express.json());
app.use(correlationIdMiddleware);
// Route Handler
app.get('/api/v1/orders', (req: AuthenticatedRequest, res: Response, next: NextFunction) => {
if (!req.headers.authorization) {
// Forward operational error
return next(new AppError('Missing Authorization Header', 401));
}
res.status(200).json({ success: true, correlationId: req.correlationId, orders: [] });
});
```

### 2. Fastify Lifecycle Hooks & Encapsulation Model

Fastify improves performance and safety through a compiled schema-based router (Ajv) and an explicit **Lifecycle Hook Architecture**. Fastify requests pass through distinct lifecycle hooks:

Incoming Request

│

▼

[onRequest] ──────────► (Logging, Early Rate Limiting)

│

▼

[preParsing] ─────────► (Body Stream Decoding)

│

▼

[preValidation] ──────► (Authentication / JWT Check)

│

▼

[preHandler] ─────────► (Authorization / RBAC Checks)

│

▼

[Handler] ────────────► (Business Logic Controller)

│

▼

[preSerialization] ──► (Data Scrubbing / Response DTO Filtering)

│

▼

[onResponse] ─────────► (Metrics, Audit Logging)

```javascript
// Fastify Plugin & Hook Encapsulation Pattern
import Fastify, { FastifyInstance } from 'fastify';
const fastify = Fastify({ logger: true });
// Registering preHandler hook for Authentication
fastify.addHook('preHandler', async (request, reply) => {
const token = request.headers['authorization'];
if (!token && request.routerPath !== '/health') {
reply.code(401).send({ success: false, error: 'Unauthorized' });
}
});
fastify.get('/api/v1/users', async (request, reply) => {
return { success: true, data: [{ id: 1, name: 'Alice' }] };
});
```

### 3. Centralized Error Handling Architecture

Production API design mandates a distinction between **Operational Errors** (predictable validation failures, 404s, 401s) and **Programmer Errors** (uncaught exceptions, null pointers, DB connection loss).

```typescript
// Custom Hierarchy of Operational Errors
export class AppError extends Error {
public readonly statusCode: number;
public readonly isOperational: boolean;
constructor(message: string, statusCode: number = 500, isOperational = true) {
super(message);
this.statusCode = statusCode;
this.isOperational = isOperational;
Object.setPrototypeOf(this, new.target.prototype);
Error.captureStackTrace(this, this.constructor);
}
}
export class BadRequestError extends AppError {
constructor(message = 'Bad Request') { super(message, 400); }
}
export class NotFoundError extends AppError {
constructor(message = 'Resource Not Found') { super(message, 404); }
}
// Express Centralized Global Error Handler (4 arguments signature)
app.use((err: Error | AppError, req: Request, res: Response, next: NextFunction) => {
const statusCode = err instanceof AppError ? err.statusCode : 500;
const message = err instanceof AppError && err.isOperational
```

? err.message

```javascript
: 'Internal Server Error';
console.error(`[ERROR] ${req.method} ${req.url} - ${err.stack}`);
res.status(statusCode).json({
```

success: false,

error: message,

timestamp: new Date().toISOString()

```javascript
});
});
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Middleware Type / Feature** | **Express Implementation** | **Fastify Equivalent** | **Best Practice** |
| --- | --- | --- | --- |
| **Global Hook / Use** | app.use(fn) | fastify.addHook('onRequest', fn)                          A | tach correlation IDs and basic request timing |
| **Route Protection** | app.get('/path', authMw, handler)      f | stify.get('/path', { preHandler: [auth] }, handler)   Run v | lidation and auth before business controllers |
| **Error Handling** | 4-arg middleware (err, req, res, next) | fastify.setErrorHandler((err, req, reply)) | Distinguish operational vs programmer errors |
| **Schema Validation** | Manual (Zod / Joi middleware) | Native Ajv JSON Schema in route options | Fastify compiles Ajv schemas for high-speed serialization |
| **Security Headers** | app.use(helmet()) | fastify.register(import('@fastify/helmet'))               M | ndatory in production environments |

### Standard HTTP Error Status Codes Mapping:

- **400**: BadRequestError (Validation failure, syntax error)

- **401**: UnauthorizedError (Authentication missing/invalid)

- **403**: ForbiddenError (Insufficient user scope/role)

- **404**: NotFoundError (URI or DB resource missing)

- **429**: TooManyRequestsError (Rate limit exceeded)

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Architecture Design (Financial Security Middleware Pipeline)

Design a multi-layer security, logging, and rate-limiting middleware pipeline for a high-security Payment Processing API endpoint (POST /api/v1/payments).

**Requirements**:

1.  Draw the middleware pipeline flow from incoming TCP connection to final response.

2.  Define how the pipeline handles:

    - Request Body Size Limiting (prevent DoS).

    - Rate limiting per API Key and IP address.

    - HMAC-SHA256 signature verification middleware.

    - Audit logging with non-blocking structured JSON logs (masking sensitive card data).

### Problem 2: End-to-End Code Implementation Challenge

Build a robust **Fastify or Express API Guard Suite** in TypeScript with custom validation and rate limiting.

**Requirements**:

1.  Implement a validateSchema(schema: ZodSchema) middleware that validates req.body, req.query, and req.params.

2.  Implement an in-memory **Token Bucket Rate Limiter** middleware (rateLimiter(maxRequests: number, windowMs: number)) that attaches rate limit headers (X-RateLimit-Limit, X-RateLimit-Remaining).

3.  Wire everything into a sample endpoint POST /api/v1/transfer with custom operational error handling (AppError).

4.  Provide unit tests covering rate limit triggering (429 status) and schema validation failure (400 status).
