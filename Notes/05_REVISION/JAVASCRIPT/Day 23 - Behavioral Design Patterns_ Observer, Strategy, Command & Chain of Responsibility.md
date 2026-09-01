---
tags:
- javascript
- design-patterns
- behavioral-patterns
- observer-pattern
- strategy-pattern
- command-pattern
- typescript
- clean-code
date: 2026-08-23
---

# Day 23 - Behavioral Design Patterns: Observer, Strategy, Command & Chain of Responsibility

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Behavioral Patterns in Modern JavaScript & TypeScript

Behavioral design patterns focus on algorithms, communication protocols, and the assignment of responsibilities between objects, increasing flexibility in carrying out complex program execution flows.

### 2. Core Behavioral Patterns

#### A. The Observer & Pub-Sub Pattern

Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically. In modern TypeScript, strong typing and clean unsubscription mechanics prevent memory leaks.

```javascript
type Listener<T> = (data: T) => void;
export class EventEmitter<TEvents extends Record<string, any>> {
private listeners: { [K in keyof TEvents]?: Set<Listener<TEvents[K]>> } = {};
```

public on<K extends keyof TEvents>(event: K, listener: Listener<TEvents[K]>): () => void {

```javascript
if (!this.listeners[event]) {
this.listeners[event] = new Set();
}
this.listeners[event]!.add(listener);
// Return unsubscription handle to avoid memory leaks
return () => this.off(event, listener);
}
```

public off<K extends keyof TEvents>(event: K, listener: Listener<TEvents[K]>): void {

```javascript
this.listeners[event]?.delete(listener);
}
```

public emit<K extends keyof TEvents>(event: K, data: TEvents[K]): void {

this.listeners[event]?.forEach((listener) => {

```javascript
try {
listener(data);
} catch (err) {
console.error(`[Event Error] in listener for ${String(event)}:`, err);
}
});
}
}
```

#### B. The Strategy Pattern

Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. It completely eliminates deeply nested if/else and switch statements.

```typescript
// Composable Strategy Pattern for Discount Calculations
export interface PricingStrategy {
calculate(basePrice: number): number;
}
export const RegularPricing: PricingStrategy = {
```

calculate: (price) => price,

```javascript
};
export const VipPricing: PricingStrategy = {
```

calculate: (price) => price * 0.85, // 15% discount

```javascript
};
export const HolidaySalePricing: PricingStrategy = {
```

calculate: (price) => Math.max(0, price * 0.7 - 10), // 30% discount + $10 voucher

```javascript
};
export class OrderCalculator {
constructor(private strategy: PricingStrategy = RegularPricing) {}
```

public setStrategy(strategy: PricingStrategy): void {

```javascript
this.strategy = strategy;
}
```

public computeTotal(basePrice: number): number {

```javascript
return this.strategy.calculate(basePrice);
}
}
```

#### C. The Command Pattern

Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support **Undo / Redo** operational history.

```typescript
export interface Command {
execute(): void;
undo(): void;
}
export class TextEditor {
private content: string = "";
```

public insert(text: string): void {

```javascript
this.content += text;
}
```

public delete(length: number): string {

```javascript
const deleted = this.content.slice(-length);
this.content = this.content.slice(0, -length);
return deleted;
}
```

public getContent(): string {

```typescript
return this.content;
}
}
export class InsertTextCommand implements Command {
constructor(private editor: TextEditor, private textToInsert: string) {}
```

execute(): void {

```javascript
this.editor.insert(this.textToInsert);
}
```

undo(): void {

```javascript
this.editor.delete(this.textToInsert.length);
}
}
export class CommandManager {
private history: Command[] = [];
private redoStack: Command[] = [];
```

public execute(command: Command): void {

```javascript
command.execute();
this.history.push(command);
this.redoStack = []; // Clear redo stack on new operation
}
```

public undo(): void {

```javascript
const command = this.history.pop();
if (command) {
command.undo();
this.redoStack.push(command);
}
}
```

public redo(): void {

```javascript
const command = this.redoStack.pop();
if (command) {
command.execute();
this.history.push(command);
}
}
}
```

#### D. The Chain of Responsibility Pattern

Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Handlers form a pipeline where each handler decides whether to process the request or pass it to the next handler in the chain.

```typescript
export interface Handler<TRequest, TResponse> {
setNext(handler: Handler<TRequest, TResponse>): Handler<TRequest, TResponse>;
handle(request: TRequest): Promise<TResponse | null>;
}
export abstract class AbstractHandler<TRequest, TResponse> implements Handler<TRequest, TResponse> {
private nextHandler: Handler<TRequest, TResponse> | null = null;
```

public setNext(handler: Handler<TRequest, TResponse>): Handler<TRequest, TResponse> {

```javascript
this.nextHandler = handler;
return handler; // Enables fluent chaining: a.setNext(b).setNext(c)
}
```

public async handle(request: TRequest): Promise<TResponse | null> {

```javascript
if (this.nextHandler) {
return this.nextHandler.handle(request);
}
return null;
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Behavioral Patterns Comparison Table:

| **Pattern** | **Primary Intent** | **Key Real-World Use Cases in JS/TS** | **Failure Mode / Pitfall** |
| --- | --- | --- | --- |
| **Observer** | 1-to-many reactive state synchronization | DOM Event Listeners, State stores, WebSockets | Memory leaks from forgotten unsubscriptions |
| **Strategy** | Interchangeable business logic algorithms | Payment gateways, Shipping costs, Auth schemes | Class explosion if functional strategies suffice |
| **Command** | Encapsulates actions for Undo/Redo & Queuing | Rich text editors, Transaction managers, CLI tools | State drift if undo() logic is non-deterministic |
| **Chain of Resp.** | Sequential request filtration & handling | Express/Fastify middlewares, Validation pipelines | Unhandled requests if chain terminus is missing |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Asynchronous Observer Ordering & Failure Isolation

Analyze the following custom event emitter execution. Predict the console output and explain why unhandled listener rejections affect subsequent subscribers:

```javascript
const emitter = new EventEmitter();
emitter.on("user:login", async (user) => {
console.log("Audit log start:", user.name);
throw new Error("DB write failed");
});
emitter.on("user:login", (user) => {
console.log("Send welcome notification:", user.name);
});
emitter.emit("user:login", { name: "Alice" });
console.log("Emit call completed.");
```

*Hint*: Differentiate between synchronous try...catch blocks and unhandled rejected Promises in synchronous forEach loops.

### Challenge 2: Refactoring Nested Order Validation into Chain of Responsibility

Refactor the following deeply nested imperative validation block into an extensible, object-oriented Chain of Responsibility pipeline where each validation step is an independent, testable handler:

```javascript
function validateOrder(order: any) {
if (!order.userId) throw new Error("Missing user");
if (!order.items || order.items.length === 0) throw new Error("Cart is empty");
if (order.totalAmount <= 0) throw new Error("Invalid total");
if (order.paymentMethod === "CREDIT" && !order.creditCardToken) throw new Error("Missing card token");
return { valid: true };
}
```

*Hint*: Each handler must inspect its specific invariant and delegate to super.handle(order).

### Challenge 3: Advanced Transactional Command Manager in TypeScript

Build a robust **Transactional Command Manager** in TypeScript:

1.  Supports **Atomic Batch Execution**: executeBatch(commands: Command[]). If any command in the batch throws an error during execute(), immediately roll back all previously executed commands in that batch in reverse order and throw a TransactionFailedException.

2.  Enforces a **Configurable Memory Cap** (e.g., maximum 50 history entries) to prevent unbounded memory growth.

3.  Provides **State Snapshotting**: Serialize state snapshots for auditing before and after each command execution.

*Hint*: Maintain an execution pointer and use a try...catch loop that invokes .undo() on completed commands when a step fails.
