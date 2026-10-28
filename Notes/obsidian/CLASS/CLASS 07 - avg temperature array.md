---
title: "CLASS 07 - avg temperature array"
aliases:
  - avg temperature array
  - 07_avg_temperature_array
tags:
  - type/lecture
  - c/arrays
  - c/loops
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/07_avg_temperature_array.c"
number: 7
up: "[[CLASS - Index]]"
prev: "[[CLASS 06 - calc menu switch]]"
next: "[[CLASS 08 - string length]]"
related:
  - "[[LAB 05 - cgpa]]"
  - "[[PRAC CW 05 - pointer sum arr]]"
created: 2026-10-29
status: draft
---
# CLASS 07 - avg temperature array

> [!abstract] Summary
> Demonstrates 1D fixed-size array allocation and accumulation over a sequence of numerical readings.

**Source:** `CLASS/07_avg_temperature_array.c`

## Problem
Store 7 consecutive daily temperature readings in memory and calculate their average value using array indexing and a summation loop.

## Concepts used
- **1D Fixed-Size Arrays (`int temp[7]`)**: Contiguous blocks of memory holding multiple elements of the identical data type, indexed from $0$ to $N-1$.
- **Zero-Based Indexing**: In C, array indices start at 0. For an array of size 7, valid indices are `0, 1, 2, 3, 4, 5, 6`. Accessing `temp[7]` is an illegal out-of-bounds access.
- **Accumulator Pattern**: Initializing a summation variable (`sum = 0`) before a loop and adding each element `sum += temp[i]`.

## Code
```c
#include<stdio.h>

int main(){
    int temp[7];
    int sum = 0;
    printf("Enter the temperature of 7 days: ");
    for(int i = 0;i<7;i++){
        scanf(" %d", &temp[i]);
        sum += temp[i];
    }
    int avg = sum/7;
    printf("Average temperature: %d", avg);
    return 0;
}
```

## How it works
1. **Stack Allocation**: `int temp[7];` reserves 28 contiguous bytes ($7 \times 4$ bytes) on the stack frame. `int sum = 0;` initializes the accumulator.
2. **Summation Traversal**: A loop runs with `i` from 0 to 6, accumulating `sum += temp[i]`.
3. **Average Calculation**: Calculates `sum / 7` and prints `"Average temperature: %d"`.

## Sample run
```text
Enter the temperature of 7 days: Average temperature: 293339894
```

## Gotchas
> [!warning] Uninitialized Array & Integer Division Truncation
> 1. **Reading Garbage Memory**: The source code prints `"Enter the temperature of 7 days:"`, but **forgets to call `scanf`** to read values! Because local variables in C contain whatever random bits previously resided on the stack, the loop sums uninitialized garbage memory, yielding wild outputs like `293339894`!
> 2. **Integer Truncation**: Even when populated, `sum / 7` performs integer division. An actual average of 25.7 truncates to 25. To preserve decimal accuracy, write `(float)sum / 7.0f`.

## My notes
> [!question]- My notes

## Related
- [[LAB 05 - cgpa]] - Array summation and weighted GPA averaging
- [[PRAC CW 05 - pointer sum arr]] - Summing array elements using pointer arithmetic
