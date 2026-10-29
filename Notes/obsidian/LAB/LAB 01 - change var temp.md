---
title: "LAB 01 - change var temp"
aliases:
  - change var temp
  - 01_change_var_temp
tags:
  - type/lab
  - c/functions
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/01_change_var_temp.c"
number: 1
up: "[[LAB - Index]]"
next: "[[LAB 02 - change var no temp]]"
related:
  - "[[LAB 02 - change var no temp]]"
  - "[[LAB 19 - pointer swap]]"
created: 2026-10-29
status: draft
---
# LAB 01 - change var temp

> [!abstract] Summary
> Swaps two integer variables using an auxiliary temporary storage variable to preserve intermediate values during reassignment.

**Source:** `LAB/01_change_var_temp.c`

## Problem
Exchange the values stored in two distinct variables $a$ and $b$ so that $a$ receives the original value of $b$, and $b$ receives the original value of $a$.

## Concepts used
- **Destructive Assignment**: In C, assigning `a = b;` immediately overwrites the original value stored in memory address `&a`. Without saving it first, the original value of $a$ is lost permanently.
- **Temporary Variable Idiom**: Introducing a third storage location (`temp`) to hold the initial value of $a$ while $b$ is copied into $a$.
- **Memory Consumption**: Requires $O(1)$ additional space (1 extra integer on the stack).

## Code
```c
#include <stdio.h>

int main()
{
    int a, b, temp;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Before swapping: a = %d, b = %d\n", a, b);

    temp = a;
    a = b;
    b = temp;

    printf("After swapping: a = %d, b = %d\n", a, b);
    return 0;
}
```

## How it works
1. **Input Allocation**: Prompts the user and reads integers $a$ and $b$ using `scanf("%d %d", &a, &b)`.
2. **Three-Step Swap Protocol**:
   - `int temp = a;` ? saves $a$'s value into `temp`.
   - `a = b;` ? overwrites $a$ with $b$'s value.
   - `b = temp;` ? assigns the saved original value of $a$ from `temp` into $b$.
3. **Display**: Prints the values before and after the swap.

## Sample run
```text
Enter two numbers: 10 20
Before swapping: a = 10, b = 20
After swapping: a = 20, b = 10
```

## Gotchas
> [!warning] Value Overwrite Sequence
> A common beginner mistake is executing `a = b; b = a;`. The first statement overwrites $a$, causing both variables to hold $b$'s value. Storing $a$ in `temp` first is mandatory when using this approach.

## My notes
> [!question]- My notes

## Related
- [[LAB 02 - change var no temp]] - Swapping without an extra variable
- [[LAB 19 - pointer swap]] - Swapping values across function scopes using pointers
