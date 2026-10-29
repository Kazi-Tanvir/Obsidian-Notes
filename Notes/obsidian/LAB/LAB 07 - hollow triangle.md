---
title: "LAB 07 - hollow triangle"
aliases:
  - hollow triangle
  - 07_hollow_triangle
tags:
  - type/lab
  - c/loops
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/07_hollow_triangle.c"
number: 7
up: "[[LAB - Index]]"
prev: "[[LAB 06 - discount]]"
next: "[[LAB 08 - pascal]]"
related:
  - "[[ASG 02 - pyramid patterns]]"
  - "[[ASG 03 - hollow box and butterfly]]"
created: 2026-10-29
status: draft
---
# LAB 07 - hollow triangle

> [!abstract] Summary
> Prints a hollow triangular pyramid of height $N$ using nested loops and geometric boundary conditions.

**Source:** `LAB/07_hollow_triangle.c`

## Problem
Given an integer height $N$, render a centered triangular pyramid where only the outer boundary (left edge, right edge, and base) contains hash symbols (`#`), while the interior remains hollow whitespace.

## Concepts used
- **2D Grid Coordinate Mapping**: Mapping row index $i$ and column index $j$ into geometric shapes.
- **Nested Loops**: An outer loop controlling the row $i$ from 1 to $N$, with inner loops printing leading indentation spaces and column characters.
- **Boundary Conditions**: A character is drawn only if it lies on:
  - The left edge (`j == 1`)
  - The right edge (`j == 2*i - 1`)
  - The bottom base (`i == N`)
  Otherwise, print a blank space (`' '`).

## Code
```c
#include <stdio.h>

int main()
{
    int height;
    printf("Enter Your Pyramid Height : ");
    scanf("%d", &height);

    for (int i = 1; i <= height; i++)
    {

        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }

        for (int j = 1; j <= (2*i - 1); j++)
        {
            if(i == height|| j==1 || j == 2*i-1 || i ==1){

                printf("#");
            }
            else{
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
```

## How it works
1. **Input**: Reads pyramid height $N$.
2. **Outer Row Loop**: For row $i$ from 1 to $N$:
   - Prints $N - i$ leading spaces to center the pyramid.
   - For column $j$ from 1 to $2i - 1$:
     - If $j == 1$ or $j == 2i - 1$ or $i == N$: prints `'#'`.
     - Else: prints `' '`.
   - Prints newline `
`.

## Sample run
```text
Enter Your Pyramid Height : 5
    #
   # #
  #   #
 #     #
#########
```

## Gotchas
> [!warning] Off-by-One in Base Width
> The width of row $i$ in a symmetric pyramid is $2i - 1$ (odd numbers: 1, 3, 5, 7, ...). Using $2i$ instead of $2i - 1$ creates an asymmetric shape that fails to align with the peak apex.

## My notes
> [!question]- My notes

## Related
- [[ASG 02 - pyramid patterns]] - Comprehensive suite of 5 pyramid patterns
- [[ASG 03 - hollow box and butterfly]] - Hollow box and butterfly coordinate patterns
