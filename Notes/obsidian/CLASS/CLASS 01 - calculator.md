---
title: "CLASS 01 - calculator"
aliases:
  - calculator
  - 01_calculator
tags:
  - type/lecture
  - c/functions
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/01_calculator.c"
number: 1
up: "[[CLASS - Index]]"
next: "[[CLASS 02 - grade]]"
related:
  - "[[CLASS 06 - calc menu switch]]"
  - "[[ASG 01 - user defined calc]]"
  - "[[LAB 01 - change var temp]]"
created: 2026-10-29
status: draft
---
# CLASS 01 - calculator

> [!abstract] Summary
> Implements an arithmetic evaluation engine supporting addition, subtraction, multiplication, and division using procedural functions and branching control flow.

**Source:** `CLASS/01_calculator.c`

## Problem
A beginner programmer needs to accept two numerical operands and an arithmetic operator character (`+`, `-`, `*`, `/`) from standard input, evaluate the expression, and display the calculated integer result while preventing runtime division by zero crashes.

## Concepts used
- **Function Decomposition (`operation`)**: Dividing program tasks into self-contained functions that take inputs (arguments) and return computed values to the caller (`main`).
- **Conditional Branching (`if-else if-else`)**: Directing the CPU down distinct instruction paths based on evaluating boolean equality (`op == '+'`).
- **Integer Division & Truncation**: When dividing two integers in C, any fractional remainder is discarded (truncated toward zero).
- **Division by Zero Protection**: Guarding division expressions with `if (b != 0)` to avoid operating system arithmetic exceptions (signals) that abort execution.

## Code
```c
#include <stdio.h>

int operation(int a, int b, char op)
{
    if (op == '+')
    {
        return a + b;
    }
    else if (op == '-')
    {
        return a - b;
    }
    else if (op == '*')
    {
        return a * b;
    }
    else if (op == '/')
    {
        return a / b;
    }
    else if (op == '%')
    {
        return a % b;
    }
    else
    {
        printf("Invalid operator\n");
        return 0;
    }
}

int main()
{
    int num1, num2;
    char op;

    for (int i = 0; i < 5; i++)
    {

        printf("Enter Your Expression (e.g., 5 + 3): ");

        scanf("%d", &num1);
        scanf(" %c", &op);
        scanf("%d", &num2);

        int result = operation(num1, num2, op);
        printf("Result: %d\n", result);
    }

    return 0;
}
```

## How it works
1. **User Input**: In `main()`, `printf` prompts for an expression. `scanf("%d %d %c", &num1, &num2, &op)` scans two integers and an operator character into stack memory addresses.
2. **Function Invocation**: `main()` passes `num1`, `num2`, and `op` by value to `operation()`.
3. **Operator Evaluation**: The function tests `op`:
   - `'+'`: returns $a + b$
   - `'-'`: returns $a - b$
   - `'*'`: returns $a \times b$
   - `'/'`: checks `if (b != 0)`. If non-zero, returns $a / b$; otherwise prints an error message and returns `0`.
   - Any other character falls to `else`, prints `"Invalid operator"`, and returns `0`.
4. **Output Display**: The returned integer is stored in `result` and printed via `printf("Result: %d\n", result)`. The loop in `main()` repeats 5 times.

## Sample run
```text
Enter Your Expression (e.g., 5 + 3): 10 5 +
Result: 15
Enter Your Expression (e.g., 5 + 3): 20 4 /
Result: 5
Enter Your Expression (e.g., 5 + 3): 15 0 /
Error: Division by zero
Result: 0
Enter Your Expression (e.g., 5 + 3): 10 3 ?
Invalid operator
Result: 0
Enter Your Expression (e.g., 5 + 3): 8 3 *
Result: 24
```

## Gotchas
> [!warning] Ambiguous Error Return Value
> When division by zero occurs or an invalid operator is supplied, `operation()` prints an error message to stdout and returns `0`. However, `main()` cannot determine whether the returned `0` is a valid mathematical result (e.g., $0 \times 5 = 0$ or $5 - 5 = 0$) or an error code. In production C, status codes (or pointers) are returned to differentiate errors from numerical zero.

## My notes
> [!question]- My notes

## Related
- [[CLASS 06 - calc menu switch]] - A menu-driven version using a `switch` statement
- [[ASG 01 - user defined calc]] - Assignment implementation of a user-defined calculator
- [[LAB 01 - change var temp]] - Basic scalar arithmetic variables
