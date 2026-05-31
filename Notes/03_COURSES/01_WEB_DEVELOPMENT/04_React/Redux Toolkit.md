---
tags:
- react
- state-management
- redux
---
# Redux Toolkit

## What's the Actual Use?
Redux Toolkit (RTK) is the official, recommended way to write Redux logic. It provides a centralized "store" for application state, making it predictable and easier to debug, especially in large-scale applications where many components need access to the same data.

## Real-Life Analogy
Imagine a busy restaurant. Without Redux, waiters (components) have to run around asking each other who has the salt or where the orders are. With Redux, there is a central "Order Board" (The Store). Every waiter checks the board to see the status, and only the authorized "Head Chef" (Reducers) can change the board based on a "Ticket" (Actions).

## Other Common Use Cases
- Storing complex user session and authentication data
- Syncing a shopping cart across multiple pages
- Caching API data to prevent redundant network requests

## Documentation & Code
RTK uses `configureStore` to create the store and `createSlice` to handle logic.

```javascript
// 1. Create a "Slice" of state
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; },
    decrement: (state) => { state.value -= 1; },
  },
});

// 2. Export actions for components to use
export const { increment, decrement } = counterSlice.actions;

// 3. Configure the central Store
export const store = configureStore({
  reducer: {
    counter: counterSlice.reducer,
  },
});

// --- Usage in a Component ---
// import { useSelector, useDispatch } from 'react-redux';
// const count = useSelector((state) => state.counter.value);
// const dispatch = useDispatch();
// <button onClick={() => dispatch(increment())}>+</button>
```