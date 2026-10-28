---
title: "CLASS - Index"
aliases:
  - Class Index
  - Lecture Notes Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
up: "[[00 - Index]]"
next: "[[LAB - Index]]"
created: 2026-10-29
status: draft
---
# CLASS - Index

The `CLASS/` directory contains 28 lecture programs demonstrating the core curriculum of CSE 1101. The progression covers fundamental arithmetic logic, iterative loops, array structures, C-string mechanics, raw pointer manipulation and pointer arithmetic, formatted and binary file streams, composite structures, bitfields, and stream cipher encryption.

| # | Note | What it teaches | Tags |
|---|---|---|---|
| 01 | [[CLASS 01 - calculator]] | Arithmetic functions, `if-else if` branching, division by zero guard | `c/functions`, `c/control-flow`, `level/basic` |
| 02 | [[CLASS 02 - grade]] | Grade evaluation, multi-branch conditional ladders, boundary tests | `c/control-flow`, `c/math`, `level/basic` |
| 03 | [[CLASS 03 - number game]] | While loops, counter decrement, state comparison, feedback hints | `c/game-logic`, `c/loops`, `level/basic` |
| 04 | [[CLASS 04 - prime number]] | Primality testing, trial division up to $n/2$, early loop break | `c/math`, `c/loops`, `level/basic` |
| 05 | [[CLASS 05 - vowel switch]] | Character evaluation, `switch-case` multi-case fallthrough, `default` branch | `c/control-flow`, `c/strings`, `level/basic` |
| 06 | [[CLASS 06 - calc menu switch]] | Menu-driven loop, procedural decomposition, switch-case dispatch | `c/control-flow`, `c/functions`, `level/basic` |
| 07 | [[CLASS 07 - avg temperature array]] | 1D fixed-size array indexing, accumulator pattern, integer division truncation | `c/arrays`, `c/loops`, `level/basic` |
| 08 | [[CLASS 08 - string length]] | Manual string length counter, null terminator `\0` detection vs `strlen` | `c/strings`, `c/loops`, `level/basic` |
| 09 | [[CLASS 09 - string copy]] | Byte-by-byte string copy loop, explicit destination null-termination vs `strcpy` | `c/strings`, `c/arrays`, `level/basic` |
| 10 | [[CLASS 10 - string check equal]] | Element-by-element string equality verification, mismatch detection vs `strcmp` | `c/strings`, `c/arrays`, `level/basic` |
| 11 | [[CLASS 11 - string merge]] | String concatenation, locating destination null terminator, buffer sizing | `c/strings`, `c/arrays`, `level/basic` |
| 12 | [[CLASS 12 - pointer strlen]] | Pointer dereference `*str`, post-increment `*(str++)`, compact string traversal | `c/pointers`, `c/pointer-arithmetic`, `level/intermediate` |
| 13 | [[CLASS 13 - pointer strcpy]] | Pointer idiom `*dest++ = *src++`, copy traversal, parameter order gotcha | `c/pointers`, `c/pointer-arithmetic`, `level/intermediate` |
| 14 | [[CLASS 14 - pointer strcmp]] | Pointer-based lexicographical string comparison, char dereference gotchas | `c/pointers`, `c/pointer-arithmetic`, `level/intermediate` |
| 15 | [[CLASS 15 - pointer strcat]] | Offset pointer arithmetic `*(x + i)`, string concatenation, buffer overflow gotcha | `c/pointers`, `c/pointer-arithmetic`, `level/intermediate` |
| 16 | [[CLASS 16 - pointer min max]] | Pointer array scanning (Template stub in repo, see Concept-Wise 02) | `c/pointers`, `c/arrays`, `level/intermediate` |
| 17 | [[CLASS 17 - pointer string reverse]] | In-place two-pointer string reversal, symmetric indexing $s[i] \leftrightarrow s[n-1-i]$ | `c/pointers`, `c/pointer-arithmetic`, `level/intermediate` |
| 18 | [[CLASS 18 - pointer books 2d arr]] | Array of pointers `char *book[20]`, dynamic allocation necessity gotcha | `c/pointers`, `c/arrays`, `level/intermediate` |
| 19 | [[CLASS 19 - pointer row sum]] | 2D array row-major memory layout, array name decay vs lvalue gotchas | `c/pointers`, `c/arrays`, `level/intermediate` |
| 20 | [[CLASS 20 - cmd arg]] | Command-line argument vector `argc`, `argv[]`, string token parsing | `c/cli-args`, `c/strings`, `level/basic` |
| 21 | [[CLASS 21 - file basic]] | Comprehensive stream guide: formatted, character, line, binary block I/O, positioning | `c/file-io`, `c/binary-io`, `level/intermediate` |
| 22 | [[CLASS 22 - space finder]] | Character stream scanning with `fgetc`, whitespace token counting, EOF handling | `c/file-io`, `c/strings`, `level/intermediate` |
| 23 | [[CLASS 23 - mid word]] | Text stream word tokenization, stream boundary detection, locating median word | `c/file-io`, `c/searching`, `level/intermediate` |
| 24 | [[CLASS 24 - take cg file]] | Reading structured records into parallel arrays with `fscanf`, path gotchas | `c/file-io`, `c/arrays`, `level/intermediate` |
| 25 | [[CLASS 25 - file sort cg]] | Indirect index sorting (`merit[i]`), preserving original data, formatted reporting | `c/file-io`, `c/sorting`, `level/intermediate` |
| 26 | [[CLASS 26 - struct student info]] | Heterogeneous records with `struct Student`, memory alignment, array of structs | `c/structs`, `c/file-io`, `level/intermediate` |
| 27 | [[CLASS 27 - binary encryption]] | Bitfield union `union Data`, 1-bit struct fields, circular 8-bit stream cipher | `c/bit-manipulation`, `c/encryption`, `level/advanced` |
| 28 | [[CLASS 28 - shift encryption]] | Command-line driven Caesar shift cipher, modular character offset mapping | `c/encryption`, `c/cli-args`, `level/intermediate` |

---

## ?? Progression & Architectural Themes

1. **Foundations (01 to 06):** Focuses on basic procedural mechanics: reading numbers from standard input, using branching ladders (`if-else`) and multi-case fallthrough (`switch`), and decomposing problems into pure functions.
2. **Sequential Memory (07 to 11):** Transitions from scalar values to contiguous blocks of memory. Arrays and strings teach the fundamental invariant of C strings: **the null terminator (`\0`)**.
3. **Pointers & Memory Addressing (12 to 20):** Direct interaction with system memory. Notes 12?15 rewrite the standard string library using pointers and pointer arithmetic (`*dest++ = *src++`). Notes 18?19 demystify 2D arrays, pointer arrays, and decay rules.
4. **Persistent Streams & Formatting (21 to 25):** File I/O transitions programs from transient memory to persistent disk storage. Note 21 serves as the master reference for all standard C I/O modes (`fprintf`, `fscanf`, `fgets`, `fgetc`, `fread`, `fwrite`, `fseek`). Notes 24 and 25 explore data management and indirect index sorting.
5. **Composed Types & Bit Manipulation (26 to 28):** Real-world data representation: grouping heterogeneous attributes into user-defined `struct` types (Note 26), bare-metal bitfield rotation via `union` (Note 27), and stream cryptography (Note 28).

---

## ?? Navigation
- [[00 - Index]]
- [[LAB - Index]]
- [[ASG - Index]]
- [[PROJ - Index]]
- [[PRAC - Index]]
- [[BUET - Index]]
- [[ARCH - Index]]
- [[Tag Glossary]]
