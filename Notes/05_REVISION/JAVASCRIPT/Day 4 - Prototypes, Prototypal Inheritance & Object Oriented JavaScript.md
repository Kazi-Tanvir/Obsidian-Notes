---
tags:
- javascript
- prototypes
- inheritance
- oop
- classes
- v8-hidden-classes
date: 2026-08-04
---

# Day 4 - Prototypes, Prototypal Inheritance & Object Oriented JavaScript

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Prototype Chain Mechanics & Object Identity

JavaScript is a prototype-based language. Every object in JavaScript has an internal link to another object called its **[[Prototype]]**.

- **prototype property**: Present on constructor functions/classes. It defines properties and methods that will be assigned as the [[Prototype]] of instances created via new.

- **__proto__ (accessor)**: Exposes the internal [[Prototype]] link of an instance.

- **Prototype Chain Lookup**: When accessing a property on an object, the JS engine checks the object itself. If not found, it traverses up [[Prototype]] links until it either finds the property or reaches Object.prototype.__proto__, which is null.

```javascript
// Classical Prototypal Inheritance Mechanics (Pre-ES6)
function Animal(name) {
this.name = name;
}
```

Animal.prototype.eat = function() {

```javascript
return `${this.name} is eating.`;
};
function Dog(name, breed) {
Animal.call(this, name); // Call super constructor
this.breed = breed;
}
// Link prototypes
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
```

Dog.prototype.bark = function() {

```javascript
return `${this.name} barks!`;
};
const myDog = new Dog("Rex", "German Shepherd");
console.log(myDog.eat()); // "Rex is eating." (Found via prototype chain)
```

### 2. ES6+ Class Syntax & Modern OOP Features

ES6 class syntax is syntactic sugar over prototypal inheritance, adding strict mode by default, non-enumerable methods, and modern features like private fields.

```javascript
// Modern Class Hierarchy with Private Fields & Static Factory
class Vehicle {
```

#vin; // ES2022 Private Field

```javascript
constructor(vin, make) {
this.#vin = vin;
this.make = make;
}
getVin() {
return this.#vin;
}
```

static isVehicle(obj) {

```javascript
return obj instanceof Vehicle;
}
}
class ElectricCar extends Vehicle {
#batteryCapacity;
constructor(vin, make, batteryCapacity) {
super(vin, make); // Must call super() before accessing 'this'
this.#batteryCapacity = batteryCapacity;
}
getDetails() {
return `${this.make} (VIN: ${this.getVin()}) - ${this.#batteryCapacity}kWh`;
}
}
const tesla = new ElectricCar("5YJ3E1EA", "Tesla", 75);
console.log(tesla.getDetails()); // "Tesla (VIN: 5YJ3E1EA) - 75kWh"
// console.log(tesla.#vin); // SyntaxError: Private field '#vin' must be declared in an enclosing class
```

### 3. V8 Engine Optimization: Hidden Classes (Shapes) & Inline Caches

Because JavaScript is dynamically typed, property access is inherently slower than in statically typed languages like C++. To optimize this, the V8 engine uses **Hidden Classes (Shapes/Maps)** and **Inline Caches (ICs)**.

- **Hidden Classes (Shapes)**: V8 assigns an internal shape map to every object. When properties are added in the exact same order, objects share the same Hidden Class.

- **Transition Chains**: Adding properties in different orders creates new hidden classes, breaking V8 optimization.

- **Inline Caches (ICs)**:

  - *Monomorphic*: IC sees only 1 hidden class (Fastest - JIT optimized).

  - *Polymorphic*: IC sees 2-4 hidden classes (Slower).

  - *Megamorphic*: IC sees 5+ hidden classes (Slowest - falls back to hash table lookup).

```javascript
// V8 Anti-Pattern: De-optimizing Hidden Classes
function BadPoint(x, y) {
this.x = x;
this.y = y;
}
const p1 = new BadPoint(1, 2);
const p2 = new BadPoint(3, 4);
p1.z = 5; // Creates a new Hidden Class transition for p1!
delete p2.x; // Forces p2 into Slow/Dictionary Mode!
// V8 Best Practice: Initialize all fields in constructor in identical order
class OptimizedPoint {
constructor(x, y, z = null) {
this.x = x;
this.y = y;
this.z = z; // Same shape for all instances!
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **API / Concept** | **Description** | **Syntax / Example** |
| --- | --- | --- |
| Object.create(proto) | Creates new object with specified prototype | const obj = Object.create(parentProto) |
| Object.getPrototypeOf(obj) | Retrieves internal [[Prototype]]                             Obj | ct.getPrototypeOf(myDog) === Dog.prototype |
| Object.setPrototypeOf(obj, proto) | Mutates internal [[Prototype]] (Slow - breaks V8 ICs)        Obj | ct.setPrototypeOf(a, b) |
| Object.hasOwn(obj, prop) | Checks if property exists on instance directly (not prototype) | Object.hasOwn(myDog, 'name') // true |
| #privateField | Enforces true private class members | #balance = 0; |
| super(...args) | nvokes parent class constructor | ust be called before this in derived class |

### V8 Hidden Class Best Practices:

1.  Always initialize all object properties in the constructor.

2.  Never delete properties (delete obj.prop) --- assign null or undefined instead.

3.  Keep property initialization order strictly uniform across instances.

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Prototype Shadowing & Identity Output Prediction

Predict the exact console output of the code snippet below and explain how property shadowing and prototype mutation affect lookup behavior.

```javascript
function Widget(name) {
this.name = name;
}
```

Widget.prototype.render = function() {

```javascript
return `Widget: ${this.name}`;
};
const w1 = new Widget("Button");
const w2 = new Widget("Input");
```

w1.render = function() {

```javascript
return `Custom: ${this.name}`;
};
delete w1.render;
```

Widget.prototype.render = function() {

```javascript
return `Global Override: ${this.name}`;
};
console.log(w1.render());
console.log(w2.render());
```

*Hint*: Differentiate between instance properties and prototype properties after property deletion.

### Challenge 2: Refactoring Legacy Prototypal Patterns to ES6 Class Hierarchy

The code below uses ES5 constructor functions and prototype mutation. Refactor it into clean, type-safe ES6 Class syntax with:

1.  Private fields for sensitive properties (#ssn).

2.  Static builder method Person.fromJSON(jsonString).

3.  Read-only getters.

```javascript
// Legacy ES5 Code
function Person(name, ssn) {
this.name = name;
this._ssn = ssn;
}
```

Person.prototype.getSSN = function() {

```javascript
return this._ssn;
};
```

Person.prototype.toJSON = function() {

```javascript
return JSON.stringify({ name: this.name });
};
```

*Hint*: Replace _ssn naming convention with #ssn private field.

### Challenge 3: Advanced Functional Class Builder (No class Keyword)

Implement a custom function createCustomClass(options) from scratch that mimics class creation, inheritance, and method resolution without using the class keyword.

**Requirements**:

1.  Accepts { constructor, superclass, methods, staticMethods }.

2.  Sets up proper prototype chain linking and constructor reference.

3.  Provides a working this._super(methodName, ...args) helper to invoke overridden parent methods.

*Hint*: Use Object.create() and Function.prototype.apply().
