---
tags:
- nextjs
- performance
- server-components
---
# Server Components vs Client Components

## What's the Actual Use?
Next.js allows you to split your app into Server Components (rendered on the server for speed and SEO) and Client Components (rendered in the browser for interactivity). This optimization reduces the amount of JavaScript sent to the user, making pages load faster.

## Real-Life Analogy
A Server Component is like a pre-cooked meal delivered to your door—you just eat it (view it). A Client Component is like a "meal kit" where you have to do some work in your own kitchen (browser) to make it edible (interactive), like clicking buttons or filling out forms.

## Other Common Use Cases
- **Server:** Fetching sensitive data from a database (hides API keys).
- **Client:** Using hooks like `useState`, `useEffect`, or browser APIs like `window`.
- **Server:** Rendering static content like a blog post or footer.

## Documentation & Code
By default, all components in the `app` router are Server Components. To make one a Client Component, add the `"use client"` directive at the top.

```jsx
// 1. SERVER COMPONENT (Default)
// Ideal for fetching data directly from DB
async function UserList() {
  const users = await db.user.findMany(); // Direct DB access!
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

// 2. CLIENT COMPONENT
"use client"; // Required for interactivity
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```