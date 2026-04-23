---
tags:
- nextjs
- middleware
- auth
---
# Middleware

## What's the Actual Use?
Middleware allows you to run code before a request is completed. It can be used to intercept users, check their authentication status, and redirect them if they don't have permission to view a page, or to rewrite URLs for internationalization.

## Real-Life Analogy
Middleware is like the bouncer at a club. Before you can enter the building (the route), the bouncer checks your ID (the session/cookie). If you have it, they let you in. If not, they tell you to go away or redirect you to the ticket booth (the login page).

## Other Common Use Cases
- Protecting all routes under `/dashboard/*` from unauthenticated users
- Implementing A/B testing by showing different versions of a page to different users
- Adding custom headers to every response (e.g., security headers)

## Documentation & Code
Middleware is defined in a `middleware.js` file at the root of the project.

```javascript
// middleware.js
import { NextResponse } from 'next/server';

export function middleware(request) {
  const token = request.cookies.get('session');

  // If trying to access dashboard without a session cookie, redirect to login
  if (request.nextUrl.pathname.startsWith('/dashboard') && !token) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next(); // Continue as normal
}

// Optional: Limit middleware to specific paths
export const config = {
  matcher: '/dashboard/:path*',
};
```