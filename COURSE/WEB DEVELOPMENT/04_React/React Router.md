---
tags:
- react
- routing
- navigation
---
# React Router

## What's the Actual Use?
React Router is the standard library for routing in React. It enables "client-side routing," allowing your application to navigate between different pages/views without the entire browser refreshing, creating a smooth, app-like experience.

## Real-Life Analogy
Think of your React app as a large museum. Without a router, you’d have to leave the building and re-enter through a different door every time you wanted to see a new exhibit. With React Router, you stay inside the museum and simply walk into different rooms (components) as the museum guide (the Router) updates your location and what you see.

## Other Common Use Cases
- Implementing navigation bars and sidebars
- Handling dynamic routes (e.g., `/profile/:id`)
- Protecting specific routes from unauthorized users (Private Routes)

## Documentation & Code
The most common implementation uses `BrowserRouter`, `Routes`, and `Route`.

```jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function Home() { return <h1>Home Page</h1>; }
function About() { return <h1>About Page</h1>; }

export default function App() {
  return (
    <BrowserRouter>
      <nav>
        {/* Use Link instead of <a href> to prevent page reloads */}
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        {/* Dynamic route example */}
        <Route path="/user/:username" element={<UserProfile />} />
      </Routes>
    </BrowserRouter>
  );
}
```