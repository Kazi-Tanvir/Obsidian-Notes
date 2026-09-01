tags:

- frontend

- nextjs

- react

- app-router

- isr

- ppr

- caching

- streaming

- performance date: 2026-08-25

# Day 25 - Next.js Rendering & Caching: SSG, ISR, Partial Prerendering (PPR) & Suspense Streaming

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Rendering Paradigms in Next.js App Router

Next.js App Router unifies multiple rendering and caching paradigms into a hybrid, composable architecture.

\[ Static Prerendering (SSG) \] ───► Fast Edge Delivery (Zero Server Compute)

\[ Incremental Regeneration (ISR) \] ──► Background On-Demand / Time-based Revalidation

\[ Dynamic Server Rendering \] ────► Per-request rendering for user-specific data

\[ Partial Prerendering (PPR) \] ──► Static Shell + Streaming Dynamic Holes in ONE request

### 2. Deep Dive into Rendering Strategies

#### A. Static Site Generation (SSG) & Prerendering

Routes without dynamic functions are automatically rendered at build time and cached globally on CDN Edge networks.

- generateStaticParams(): Statically generates dynamic route segments (e.g. /posts/\[id\]) at build time.

#### B. Incremental Static Regeneration (ISR)

Enables updating static pages in the background without rebuilding the entire website.

- **Time-based ISR**: fetch(url, { next: { revalidate: 60 } }) or export const revalidate = 60;.

- **On-Demand Tag-based ISR**: revalidateTag(\"products\") or revalidatePath(\"/products\") inside Server Actions.

// Example: ISR with On-Demand Revalidation

export async function getProduct(id: string) {

const res = await fetch(\`https://api.example.com/products/\${id}\`, {

next: { tags: \[\`product-\${id}\`, \'products\'\] },

});

return res.json();

}

// Server Action triggering instant cache invalidation

\'use server\';

import { revalidateTag } from \'next/cache\';

export async function updateProductPrice(productId: string, newPrice: number) {

await db.product.update({ where: { id: productId }, data: { price: newPrice } });

revalidateTag(\`product-\${productId}\`); // Purges cache instantly across all CDN nodes

}

#### C. Partial Prerendering (PPR) & React Suspense Streaming

PPR combines the ultra-fast TTFB of static websites with the flexibility of dynamic rendering.

1.  The static HTML shell (Navbar, Sidebar, Layout skeleton) is prerendered at build time and served immediately from the Edge CDN.

2.  Inside the same HTTP response, dynamic server components wrapped in \<Suspense\> stream in parallel as chunked HTML over HTTP/2 once data fetching completes.

// app/dashboard/page.tsx (Partial Prerendering Pattern)

import { Suspense } from \'react\';

import { StaticSidebar } from \'@/components/Sidebar\';

import { DynamicUserFeed, FeedSkeleton } from \'@/components/DynamicUserFeed\';

export const experimental_ppr = true; // Enables Partial Prerendering

export default function DashboardPage() {

return (

\<div className=\"layout\"\>

{/\* 1. Prerendered Static Shell (Served instantly from Edge) \*/}

\<StaticSidebar /\>

\<main\>

\<h1\>Welcome to Dashboard\</h1\>

{/\* 2. Dynamic Streaming Hole (Streamed into the response) \*/}

\<Suspense fallback={\<FeedSkeleton /\>}\>

\<DynamicUserFeed /\>

\</Suspense\>

\</main\>

\</div\>

);

}

### 3. The 4 Next.js Caching Layers

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Layer**                 **Where it Lives**            **What it Caches**                     **Lifespan / Invalidation**
  ------------------------- ----------------------------- -------------------------------------- -------------------------------------------------------------------
  **Request Memoization**   Server Memory (per request)   Return values of fetch GET requests    Single request lifecycle (React Component Tree render)

  **Data Cache**            Server Persistent Storage     HTTP fetch responses across requests   Persistent until revalidateTag or time TTL expires

  **Full Route Cache**      Server Persistent Storage     Rendered HTML & RSC Payload            Persistent across user visits; cleared on Data Cache invalidation

  **Router Cache**          Browser Memory                Prefetched & visited RSC payloads      Session / 30s dynamic, 5min static
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Route Segment Config Options Reference:

// Segment-level Cache Controls

export const dynamic = \'auto\' \| \'force-dynamic\' \| \'error\' \| \'force-static\';

export const dynamicParams = true \| false;

export const revalidate = false \| 0 \| number; // 0 = dynamic, number = seconds

export const fetchCache = \'auto\' \| \'default-cache\' \| \'only-cache\' \| \'force-cache\' \| \'force-no-store\';

export const runtime = \'nodejs\' \| \'edge\';

export const preferredRegion = \'auto\' \| \'home\' \| \'edge\';

### Cache Invalidation APIs:

import { revalidatePath, revalidateTag, unstable_noStore as noStore } from \'next/cache\';

// Purge specific cache tag

revalidateTag(\'inventory-tag\');

// Purge entire route path

revalidatePath(\'/blog/\[slug\]\', \'page\');

// Opt out of Data Cache inside component

noStore();

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: High-Traffic News Media Portal Architecture

Design an enterprise-scale architecture for a global breaking-news portal handling 50M monthly visits:

**Requirements**:

1.  Formulate the rendering strategy for:

    - Breaking News Headlines (Dynamic / Sub-second cache invalidation).

    - Evergreen Articles (ISR with 24-hour TTL and on-demand editor revalidation).

    - Personalized User Subscription & Paywall Banners (Partial Prerendering with Suspense streaming).

2.  Detail how multi-region Edge CDN caching interacts with revalidateTag when journalists publish emergency article updates.

3.  Design the fallback UI strategy and error boundary architecture to prevent dynamic third-party analytics/ad widgets from breaking static article rendering.

### Problem 2: End-to-End Code Implementation Challenge

Build an ISR & PPR-Optimized **E-Commerce Product Page** in Next.js App Router:

**Requirements**:

1.  Implement app/products/\[id\]/page.tsx with:

    - generateStaticParams() to prerender top 100 featured products at build time.

    - Static product details (Title, Images, Description) loaded with tagged data caching (next: { tags: \[\'product-{id}\'\] }).

    - Dynamic real-time inventory and pricing status wrapped in a \<Suspense\> boundary with a custom skeleton loader.

2.  Implement a Server Action syncInventoryAndNotify(productId: string, stock: number) that updates the database and triggers on-demand cache tag revalidation (revalidateTag).

3.  Include error boundary handling with an error.tsx component that allows users to retry failed dynamic inventory fetches without reloading the static page shell.
