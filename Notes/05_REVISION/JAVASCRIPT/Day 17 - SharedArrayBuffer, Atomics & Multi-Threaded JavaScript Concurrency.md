tags:

- javascript

- shared-array-buffer

- atomics

- concurrency

- web-workers

- multithreading

- v8-memory date: 2026-08-17

# Day 17 - SharedArrayBuffer, Atomics & Multi-Threaded JavaScript Concurrency

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. True Shared Memory vs. Structured Cloning

Standard Web Worker communication via postMessage() relies on **Structured Cloning**, which deep-copies data across memory boundaries, or **Transferable Objects**, which transfer ownership (\$O(1)\$ zero-copy) but detach the buffer from the sending thread.

**SharedArrayBuffer (SAB)** introduces true shared memory in JavaScript, allowing multiple Web Workers and the main thread to read and write to the exact same physical byte addresses concurrently.

#### The Security Prerequisite (Cross-Origin Isolation):

Due to CPU side-channel attacks (Spectre/Meltdown), SharedArrayBuffer is disabled by default in browsers unless the server sends strict **Cross-Origin Isolation** HTTP response headers:

Cross-Origin-Opener-Policy: same-origin

Cross-Origin-Embedder-Policy: require-corp

### 2. Race Conditions & The Atomics Object

When multiple worker threads mutate shared memory simultaneously without synchronization, **race conditions** occur, leading to data corruption and lost updates.

JavaScript provides the static **Atomics** global object to execute indivisible (atomic) read-modify-write operations guaranteed to be sequential and free from interleaving thread interference.

// Shared Memory Setup

const sharedBuffer = new SharedArrayBuffer(16); // 16 bytes

const sharedInt32 = new Int32Array(sharedBuffer); // 4 integer slots

// Worker 1 & Worker 2 executing concurrently:

// BAD: Non-atomic increment causes lost updates under contention!

// sharedInt32\[0\] += 1;

// GOOD: Indivisible Atomic Addition guaranteed at hardware CPU level

const previousValue = Atomics.add(sharedInt32, 0, 1);

console.log(\`Updated value. Previous was: \${previousValue}\`);

### 3. Thread Synchronization: Atomics.wait() and Atomics.notify()

To prevent CPU-burning while(true) polling loops in background workers, JavaScript provides a low-level sleeping/waking synchronization primitive:

- **Atomics.wait(typedArray, index, value, timeout)**: Suspends the calling worker thread until the value at typedArray\[index\] changes or Atomics.notify() is called. *(Note: Forbidden on the main browser thread to prevent UI freezing).*

- **Atomics.notify(typedArray, index, count)**: Wakes up count worker threads sleeping on that specific buffer index.

// Worker Thread: Sleeping until signaled

const stateArray = new Int32Array(sharedBuffer);

const INDEX_STATE = 0;

const EXPECTED_VALUE = 0;

console.log(\"\[Worker\]: Entering sleep state\...\");

// Sleeps indefinitely until index 0 is no longer 0, or notified

const waitResult = Atomics.wait(stateArray, INDEX_STATE, EXPECTED_VALUE);

console.log(\`\[Worker\]: Awakened! Status: \${waitResult}\`); // \"ok\" \| \"not-equal\" \| \"timed-out\"

// Main / Coordinator Thread: Awakening worker

Atomics.store(stateArray, INDEX_STATE, 1); // Mutate state

Atomics.notify(stateArray, INDEX_STATE, 1); // Wake 1 sleeping worker

### 4. Advanced Atomic Operations

- **Atomics.compareExchange(typedArray, index, expectedVal, replacementVal)**: Compares current value with expectedVal; if equal, atomically replaces it with replacementVal and returns the old value. Foundational for **Lock-Free** algorithms.

- **Atomics.exchange(typedArray, index, val)**: Stores value and returns previous value in one atomic step.

- **Atomics.isLockFree(size)**: Validates if operations on \$1, 2, 4, 8\$-byte arrays are supported by native hardware lock-free CPU instructions.

## SECTION 2: DOCUMENTATION CHEAT SHEET

  -------------------------------------------------------------------------------------------------------------------------------------------------
  **Atomic Method**             **Signature**                                 **Action / Description**
  ----------------------------- --------------------------------------------- ---------------------------------------------------------------------
  **Atomics.add**               Atomics.add(arr, idx, val)                    Atomically adds val to arr\[idx\] and returns previous value

  **Atomics.sub**               Atomics.sub(arr, idx, val)                    Atomically subtracts val from arr\[idx\] and returns previous value

  **Atomics.load**              Atomics.load(arr, idx)                        Atomically reads and returns value with memory barrier

  **Atomics.store**             Atomics.store(arr, idx, val)                  Atomically writes val and returns val with memory barrier

  **Atomics.compareExchange**   Atomics.compareExchange(arr, idx, exp, rep)   Replaces arr\[idx\] with rep IF current equals exp

  **Atomics.wait**              Atomics.wait(int32Arr, idx, exp, timeout?)    Blocks worker thread while int32Arr\[idx\] === exp

  **Atomics.notify**            Atomics.notify(int32Arr, idx, count)          Wakes up count worker threads blocked on arr\[idx\]
  -------------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Race Condition Verification & Contention Prediction

Given 4 Web Workers running in parallel, each attempting to increment an index \$100,000\$ times:

1.  Explain what value sharedArray\[0\] will contain if using standard assignment sharedArray\[0\]++.

2.  Explain why Atomics.add(sharedArray, 0, 1) guarantees exactly \$400,000\$ as the final counter.

// Worker task:

for (let i = 0; i \< 100000; i++) {

// Non-atomic: Read -\> Add -\> Write (3 separate CPU instructions)

// Atomic: Single atomic hardware fetch-and-add instruction

}

*Hint*: Focus on CPU context-switching and interleaved assembly instructions during read-modify-write cycles.

### Challenge 2: Eliminating Busy-Wait Polling with Atomics.wait/notify

Refactor a CPU-heavy worker spin-lock loop (while (sharedArray\[0\] === 0) {}) into an energy-efficient sleeping synchronization mechanism using Atomics.wait() and Atomics.notify().

// Bad Anti-Pattern: Consumes 100% CPU core spinning

function waitForJob(sharedState) {

while (sharedState\[0\] === 0) {

// Busy wait wasting battery and CPU cycles!

}

processJob();

}

*Hint*: Use Atomics.wait(sharedState, 0, 0) in the worker and Atomics.notify(sharedState, 0, 1) in the dispatcher.

### Challenge 3: Building a Lock-Free Single-Producer Single-Consumer (SPSC) Ring Buffer

Build a high-performance **LockFreeRingBuffer** in TypeScript using SharedArrayBuffer and Atomics:

1.  Use a designated 16-byte header: \[HeadIndex, TailIndex, Capacity, Flags\].

2.  Implement push(value: number): boolean for Producer Worker (returns false if buffer full).

3.  Implement pop(): number \| null for Consumer Worker (returns null if buffer empty).

4.  Enforce strict memory consistency using Atomics.load and Atomics.store without relying on mutex locks.

*Hint*: Use modulo arithmetic for circular indexing and atomic pointers for head/tail increments.
