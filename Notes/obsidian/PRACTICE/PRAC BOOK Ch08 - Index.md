---
title: "PRAC BOOK Ch08 - Index"
aliases:
  - C Book Chapter 8 Index
  - Chapter 8 Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/C_BOOK/CHAPTER_08/"
up: "[[PRAC - Index]]"
prev: "[[PRAC BOOK Ch07 - Index]]"
next: "[[PRAC BOOK Ch09 - Index]]"
created: 2026-10-29
status: draft
---
# PRAC BOOK Ch08 - Index

Chapter 8 explores console input and output: unbuffered and buffered character I/O (`getchar`, `putchar`, `getche`, `getch`), line I/O (`gets`, `puts`), and advanced format specifiers and modifiers for `printf()` and `scanf()`.

| File | What it teaches | Status |
|---|---|---|
| `01_RSC_1.c` | Conceptual review: What must you do to enable the compiler to check that a function is being called correctly? | Implemented |
| `02_RSC_2.c` | Conceptual review: What are the principal advantages of using function prototypes? | Implemented |
| `03_RSC_3.c` | hypot() function using math library | Implemented |
| `04_RSC_4.c` | Conceptual review: What return type should you use for a function that returns no value? | Implemented |
| `05_RSC_5.c` | Recursive string length function rstrlen() | Implemented |
| `06_RSC_6.c` | Reports argument count and last argument | Implemented |
| `07_RSC_7.c` | Conceptual review: How is this declaration coded using the old-style function declaration? float func(int a, char ch,... | Implemented |
| `08_Example_811.c` | Macro name in place of a quoted string | Implemented |
| `09_Example_812.c` | Defining macros in terms of other macros | Implemented |
| `10_Example_813.c` | Macro name inside a quoted string is not replaced | Implemented |
| `11_Exercise_811.c` | Count from 0 to MAX-1 by COUNTBY | Implemented |
| `12_Exercise_812.c` | Conceptual review: Is this fragment correct? #define MAX MIN+100 #define MIN 10 | Implemented |
| `13_Exercise_813.c` | Conceptual review: Is this fragment correct? #define STR this is a test printf(STR); | Implemented |
| `14_Exercise_814.c` | Macro defining header name | Implemented |
| `15_Example_821.c` | Line-buffered character input with getchar() | Implemented |
| `16_Example_822.c` | Using backslash escape sequences with putchar() | Implemented |
| `17_Exercise_821.c` | getchar() and putchar() with error checking for EOF | Implemented |
| `18_Exercise_822.c` | Conceptual review: What is wrong with this fragment? char str[80] = "this is a test"; putchar(str); | Implemented |
| `19_Example_831.c` | Interactive keyboard input using getch() and cprintf() | Implemented |
| `20_Example_832.c` | Sales-tax table with keyboard interrupt check using kbhit() | Implemented |
| `21_Exercise_831.c` | Displays ASCII code of each typed key without echoing character | Implemented |
| `22_Exercise_832.c` | Prints periods continuously until a key is pressed | Implemented |
| `23_Example_841.c` | Checking return value of gets() | Implemented |
| `24_Example_842.c` | Calling gets() directly inside if condition | Implemented |
| `25_Example_843.c` | Conceptual review: Why does calling gets(p) with an uninitialized pointer cause program failure? | Implemented |
| `26_Example_844.c` | Outputting lines of text using puts() | Implemented |
| `27_Exercise_841.c` | Comparing puts() vs printf() output | Implemented |
| `28_Exercise_842.c` | Conceptual review: Is this program correct? If not, why not? #include <stdio.h> int main(void) { char *p, *q; printf(... | Implemented |
| `29_Example_851.c` | Precision specifier with printf() | Implemented |
| `30_Example_852.c` | Minimum field width for column alignment | Implemented |
| `31_Example_853.c` | Printing integers in dec, oct, hex and floats in scientific notation | Implemented |
| `32_Example_854.c` | Demonstrating the %n specifier in printf() | Implemented |
| `33_Exercise_851.c` | Table of numbers, squares, and cubes left-justified | Implemented |
| `34_Exercise_852.c` | Outputting a percent sign using %% in printf() | Implemented |
| `35_Exercise_853.c` | Displaying 1023.03 with two decimal places | Implemented |
| `36_Example_861.c` | %s stops at first whitespace in scanf() | Implemented |
| `37_Example_862.c` | Scanset reading upper and lowercase letters | Implemented |
| `38_Example_863.c` | Scanset reading letters and spaces | Implemented |
| `39_Example_864.c` | Arithmetic calculator reading operation with scanf() | Implemented |
| `40_Example_865.c` | Maximum field width specifier in scanf() | Implemented |
| `41_Example_866.c` | Matching non-whitespace characters in format string | Implemented |
| `42_Exercise_861.c` | Input first, middle, and last names with field limit | Implemented |
| `43_Exercise_862.c` | Read floating-point number as string using scanset | Implemented |
| `44_Exercise_863.c` | Conceptual review: Is this fragment correct? If not why not? char ch; scanf("%2c", &ch); | Implemented |
| `45_Exercise_864.c` | Input string, double, int, and count characters read using %n | Implemented |
| `46_Exercise_865.c` | Convert hexadecimal input to decimal and octal | Implemented |
| `47_MSC_1.c` | Conceptual review: What is the difference between getchar(), getche(), and getch()? | Implemented |
| `48_MSC_2.c` | Conceptual review: What is the difference between the %e and the %E printf() format specifiers? | Implemented |
| `49_MSC_3.c` | Conceptual review: What is a scanset? | Implemented |
| `50_MSC_4.c` | Input first name, birth date, and phone number | Implemented |
| `51_MSC_5.c` | Conceptual review: What is one advantage to using puts() over printf() when you only need to output a string? What is... | Implemented |
| `52_MSC_6.c` | Macro COUNT as 100, display 0 to 99 | Implemented |
| `53_MSC_7.c` | Conceptual review: What is EOF, and where is it defined? | Implemented |
| `54_CSC_1.c` | Little league batting averages | Implemented |
| `55_CSC_2.c` | Electronic library card catalog | Implemented |

---

## 🧭 Navigation
- [[PRAC - Index]]
- [[PRAC BOOK Ch07 - Index]]
- [[PRAC BOOK Ch09 - Index]]
