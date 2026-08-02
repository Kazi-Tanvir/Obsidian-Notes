---

tags:

- javascript  
- closures  
- memory-management  
- garbage-collection  
- v8-heap date: 2026-08-02

---

# Day 2 \- Closures, Memory Management & Garbage Collection

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1\. Closures & Lexical Environment Persistence

A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **Lexical Environment**). In JavaScript, closures give inner functions access to an outer function's scope even after the outer function has finished executing and its execution context has been popped off the Call Stack.

#### Under the Hood Mechanics:

- When a function is declared, it holds an internal `[[Environment]]` reference pointing to the Lexical Environment in which it was created.  
- When an inner function references variables from its outer scope, those variables are stored in heap memory inside a **Closure Object** instead of being garbage-collected when the parent function context exits.

// Module Pattern using Closures for Data Encapsulation

function createBankContext(initialBalance) {

  let balance \= initialBalance; // Private state

  return {

    deposit(amount) {

      if (amount \<= 0\) throw new Error("Invalid deposit amount");

      balance \+= amount;

      return balance;

    },

    withdraw(amount) {

      if (amount \> balance) throw new Error("Insufficient funds");

      balance \-= amount;

      return balance;

    },

    getBalance() {

      return balance;

    }

  };

}

const myAccount \= createBankContext(1000);

console.log(myAccount.deposit(500)); // 1500

console.log(myAccount.getBalance()); // 1500

// console.log(myAccount.balance);  // undefined (Private\!)

---

### 2\. V8 Memory Layout & Garbage Collection (GC)

JavaScript manages memory automatically using **Garbage Collection**. The V8 JavaScript Engine divides heap memory into distinct spaces for optimization:

#### Memory Spaces:

1. **Young Generation (Nursery & Intermediate)**:  
   - Stores short-lived objects (most allocations).  
   - Cleaned frequently using the fast **Scavenger Algorithm (Cheney's Copying Algorithm)**.  
2. **Old Generation (Old Pointer Space & Old Data Space)**:  
   - Stores long-lived objects that survived two Scavenger cycles.  
   - Managed using **Mark-Sweep-Compact Algorithm**.  
3. **Large Object Space**: Stores allocations exceeding single-page heap limits.  
4. **Code Space**: Stores JIT-compiled machine code instructions.

#### GC Algorithms:

- **Scavenger (Minor GC)**: Divides Young Generation into *From-Space* and *To-Space*. Copies active objects from *From* to *To*, discards dead objects, and swaps spaces.  
- **Mark-Sweep-Compact (Major GC)**:  
  - *Marking*: Traverses object references starting from GC Roots (Global, Stack pointers).  
  - *Sweeping*: Recovers memory addresses of unreferenced objects.  
  - *Compacting*: Shifts live objects together to defragment memory space.

---

### 3\. Common Memory Leaks & Fixes

A **memory leak** occurs when allocated memory is no longer needed by the application but is not returned to the operating system/free memory pool because references persist.

#### Primary Memory Leak Causes:

1. **Accidental Global Variables**: Un-declared variables (`x = 10`) attach to `globalThis` / `window`.  
2. **Forgotten Timers / Callbacks**: `setInterval` keeping references to closed-over variables.  
3. **Detached DOM Nodes**: References to removed DOM nodes stored inside JS arrays/objects.  
4. **Uncleaned Event Listeners**: Event handlers holding references to large objects.

// Pitfall: Memory Leak via Detached DOM Node

function LeakExample() {

  const element \= document.getElementById("button");

  const heavyData \= new Array(1000000).fill("data");

  element.addEventListener("click", function onClick() {

    console.log(heavyData.length);

  });

  // If 'element' is removed from DOM without removeEventListener,

  // 'heavyData' remains pinned in memory via the event listener closure\!

}

// Fix: Use WeakMap or explicitly detach listener / nullify references

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

| Concept | Description | V8 Mechanism | Key Benefit / Pitfall |
| :---- | :---- | :---- | :---- |
| **Closure** | Function retaining access to outer Lexical Scope | Stored in Heap via `[[Environment]]` reference | Enables encapsulation; retain unwanted references if misused |
| **Minor GC** | Collects short-lived allocations | Cheney's Scavenger Algorithm | Extremely fast (milliseconds); operates on Young Generation |
| **Major GC** | Collects long-lived allocations | Mark-Sweep-Compact Algorithm | Defragments Old Space; runs incrementally to minimize pause time |
| **WeakMap** | Key-value store holding weak object references | Weak Garbage Collection tracking | Keys are garbage collected if no other references exist |
| **WeakSet** | Collection holding weak object references | Weak Garbage Collection tracking | Items collected automatically when unreferenced elsewhere |

### Key Garbage Collection Metrics & Rules:

- **GC Roots**: Global variables, active Execution Context Call Stack frames, DOM trees, internal engine pointers.  
- **`WeakMap` Rules**: Keys MUST be objects/symbols; non-iterable; prevent retention memory leaks.

---

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Basic Concept & Closure State Prediction

Predict the exact console output of the code snippet below and explain how closure references behave across multiple function calls.

function createCounter() {

  let count \= 0;

  return function() {

    count++;

    return count;

  };

}

const counter1 \= createCounter();

const counter2 \= createCounter();

console.log(counter1());

console.log(counter1());

console.log(counter2());

console.log(counter1());

*Hint*: Determine whether `counter1` and `counter2` share the same Lexical Environment or instantiate separate closures.

---

### Challenge 2: Intermediate Refactoring (Event Subscription Leak)

The `EventEmitter` implementation below contains a severe memory leak when listeners are registered and unsubscribed. Identify the leak and refactor the code to ensure memory is properly garbage-collected upon unsubscription.

// Buggy Memory Leaking Event Emitter

class LeakyEventEmitter {

  constructor() {

    this.events \= {};

  }

  on(event, listener) {

    if (\!this.events\[event\]) this.events\[event\] \= \[\];

    this.events\[event\].push(listener);

    

    return () \=\> {

      // Buggy Unsubscribe: Does not remove listener completely\!

      this.events\[event\] \= this.events\[event\].map(fn \=\> fn \=== listener ? null : fn);

    };

  }

}

*Hint*: Look at array filtering vs setting elements to `null`, and clean up empty event key arrays.

---

### Challenge 3: Advanced Memory-bounded Cache Implementation

Implement a production-grade `BoundedCache` class in JavaScript from scratch with the following specs:

1. Max capacity limit `N`.  
2. LRU (Least Recently Used) eviction policy when capacity is reached.  
3. Automatically uses `WeakRef` / `FinalizationRegistry` or strict internal reference cleanup so unreferenced values do not cause persistent leaks.  
4. Exposes `set(key, value)`, `get(key)`, `has(key)`, and `clear()`.

*Hint*: Combine a JavaScript `Map` (which maintains insertion order for LRU tracking) with proper eviction on capacity breach.  
