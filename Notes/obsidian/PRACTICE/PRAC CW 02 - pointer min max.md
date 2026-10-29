---
title: "PRAC CW 02 - pointer min max"
aliases:
  - pointer min max
  - 02_pointer_min_max
tags:
  - type/practice
  - c/pointers
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/02_pointer_min_max.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 16 - pointer min max]]"
created: 2026-10-29
status: draft
---
# PRAC CW 02 - pointer min max

> [!abstract] Summary
> Locates the minimum and maximum elements of an array using pointer traversal.

**Source:** `PRACTICE/CONCEPT_WISE/02_pointer_min_max.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer min max` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
    #include<stdio.h>

    void get_min_max(int *arr, int size, int *min ,int *max){
        for(int i = 0 ;i < size-1; i++){
            for(int j = 0; j < size - i - 1;j++){
                if(*(arr + j) > *(arr + j + 1)){
                    int temp = *(arr + j);
                    *(arr + j) = *(arr + j + 1);
                    *(arr + j + 1) = temp;
                }
            }
        }
        *min = *(arr);
        *max = *(arr + size -1);
    }

    int main(){
        int size;
        int min ,max;
        scanf("%d",&size);

        int arr[size];
        for(int i = 0; i < size; i++){
            scanf("%d",arr + i);
        }

        get_min_max(arr, size, &min, &max);
        printf("min:%d\nmax:%d\n",min,max);
        
        return 0; 
    }
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.

## My notes
> [!question]- My notes

## Related
- [[CLASS 16 - pointer min max]]
