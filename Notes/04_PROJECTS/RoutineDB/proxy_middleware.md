---
tags: [lib, middleware, security, clerk, matcher, backend]
---

# Code Library: Clerk Authentication Middleware

This file acts as the request proxy gateway, protecting routes and intercepting session payloads, located at `src/proxy.ts`.

- **File Link**: [proxy.ts](file:///d:/02_CODE/04_TEST/Routine/src/proxy.ts)
- **Backlinks**: [[index]], [[signin_page]], [[signup_page]]

---

## Technical Details

The middleware utilizes Clerk's `clerkMiddleware` to secure routes.
1. **Public Exclusions**: Declares `/sign-in` and `/sign-up` as public routes using `createRouteMatcher()`.
2. **Protection Gate**: For any incoming request that does NOT match the public route list, `auth.protect()` is executed, forcing a redirect to the Clerk Sign-In screen if a valid JWT cookie is missing.
3. **Matcher Boundaries**: Defines matching rules to intercept dashboard renders, API triggers (`/api/:path*`), and internal Clerk calls, while skipping static resources (JS, CSS, images, icons).

---

## Source Code

Here is the complete implementation of `src/app/proxy.ts` (placed as `src/proxy.ts` or `src/middleware.ts`):

```typescript
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isPublicRoute = createRouteMatcher([
  '/sign-in(.*)',
  '/sign-up(.*)',
]);

export const proxy = clerkMiddleware(async (auth, req) => {
  if (!isPublicRoute(req)) {
    await auth.protect();
  }
});

export const config = {
  matcher: [
    // Skip Next.js internals and all static files
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
    // Clerk auto-proxy path
    '/__clerk/:path*',
  ],
};
```
