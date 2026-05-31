---
tags:
- javascript
- oop
- classes
---
# Classes and Objects (OOP)

## What's the Actual Use?
Object-Oriented Programming (OOP) allows you to model real-world entities. Classes act as blueprints for creating multiple objects with similar properties and methods.

## Other Common Use Cases
- Creating a `User` class to handle logins and profiles.
- Creating a `Product` class for an e-commerce store.

## Documentation & Code
- `constructor`: Initializes new objects.
- `extends`: Creates a child class (inheritance).
- `super()`: Calls the parent class constructor.

````javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(`${this.name} makes a noise.`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks!`);
    }
}

const myDog = new Dog("Rex");
myDog.speak(); // "Rex barks!"
````
