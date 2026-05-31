---
tags:
  - python-programming
  - inheritance
  - dunder-methods
---

# Inheritance & more on OOPs

Inheritance is a way of creating a new class from an existing class.

*Syntax:*
```python
class Employee: # Base class
    # Code
    pass

class Programmer(Employee): # Derived or child class
    # Code
    pass
```
We can use the method and attributes of ‘Employee’ class in ‘Programmer’ object. Also, we can overwrite or add new attributes and methods in ‘Programmer’ class.

## Types of Inheritance
- Single inheritance
- Multiple inheritance
- Multilevel inheritance

### Single Inheritance
Single inheritance occurs when child class inherits only a single parent class.

### Multiple Inheritance
Multiple Inheritance occurs when the child class inherits from more than one parent classes.

### Multilevel Inheritance
When a child class becomes a parent for another child class.

## super() method
super() method is used to access the methods of a super class in the derived class.
```python
super().__init__() # Calls constructor of the base class
```

## class method
A class method is a method which is bound to the class and not the object of the class. @classmethod decorator is used to create a class method.

*Syntax:*
```python
@classmethod
def (cls, p1, p2):
    pass
```

## @property Decorators
If e = Employee() is an object of class employee, we can print (e.name) to print the ename by internally calling name() function. The method name with ‘@property’ decorator is called getter method.
```python
class Employee:
    @property
    def name(self):
        return self.ename
```

## @.getters and @.setters
We can define a function + @ name.setter decorator like below:
```python
@name.setter
def name(self, value):
    self.ename = value
```

## Operator Overloading in Python
Operators in Python can be overloaded using dunder methods. These methods are called when a given operator is used on the objects.
- `p1+p2` -> `p1.__add__(p2)`
- `p1-p2` -> `p1.__sub__(p2)`
- `p1*p2` -> `p1.__mul__(p2)`
- `__str__()` -> used to set what gets displayed upon calling str(obj)
- `__len__()` -> used to set what gets displayed upon calling `__len__()` or len(obj)

## Practice Set
- [ ] 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
- [ ] 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
- [ ] 3. Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
- [ ] 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
- [ ] 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
- [ ] 6. Write `__str__()` method to print the vector as follows:
`7i + 8j +10k`
Assume vector of dimension 3 for this problem.
- [ ] 7. Override the `__len__()` method on vector of problem 5 to display the dimension of the vector.