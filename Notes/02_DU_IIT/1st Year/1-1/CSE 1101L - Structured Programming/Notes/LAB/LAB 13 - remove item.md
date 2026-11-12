---
title: "LAB 13 - remove item"
aliases:
  - remove item
  - 13_remove_item
tags:
  - type/lab
  - c/arrays
  - c/searching
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/13_remove_item.c"
number: 13
up: "[[LAB - Index]]"
prev: "[[LAB 12 - swap array]]"
next: "[[LAB 14 - merge array]]"
related:
  - "[[LAB 20 - pointer remove]]"
  - "[[PRAC LC - Index]]"
created: 2026-10-29
status: draft
---
# LAB 13 - remove item

> [!abstract] Summary
> Eliminates duplicate integer values from an array by left-shifting subsequent elements and decrementing the active array size.

**Source:** `LAB/13_remove_item.c`

## Problem
Read an array of $n$ integers, identify duplicate elements, delete duplicate copies by shifting remaining elements to the left, and print the deduplicated array.

## Concepts used
- **In-Place Element Deletion:** Shifting elements `x[k] = x[k+1]` leftwards to overwrite an unwanted element without creating a second array.
- **Dynamic Size Decrement:** Decrementing `n--` so the logical size reflects the deletion.
- **Nested Matching:** Comparing pairs $(i, j)$ where $x[i] == x[j]$ and $i 
e j$.

## Code
```c
#include<stdio.h>

int main(){
    int n;
    printf("Enter the length of array :");
    scanf("%d",&n);
    int x[n];

    //input 
    printf("Enter %d positive integers for x:", n);
    for(int i = 0; i < n;i++){
        scanf("%d",&x[i]);
    }

    for(int i = 0 ; i< n ; i++){
        for(int j = 0; j < n ; j++){
            if(x[i] == x[j] && i!=j){
                for(int k = j;k < n;k++ )
                    x[k]=x[k+1];
                n--;
            }
        }
    }
    printf("Array X\n");
    for(int i = 0; i < n;i++){
            printf("%d ",x[i]);
        
    }
    printf("\n");

}
```

## How it works
1. Allocates variable-length array `x[n]` and reads `n` integers.
2. A nested pair of loops compares `x[i]` against `x[j]`.
3. When a duplicate is detected (`x[i] == x[j] && i != j`), a third loop shifts all items from $k = j$ up to $n - 1$ one position left (`x[k] = x[k+1]`).
4. Decrements `n` and continues scanning.
5. Prints the final deduplicated sequence of length `n`.

## Sample run
```text
Enter the length of array :6
Enter 6 positive integers for x:1 2 2 3 4 4
Array X
1 2 3 4 
```

## Gotchas
> [!warning] Out-of-bounds Read during Shift
> In the shift loop `for (int k = j; k < n; k++) x[k] = x[k+1];`, when $k = n - 1$, `x[k+1]` accesses index $n$, which is one element beyond the allocated boundary. The loop should stop at $k < n - 1$.

## My notes
> [!question]- My notes

## Related
- [[LAB 20 - pointer remove]]
- [[PRAC LC - Index]]
