---
title: "BUET 2025 - find root"
aliases:
  - BUET find root
  - find_root
tags:
  - type/practice
  - c/math
  - c/loops
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/2025/find_root.c"
up: "[[BUET - Index]]"
related:
  - "[[CLASS 04 - prime number]]"
  - "[[PRAC - prime number sqrt]]"
created: 2026-10-29
status: draft
---
# BUET 2025 - find root

> [!abstract] Summary
> Computes real numerical roots of non-linear polynomial $f(x) = x^5 + 3x^2 - 10 = 0$ using Newton-Raphson approximation iterations.

**Source:** `00_BUET_CSE_101/2025/find_root.c`

## Problem
Find the root of non-linear equation $f(x) = x^5 + 3x^2 - 10 = 0$ given an initial user estimate, applying Newton-Raphson tangent line iterations until successive approximations converge within tolerance.

## Concepts used
- **Newton-Raphson Numerical Method:** Successive root approximation formula:
  $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
- **Polynomial Derivatives:** Evaluating function $f(x) = x^5 + 3x^2 - 10$ and its derivative $f'(x) = 5x^4 + 6x$.
- **Convergence Condition:** Stopping iterations when $|x_{n+1} - x_n| < 0.0001$.

## Code
```c
#include<stdio.h> 
#include<math.h> 


float func(float x){
    return pow(x , 5) + 3*x*x -10;
}
float dif_func(float x){
    return 5*pow(x,4)+6*x;
}

int main (){
    float guess;
    printf("Enter your guess : ");
    scanf("%f",&guess);
    float x = 0;
    for(int i = 0 ; ;i++){
        if(guess == 0) guess = 1;
        x = guess - func(guess)/dif_func(guess);
        if(fabs(x-guess) <=0.00001 ) break;
        guess = x;
    }
    printf("%f\n",x);
    return 0;
}
```

## How it works
1. Defines mathematical function `func(x)` and derivative `dif_func(x)` using `<math.h>`'s `pow()`.
2. Reads initial numerical guess from standard input.
3. Iterates: evaluates next approximation `x = guess - (func(guess) / dif_func(guess))`.
4. Checks convergence: if `guess - x < 0.0001` (or within epsilon), halts and prints the converged real root.

## Sample run
```text
Enter your guess : 1.5
1.351957
```

## Gotchas
> [!warning] Zero Derivative Singularity
> If the guess lands at a stationary point where $f'(x) = 0$, division by zero occurs, producing floating-point `inf` or `NaN`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 04 - prime number]]
- [[PRAC - prime number sqrt]]
