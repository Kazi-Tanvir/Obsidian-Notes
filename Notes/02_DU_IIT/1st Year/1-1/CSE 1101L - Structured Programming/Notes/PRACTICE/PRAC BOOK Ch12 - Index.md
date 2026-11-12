---
title: "PRAC BOOK Ch12 - Index"
aliases:
  - C Book Chapter 12 Index
  - Chapter 12 Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/C_BOOK/CHAPTER_12/"
up: "[[PRAC - Index]]"
prev: "[[PRAC BOOK Ch11 - Index]]"
created: 2026-10-29
status: draft
---
# PRAC BOOK Ch12 - Index

Chapter 12 details the C preprocessor and advanced compiler controls: object-like and function-like macro definitions (`#define`), file inclusion (`#include`), conditional compilation (`#ifdef`, `#ifndef`, `#if`, `#elif`, `#else`, `#endif`), predefined macros, compiler directives (`#error`, `#pragma`), and variable-argument functions (`va_list`, `va_start`, `va_arg`, `va_end`).

| File | What it teaches | Status |
|---|---|---|
| `01_RSC_1.c` | Conceptual review: What is the major advantage gained when a variable is declared using register? | Implemented |
| `02_RSC_2.c` | Conceptual review: What is wrong with this function? void f(const int *i) { *i = 100; } | Implemented |
| `03_RSC_3.c` | Conceptual review: What is the outcome of these operations? | Implemented |
| `04_RSC_4.c` | Double and halve integer using shift operators | Implemented |
| `05_RSC_5.c` | How can these statements be written differently? | Implemented |
| `06_RSC_6.c` | Conceptual review: What is the extern type specifier for? | Implemented |
| `07_Example_1211.c` | Function-like parameterized macro MAX() | Implemented |
| `08_Example_1212.c` | Using quotes in #include directive | Implemented |
| `09_Example_1213.c` | Combining both forms of #include in a program | Implemented |
| `10_Exercise_1211.c` | Corrected RANGE macro with parentheses | Implemented |
| `11_Exercise_1212.c` | Parameterized macro ABS() to compute absolute value | Implemented |
| `12_Exercise_1213.c` | Verification of quote include syntax | Implemented |
| `13_Example_1221.c` | Conditional compilation using #if and #else | Implemented |
| `14_Example_1222.c` | Conditional compilation using #ifdef for debugging | Implemented |
| `15_Example_1223.c` | Conditional compilation using #ifndef | Implemented |
| `16_Example_1224.c` | Conditional compilation using #elif | Implemented |
| `17_Example_1225.c` | The defined preprocessor operator | Implemented |
| `18_Exercise_1221.c` | Conditional compilation selecting INT or FLOAT power routine | Implemented |
| `19_Exercise_1222.c` | Conceptual review: Is this fragment correct? If not, show one way to fix it: #if MAX < 10 / * ... * / #else MAX > 10 ... | Implemented |
| `20_Example_1231.c` | Conceptual review: What does the #error directive do? | Implemented |
| `21_Example_1232.c` | Demonstrating the #undef directive | Implemented |
| `22_Example_1233.c` | Demonstrating the #line directive | Implemented |
| `23_Example_1234.c` | Conceptual review: Check your compiler's user manual and learn about any #pragma directives supported by your system. | Implemented |
| `24_Exercise_1231.c` | Verifying #undef and #line directives | Implemented |
| `25_Example_1241.c` | Built-in macros __LINE__, __FILE__, __DATE__, __TIME__, __STDC__ | Implemented |
| `26_Example_1242.c` | Using __LINE__ and __FILE__ with #line reset | Implemented |
| `27_Exercise_1241.c` | Displaying compilation environment using built-in macros | Implemented |
| `28_Example_1251.c` | The # stringize operator | Implemented |
| `29_Example_1252.c` | The ## token concatenation operator | Implemented |
| `30_Exercise_1251.c` | Running # and ## operator examples | Implemented |
| `31_Exercise_1252.c` | Output of token-pasting program | Implemented |
| `32_Exercise_1253.c` | Macro generating variable names and debug prints | Implemented |
| `33_Example_1261.c` | Calling a function using a function pointer | Implemented |
| `34_Example_1262.c` | Array of function pointers for arithmetic operations | Implemented |
| `35_Example_1263.c` | Generic array sorting with qsort() | Implemented |
| `36_Exercise_1261.c` | Experimenting with function pointers | Implemented |
| `37_Exercise_1262.c` | Searching a sorted array with bsearch() | Implemented |
| `38_Exercise_1263.c` | Function pointer array with modulus() operation | Implemented |
| `39_Example_1271.c` | Checking return value of malloc() | Implemented |
| `40_Example_1272.c` | Dynamically allocated character array | Implemented |
| `41_Example_1273.c` | Estimating free memory using malloc() | Implemented |
| `42_Example_1274.c` | Using dynamic allocation for file I/O buffer | Implemented |
| `43_Example_1275.c` | Conceptual review: What is wrong with this fragment? p = malloc(10); for (i = 0; i < 100; i++) p[i] = i; | Implemented |
| `44_Exercise_1271.c` | Compiling dynamic allocation test | Implemented |
| `45_Exercise_1272.c` | Ten-element dynamic integer array | Implemented |
| `46_Exercise_1273.c` | Conceptual review: What is wrong with this fragment? char *p; *p = malloc(10); gets(p); | Implemented |
| `47_MSC_1.c` | Conceptual review: What is the difference between using quotes and angle brackets with #include? | Implemented |
| `48_MSC_2.c` | Conditionally compile fragment with #ifdef DEBUG | Implemented |
| `49_MSC_3.c` | Conditionally compile when DEBUG == 1 | Implemented |
| `50_MSC_4.c` | Conceptual review: How do you undefine a macro? | Implemented |
| `51_MSC_5.c` | Conceptual review: What is __FILE__ and what does it represent? | Implemented |
| `52_MSC_6.c` | Conceptual review: What do the # and ## preprocessor operators do? | Implemented |
| `53_MSC_7.c` | Sort string using qsort() | Implemented |
| `54_MSC_8.c` | Dynamically allocate memory for one double | Implemented |
| `55_CSC_1.c` | Card catalog using dynamic allocation for each book | Implemented |
| `56_CSC_2.c` | Macro equivalent of code_it() function | Implemented |
| `57_CSC_3.c` | - Use conditional compilation for debugging and platform adaptation. | Implemented |
| `58_CSC_4.c` | Study Exercise: Standard C Library exploration. | Implemented |
| `59_CSC_5.c` | Synthesis Review: Retrospective review of the C programming language. | Implemented |
| `60_CSC_6.c` | Practice Principle: C is a language best learned by active programming and reading real-world code. | Implemented |
| `61_CSC_7.c` | Conclusion: Foundation complete. You have mastered C fundamentals, program control, data types, arrays, pointers, fun... | Implemented |

---

## 🧭 Navigation
- [[PRAC - Index]]
- [[PRAC BOOK Ch11 - Index]]
