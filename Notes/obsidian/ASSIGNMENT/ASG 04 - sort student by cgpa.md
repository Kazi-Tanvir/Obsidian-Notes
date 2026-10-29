---
title: "ASG 04 - sort student by cgpa"
aliases:
  - sort student by cgpa
  - sort_student_by_cgpa
tags:
  - type/assignment
  - c/arrays
  - c/sorting
  - c/functions
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "ASSIGNMENT/ASSIGNMENT_04/sort_student_by_cgpa.c"
number: 4
up: "[[ASG - Index]]"
prev: "[[ASG 03 - hollow box and butterfly]]"
next: "[[ASG 05 - dictionary sort lexicographic]]"
related:
  - "[[CLASS 25 - file sort cg]]"
  - "[[LAB 05 - cgpa]]"
  - "[[ASG 06 - grading app]]"
created: 2026-10-29
status: draft
---
# ASG 04 - sort student by cgpa

> [!abstract] Summary
> Computes credit-weighted university CGPA across 7 academic courses for 5 students, tracks student roll numbers, and produces a sorted merit list in descending order.

**Source:** `ASSIGNMENT/ASSIGNMENT_04/sort_student_by_cgpa.c`

## Problem
Calculate the semester CGPA for 5 students across 7 course marks according to university credit weightings (6 theory courses $\times$ 3.0 credits + 1 lab course $\times$ 1.5 credits = 19.5 total credits), and rank students by merit.

## Concepts used
- **Credit-Weighted Accumulation:** Multiplying grade points by course credits: theory courses receive $3.0$ credits while lab course (index 6) receives $1.5$ credits, dividing by total credits ($19.5$).
- **Parallel Array Tracking:** Maintaining `student[5]` for floating-point GPAs and `roll[5]` for student ID numbers.
- **Dual Bubble/Selection Exchange:** Swapping `student[i]` with `student[j]` and simultaneously swapping `roll[i]` with `roll[j]` to preserve ID-score alignment.

## Code
```c
#include <stdio.h>

float checkCGPA(int marks)
{
    if (marks >= 80 && marks <= 100)  return 4.0;
    if (marks >= 75)  return 3.75;
    if (marks >= 70)  return 3.5;
    if (marks >= 65)  return 3.25;
    if (marks >= 60)  return 3.0;
    if (marks >= 55)  return 2.75;
    if (marks >= 50)  return 2.5;
    if (marks >= 45)  return 2.25;
    if (marks >= 40)  return 2.0;
    else return 0;
}

float countCGPA(int idx){
    int sub[7]; float sum = 0;
    printf("enter Your Marks : (Format is 110X) \n");
    for (int i = 0; i < 7; i++) scanf("%d", &sub[i]);
    for (int i = 0; i < 7; i++) {
        if (i < 6) sum += checkCGPA(sub[i]) * 3;
        else sum += checkCGPA(sub[i]) * 1.5;
    }
    float grade = sum / 19.5;
    printf("Grade of student %d is %.2f\n", idx + 1, grade);
    return grade;
}

int main(){
    float student[5];
    int roll[5];
    for(int i = 0; i < 5; i++){
        printf("Enter the marks of student %d: \n", i + 1);
        student[i] = countCGPA(i);
        roll[i] = i + 1;
    }
    for(int i = 0 ; i < 5 ; i++){
        for(int j = i + 1 ; j < 5 ; j++){
            if(student[i] < student[j]){
                float temp = student[i];
                student[i] = student[j];
                student[j] = temp;
                int t = roll[i];
                roll[i] = roll[j];
                roll[j] = t;
            }
        }
    }
    printf("Merit List: \n");
    for(int i = 0; i < 5; i++) printf("Merit %d: Roll %d (CGPA: %.2f)\n", i + 1, roll[i], student[i]);
    return 0;
}
```

## How it works
1. `checkCGPA(marks)` converts numeric raw marks ($0 \dots 100$) to standard grade points ($4.0, 3.75, \dots, 2.0, 0.0$).
2. `countCGPA(idx)` reads 7 subject marks for student `idx`, sums weighted points ($3.0 	imes 	ext{GP}$ for indices $0 \dots 5$ and $1.5 	imes 	ext{GP}$ for index 6), divides by $19.5$, and returns the resulting GPA.
3. In `main()`, iterates for 5 students, storing GPAs into `student[i]` and assigning 1-based roll numbers `roll[i] = i + 1`.
4. Executes nested comparison loops: if `student[i] < student[j]`, swaps both the GPA values and the corresponding roll numbers.
5. Prints the ranked Merit List.

## Sample run
```text
Enter the marks of student 1: 
enter Your Marks : (Format is 110X) 
Grade of student 1 is 3.10
Enter the marks of student 2: 
enter Your Marks : (Format is 110X) 
Grade of student 2 is 3.08
Enter the marks of student 3: 
enter Your Marks : (Format is 110X) 
Grade of student 3 is 3.17
Enter the marks of student 4: 
enter Your Marks : (Format is 110X) 
Grade of student 4 is 2.67
Enter the marks of student 5: 
enter Your Marks : (Format is 110X) 
Grade of student 5 is 3.13
Merit List: 
Merit 1: Roll 3 (CGPA: 3.17)
Merit 2: Roll 5 (CGPA: 3.13)
Merit 3: Roll 1 (CGPA: 3.10)
Merit 4: Roll 2 (CGPA: 3.08)
Merit 5: Roll 4 (CGPA: 2.67)
```

## Gotchas
> [!warning] Desynchronization in Parallel Arrays
> When sorting parallel arrays (`student` and `roll`), failing to swap `roll[i]` alongside `student[i]` will attribute the highest grades to the wrong students. Using a `struct` avoids this pitfall.

## My notes
> [!question]- My notes

## Related
- [[CLASS 25 - file sort cg]]
- [[LAB 05 - cgpa]]
- [[ASG 06 - grading app]]
