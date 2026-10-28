---
title: "CLASS 13 - pointer strcpy"
aliases:
  - pointer strcpy
  - 13_pointer_strcpy
tags:
  - type/lecture
  - c/pointers
  - c/strings
  - c/pointer-arithmetic
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/13_pointer_strcpy.c"
number: 13
up: "[[CLASS - Index]]"
prev: "[[CLASS 12 - pointer strlen]]"
next: "[[CLASS 14 - pointer strcmp]]"
related:
  - "[[CLASS 09 - string copy]]"
  - "[[LAB 19 - pointer swap]]"
created: 2026-10-29
status: draft
---
# CLASS 13 - pointer strcpy

> [!abstract] Summary
> Demonstrates the classic C pointer copy idiom `*dest++ = *src++` to duplicate strings across memory buffers.

**Source:** `CLASS/13_pointer_strcpy.c`

## Problem
Copy all characters from a source string into a destination buffer using bare-metal pointer dereferencing and advancing.

## Concepts used
- **Classic Copy Idiom (`*dest++ = *src++`)**: Dereferences `src` to read a character, stores it at the address referenced by `dest`, and then post-increments both pointer addresses to point to the next bytes.
- **Pass-by-Reference via Pointers**: Because functions receive pointers (addresses), modifications through `*dest` directly alter the caller's memory buffer.
- **Explicit Sentinel Writing**: Setting `*dest = '\0'` after the copy loop to terminate the new string.

## Code
```c
#include<stdio.h>

void my_strcpy(char *dest, char *src){
    for(;*src;){
        *dest++ = *src++;
    }
    *dest = '\0';
}

int main(){
    char x[] = "Tanvir";
    char y[10];
    my_strcpy(x, y);
    printf("%s",y);
    return 0;
}
```

## How it works
1. **Function Definition**: `my_strcpy(char *dest, char *src)` accepts two pointer variables pointing to destination and source buffers.
2. **Copy Loop**: `for (; *src;) { *dest++ = *src++; }`
   - Checks `*src`: while the character at `src` is not `'\0'`, execution continues.
   - `*dest++ = *src++`: assigns the current source byte to destination, then advances both pointers.
3. **Termination**: `*dest = '\0';` writes the null byte at the final position.

## Sample run
```text
[no stdout or garbage printed]
```

## Gotchas
> [!warning] Parameter Inversion in Caller
> Look closely at `main()`:
> ```c
> char x[] = "Tanvir";
> char y[10];
> my_strcpy(x, y);
> printf("%s", y);
> ```
> `my_strcpy` is defined as `(char *dest, char *src)`. But `main()` called `my_strcpy(x, y)`!
> This passes populated string `x` as the **destination** and uninitialized buffer `y` as the **source**!
> As a result, the function reads uninitialized garbage memory from `y` and writes it over `"Tanvir"` in `x`, while `y` remains untouched and uninitialized! Calling `printf("%s", y)` prints empty or garbage text. The call should have been `my_strcpy(y, x);`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 09 - string copy]] - Array index string copy
- [[LAB 19 - pointer swap]] - Swapping values using pointers
