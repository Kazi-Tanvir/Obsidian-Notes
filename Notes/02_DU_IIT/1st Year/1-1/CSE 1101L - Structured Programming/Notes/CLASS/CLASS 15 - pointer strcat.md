---
title: "CLASS 15 - pointer strcat"
aliases:
  - pointer strcat
  - 15_pointer_strcat
tags:
  - type/lecture
  - c/pointers
  - c/strings
  - c/pointer-arithmetic
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/15_pointer_strcat.c"
number: 15
up: "[[CLASS - Index]]"
prev: "[[CLASS 14 - pointer strcmp]]"
next: "[[CLASS 16 - pointer min max]]"
related:
  - "[[CLASS 11 - string merge]]"
  - "[[LAB 21 - pointer merge]]"
created: 2026-10-29
status: draft
---
# CLASS 15 - pointer strcat

> [!abstract] Summary
> Implements string concatenation using pointer arithmetic offset indexing `*(x + i)`.

**Source:** `CLASS/15_pointer_strcat.c`

## Problem
Append one string onto the tail of another using pointer arithmetic expressions without calling standard `strcat`.

## Concepts used
- **Offset Pointer Arithmetic (`*(x + i)`)**: An alternative syntax to array indexing `x[i]`. The expression `x + i` calculates the memory address shifted by $i \times \text{sizeof(type)}$ bytes, and `*` dereferences it.
- **String Termination**: Appending characters into destination memory and placing a null terminator at the final offset.

## Code
```c
#include<stdio.h>
#include<string.h>

void my_strcat(char *x, char *y){
    int i;
    for(i = strlen(x); i <= (strlen(x) + strlen(y)) ; i++){
        *(x+i) = *y++;
    }
    *(x+i) = '\0';
}

int main(){
    char x[] = "Kazi";
    char y[] = "Tanvir";
    my_strcat(x, y);
    printf("%s",x);
    return 0;
}
```

## How it works
1. **Offset Calculation**: `i` begins at `strlen(x)`, which represents the index of the null terminator in the first string.
2. **Copy Loop**:
   - `for (i = strlen(x); i <= (strlen(x) + strlen(y)); i++) *(x + i) = *y++;`
   - Copies characters from `*y` into `*(x + i)`, post-incrementing `y`.
3. **Termination**: `*(x + i) = '\0';` seals the concatenated string.
4. **Execution in `main()`**: Concatenates `"Tanvir"` onto `"Kazi"` and outputs `x`.

## Sample run
```text
KaziTanvir
```

## Gotchas
> [!warning] Stack Buffer Overflow & Dynamic Re-evaluation of `strlen`
> 1. **Stack Memory Corruption**: In `main()`, `char x[] = "Kazi";` allocates exactly **5 bytes** on the stack. Concatenating `"Tanvir"` writes 11 bytes into `x`, writing 6 bytes past the buffer and corrupting adjacent stack variables!
> 2. **Loop Condition Side-Effect**: In the condition `i <= (strlen(x) + strlen(y))`, `strlen(x)` is re-evaluated on every iteration! As characters are appended into `x`, `x` lengthens, which can cause the upper bound to continually move forward if not cached in a local variable.

## My notes
> [!question]- My notes

## Related
- [[CLASS 11 - string merge]] - Array index string concatenation
- [[LAB 21 - pointer merge]] - Merging arrays using pointers
