---
tags: [lib, database, prisma, client, singleton, backend]
---

# Code Library: Prisma Connection Singleton

This script instantiates the **Prisma Client** ORM connection pool and registers it globally to prevent hot-reloading memory leaks in non-production environments, located at `src/lib/prisma.ts`.

- **File Link**: [prisma.ts](file:///d:/02_CODE/04_TEST/Routine/src/lib/prisma.ts)
- **Backlinks**: [[index]], [[SCHEMA]]

---

## Technical Details

In serverless or fast-refresh development environments (like Next.js dev server), edits to files trigger updates that re-execute import headers. If the Prisma Client were initialized directly (`const prisma = new PrismaClient()`), each file change would establish a new connection pool to the database, exhausting the MySQL database connection limit within minutes.

To resolve this, the script:
1. Declares a global type wrapper `globalForPrisma`.
2. Stores the client instance in `globalThis.prisma`.
3. In `production`, initializes a fresh client directly.
4. In `development` (non-production), checks if `globalThis.prisma` exists. If not, instantiates it, and reuse it for subsequent calls.

---

## Source Code

Here is the complete implementation of `src/lib/prisma.ts`:

```typescript
import { PrismaClient } from '@prisma/client';

const globalForPrisma = global as unknown as { prisma: PrismaClient };

export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient({
    log: process.env.NODE_ENV === 'development' ? ['query', 'error', 'warn'] : ['error'],
  });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
```
