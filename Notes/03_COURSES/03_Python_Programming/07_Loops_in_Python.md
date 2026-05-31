---
tags:
  - python-programming
  - loops
  - while-loop
  - for-loop
---

# Loops in Python

Sometimes we want to repeat a set of statements in our program. For instance: Print 1 to 1000. Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!

## Types of Loops in Python
Primarily there are two types of loops in python:
- `while` loops
- `for` loops

We will look into these one by one.

## While Loop
In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not! If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.

*Syntax:*
```python
while (condition): # The block keeps executing until the condition is true
    # Body of the loop
```

*Example:*
```python
i = 0
while i < 5: # print "Harry" - 5 times!
    print("Harry")
    i = i + 1
```

## For Loop
A for loop is used to iterate through a sequence like list, tuple, or string [iterables].

*Syntax:*
```python
l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8
```

## range() Function in Python
The range() function in python is used to generate a sequence of number. We can also specify the start, stop and step-size as follows:
```python
range(start, stop, step_size)
```

*Example:*
```python
for i in range(0, 7): # range(7) can also be used.
    print(i) # prints 0 to 6
```

## For Loop with Else
An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

*Example:*
```python
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!
```

## The Break Statement
‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

*Example:*
```python
for i in range(0, 80):
    print(i) # this will print 0, 1, 2 and 3
    if i == 3:
        break
```

## The Continue Statement
‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.

*Example:*
```python
for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)
```

## Pass Statement
pass is a null statement in python. It instructs to “do nothing”.

*Example:*
```python
l = [1, 7, 8]
for item in l:
    pass # without pass, the program will throw an error
```

## Practice Set
- [ ] 1. Write a program to print multiplication table of a given number using for loop.
- [ ] 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
`l = ["Harry", "Soham", "Sachin", "Rahul"]`
- [ ] 3. Attempt problem 1 using while loop.
- [ ] 4. Write a program to find whether a given number is prime or not.
- [ ] 5. Write a program to find the sum of first n natural numbers using while loop.
- [ ] 6. Write a program to calculate the factorial of a given number using for loop.
- [ ] 7. Write a program to print the following star pattern.
```text
  *
 ***
***** for n = 3
```
- [ ] 8. Write a program to print the following star pattern:
```text
*
**
***   for n = 3
```
- [ ] 9. Write a program to print the following star pattern.
```text
* * *
*   * for n = 3
* * *
```
- [ ] 10. Write a program to print multiplication table of n using for loops in reversed order.