---
tags:
  - python-programming
  - conditionals
  - if-else
---

# Conditional Expression

Sometimes we want to play PUBG on our phone if the day is Sunday. Sometimes we order Ice Cream online if the day is sunny. Sometimes we go hiking if our parents allow. All these are decisions which depend on a condition being met. In python programming too, we must be able to execute instructions on a condition(s) being met. This is what conditionals are for!

## If Else and Elif in Python
If else and elif statements are a multiway decision taken by our program due to certain conditions in our code.

*Syntax:*
```python
if (condition1):    # if condition1 is True
    print("yes")
elif (condition2):  # if condition2 is True
    print("no")
else:               # otherwise
    print("maybe")
```

## Code Example
```python
a = 22
if (a > 9):
    print("greater")
else:
    print("lesser")
```

## Relational Operators
Relational Operators are used to evaluate conditions inside the if statements. Some examples of relational operators are:
- `==`: equals.
- `>=`: greater than/ equal to.
- `<=`: lesser than/ equal to.

## Logical Operators
In python logical operators operate on conditional statements. For Example:
- `and`: true if both operands are true else false.
- `or`: true if at least one operand is true or else false.
- `not`: inverts true to false & false to true.

## Elif Clause
elif in python means [else if]. An if statements can be chained together with a lot of these elif statements followed by an else statement.

**Important notes:**
1. There can be any number of elif statements.
2. Last else is executed only if all the conditions inside elifs fail.

## Practice Set
- [ ] 1. Write a program to find the greatest of four numbers entered by the user.
- [ ] 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
- [ ] 3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
- [ ] 4. Write a program to find whether a given username contains less than 10 characters or not.
- [ ] 5. Write a program which finds out whether a given name is present in a list or not.
- [ ] 6. Write a program to calculate the grade of a student from his marks from the following scheme:
  - 90 – 100 => Ex
  - 80 – 90 => A
  - 70 – 80 => B
  - 60 – 70 => C
  - 50 – 60 => D
  - <50 => F
- [ ] 7. Write a program to find out whether a given post is talking about “Harry” or not.