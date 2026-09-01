---
tags:
- javascript
- error-handling
- stack-trace
- custom-errors
- v8-engine
- async-errors
date: 2026-08-12
---

# Day 12 - Error Handling, Custom Errors, Async Error Boundaries & Stack Trace Manipulation

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The JavaScript Error Object & V8 Stack Trace Mechanics

In JavaScript, an Error object represents an exceptional condition. When an error is instantiated, the V8 engine captures a call stack snapshot formatted as a string in error.stack.

#### Standard Error Hierarchy:

- Error: Base class for all runtime errors.

- Built-in subtypes: TypeError, ReferenceError, SyntaxError, RangeError, URIError, AggregateError.

#### Stack Trace Hiding with Error.captureStackTrace:

In library or framework development, internal helper stack frames clutter stack traces. V8's non-standard Error.captureStackTrace(targetObject, constructorOpt) hides internal helper frames from end users.

```javascript
class DomainError extends Error {
constructor(message, statusCode = 500) {
super(message);
this.name = this.constructor.name;
this.statusCode = statusCode;
this.timestamp = new Date().toISOString();
// Omits constructor frame from stack trace for clean debugging
if (Error.captureStackTrace) {
Error.captureStackTrace(this, this.constructor);
}
}
}
class ValidationError extends DomainError {
constructor(message, details = []) {
super(message, 400);
this.details = details;
}
}
try {
throw new ValidationError("Invalid payload", ["email is required"]);
} catch (err) {
console.log(err.name); // ValidationError
console.log(err.statusCode); // 400
console.log(err.stack); // Stack trace starts directly at throw site!
}
```

### 2. Error Cause Chaining (Error.cause)

ES2022 introduced the cause option in Error constructors, allowing developers to wrap low-level system errors inside high-level domain errors without losing the original root cause stack trace.

```javascript
async function fetchUserProfile(userId) {
try {
const response = await fetch(`/api/users/${userId}`);
if (!response.ok) throw new Error(`HTTP ${response.status}`);
return await response.json();
} catch (networkError) {
// Contextual Error Wrapping
throw new DomainError(`Failed to load profile for user ${userId}`, {
```

cause: networkError,

```javascript
});
}
}
```

### 3. Global Uncaught Exception & Promise Rejection Handlers

Async errors that escape try/catch or .catch() bubble up to global runtime error hooks.

```javascript
// Browser Global Error Handlers
window.addEventListener('error', (event) => {
console.error('Global Uncaught Error:', event.error);
});
window.addEventListener('unhandledrejection', (event) => {
console.error('Unhandled Promise Rejection Reason:', event.reason);
event.preventDefault(); // Prevents console error spam
});
// Node.js Global Error Handlers
process.on('uncaughtException', (err) => {
console.fatal('Fatal Uncaught Exception:', err);
process.exit(1); // Recommended: Exit process gracefully
});
process.on('unhandledRejection', (reason, promise) => {
console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Error API / Property** | **Usage / Syntax** | **Purpose** |
| --- | --- | --- |
| **Error.captureStackTrace** | Error.captureStackTrace(this, CustomConstructor) | Truncates stack trace at constructor boundary |
| **Error.cause** | new Error("msg", { cause: originalErr })             P | eserves root cause in error wrapper chains |
| **AggregateError** | new AggregateError([err1, err2], "Batch failed")   Gro | ps multiple errors into a single exception |
| **window.onunhandledrejection** | window.addEventListener('unhandledrejection', fn)    C | tches unhandled async Promise rejections |
| **process.on('uncaughtException')**   p | ocess.on('uncaughtException', fn)                  Nod | .js process guard for synchronous exceptions |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Stack Trace & Error Cause Output Prediction

Analyze the following nested error chain and predict what err.message and err.cause.message will output. Explain why Error.captureStackTrace alters the printed stack trace lines.

```javascript
function innerDatabaseCall() {
const err = new Error("Connection Timeout");
Error.captureStackTrace(err, innerDatabaseCall);
throw err;
}
function serviceLayer() {
try {
innerDatabaseCall();
} catch (dbErr) {
throw new Error("Service layer failed", { cause: dbErr });
}
}
try {
serviceLayer();
} catch (e) {
console.log(e.message);
console.log(e.cause?.message);
}
```

*Hint*: Trace the cause property access and stack truncation.

### Challenge 2: Refactoring Swallowed Batch Async Errors

Refactor a batch data processing pipeline using Promise.allSettled so that if one or more operations fail, it aggregates all individual item errors into an AggregateError with full telemetry, rather than failing silently or returning partial data without error notice.

```javascript
// Anti-pattern: Swallows errors or fails partially
async function processBatch(items) {
const results = await Promise.allSettled(items.map(item => processItem(item)));
return results.filter(r => r.status === 'fulfilled').map(r => r.value);
}
```

*Hint*: Extract rejected entries and throw a custom AggregateError(failedErrors, "Batch processing partially failed").

### Challenge 3: Building an Enterprise Domain Error System

Write a production TypeScript Error Framework containing:

1.  Base AppError extending Error with statusCode, code, isOperational flag, and Error.captureStackTrace.

2.  Specialized subclasses: NotFoundException (404), UnauthorizedException (401), ValidationException (422 with field-level details array).

3.  A global error sanitizer function formatErrorForClient(err) that returns safe JSON { code, message, details } without leaking sensitive stack traces in production environments (NODE_ENV === 'production').

*Hint*: Use NODE_ENV check to conditionally obscure internal error stacks.
