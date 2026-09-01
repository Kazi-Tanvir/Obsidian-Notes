tags:

- frontend

- react

- fiber

- concurrent-react

- performance

- architecture

- virtual-dom date: 2026-08-22

# Day 22 - Advanced React Internals: Fiber Architecture, Reconciliation & Concurrent Mode

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Evolution of the React Reconciler

Early versions of React (v15 and below) used the **Stack Reconciler**, which traversed the component tree recursively and synchronously. Once reconciliation began, the browser main thread was completely blocked until the entire tree finished rendering. If a tree was large, user keystrokes, animations, and scrolling stuttered (dropped frames below 60fps).

**React Fiber (v16+)** redesigned the core algorithm from synchronous recursion to an **incremental, cooperative unit-of-work scheduler**.

\[ Stack Reconciler \]:

Render Start ──────────────── Synchronous Recursive Walk (Blocks Main Thread) ────────────────► DOM Paint

\[ Fiber Reconciler \]:

Render Start ──► \[Work Slice 5ms\] ──► (Yield to Browser for Input/Paint) ──► \[Work Slice 5ms\] ──► Commit DOM

### 2. The Fiber Node Data Structure

A **Fiber** is a plain JavaScript object representing a unit of work and a 1-to-1 relationship with a component or DOM node:

interface FiberNode {

// Tree Structure Links (Linked List representation instead of recursive tree)

child: FiberNode \| null; // First child

sibling: FiberNode \| null; // Next sibling

return: FiberNode \| null; // Parent fiber

// Component Information

tag: WorkTag; // FunctionComponent, ClassComponent, HostComponent (DOM node)

type: any; // Component function or \'div\', \'span\'

key: null \| string;

// Props & State

pendingProps: any; // Incoming props to process

memoizedProps: any; // Props used to create last render

memoizedState: any; // State linked list (Hooks)

// Double Buffering & Effects

alternate: FiberNode \| null; // Pointer to corresponding Fiber in alternate tree

flags: Flags; // Placement, Update, Deletion side-effects

lanes: Lanes; // 32-bit bitmask indicating priority level

}

#### The Double Buffering Technique:

React maintains two Fiber trees simultaneously in memory:

1.  **Current Tree**: Reflects the nodes currently visible on the screen.

2.  **Work-In-Progress (WIP) Tree**: Built asynchronously in memory during rendering. Once complete, React swaps the root pointer (current = workInProgress) in a single \$O(1)\$ pointer assignment.

### 3. The 2 Phases of React Rendering

┌─────────────────────────────────────────────────────────────┐

│ 1. Render / Reconciliation Phase (Asynchronous) │

│ - Pure calculations without DOM mutations │

│ - Interruptible & restartable by scheduler │

│ - Invokes component render functions and Hook reducers │

└──────────────────────────────┬──────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│ 2. Commit Phase (Synchronous) │

│ - Uninterruptible DOM mutations (appendChild, remove) │

│ - Invokes useLayoutEffect (synchronous before paint) │

│ - Browser Paints Screen │

│ - Invokes useEffect (asynchronous after paint) │

└─────────────────────────────────────────────────────────────┘

### 4. Concurrent Mode & Lanes Priority Scheduling

React models update urgency using a 32-bit bitmask called **Lanes**:

- **SyncLane**: Immediate user interactions (typing into an input).

- **TransitionLane**: Non-urgent updates (switching tabs, filtering a 10,000-item table).

#### Primitives: useTransition vs useDeferredValue

- useTransition: Wraps state updates to execute at low priority, keeping the UI interactive.

- useDeferredValue: Defers re-rendering a subtree until higher-priority updates have finished.

import { useState, useTransition, useDeferredValue } from \'react\';

export function SearchDashboard() {

const \[query, setQuery\] = useState(\"\");

const \[isPending, startTransition\] = useTransition();

function handleChange(e: React.ChangeEvent\<HTMLInputElement\>) {

// High-priority immediate update: input field responds at 120fps

const nextValue = e.target.value;

setQuery(nextValue);

// Low-priority transition: heavy filtering can be interrupted by new keystrokes

startTransition(() =\> {

// Background filtering state updates

});

}

return (

\<div\>

\<input value={query} onChange={handleChange} /\>

{isPending && \<span className=\"spinner\"\>Updating results\...\</span\>}

\<HeavyProductGrid query={query} /\>

\</div\>

);

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Fiber & Concurrent API Reference:

  -------------------------------------------------------------------------------------------------------------------------------------------------------
  **API / Feature**       **Type**          **Primary Purpose**                               **Timing / Behavior**
  ----------------------- ----------------- ------------------------------------------------- -----------------------------------------------------------
  useTransition()         Hook              Mark state updates as non-blocking transitions    Yields main thread to higher-priority user events

  useDeferredValue(val)   Hook              Defer rendering a computed sub-tree               Re-renders in background; keeps stale value during render

  useLayoutEffect()       Hook              Read DOM layout & synchronously re-render         Fires **before** browser paint; blocks visual update

  useEffect()             Hook              Perform asynchronous side effects                 Fires **after** browser paint; non-blocking

  Suspense                Component         Declare fallback UI for async component loading   Coordinates concurrent boundary reveals
  -------------------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (High-Frequency Real-Time Financial Trading Terminal in React)

Design a high-frequency cryptocurrency order book and trading chart UI in React receiving 500 WebSocket price updates/second.

**Requirements**:

1.  Detail how to prevent main-thread UI freezing using Concurrent React (useTransition, useDeferredValue, and Web Workers).

2.  Design the component hierarchy separating volatile, fast-updating price ticks from slow-updating heavy SVG candlestick charts.

3.  Formulate an update batching and time-slicing strategy ensuring input fields (order submit forms) maintain sub-16ms latency under heavy render load.

### Problem 2: End-to-End Code Implementation Challenge

Build a standalone **Cooperative Mini-Fiber Work Scheduler** in TypeScript from scratch (without React dependencies):

**Requirements**:

1.  Implement a FiberNode structure with child, sibling, and return linked-list pointers.

2.  Implement a workLoop scheduler using MessageChannel (or requestIdleCallback) that processes a tree of 1,000 synthetic Fiber nodes in \$5\\text{ms}\$ time-sliced chunks.

3.  Support **Priority Interruption**: If a high-priority task is queued while the scheduler is processing low-priority nodes, pause the current work-in-progress tree, execute the high-priority task, and resume or restart the low-priority tree.

4.  Provide unit tests verifying:

    - Time-sliced non-blocking execution across multiple event loop turns.

    - High-priority task preemption and correct completion.
