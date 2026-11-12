---
title: "BUET 2025 - factorial"
aliases:
  - BUET factorial
  - factorial
tags:
  - type/practice
  - c/recursion
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/2025/factorial.c"
up: "[[BUET - Index]]"
related:
  - "[[BUET 2025 - pascal]]"
  - "[[LAB 15 - sum array recursion]]"
created: 2026-10-29
status: draft
---
# BUET 2025 - factorial

> [!abstract] Summary
> Evaluates the factorial of an integer ($n!$) using recursive self-multiplication down to base case $0! = 1$.

**Source:** `00_BUET_CSE_101/2025/factorial.c`

## Problem
Given a non-negative integer $n$, compute its mathematical factorial $n! = n \times (n-1) \times \dots \times 1$ recursively.

## Concepts used
- **Recursion Base Case:** Halting recursion when $n == 0$, returning 1.
- **Recursive Step:** Evaluating $n \times \text{factorial}(n - 1)$.

## Code
```c
#include<stdio.h>

int factorial(int n){
    if (n == 0){
        return 1;
    }
    return n * factorial(n-1);
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", factorial(n));
    return 0;
}
```

## How it works
1. Reads non-negative integer $n$.
2. In `factorial(n)`, if $n == 0$ returns 1; otherwise evaluates `n * factorial(n - 1)`.
3. Unwinds the recursive call stack and prints result.

## Sample run
```text
5
120
```

## Gotchas
> [!warning] Integer Overflow on Large $n$
> Standard 32-bit signed integers overflow for $n > 12$ ($13! = 6,227,020,800$, exceeding $2^{31} - 1$). Larger factorials require `unsigned long long` or arbitrary-precision libraries.

## My notes
> [!question]- My notes

## Related
- [[BUET 2025 - pascal]]
- [[LAB 15 - sum array recursion]]
