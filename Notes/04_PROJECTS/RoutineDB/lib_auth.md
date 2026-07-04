---
tags: [lib, auth, clerk, session, cache, admin, backend]
---

# Code Library: Authentication Utilities

This utility module handles authentication session verification, automatic system profile registration, role promotions, caching, and role validations, located at `src/lib/auth.ts`.

- **File Link**: [auth.ts](file:///d:/02_CODE/04_TEST/Routine/src/lib/auth.ts)
- **Backlinks**: [[index]], [[SCHEMA]], [[api_user]]

---

## 1. Core Functions

### `getAuthenticatedUser()` (Cached)
- Uses React's `cache()` wrapper to ensure that multiple invocations of this helper during a single server-side rendering cycle or request roundtrip resolve to a single cache entry, minimizing Clerk API overhead.
- Fetches the active Clerk ID from the request headers using `auth()`.
- Queries the MySQL user table. If the student does not exist (first-time sign-in):
  - Fetches profile info (Name, Email) from Clerk's `currentUser()`.
  - Determines the student's role:
    - Checks Clerk public metadata for overrides.
    - If it's the very first user record in the MySQL table, auto-promotes the student to `"admin"`.
    - Otherwise, defaults to `"user"`.
  - Inserts the new record into the database.
- If the user already exists, checks if the role stored in Clerk's public metadata has changed and syncs it.

### `requireAdmin()`
- Invocable by admin-only pages or API endpoints. Calls `getAuthenticatedUser()`, checks if the user's role is `"admin"`, and throws a `403 Forbidden` error if the role check fails.

### `getClerkUserId()`
- Fast check to retrieve the Clerk string identifier without loading the database record.

---

## 2. Source Code

Here is the complete implementation of `src/lib/auth.ts`:

```typescript
import { cache } from 'react';
import { auth, currentUser } from '@clerk/nextjs/server';
import { prisma } from './prisma';

/**
 * Get the authenticated user from Clerk + find/create in our DB.
 * Auto-creates a User record on first sign-in.
 * First user ever is auto-promoted to admin.
 * 
 * Wrapped with React.cache() so that within a single server request,
 * multiple calls resolve to the same cached result (no duplicate
 * Clerk API roundtrips or Prisma queries).
 */
export const getAuthenticatedUser = cache(async () => {
  const { userId } = await auth();
  if (!userId) {
    throw new Error('Unauthorized: No authenticated user');
  }

  // Check if user already exists in our DB
  let user = await prisma.user.findUnique({
    where: { clerkId: userId },
  });

  if (!user) {
    // First-time sign-in: create user record
    let clerkUser = null;
    try {
      clerkUser = await currentUser();
    } catch (err) {
      console.error('⚠️ Failed to fetch user profile from Clerk during initial sign-in:', err);
    }

    // Check if this is the very first user in the system → make them admin
    const userCount = await prisma.user.count();
    const isFirstUser = userCount === 0;

    // Check Clerk metadata for role override
    const metadataRole = (clerkUser?.publicMetadata?.role as string) || null;
    const role = metadataRole || (isFirstUser ? 'admin' : 'user');

    user = await prisma.user.create({
      data: {
        clerkId: userId,
        name: clerkUser?.fullName || clerkUser?.firstName || 'New User',
        email: clerkUser?.primaryEmailAddress?.emailAddress || '',
        role,
      },
    });

    if (isFirstUser) {
      console.log(`🎉 First user "${user.name}" auto-promoted to admin!`);
    }
  } else {
    // Sync role from Clerk metadata if it changed, catching any network/API errors
    try {
      const clerkUser = await currentUser();
      if (clerkUser) {
        const metadataRole = (clerkUser.publicMetadata?.role as string) || null;
        if (metadataRole && metadataRole !== user.role) {
          user = await prisma.user.update({
            where: { id: user.id },
            data: { role: metadataRole },
          });
        }
      }
    } catch (error) {
      console.warn('⚠️ Could not sync user role from Clerk (network error):', error);
    }
  }

  return user;
});

/**
 * Require admin role. Throws if user is not admin.
 */
export async function requireAdmin() {
  const user = await getAuthenticatedUser();
  if (user.role !== 'admin') {
    throw new Error('Forbidden: Admin access required');
  }
  return user;
}

/**
 * Get user ID from auth without creating a record (for lightweight checks).
 */
export async function getClerkUserId(): Promise<string> {
  const { userId } = await auth();
  if (!userId) {
    throw new Error('Unauthorized');
  }
  return userId;
}
```
