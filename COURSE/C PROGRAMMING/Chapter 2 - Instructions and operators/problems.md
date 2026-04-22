# Chapter 2 - Practice Set

## Problem 1
Which of the following is invalid in C?
a. `int a=1; int b = a;`
b. `int v = 3^3;`
c. `char dt = '21 dec 2020';`

**Solution:**
- `c` is invalid because character variables can only store a single character, not a string or multiple characters.
- `b` is technically valid C but `^` is bitwise XOR, not exponentiation.

## Problem 2
What data type will 3.0/8 - 2 return?

**Solution:**
It will return a `double` (or `float`) because `3.0` is a floating-point literal. The result is `-1.625`.

## Problem 3
Write a program to check whether a number is divisible by 97 or not.

**Solution:**
```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter the number: ");
    scanf("%d", &num);
    printf("Divisibility test returns: %d\n", num % 97 == 0);
    return 0;
}
```

## Problem 4
Explain step by step evaluation of `3*x/y - z+k`, where `x=2, y=3, z=3, k=1`

**Solution:**
```c
3 * 2 / 3 - 3 + 1
6 / 3 - 3 + 1
2 - 3 + 1
-1 + 1
0
```

## Problem 5
`3.0 + 1` will be:
a. Integer.
b. Floating point number.
c. Character.

**Solution:**
`b. Floating point number.`
