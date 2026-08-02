---

tags:

- backend  
- nodejs  
- event-loop  
- async-io  
- libuv  
- worker-threads date: 2026-08-02

---

# Day 2 \- Advanced Node.js Event Loop, Asynchronous I/O & Worker Threads

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1\. Node.js Architecture: V8, libuv & C++ Bindings

Node.js is an asynchronous, event-driven JavaScript runtime. It is built on three core pillars:

1. **Google V8 Engine**: Compiles JavaScript into native machine code, manages Call Stack & Memory Heap.  
2. **libuv (C Library)**: Multi-platform C library that handles the Event Loop, Thread Pool (`UV_THREADPOOL_SIZE`), non-blocking asynchronous I/O (epoll on Linux, kqueue on macOS, IOCP on Windows), and timers.  
3. **C++ Bindings & Core Modules**: Connects JS code (e.g., `fs`, `net`, `crypto`, `http`) with underlying C/C++ libuv primitives.

\+-------------------------------------------------------+

|                   Node.js Application                 |

\+-------------------------------------------------------+

|            Node.js Standard Library (JS)              |

\+-------------------------------------------------------+

|             Node.js C++ Bindings / Addons             |

\+---------------------------+---------------------------+

|      V8 JS Engine         |       libuv (C)           |

| (Call Stack / Memory Heap) | (Event Loop, Thread Pool) |

\+---------------------------+---------------------------+

---

### 2\. The 6 Phases of the libuv Event Loop

When Node.js starts, it initializes the Event Loop. Each iteration of the Event Loop is called a **Tick**. The Event Loop moves sequentially through 6 phases:

1. **Timers Phase**: Executes callbacks scheduled by `setTimeout()` and `setInterval()`.  
2. **Pending Callbacks Phase**: Executes I/O callbacks deferred from the previous loop iteration (e.g. TCP errors).  
3. **Idle, Prepare Phase**: Used internally by libuv for system maintenance.  
4. **Poll Phase**:  
   - Calculates block wait time and retrieves new I/O events.  
   - Executes callbacks for I/O (files, network, databases).  
   - If poll queue is empty, checks for `setImmediate()` callbacks. If present, transitions to Check Phase.  
5. **Check Phase**: Executes callbacks scheduled by `setImmediate()`.  
6. **Close Callbacks Phase**: Executes close handlers (e.g. `socket.on('close', ...)`).

#### Microtask Priority (Between Phases):

Before transitioning to the next phase, Node.js drains:

1. `process.nextTick()` queue (highest priority).  
2. Promise Microtask queue (`queueMicrotask` / resolved Promise `.then()`).

// Execution Order Demonstration

console.log("1. Sync Main Execution");

setTimeout(() \=\> console.log("2. Timers Phase (setTimeout)"), 0);

setImmediate(() \=\> console.log("3. Check Phase (setImmediate)"));

Promise.resolve().then(() \=\> console.log("4. Promise Microtask"));

process.nextTick(() \=\> console.log("5. process.nextTick"));

console.log("6. Sync End");

/\*

Output Order:

1\. Sync Main Execution

6\. Sync End

5\. process.nextTick

4\. Promise Microtask

2\. Timers Phase (setTimeout)

3\. Check Phase (setImmediate)

\*/

---

### 3\. Offloading CPU-Bound Work: Worker Threads vs Thread Pool

- **libuv Thread Pool**: Default 4 threads (configurable up to 1024 via `UV_THREADPOOL_SIZE=16`). Used for file I/O (`fs`), DNS lookups (`dns.lookup`), and crypto/zlib operations.  
- **Worker Threads (`worker_threads`)**: Enables running CPU-bound JavaScript execution in parallel across true OS threads sharing memory via `ArrayBuffer` / `SharedArrayBuffer`.

// Main Thread: offloadHeavyTask.ts

import { Worker } from 'worker\_threads';

import path from 'path';

export function runCpuHeavyTask(data: number): Promise\<number\> {

  return new Promise((resolve, reject) \=\> {

    const worker \= new Worker(path.resolve(\_\_dirname, './worker.js'), {

      workerData: data

    });

    worker.on('message', resolve);

    worker.on('error', reject);

    worker.on('exit', (code) \=\> {

      if (code \!== 0\) reject(new Error(\`Worker stopped with exit code ${code}\`));

    });

  });

}

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

| API / Concept | Category | Execution Phase / Mechanism | Primary Use Case |
| :---- | :---- | :---- | :---- |
| `process.nextTick()` | Microtask | Drains immediately after current operation completes | Deferring execution before next event loop phase |
| `Promise.then()` | Microtask | Drains immediately after `nextTick` queue | Asynchronous resolution / chaining |
| `setTimeout(fn, 0)` | Timers Phase | Executed in Timers phase after minimum threshold | Scheduled delayed tasks |
| `setImmediate(fn)` | Check Phase | Executed in Check phase immediately after Poll phase | I/O completion callbacks |
| `UV_THREADPOOL_SIZE` | Environment Var | Configures libuv C thread pool size | Scaling file I/O & crypto concurrency |
| `worker_threads` | Module | Spawns separate V8 isolates & OS threads | Heavy CPU calculation without blocking event loop |

### Environment Setup Commands:

\# Increase libuv thread pool size for high-concurrency Node.js crypto/file server

export UV\_THREADPOOL\_SIZE=16

node server.js

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Architecture Design (CPU-bound Rate-Limited Task Queue)

Design an asynchronous CPU-intensive Video Transcoding & Hashing Pipeline for a Node.js backend.

**Requirements**:

1. Draw the architectural request flow showing API Gateway, Main Event Loop, Worker Thread Pool, and Redis Queue.  
2. Specify how the main Node.js Event Loop remains responsive under 10,000 concurrent API requests while offloading heavy hashing tasks.  
3. Define the error recovery, task timeout, and worker thread lifecycle management strategy.

---

### Problem 2: End-to-End Code Implementation Challenge

Build a resilient **Worker Thread Pool Manager** class in TypeScript from scratch.

**Requirements**:

1. Implement `WorkerPool` class accepting `poolSize` and `workerScriptPath`.  
2. Maintain a queue of pending tasks when all workers are busy.  
3. Automatically replace crashed workers without dropping queued jobs.  
4. Expose `exec(taskData: any): Promise<any>` and `destroy(): Promise<void>`.  
5. Provide unit test scenarios simulating 20 concurrent tasks dispatched across 4 workers.

