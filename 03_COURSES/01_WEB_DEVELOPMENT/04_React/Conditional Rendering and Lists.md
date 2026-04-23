---
tags:
- react
- jsx
- lists
- conditionals
---
# Conditional Rendering and Lists

## What's the Actual Use?
Conditional rendering allows you to display different UI elements based on specific states or conditions (like showing a login button vs. a user profile). Rendering lists is the process of mapping over arrays of data to dynamically generate repeating HTML elements.

## Other Common Use Cases
- Displaying a loading spinner while waiting for an API response
- Showing error messages if a form validation fails
- Rendering e-commerce product grids or social media feeds from an array of objects

## Documentation & Code
Use JavaScript logical operators (`&&`, `? :`) for conditions, and the `.map()` array method for lists. Always provide a unique `key` prop when mapping lists to help React optimize updates.

```jsx
export default function Dashboard({ isLoggedIn, userRole, products }) {
  return (
    <div>
      {/* 1. Conditional Rendering: Ternary Operator (if/else) */}
      {isLoggedIn ? (
        <h1>Welcome back!</h1>
      ) : (
        <button>Please Log In</button>
      )}

      {/* 2. Conditional Rendering: Logical AND (if true, do this) */}
      {userRole === 'admin' && (
        <button className="admin-btn">Edit Dashboard</button>
      )}

      {/* 3. Rendering Lists */}
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          // The 'key' must be unique and stable (like an ID), not an array index
          <li key={product.id}>
            {product.name} - ${product.price}
          </li>
        ))}
      </ul>
    </div>
  );
}
```