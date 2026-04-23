---
tags:
  - python-programming
  - advanced
  - exception-handling
---

# Advanced Python 1

## Newly added features in python
Following are some of the newly added features in Python programming language.

### Walrus Operator
The walrus operator (`:=`), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression."

```python
# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
```

### Types Definitions in Python
Type hints are added using the colon (`:`) syntax for variables and the `->` syntax for function return types.
```python
# Variable type hint
age: int = 25

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
```

### Advanced Type Hints
Python's `typing` module provides more advanced type hints, such as List, Tuple, Dict, and Union.
```python
from typing import List, Tuple, Dict, Union

numbers: List[int] = [1, 2, 3, 4, 5]
identifier: Union[int, str] = "ID123"
```

### Match Case
Python 3.10 introduced the `match` statement, which is similar to the switch statement found in other programming languages.
```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown status"
```

### Dictionary Merge & Update Operators
New operators `|` and `|=` allow for merging and updating dictionaries.
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
```

## Exception handling in Python
There are many built-in exceptions which are raised in python when something goes wrong.
Exception in python can be handled using a `try` statement. The code that handles the exception is written in the except clause.

```python
try:
    # Code which might throw exception
except Exception as e:
    print(e)
```
We can also specify the exception to catch like `ZeroDivisionError` or `TypeError`.

### Raising Exceptions
We can raise custom exceptions using the `raise` keyword in python.

### try with else clause
Sometimes we want to run a piece of code when try was successful.

### try with finally
Python offers a `finally` clause which ensures execution of a piece of code irrespective of the exception.

## `__name__ == '__main__'` in python
`__name__` evaluates to the name of the module in python from where the program is ran. If the module is being run directly from the command line, the `__name__` is set to string `__main__`. This behaviour is used to check whether the module is run directly or imported to another file.

## The global keyword
`global` keyword is used to modify the variable outside of the current scope.

## enumerate function in python
The `enumerate` function adds counter to an iterable and returns it.
```python
for i, item in enumerate(list1):
    print(i, item)
```

## List comprehensions
List Comprehension is an elegant way to create lists based on existing lists.
```python
list1 = [1, 7, 12, 11, 22]
list2 = [item for item in list1 if item > 8]
```

## Practice Set
- [ ] 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
- [ ] 2. Write a program to print third, fifth and seventh element from a list using enumerate function.
- [ ] 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
- [ ] 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
- [ ] 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.