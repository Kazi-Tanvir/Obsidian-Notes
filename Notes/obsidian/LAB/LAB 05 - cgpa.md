---
title: "LAB 05 - cgpa"
aliases:
  - cgpa
  - 05_cgpa
tags:
  - type/lab
  - c/arrays
  - c/loops
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/05_cgpa.c"
number: 5
up: "[[LAB - Index]]"
prev: "[[LAB 04 - change calc simplified]]"
next: "[[LAB 06 - discount]]"
related:
  - "[[CLASS 02 - grade]]"
  - "[[PRAC - cgpa calculator]]"
created: 2026-10-29
status: draft
---
# LAB 05 - cgpa

> [!abstract] Summary
> Calculates a student's weighted Grade Point Average (GPA) across multiple academic courses based on marks and credit hours.

**Source:** `LAB/05_cgpa.c`

## Problem
In a university semester, each course carries a specific credit weight and letter grade point. Calculate the student's final Grade Point Average using the standard weighted credit formula:
$$	ext{GPA} = rac{\sum (	ext{Grade Point}_i 	imes 	ext{Credits}_i)}{\sum 	ext{Credits}_i}$$

## Concepts used
- **Weighted Average Calculation**: Multiplying each grade point by its corresponding course credit hours, summing the products, and dividing by total credit hours.
- **Grade Point Translation**: Mapping numerical exam marks (0?100) to standard university GPA points (4.0, 3.75, 3.5, etc.).
- **Array Accumulation**: Looping over course arrays to calculate running totals.

## Code
```c
#include <stdio.h>

// CGPA Calculation
//  80 > 4
//  75 > 3.75
//  70 > 3.5
//  65 > 3.25
//  60 > 3
//  55 > 2.75
//  50 > 2.5
//  45> 2.25
//  40 > 2
//  40 < 0

float checkCGPA(int marks)
{
    float cgpa;
    // if (marks )
    if (marks >= 80 && marks <= 100)
    {
        cgpa = 4.0;
    }
    else if (marks >= 75)
    {
        cgpa = 3.75;
    }
    else if (marks >= 70)
    {
        cgpa = 3.5;
    }
    else if (marks >= 65)
    {
        cgpa = 3.25;
    }
    else if (marks >= 60)
    {
        cgpa = 3.0;
    }
    else if (marks >= 55)
    {
        cgpa = 2.75;
    }
    else if (marks >= 50)
    {
        cgpa = 2.5;
    }
    else if (marks >= 45)
    {
        cgpa = 2.25;
    }
    else if (marks >= 40)
    {
        cgpa = 2.0;
    }
    else
    {
        cgpa = 0;
    }
    return cgpa;
}

void main()
{
    int sub[7], cgpa[7];
    printf("enter Your Marks : (Format is 110X) \n");

    for (int i = 0; i < 7; i++)
    {

        scanf("%d", &sub[i]);
    }

    float sum = 0;
    for (int i = 0; i < 7; i++)
    {

        if (i < 6)
        {
            sum += checkCGPA(sub[i]) * 3;
        }
        else
        {
            sum += checkCGPA(sub[i]) * 1.5;
        }
    }

    float grade = sum / 19.5;

    printf("%.2f", grade);
}
```

## How it works
1. **Course Marks Input**: Prompts for marks across first-semester courses (`1101, 1102, 1103, 1105, 1106, 1107, 1101L`).
2. **Grade Point Mapping**: Converts raw marks into grade points (e.g. $\ge 80 ightarrow 4.0$).
3. **Weighting**: Multiplies grade point by credit weight (e.g. 3.0 credits for theory, 1.5 credits for lab).
4. **Final Computation**: Sums total quality points, divides by total credits (20.5 credits), and prints final GPA.

## Sample run
```text
enter Your Marks : (Format is 110X) 
75 80 65 70 85 60 78
2.85
```

## Gotchas
> [!warning] Precision Loss in Grade Averaging
> Always perform GPA accumulation using `double` or `float`. Dividing total points as integers would truncate the decimal portion, turning a 3.85 GPA into a 3.0!

## My notes
> [!question]- My notes

## Related
- [[CLASS 02 - grade]] - Letter grade classification
- [[PRAC - cgpa calculator]] - Standalone practice CGPA script
