---
tags:
- react
- components
- jsx
- props
---
# Components, Props, and JSX

## What's the Actual Use?
Components are independent, reusable pieces of UI that manage their own rendering. JSX is a syntax extension for React that allows writing HTML-like code directly inside JavaScript. Props (properties) are the mechanism for passing data down from a parent component to a child component.

## Real-Life Analogy
A component is like a standardized blueprint for a house. Props are the custom choices you pass to the builder—like "blue paint" or "3 bedrooms." No matter what props you pass, the house still gets built according to the core blueprint.

## Other Common Use Cases
- Creating reusable UI libraries (Buttons, Cards, Modals)
- Passing dynamic data from a central state to view layers
- Structuring complex UIs into maintainable, bite-sized files

## Documentation & Code
JSX allows embedding JavaScript expressions using curly braces `{}`. Props are passed as attributes and received as an object in the component's parameters.

```jsx
// 1. A reusable child component receiving props
function Greeting({ name, role }) {
  // JSX: combining HTML and JavaScript variables
  return (
    <div className="user-card">
      <h2>Hello, {name}!</h2>
      <p>Your role is: {role}</p>
    </div>
  );
}

// 2. A parent component passing props
export default function App() {
  return (
    <main>
      <h1>Dashboard</h1>
      {/* Reusing the component with different props */}
      <Greeting name="Alice" role="Admin" />
      <Greeting name="Bob" role="User" />
    </main>
  );
}
```