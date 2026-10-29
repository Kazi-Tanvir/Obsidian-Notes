---
title: "LAB 02 - change var no temp"
aliases:
  - change var no temp
  - 02_change_var_no_temp
tags:
  - type/lab
  - c/math
  - c/functions
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/02_change_var_no_temp.c"
number: 2
up: "[[LAB - Index]]"
prev: "[[LAB 01 - change var temp]]"
next: "[[LAB 03 - age calc simple]]"
related:
  - "[[LAB 01 - change var temp]]"
  - "[[LAB 19 - pointer swap]]"
created: 2026-10-29
status: draft
---
# LAB 02 - change var no temp

> [!abstract] Summary
> Swaps two integer variables in place using arithmetic addition and subtraction without allocating a third temporary variable.

**Source:** `LAB/02_change_var_no_temp.c`

## Problem
Exchange the values of two variables $a$ and $b$ strictly using the existing storage locations of $a$ and $b$, without declaring any auxiliary variables.

## Concepts used
- **Arithmetic Inversion Swap**: Using the mathematical properties of addition and subtraction to encode both values into their sum, and then extracting each value individually.
- **Space Optimization**: Consumes zero additional stack storage ($O(1)$ space).

## Code
```c
#include <stdio.h>

int main()
{
    int a, b, temp;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Before swapping: a = %d, b = %d\n", a, b);

    a = a + b; 
    b = a - b; 
    a = a - b; 

    printf("After swapping: a = %d, b = %d\n", a, b);
    return 0;
}
```

## How it works
1. **Input**: Reads initial values $a$ and $b$.
2. **Arithmetic Transformation**:
   - `a = a + b;` $ightarrow$ $a$ now stores the combined sum ($a_{orig} + b_{orig}$).
   - `b = a - b;` $ightarrow$ subtracts $b_{orig}$ from the sum, leaving $a_{orig}$. Thus, $b$ now holds $a_{orig}$!
   - `a = a - b;` $ightarrow$ subtracts the new $b$ ($a_{orig}$) from the sum, leaving $b_{orig}$. Thus, $a$ now holds $b_{orig}$!
3. **Display**: Prints values before and after swapping.

## Sample run
```text
Enter two numbers: 15 25
Before swapping: a = 15, b = 25
After swapping: a = 25, b = 15
```

## Gotchas
> [!warning] Integer Arithmetic Overflow
> If $a$ and $b$ are large integers near `INT_MAX` (e.g. $2 	imes 10^9$), their sum `a + b` will exceed the maximum 32-bit signed integer limit (`2147483647`), causing signed integer overflow (Undefined Behavior in C). In systems programming, bitwise XOR (`a ^= b; b ^= a; a ^= b;`) or standard temporary variables are preferred for safety.

## My notes
> [!question]- My notes

## Related
- [[LAB 01 - change var temp]] - Classic swap using a temporary variable
- [[LAB 19 - pointer swap]] - Pointer-based swap function
