---
title: "PRAC BOOK Ch10 - Index"
aliases:
  - C Book Chapter 10 Index
  - Chapter 10 Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/C_BOOK/CHAPTER_10/"
up: "[[PRAC - Index]]"
prev: "[[PRAC BOOK Ch09 - Index]]"
next: "[[PRAC BOOK Ch11 - Index]]"
created: 2026-10-29
status: draft
---
# PRAC BOOK Ch10 - Index

Chapter 10 covers user-defined composite data types: structures (`struct`), arrays of structures, nested structures, pointers to structures (`->`), parameter passing with structures, unions (`union`), bit-fields, and enumerations (`enum`).

| File | What it teaches | Status |
|---|---|---|
| `01_RSC_1.c` | File copy with command-line arguments | Implemented |
| `02_RSC_2.c` | Writing formatted data with fprintf() | Implemented |
| `03_RSC_3.c` | Initialize 20-element array and write to TEMP | Implemented |
| `04_RSC_4.c` | Read TEMP into array with fread() | Implemented |
| `05_RSC_5.c` | Conceptual review: What are stdin, stdout, and stderr? | Implemented |
| `06_RSC_6.c` | Conceptual review: How do functions like printf() and scanf() relate to the C file system? | Implemented |
| `07_Example_1011.c` | Basic structure definition and member access | Implemented |
| `08_Example_1012.c` | Using sizeof with structures | Implemented |
| `09_Example_1013.c` | Array of structures for card catalog | Implemented |
| `10_Example_1014.c` | Writing and reading structure array in single file operation | Implemented |
| `11_Example_1015.c` | Member names do not conflict with local variables | Implemented |
| `12_Example_1016.c` | Function returning a structure | Implemented |
| `13_Example_1017.c` | Passing structure to function by value | Implemented |
| `14_Exercise_1011.c` | Telephone directory using structure array | Implemented |
| `15_Exercise_1012.c` | Conceptual review: What is wrong with this fragment? struct s_type { int a; char ch; }; s_type.a = 10; | Implemented |
| `16_Exercise_1013.c` | Conceptual review: Examine header file STDIO.H and look at how the FILE structure is defined. | Implemented |
| `17_Example_1021.c` | Pointers to structures and the arrow operator | Implemented |
| `18_Example_1022.c` | Using structure pointers with time functions | Implemented |
| `19_Exercise_1021.c` | Conceptual review: Is this program fragment correct? struct s_type { int a; char ch; } *p; p.a = 100; | Implemented |
| `20_Exercise_1022.c` | Time and UTC time using gmtime() | Implemented |
| `21_Example_1031.c` | Nested structures in catalog program | Implemented |
| `22_Exercise_1031.c` | Telephone directory with nested address structure | Implemented |
| `23_Example_1041.c` | Bit-fields with unnamed spacer bits | Implemented |
| `24_Example_1042.c` | Simulation of flight recorder using bit-fields | Implemented |
| `25_Exercise_1041.c` | Structure with three bit-fields of size 3, 3, and 2 bits | Implemented |
| `26_Exercise_1042.c` | Conceptual review: How are bit-fields used when interfacing with hardware status registers? | Implemented |
| `27_Example_1051.c` | Swapping bytes of an integer using a union | Implemented |
| `28_Example_1052.c` | Binary display of character using union of char and bit-field struct | Implemented |
| `29_Exercise_1051.c` | Union of double and byte array to read/write double byte-by-byte | Implemented |
| `30_Exercise_1052.c` | Convert int into long using a union | Implemented |
| `31_MSC_1.c` | Conceptual review: In general terms what is a structure, and what is a union? | Implemented |
| `32_MSC_2.c` | Definition of struct s_type | Implemented |
| `33_MSC_3.c` | Conceptual review: What is wrong with this fragment? struct s_type { int a; char ch; } *p; p.a = 10; | Implemented |
| `34_MSC_4.c` | Array of employee structures written to file EMP | Implemented |
| `35_MSC_5.c` | Read and display records from EMP file | Implemented |
| `36_MSC_6.c` | Conceptual review: What is a bit-field? | Implemented |
| `37_MSC_7.c` | Display high- and low-order bytes of an integer using a union | Implemented |
| `38_CSC_1.c` | struct_swap() to swap contents of two structures | Implemented |
| `39_CSC_2.c` | File copy using union to hold fgetc() return value | Implemented |
| `40_CSC_3.c` | Conceptual review: What is wrong with this fragment? struct s_type { int a; int b: 2; int c: 6; } var; scanf("%d", &v... | Implemented |
| `41_CSC_4.c` | Enclosing array in struct to achieve call-by-value semantics | Implemented |

---

## 🧭 Navigation
- [[PRAC - Index]]
- [[PRAC BOOK Ch09 - Index]]
- [[PRAC BOOK Ch11 - Index]]
