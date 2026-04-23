---
tags:
- nextjs
- rendering
- performance
---
# SSR, SSG, and ISR

## What's the Actual Use?
These are three different ways Next.js can render your content to balance speed and data freshness. 
- **SSG (Static Site Generation):** Pre-builds pages at build time (Fastest).
- **SSR (Server-Side Rendering):** Generates a page on every request (Freshest data).
- **ISR (Incremental Static Regeneration):** Updates static pages in the background after they are built.

## Real-Life Analogy
- **SSG:** Buying a pre-packaged sandwich at a deli (Instant, but made earlier).
- **SSR:** Ordering a steak at a restaurant (Made fresh for you, but you have to wait).
- **ISR:** A vending machine that gets refilled with fresh sandwiches every hour (Fast like the deli, but updated regularly).

## Other Common Use Cases
- **SSG:** Marketing pages, documentation, blog posts.
- **SSR:** Personalized dashboards, search results, checkout pages.
- **ISR:** Product catalogs where prices or stock levels change occasionally.

## Documentation & Code
In the `app` router, rendering is controlled by the `fetch` options and the `revalidate` variable.

```javascript
// 1. SSG (Default behavior for fetch)
const data = await fetch('https://api.example.com/data');

// 2. SSR (Force dynamic rendering)
const data = await fetch('https://api.example.com/data', { cache: 'no-store' });

// 3. ISR (Revalidate every 60 seconds)
const data = await fetch('https://api.example.com/data', { 
  next: { revalidate: 60 } 
});

// Alternative: Export a segment config variable
export const revalidate = 3600; // Revalidate the whole page every hour
```