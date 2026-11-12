---
title: "CLASS 19 - pointer row sum"
aliases:
  - pointer row sum
  - 19_pointer_row_sum
tags:
  - type/lecture
  - c/pointers
  - c/arrays
  - c/math
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/19_pointer_row_sum.c"
number: 19
up: "[[CLASS - Index]]"
prev: "[[CLASS 18 - pointer books 2d arr]]"
next: "[[CLASS 20 - cmd arg]]"
related:
  - "[[LAB 28 - matrix]]"
  - "[[PRAC CW 05 - pointer sum arr]]"
created: 2026-10-29
status: draft
---
# CLASS 19 - pointer row sum

> [!abstract] Summary
> Examines 2D array memory representation and highlights the non-modifiable lvalue rules governing array names.

**Source:** `CLASS/19_pointer_row_sum.c`

## Problem
Calculate the sum of elements in each row of a $10 \times 20$ two-dimensional integer matrix using pointer traversal.

## Concepts used
- **2D Array Memory Layout (Row-Major Order)**: In C, a 2D array `int b[10][20]` is stored as a single contiguous block of $10 \times 20 \times 4 = 800$ bytes. Row 0 is stored immediately followed by Row 1, Row 2, etc.
- **Array Names are Constant Addresses**: An array name `b[i]` evaluates to the address of the first element of row $i$ (`&b[i][0]`). However, **an array name is not a variable lvalue**; its address is fixed and cannot be modified with increment operators like `b[i]++`.

## Code
```c
#include<stdio.h>

int main(){
    int b[10][20] = {{1,2,3,4,5,6,7,8,9,10,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20,
                     11,12,13,14,15,16,17,18,19,20}};

    for(int i = 0;i<10;i++){
        int sum = 0;
        for(int j = 0;j<20;j++){
            sum += *(b[i]++)
        }
        printf("Row-%d sum = %d\n",i,sum);
    }

    return 0;
}
```

## How it works
1. **Matrix Allocation**: `int b[10][20]` allocates a $10 \times 20$ matrix initialized with numerical constants.
2. **Row Traversal**: Outer loop iterates through each row index `i` from 0 to 9.
3. **Column Summation**: Intended inner loop sums the 20 elements of row `i` and prints `"Row-%d sum = %d"`.

## Sample run
> [!note] Traced from the source, not executed.
> This program fails to compile due to lvalue increment errors on line 19.

## Gotchas
> [!warning] Invalid Increment on Array Name (`lvalue required`)
> The compiler rejects line 19:
> ```c
> sum += *(b[i]++)
> ```
> In C, `b[i]` represents an array of 20 integers (`int[20]`). Although `b[i]` decays to a pointer (`int*`) when passed to expressions, `b[i]` itself is a constant base address, **not a modifiable pointer variable**! Attempting `b[i]++` results in:
> `error: lvalue required as increment operand`
> **Correct Fix**: Assign the row address to an explicit pointer variable:
> ```c
> int *p = b[i];
> for (int j = 0; j < 20; j++) {
>     sum += *p++;
> }
> ```
> Additionally, line 19 is missing a terminating semicolon `;`.

## My notes
> [!question]- My notes

## Related
- [[LAB 28 - matrix]] - Complete working 2D matrix multiplication
- [[PRAC CW 05 - pointer sum arr]] - 1D array summation via pointers
