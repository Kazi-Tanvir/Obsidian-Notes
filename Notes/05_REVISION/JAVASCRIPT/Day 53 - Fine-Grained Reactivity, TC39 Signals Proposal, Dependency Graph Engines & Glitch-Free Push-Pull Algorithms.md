---
tags:
  - javascript
  - reactivity
  - signals
  - tc39
  - state-management
  - dependency-graph
  - algorithms
  - architecture
date: 2026-09-22
---

# Day 53 - Fine-Grained Reactivity, TC39 Signals Proposal, Dependency Graph Engines & Glitch-Free Push-Pull Algorithms

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Reactivity Paradigm Shift: Virtual DOM vs. Fine-Grained Signals

For over a decade, web frontends relied on **Virtual DOM (VDOM) reconciliation** (React). In a VDOM architecture:

- When state changes inside a component, the framework re-executes the entire component function.

- It generates a new virtual tree in memory, diffs it against the previous virtual tree (\$O(N)\$ tree comparison), and commits changes to the real DOM.

- **The Performance Penalty**: Even with compiler optimizations and memoization (useMemo, useCallback), VDOM diffing burns CPU cycles recalculating trees that didn't change, creating garbage collection pressure and requiring complex dependency arrays ([a, b]).

**Fine-Grained Reactivity (Signals)** flips this model on its head:

- Components run **exactly once** during initialization to build a reactive Directed Acyclic Graph (DAG).

- When a Signal value updates, it bypasses component boundaries entirely and updates **only the specific text node or attribute in the real DOM** that depends on it (\$O(1)\$ direct targeted mutations)!

```text
┌────────────────────────────────────── Virtual DOM vs. Signals ──────────────────────────────────────┐
│                                                                                                     │
│  Virtual DOM Reconciliation (Coarse-Grained):                                                       │
│  State Change ──► Re-run Entire Component ──► Generate VDOM Tree ──► Diff Trees ──► Patch Real DOM  │
│  • High CPU overhead, high GC allocations, requires manual dependency arrays.                      │
│                                                                                                     │
│  Fine-Grained Reactivity / Signals (Targeted Micro-Updates):                                        │
│  Signal.State.set(value) ──► Mark Graph Dirty ──► Direct Targeted DOM Mutation ⚡                   │
│  • Zero VDOM diffing, zero component re-executions, automatic dynamic dependency tracking!          │
│                                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The TC39 Signals Standard Architecture

Recognizing that modern frontend frameworks (Solid.js, Preact, Vue, Angular, Svelte 5) had converged on Signals, TC39 introduced the official **ECMAScript Signals Standard Proposal**:

1.  **Signal.State<T> (Writable Source)**: Represents root reactive state. Reading it records dependencies; writing to it marks dependents dirty.

2.  **Signal.Computed<T> (Derived Memo)**: Represents cached computed formulas. Lazily evaluated; only recomputes if its upstream dependencies have changed.

3.  **Signal.subtle.Watcher (Reaction Driver)**: Low-level primitive utilized by framework schedulers to detect when signals become dirty and schedule reactions (effects).

```text
┌────────────────────────────────────── Reactive Dependency Graph (DAG) ──────────────────────────────────────┐
│                                                                                                             │
│             [ Signal.State: firstName ]        [ Signal.State: lastName ]                                   │
│                           │                                │                                                │
│                           └───────────────┬────────────────┘                                                │
│                                           ▼                                                                 │
│                             [ Signal.Computed: fullName ]                                                   │
│                                           │                                                                 │
│                                           ▼                                                                 │
│                         [ Signal.subtle.Watcher / Effect ]                                                  │
│                                           │                                                                 │
│                                           ▼                                                                 │
│                              Direct DOM Text Node Update!                                                   │
│                                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3. The Diamond Dependency Problem & Glitch-Free Algorithms

A fundamental flaw in naive reactive implementations is **Glitches** (transient inconsistencies where computed values evaluate with mismatched data).

#### The Classic Diamond Graph:

Suppose:

- Root signal: \$A = 1\$

- Derived: \$B = A \\times 2\$ (so \$B = 2\$)

- Derived: \$C = A + 1\$ (so \$C = 2\$)

- Output: \$D = B + C\$ (so \$D = 4\$)

[ A ]

/

[ B ] [ C ]

\\ /

[ D ]

If \$A\$ updates to \$2\$:

- **Naive Eager Evaluation**: \$A\$ notifies \$B \\to B\$ updates to \$4 \\to B\$ notifies \$D \\to D\$ evaluates with *new* \$B\$ (\$4\$) and *stale* \$C\$ (\$2\$), producing \$D = 6\$ (A GLITCH!).

- Then \$A\$ notifies \$C \\to C\$ updates to \$3 \\to C\$ notifies \$D \\to D\$ evaluates to \$7\$.

- \$D\$ updated **twice**, temporarily exposing invalid intermediate state!

