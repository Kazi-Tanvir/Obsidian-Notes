---
title: "ASG 05 - dictionary sort lexicographic"
aliases:
  - dictionary sort lexicographic
  - dictionary_sort_lexicographic
tags:
  - type/assignment
  - c/strings
  - c/searching
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "ASSIGNMENT/ASSIGNMENT_05/dictionary_sort_lexicographic.c"
number: 5
up: "[[ASG - Index]]"
prev: "[[ASG 04 - sort student by cgpa]]"
next: "[[ASG 06 - grading app]]"
related:
  - "[[CLASS 10 - string check equal]]"
  - "[[CLASS 14 - pointer strcmp]]"
created: 2026-10-29
status: draft
---
# ASG 05 - dictionary sort lexicographic

> [!abstract] Summary
> Compares two user-input strings lexicographically using `strcmp()` and computes the absolute difference between their cumulative ASCII character values.

**Source:** `ASSIGNMENT/ASSIGNMENT_05/dictionary_sort_lexicographic.c`

## Problem
Read two words from standard input, determine their alphabetical dictionary order using `strcmp`, and calculate the numerical difference between the sum of their ASCII character codes.

## Concepts used
- **Lexicographical Comparison (`strcmp`):** Comparing strings character-by-character based on ASCII values. Returns $< 0$ if word 1 precedes word 2, $> 0$ if word 2 precedes word 1, and $0$ if identical.
- **ASCII Code Accumulation:** Iterating over character bytes via `strlen()` and accumulating integer ASCII representations.
- **Alphabetical Sorting Output:** Ordering output strings so the alphabetically prior word appears first.

## Code
```c
#include<stdio.h>
#include<string.h>
#include<math.h>
int ASCII_value(char word[]){
    int value = 0;
    for (int i = 0; i < strlen(word); i++)  value += word[i] ;
    return value;
}
int main(){
    char word1[100] , word2[100];
    scanf("%s",word1);
    scanf("%s",word2);
    int result = strcmp(word1 , word2);
    if(result == 0) printf("\n%s\n%s\nThey are same word. \n",word1,word2);
    if (result < 0) printf("\n%s\n%s\n ",word1,word2);
    if(result > 0) printf("\n%s\n%s\n ",word2,word1);
    int num = fabs(ASCII_value(word1) - ASCII_value(word2));
    printf("\nASCII value Difference : %d",num);
    return 0;
}
```

## How it works
1. Defines `ASCII_value(char word[])` which sums character codes using a loop.
2. In `main()`, reads `word1` and `word2` via `scanf("%s")`.
3. Calls `strcmp(word1, word2)`:
   - If 0, prints that they are identical.
   - If negative, prints `word1` then `word2`.
   - If positive, prints `word2` then `word1`.
4. Calculates ASCII sums for both words and prints `|ASCII(word1) - ASCII(word2)|`.

## Sample run
```text
apple
banana

apple
banana
 
ASCII value Difference : 79
```

## Gotchas
> [!warning] Lexicographic Order vs ASCII Sum
> A word with a higher ASCII sum is not necessarily alphabetically later (e.g. short words starting with 'z' vs long words starting with 'a'). `strcmp` evaluates alphabetical prefix order, whereas `ASCII_value` computes length-weighted character sums.

## My notes
> [!question]- My notes

## Related
- [[CLASS 10 - string check equal]]
- [[CLASS 14 - pointer strcmp]]
