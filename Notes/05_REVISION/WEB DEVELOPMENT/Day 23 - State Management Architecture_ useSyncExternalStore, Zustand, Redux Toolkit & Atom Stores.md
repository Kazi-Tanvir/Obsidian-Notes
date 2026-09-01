---
tags:
- frontend
- react
- state-management
- zustand
- redux
- useSyncExternalStore
- performance
- architecture
date: 2026-08-23
---

# Day 23 - State Management Architecture: useSyncExternalStore, Zustand, Redux Toolkit & Atom Stores

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Tearing Problem in Concurrent React

In React 18+ Concurrent Mode, React can pause, yield, and resume rendering to maintain responsive 60fps/120fps UI interactions.

If components read from an **external mutable store** (outside React's useState/useReducer tree) via standard useEffect subscriptions:

1.  Component A renders with external state value v1.

2.  React yields the main thread to handle an incoming WebSocket event.

3.  The WebSocket updates the external store to v2.

4.  React resumes rendering and renders Component B with external state value v2.

5.  Result: **Tearing** --- the same UI tree displays conflicting visual states simultaneously in a single frame.

[ Tearing Scenario ]:

Render Frame Start ────► Component A (Reads Store: v1)

│

▼ [Main thread yields: WebSocket mutates Store to v2]

│

Component B (Reads Store: v2) ────► Inconsistent Corrupted UI Render!

### 2. The useSyncExternalStore Hook Architecture

To fix tearing, React introduced useSyncExternalStore. It forces React to synchronously re-evaluate the snapshot whenever an external store emits an update during rendering, guaranteeing state consistency across concurrent slices.

```javascript
import { useSyncExternalStore } from 'react';
export function useStore<TState, TSelected>(
```

store: {

```javascript
subscribe: (listener: () => void) => () => void;
getSnapshot: () => TState;
getServerSnapshot?: () => TState;
```

},

selector: (state: TState) => TSelected

): TSelected {

```javascript
const getSnapshot = () => selector(store.getSnapshot());
return useSyncExternalStore(store.subscribe, getSnapshot, store.getServerSnapshot);
}
```

### 3. Global State Architectural Paradigms Compared

#### A. Centralized / Slice-Based Architecture (Zustand, Redux Toolkit)

- **Model**: Single source of truth tree.

- **Subscription Mechanism**: Selector functions ((state) => state.user.name) subscribe components only to the specific slices they read.

- **Why Zustand Outperforms Context**: React Context causes all consumer components to re-render whenever *any* value inside the context object changes. Zustand bypasses React Context entirely, using module-level closures and useSyncExternalStore for surgical re-renders.

```typescript
// Modern Zustand Store with Slice Pattern & Immer Middleware
import { create } from 'zustand';
import { immer } from 'zustand/middleware/immer';
interface UserSlice {
profile: { name: string; email: string };
updateEmail: (email: string) => void;
}
export const useAppStore = create<UserSlice>()(
```

immer((set) => ({

profile: { name: "Tanvir", email: "tanvir@example.com" },

updateEmail: (newEmail) =>

set((state) => {

```javascript
state.profile.email = newEmail; // Mutative syntax converted to immutable update via Immer
}),
}))
);
```

#### B. Atomic / Bottom-Up Architecture (Jotai, Recoil)

- **Model**: State is decomposed into isolated, composable primitives called **Atoms**.

- **Dependency Graph**: Components only subscribe to individual atoms. Derived state atoms (read getters) compute transformations automatically without triggering unnecessary parent re-renders.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### State Management Paradigms Comparison:

| **Feature / Metric** | **React Context API** | **Zustand** | **Redux Toolkit (RTK)** | **Jotai / Recoil** |
| --- | --- | --- | --- | --- |
| **Architecture** | Component Tree Provider | External Module Store | External Redux Store | Decentralized Atoms |
| **Re-render Scope** | All consumers re-render | Only subscribed selectors | Only subscribed selectors | Only subscribed atoms |
| **Boilerplate** | Low | Minimal | Moderate (Slices/Thunks) | Minimal |
| **Async Handling** | Manual in useEffect | Native inside actions | createAsyncThunk / RTK Query | Async Atoms & Suspense |
| **Concurrent Safe** | Yes (inside React) | Yes (useSyncExternalStore) | Yes (useSyncExternalStore) | Yes (useSyncExternalStore) |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Multi-Tab Synced Document State Architecture

Design a real-time collaborative document state architecture for a multi-tab browser application.

**Requirements**:

1.  Detail how local client mutations synchronize across multiple open browser tabs using BroadcastChannel and IndexedDB.

2.  Formulate a conflict resolution strategy (Last-Write-Wins timestamps vs CRDT vector clocks) when two tabs edit the same document offline.

3.  Design the React state layer using useSyncExternalStore so tab switches and background storage events update the active React view with zero tearing and zero lost focus states.

### Problem 2: End-to-End Code Implementation Challenge

Build a typed, dependency-free **Mini-Zustand Global State Store** library from scratch in TypeScript:

**Requirements**:

1.  Implement createStore<T>(initializer) returning an external store with:

    - getState(): Returns current immutable state.

    - setState(partialOrFn): Updates state and notifies subscribers.

    - subscribe(listener): Subscribes to changes and returns an unsubscription function.

2.  Implement a React Hook wrapper useCustomStore(store, selector, equalityFn?) powered by useSyncExternalStore that only re-renders the component if the selected state slice changes (using shallow equality checks).

3.  Implement a built-in devtools middleware that logs state transitions with timestamp and action names to the console.

4.  Provide unit tests verifying:

    - Component does not re-render when an unselected slice changes.

    - Unsubscription cleans up listeners completely.
