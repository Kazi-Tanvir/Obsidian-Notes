---
tags:
- backend
- api-gateway
- rate-limiting
- microservices
- reverse-proxy
- system-design
date: 2026-08-16
---

# Day 16 - API Gateway Architecture, Rate Limiting, Request Aggregation & Reverse Proxies

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Core Purpose of an API Gateway

In modern microservices architectures, exposing internal microservices directly to client applications leads to excessive client-server roundtrips, tight coupling, and complex authentication logic spread across multiple services. An **API Gateway** serves as the single reverse-proxy entry point for all external traffic.

#### Key Gateway Responsibilities:

1.  **Request Routing & Path Rewriting**: Maps external endpoints (e.g. /api/v1/orders) to internal service IPs (http://order-service:5000/orders).

2.  **Authentication & Authorization Offloading**: Validates JWTs or session tokens at the boundary, appending enriched headers (X-User-Id, X-User-Role) before passing requests downstream.

3.  **Request Aggregation (Gateway Aggregation / BFF Pattern)**: Collates responses from multiple internal microservices into a single JSON payload for mobile/web frontends.

4.  **SSL Termination & CORS Handling**: Manages TLS certificates and browser CORS preflight requests centrally.

5.  **Traffic Shaping & Global Rate Limiting**: Protects backend services against DoS attacks and resource exhaustion.

### 2. Distributed Rate Limiting Algorithms

| **Algorithm** | **Mechanism** | **Pros** | **Cons / Trade-offs** |
| --- | --- | --- | --- |
| **Token Bucket** | Tokens added at fixed rate; requests consume tokens | Handles bursts smoothly; memory efficient | Requires atomic decrement operations |
| **Leaky Bucket** | Requests enter queue; processed at constant output rate | Smooths traffic peaks; prevents downstream overload | Drops bursts if buffer queue is full |
| **Fixed Window** | Counts requests in fixed time intervals (e.g. 1 min) | Minimal memory usage; simple counters | Burst at boundary edges can double rate limit |
| **Sliding Window Counter** | Combines previous window weight with current window count | High accuracy; prevents window boundary spikes | Moderate Redis memory & compute overhead |

```typescript
// Redis Sliding Window Counter Rate Limiting Algorithm
import Redis from 'ioredis';
const redis = new Redis();
async function checkRateLimit(key: string, limit: number, windowSeconds: number): Promise<{ allowed: boolean; remaining: number }> {
const now = Date.now();
const windowMs = windowSeconds * 1000;
const clearBefore = now - windowMs;
// Pipeline: 1. Remove expired requests 2. Add current request 3. Count requests in window 4. Set TTL
const multi = redis.multi();
multi.zremrangebyscore(key, 0, clearBefore);
multi.zadd(key, now, `${now}-${Math.random()}`);
multi.zcard(key);
multi.expire(key, windowSeconds);
const results = await multi.exec();
const currentCount = results?.[2]?.[1] as number;
const allowed = currentCount <= limit;
const remaining = Math.max(0, limit - currentCount);
return { allowed, remaining };
}
```

### 3. Circuit Breaker Pattern & Cascading Failure Prevention

When an upstream microservice degrades, continuous incoming requests can exhaust thread pools and connection sockets across the gateway. A **Circuit Breaker** monitors error rates and stops forwarding requests to unhealthy services:

- **CLOSED State**: Normal operation. Requests pass through. Failures are counted.

- **OPEN State**: Failure threshold exceeded (e.g. 50% errors). Requests immediately fail fast or return fallback data without touching the backend.

- **HALF-OPEN State**: After a reset timeout, a fraction of requests are allowed through to probe service recovery.

```javascript
// Circuit Breaker State Transition
enum CircuitState { CLOSED, OPEN, HALF_OPEN }
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Standard Rate Limiting Headers:

- X-RateLimit-Limit: Maximum requests permitted within the time window.

- X-RateLimit-Remaining: Number of requests remaining in current window.

- X-RateLimit-Reset: Unix epoch timestamp when quota resets.

- Retry-After: Number of seconds the client must wait before making another request (on 429 Too Many Requests).

### Essential Reverse Proxy Headers:

X-Forwarded-For: <client-ip>, <proxy1-ip>

X-Forwarded-Proto: https

X-Forwarded-Host: api.example.com

X-Request-Id: 7d1a2f3b-8c4e-4b9d-a1f0-938204918234

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: High-Throughput API Gateway Architecture

Design a globally distributed API Gateway architecture for an Enterprise E-Commerce platform handling 150k Requests Per Second (RPS).

**Requirements**:

1.  Draw the network topology showing the relationship between Anycast DNS, Cloudflare/AWS CloudFront Edge, Envoy Proxy / Kong Gateway instances, Redis cluster, and downstream microservices (AuthService, ProductService, CartService, PaymentService).

2.  Specify the authentication token caching strategy and rate-limiting tiers (Public unauthenticated vs Authenticated User vs VIP Tier).

3.  Detail the Request Aggregation strategy for a mobile Product Detail Page (combining product details, real-time inventory, and user-personalized recommendations).

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **API Gateway Request Aggregator & Rate Limiter** in Node.js / Fastify.

**Requirements**:

1.  Implement a unified aggregation route GET /api/v1/dashboard that concurrently fetches:

    - User Profile from http://user-service:4001/profile

    - Active Notifications from http://notification-service:4002/unread

    - Account Metrics from http://analytics-service:4003/summary

2.  Integrate a Redis-backed Sliding Window rate-limiting middleware that returns standard X-RateLimit-* headers and responds with 429 Too Many Requests when limits are breached.

3.  Wrap downstream service calls with an in-memory Circuit Breaker: if analytics-service fails 3 times consecutively, return cached fallback metrics { metrics: null, status: "degraded" } without failing the entire dashboard response.

4.  Include test cases verifying rate-limit enforcement and circuit-breaker graceful degradation.
