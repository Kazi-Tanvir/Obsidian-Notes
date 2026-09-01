---
tags:
- devops
- system-design
- monorepo
- serverless
- docker
- cloud-architecture
date: 2026-08-14
---

# Day 14 - Week 2 Review: Monorepos, Serverless Edge Compute, Docker & Full-Stack System Integration

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Unified Full-Stack Architecture Topology

Modern enterprise web architectures integrate heterogeneous compute environments to balance execution latency, cold-start characteristics, compute cost, and development ergonomics.

[Client / Mobile App]

│

▼

[CDN & Edge Layer] ── (Vercel Edge / Cloudflare Workers: Auth, Geo-Routing, A/B Flags)

│

├──► Static Assets & Cached SSR Pages (Global Edge CDN)

▼

[Reverse Proxy / API Gateway] ── (Nginx / Envoy / Traefik: SSL Termination, Rate Limiting)

│

├──► [Serverless Compute] (AWS Lambda: Spike Traffic, Async Jobs, PDF Generation)

▼

[Containerized Microservices Cluster] (Docker Compose / ECS / Kubernetes: Fastify, Express)

│

├──► [Distributed Cache] (Redis: Session Store, Token Bucket Rate Limiting, Pub/Sub)

├──► [Primary Data Stores] (PostgreSQL + Prisma, MongoDB + Mongoose)

▼

[Event Broker] (Apache Kafka / RabbitMQ: Transactional Outbox, Order Event Processing)

### 2. High-Availability & Production Reliability Patterns

#### 1. Graceful Shutdown Draining:

When containers receive SIGTERM, they must stop accepting new HTTP requests, complete in-flight transactions within a timeout grace period, close database connection pools, and exit cleanly with code 0.

#### 2. Healthcheck Probes:

- **Liveness Probe**: Confirms the process is running. If failed, the orchestrator restarts the container.

- **Readiness Probe**: Confirms the service is ready to accept user traffic (database connections connected, Redis caches reachable).

#### 3. Distributed Tracing & Observability:

Propagate W3C Trace Context headers (traceparent, tracestate) across HTTP, gRPC, and Kafka messages to correlate distributed logs across microservice boundaries.

```typescript
// Production Graceful Shutdown Implementation Pattern
import http from 'http';
import { PrismaClient } from '@prisma/client';
import Redis from 'ioredis';
const prisma = new PrismaClient();
const redis = new Redis(process.env.REDIS_URL || 'redis://localhost:6379');
const server = http.createServer((req, res) => res.end('OK'));
async function handleShutdown(signal: string) {
console.log(`[Shutdown]: Received ${signal}. Draining connections...`);
// 1. Stop accepting new HTTP requests
server.close(async () => {
console.log('[Shutdown]: HTTP server closed.');
try {
// 2. Disconnect database connection pools & caches
await prisma.$disconnect();
await redis.quit();
console.log('[Shutdown]: Database & Redis connections released cleanly.');
process.exit(0);
} catch (err) {
console.error('[Shutdown Error]:', err);
process.exit(1);
}
});
// 3. Force exit if shutdown hangs beyond 10 seconds
```

setTimeout(() => {

```javascript
console.error('[Shutdown Timeout]: Forcing termination.');
process.exit(1);
}, 10000);
}
process.on('SIGTERM', () => handleShutdown('SIGTERM'));
process.on('SIGINT', () => handleShutdown('SIGINT'));
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Layer / Primitive** | **Key Configuration / Pattern** | **Production Role** |
| --- | --- | --- |
| **Turborepo** | turbo.json (dependsOn: ["\^build"])   Mon | repo dependency task graphs & remote caching |
| **Docker Multi-Stage** | FROM node:20-alpine AS runner | Strips devDependencies and produces minimal image |
| **Edge Compute** | runtime: 'edge' (Vercel / Cloudflare)   L | w-latency routing & auth token validation at PoPs |
| **Graceful Shutdown** | process.on('SIGTERM', cleanupFn)        P | events dropped requests during deployments |
| **Kafka Outbox** | Outbox Table + Debezium / Poller | Guarantees atomic database updates and event publishing |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Full-Scale System Design (Enterprise Global Video Platform)

Design an end-to-end architecture for a high-traffic Global Video Streaming & Analytics platform.

**Requirements**:

1.  **Frontend & Monorepo**: Structure a Turborepo monorepo with apps/web (Next.js App Router for viewer UI), apps/creator (creator portal), and packages/ui, packages/db.

2.  **Edge Auth & Routing**: Use Vercel Edge Middleware to validate JWTs and route users to the nearest regional video cache.

3.  **Async Event Pipeline**: Ingest video view telemetry events through Apache Kafka into a ClickHouse/PostgreSQL analytics cluster.

4.  **Resilience**: Implement rate limiting using Redis sliding window algorithms and automated dead-letter queues (DLQ) for failed video processing tasks.

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **Healthcheck & Resilience Lifecycle Manager** in TypeScript.

**Requirements**:

1.  Implement a /health/liveness route that returns 200 OK if the Node.js event loop is responsive.

2.  Implement a /health/readiness route that concurrently pings PostgreSQL (SELECT 1) and Redis (PING) and returns 503 Service Unavailable if any dependency is degraded.

3.  Implement a centralized GracefulShutdownManager class that tracks active in-flight HTTP requests and prevents process termination until all requests complete (or until timeout expires).

4.  Include automated integration tests simulating sudden SIGTERM signals and verifying zero lost requests during shutdown.
