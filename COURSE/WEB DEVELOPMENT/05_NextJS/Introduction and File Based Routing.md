---
tags:
- nextjs
- routing
- fullstack
---
# Introduction and File Based Routing

## What's the Actual Use?
Next.js is a React framework that simplifies building production-ready apps with features like Server-Side Rendering (SSR) and File-Based Routing. Instead of using a library like React Router, you define your pages by simply creating files inside the `app` or `pages` directory.

## Real-Life Analogy
Think of a traditional React app like a custom-built house where you have to manually wire every light switch to its bulb (React Router). Next.js is like a "Smart Home" kit where the wiring is already built into the walls; if you put a light in the "Kitchen" room, it automatically knows it belongs to the `/kitchen` route.

## Other Common Use Cases
- SEO-focused websites (Blogs, E-commerce)
- Fast-loading landing pages
- Building full-stack apps with integrated APIs

## Documentation & Code
In the modern Next.js `app` router, folders define paths, and `page.js` files define the UI.

```text
app/
├── layout.js      (Shared UI for all routes)
├── page.js        (The route: /)
├── about/
│   └── page.js    (The route: /about)
└── blog/
    ├── page.js    (The route: /blog)
    └── [id]/
        └── page.js (Dynamic route: /blog/1, /blog/abc)
```

```jsx
// app/about/page.js
export default function About() {
  return <h1>About Us</h1>;
}
```