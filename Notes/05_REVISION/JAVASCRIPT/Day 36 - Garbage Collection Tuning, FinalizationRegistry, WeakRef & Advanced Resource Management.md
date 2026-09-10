---
tags:
  - javascript
  - memory-management
  - weakref
  - finalization-registry
  - garbage-collection
  - v8-internals
  - resource-management
  - performance
date: 2026-09-05
---

# Day 36 - Garbage Collection Tuning, FinalizationRegistry, WeakRef & Advanced Resource Management

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Weak References & Ephemeron Semantics in V8

In standard JavaScript, storing an object reference in an array, object, or closure creates a **Strong Reference**. As long as that reference is reachable from a root (the global object, current call stack frames, or active event listeners), the V8 Garbage Collector cannot reclaim its memory.

JavaScript provides two complementary tiers of weak retention:

1. **Ephemeron Collections (`WeakMap` & `WeakSet`)**: Keys are held weakly, but values are held strongly *conditioned on the reachability of the key*. When the key object is collected, the entry is automatically purged. They are non-enumerable because the set of keys is inherently non-deterministic.
2. **First-Class Weak References (`WeakRef`)**: An explicit wrapper that holds a weak reference to a target object without preventing its collection, accessed via `weakRef.deref()`.
3. **Cleanup Lifecycle Callbacks (`FinalizationRegistry`)**: Registers cleanup callbacks invoked by the host environment after a target object has been collected by the Garbage Collector.

┌────────────────────────────────────── Reference Strength & GC Reachability ──────────────────────────────────────┐

│                                                                                                                  │

│  Strong Reference:                                                                                               │

│  [ GC Root ] ══════════════════════════════════════════════════════════════════════════► [ Target Object ]       │

│  (Target CANNOT be collected under any GC cycle)                                                                 │

│                                                                                                                  │

│  WeakRef / WeakMap Key:                                                                                          │

│  [ GC Root ] -------------------------------- (Weak Pointer) ------------------------► [ Target Object ]       │

│  (Target CAN be reclaimed during Minor/Major GC if no strong references exist)                                   │

│                                                                                                                  │

│  When Target is reclaimed:                                                                                       │

│  [ WeakRef.deref() ] ──► Returns `undefined`                                                                     │

│  [ FinalizationRegistry ] ──► Invokes cleanup callback with uncollected heldValue                                │

│                                                                                                                  │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. Implementation: WeakRef, FinalizationRegistry & The Memory-Leak Pitfall

// Cache with Automatic Memory-Reclamation via WeakRef & FinalizationRegistry

class WeakCache {

  #cache \= new Map(); // Stores key -> WeakRef(Object)

  #registry;

  constructor() {

    // Finalizer callback invoked after GC reclaims the cached object

    this.#registry \= new FinalizationRegistry((key) \=> {

      const ref \= this.#cache.get(key);

      // Clean up the dangling Map entry if the WeakRef was indeed collected

      if (ref && ref.deref() \=== undefined) {

        this.#cache.delete(key);

        console.log(`[GC]: Key "${key}" cleared from cache.`);

      }

    });

  }

  set(key, value) {

    if (typeof value !== 'object' || value \=== null) {

      throw new TypeError('WeakCache only stores object values.');

    }

    // Deregister prior entries if overwriting

    this.#cache.set(key, new WeakRef(value));

    // Register for finalization: unregisterToken is value itself

    this.#registry.register(value, key, value);

  }

  get(key) {

    const ref \= this.#cache.get(key);

    if (!ref) return undefined;

    const value \= ref.deref();

    if (value \=== undefined) {

      // Memory was reclaimed by GC before finalizer ran

      this.#cache.delete(key);

      return undefined;

    }

    return value;

  }

}

#### Critical Rules & Pitfalls:

- **Non-Determinism**: Garbage collection timing is unpredictable across different browsers and V8 optimizations. Never rely on `FinalizationRegistry` for critical business logic (e.g. database commits, financial operations, or security clearances).
- **Held Value Leaks**: The `heldValue` passed to `FinalizationRegistry` must **never** strongly retain the target object, or the object will become uncollectible, creating a permanent memory leak.
- **Short-Lived Retention**: Between the start of a turn and the end of microtask execution, `deref()` is guaranteed to return the object consistently to avoid mid-expression reclamation.

---

### 3. Explicit Resource Management: TC39 `using` and `Symbol.dispose`

