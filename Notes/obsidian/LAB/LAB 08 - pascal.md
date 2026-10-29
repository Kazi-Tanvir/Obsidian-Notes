---
title: "LAB 08 - pascal"
aliases:
  - pascal
  - 08_pascal
tags:
  - type/lab
  - c/loops
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/08_pascal.c"
number: 8
up: "[[LAB - Index]]"
prev: "[[LAB 07 - hollow triangle]]"
next: "[[LAB 09 - password]]"
related:
  - "[[BUET 2025 - pascal]]"
  - "[[LAB 07 - hollow triangle]]"
created: 2026-10-29
status: draft
---
# LAB 08 - pascal

> [!abstract] Summary
> Generates Pascal's triangle of height $N$ using binomial coefficient recurrence relationships in nested loops.

**Source:** `LAB/08_pascal.c`

## Problem
Generate and display the first $N$ rows of Pascal's triangle, where each entry is the sum of the two numbers directly above it, or mathematically: $inom{n}{k} = rac{n!}{k!(n-k)!}$.

## Concepts used
- **Binomial Coefficient Recurrence**: Rather than recomputing expensive factorials for each term, consecutive terms in row $n$ are computed in $O(1)$ time via:
  $$inom{n}{k} = inom{n}{k-1} 	imes rac{n - k + 1}{k}$$
- **Nested Iteration**: Outer loop controls row $n$, inner loop generates terms $k$ from 0 to $n$.

## Code
```c
#include<stdio.h>

int factorial(int n){
    if(n==0) return 1;
    return n*factorial(n-1);
}

int main(){
    int height ;
    printf("Enter the trianngle height : ");
    scanf("%d",&height);

    for(int i = 0; i <= height ; i++){
        for(int j = 0;j<= i;j++){
            int value = factorial(i)/(factorial(i-j)*factorial(j));
            printf("%d " ,value);
        }
        printf("\n");
    }
}
```

## How it works
1. **Input**: Reads triangle height `n`.
2. **Row Generation**:
   - Starts each row with `val = 1`.
   - Inner loop computes subsequent terms using integer multiplication and division: `val = val * (i - j) / j;`.
3. **Display**: Prints terms separated by spaces, concluding each row with a newline.

## Sample run
```text
Enter the trianngle height : 5
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1
```

## Gotchas
> [!warning] Multiplication Before Division
> In the recurrence `val = val * (i - j) / j;`, **multiplication must precede division**! If division were executed first (`(val / j) * (i - j)`), integer truncation would immediately zero out fractional terms, breaking the entire row.

## My notes
> [!question]- My notes

## Related
- [[BUET 2025 - pascal]] - External university Pascal's triangle problem
- [[LAB 07 - hollow triangle]] - 2D geometric nested loop structures
