---
title: "BUET 2025 - prime number"
aliases:
  - BUET prime number
  - 2025 prime_number
tags:
  - type/practice
  - c/math
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/2025/prime_number.c"
up: "[[BUET - Index]]"
related:
  - "[[CLASS 04 - prime number]]"
  - "[[PRAC - prime number sqrt]]"
created: 2026-10-29
status: draft
---
# BUET 2025 - prime number

> [!abstract] Summary
> Tests positive integers for primality using square root loop bounds, reporting whether the candidate is prime or composite.

**Source:** `00_BUET_CSE_101/2025/prime_number.c`

## Problem
Read a positive integer, test divisibility from 2 up to $\sqrt{n}$, and report whether the number is prime.

## Concepts used
- **Square Root Upper Limit:** Limiting divisor checks to $i < \sqrt{n}$.
- **Input Validation:** Rejecting negative integers.

## Code
```c
#include<stdio.h>
#include<math.h>

int main(){
    int num ; 
    printf("Enter a Positive Number : ");
    scanf("%d",&num);
    if (num < 0){
        printf("Please enter a positive number");
        return 0;
    }
    int isPrime = 1;
    for(int i = 2 ; i <sqrt(num);i++ ){
        if( num == 0 || num == 1 ||num % i == 0) {
            isPrime = 0;
            break;
        }
    }
    isPrime == 1? printf("IsPrime"):printf("Not Prime");
    return 0;
}
```

## How it works
1. Reads integer `num`. If negative, prints warning and terminates.
2. Loops $i$ from 2 while $i < \sqrt{\text{num}}$:
   - If `num % i == 0`, marks `isPrime = 0` and breaks.
3. If `isPrime == 1`, prints `IsPrime`.

## Sample run
```text
Enter a Positive Number : 17
IsPrime
```

## Gotchas
> [!warning] Strict Inequality in Sqrt Bound
> Using `i < sqrt(num)` rather than `i <= sqrt(num)` misses square factors of perfect squares (e.g. 9, 25, 49), mistakenly reporting them as prime! The condition must be `i <= sqrt(num)`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 04 - prime number]]
- [[PRAC - prime number sqrt]]
