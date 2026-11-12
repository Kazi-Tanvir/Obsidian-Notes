---
title: "PRAC BOOK Ch07 - Index"
aliases:
  - C Book Chapter 7 Index
  - Chapter 7 Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/C_BOOK/CHAPTER_07/"
up: "[[PRAC - Index]]"
prev: "[[PRAC BOOK Ch06 - Index]]"
next: "[[PRAC BOOK Ch08 - Index]]"
created: 2026-10-29
status: draft
---
# PRAC BOOK Ch07 - Index

Chapter 7 focuses on function design and architecture: function prototypes, call-by-value vs. call-by-reference parameter passing, local and global variable scope, recursion, and command-line argument processing (`argc`, `argv`).

| File | What it teaches | Status |
|---|---|---|
| `01_RSC_1.c` | Conceptual review: What does this fragment do? int *p, i; p = &i; *p = 19; | Implemented |
| `02_RSC_2.c` | Conceptual review: What is generated when you use an array name without an index? | Implemented |
| `03_RSC_3.c` | Conceptual review: Is this fragment correct? char *p; p = "this is a string"; | Implemented |
| `04_RSC_4.c` | Assign float value using pointer | Implemented |
| `05_RSC_5.c` | Custom mystrlen() function | Implemented |
| `06_RSC_6.c` | Output of pointer expression | Implemented |
| `07_Example_711.c` | Prototype catching type mismatch errors | Implemented |
| `08_Example_712.c` | Function defined prior to main does not require separate prototype | Implemented |
| `09_Example_713.c` | Calling math library function sqrt() | Implemented |
| `10_Example_714.c` | Passing different numeric types promoted to match parameters | Implemented |
| `11_Example_715.c` | Function returning a pointer | Implemented |
| `12_Example_716.c` | Standard form of main() returning integer | Implemented |
| `13_Exercise_711.c` | Function avg() without prototype parameter list | Implemented |
| `14_Exercise_712.c` | Function avg() with full modern prototype | Implemented |
| `15_Exercise_713.c` | Conceptual review: Is the program correct? | Implemented |
| `16_Exercise_714.c` | Prototype for Purge() returning pointer to double | Implemented |
| `17_Exercise_715.c` | Experimenting with function prototypes and return types | Implemented |
| `18_Example_721.c` | Recursive function printing numbers 1 to 10 | Implemented |
| `19_Example_722.c` | Recursive factorial calculation | Implemented |
| `20_Example_723.c` | Mutually recursive functions f1 and f2 | Implemented |
| `21_Exercise_721.c` | Recursive factorial of 5 | Implemented |
| `22_Exercise_722.c` | Conceptual review: What is wrong with this recursive function? void f(void) { f(); } | Implemented |
| `23_Exercise_723.c` | Display string character by character recursively | Implemented |
| `24_Example_731.c` | Call by reference to modify callers arguments | Implemented |
| `25_Exercise_731.c` | Conceptual review: Is this program correct? void myfunc(int *p); int main(void) { int i; myfunc(i); ... } | Implemented |
| `26_Exercise_732.c` | Input function prompt() printing message and reading string | Implemented |
| `27_Exercise_733.c` | Conceptual review: Explain the difference between call by value and call by reference. | Implemented |
| `28_Example_741.c` | Printing command-line arguments argc and argv | Implemented |
| `29_Example_742.c` | Command-line ounces to pounds converter | Implemented |
| `30_Example_743.c` | Command-line password protection | Implemented |
| `31_Exercise_741.c` | Compare two command-line string arguments | Implemented |
| `32_Exercise_742.c` | Sum two command-line numeric arguments | Implemented |
| `33_Exercise_743.c` | Four-function command-line calculator | Implemented |
| `34_Example_751.c` | Traditional K&R function declaration syntax | Implemented |
| `35_Exercise_751.c` | Feet to meters using old-style declaration | Implemented |
| `36_MSC_1.c` | Conceptual review: How do you prototype a function that does not have parameters? | Implemented |
| `37_MSC_2.c` | Conceptual review: What is a function prototype, and what are the benefits it provides? | Implemented |
| `38_MSC_3.c` | Conceptual review: How do command-line arguments get passed to a C program? | Implemented |
| `39_MSC_4.c` | Recursive function printing alphabet A to Z | Implemented |
| `40_MSC_5.c` | Encode command-line string by adding 1 | Implemented |
| `41_MSC_6.c` | Prototype for myfunc(int x, int y, char ch) | Implemented |
| `42_MSC_7.c` | Old-style function declaration for myfunc | Implemented |
| `43_MSC_8.c` | Conceptual review: What does the exit() function do? | Implemented |
| `44_MSC_9.c` | atoi() function demonstration | Implemented |
| `45_CSC_1.c` | Command-line password check | Implemented |
| `46_CSC_2.c` | string_up() function converting string to uppercase | Implemented |
| `47_CSC_3.c` | avg() function averaging double array using pointers | Implemented |
| `48_CSC_4.c` | Conceptual review: Explain how pointers allow C to construct a call-by-reference parameter passing mechanism. | Implemented |

---

## 🧭 Navigation
- [[PRAC - Index]]
- [[PRAC BOOK Ch06 - Index]]
- [[PRAC BOOK Ch08 - Index]]
