---
tags:
  - python-programming
  - functions
  - recursion
---

# Functions & Recursions

A function is a group of statements performing a specific task. When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what! A function can be reused by the programmer in a given program any number of times.

## Example and Syntax of a Function
The syntax of a function looks as follows:

```python
def func1():
    print('hello')
```
This function can be called any number of times, anywhere in the program.

## Function Call
Whenever we want to call a function, we put the name of the function followed by parentheses as follows:

```python
func1() # This is called function call
```

## Function Definition
The part containing the exact set of instructions which are executed during the function call.

## Types of Functions in Python
There are two types of functions in python:
- **Built in functions:** Already present in python (e.g., `len()`, `print()`, `range()`).
- **User defined functions:** Defined by the user (e.g., our `func1()`).

## Functions with Arguments
A function can accept some value it can work with. We can put these values in the parentheses. A function can also return value as shown below:

```python
def greet(name):
    gr = "hello" + name
    return gr

a = greet("harry")
# a will now contain "hello harry"
```

## Default Parameter Value
We can have a value as default as default argument in a function. If we specify name = “stranger” in the line containing def, this value is used when no argument is passed.

*Example:*
```python
def greet(name="stranger"):
    print("Hello", name)

greet() # name will be "stranger" (default)
greet("harry") # name will be "harry" (passed)
```

## Recursion
Recursion is a function which calls itself. It is used to directly use a mathematical formula as function.

*Example:* `factorial(n) = n x factorial (n-1)`
This function can be defined as follows:

```python
def factorial(n):
    if n == 0 or n == 1: # base condition
        return 1
    else:
        return n * factorial(n-1) # function calling itself
```

The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most direct way to code an algorithm.

## Practice Set
- [ ] 1. Write a program using functions to find greatest of three numbers.
- [ ] 2. Write a python program using function to convert Celsius to Fahrenheit.
- [ ] 3. How do you prevent a python print() function to print a new line at the end.
- [ ] 4. Write a recursive function to calculate the sum of first n natural numbers.
- [ ] 5. Write a python function to print first n lines of the following pattern:
```text
***
**    - for n = 3
*
```
- [ ] 6. Write a python function which converts inches to cms.
- [ ] 7. Write a python function to remove a given word from a list and strip it at the same time.
- [ ] 8. Write a python function to print multiplication table of a given number.