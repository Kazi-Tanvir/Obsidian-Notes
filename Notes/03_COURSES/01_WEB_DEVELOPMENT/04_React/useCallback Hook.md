---
tags:
- react
- hooks
- performance
- memoization
---
# useCallback Hook

## What's the Actual Use?
The `useCallback` hook caches a function definition between renders. It is primarily used to prevent unnecessary re-renders of child components that rely on referential equality to determine if they should update.

## Real-Life Analogy
Imagine a manager handing out a task list to an employee. If the manager types out a brand-new, identical copy of the list every hour, the employee gets confused and stops working to read it (a re-render). `useCallback` is the manager laminating the original list and pointing to it; the employee knows it hasn't changed, so they keep working without interruption.

## Other Common Use Cases
- Passing callback functions to heavily optimized child components (using `React.memo`)
- Debouncing or throttling functions inside functional components
- Keeping functions stable when they are used as dependencies in `useEffect`

## Documentation & Code
`useCallback` returns a memoized version of the callback that only changes if one of the dependencies has changed. 

```jsx
import { useState, useCallback, memo } from 'react';

// A child component optimized with React.memo
// It only re-renders if its props change.
const Button = memo(({ onClick, children }) => {
  console.log(`Rendering button - ${children}`);
  return <button onClick={onClick}>{children}</button>;
});

export default function ParentComponent() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');

  // Without useCallback, this function is re-created on EVERY render.
  // By wrapping it, the reference stays the same unless 'count' changes.
  const incrementCount = useCallback(() => {
    setCount((prev) => prev + 1);
  }, []); // Empty array means the function reference NEVER changes

  return (
    <div>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      {/* 
        Because incrementCount is memoized, typing in the input (changing 'text') 
        will NOT cause the Button component to re-render.
      */}
      <Button onClick={incrementCount}>Increment: {count}</Button>
    </div>
  );
}
```