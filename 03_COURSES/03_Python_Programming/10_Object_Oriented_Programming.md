---
tags:
  - python-programming
  - oop
  - class
  - object
---

# Object Oriented Programming

Solving a problem by creating object is one of the most popular approaches in programming. This is called object-oriented programming. This concept focuses on using reusable code (DRY Principle).

## Class
A class is a blueprint for creating object.

*Syntax:*
```python
class Employee: # Class name is written in pascal case
    # Methods & Variables
    pass
```

## Object
An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.

Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. – Abstractions & Encapsulation!

## Modelling a problem in OOPs
We identify the following in our problem:
- **Noun** -> Class -> Employee
- **Adjective** -> Attributes -> name, age, salary
- **Verbs** -> Methods -> getSalary(), increment()

## Class Attributes
An attribute that belongs to the class rather than a particular object.

*Example:*
```python
class Employee:
    company = "Google" # Specific to Each Class

harry = Employee() # Object Instantiation
print(harry.company)
Employee.company = "YouTube" # Changing Class Attribute
```

## Instance attributes
An attribute that belongs to the Instance (object).

```python
harry.name = "harry"
harry.salary = "30k" # Adding instance attribute
```
*Note:* Instance attributes, take preference over class attributes during assignment & retrieval.

## self parameter
self refers to the instance of the class. It is automatically passed with a function call from an object.

```python
harry.getSalary() # here self is harry
# equivalent to Employee.getSalary(harry)
```

## static method
Sometimes we need a function that does not use the self-parameter. We can define a static method like this:

```python
@staticmethod # decorator to mark greet as a static method
def greet():
    print("Hello user")
```

## `__init__()` constructor
`__init__()` is a special method which is first run as soon as the object is created. `__init__()` method is also known as constructor. It takes ‘self’ argument and can also take further arguments.

*For Example:*
```python
class Employee:
    def __init__(self, name):
        self.name = name
    def getSalary(self):
        pass

harry = Employee("Harry")
```

## Practice Set
- [ ] 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
- [ ] 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
- [ ] 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
- [ ] 4. Add a static method in problem 2, to greet the user with hello.
- [ ] 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
- [ ] 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.