---
title: "PRAC BOOK Ch11 - Index"
aliases:
  - C Book Chapter 11 Index
  - Chapter 11 Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/C_BOOK/CHAPTER_11/"
up: "[[PRAC - Index]]"
prev: "[[PRAC BOOK Ch10 - Index]]"
next: "[[PRAC BOOK Ch12 - Index]]"
created: 2026-10-29
status: draft
---
# PRAC BOOK Ch11 - Index

Chapter 11 covers advanced data types and operators: compile-time type sizing with `sizeof()`, user-defined type aliases with `typedef`, bitwise logical and shift operators (`&`, `|`, `^`, `~`, `>>`, `<<`), and the ternary conditional operator (`? :`).

| File | What it teaches | Status |
|---|---|---|
| `01_RSC_1.c` | Array of structures holding squares and cubes | Implemented |
| `02_RSC_2.c` | Union to display individual bytes of double | Implemented |
| `03_RSC_3.c` | Conceptual review: What does this fragment display? (Assume two-byte ints and eight-byte doubles) union u_type { int ... | Implemented |
| `04_RSC_4.c` | Conceptual review: What is wrong with this fragment? struct s_type { int a; double b; } s; s = 10; | Implemented |
| `05_RSC_5.c` | Conceptual review: What is a bit-field? | Implemented |
| `06_Example_1111.c` | Timing register vs non-register loop using clock() | Implemented |
| `07_Example_1112.c` | Register variables in separate functions | Implemented |
| `08_Example_1113.c` | Static local variable for one-time initialization | Implemented |
| `09_Example_1114.c` | Static local variable controlling recursive function | Implemented |
| `10_Example_1115.c` | Using extern declaration for global data | Implemented |
| `11_Exercise_1111.c` | Conceptual review: Which two variables are the best ones to be made into register variables in the nested loop? | Implemented |
| `12_Exercise_1112.c` | sum_it() maintains running total using local static variable | Implemented |
| `13_Exercise_1113.c` | Demonstrating extern linkage in single compilation unit | Implemented |
| `14_Exercise_1114.c` | Conceptual review: What is wrong with this fragment? register int i; int *p; p = &i; | Implemented |
| `15_Example_1121.c` | const variable declaration and usage | Implemented |
| `16_Example_1122.c` | Pointer parameter declared as const char *p | Implemented |
| `17_Example_1123.c` | Conceptual review: Why does assigning through a const pointer parameter produce a compiler error? | Implemented |
| `18_Example_1124.c` | volatile variable declaration | Implemented |
| `19_Exercise_1121.c` | const version control string | Implemented |
| `20_Exercise_1122.c` | Custom mystrcpy() with const source pointer | Implemented |
| `21_Exercise_1123.c` | Conceptual review: What are practical uses of volatile? | Implemented |
| `22_Example_1131.c` | Defining and using enumerations | Implemented |
| `23_Example_1132.c` | Displaying string representation of enumeration | Implemented |
| `24_Example_1133.c` | Enumeration constants with assigned integer values | Implemented |
| `25_Exercise_1131.c` | Running enumeration test program | Implemented |
| `26_Exercise_1132.c` | Enumeration of coins of the U.S. | Implemented |
| `27_Exercise_1133.c` | Conceptual review: Is this fragment correct? If not, why not? enum color {red, green, blue} c; c = red; printf("%s", c); | Implemented |
| `28_Example_1141.c` | typedef defining new type names based on existing ones | Implemented |
| `29_Example_1142.c` | typedef with structures | Implemented |
| `30_Exercise_1141.c` | typedef UL for unsigned long | Implemented |
| `31_Exercise_1142.c` | Conceptual review: What is wrong with this fragment? typedef new_type int; | Implemented |
| `32_Example_1151.c` | Bitwise XOR operation | Implemented |
| `33_Example_1152.c` | Bitwise AND to display binary representation of byte | Implemented |
| `34_Example_1153.c` | Bitwise OR to set bits | Implemented |
| `35_Example_1154.c` | Bitwise AND to determine odd or even | Implemented |
| `36_Example_1155.c` | 1's complement operator ~ | Implemented |
| `37_Exercise_1151.c` | File encoding using 1's complement operator ~ | Implemented |
| `38_Exercise_1152.c` | File encryption using 8-character key with XOR | Implemented |
| `39_Exercise_1153.c` | Conceptual review: What is the outcome of these operations? | Implemented |
| `40_Exercise_1154.c` | Check and clear parity bit (8th bit) | Implemented |
| `41_Example_1161.c` | Right and left shift operators | Implemented |
| `42_Example_1162.c` | Multiplication and division by 2 via bit shifts | Implemented |
| `43_Exercise_1161.c` | Multiply and divide numbers using shift operators | Implemented |
| `44_Exercise_1162.c` | Circular bit rotate function | Implemented |
| `45_Example_1171.c` | Demonstrating the ? ternary operator | Implemented |
| `46_Example_1172.c` | Computerized coin toss using ternary operator | Implemented |
| `47_Exercise_1171.c` | Preventing division by zero using ? operator | Implemented |
| `48_Exercise_1172.c` | Conceptual review: Convert the following statement into its equivalent ? statement: if (a > b) count = 100; else coun... | Implemented |
| `49_Example_1181.c` | Multiple assignment statement | Implemented |
| `50_Example_1182.c` | Compound arithmetic assignment operators | Implemented |
| `51_Example_1183.c` | Compound shift assignment operator <<= | Implemented |
| `52_Exercise_1181.c` | Proving multiple assignment assigns all variables | Implemented |
| `53_Exercise_1182.c` | Conceptual review: How is the statement x = x & y written using C shorthand? | Implemented |
| `54_Exercise_1183.c` | Even multiples of 17 from 17 to 1000 | Implemented |
| `55_Example_1191.c` | Comma operator in for loop | Implemented |
| `56_Example_1192.c` | Comma operator in expression | Implemented |
| `57_Exercise_1191.c` | Comma operator maintaining three loop variables | Implemented |
| `58_Exercise_1192.c` | Conceptual review: What is the value of i after the following statement executes? i = (j = 1, k = 2, j + k); | Implemented |
| `59_MSC_1.c` | Conceptual review: What does the register specifier do? | Implemented |
| `60_MSC_2.c` | Conceptual review: What do the const and volatile modifiers do? | Implemented |
| `61_MSC_3.c` | Sum numbers 1 to 100 with register variables | Implemented |
| `62_MSC_4.c` | Conceptual review: Is this statement valid? If so, what does it do? count += 2; | Implemented |
| `63_MSC_5.c` | Compare corresponding bits of two characters using XOR | Implemented |
| `64_MSC_6.c` | Conceptual review: What do the << and >> operators do? | Implemented |
| `65_MSC_7.c` | Conceptual review: Show how this statement can be rewritten: a = a ^ b; | Implemented |
| `66_MSC_8.c` | Conceptual review: Rewrite this statement using the ? operator: if (c == 0) printf("is zero"); else printf("is not ze... | Implemented |
| `67_MSC_9.c` | Enumeration of planets | Implemented |
| `68_CSC_1.c` | Swap low-order and high-order nibbles of a byte | Implemented |
| `69_CSC_2.c` | Decode and display 1's complement encoded file | Implemented |
| `70_CSC_3.c` | Conceptual review: Is this fragment correct? register FILE *fp; | Implemented |
| `71_CSC_4.c` | Optimized telephone directory using register variables | Implemented |

---

## 🧭 Navigation
- [[PRAC - Index]]
- [[PRAC BOOK Ch10 - Index]]
- [[PRAC BOOK Ch12 - Index]]
