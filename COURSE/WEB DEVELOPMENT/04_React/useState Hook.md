---
tags:
- react
- hooks
- state
---
# useState Hook

## What's the Actual Use?
The `useState` hook allows functional components in React to hold and update their own local state. When state changes, React automatically re-renders the component to reflect the new data on the screen.

## Real-Life Analogy
Imagine a light switch with a digital counter. `useState` is the memory chip that remembers the current number. Every time you flip the switch (trigger the state setter function), the chip updates the number, and the digital display (the React component) instantly updates to show the new value.

## Other Common Use Cases
- Managing form input values as the user types
- Toggling UI elements (e.g., opening/closing a modal or dropdown)
- Keeping track of scores, counters, or selections

## Documentation & Code
`useState` returns an array with exactly two items: the current state value, and a function to update it.

```jsx
import { useState } from 'react';

export default function Counter() {
  // Declare a state variable 'count', initialized to 0
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    // Update state based on previous state
    setCount((prevCount) => prevCount + 1);
  };

  return (
    <div>
      <p>Current Count: {count}</p>
      <button onClick={handleIncrement}>Increase</button>
      {/* Direct update example */}
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```