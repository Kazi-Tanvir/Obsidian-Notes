---
title: "PRAC PYG 01 - final 23 2d"
aliases:
  - final 23 2d
  - 01_Final_23_2d
tags:
  - type/practice
  - c/loops
  - c/math
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/PYG/01_Final_23_2d.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 04 - prime number]]"
  - "[[PRAC - prime number sqrt]]"
created: 2026-10-29
status: draft
---
# PRAC PYG 01 - final 23 2d

> [!abstract] Summary
> Solves University Final Exam 2023 Question 2(d): prints a progressive prime factorization ladder with indented formatting showing successive factor extractions.

**Source:** `PRACTICE/PYG/01_Final_23_2d.c`

## Problem
For an integer $n$, iteratively extract its smallest non-trivial divisor, print the divisor and remaining quotient with increasing indentation at each step, and terminate when the quotient reduces to prime.

## Concepts used
- **Smallest Divisor Extraction (`Divisor`):** Searching for the lowest integer factor $i \ge 2$ where $n \% i == 0$.
- **Indentation Formatting:** Printing $k$ spaces on each row to visually depict a recursive-style factorization tree.
- **Iterative Reduction:** Updating $n = n / \text{divisor}$ and incrementing space counter $k$.

## Code
```c
#include<stdio.h>

int Divisor(int n){
    if(n == 2) return 1;
    for(int i = 2 ; i < n; i++ ){
        if(n%i==0) return i;
    }
    return 1;
}

int main(void){
    int n = 23;
    int k = 0;
    printf("%d\n",n);
    for(int i = 1;;i++){
        for(int j = 0; j < k ; j++){
            printf(" ");
        }
        int divisor = Divisor(n);
        if(divisor == 1){
            printf("%d %d",n,divisor);
            break;
        }
        else{
            printf("%d %d\n",divisor,n/divisor);
            n = n/divisor;
            k++;
        }
    }
}
```

## How it works
1. Initializes $n = 23$ (or arbitrary input).
2. Prints $n$.
3. Inside an infinite loop:
   - Prints $k$ leading spaces.
   - Finds smallest divisor via `Divisor(n)`.
   - If divisor is 1, $n$ is prime; prints final values and breaks.
   - Otherwise, prints divisor and quotient, updates $n = n / \text{divisor}$, and increments indentation $k$.

## Sample run
```text
23
23 1
```

## Gotchas
> [!warning] Special Case for 2
> In `Divisor(int n)`, line 4 contains `if (n == 2) return 1;`. Returning 1 for 2 treats 2 as having no factor other than 1, allowing the loop to break cleanly for prime terminations.

## My notes
> [!question]- My notes

## Related
- [[CLASS 04 - prime number]]
- [[PRAC - prime number sqrt]]
