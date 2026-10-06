tags:

- javascript

- decorators

- metaprogramming

- tc39

- explicit-resource-management

- typescript

- architecture

- modern-javascript date: 2026-09-21

# Day 52 - Modern ECMAScript Metaprogramming: TC39 Stage 3 Decorators, Decorator Metadata & Explicit Resource Management

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Great Decorator Evolution: Legacy vs. TC39 Standard

For almost a decade, JavaScript developers relied on TypeScript\'s
\--experimentalDecorators (Stage 1 / 2014 proposal). However, legacy
decorators suffered from severe architectural flaws:

- **Global Mutation**: Legacy decorators mutated target prototypes
  directly without clear runtime boundaries.

- **External Reflection Dependency**: Required the bulky
  reflect-metadata polyfill and TypeScript-only metadata emission
  (emitDecoratorMetadata), leaking types into production bundles.

- **Incompatible with Standard JS**: They were a non-standard TypeScript
  quirk rather than official ECMAScript.

**TC39 Stage 3 Decorators** (standardized in ECMAScript 2023/2024+)
establish a first-class, standardized metaprogramming model across all
modern JavaScript engines (V8, SpiderMonkey, JavaScriptCore):

1.  **Pure Functional Composition**: Decorators do not mutate classes
    arbitrarily; they are pure functions that wrap, transform, or
    replace classes and class elements.

2.  **Standard Decorator Context**: Every decorator receives a
    strongly-typed context object containing metadata, member kind,
    name, accessors, and lifecycle initializers.

3.  **First-Class Decorator Metadata (Symbol.metadata)**: Native runtime
    metadata storage directly on the constructor, eliminating the need
    for reflect-metadata.

┌────────────────────────────────────── TC39 Decorator Execution Flow
──────────────────────────────────────┐

│ │

│ Class Definition Evaluated: │

│ \@logged │

│ class AccountService { │

│ \@memoize │

│ calculateBalance() { \... } │

│ } │

│ │

│ Evaluation & Application Order: │

│ 1. Decorator Expressions Evaluated: Top-to-Bottom (like function
arguments) │

│ 2. Member Decorators Applied: Bottom-up, Inside-Out (calculateBalance
decorated first) │

│ 3. Class Decorator Applied: After all member decorators have completed
│

│ 4. Initializers Invoked: context.addInitializer() runs during instance
construction │

│ │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. The 5 Member Decorator Kinds & The accessor Keyword

TC39 defines distinct decorator signatures based on what element is
being decorated:

  -----------------------------------------------------------------------
  **Kind**                **Target**              **Decorator Return
                                                  Value**
  ----------------------- ----------------------- -----------------------
  class                   Class constructor       Replacement constructor
                                                  or void

  method                  Class method            Replacement function or
                                                  void

  getter / setter         Property getter /       Replacement getter /
                          setter                  setter or void

  field                   Instance field          Initializer transformer
                                                  (initialValue: T) =\> T

  accessor                Auto-accessor field     Object with { get?,
                                                  set?, init? }
  -----------------------------------------------------------------------

#### The New accessor Keyword:

