tags:

- javascript

- memory-profiling

- v8-heap

- garbage-collection

- performance

- memory-leaks date: 2026-08-13

# Day 13 - Garbage Collection Optimization, Memory Profiling & V8 Heap Allocation

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. V8 Engine Memory Architecture & Heap Spaces

The V8 Engine manages JavaScript memory through a structured heap memory layout divided into specialized spaces to optimize allocation speed and garbage collection overhead.

#### V8 Heap Organization:

- **New Space (Nursery & Intermediate)**: Allocation pool for short-lived objects (typically 1MB -- 8MB). Managed by the fast **Minor GC (Scavenger)**. Objects that survive two Minor GC cycles are promoted to the Old Space.

- **Old Pointer Space**: Stores promoted objects that contain references to other objects.

- **Old Data Space**: Stores raw payload objects (strings, raw byte arrays, unboxed numbers).

- **Large Object Space**: Allocations exceeding the size limit of other spaces bypass standard GC and are allocated directly here to prevent heap fragmentation.

- **Code Space**: Stores compiled JIT machine code produced by TurboFan.

### 2. V8 Garbage Collection Mechanics: Minor vs Major GC

Garbage collection reclaims memory occupied by unreferenced objects. V8 utilizes a generational garbage collection strategy:

#### Minor GC (Scavenger / Cheney\'s Algorithm):

- Uses a **To-Space** and **From-Space** semi-space copying collector.

- Extrema fast because it only inspects live objects in the New Space and copies them sequentially, freeing the remaining space in a single sweep.

#### Major GC (Mark-Sweep-Compact):

When the Old Space reaches its dynamic threshold, V8 triggers Major GC across 3 phases:

1.  **Marking**: Traces reachable objects starting from the GC Root (Global Object, Call Stack variables). V8 uses **Concurrent Marking** on background worker threads to avoid main-thread UI pauses.

2.  **Sweeping**: Scans memory ranges and adds unreferenced memory addresses back to free lists.

3.  **Compacting**: Relocates surviving objects into contiguous memory blocks to eliminate fragmentation.

// Visualizing Memory Allocation Dynamics in V8

function AllocationPatternTest() {

// 1. Short-lived allocation -\> Allocated in New Space (Nursery)

for (let i = 0; i \< 10000; i++) {

const temp = { id: i, payload: \"transient\" };

// Automatically collected by Minor GC (Scavenger)

}

// 2. Long-lived allocation -\> Promoted to Old Space after 2 GC cycles

const persistentCache = new Map();

for (let i = 0; i \< 1000; i++) {

persistentCache.set(\`key-\${i}\`, { data: new Array(100).fill(\"persistent\") });

}

return persistentCache;

}

### 3. Memory Leak Anti-Patterns in JavaScript

A memory leak occurs when an application retains references to objects that are no longer required, preventing GC reclamation.

#### Common Leak Patterns:

1.  **Detached DOM Nodes**: Keeping JavaScript references to DOM elements that have been removed from the DOM tree.

2.  **Closure Scope Leaks**: Outer function variables retained indefinitely inside un-garbage-collected callbacks.

3.  **Uncleared Timers & Listeners**: Global setInterval or EventEmitter callbacks holding reference to enclosing scopes.

// Anti-Pattern: Detached DOM Node Leak

let detachedElementRef;

function createLeak() {

const button = document.createElement(\"button\");

button.id = \"leak-button\";

document.body.appendChild(button);

// JS holds reference to button

detachedElementRef = button;

// Button removed from DOM, but detachedElementRef keeps entire subtree in memory!

document.body.removeChild(button);

}

// Remediation: Nullify reference after DOM removal

function fixLeak() {

createLeak();

detachedElementRef = null; // Released for GC

}

### 4. Memory Profiling in Chrome DevTools

- **Shallow Size**: Memory directly held by the object itself.

- **Retained Size**: Total memory freed when the object is garbage collected (includes transitively referenced objects).

- **Distance**: Shortest path of references from GC Roots.

## SECTION 2: DOCUMENTATION CHEAT SHEET

  -------------------------------------------------------------------------------------------------------------------------------------
  **Metric / Command**                  **Purpose / Usage**                        **Significance**
  ------------------------------------- ------------------------------------------ ----------------------------------------------------
  **node \--trace-gc script.js**        Logs detailed V8 GC execution statistics   Identifies GC frequency & Stop-The-World duration

  **node \--max-old-space-size=4096**   Configures Node.js heap limit (e.g. 4GB)   Prevents OOM crashes in heavy workloads

  **Shallow Size**                      Object.keys() & internal field bytes       Direct memory footprint of target object

  **Retained Size**                     Distance graph reachability size           Real memory reclaimed if object is dereferenced

  **WeakRef & FinalizationRegistry**    const ref = new WeakRef(obj)               Allows non-retaining references & GC cleanup hooks
  -------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Shallow vs Retained Size Memory Graph Analysis

Analyze the object graph below and calculate:

1.  The **Shallow Size** of UserSessionManager.

2.  The **Retained Size** of UserSessionManager.

3.  What happens to the memory when manager = null is executed?

class UserSession {

constructor(id) {

this.id = id; // 8 bytes

this.buffer = new ArrayBuffer(1024 \* 1024); // 1MB payload

}

}

class UserSessionManager {

constructor() {

this.sessions = new Map(); // 128 bytes map metadata

}

addSession(id) {

this.sessions.set(id, new UserSession(id));

}

}

let manager = new UserSessionManager();

manager.addSession(\"usr_100\");

*Hint*: Calculate retained memory transitively through this.sessions.

### Challenge 2: Diagnosing and Fixing a Closure Scope Memory Leak

The following code leaks memory when startWorker() is invoked repeatedly. Identify the root cause of the retained memory and refactor it so that unused data is freed by V8.

// Leaky Code Pattern

let unusedClosureLeak = null;

function startWorker() {

const originalLeak = unusedClosureLeak;

// Large allocation

const hugeData = new ArrayBuffer(10 \* 1024 \* 1024); // 10MB

unusedClosureLeak = function () {

if (originalLeak) {

console.log(\"Worker active\");

}

};

}

setInterval(startWorker, 1000); // 10MB leaked every second!

*Hint*: Explain how hugeData is trapped in the lexical environment shared by unusedClosureLeak.

### Challenge 3: Building a Zero-Allocation Object Pool Engine

Write a high-performance, reusable **Object Pool Class** ObjectPool\<T\> in TypeScript that:

1.  Pre-allocates an array of N instances using a factory function allocator().

2.  Provides a acquire() method to retrieve an idle instance.

3.  Provides a release(instance: T) method to reset object state and return it to the pool.

4.  Prevents garbage collection churn during high-frequency short-lived object allocation loops (e.g. 100,000 requests/sec).

*Hint*: Implement state reset inside release() and benchmark memory usage using process.memoryUsage().heapUsed.
