tags:

- database

- postgresql

- prisma

- sql

- orm

- backend date: 2026-08-04

# Day 4 - Relational Databases, PostgreSQL & Prisma ORM Architecture

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Relational Database Principles: ACID & Isolation Levels

Relational Database Management Systems (RDBMS) ensure transactional integrity via **ACID** properties:

- **Atomicity**: All operations in a transaction succeed or all fail/rollback completely.

- **Consistency**: Database transitions from one valid state to another, enforcing constraints (FK, Unique, Check).

- **Isolation**: Concurrent transactions execute without cross-contamination.

- **Durability**: Committed data persists across crashes (WAL - Write-Ahead Logging).

#### Concurrency Isolation Levels & Anomalies:

  ------------------------------------------------------------------------------------------------------------------------------------------
  **Isolation Level**                       **Dirty Read**   **Non-Repeatable Read**   **Phantom Read**          **Serialization Anomaly**
  ----------------------------------------- ---------------- ------------------------- ------------------------- ---------------------------
  **Read Uncommitted**                      Possible         Possible                  Possible                  Possible

  **Read Committed** (PostgreSQL Default)   Prevented        Possible                  Possible                  Possible

  **Repeatable Read**                       Prevented        Prevented                 Prevented (in Postgres)   Possible

  **Serializable**                          Prevented        Prevented                 Prevented                 Prevented
  ------------------------------------------------------------------------------------------------------------------------------------------

### 2. PostgreSQL Architecture & Indexing Mechanics

PostgreSQL uses multi-version concurrency control (**MVCC**) to handle concurrent reads and writes without locking.

#### Index Types & Use Cases:

1.  **B-Tree (Default)**: Equality (=) and range queries (\<, \>, BETWEEN, ORDER BY).

2.  **GIN (Generalized Inverted Index)**: Array types, JSONB fields, full-text search.

3.  **GiST / SP-GiST**: Geometric data, range types, nearest-neighbor searches.

4.  **BRIN (Block Range Index)**: Large append-only data (timeseries/logs) with minimal disk footprint.

\-- PostgreSQL B-Tree Composite Index Optimization

CREATE INDEX idx_orders_user_created ON orders (user_id, created_at DESC);

\-- Optimizes queries matching: WHERE user_id = \'usr_101\' ORDER BY created_at DESC;

### 3. Prisma ORM Architecture & Query Engine

Prisma bridges Node.js/TypeScript applications with SQL databases via a modular architecture:

1.  **Prisma Schema (schema.prisma)**: Declarative data model mapping models to SQL tables.

2.  **Prisma Client (TypeScript)**: Auto-generated type-safe client query builder.

3.  **Prisma Query Engine (Rust)**: High-performance binary executable that compiles Prisma query ASTs into optimized native SQL queries.

// Production schema.prisma

datasource db {

provider = \"postgresql\"

url = env(\"DATABASE_URL\")

}

generator client {

provider = \"prisma-client-js\"

}

enum Role {

USER

ADMIN

}

model User {

id String \@id \@default(uuid())

email String \@unique

name String?

role Role \@default(USER)

orders Order\[\]

createdAt DateTime \@default(now())

updatedAt DateTime \@updatedAt

@@index(\[email\])

@@map(\"users\")

}

model Order {

id String \@id \@default(uuid())

userId String

user User \@relation(fields: \[userId\], references: \[id\], onDelete: Cascade)

totalAmount Decimal \@db.Decimal(10, 2)

status String \@default(\"PENDING\")

version Int \@default(1) // For Optimistic Locking

createdAt DateTime \@default(now())

@@index(\[userId, createdAt(sort: Desc)\])

@@map(\"orders\")

}

// Transaction & N+1 Prevention Pattern in Prisma

import { PrismaClient } from \'@prisma/client\';

const prisma = new PrismaClient();

// Interactive Transaction with Optimistic Locking

async function processCheckout(userId: string, totalAmount: number) {

return await prisma.\$transaction(async (tx) =\> {

// 1. Fetch user & check state

const user = await tx.user.findUnique({

where: { id: userId },

select: { id: true, email: true } // Select specific fields to prevent over-fetching

});

if (!user) throw new Error(\"User not found\");

// 2. Create Order

const order = await tx.order.create({

data: {

userId: user.id,

totalAmount,

status: \"COMPLETED\"

}

});

return order;

});

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Operation / Feature**     **Prisma CLI / Syntax**                               **SQL Equivalence**                        **Best Practice**
  --------------------------- ----------------------------------------------------- ------------------------------------------ -----------------------------------------------------------
  **Apply Dev Migration**     npx prisma migrate dev                                ALTER TABLE / CREATE TABLE                 Auto-generates timestamped SQL migration files

  **Generate Client Types**   npx prisma generate                                   N/A                                        Run automatically after schema modifications

  **Field Select**            prisma.user.findMany({ select: { id: true } })        SELECT id FROM users;                      Prevents over-fetching large JSON/text columns

  **Relation Join**           prisma.user.findMany({ include: { orders: true } })   JOIN orders ON users.id = orders.user_id   Solves N+1 query problem by fetching in unified queries

  **Transactions**            prisma.\$transaction(\[p1, p2\])                      BEGIN; \... COMMIT;                        Use sequential array transactions or interactive callback
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Schema & Transaction Design (Multi-tenant Inventory & Order Engine)

Design a multi-tenant Prisma schema and transaction architecture for a **Flash Sale E-Commerce Platform**.

**Requirements**:

1.  Define the Prisma models for Store, Product, Stock, Order, and OrderItem.

2.  Implement **Optimistic Locking** using a \@default(1) version column to prevent race conditions during high-concurrency item reservations.

3.  Write an architectural strategy to prevent deadlock scenarios when multiple buyers attempt to reserve the final stock items simultaneously.

### Problem 2: End-to-End Code Implementation Challenge

Build a robust **Prisma Financial Ledger & Transfer Service** in TypeScript.

**Requirements**:

1.  Implement a transferFunds(fromAccountId: string, toAccountId: string, amount: number) function inside a Prisma \$transaction.

2.  Ensure accounts cannot go below a zero balance (throw operational error).

3.  Implement an exponential backoff retry wrapper (retryTransaction(fn, maxRetries = 3)) to automatically catch Postgres serialization failure/deadlock errors (SQLSTATE 40001 / 40P01) and retry.

4.  Write test cases simulating 10 concurrent transfers between two accounts.
