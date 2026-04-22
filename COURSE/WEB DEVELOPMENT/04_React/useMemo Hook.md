---
tags:
- react
- hooks
- performance
- memoization
---
# useMemo Hook

## What's the Actual Use?
The `useMemo` hook is a performance optimization tool that caches (memoizes) the result of an expensive calculation. It only recalculates the value when one of its dependencies changes, preventing slow operations from running on every single render.

## Real-Life Analogy
Imagine you have to calculate a massive math equation by hand (e.g., `14592 * 8371`). It takes you 5 minutes. If someone asks you for the answer again, you don't recalculate it; you read the cached answer off your notepad (`useMemo`). You only do the math again if they give you different numbers (the dependencies change).

## Other Common Use Cases
- Filtering or sorting large lists or arrays of data
- Processing complex derived state (e.g., generating chart data from raw API responses)
- Preventing expensive child components from re-rendering unnecessarily

## Documentation & Code
`useMemo` returns a memoized value. It takes a "create" function and an array of dependencies.

```jsx
import { useState, useMemo } from 'react';

export default function ExpensiveComponent({ items }) {
  const [filterQuery, setFilterQuery] = useState('');
  const [theme, setTheme] = useState('light');

  // The filtering logic only runs when 'items' or 'filterQuery' changes.
  // It will NOT run when 'theme' changes, saving processing time.
  const filteredItems = useMemo(() => {
    console.log("Running expensive filter operation...");
    return items.filter(item => item.name.includes(filterQuery));
  }, [items, filterQuery]); 

  return (
    <div className={`app-${theme}`}>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
      
      <input 
        value={filterQuery} 
        onChange={(e) => setFilterQuery(e.target.value)} 
        placeholder="Search..."
      />

      <ul>
        {filteredItems.map(item => <li key={item.id}>{item.name}</li>)}
      </ul>
    </div>
  );
}
```