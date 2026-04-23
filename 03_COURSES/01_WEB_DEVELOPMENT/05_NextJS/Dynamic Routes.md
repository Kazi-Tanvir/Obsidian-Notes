---
tags:
- nextjs
- routing
- dynamic-routes
---
# Dynamic Routes

## What's the Actual Use?
Dynamic Routes allow you to create pages where the actual path isn't known ahead of time, such as a blog post (`/blog/my-first-post`) or a user profile (`/user/john_doe`). You define a placeholder in the file system, and Next.js fills it with the actual data from the URL.

## Real-Life Analogy
Imagine a hotel with 100 rooms. Instead of building a unique blueprint for every single room, the architect creates one "Generic Room" blueprint. When a guest arrives, the hotel assigns them a room number (the dynamic ID), and that generic blueprint becomes "Room 101" or "Room 205" for that guest.

## Other Common Use Cases
- E-commerce product pages (`/products/[slug]`)
- Documentation sections (`/docs/[category]/[page]`)
- Search results pages with dynamic queries

## Documentation & Code
In the `app` router, you use square brackets `[]` in the folder name to create a dynamic segment.

```jsx
// app/blog/[id]/page.js

export default function Post({ params }) {
  // 'params' contains the dynamic segments from the URL
  const { id } = params;

  return (
    <div>
      <h1>Viewing Post: {id}</h1>
      <p>This content was loaded dynamically for ID: {id}</p>
    </div>
  );
}
```