tags:

- backend

- redis

- caching

- performance

- database

- system-design date: 2026-08-06

# Day 6 - In-Memory Caching, Redis Data Structures & Cache Invalidation Strategies

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. In-Memory Caching Architecture & Value Proposition

In high-throughput microservices, disk-bound databases (PostgreSQL, MongoDB) become performance bottlenecks. In-Memory caching sits in front of storage layer to deliver **sub-millisecond data access** and protect databases from traffic surges.

#### Core Caching Strategies:

1.  **Cache-Aside (Lazy Loading)**: Application queries Cache first. On Cache Miss, reads DB, populates Cache with TTL, and returns data. (Most common).

2.  **Write-Through**: Application writes to Cache; Cache synchronously writes to DB before acknowledging client.

3.  **Write-Behind (Write-Back)**: Application writes to Cache; Cache asynchronously flushes writes to DB in batches (High throughput, risk of data loss on crash).

4.  **Refresh-Ahead**: Cache automatically refreshes items before expiration based on access patterns.

### 2. Redis Engine Architecture & Native Data Structures

Redis (Remote Dictionary Server) is an in-memory key-value data store powered by an **I/O Multiplexed Single-Threaded Event Loop Engine**, eliminating concurrency locks while executing atomic operations.

#### Essential Redis Data Primitives:

- **Strings**: Text, JSON strings, integers (supports atomic INCR / DECR).

- **Hashes**: Object representations (HSET user:101 name \"Alice\" age 30).

- **Lists**: Linked lists (LPUSH / RPOP for job queues).

- **Sets**: Unique unordered elements (SADD / SINTER for common friends).

- **Sorted Sets (ZSET)**: Unique elements scored by floating-point numbers (ZADD leaderboard 1500 \"user101\"). Ideal for leaderboard ranking and Sliding Window Rate Limiters.

// Production Node.js ioredis Cache-Aside Service Pattern

import Redis from \'ioredis\';

const redis = new Redis({

host: process.env.REDIS_HOST \|\| \'127.0.0.1\',

port: Number(process.env.REDIS_PORT) \|\| 6379,

maxRetriesPerRequest: 3

});

export async function getCachedData\<T\>(

key: string,

ttlSeconds: number,

fetchFromDbFn: () =\> Promise\<T\>

): Promise\<T\> {

// 1. Check Redis Cache

const cached = await redis.get(key);

if (cached) {

return JSON.parse(cached) as T;

}

// 2. Cache Miss: Query Database

const freshData = await fetchFromDbFn();

// 3. Populate Redis with TTL (SETEX)

if (freshData) {

await redis.setex(key, ttlSeconds, JSON.stringify(freshData));

}

return freshData;

}

### 3. Mitigating Cache Stampede (Thundering Herd) & Distributed Locks

**Cache Stampede** occurs when a highly requested cache key expires simultaneously under heavy traffic, causing thousands of concurrent requests to hit the database at once.

#### Solution: Distributed Mutex Locking (Redlock / Mutex Key)

When a Cache Miss occurs, the first request acquires a short-lived distributed Redis lock (SET key value NX PX 5000) to recompute and populate the cache while secondary requests wait or retry.

// Redis Mutex Lock to Prevent Cache Stampede

async function getWithMutexLock\<T\>(

key: string,

lockKey: string,

ttl: number,

fetchFn: () =\> Promise\<T\>

): Promise\<T\> {

let cached = await redis.get(key);

if (cached) return JSON.parse(cached);

// Acquire Lock (NX = Only set if Not Exist, PX = Expiration in ms)

const acquiredLock = await redis.set(lockKey, \'locked\', \'NX\', \'PX\', 3000);

if (acquiredLock === \'OK\') {

try {

const freshData = await fetchFn();

await redis.setex(key, ttl, JSON.stringify(freshData));

return freshData;

} finally {

await redis.del(lockKey); // Release lock

}

} else {

// Lock held by another request: Sleep and retry

await new Promise((resolve) =\> setTimeout(resolve, 50));

return getWithMutexLock(key, lockKey, ttl, fetchFn);

}

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

  ----------------------------------------------------------------------------------------------------
  **Command**             **Syntax**                **Description / Use Case**
  ----------------------- ------------------------- --------------------------------------------------
  **SETEX**               SETEX key seconds value   Sets key with automatic expiration (TTL)

  **HSET / HGETALL**      HSET key field value      Reads/writes Hash fields (Memory efficient DTOs)

  **ZADD / ZRANGE**       ZADD key score member     Adds to Sorted Set (Leaderboards, Rate Limiters)

  **EXPIRE / TTL**        EXPIRE key seconds        Updates TTL or checks remaining time

  **DEL / UNLINK**        UNLINK key                Asynchronous non-blocking deletion of large keys
  ----------------------------------------------------------------------------------------------------

### Redis Eviction Policies (redis.conf):

- allkeys-lru: Evicts least recently used keys out of all keys (Best for general caching).

- volatile-lru: Evicts LRU keys only among keys with an explicit TTL.

- noeviction: Returns error on memory limit reached (Best for queues/DB state).

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Multi-Tier Caching for E-Commerce Flash Sale)

Design a multi-tier caching architecture for an E-Commerce Flash Sale platform facing **500,000 Reads/sec** on product stock pages.

**Requirements**:

1.  Diagram Local In-Memory Cache (L1 - Node.js node-cache) vs Centralized Redis Cache (L2).

2.  Define key naming schemes, TTL strategies, and active cache invalidation upon stock updates.

3.  Architect a solution for handling **Hot Key Problem** (single item getting 90% of traffic).

### Problem 2: End-to-End Code Implementation Challenge

Build a **Redis Sliding Window Rate Limiter Middleware** in TypeScript using Redis Sorted Sets (ZSET).

**Requirements**:

1.  Create rateLimiter(windowMs: number, maxLimit: number) middleware for Express/Fastify.

2.  Track client IP request timestamps using ZSET (ZADD key timestamp timestamp).

3.  Remove outdated entries outside window (ZREMRANGEBYSCORE key 0 (now - windowMs)).

4.  Return HTTP 429 Too Many Requests with rate headers (X-RateLimit-Limit, X-RateLimit-Remaining, Retry-After) when request count exceeds threshold.

5.  Provide unit tests testing rate window overflow.
