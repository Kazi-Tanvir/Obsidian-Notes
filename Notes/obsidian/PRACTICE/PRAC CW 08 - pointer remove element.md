---
title: "PRAC CW 08 - pointer remove element"
aliases:
  - pointer remove element
  - 08_pointer_remove_element
tags:
  - type/practice
  - c/pointers
  - c/arrays
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/08_pointer_remove_element.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 20 - pointer remove]]"
created: 2026-10-29
status: draft
---
# PRAC CW 08 - pointer remove element

> [!abstract] Summary
> Removes target elements from an array in place by shifting remaining elements leftward.

**Source:** `PRACTICE/CONCEPT_WISE/08_pointer_remove_element.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer remove element` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>
#include<math.h>

void moveZeroes(int* nums, int numsSize , int val) {
    if(numsSize < 1 && numsSize > 10000) return;
    for( int i = 0 ; i < numsSize ; i++){
        if(nums[i]< -pow(2,31) && nums[i] > pow(2,31) - 1) return;
    }
    for(int i = 0; i < numsSize ;i++){
        if(*(nums + i) == val){
            for(int j = i ; j < numsSize ; j++){
                *(nums + j) = *(nums + j + 1);
            }
            *(nums + numsSize - 1) = "";
            i--;
            numsSize--;
        }
    }
}

int main(){
    int n ,val;
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
    
    scanf("%d",&val);

    moveZeroes(nums,numSize,val);

    for(int i = 0 ; i < numSize ; i++){
        printf("%d ",nums[i]);
    }

}
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.
## Gotchas
> [!bug] Type Incompatibility in Zero Assignment
> On line 14, `*(nums + numsSize - 1) = "";` attempts to assign a string literal `""` to an `int` element. This causes a compiler error under standard GCC flags; it should be assigned integer `0`.


## My notes
> [!question]- My notes

## Related
- [[LAB 20 - pointer remove]]
