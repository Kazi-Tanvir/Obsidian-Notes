tags:

- javascript

- execution-context

- call-stack

- hoisting

- scope-chain

- v8

date: 2026-08-01

# Day 1 - Execution Context, Call Stack & Scope Chain

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The JavaScript Execution Engine & Execution Context (EC)

JavaScript is a single-threaded, synchronous language at its core. Everything in JavaScript happens inside an **Execution Context**. Think of an Execution Context as a containerized environment where JavaScript code is evaluated and executed.

An Execution Context consists of two primary phases:

1.  **Creation Phase (Memory Allocation / Variable Environment)**:

    - The engine scans the code and allocates memory for variables and functions.

    - Variables declared with var are assigned undefined.

    - Function declarations are stored completely in memory (pointer to the function body).

    - Variables declared with let and const are allocated memory but remain uninitialized in the **Temporal Dead Zone (TDZ)**.

    - The this keyword binding is established.

    - The outer lexical environment reference (OuterEnv) is set up.

2.  **Execution Phase (Code Execution)**:

    - Code is executed line-by-line.

    - Variables are assigned their actual values.

    - Function invocations create new **Function Execution Contexts (FEC)** on top of the **Global Execution Context (GEC)**.

// Example: Execution Context Breakdown

console.log(a); // Output: undefined (hoisted var)

// console.log(b); // Throws ReferenceError: Cannot access \'b\' before initialization (TDZ)

var a = 10;

let b = 20;

function multiply(x, y) {

var result = x \* y;

return result;

}

var res = multiply(a, b);

console.log(res); // 200



### 2. The Call Stack & V8 Mechanics

The **Call Stack** (or Execution Context Stack) is a LIFO (Last In, First Out) data structure that tracks the current execution point of the script.

- When the script starts, the **Global Execution Context** is pushed to the bottom of the stack.

- Whenever a function is invoked, a new **Function Execution Context** is created and pushed onto the Call Stack.

- When a function returns or finishes executing, its context is popped off the stack, and control returns to the underlying context.

- **Stack Overflow**: Exceeding maximum stack size due to unbounded recursion.

// Call Stack Visualization

function first() {

console.log(\"Inside first\");

second();

console.log(\"Exiting first\");

}

function second() {

console.log(\"Inside second\");

}

first();

/\*

Call Stack Trajectory:

1\. Push Global Execution Context

2\. Push first() EC

3\. Push second() EC -\> console.log -\> Pop second() EC

4\. Resume first() -\> console.log -\> Pop first() EC

5\. Global Execution Context remains until window/process closes.

\*/



### 3. Hoisting, Lexical Scope & Scope Chain

- **Hoisting**: The behavior where variable and function declarations are moved to the top of their containing scope during the Creation Phase.

  - **Function Declarations** are fully hoisted.

  - **Function Expressions** assigned to var/let/const follow variable hoisting rules.

- **Lexical Environment**: Local memory plus reference to the parent\'s (outer) lexical environment.

- **Scope Chain**: The hierarchy of lexical environments used to resolve identifier names. If a variable is not found in the local scope, the JS engine searches up the Scope Chain until it reaches the Global Scope. If not found there, a ReferenceError is thrown.

// Pitfall & Edge Case: Shadowing & TDZ

const x = \"global\";

function scopeTest() {

// console.log(x); // ReferenceError! \'x\' is shadowed by local \'let x\' which is in TDZ here!

let x = \"local\";

console.log(x); // \'local\'

}

scopeTest();



## SECTION 2: DOCUMENTATION CHEAT SHEET

  -------------------------------------------------------------------------------------------------------------------
  **Concept**           **Declaration**   **Hoisted?**   **Initial Value**   **Scope**           **Re-declarable?**
  --------------------- ----------------- -------------- ------------------- ------------------- --------------------
  var                   Variable          Yes            undefined           Function / Global   Yes

  let                   Variable          Yes (TDZ)      Uninitialized       Block Scope {}      No

  const                 Constant          Yes (TDZ)      Uninitialized       Block Scope {}      No

  function foo(){}      Declaration       Yes            Function Body       Block / Function    Yes (varies)

  var foo = () =\> {}   Expression        Yes (as var)   undefined           Function / Global   Yes
  -------------------------------------------------------------------------------------------------------------------

### Core Rules & Mechanics

- **Creation Phase vs Execution Phase**: Memory setup happens before code runs.

- **Temporal Dead Zone (TDZ)**: Time window between enter block scope and actual variable initialization for let / const.

- **Lexical Scope**: Scope is determined at **compile time** (where function is defined), not run time (where function is called).

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Basic Concept & Scope Prediction

Predict the exact console output of the code snippet below and explain why each line produces its specific output based on Hoisting and Scope Chain rules.

var a = 1;

function b() {

a = 10;

return;

function a() {}

}

b();

console.log(a);

*Hint*: Consider how function a() {} inside b() is hoisted relative to assignment a = 10.

### Challenge 2: Intermediate Refactoring & Bug Fix

The following loop attempts to output indices 0, 1, 2 after a delay of 100ms, but currently prints 3, 3, 3. Refactor it in **two different ways**:

1.  Fix using modern block-scoping (let).

2.  Fix using an IIFE (Immediately Invoked Function Expression) maintaining var.

// Buggy Code

for (var i = 0; i \< 3; i++) {

setTimeout(function() {

console.log(\"Index: \" + i);

}, 100);

}

*Hint*: Explain how closure and scope chain binding cause the original bug.

### Challenge 3: Advanced Execution Context Tracer

Write a lightweight custom tracer wrapper function createExecutionContextTracer(fn, fnName) from scratch that wraps any target function and logs:

- \[Pushed EC\]: \<fnName\> with arguments: \<args\>

- Execution duration in milliseconds.

- \[Popped EC\]: \<fnName\> returned: \<result\>

- Catches and logs any thrown error before re-throwing it without breaking the stack.

*Hint*: Use High-Resolution timers (performance.now()) and try\...finally block.
