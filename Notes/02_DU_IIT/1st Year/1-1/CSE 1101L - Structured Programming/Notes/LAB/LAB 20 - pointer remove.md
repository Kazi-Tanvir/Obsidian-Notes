---
title: "LAB 20 - pointer remove"
aliases:
  - pointer remove
  - 20_pointer_remove
tags:
  - type/lab
  - c/pointers
  - c/pointer-arithmetic
  - c/dynamic-memory
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "LAB/20_pointer_remove.c"
number: 20
up: "[[LAB - Index]]"
prev: "[[LAB 19 - pointer swap]]"
next: "[[LAB 21 - pointer merge]]"
related:
  - "[[LAB 13 - remove item]]"
  - "[[PRAC LC - Index]]"
created: 2026-10-29
status: draft
---
# LAB 20 - pointer remove

> [!abstract] Summary
> Removes duplicate integers from a dynamically allocated heap array by shifting subsequent memory cells leftwards via pointer dereferencing.

**Source:** `LAB/20_pointer_remove.c`

## Problem
Allocate a dynamic integer buffer, detect duplicate elements using pointer comparisons, eliminate duplicates in place by shifting remaining elements left, and free heap memory.

## Concepts used
- **Dynamic Allocation with Extra Padding:** Allocating `(n + 1) * sizeof(int)` to provide safe headroom during look-ahead element shifts.
- **Pointer Dereferencing Shifts:** Copying `*(x + k) = *(x + k + 1)` using pointer addition.
- **Resource Deallocation (`free`):** Returning heap memory to the operating system after display.

## Code
```c

#include<stdio.h>
#include<stdlib.h>

int main(){
    int n;
    printf("Enter the length of array :");
    scanf("%d",&n);
    int *x = (int*)malloc((n + 1) * sizeof(int));

    
    printf("Enter %d positive integers for x:", n);
    for(int i = 0; i < n;i++){
        scanf("%d",x+i);
    }
    if (x == NULL ) return 0;

    for(int i = 0 ; i< n ; i++){
        for(int j = 0; j < n ; j++){
            if(*(x + i) == *(x + j) && i!=j){
                for(int k = j;k < n;k++ )
                    *(x+k)=*(x + k + 1);
                n--;
            }
        }
    }
    printf("Array X\n");
    for(int i = 0; i < n;i++){
            printf("%d ",*(x + i));
        
    }
    free(x);
    printf("\n");

}
```

## How it works
1. Allocates heap storage `x` for $n + 1$ integers and reads user input into `x + i`.
2. Compares pairs of elements using `*(x + i) == *(x + j) && i != j`.
3. When duplicate found, shifts elements left from index $j$ up to $n-1$: `*(x + k) = *(x + k + 1)`.
4. Decrements active size `n--`.
5. Prints deduplicated contents and calls `free(x)`.

## Sample run
```text
Enter the length of array :6
Enter 6 positive integers for x:10 20 20 30 40 40
Array X
10 20 30 40 
```

## Gotchas
> [!bug] Misplaced NULL Check
> The check `if (x == NULL) return 0;` is executed on line 16, *after* the `scanf` loop on lines 13–15 has already attempted to dereference `x + i`. If `malloc` fails, the program will crash on the first `scanf` before reaching the safety check.

## My notes
> [!question]- My notes

## Related
- [[LAB 13 - remove item]]
- [[PRAC LC - Index]]
