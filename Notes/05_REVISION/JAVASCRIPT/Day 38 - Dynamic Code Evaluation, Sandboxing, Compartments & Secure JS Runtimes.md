---
tags:
  - javascript
  - security
  - sandboxing
  - eval
  - compartments
  - v8-isolates
  - nodejs
  - vm
date: 2026-09-07
---

# Day 38 - Dynamic Code Evaluation, Sandboxing, Compartments & Secure JS Runtimes

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Hazards of Dynamic Evaluation in JavaScript

Dynamic code execution has existed in JavaScript since its inception through `eval()`, `new Function()`, and string-based timers (`setTimeout("code", 100)`). In enterprise software, these mechanisms pose catastrophic security and performance hazards:

1. **Arbitrary Code Execution & Prototype Hijacking**: Untrusted input executed in `eval()` inherits complete execution privileges, exposing file systems, process environment variables, and network sockets.
2. **Engine De-Optimization**: Direct `eval()` forces the V8 engine to retain the entire lexical scope environment and disables TurboFan optimizations because variable identifier resolutions cannot be statically analyzed at compile time.
3. **Direct vs. Indirect Eval**:
   - **Direct Eval**: `eval("...")` executes within the local lexical scope, capable of reading and mutating local variables.
   - **Indirect Eval**: `(0, eval)("...")` or `const geval = eval; geval("...")` executes strictly in the global scope, preventing local variable leakage but still having full access to global state.

┌────────────────────────────────────── The Dynamic Execution Spectrum ──────────────────────────────────────┐

│                                                                                                              │

│  Unsafe: Local Scope Access                                                                                  │

│  eval("code") ────────────────────────► Reads & mutates caller's local scope. De-optimizes entire function.  │

│                                                                                                              │

│  Marginally Safer: Global Scope Only                                                                         │

│  (0, eval)("code") / new Function() ──► Executes in Global Scope. Cannot access local variables.             │

│                                         (Still accesses `globalThis`, `process`, and prototypes!)            │

│                                                                                                              │

│  Flawed Isolation: Node.js VM                                                                                │

│  vm.runInContext(code, context) ──────► Escapable via constructor chaining:                                  │

│                                         `this.constructor.constructor("return process")()`                  │

│                                                                                                              │

│  True Process/Engine Isolation:                                                                              │

│  isolated-vm / WebAssembly ──────────► Separate V8 Isolate, separate memory heap, strict CPU/RAM limits.     │

│                                                                                                              │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. Why Node.js `node:vm` Is Not a Security Sandbox

Developers frequently attempt to use `node:vm` (`vm.createContext`, `vm.runInContext`) to execute user-submitted plugins or untrusted scripts. **Node.js documentation explicitly warns: `node:vm` is not a security sandbox.**

#### The Classical Sandbox Escape:

Objects passed into a `node:vm` context share the same underlying V8 prototype chain as the host process. An attacker can traverse the prototype chain back to the host `Function` constructor:

const vm \= require('node:vm');

// Naive sandbox attempt

const sandbox \= { data: 'user-input' };

vm.createContext(sandbox);

// Malicious payload escaping the sandbox:

const maliciousCode \= `

  const foreignObject \= this.data;

  const HostFunction \= foreignObject.constructor.constructor;

  const process \= HostFunction('return process')();

  process.mainModule.require('child\_process').execSync('whoami').toString();

`;

const result \= vm.runInContext(maliciousCode, sandbox);

console.log('Attacker gained host shell access:', result);

---

### 3. Modern Production Isolation: V8 Isolates & Hardened JavaScript (SES)

To safely execute untrusted multi-tenant JavaScript in production, architects utilize two proven patterns:

#### 1. V8 Isolates via `isolated-vm`

A **V8 Isolate** is a completely independent instance of the V8 JavaScript engine with its own heap manager, garbage collector, and execution thread.

- Memory cannot leak between isolates.
- CPU timeouts are enforced by V8 runtime interrupts.
- Memory size is hard-capped (e.g. 16MB) at the C++ level.

