tags:

- javascript

- iterators

- generators

- async-generators

- streams

- memory-optimization date: 2026-08-07

# Day 7 - Iterators, Generators, Async Iteration & Custom Streams

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Iteration Protocols: Iterables & Iterators

JavaScript objects can be made iterable by implementing the **Iterable Protocol**.

- **Iterable Protocol**: An object must define a method under \[Symbol.iterator\] that returns an Iterator object.

- **Iterator Protocol**: An object with a .next() method that returns an object shaped { value: any, done: boolean }.

// Custom Range Iterable Object

const createRange = (start, end, step = 1) =\> ({

\[Symbol.iterator\]() {

let current = start;

return {

next() {

if (current \<= end) {

const value = current;

current += step;

return { value, done: false };

}

return { value: undefined, done: true };

}

};

}

});

for (const num of createRange(1, 5)) {

console.log(num); // 1, 2, 3, 4, 5

}

### 2. Generator Functions (function\* & yield)

Generators are special functions that can be paused (yield) and resumed (.next()), maintaining their execution context across suspensions.

- **yield**: Pauses generator execution and returns a value.

- **Two-Way Communication**: Passing arguments to .next(val) feeds values back into the generator where yield was invoked.

- **yield\* Delegation**: Delegates iteration to another iterable/generator.

// Two-Way Generator Data Stream

function\* conversationEngine() {

const name = yield \"What is your name?\";

const role = yield \`Hello \${name}, what is your role?\`;

return \`\${name} works as a \${role}.\`;

}

const gen = conversationEngine();

console.log(gen.next().value); // \"What is your name?\"

console.log(gen.next(\"Alice\").value); // \"Hello Alice, what is your role?\"

console.log(gen.next(\"Architect\").value); // \"Alice works as a Architect.\"

### 3. Asynchronous Iteration (Symbol.asyncIterator & async function\*)

Async Iterators handle asynchronous streams of data (e.g., paginated API responses or file chunk buffers) lazily without loading everything into memory.

// Async Generator Streaming Paginated API Data

async function\* fetchPaginatedUsers(apiUrl) {

let page = 1;

let hasMore = true;

while (hasMore) {

const response = await fetch(\`\${apiUrl}?page=\${page}\`);

const data = await response.json();

yield\* data.results; // Delegate each user item lazily

hasMore = page \< data.totalPages;

page++;

}

}

// Processing stream with \'for await\...of\'

async function processAllUsers() {

for await (const user of fetchPaginatedUsers(\"https://api.example.com/users\")) {

console.log(\`Processing user: \${user.name}\`);

}

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

  --------------------------------------------------------------------------------------------------------------
  **Protocol / Feature**      **Identifier / Syntax**                **Key Characteristics**
  --------------------------- -------------------------------------- -------------------------------------------
  **Iterable Protocol**       \[Symbol.iterator\]()                  Returns iterator with .next() method

  **Async Iterable**          \[Symbol.asyncIterator\]()             Returns iterator with async next() method

  **Generator Declaration**   function\* name() {}                   Creates GeneratorObject instance

  **Yield Value**             yield value;                           Pauses function and yields value

  **Yield Delegation**        yield\* iterable;                      Delegates control to another iterable

  **Async Loop**              for await (const x of asyncIterable)   Consumes Async Iterables sequentially
  --------------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Generator Yield Delegation & State Prediction

Predict the exact execution trace and output values returned by the following generator sequence.

function\* innerGenerator() {

const x = yield \"Inner 1\";

yield \`Inner 2: \${x}\`;

}

function\* outerGenerator() {

yield \"Start\";

const result = yield\* innerGenerator();

yield \"End\";

}

const gen = outerGenerator();

console.log(gen.next().value);

console.log(gen.next().value);

console.log(gen.next(\"PassToInner\").value);

console.log(gen.next().value);

*Hint*: Pay attention to how .next() inputs map to yield expressions inside delegated generators.

### Challenge 2: Memory Optimization via Lazy Infinite Stream Generator

The following code loads a 1,000,000 item dataset into memory at once, causing heap memory spikes. Refactor it into a memory-efficient Generator function that generates Fibonacci numbers lazily up to \$N\$.

// Buggy / High Memory Usage

function getFibonacciUpToN(n) {

const sequence = \[0, 1\];

for (let i = 2; i \< n; i++) {

sequence.push(sequence\[i - 1\] + sequence\[i - 2\]);

}

return sequence; // Allocates large array in heap

}

*Hint*: Use a while(true) generator loop with yield to maintain \$O(1)\$ memory footprint.

### Challenge 3: Advanced Async Stream Pipeline Processor

Implement a custom function asyncPipeGenerators(\...generatorTransforms) from scratch that accepts an Async Generator source and pipes it through multiple async transformation functions.

**Requirements**:

1.  Supports chaining transformations (e.g. map, filter, batch).

2.  Streams item by item without buffering entire collections in memory.

3.  Handles thrown errors gracefully by calling .return() on upstream iterators to clean up resources.

*Hint*: Each transformer should be an async function\* that consumes for await\...of from the previous source.
