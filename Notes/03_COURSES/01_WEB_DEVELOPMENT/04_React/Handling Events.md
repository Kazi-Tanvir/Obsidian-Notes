---
tags:
- react
- events
- interaction
---
# Handling Events

## What's the Actual Use?
Handling events in React allows you to respond to user interactions like clicks, typing, form submissions, and mouse movements. React uses a synthetic event system that normalizes events to work consistently across all browsers.

## Other Common Use Cases
- Capturing user input in text fields (`onChange`)
- Submitting forms and preventing the default page reload (`onSubmit`)
- Triggering state updates or API calls on button clicks (`onClick`)

## Documentation & Code
React events are named using camelCase, rather than lowercase (e.g., `onClick` instead of `onclick`). You pass a function reference as the event handler, not a string.

```jsx
import { useState } from 'react';

export default function FormComponent() {
  const [inputValue, setInputValue] = useState('');

  // Event handler for typing
  const handleChange = (event) => {
    // Access the element that triggered the event via event.target
    setInputValue(event.target.value);
  };

  // Event handler for submission
  const handleSubmit = (event) => {
    // Prevent the browser from refreshing the page
    event.preventDefault();
    console.log(`Submitted value: ${inputValue}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={inputValue} 
        onChange={handleChange} 
        placeholder="Type here..."
      />
      {/* Clicking this triggers the form's onSubmit */}
      <button type="submit">Submit</button>

      {/* Inline arrow function for simple events */}
      <button 
        type="button" 
        onClick={() => setInputValue('')}
      >
        Clear
      </button>
    </form>
  );
}
```