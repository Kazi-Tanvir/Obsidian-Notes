---
title: "CLASS 06 - calc menu switch"
aliases:
  - calc menu switch
  - 06_calc_menu_switch
tags:
  - type/lecture
  - c/control-flow
  - c/functions
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/06_calc_menu_switch.c"
number: 6
up: "[[CLASS - Index]]"
prev: "[[CLASS 05 - vowel switch]]"
next: "[[CLASS 07 - avg temperature array]]"
related:
  - "[[CLASS 01 - calculator]]"
  - "[[ASG 01 - user defined calc]]"
created: 2026-10-29
status: draft
---
# CLASS 06 - calc menu switch

> [!abstract] Summary
> A menu-driven interactive calculator program demonstrating procedural function dispatch via numerical menu choices.

**Source:** `CLASS/06_calc_menu_switch.c`

## Problem
Provide an interactive text console interface where users select mathematical operations from a numbered menu (1 for Add, 2 for Subtract, 3 for Multiply, 4 for Divide) and provide operands for calculation.

## Concepts used
- **Menu-Driven Interface**: Presenting numbered options to the user and executing corresponding logic based on their choice.
- **Procedural Modularity**: Encapsulating mathematical operations inside distinct helper functions (`add`, `sub`, `mul`, `div`).
- **`switch` Multi-Way Selection**: Routing numerical choices (`choice 1, 2, 3, 4`) to corresponding function invocations.

## Code
```c
#include<stdio.h>

int add(int a,int b){
    return a + b;
}

int sub(){
    return a - b;
}

int mul(){
    return a*b;
}

int div(){
    return a/b;
}

int main(){
    char choice;
    int a, b;

    printf("1. Add\n2. Sub\n3. Mul\n4. Div\n");
    printf("Exit by entering x");
    scanf("%c", &choice);
    for(int i = 0 ; c!=x;i++){
        printf("Enter a and b: ");
        scanf("%d %d", &a, &b);
    switch(choice){
        case 'a':
            printf("Result: %d\n", add(a,b));
            break;
        case 's':
            printf("Result: %d\n", sub(a,b));
            break;
        case 'm':
            printf("Result: %d\n", mul(a,b));
            break;
        case 'd':
            printf("Result: %d\n", div(a,b));
            break;
        default:
            printf("Invalid choice\n");
        }
}
    return 0;
}
```

## How it works
1. **Function Declarations**: Functions `add`, `sub`, `mul`, and `div` are declared to perform arithmetic operations.
2. **Menu Loop**: The program prints options 1 through 4 and prompts the user for their choice.
3. **Operand Reading**: Prompts for operands `a` and `b`.
4. **Switch Dispatch**:
   - `case 1`: calls `add(a, b)`
   - `case 2`: calls `sub(a, b)`
   - `case 3`: calls `mul(a, b)`
   - `case 4`: calls `div(a, b)`
   - `default`: prints `"Invalid Choice"`.

## Sample run
> [!note] Traced from the source, not executed.
> Compiling this file produces compile-time syntax errors due to undeclared loop variables and incomplete function parameter definitions. The expected logical behavior when fixed is:
```text
1. Add
2. Subtract
3. Multiply
4. Divide
Choose an option: 1
Enter two numbers: 12 8
Result: 20
```

## Gotchas
> [!warning] Real Compiler Errors in Source Code
> This lecture file exhibits authentic syntax errors:
> 1. **Missing Parameter Declarations**: Functions `sub()`, `mul()`, and `div()` are declared with empty parameter lists `int sub() { return a - b; }`, but reference identifiers `a` and `b` which are undeclared in their local scopes! They must be declared as `int sub(int a, int b)`.
> 2. **Undeclared Loop Control Variables**: In `main()`, the loop statement `for (int i = 0 ; c!=x;i++)` references identifiers `c` and `x` which do not exist anywhere in `main()`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 01 - calculator]] - Single-line expression calculator
- [[ASG 01 - user defined calc]] - Assignment implementation of interactive calculator
