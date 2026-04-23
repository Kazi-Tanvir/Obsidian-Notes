---
tags:
  - python-programming
  - modules
  - comments
  - pip
---

# Modules, Comments & pip

Let's write our very first python program. Create a file called `hello.py` and paste the below code in it.

```python
print("hello world") # print is a function (more later)
```

To run this file (.py extension), type `python hello.py` in the terminal, and you will see 'Hello World' printed on the screen.

## Modules
A module is a file containing code written by somebody else (usually) which can be imported and used in our programs.

### Types of Modules
There are two types of modules in Python:
1. **Built in Modules:** These are preinstalled in Python (e.g., `os`, `random`).
2. **External Modules:** These need to be installed using `pip` (e.g., `tensorflow`, `flask`).

## pip
pip is the package manager for python. You can use pip to install a module on your system.

```bash
pip install flask # Installs Flask Module
```

## Using python as a calculator
We can use python as a calculator by typing `python` and pressing enter in the terminal. This opens the REPL (Read Evaluate Print Loop).

## Comments
Comments are used to write something which the programmer does not want to execute. This can be used to mark author name, date etc.

### Types of Comments
There are two types of comments in python:
1. **Single Line Comments:** To write a single line comment just add a `#` at the start of the line.
```python
# This is a Single-Line Comment
```
2. **Multiline Comments:** To write multi-line comments you can use `#` at each line or you can use the multiline string (`""" """`).
```python
"""This is an amazing
example of a Multiline
comment!"""
```

## Practice Set
- [ ] 1. Write a program to print Twinkle twinkle little star poem in python.
- [ ] 2. Use REPL and print the table of 5 using it.
- [ ] 3. Install an external module and use it to perform an operation of your interest.
- [ ] 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
- [ ] 5. Label the program written in problem 4 with comments.