#### The Glitch-Free Solution: The Push-Pull Algorithm

Modern signal engines solve this via a **two-phase Push-Pull evaluation algorithm**:

1.  **Push Phase (Dirty Marking)**: When \$A\$ mutates, it pushes a lightweight DIRTY notification down through its child nodes (\$B, C, D\$). **Zero values are recalculated in this phase.**

2.  **Pull Phase (Lazy Evaluation with Version Counters)**: When \$D\$ is read, it inspects its parents. It asks \$B\$ and \$C\$ to recompute first if they are marked dirty. Once both are stable, \$D\$ recalculates exactly **once**.

### 4. Anatomy of Automatic Dependency Tracking

How does a Signal know which computed function is reading it without passing explicit subscribers? It uses **Lexical Execution Context on the Call Stack**:

```typescript
// Minimalist Signals Engine Implementation
let activeSubscriber = null;
class SignalState {
  constructor(value) {
    this.value = value;
    this.subscribers = new Set();
  }
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### TC39 Signals API Reference:

------------------------------------------------------------------------------- **Class / Method**              **Signature**           **Purpose & Performance Rule** ------------------------------- ----------------------- ----------------------- new Signal.State(initialValue)  <T>(val: T) =>       Creates mutable root Signal.State<T>       reactive state.

state.get()                     () => T                Reads value; dynamically registers subscriber if inside computation context.

state.set(newValue)             (val: T) => void       Updates value; checks Object.is(); pushes dirty notifications down graph.

new Signal.Computed(fn)         <T>(computation: ()   Creates a memoized lazy => T) =>              derived signal. Only Signal.Computed<T>    recomputes on demand when dirty.

new                             (notifyCallback: () => Framework primitive to Signal.subtle.Watcher(notify)   void) => Watcher       observe signals for reactive scheduler loops.

watcher.watch(\...signals)      (\...signals:           Subscribes watcher to a Signal[]) => void    set of signals.

watcher.unwatch(\...signals)    (\...signals:           Removes subscription, Signal[]) => void    allowing garbage collection.

watcher.getPending()            () => Signal[]       Returns all observed signals that are currently dirty. -------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Problem 1 (Basic): Dynamic Conditional Dependency Pruning

**Context**: In dynamic UIs, dependencies change conditionally: const message = computed(() => showDetails.get() ? detailedInfo.get() : summary.get()); If showDetails is false, detailedInfo must **not** be tracked as a dependency. If detailedInfo changes while showDetails is false, the computed signal should not re-evaluate.

**Challenge**: Implement a dependency tracking algorithm inside a Computed class that:

1.  Clears or prunes inactive dependencies on every evaluation cycle.

2.  Demonstrates with unit test assertions that when a conditional branch is skipped, modifying the unread branch signal incurs zero dirty notifications and zero recalculations.

*Hint: Contrast the "Clear-and-Re-add" strategy against the "Generational Index" strategy used in Solid.js and Vue 3.*

### Problem 2 (Intermediate): Glitch-Free Topological Sorter for Diamond Graphs

**Context**: When complex reactive networks have diamond dependencies, scheduling evaluations naively executes effects multiple times with inconsistent intermediate states.

**Challenge**: Build a ReactiveScheduler class:

1.  Implements a batching transaction wrapper: batch(fn: () => void): void.

2.  When multiple signals update inside batch(), defers all downstream effect executions until the batch terminates.

3.  Performs a **topological sort** or height/rank traversal on the dirty subgraph to guarantee that parent nodes always re-evaluate before their children.

4.  Verify with test assertions that in the diamond graph (\$A \\to B, C \\to D\$), updating \$A\$ causes \$D\$ to execute **exactly once** with the final synchronized values.

*Hint: Assign each node a level / rank in the DAG: \$\\text{rank}(node) = 1 + \\max(\\text{rank}(parents))\$. Always evaluate lower ranks first.*

### Problem 3 (Advanced): High-Performance Memory-Safe Reactive Store with WeakRefs

**Context**: Long-lived single-page enterprise applications accumulate memory leaks when transient DOM components subscribe to global signals without calling explicit unsubscription handlers.

**Challenge**: Develop an enterprise-grade ReactiveStore<T> in TypeScript:

1.  Stores an object of signals where nested properties are wrapped in reactive getters/setters via an ES6 Proxy.

2.  Implements **Weak References** (WeakRef) and a FinalizationRegistry to manage subscriber listeners:

    - If a DOM element or subscriber closure is garbage collected by V8, the store automatically cleans up its internal subscriber graph references without memory leaks.

3.  Implements an explicit micro-task batched scheduler using queueMicrotask.

4.  Benchmark verifying that creating and abandoning 100,000 transient subscriptions leaves zero memory leaks in the V8 heap.

*Hint: Store subscribers as WeakRef<Subscriber> and register them in a FinalizationRegistry to remove dead references from the signal's subscriber set.*
