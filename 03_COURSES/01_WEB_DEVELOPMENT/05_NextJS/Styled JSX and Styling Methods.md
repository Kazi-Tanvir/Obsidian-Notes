---
tags:
- nextjs
- css
- styling
---
# Styled JSX and Styling Methods

## What's the Actual Use?
Next.js supports multiple ways to style your application, ranging from traditional CSS files to modern solutions like CSS Modules (scoped styles), Tailwind CSS (utility-first), and Styled JSX (CSS-in-JS). This flexibility allows you to choose the best tool for your project's complexity.

## Other Common Use Cases
- **CSS Modules:** Preventing CSS class name collisions in large projects.
- **Tailwind CSS:** Rapidly prototyping and building responsive UIs without leaving your HTML.
- **Styled JSX:** Keeping component-specific styles directly inside the component file for better portability.

## Documentation & Code
CSS Modules are the default recommended way for standard CSS in Next.js.

```jsx
// 1. CSS MODULES (filename must end in .module.css)
import styles from './Button.module.css';

export function Button() {
  // Styles are scoped automatically: 'styles.btn' becomes a unique class
  return <button className={styles.btn}>Click Me</button>;
}

// 2. STYLED JSX (Built into Next.js)
export function Card() {
  return (
    <div className="card">
      <h2>Hello</h2>
      <style jsx>{`
        .card { padding: 20px; background: #eee; }
        h2 { color: blue; }
      `}</style>
    </div>
  );
}
```