Modern JavaScript introduces deterministic cleanup using the **Explicit Resource Management** standard (`using` and `await using`), solving the manual `try...finally` boilerplate for file handles, sockets, and transactions.

// Disposable Database Client Pattern

class DatabaseTransaction implements AsyncDisposable {

  #txId: string;

  #isActive \= true;

  constructor(txId: string) {

    this.#txId \= txId;

  }

  async query(sql: string) {

    if (!this.#isActive) throw new Error('Transaction is closed.');

    return `Result of ${sql} on ${this.#txId}`;

  }

  async commit() {

    this.#isActive \= false;

    console.log(`Committed transaction ${this.#txId}`);

  }

  // Invoked automatically when leaving lexical block scope!

  async [Symbol.asyncDispose]() {

    if (this.#isActive) {

      this.#isActive \= false;

      console.log(`[Auto-Rollback]: Transaction ${this.#txId} safely closed.`);

    }

  }

}

// Deterministic Scope-Bound Usage

async function processOrder() {

  await using tx \= new DatabaseTransaction('tx-8831');

  await tx.query('UPDATE accounts SET balance \= balance - 100');

  // If an error is thrown here, [Symbol.asyncDispose] runs automatically, rolling back!

  await tx.commit();

} // tx is disposed automatically right here upon exiting scope

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Resource Management & Reference Capabilities Matrix:

| Primitive | Weak Target | Weak Value | Enumerable? | Primary Use Case |
| :---- | :---- | :---- | :---- | :---- |
| `WeakMap` | Objects / Symbols | No (Strong) | No | Private state, metadata attachment to foreign objects |
| `WeakSet` | Objects / Symbols | N/A | No | Branding, cycle detection, object tagging |
| `WeakRef` | Objects / Symbols | N/A | N/A | Memory-sensitive caches, optional object access |
| `FinalizationRegistry` | Target Object | N/A | N/A | Native handle cleanup, cache key cleanup notifications |
| `Symbol.dispose` | N/A | N/A | N/A | Synchronous deterministic cleanup (`using res = ...`) |
| `Symbol.asyncDispose` | N/A | N/A | N/A | Asynchronous deterministic cleanup (`await using res = ...`) |

---

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: GC Reclamation Prediction & Microtask Invariant

Analyze the following script and predict the output under V8 garbage collection:

let target \= { name: "BigDataPayload" };

const ref \= new WeakRef(target);

Promise.resolve().then(() \=> {

  target \= null; // Strong reference severed

  // Force Minor/Major GC in Node.js via global.gc()

  if (global.gc) global.gc();

  console.log("Check 1:", ref.deref()?.name);

});

setTimeout(() \=> {

  if (global.gc) global.gc();

  console.log("Check 2:", ref.deref()?.name);

}, 50);

*Question*: Why does Check 1 reliably retain the object even after `global.gc()` is called in some JavaScript engine implementations, while Check 2 returns `undefined`? Explain the ECMAScript execution turn lifetime invariant for `WeakRef`.

---

### Challenge 2: Memory-Bounded Image Texture Cache

Refactor a memory-intensive WebGL texture cache:

1. Cache entries must hold textures via `WeakRef` so the browser can reclaim textures under low VRAM conditions.
2. When a texture is collected, its entry in the key-lookup map must be cleaned up via `FinalizationRegistry`.
3. Provide an explicit `pin(key)` method that temporarily elevates a cached texture to a strong reference to prevent GC while actively rendering.

---

### Challenge 3: Leak-Detecting Connection Pool in TypeScript

Build an Enterprise **Leak-Detecting Connection Pool** in TypeScript using `FinalizationRegistry` and `Symbol.asyncDispose`:

**Requirements**:

1. **Connection Lifecycle**:
   - Manages a pool of 10 virtual database connections.
   - `pool.acquire()` returns a connection wrapped in an `AsyncDisposable` resource (`await using conn = await pool.acquire()`).
2. **Leak Detection via FinalizationRegistry**:
   - If a consumer acquires a connection, drops all references, and exits scope **without** calling `[Symbol.asyncDispose]()` or `.release()`, the `FinalizationRegistry` must detect the abandoned connection when garbage-collected, emit a critical telemetry alert with the allocation stack trace, and reclaim the underlying socket for the pool.
3. **Graceful Drain**:
   - `pool.drain()` safely closes all active and idle sockets, rejecting new acquisition requests.

