tags:

- frontend

- nextjs

- react

- rsc

- app-router

- server-components date: 2026-08-08

# Day 8 - Next.js App Router Architecture, Server Components (RSC) vs Client Components & Data Fetching

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Next.js App Router & Special File Conventions

The App Router (app/ directory) uses file-system based routing leveraging React Server Components (RSC) primitives. Special file conventions create nested layout hierarchies and UI boundaries:

- page.tsx: Defines the unique UI for a route.

- layout.tsx: Shared UI that preserves state and avoids re-renders across child navigations.

- loading.tsx: Automatically wraps page.tsx in a React Suspense boundary for instant streaming UI.

- error.tsx: React Error Boundary (\'use client\') for localized error catching.

- not-found.tsx: Custom 404 UI triggered by notFound().

- route.ts: Server-side API endpoints (GET, POST, PUT, DELETE).

### 2. React Server Components (RSC) vs Client Components (\'use client\')

In Next.js, all components inside the app/ directory are **React Server Components** by default unless explicitly opted into client hydration via \'use client\'.

  ----------------------------------------------------------------------------------------------------------------------
  **Characteristic**          **React Server Components (RSC)**         **Client Components (\'use client\')**
  --------------------------- ----------------------------------------- ------------------------------------------------
  **Execution Environment**   Server-only (never executes in browser)   Rendered on server, Hydrated in browser

  **Bundle Impact**           **0 KB JS Bundle**                        Added to Client JS Bundle

  **Data Access**             Direct DB / File System access            Browser APIs (window, localStorage)

  **React Hooks**             Unsupported (useState, useEffect)         Supported (useState, useReducer, custom hooks)

  **Interactivity**           No event listeners (onClick)              Full event listener interactivity
  ----------------------------------------------------------------------------------------------------------------------

#### Composition Boundary Rule:

You cannot import a Server Component into a Client Component directly. However, you can pass a Server Component as a children prop into a Client Component wrapper.

// Correct Composition Pattern

// \'use client\'

export function ClientModalWrapper({ children }: { children: React.ReactNode }) {

const \[isOpen, setIsOpen\] = useState(false);

return (

\<div\>

\<button onClick={() =\> setIsOpen(true)}\>Open\</button\>

{isOpen && \<div className=\"modal\"\>{children}\</div\>}

\</div\>

);

}

// Server Component Page (page.tsx)

import { ClientModalWrapper } from \'./ClientModalWrapper\';

import { HeavyServerDataView } from \'./HeavyServerDataView\';

export default async function Page() {

return (

\<ClientModalWrapper\>

\<HeavyServerDataView /\> {/\* Passed as children prop! \*/}

\</ClientModalWrapper\>

);

}

### 3. Caching & Data Fetching Paradigm

Next.js extends native fetch API to provide fine-grained control over four distinct caching layers:

1.  **Request Memoization**: Deduplicates identical fetch requests within a single render pass.

2.  **Data Cache**: Persists fetched data across server requests (fetch(url, { cache: \'force-cache\' })).

3.  **Full Route Cache**: Caches HTML and RSC payload at build time or revalidation window.

4.  **Router Cache**: In-memory client-side cache storing route segments.

#### On-Demand Revalidation:

- revalidateTag(\'tag-name\'): Invalidates all cache entries tagged with next: { tags: \[\'tag-name\'\] }.

- revalidatePath(\'/dashboard\'): Purges cached route payload on demand (e.g. inside a Server Action).

## SECTION 2: DOCUMENTATION CHEAT SHEET

  ------------------------------------------------------------------------------------------------------------------------
  **Fetch / Caching Strategy**   **Code / Option**                                  **Behavior**
  ------------------------------ -------------------------------------------------- --------------------------------------
  **Static Data Fetching**       fetch(url, { cache: \'force-cache\' })             Caches indefinitely (SSG equivalent)

  **Dynamic Data Fetching**      fetch(url, { cache: \'no-store\' })                Fetches fresh on every request (SSR)

  **Time-based Revalidation**    fetch(url, { next: { revalidate: 3600 } })         Revalidates cache after 1 hour (ISR)

  **Tagged Revalidation**        fetch(url, { next: { tags: \[\'products\'\] } })   Tagged for on-demand invalidation

  **Dynamic Segment Option**     export const dynamic = \'force-dynamic\'           Forces route to execute dynamically
  ------------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Enterprise Dashboard Streaming Architecture)

Design a high-performance Next.js App Router Dashboard for an analytics platform fetching data from 4 slow microservices (User Analytics, Revenue, Server Health, Activity Logs).

**Requirements**:

1.  Demonstrate how sequential await calls create waterfall bottlenecks and how to resolve them with Promise.all and React Suspense streaming boundaries.

2.  Define loading.tsx and skeletal loading strategies for independent UI blocks.

3.  Architect an on-demand revalidation pipeline using Server Actions and revalidateTag.

### Problem 2: End-to-End Code Implementation Challenge

Build an **E-Commerce Product Catalog Page** in Next.js App Router (app/products/page.tsx).

**Requirements**:

1.  Server Component page that fetches product list from an API with tagged caching (next: { tags: \[\'products-list\'\] }).

2.  Client Component (FilterBar.tsx) that updates URL search parameters (?category=electronics&sort=price_asc) without full page refreshes using useRouter and useSearchParams.

3.  Server Component that reads searchParams prop to filter/sort database results.

4.  Provide a Server Action function refreshProductCache() that calls revalidateTag(\'products-list\') to purge cached catalog data upon admin edits.
