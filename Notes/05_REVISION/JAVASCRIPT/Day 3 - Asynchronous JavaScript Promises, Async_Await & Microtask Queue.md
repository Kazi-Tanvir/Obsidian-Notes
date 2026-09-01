tags:

- javascript

- async-js

- promises

- async-await

- microtasks

- event-loop date: 2026-08-03

# Day 3 - Asynchronous JavaScript: Promises, Async/Await & Microtask Queue

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Promise Architecture & Internal Engine Mechanics

A **Promise** is a proxy for a value not necessarily known when the promise is created. It enables asynchronous methods to return values like synchronous methods.

#### Internal Promise Slots (ECMAScript Spec):

- \[\[PromiseState\]\]: \"pending\", \"fulfilled\", or \"rejected\".

- \[\[PromiseResult\]\]: The resolved value or rejection reason (undefined initially).

- \[\[PromiseFulfillReactions\]\]: Queue of reactions to execute when fulfilled.

- \[\[PromiseRejectReactions\]\]: Queue of reactions to execute when rejected.

- \[\[PromiseIsHandled\]\]: Boolean indicating whether a rejection handler (.catch()) has been attached. If false when rejected, triggers unhandledrejection.

// Anatomy of Promise Creation and Chaining

const fetchUserData = (userId) =\> {

return new Promise((resolve, reject) =\> {

if (!userId) {

return reject(new Error(\"User ID is required\"));

}

setTimeout(() =\> {

resolve({ id: userId, name: \"Alice\", role: \"Engineer\" });

}, 100);

});

};

fetchUserData(\"usr_101\")

.then((user) =\> {

console.log(\"User retrieved:\", user.name);

return user.role; // Automatically wrapped in a fulfilled Promise

})

.then((role) =\> console.log(\"Role:\", role))

.catch((err) =\> console.error(\"Error in chain:\", err.message))

.finally(() =\> console.log(\"Operation cleanup finished\"));

### 2. Async/Await & Engine State Machines

async/await is syntactic sugar built over Promises and Generator functions.

- An async function always implicitly returns a Promise.

- The await keyword pauses execution of the async function until the awaited Promise settles.

- Under the V8 engine, await breaks the function into execution resumption points (state machine). When await is encountered, the rest of the async function is scheduled as a microtask in the **Microtask Queue**.

// Parallel vs Sequential Execution Mechanics

async function fetchSequential(id1, id2) {

// Slow: Takes \~200ms total

const user1 = await fetchUserData(id1); // Waits 100ms

const user2 = await fetchUserData(id2); // Waits 100ms

return \[user1, user2\];

}

async function fetchParallel(id1, id2) {

// Fast: Takes \~100ms total

const promise1 = fetchUserData(id1);

const promise2 = fetchUserData(id2);

const user1 = await promise1;

const user2 = await promise2;

return \[user1, user2\];

}

### 3. Promise Combinators Comparison

JavaScript provides 4 built-in static methods for managing multiple concurrent promises:

1.  **Promise.all(\[promises\])**: Fulfilled when **ALL** promises fulfill. Rejects **immediately** if any single promise rejects (short-circuit).

2.  **Promise.allSettled(\[promises\])**: Waits for **ALL** promises to settle (either fulfill or reject). Never short-circuits. Returns an array of { status: \"fulfilled\", value } or { status: \"rejected\", reason }.

3.  **Promise.race(\[promises\])**: Settles as soon as **ANY** single promise fulfills or rejects (fastest wins).

4.  **Promise.any(\[promises\])**: Fulfilled as soon as **ANY** single promise fulfills. Rejects only if **ALL** promises reject (returns AggregateError).

// Example: Promise.allSettled Resilience Pattern

const endpoints = \[\"/api/v1/users\", \"/api/v1/posts\", \"/invalid-endpoint\"\];

async function loadDashboardData() {

const results = await Promise.allSettled(

endpoints.map((url) =\> fetch(url).then((res) =\> res.json()))

);

const successfulData = results

.filter((res) =\> res.status === \"fulfilled\")

.map((res) =\> res.value);

const failedErrors = results

.filter((res) =\> res.status === \"rejected\")

.map((res) =\> res.reason);

return { successfulData, failedErrors };

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  **Combinator**         **Fulfills When**        **Rejects When**                              **Use Case**
  ---------------------- ------------------------ --------------------------------------------- -------------------------------------------------------------
  Promise.all()          All promises fulfill     Any promise rejects (short-circuit)           All-or-nothing dependent batch operations

  Promise.allSettled()   All promises settle      Never rejects                                 Independent batch tasks where partial failure is acceptable

  Promise.race()         First promise settles    First promise settles (if it rejects first)   Timeout wrapping or fastest mirror server

  Promise.any()          First promise fulfills   All promises reject (AggregateError)          Redundant service fallback requests
  -----------------------------------------------------------------------------------------------------------------------------------------------------------

### Key Execution Rules:

- **Microtask Queue Priority**: Promise .then(), .catch(), .finally(), await, and queueMicrotask() callbacks run in the Microtask Queue, which drains completely before the Next Event Loop Phase (Timers, Poll, Check) can run.

- **Unhandled Rejections**: Always attach .catch() or use try/catch with await to prevent unhandled rejection crashes.

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Basic Execution Order & Microtask Prediction

Predict the exact line-by-line console output of the code snippet below and explain the priority between synchronous code, setTimeout, Promise.then, queueMicrotask, and async/await.

console.log(\"1. Script Start\");

setTimeout(() =\> console.log(\"2. setTimeout\"), 0);

async function asyncFn() {

console.log(\"3. Async Start\");

await Promise.resolve();

console.log(\"4. Async End\");

}

asyncFn();

Promise.resolve().then(() =\> console.log(\"5. Promise 1\"));

queueMicrotask(() =\> console.log(\"6. queueMicrotask\"));

console.log(\"7. Script End\");

*Hint*: Pay attention to what executes synchronously before await pauses asyncFn().

### Challenge 2: Intermediate Refactoring (Fault-Tolerant Batch Processor)

The following code sequentially processes an array of item IDs, but fails entirely if one item throws an error and executes slowly. Refactor processItemsBatch to:

1.  Process tasks in parallel.

2.  Limit max active concurrent promises to concurrencyLimit (e.g., max 3 at a time).

3.  Collect all errors without aborting valid items.

// Unoptimized Sequential Batch Code

async function processItemsBatch(itemIds, processFn) {

const results = \[\];

for (const id of itemIds) {

// Buggy: Sequential & unhandled rejection risk

const res = await processFn(id);

results.push(res);

}

return results;

}

*Hint*: Use a worker pool pattern or chunk array with concurrent execution handlers.

### Challenge 3: Advanced Custom Promise.allSettled Polyfill

Write a custom implementation of promiseAllSettledCustom(promises) from scratch without using built-in Promise.allSettled or Promise.all.

**Requirements**:

1.  Accepts an iterable of promises (or plain values).

2.  Returns a Promise resolving to an array of objects: { status: \'fulfilled\', value: \... } or { status: \'rejected\', reason: \... }.

3.  Handles empty input arrays immediately.

4.  Preserves exact index ordering of the input array.

*Hint*: Track settled count vs input array length and resolve parent promise when counts match.
