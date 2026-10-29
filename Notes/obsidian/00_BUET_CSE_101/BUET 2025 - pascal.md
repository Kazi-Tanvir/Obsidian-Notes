---
title: "BUET 2025 - pascal"
aliases:
  - BUET pascal
  - 2025 pascal
tags:
  - type/practice
  - c/recursion
  - c/math
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/2025/pascal.c"
up: "[[BUET - Index]]"
related:
  - "[[LAB 08 - pascal]]"
  - "[[BUET 2025 - factorial]]"
created: 2026-10-29
status: draft
---
# BUET 2025 - pascal

> [!abstract] Summary
> Renders an equilateral Pascal's Triangle using recursive factorial-based combinations formula $nCr = \frac{n!}{r!(n-r)!}$.

**Source:** `00_BUET_CSE_101/2025/pascal.c`

## Problem
Prompt for the number of rows $N$ and render an aligned triangular Pascal's Triangle where each element at row $n$ and position $r$ equals the binomial coefficient $\binom{n}{r}$.

## Concepts used
- **Binomial Combinations ($nCr$):** Calculating $\binom{n}{r} = \frac{n!}{r!(n-r)!}$ using recursive factorial calls.
- **Centered Layout Spacing:** Printing decreasing padding spaces before row numbers to center the triangle.

## Code
```c
#include<stdio.h>

int factorial(int n){
    if (n == 0) return 1;
    return n * factorial(n-1);
}
int nCr(int n, int r ){
    return factorial(n) / ( factorial(r) * factorial(n-r));
}
int main(){
    int line;
    scanf("%d", &line);
    for(int n =0 ; n < line ;n++ ){
        for(int i = line - n - 1 ; i > 0 ; i-- ){
            printf(" ");
        }
        for (int r = 0 ; r <= n ; r++){
            printf("%d ",nCr(n , r));
        }
        printf("\n");
    }
    return 0;
}
```

## How it works
1. `factorial(n)` computes $n!$ recursively.
2. `nCr(n, r)` calculates combinations via the quotient of factorials.
3. Nested loops run row $n$ from 0 to $\text{line} - 1$:
   - Prints padding spaces `line - n`.
   - Loops column $r$ from 0 to $n$, printing `nCr(n, r)`.
4. Produces a centered Pascal's triangle.

## Sample run
```text
4
    1 
   1 1 
  1 2 1 
 1 3 3 1 
```

## Gotchas
> [!warning] Factorial Overflow in Combinations
> Computing combinations via full factorials causes 32-bit overflow for $n \ge 13$, even though the resulting combination $\binom{n}{r}$ fits comfortably in an integer. Multiplicative recurrence (used in [[LAB 08 - pascal]]) avoids this overflow.

## My notes
> [!question]- My notes

## Related
- [[LAB 08 - pascal]]
- [[BUET 2025 - factorial]]