Traditional fields (name = \"Tamim\") cannot be intercepted by
getters/setters without rewriting class prototypes. The accessor keyword
introduces an **auto-accessor** that desugars into a private storage
slot with auto-generated getter/setter methods:

// Implementing a Reactive Auto-Accessor Decorator

function observed\<T, V\>(

target: ClassAccessorDecoratorTarget\<T, V\>,

context: ClassAccessorDecoratorContext\<T, V\>

): ClassAccessorDecoratorResult\<T, V\> {

const { get, set } = target;

return {

get() {

const value = get.call(this);

console.log(\`\[GET\] \${String(context.name)} =\>\`, value);

return value;

},

set(newValue: V) {

console.log(\`\[SET\] \${String(context.name)} from\`, get.call(this),
\'to\', newValue);

set.call(this, newValue);

},

init(initialValue: V) {

console.log(\`\[INIT\] \${String(context.name)} with\`, initialValue);

return initialValue;

}

};

}

class UserProfile {

\@observed accessor username: string = \'tamim_dev\';

}

### 3. Native Decorator Metadata (Symbol.metadata)

TC39 standardizes runtime reflection without third-party libraries via
context.metadata. All decorators applied to a class share the exact same
metadata dictionary:

// An API Routing Decorator using native Symbol.metadata

function Route(path: string) {

return function (target: Function, context: ClassMethodDecoratorContext)
{

if (context.kind !== \'method\') throw new Error(\'@Route can only
decorate methods\');

// Attach metadata to the class\'s Symbol.metadata dictionary

const metadata = context.metadata;

metadata.routes = metadata.routes \|\| \[\];

(metadata.routes as Array\<{ path: string; methodName: string \| symbol
}\>).push({

path,

methodName: context.name,

});

};

}

class PaymentController {

\@Route(\'/api/v1/charge\')

processPayment() { return { status: \'ok\' }; }

\@Route(\'/api/v1/refund\')

processRefund() { return { status: \'refunded\' }; }

}

// Inspecting metadata directly from the class constructor:

const routes = (PaymentController as any)\[Symbol.metadata\]?.routes;

console.log(routes);

// Output: \[ { path: \'/api/v1/charge\', methodName: \'processPayment\'
}, \... \]

### 4. Explicit Resource Management: The using Keyword & RAII in JS

Resource leaks (unclosed database transactions, forgotten file handles,
dangling Web Workers, unreleased mutexes) are a primary source of memory
bloat and deadlocks. Inspired by C# using, Python with, and Rust\'s RAII
(Resource Acquisition Is Initialization), TC39 introduces **Explicit
Resource Management**:

#### The Disposable Contract (Symbol.dispose & Symbol.asyncDispose):

// Implementing a Database Transaction Disposable

class ScopedTransaction implements Disposable {

private active = true;

constructor(private txId: string) {

console.log(\`\[BEGIN\] Transaction \${this.txId}\`);

}

commit() {

this.active = false;

console.log(\`\[COMMIT\] Transaction \${this.txId}\`);

}

// Invoked AUTOMATICALLY when block scope exits!

\[Symbol.dispose\]() {

if (this.active) {

console.warn(\`\[ROLLBACK\] Transaction \${this.txId} rolled back due to
unhandled error or early return!\`);

}

}

}

function transferFunds(from: string, to: string, amount: number) {

// \'using\' guarantees cleanup as soon as the block terminates!

using tx = new ScopedTransaction(\'tx-9821\');

if (amount \<= 0) {

return; // tx\[Symbol.dispose\]() automatically called! Rollback logged!

}

// Perform database mutations\...

tx.commit();

} // tx\[Symbol.dispose\]() called here automatically!

## SECTION 2: DOCUMENTATION CHEAT SHEET

### TC39 Decorator Context Object API:

  ---------------------------------------------------------------------------------
  **Property**            **Type**                **Description**
  ----------------------- ----------------------- ---------------------------------
  kind                    string                  \'class\', \'method\',
                                                  \'getter\', \'setter\',
                                                  \'field\', \'accessor\'.

  name                    string \| symbol        Name of the decorated element.

  static                  boolean                 true if static member; false if
                                                  instance member.

  private                 boolean                 true if declared with
                                                  #privateName.

  access                  object                  Object containing { has, get, set
                                                  } functions to inspect/mutate the
                                                  value.

  metadata                object                  Shared inheritance-preserving
                                                  dictionary attached to
                                                  Constructor\[Symbol.metadata\].

  addInitializer          (fn: Function) =\> void Registers an initialization hook
                                                  executed during construction or
                                                  class definition.
  ---------------------------------------------------------------------------------

### Explicit Resource Management Keywords:

// Synchronous Disposable:

using resource = acquireResource(); // Must implement
\[Symbol.dispose\](): void

// Asynchronous Disposable:

await using asyncResource = acquireAsyncResource(); // Must implement
\[Symbol.asyncDispose\](): Promise\<void\>

## SECTION 3: PRACTICAL PROBLEMS

### Problem 1 (Basic): Safe Execution Guard & Timing Decorator

**Context**: In production micro-frontends, flaky remote RPC calls must
be timed accurately and wrapped in structured telemetry logs without
scattering try/catch and performance.now() across business services.

**Challenge**: Implement a method decorator \@MeasureLatency:

1.  Validates that it is only applied to methods (context.kind ===
    \'method\').

2.  Wraps asynchronous and synchronous method executions.

3.  Records total execution duration using performance.now().

4.  If the execution exceeds a threshold maxDurationMs, dispatches a
    warning log containing the class name, method name, and latency.

5.  Injects the execution time into context.metadata.telemetryMetrics.

*Hint: Remember to maintain the lexical this binding using
target.apply(this, args) inside the replacement method wrapper.*

### Problem 2 (Intermediate): Enterprise Dependency Injection (DI) Container via Decorator Metadata

**Context**: Traditional IoC containers (like NestJS or Inversify)
require bulky reflect-metadata shims and TypeScript compiler flags.
Modern architectures require clean, zero-dependency TC39 decorator
injection.

**Challenge**: Build a lightweight Dependency Injection framework using
native Symbol.metadata:

1.  \@Injectable(token?: string): Class decorator that registers the
    class factory inside a singleton Container registry.

2.  \@Inject(token: string): Field or Auto-Accessor decorator that
    stores dependency tokens in context.metadata.

3.  In context.addInitializer(), resolves the requested dependency token
    from the Container and initializes the field automatically upon
    instance creation.

4.  Handles circular dependency detection by throwing a descriptive
    CircularDependencyError.

*Hint: Use context.addInitializer(function(this: any) { \... }) to
populate instance properties before the constructor body executes.*

### Problem 3 (Advanced): Lock-Guarded Async Mutex with await using Disposable

**Context**: Concurrent Node.js or browser web worker operations (e.g.
updating an IndexedDB ledger or coordinating a shared WebSocket state)
suffer from race conditions unless guarded by an asynchronous mutual
exclusion lock.

**Challenge**: Implement an enterprise-grade AsyncMutex coordinating
access with deterministic await using cleanup:

1.  class AsyncMutex:

    - Maintains a FIFO queue of waiting promises.

    - acquire(): Promise\<AsyncMutexGuard\>: Resolves as soon as the
      lock is granted.

2.  class AsyncMutexGuard implements AsyncDisposable:

    - Holds an active lock on the mutex.

    - Implements \[Symbol.asyncDispose\](): Promise\<void\> which
      immediately releases the lock, permitting the next queued
      operation to proceed.

3.  Write test scenarios demonstrating that:

    - 10 concurrent async tasks execute in strict serial order without
      overlapping critical sections.

    - Even if an asynchronous task throws an unhandled rejection, await
      using guard = await mutex.acquire() guarantees the lock is
      immediately released without deadlocking subsequent callers.

*Hint: The mutex guard must call mutex.release() inside its
\[Symbol.asyncDispose\]() implementation.*
