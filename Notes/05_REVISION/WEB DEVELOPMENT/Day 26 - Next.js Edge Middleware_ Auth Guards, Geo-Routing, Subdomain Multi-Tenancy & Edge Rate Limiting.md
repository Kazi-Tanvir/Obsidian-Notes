---
tags:
- frontend
- nextjs
- edge-middleware
- auth
- rate-limiting
- multi-tenancy
- performance
- devops
date: 2026-08-26
---

# Day 26 - Next.js Edge Middleware: Auth Guards, Geo-Routing, Subdomain Multi-Tenancy & Edge Rate Limiting

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Edge Middleware Paradigm

Next.js Edge Middleware executes on globally distributed Edge servers (V8 Isolates) directly in the path of incoming HTTP requests before they reach the cache, static assets, or Node.js serverless compute.

Incoming Request ──► [ Anycast Edge CDN ] ──► [ Edge Middleware ] ──► Route Decision:

│

┌────────────────────────────────┼──────────────────────────────┐

▼ ▼ ▼

NextResponse.redirect() NextResponse.rewrite() NextResponse.next()

(307/308 URL changes) (Proxies internal path) (Passes to RSC/API)

#### Edge Runtime Constraints:

- Fast startup times (sub-5ms) with ultra-low memory overhead.

- No Node.js native binary addons (native C++), no filesystem (fs), no eval().

- Standard Web APIs supported: Fetch, Request, Response, Web Crypto API, URL, Headers, Cookies.

### 2. Core Architectural Use Cases

#### A. Edge Authentication & JWT Verification (via jose)

Verifying tokens at the Edge prevents unauthorized requests from ever triggering expensive database or serverless compute.

```javascript
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { jwtVerify } from 'jose';
const JWT_SECRET = new TextEncoder().encode(process.env.JWT_SECRET!);
export async function middleware(req: NextRequest) {
const token = req.cookies.get('auth_token')?.value;
if (!token) {
return NextResponse.redirect(new URL('/login', req.url));
}
try {
const { payload } = await jwtVerify(token, JWT_SECRET);
// Inject verified user metadata into headers for downstream Server Components
const requestHeaders = new Headers(req.headers);
requestHeaders.set('x-user-id', payload.sub as string);
requestHeaders.set('x-user-role', payload.role as string);
return NextResponse.next({
```

request: { headers: requestHeaders },

```javascript
});
} catch (err) {
return NextResponse.redirect(new URL('/login?error=invalid_session', req.url));
}
}
export const config = {
```

matcher: ['/dashboard/:path*', '/api/protected/:path*'],

```javascript
};
```

#### B. Subdomain Multi-Tenancy Rewriting

Allows SaaS platforms to map dynamic subdomains (tenant1.domain.com or custom domains acme.com) to internal multi-tenant routes (/app/tenants/tenant1) seamlessly without changing the browser address bar.

```javascript
export function handleMultiTenancy(req: NextRequest) {
const hostname = req.headers.get('host') || '';
const currentHost = hostname.replace(`.${process.env.NEXT_PUBLIC_ROOT_DOMAIN}`, '');
// If request is from root domain or admin portal, pass through
if (hostname === process.env.NEXT_PUBLIC_ROOT_DOMAIN || currentHost === 'admin') {
return NextResponse.next();
}
// Rewrite internal path: /posts -> /tenants/[tenant]/posts
const { pathname } = req.nextUrl;
return NextResponse.rewrite(
new URL(`/tenants/${currentHost}${pathname}`, req.url)
);
}
```

#### C. Geolocation Routing & Edge Compliance

Inspects incoming geolocation headers (geo.country, geo.city) to enforce data compliance (GDPR banner injection, regional content locking, currency localization).

```javascript
export function handleGeoRouting(req: NextRequest) {
const country = req.geo?.country || 'US';
const response = NextResponse.next();
response.headers.set('x-user-country', country);
if (country === 'EU' && !req.cookies.has('gdpr_consent')) {
response.cookies.set('show_gdpr_banner', 'true');
}
return response;
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Middleware Matching & Routing Reference:

| **API / Method** | **Purpose** | **Browser URL Behavior** | **Typical Use Case** |
| --- | --- | --- | --- |
| NextResponse.next() | Continues request pipeline | Unchanged | Header/Cookie injection, telemetry |
| NextResponse.redirect(url) | Emits 307 / 308 HTTP redirect | Updates to new URL | Unauthenticated login redirects |
| NextResponse.rewrite(url) | Proxies content from a different path | Unchanged | Multi-tenancy, A/B split testing |
| req.cookies.get(name) | Reads incoming request cookie | N/A | Session token inspection |
| res.cookies.set(name, val) | Sets outgoing response cookie | N/A | Session refresh, A/B bucket tagging |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global SaaS Edge Multi-Tenant & Security Architecture

Design an enterprise-scale Edge routing architecture for a multi-tenant platform serving 100,000 subdomains:

**Requirements**:

1.  Detail how Edge Middleware handles:

    - Dynamic Custom Domains (e.g. analytics.customer.com -> /sites/[siteId]) using Edge key-value lookup caches.

    - Bot & Scraping Detection (identifying malicious User-Agents and IP spikes).

    - Distributed Rate Limiting via Redis / Upstash with minimal latency impact ($<10\text{ms}$).

2.  Formulate a fail-open vs fail-closed security policy if the Edge rate limiting service experiences an outage.

3.  Design downstream Server Component context extraction for multi-tenant database partitioning.

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **Edge Security & Routing Guard** in Next.js Middleware (middleware.ts):

**Requirements**:

1.  Implement a pipeline router executing the following stages in order:

    - **Rate Limiting**: Sliding Window counter via Upstash Redis REST API (max 20 requests per 10 seconds per IP).

    - **Edge Auth Verification**: Verifies JWT using jose library, injecting x-user-id and x-tenant-id into request headers.

    - **Subdomain Multi-Tenant Rewriting**: Rewrites [tenant].domain.com/dashboard to /app/tenants/[tenant]/dashboard.

2.  Ensure public routes (/login, /api/health, /_next/static, /favicon.ico) bypass authentication with strict regex matchers.

3.  Include unit tests simulating:

    - 429 Too Many Requests response with standard Retry-After header when rate limit is exceeded.

    - 307 Redirect to /login when JWT token is expired.

    - Correct internal URL rewriting for multi-tenant subdomains.
