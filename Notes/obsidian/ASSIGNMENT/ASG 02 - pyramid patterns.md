---
title: "ASG 02 - pyramid patterns"
aliases:
  - pyramid patterns
  - pyramid1 to pyramid5
tags:
  - type/assignment
  - c/loops
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "ASSIGNMENT/ASSIGNMENT_02/"
number: 2
up: "[[ASG - Index]]"
prev: "[[ASG 01 - user defined calc]]"
next: "[[ASG 03 - hollow box and butterfly]]"
related:
  - "[[ASG 03 - hollow box and butterfly]]"
  - "[[LAB 07 - hollow triangle]]"
  - "[[LAB 08 - pascal]]"
created: 2026-10-29
status: draft
---
# ASG 02 - pyramid patterns

> [!abstract] Summary
> Comprehensive study of 2D character pattern generation, comparing five geometric pyramid variations (right-angled, inverted, right-aligned, and centered diamond pyramids).

**Source:** `ASSIGNMENT/ASSIGNMENT_02/pyramid1.c` through `pyramid5.c`

## Problem
Read a pyramid height $n$ from the user and print various triangular and diamond star configurations using nested iteration loops.

## Concepts used
- **Nested Iteration Loops:** Outer loop controlling row position $i$ ($0$ to $n-1$), inner loops controlling column spaces and star characters.
- **Geometric Offset Calculations:**
  - Leading spaces: $n - 1 - i$ spaces for centered alignment.
  - Star count: $2i + 1$ stars for equilateral pyramids.
- **Pattern Symmetry:** Concatenating an ascending upper pyramid with an inverted lower pyramid to generate diamond shapes.

---

## Pattern Variations & Code

### 1. Left-Aligned Right Triangle (`pyramid1.c`)
Row $i$ prints $i + 1$ stars directly from the left margin.
```c
#include <stdio.h>

int main()
{
    int height;
    printf("Enter Your Pyramid Height : ");
    scanf("%d", &height);

    for (int i = 1; i <= height; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
```
**Sample Run ($n = 4$):**
```text
*
**
***
****
```

### 2. Inverted Left-Aligned Triangle (`pyramid2.c`)
Row $i$ prints $n - i$ stars, decreasing downward.
```c
#include <stdio.h>

int main()
{
    int height;
    printf("Enter Your Pyramid Height : ");
    scanf("%d", &height);

    for (int i = 1; i <= height; i++)
    {
        //for spaces
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }
        // for #
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
```
**Sample Run ($n = 4$):**
```text
****
***
**
*
```

### 3. Right-Aligned Right Triangle (`pyramid3.c`)
Row $i$ prints $n - 1 - i$ spaces followed by $i + 1$ stars.
```c
#include <stdio.h>

int main()
{
    int height;
    printf("Enter Your Pyramid Height : ");
    scanf("%d", &height);

    for (int i = 0; i < height; i++)
    {
        //for spaces
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }
        // for #
        for (int j = 0; j < (2*i + 1); j++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
```
**Sample Run ($n = 4$):**
```text
   *
  **
 ***
****
```

### 4. Inverted Right-Aligned Triangle (`pyramid4.c`)
Row $i$ prints $i$ leading spaces followed by $n - i$ stars.
```c
#include <stdio.h>

int main()
{
    int height;
    printf("Enter Your Pyramid Height : ");
    scanf("%d", &height);

    for (int i = height; i > 0 ; i--)
    {
        //for spaces
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }
        // for #
        for (int j = 0; j < (2*i - 1); j++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
```
**Sample Run ($n = 4$):**
```text
****
 ***
  **
   *
```

### 5. Centered Equilateral & Diamond Pyramid (`pyramid5.c`)
Combines centered leading spaces with odd-count hash `#` symbols ($2i + 1$), followed by an inverted bottom half to form a diamond.
```c
#include <stdio.h>

int main()
{
    int height;
    printf("Enter Your Pyramid Height : ");
    scanf("%d", &height);
    // normal pyramid
    for (int i = 0; i < height; i++)
    {
        // for spaces
        for (int j = height - i; j > 0; j--)
        {
            printf(" ");
        }
        // for #
        for (int j = 0; j < (2 * i + 1); j++)
        {
            printf("#");
        }
        printf("\n");
    }
    // inverted pyramid
    for (int i = height - 1; i > 0; i--)
    {
        // for spaces
        for (int j = height - i + 1; j > 0; j--)
        {
            printf(" ");
        }
        // for #
        for (int j = 0; j < (2 * i - 1); j++)
        {
            printf("#");
        }
        printf("\n");
    }
    //
    return 0;
}
```
**Sample Run ($n = 4$):**
```text
    #
   ###
  #####
 #######
  #####
   ###
    #
```

## How it works
1. Each variant queries the user for pyramid height $n$.
2. The outer loop coordinates row index $i$.
3. Inner loops run sequentially: first printing horizontal padding spaces where needed, then printing the symbol (`*` or `#`).
4. An explicit newline `printf("\n")` terminates each row before advancing to the next row.

## Gotchas
> [!warning] Off-By-One Spacing Errors
> In centered pyramids, the number of spaces must exactly decrease as row index increases. Printing $n - i$ spaces instead of $n - 1 - i$ creates a 1-character horizontal shift.

## My notes
> [!question]- My notes

## Related
- [[ASG 03 - hollow box and butterfly]]
- [[LAB 07 - hollow triangle]]
- [[LAB 08 - pascal]]
