---
title: "PRAC CW 07 - pointer move zero end"
aliases:
  - pointer move zero end
  - 07_pointer_move_zero_end
tags:
  - type/practice
  - c/pointers
  - c/arrays
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/07_pointer_move_zero_end.c"
up: "[[PRAC - Index]]"
related:
  - "[[PRAC LC - Index]]"
created: 2026-10-29
status: draft
---
# PRAC CW 07 - pointer move zero end

> [!abstract] Summary
> Compacts an array by moving all zero elements to the end while maintaining relative order.

**Source:** `PRACTICE/CONCEPT_WISE/07_pointer_move_zero_end.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer move zero end` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>
#include<math.h>

void moveZeroes(int* nums, int numsSize) {
    if(numsSize < 1 && numsSize > 10000) return;
    for( int i = 0 ; i < numsSize ; i++){
        if(nums[i]< -pow(2,31) && nums[i] > pow(2,31) - 1) return;
    }
    for(int i = 0; i < numsSize ;i++){
        if(*(nums + i) == 0){
            for(int j = i ; j < numsSize ; j++){
                *(nums + j) = *(nums + j + 1);
            }
            *(nums + numsSize - 1) = 0;
            i--;
            numsSize--;
        }
    }
}

int main(){
    int n;
    scanf("%d",&n);
    int nums[n];
    int numSize = sizeof(nums)/sizeof(int);
    for(int i = 0 ; i < numSize ; i++){
        scanf("%d",&nums[i]);
    }
    for(int i = 0 ; i < numSize ; i++){
        printf("%d ",nums[i]);
    }
    printf("\n");
    moveZeroes(nums,numSize);

    for(int i = 0 ; i < numSize ; i++){
        printf("%d ",nums[i]);
    }

}
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.

## My notes
> [!question]- My notes

## Related
- [[PRAC LC - Index]]
