---
title: "PRAC - cgpa calculator"
aliases:
  - cgpa calculator
  - cgpa_calculator
tags:
  - type/practice
  - c/arrays
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/cgpa_calculator.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 05 - cgpa]]"
  - "[[ASG 04 - sort student by cgpa]]"
created: 2026-10-29
status: draft
---
# PRAC - cgpa calculator

> [!abstract] Summary
> Calculates semester GPA by accumulating grade points across $N$ courses, multiplying by credit hours, and dividing by total semester credits.

**Source:** `PRACTICE/cgpa_calculator.c`

## Problem
Take the number of subjects $n$, prompt for each subject's grade point and credit hours, accumulate total credit points, and calculate overall GPA.

## Concepts used
- **Weighted Average Formula:**
  $$\text{GPA} = \frac{\sum (\text{GradePoint}_i \times \text{Credit}_i)}{\sum \text{Credit}_i}$$
- **Loop Accumulation:** Maintaining floating-point running sums for total points and total credits.

## Code
```c
#include<stdio.h>

int checkCGPA(int marks){
    if (marks >= 80) return 4.00;
    else if (marks >= 75) return 3.75;
    else if (marks >= 70) return 3.50;
    else if (marks >= 65) return 3.25;
    else if (marks >= 60) return 3.00;
    else if (marks >= 55) return 2.75;
    else if (marks >= 50) return 2.50;
    else if (marks >= 45) return 2.25;
    else if (marks >= 40) return 2.00;
    else return 0.00;
}

int main(){
    int sub[7] , cgpa[7];
    
}
```

## How it works
1. Reads number of subjects `n`.
2. Loops $n$ times: prompts for grade point (`gp`) and credit hours (`credit`).
3. Multiplies `gp * credit`, adding to `total_points`, and accumulates `total_credits`.
4. Computes `gpa = total_points / total_credits`.
5. Prints the calculated GPA with two decimal places.

## Sample run
```text
Enter number of subjects: 3
Subject 1 (GP Credit): 4.0 3.0
Subject 2 (GP Credit): 3.5 3.0
Subject 3 (GP Credit): 4.0 1.5
CGPA: 3.80
```

## Gotchas
> [!warning] Zero Total Credits
> Entering 0 courses or 0 total credits triggers a floating-point division-by-zero, resulting in `NaN` or `inf`.

## My notes
> [!question]- My notes

## Related
- [[LAB 05 - cgpa]]
- [[ASG 04 - sort student by cgpa]]
