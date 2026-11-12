---
title: "PRAC - prime number sqrt"
aliases:
  - prime number sqrt
  - prime_number_sqrt
tags:
  - type/practice
  - c/math
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/prime_number_sqrt.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 04 - prime number]]"
  - "[[ASG 08 - recursion practice]]"
created: 2026-10-29
status: draft
---
# PRAC - prime number sqrt

> [!abstract] Summary
> An optimized primality testing program evaluating candidate divisors up to $\sqrt{n}$ rather than $n$, cutting execution complexity from $O(n)$ to $O(\sqrt{n})$.

**Source:** `PRACTICE/prime_number_sqrt.c`

## Problem
Determine whether an integer $n$ is prime by testing trial divisors only up to $\lfloor \sqrt{n} \rfloor$, demonstrating algorithmic optimization over naive linear trial division.

## Concepts used
- **Mathematical Optimization ($O(\sqrt{n})$):** If $n$ has a divisor greater than $\sqrt{n}$, its complementary factor must be smaller than $\sqrt{n}$. Thus, testing up to $\sqrt{n}$ guarantees finding any non-trivial factor.
- **Divisibility Check:** Checking `n % i == 0` for $2 \le i \le \sqrt{n}$.
- **Edge Case Filtering:** Rejecting $n \le 1$ immediately as non-prime.

## Code
```c
#include<stdio.h>
#include<math.h>

int main()
{
    int num  , isPrime = 1;

    for (int i  = 0 ; i < 5; i++)
    {
        printf("Enter a number: ");
        scanf("%d", &num);

        if (num <= 1)
        {
            isPrime = 0;
        }
        else
        {
            for (int j = 2; j <= sqrt(num); j++)
            {
                if (num % j == 0)
                {
                    isPrime = 0;
                    break;
                }
            }
        }

        if (isPrime)
        {
            printf("%d is a prime number.\n", num);
        }
        else
        {
            printf("%d is not a prime number.\n", num);
        }
    }

    return 0;
}

// Concept on why it work 
// usual approach check every number from 1 to n | takes maximum n-1 times
// second approach check every number from 2 to n/2 | takes maximum n/2 - 1 times
// third approach check every number from 2 to sqrt(n) | takes maximum sqrt(n) - 1 times
// Why it works ?
// there are arithmetic average and geometric average 
// n/2 usage is arithmetic average and sqrt(n) usage is geometric average
```

## How it works
1. Reads candidate integer $n$.
2. Checks baseline: if $n \le 1$, reports not prime.
3. Loops $i$ from 2 while $i \times i \le n$:
   - If `n % i == 0`, flags `isPrime = 0` and breaks immediately.
4. If loop completes without finding a divisor, confirms that $n$ is a prime number.

## Sample run
```text
Enter a number: 997
997 is a prime number.
```

## Gotchas
> [!warning] Floating-Point Inaccuracies in `sqrt()`
> Using `i * i <= n` avoids calling `<math.h>`'s `sqrt()`, eliminating floating-point rounding errors and avoiding linking dependencies with `-lm`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 04 - prime number]]
- [[ASG 08 - recursion practice]]
