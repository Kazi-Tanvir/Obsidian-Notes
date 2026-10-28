---
title: "CLASS 04 - prime number"
aliases:
  - prime number
  - 04_prime_number
tags:
  - type/lecture
  - c/math
  - c/loops
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/04_prime_number.c"
number: 4
up: "[[CLASS - Index]]"
prev: "[[CLASS 03 - number game]]"
next: "[[CLASS 05 - vowel switch]]"
related:
  - "[[PRAC - prime number sqrt]]"
  - "[[ASG 08 - recursion practice]]"
  - "[[BUET 2025 - prime number]]"
created: 2026-10-29
status: draft
---
# CLASS 04 - prime number

> [!abstract] Summary
> Tests integer primality using trial division up to $n/2$ with an early loop exit flag.

**Source:** `CLASS/04_prime_number.c`

## Problem
Determine whether an arbitrary positive integer $n$ is a prime number (divisible only by 1 and itself) or a composite number.

## Concepts used
- **Trial Division**: Testing potential divisors from 2 upward to see if any divisor evenly divides $n$ (`num % i == 0`).
- **Boolean Flag Idiom**: Using an integer (`isPrime = 1`) to represent true/false state across loop iterations.
- **Modulo Arithmetic (`%`)**: The remainder operator; `a % b == 0` proves that $b$ is an exact factor of $a$.
- **Early Break**: Calling `break` as soon as the first factor is discovered, avoiding unnecessary computations.

## Code
```c
#include<stdio.h>

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
            for (int j = 2; j <= num / 2; j++)
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
```

## How it works
1. **Loop Framework**: An outer `for (int j = 0; j < 5; j++)` allows testing 5 numbers in a single session.
2. **Flag Initialization**: `isPrime` is reset to `1` (assumed prime) at the start of each test.
3. **Divisor Search**: The loop iterates `i` from `2` up to `num / 2`:
   - If `num % i == 0`, a factor exists: `isPrime` is set to `0` and `break` terminates the trial loop immediately.
4. **Classification**:
   - `if (isPrime == 1)`: prints that `num` is a prime number.
   - `else`: prints that `num` is not a prime number.

## Sample run
```text
Enter a number: 17
17 is a prime number.
Enter a number: 24
24 is not a prime number.
Enter a number: 2
2 is a prime number.
Enter a number: 9
9 is not a prime number.
Enter a number: 1
1 is a prime number.
```

## Gotchas
> [!warning] Edge Cases <= 1 and Algorithmic Complexity
> 1. **Input 1**: Mathematically, 1 is neither prime nor composite. However, for `num = 1`, the loop condition `i <= 1/2` ($2 <= 0$) is immediately false. The loop never executes, leaving `isPrime = 1`, which falsely reports 1 as prime!
> 2. **Algorithmic Inefficiency**: Checking divisors up to $n/2$ takes $O(n)$ time. Any composite number must have a factor <= sqrt(n); checking up to sqrt(n) drops complexity to $O(\sqrt{n})$ (see [[PRAC - prime number sqrt]]).

## My notes
> [!question]- My notes

## Related
- [[PRAC - prime number sqrt]] - Optimized primality testing using sqrt(n)
- [[ASG 08 - recursion practice]] - Recursive primality checking
- [[BUET 2025 - prime number]] - External university primality problem
