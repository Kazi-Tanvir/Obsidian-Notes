---
tags:
- javascript
- typescript
- type-system
- type-level-programming
- generics
- metaprogramming
date: 2026-08-24
---

# Day 24 - Advanced TypeScript Type-Level Programming: Conditional, Mapped & Template Literal Types

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The TypeScript Type System as a Pure Functional Language

The TypeScript type system is Turing-complete. Types can be treated as functions that accept types as arguments, perform transformations, branch conditionally, recurse over data structures, and return new types.

### 2. Core Type-Level Primitives

#### A. Conditional Types & Distributive Conditionals

Conditional types take the form T extends U ? X : Y. When T is a generic naked type parameter and a union type is passed, the conditional type automatically **distributes** across each union member:

```typescript
// Distributive Behavior
type ToArray<T> = T extends any ? T[] : never;
type TestDistributive = ToArray<string | number>;
// Result: string[] | number[] (NOT (string | number)[])
// Preventing Distribution using Tuple Boxing
type NonDistributiveToArray<T> = [T] extends [any] ? T[] : never;
type TestNonDistributive = NonDistributiveToArray<string | number>;
// Result: (string | number)[]
```

#### B. Type Pattern Matching with the infer Keyword

The infer keyword allows you to declare a type variable within the extends clause of a conditional type to extract nested sub-types:

```typescript
// Unboxing Nested Promise Types (Polyfill of Awaited<T>)
type DeepAwaited<T> = T extends Promise<infer U> ? DeepAwaited<U> : T;
type Test1 = DeepAwaited<Promise<Promise<string>>>; // string
// Extracting Function Return and Parameter Types
type CustomReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type CustomFirstParam<T> = T extends (first: infer P, ...rest: any[]) => any ? P : never;
type Fn = (id: number, active: boolean) => { success: boolean };
type Ret = CustomReturnType<Fn>; // { success: boolean }
type Param1 = CustomFirstParam<Fn>; // number
```

#### C. Mapped Types with Key Remapping (as)

Mapped types iterate over keys using the in operator, allowing property modifier adjustments (readonly, ?, -readonly, -?) and key transformation via the as clause:

```typescript
interface User {
id: string;
name: string;
age: number;
}
// Prefix all keys and make them optional
type PrefixedOptional<T, Prefix extends string> = {
[K in keyof T as `${Prefix}_${string & K}`]?: T[K];
};
type PrefixedUser = PrefixedOptional<User, "user">;
// Result: { user_id?: string; user_name?: string; user_age?: number }
// Filtering Object Properties by Value Type
type PickByType<T, ValueType> = {
[K in keyof T as T[K] extends ValueType ? K : never]: T[K];
};
type StringFieldsOnly = PickByType<User, string>;
// Result: { id: string; name: string }
```

#### D. Template Literal Types & String Pattern Parsing

Template literal types combine string literals to model URL paths, event names, and CSS properties with full type-safety:

```javascript
// Modeling Event Emitter Strings
type Entity = "user" | "order" | "invoice";
type Action = "created" | "updated" | "deleted";
type EventName = `${Entity}:${Action}`;
// Result: "user:created" | "user:updated" | "user:deleted" | "order:created" ...
// Parsing Path Parameters from a Route String
export type ExtractRouteParams<T extends string> =
```

T extends `${string}:${infer Param}/${infer Rest}`

? { [K in Param | keyof ExtractRouteParams<`/${Rest}`>]: string }

: T extends `${string}:${infer Param}`

? { [K in Param]: string }

```typescript
: Record<string, never>;
type UserRouteParams = ExtractRouteParams<"/api/v1/users/:userId/posts/:postId">;
// Result: { userId: string; postId: string }
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Built-In Utility Types Reference:

| **Utility Type** | **Definition / Mechanism** | **Primary Use Case** |
| --- | --- | --- |
| Partial<T>            { | P in keyof T]?: T[P]}                             Make | ll properties optional |
| Required<T>           { | P in keyof T]-?: T[P]}                            Remov | all optional modifiers |
| Readonly<T>           { | eadonly [P in keyof T]: T[P]}                     Preve | t property re-assignment |
| Pick<T, K>            { | P in K]: T[P]}                                    Extra | t a subset of properties |
| Omit<T, K>            P | ck<T, Exclude<keyof T, K>>                        Exclu | e a subset of properties |
| Exclude<T, U>         T | extends U ? never : T                                 R | move types from a union |
| Extract<T, U>         T | extends U ? T : never                                 K | ep matching types in a union |
| NonNullable<T>        T | extends null | undefined ? never : T                 St | ip null and undefined |
| Parameters<T>         T | extends (...args: infer P) => any ? P : never       Ext | act parameter tuple |
| ReturnType<T>         T | extends (...args: any[]) => infer R ? R : never   Extra | t function return type |
| Awaited<T>            R | cursive infer unboxing                                U | wrap Promise return types |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Distributive Union Type Predictor

Analyze the type expressions below. Predict the resulting evaluated type for ResultA versus ResultB and explain why they differ:

```javascript
type DiffA<T, U> = T extends U ? never : T;
type DiffB<T, U> = [T] extends [U] ? never : T;
type Union = "a" | "b" | "c";
type ResultA = DiffA<Union, "a">;
type ResultB = DiffB<Union, "a">;
```

*Hint*: Evaluate distributive conditional behavior across naked generic parameters vs boxed tuple expressions.

### Challenge 2: Deep Readonly and Deep Mutable

Implement two recursive utility types:

1.  DeepReadonly<T>: Recursively makes every nested object, array, and map property readonly, while preserving function signatures and primitive values without boxing them.

2.  DeepMutable<T>: Recursively removes all readonly modifiers from nested objects and arrays.

```typescript
// Target test structure
interface ComplexState {
```

meta: {

```typescript
readonly version: number;
tags: readonly string[];
};
```

nested: {

flags: {

```typescript
readonly active: boolean;
};
};
}
```

*Hint*: Handle array types (T extends readonly (infer U)[]) separately from generic object records.

### Challenge 3: Type-Safe JSON Schema to TypeScript Type Compiler

Build an advanced type-level parser FromSchema<T> in TypeScript that converts a const JSON Schema object definition into an exact static TypeScript interface:

```javascript
const userSchema = {
```

type: "object",

properties: {

id: { type: "string" },

age: { type: "number" },

isAdmin: { type: "boolean" },

address: {

type: "object",

properties: {

city: { type: "string" },

},

required: ["city"],

},

},

required: ["id", "address"],

```typescript
} as const;
// Expected:
// type InferredUser = FromSchema<typeof userSchema>;
// {
// id: string;
// age?: number;
// isAdmin?: boolean;
// address: {
// city: string;
// };
// }
```

*Hint*: Use recursive mapped types with key remapping, conditional property type conversions ("string" -> string, "number" -> number), and distribute required vs optional keys using keyof T["properties"] extends T["required"][number].