import ivm from 'isolated-vm';

async function runUntrustedCode(userCode: string): Promise<string> {

  // 1. Create a fresh V8 Isolate with hard 16MB memory limit

  const isolate \= new ivm.Isolate({ memoryLimit: 16 });

  // 2. Create isolated context inside the isolate

  const context \= await isolate.createContext();

  const jail \= context.global;

  await jail.set('global', jail.derefInto());

  // 3. Inject safe, copied primitives (No prototype sharing!)

  await jail.set('log', new ivm.Reference((msg: string) \=> {

    console.log('[Isolated Sandbox]:', msg);

  }));

  // 4. Compile and run with a strict 50ms CPU execution deadline

  const script \= await isolate.compileScript(userCode);

  const result \= await script.run(context, { timeout: 50 });

  // 5. Clean up isolate memory immediately

  isolate.dispose();

  return String(result);

}

#### 2. Hardened JavaScript & TC39 Compartments (SES - Secure ECMAScript)

Pioneered by Agoric and the TC39 security working group, **Compartments** freeze all native prototypes (`Object.prototype`, `Array.prototype`) using `Object.freeze()` before evaluating code in an isolated scope with custom import hooks.

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Sandboxing & Evaluation Mechanisms Comparison Matrix:

| Technology | Scope Isolation | Heap Isolation | CPU Timeouts | Memory Hard Caps | Security Boundary |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `eval()` / `Function()` | None | Shared | No | No | ❌ Severe Risk |
| `node:vm` | Contextual | Shared | Wall-clock only | No | ❌ Escapable |
| `Web Workers` (Browser) | Script | Shared Origin | Cooperative only | Quota-based | ⚠️ Same Origin DOM Leak |
| **`isolated-vm` (Node.js)** | Complete | **Independent** | **Preemptive (Microsecond)** | **Enforced (MB)** | ✅ **Production Secure** |
| **Wasm Sandbox (Wasmtime)** | Complete | **Linear Memory** | **Instruction Fuel** | **Enforced (Pages)** | ✅ **Military Grade** |

---

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Prototype-Defended Context in `node:vm`

Analyze the following attempts to secure `node:vm`:

const sandbox \= Object.create(null);

sandbox.print \= (msg) \=> console.log(msg);

vm.createContext(sandbox);

*Question*: Despite using `Object.create(null)`, explain how an attacker can still reach the host `Function` constructor through an arrow function or object literal returned by the sandbox. What specific prototype properties must be severed or frozen?

---

### Challenge 2: Safe Domain-Specific Math Expression Evaluator

Build a high-performance, completely safe mathematical expression evaluator in TypeScript:

1. Must parse and evaluate expressions like `"2 * (x + 5) - Math.sqrt(y)"`.
2. Strictly forbid `eval()`, `new Function()`, or `node:vm`.
3. Tokenize and parse into an Abstract Syntax Tree (AST), validating that only approved identifiers (`Math.sqrt`, numbers, arithmetic operators, allowed variables) are present.
4. Execute via recursive AST interpretation with zero security exposure.

---

### Challenge 3: Multi-Tenant Plugin Execution Sandbox in TypeScript

Build an Enterprise **Multi-Tenant Plugin Execution Engine** in TypeScript using `isolated-vm`:

**Requirements**:

1. **Isolate Lifecycle & Pool**:
   - Manages a warm pool of V8 Isolates with a 16MB memory ceiling per tenant.
2. **Strict Timeouts & Memory Guards**:
   - Enforces a 50ms preemptive CPU timeout per plugin invocation. Catches and reports timeout errors gracefully without crashing the parent process.
3. **Controlled Bidirectional Bridge**:
   - Exposes a safe logging method and a key-value storage retrieval API (`storage.get(key)`) across the isolate boundary using `ivm.Reference` and `ivm.Callback`.
4. **Isolate Disposal & Zero-Leak Guarantees**:
   - Guarantees immediate cleanup of the isolate instance and its memory context upon execution completion or termination.

