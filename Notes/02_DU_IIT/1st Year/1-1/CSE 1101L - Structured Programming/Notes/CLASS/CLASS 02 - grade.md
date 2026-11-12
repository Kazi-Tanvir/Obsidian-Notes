---
title: "CLASS 02 - grade"
aliases:
  - grade
  - 02_grade
tags:
  - type/lecture
  - c/control-flow
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/02_grade.c"
number: 2
up: "[[CLASS - Index]]"
prev: "[[CLASS 01 - calculator]]"
next: "[[CLASS 03 - number game]]"
related:
  - "[[ASG 06 - grading app]]"
  - "[[LAB 06 - discount]]"
created: 2026-10-29
status: draft
---
# CLASS 02 - grade

> [!abstract] Summary
> Evaluates student numerical examination scores against standard academic grade thresholds using sequential conditional branching ladders.

**Source:** `CLASS/02_grade.c`

## Problem
Given a student's numerical exam score (marks), categorize their academic performance into letter grades: A+ (80+), A (70?79), B (60?69), C (50?59), D (40?49), or F (<40).

## Concepts used
- **Conditional Ladder (`if-else if-else`)**: A sequential control structure where conditions are evaluated from top to bottom; the first true expression executes, and all remaining branches are skipped.
- **Relational Operators (`>=`, `<`)**: Boolean comparison operators producing `1` (true) or `0` (false) used to establish numerical bounds.
- **Order of Evaluation**: By structuring conditions in descending order (`marks >= 80`, then `marks >= 70`, etc.), each subsequent branch implicitly knows the upper bound without requiring redundant compound conditions like `marks >= 70 && marks < 80`.

## Code
```c
#include<stdio.h>

int main()
{
    int marks;
    char grade;

    printf("Enter your marks: ");
    scanf("%d", &marks);

    if (marks >= 80)
    {
        grade = 'A+';
    }
    else if (marks >= 70)
    {
        grade = 'A';
    }
    else if (marks >= 60)
    {
        grade = 'A-';
    }
    else if (marks >= 50)
    {
        grade = 'B';
    }
    else if (marks >= 40)
    {
        grade = 'C';
    }
    else if (marks >= 30)
    {
        grade = 'D';
    }
    else
    {
        grade = 'F';
    }

    printf("Your grade is: %c\n", grade);

    return 0;
}
```

## How it works
1. **Input Allocation**: An integer `marks` is allocated on the stack. `scanf("%d", &marks)` reads the integer entered by the user.
2. **Threshold Evaluation**:
   - `marks >= 80`: executes the first branch.
   - `marks >= 70`: triggered only if marks are between 70 and 79.
   - `marks >= 60`: triggered for 60 to 69.
   - `marks >= 50`: triggered for 50 to 59.
   - `marks >= 40`: triggered for 40 to 49.
   - `else`: triggers for any score below 40, assigning grade `'F'`.

## Sample run
```text
Enter your marks: 85
Your grade is: +

Enter your marks: 74
Your grade is: A

Enter your marks: 32
Your grade is: F
```

## Gotchas
> [!warning] Printf Format Specifier Character Bug
> Notice the first branch of the source code:
> ```c
> if (marks >= 80) {
>     printf("Your grade is: %c\n", '+');
> }
> ```
> The author intended to print `"A+"`, but passed the character constant `'+'` to `%c`. Consequently, entering a mark >= 80 outputs `"Your grade is: +"` instead of `"A+"`! The string specifier `%s` with `"A+"` should have been used.

## My notes
> [!question]- My notes

## Related
- [[ASG 06 - grading app]] - Full file-backed student grading management system
- [[LAB 06 - discount]] - Multi-threshold conditional calculations
