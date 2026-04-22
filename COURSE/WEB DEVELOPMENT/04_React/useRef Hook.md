---
tags:
- react
- hooks
- refs
- dom
---
# useRef Hook

## What's the Actual Use?
The `useRef` hook allows you to persist a mutable value across renders without triggering a component re-render when the value changes. It is most commonly used to directly access and interact with a specific DOM element.

## Real-Life Analogy
If `useState` is a public bulletin board where changing a notice causes everyone to stop and look (a re-render), `useRef` is a personal notebook in your pocket. You can jot things down and update them constantly, but nobody else in the room (the React component) notices or reacts to you doing it.

## Other Common Use Cases
- Focusing an input element automatically when a page loads
- Storing mutable interval IDs or timer references for cleanup
- Tracking previous state values without causing infinite render loops

## Documentation & Code
`useRef` returns a mutable object with a single `.current` property.

```jsx
import { useRef } from 'react';

export default function FocusInput() {
  // Create a reference to attach to a DOM element
  const inputRef = useRef(null);
  // Create a reference to store a mutable value (won't trigger re-render)
  const renderCount = useRef(0);

  renderCount.current += 1;

  const handleFocus = () => {
    // Directly access the DOM node via .current and call standard DOM methods
    inputRef.current.focus();
    inputRef.current.style.border = '2px solid red';
  };

  return (
    <div>
      <p>Component has rendered {renderCount.current} times.</p>
      {/* Attach the ref to the specific React element */}
      <input ref={inputRef} type="text" placeholder="Click button to focus me" />
      <button onClick={handleFocus}>Focus the Input</button>
    </div>
  );
}
```