---
tags:
- nextjs
- layout
- ui
---
# Layouts

## What's the Actual Use?
Layouts are UI elements that are shared across multiple pages in your application. When you navigate between pages that share the same layout, the layout state is preserved, and the layout itself does not re-render, improving performance and user experience.

## Real-Life Analogy
A layout is like the frame and dashboard of a car. As you drive to different locations (navigate to different pages), the view out the window changes ( the page content), but your steering wheel, seats, and radio (the layout) stay exactly where they are.

## Other Common Use Cases
- Persistent navigation bars and footers
- Sidebar menus for dashboard sections
- Wrapping specific sections of the app with Context Providers (e.g., Theme, Auth)

## Documentation & Code
A layout accepts a `children` prop, which represents the pages or sub-layouts nested inside it.

```jsx
// app/layout.js (Root Layout - Required)
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <nav>
          <a href="/">Home</a>
          <a href="/about">About</a>
        </nav>
        
        {/* The specific page content will be injected here */}
        <main>{children}</main>
        
        <footer>© 2024 My App</footer>
      </body>
    </html>
  );
}
```