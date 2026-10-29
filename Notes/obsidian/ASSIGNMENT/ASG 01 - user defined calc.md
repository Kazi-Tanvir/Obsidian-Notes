---
title: "ASG 01 - user defined calc"
aliases:
  - user defined calc
  - user_defined_calc
tags:
  - type/assignment
  - c/functions
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "ASSIGNMENT/ASSIGNMENT_01/user_defined_calc.c"
number: 1
up: "[[ASG - Index]]"
next: "[[ASG 02 - pyramid patterns]]"
related:
  - "[[CLASS 01 - calculator]]"
  - "[[CLASS 06 - calc menu switch]]"
created: 2026-10-29
status: draft
---
# ASG 01 - user defined calc

> [!abstract] Summary
> Demonstrates procedural programming by wrapping basic arithmetic operations (addition, subtraction, multiplication, and division) inside user-defined functions.

**Source:** `ASSIGNMENT/ASSIGNMENT_01/user_defined_calc.c`

## Problem
Prompt the user for two integers, execute arithmetic operations through distinct user-defined helper functions, and print formatted equations showing inputs and results.

## Concepts used
- **Function Prototypes & Definitions:** Declaring modular functions (`add`, `sub`, `multiply`, `divide`) returning integer values.
- **Formal vs Actual Parameters:** Passing caller integer variables `a` and `b` by value into formal function parameters.
- **Standard Input/Output:** Reading values with `scanf` and formatting output strings with `printf`.

## Code
```c
#include <stdio.h>

int addition(int a, int b)
{
    return a + b;
}

int subtraction(int a, int b)
{
    return a - b;
}

int multiplication(int a, int b)
{
    return a * b;
}

int division(int a, int b)
{
    return a / b;
}

int main()
{
    int num1, num2;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    printf("%d + %d = %d\n", num1, num2, addition(num1, num2));
    printf("%d - %d = %d\n", num1, num2, subtraction(num1, num2));
    printf("%d * %d = %d\n", num1, num2, multiplication(num1, num2));
    printf("%d / %d = %d\n", num1, num2, division(num1, num2));

    return 0;
}


// use user defined functions for making a simple calculator that performs addition, subtraction, multiplication, and division. The program should take two numbers as input and display the results of all four operations.
// Lesson : Teaches you how to use user user defined function
```

## How it works
1. Declares four arithmetic helper functions returning integers: `add()`, `sub()`, `multiply()`, and `divide()`.
2. In `main()`, prompts user for two integers and reads them into `a` and `b`.
3. Invokes each function in separate `printf` statements.
4. Each function calculates the corresponding arithmetic expression and returns the evaluated integer.

## Sample run
```text
Enter first number: 10
Enter second number: 5
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

## Gotchas
> [!warning] Integer Division Truncation and Zero Division
> Function `divide(int a, int b)` performs integer division (`a / b`), which truncates any decimal remainder. Furthermore, passing $b = 0$ triggers a runtime division-by-zero crash (`SIGFPE`).

## My notes
> [!question]- My notes

## Related
- [[CLASS 01 - calculator]]
- [[CLASS 06 - calc menu switch]]
