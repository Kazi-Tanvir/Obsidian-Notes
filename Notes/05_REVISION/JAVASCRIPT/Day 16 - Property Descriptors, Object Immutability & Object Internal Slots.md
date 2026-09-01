---
tags:
- javascript
- property-descriptors
- immutability
- object-internals
- v8-engine
- metaprogramming
date: 2026-08-16
---

# Day 16 - Property Descriptors, Object Immutability & Object Internal Slots

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Property Descriptors: Data vs. Accessor Attributes

Every property in a JavaScript object is represented internally by a **Property Descriptor** record containing specific metadata attributes governing its behavior.

#### Descriptor Categories:

1.  **Data Descriptor**: Contains a concrete value and mutation controls:

    - value: The actual data value stored.

    - writable: If true, the property value can be modified via assignment.

    - enumerable: If true, the property shows up in for...in, Object.keys(), and JSON.stringify().

    - configurable: If true, the descriptor attributes can be altered and the property can be deleted from the object.

2.  **Accessor Descriptor**: Contains getter/setter functions instead of a static value:

    - get: Function executed when reading the property.

    - set: Function executed when assigning a value to the property.

    - enumerable & configurable.

```javascript
// Defining Fine-Grained Property Descriptors
const userConfig = {};
```

Object.defineProperty(userConfig, "apiKey", {

value: "SECRET_KEY_9981",

writable: false, // Cannot be reassigned

enumerable: false, // Hidden from Object.keys() and JSON.stringify()

configurable: false // Cannot be deleted or re-configured

```javascript
});
console.log(userConfig.apiKey); // "SECRET_KEY_9981"
console.log(Object.keys(userConfig)); // [] (Hidden)
// In strict mode ('use strict'), this throws TypeError: Cannot assign to read only property
userConfig.apiKey = "NEW_KEY";
console.log(userConfig.apiKey); // Still "SECRET_KEY_9981"
```

### 2. Immutability Tiers & Object Integrity Levels

JavaScript provides three built-in integrity levels to restrict object mutations, each modifying internal slots like [[Extensible]]:

1.  **Object.preventExtensions(obj)**:

    - Sets internal [[Extensible]] slot to false.

    - Prevents adding **new** properties. Existing properties can still be modified or deleted.

2.  **Object.seal(obj)**:

    - Prevents adding new properties.

    - Marks all existing properties as configurable: false.

    - Existing writable properties can still have their **values changed**, but properties cannot be deleted or converted between data/accessor types.

3.  **Object.freeze(obj)**:

    - Highest built-in immutability tier.

    - Prevents adding new properties, prevents deleting existing properties.

    - Marks all data properties as writable: false and configurable: false.

```javascript
// Integrity Level Comparisons
const state = { version: 1, author: "Tamim" };
Object.seal(state);
state.version = 2; // Allowed (writable is true)
delete state.author; // Silently fails (or TypeError in strict mode)
// state.newProp = "test"; // Fails: Object is not extensible
Object.freeze(state);
state.version = 3; // Fails: Object is read-only
```

#### The Shallow Immutability Caveat:

Object.freeze() is strictly **shallow**. Nested objects inside a frozen object retain their default mutability and can still be modified unless recursively frozen.

```javascript
const appConfig = Object.freeze({
```

db: {

host: "localhost",

port: 5432

```javascript
}
});
// Mutating nested object is permitted because 'db' object reference is frozen, but its contents are not!
appConfig.db.port = 3306;
console.log(appConfig.db.port); // 3306 (Mutated!)
```

### 3. V8 Engine Internals: Fast vs. Dictionary Mode

In the V8 engine, standard objects utilize **Hidden Classes (Shapes)** for fast $O(1)$ inline cache lookups. When you apply Object.preventExtensions(), Object.seal(), or Object.freeze(), V8 creates a new transition shape with mutated integrity flags. If an object is subjected to non-standard, repeated descriptor modifications or extensive deletions, V8 may demote it to **Slow Dictionary Mode (Hash Table)**, increasing property access lookup overhead.

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Method** | **Can Add Props?** | **Can Delete Props?** | **Can Modify Values?** | **Modifies Descriptors?** |
| --- | --- | --- | --- | --- |
| **Default Object** | Yes | Yes | Yes | configurable: true, writable: true |
| **Object.preventExtensions()** | **No** | Yes | Yes | Sets [[Extensible]] = false |
| **Object.seal()** | **No** | **No** | Yes | Sets configurable: false on all props |
| **Object.freeze()** | **No** | **No** | **No** | Sets writable: false, configurable: false |

### Reflection & Inspection APIs:

- Object.getOwnPropertyDescriptor(target, prop): Retrieves single descriptor.

- Object.getOwnPropertyDescriptors(target): Retrieves all descriptors.

- Object.isExtensible(obj) / Object.isSealed(obj) / Object.isFrozen(obj): State validation helpers.

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Property Descriptor Mutation & Strict Mode Output Prediction

Analyze the code snippet below. Predict the console output and explain why the second Object.defineProperty call throws an error.

```javascript
const config = {};
```

Object.defineProperty(config, "mode", {

value: "production",

writable: true,

enumerable: true,

configurable: false

```javascript
});
config.mode = "development";
console.log(config.mode);
// What happens here?
```

Object.defineProperty(config, "mode", {

enumerable: false

```javascript
});
```

*Hint*: When configurable: false, which descriptor attributes can still transition from true to false, and which ones cannot be altered at all?

### Challenge 2: Recursive Deep Freeze with Circular Reference Safety

Standard Object.freeze() only protects top-level properties. Implement a robust deepFreeze<T>(obj: T): T utility function that:

1.  Recursively freezes all nested objects, arrays, and functions.

2.  Handles and prevents infinite recursion on **circular references** using a WeakSet.

3.  Preserves prototype chains and symbol properties (Reflect.ownKeys).

*Hint*: Use Reflect.ownKeys() and track visited objects in a new WeakSet().

### Challenge 3: Building a Tamper-Proof Audit-Logging State Container

Build a production-grade createSecureStateStore<T>(initialState: T) class in TypeScript that:

1.  Stores state internally with configurable: false and enumerable: true.

2.  Provides accessors (get, set) that automatically log every read and write attempt with timestamps and caller metadata.

3.  Completely disallows adding unauthorized properties by enforcing Object.preventExtensions().

4.  Returns an immutable snapshot (deepFreeze) when calling .getState().

*Hint*: Combine Object.defineProperties, accessor getters/setters, and deep freezing.
