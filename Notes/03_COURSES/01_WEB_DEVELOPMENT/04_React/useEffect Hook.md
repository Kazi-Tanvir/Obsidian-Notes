---
tags:
- react
- hooks
- lifecycle
- side-effects
---
# useEffect Hook

## What's the Actual Use?
The `useEffect` hook lets you perform side effects in functional components. A side effect is any operation that reaches outside the React component, such as fetching data from an API, directly updating the DOM, or setting up subscriptions and timers.

## Real-Life Analogy
Think of a component as a chef cooking a meal (rendering UI). `useEffect` is the chef asking an assistant to go outside the kitchen to buy a specific missing ingredient (fetching data) or setting a kitchen timer (setTimeout). The dependency array is the chef's instruction: "Only go to the store if the recipe changes" or "Only go once when we first open."

## Other Common Use Cases
- Fetching data from an external API on component mount
- Setting up and tearing down event listeners (e.g., window resize)
- Syncing React state with `localStorage`

## Documentation & Code
`useEffect` takes a callback function and an optional dependency array. The cleanup function handles unmounting.

```jsx
import { useState, useEffect } from 'react';

export default function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // 1. The Effect: Fetch data when component mounts or userId changes
    let isMounted = true;
    
    fetch(`https://api.example.com/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        if (isMounted) setUser(data);
      });

    // 2. The Cleanup: Runs before the component unmounts or before the next effect runs
    return () => {
      isMounted = false; // Prevent state updates on unmounted component
    };
  }, [userId]); // 3. Dependency Array: Re-run only if userId changes

  if (!user) return <p>Loading...</p>;
  return <div>{user.name}</div>;
}
```