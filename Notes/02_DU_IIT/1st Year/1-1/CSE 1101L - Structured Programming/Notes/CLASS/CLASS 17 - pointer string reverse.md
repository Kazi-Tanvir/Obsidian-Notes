---
title: "CLASS 17 - pointer string reverse"
aliases:
  - pointer string reverse
  - 17_pointer_string_reverse
tags:
  - type/lecture
  - c/pointers
  - c/strings
  - c/pointer-arithmetic
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/17_pointer_string_reverse.c"
number: 17
up: "[[CLASS - Index]]"
prev: "[[CLASS 16 - pointer min max]]"
next: "[[CLASS 18 - pointer books 2d arr]]"
related:
  - "[[LAB 23 - pointer array reverse]]"
  - "[[PRAC LC - Index]]"
  - "[[PRAC CW 06 - pointer reverse string]]"
created: 2026-10-29
status: draft
---
# CLASS 17 - pointer string reverse

> [!abstract] Summary
> Reverses a string in-place using two-pointer symmetric index swapping up to the midpoint of the string.

**Source:** `CLASS/17_pointer_string_reverse.c`

## Problem
Reverse a character string in place ($O(1)$ auxiliary space) without allocating a secondary buffer, swapping characters from outer ends toward the center.

## Concepts used
- **In-Place Transformation**: Mutating the input array directly without allocating additional memory buffers.
- **Symmetric Index Swapping**: In an array of size $N$, element at index $i$ corresponds symmetrically to index $N - 1 - i$. Swapping them inverts the sequence.
- **Midpoint Boundary ($N / 2$)**: The swap loop must stop at $N / 2$; continuing to $N$ would swap the elements a second time, restoring the original order!

## Code
```c
#include<stdio.h>
#include<string.h>

void reverseString(char* s, int sSize) {
    if(sSize <= 1 && sSize>= 100000) return;
    for(int i = 0 ; i < sSize ; i++){
        int ascii = s[i];
        if(ascii > 255 && ascii < 0) return;
    }

    for(int i = 0;i < sSize/2 ; i++){
        char temp = *(s + i);
        *(s + i) = *(s + sSize -1- i); 
        *(s + sSize - i-1) = temp;
    }
}

int main(){
    char str[100];
    fgets(str, sizeof(str), stdin);
    int sSize = strlen(str);

    reverseString(str , sSize);
    printf("%s\n",str);

    return 0;
}
```

## How it works
1. **Signature**: `reverseString(char* s, int sSize)` matches the LeetCode #344 problem signature.
2. **Guard Clause**: Evaluates size constraints.
3. **Swap Loop**:
   - `for (int i = 0; i < sSize / 2; i++)`
   - Uses a temporary variable `temp = s[i]`.
   - `s[i] = s[sSize - 1 - i];`
   - `s[sSize - 1 - i] = temp;`
4. **Main Verification**: Inverts `"Tanvir"` ($N=6$) and prints the resulting reversed string `"rivnaT"`.

## Sample run
```text
rivnaT
```

## Gotchas
> [!warning] Contradictory Guard Condition Bug
> Examine line 4:
> ```c
> if (sSize <= 1 && sSize >= 100000) return;
> ```
> The author used logical AND (`&&`). A number **cannot** be both <= 1 and >= 100000 at the same time! This condition evaluates to false for every possible value, meaning the guard clause is completely inert. It should have been logical OR (`||`).

## My notes
> [!question]- My notes

## Related
- [[LAB 23 - pointer array reverse]] - Recursive pointer-based array reversal
- [[PRAC LC - Index]] - LeetCode #344 solution
- [[PRAC CW 06 - pointer reverse string]] - Concept-wise pointer string reverse
