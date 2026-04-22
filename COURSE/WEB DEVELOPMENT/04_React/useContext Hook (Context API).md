---
tags:
- react
- hooks
- state-management
- context
---
# useContext Hook (Context API)

## What's the Actual Use?
The `useContext` hook allows React components to read and subscribe to global data from a Context without having to manually pass props down through every intermediate component (a problem known as "prop drilling").

## Real-Life Analogy
Imagine a large office building. Prop drilling is like handing a physical memo to a manager, who hands it to a supervisor, who hands it to a worker. Context is like the building's PA system: the CEO broadcasts the message, and any worker with a radio (`useContext`) can tune in and hear it instantly, bypassing the middle managers entirely.

## Other Common Use Cases
- Managing global theme preferences (Light/Dark mode)
- Storing the current authenticated user's session data
- Managing application-wide language/localization settings

## Documentation & Code
You must first create a context, provide it via a wrapper component, and then consume it in children.

```jsx
import { createContext, useContext, useState } from 'react';

// 1. Create the Context
const ThemeContext = createContext();

// 2. Create a Provider Component (usually at the top level of your app)
export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prev => (prev === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// 3. Consume the Context in a deeply nested component
export function ThemeButton() {
  // Use the hook to extract the values passed to the Provider
  const { theme, toggleTheme } = useContext(ThemeContext);

  return (
    <button 
      onClick={toggleTheme}
      style={{ background: theme === 'dark' ? '#333' : '#FFF' }}
    >
      Toggle to {theme === 'dark' ? 'Light' : 'Dark'} Mode
    </button>
  );
}
```