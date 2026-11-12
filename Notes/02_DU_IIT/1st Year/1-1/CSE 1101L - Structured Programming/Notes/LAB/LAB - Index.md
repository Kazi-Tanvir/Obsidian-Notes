---
title: "LAB - Index"
aliases:
  - Lab Index
  - Lab Experiments Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
up: "[[00 - Index]]"
prev: "[[CLASS - Index]]"
next: "[[ASG - Index]]"
created: 2026-10-29
status: draft
---
# LAB - Index

The `LAB/` directory contains 30 hands-on structured laboratory experiments. The curriculum systematically advances from fundamental variable manipulation, date arithmetic, and currency decomposition through sorting algorithms, divide-and-conquer recursion, pointer-based data transformations, real-world CSV dataset parsing (the Titanic disaster), 24-bit binary BMP image manipulation, and file-backed interactive database systems.

| # | Note | What it teaches | Tags |
|---|---|---|---|
| 01 | [[LAB 01 - change var temp]] | Variable swapping using an auxiliary temporary storage variable | `c/functions`, `c/math`, `level/basic` |
| 02 | [[LAB 02 - change var no temp]] | Arithmetic variable swapping without third variables ($a = a+b, b=a-b, a=a-b$) | `c/math`, `c/functions`, `level/basic` |
| 03 | [[LAB 03 - age calc simple]] | Calendar date arithmetic, borrowing days/months, leap-year approximations | `c/control-flow`, `c/math`, `level/basic` |
| 04 | [[LAB 04 - change calc simplified]] | Greedy cash change distribution across currency denominations (1000 down to 1) | `c/math`, `c/control-flow`, `level/basic` |
| 05 | [[LAB 05 - cgpa]] | Weighted credit average calculation, array accumulation, GPA bounds | `c/arrays`, `c/loops`, `level/basic` |
| 06 | [[LAB 06 - discount]] | Tiered discount thresholds and loyalty point accumulation logic | `c/control-flow`, `c/math`, `level/basic` |
| 07 | [[LAB 07 - hollow triangle]] | Nested loop coordinate boundary conditions for hollow star patterns | `c/loops`, `c/control-flow`, `level/basic` |
| 08 | [[LAB 08 - pascal]] | Pascal's triangle generation using combinations / multiplicative recurrence | `c/loops`, `c/math`, `level/basic` |
| 09 | [[LAB 09 - password]] | Interactive credential validation, masked string comparison, retry loops | `c/loops`, `c/strings`, `level/basic` |
| 10 | [[LAB 10 - discount budget]] | Dynamic shopping budget calculations with conditional discount scaling | `c/loops`, `c/math`, `level/basic` |
| 11 | [[LAB 11 - sort array]] | Selection Sort descending, finding extrema (min/max) in a single pass | `c/sorting`, `c/arrays`, `level/basic` |
| 12 | [[LAB 12 - swap array]] | In-place element exchange between arrays at specified indices | `c/arrays`, `c/loops`, `level/basic` |
| 13 | [[LAB 13 - remove item]] | Element deletion by left-shifting array elements to preserve order | `c/arrays`, `c/searching`, `level/basic` |
| 14 | [[LAB 14 - merge array]] | Merging two sorted arrays into a unified sorted array in linear time | `c/arrays`, `c/sorting`, `level/basic` |
| 15 | [[LAB 15 - sum array recursion]] | Recursive array summation, base cases, and call-stack unwinding | `c/recursion`, `c/arrays`, `level/basic` |
| 16 | [[LAB 16 - reverse array recursion]] | In-place recursive two-pointer array reversal | `c/recursion`, `c/arrays`, `level/basic` |
| 17 | [[LAB 17 - merge sort recursion]] | Divide-and-conquer recursive Merge Sort ($O(n \log n)$) | `c/recursion`, `c/sorting`, `level/intermediate` |
| 18 | [[LAB 18 - pointer sort]] | Selection Sort implemented via direct pointer addressing and offsets | `c/pointers`, `c/sorting`, `level/intermediate` |
| 19 | [[LAB 19 - pointer swap]] | Dynamic array allocation (`malloc`) and pointer value substitution | `c/pointers`, `c/functions`, `level/basic` |
| 20 | [[LAB 20 - pointer remove]] | Deleting elements from arrays using pointer shifts and dereferencing | `c/pointers`, `c/arrays`, `level/intermediate` |
| 21 | [[LAB 21 - pointer merge]] | Merging strings/arrays using pointer offsets and dynamic buffers | `c/pointers`, `c/arrays`, `level/intermediate` |
| 22 | [[LAB 22 - pointer recursion array sum]] | Recursive array summation expressed entirely through pointer arithmetic | `c/pointers`, `c/recursion`, `level/intermediate` |
| 23 | [[LAB 23 - pointer array reverse]] | Recursive two-pointer array inversion using raw memory pointers | `c/pointers`, `c/recursion`, `level/intermediate` |
| 24 | [[LAB 24 - merge sort]] | Complete recursive Merge Sort with dynamic temporary merge buffers | `c/sorting`, `c/pointers`, `level/intermediate` |
| 25 | [[LAB 25 - titanic p1]] | CSV file stream ingestion, token parsing, demographic mortality metrics | `c/csv-parsing`, `c/file-io`, `level/advanced` |
| 26 | [[LAB 26 - titanic p2]] | Filtering structured CSV records and exporting clean subsets to disk | `c/csv-parsing`, `c/file-io`, `level/advanced` |
| 27 | [[LAB 27 - titanic p3]] | Comprehensive demographic survival analysis across passenger classes | `c/csv-parsing`, `c/file-io`, `level/advanced` |
| 28 | [[LAB 28 - matrix]] | 2D matrix multiplication, dimension validation, row-column dot products | `c/arrays`, `c/pointers`, `level/intermediate` |
| 29 | [[LAB 29 - grayscale]] | Binary BMP header parsing, pixel byte manipulation, grayscale conversion | `c/bmp-format`, `c/image-processing`, `level/advanced` |
| 30 | [[LAB 30 - student app]] | Production-grade menu-driven student database with file persistence | `c/structs`, `c/file-io`, `level/intermediate` |

---

## ?? Progression & Laboratory Themes

1. **Foundational Mechanics (01 to 06):** Scalar variables, arithmetic expressions, conditional logic, and greedy algorithms. Experiments 01 and 02 contrast memory-space trade-offs between temporary storage variables versus arithmetic XOR/addition swaps.
2. **Patterns & Iterative Logic (07 to 10):** Coordinate geometry on 2D character grids, printing hollow triangular borders and computing Pascal's triangle coefficients.
3. **Array Transformations (11 to 14):** Sorting, element swapping, in-place deletion by shifting, and two-way array merging.
4. **Recursion & Divide-and-Conquer (15 to 17):** Transitioning from iterative loops to recursive call stacks. Experiment 17 introduces Merge Sort ($O(n \log n)$).
5. **Pointer-Based Re-Engineering (18 to 24):** Rewriting previous array algorithms using raw pointer arithmetic (`*(p + i)`), dynamic heap memory (`malloc`/`free`), and two-pointer recursion.
6. **Data Systems & Binary Stream Processing (25 to 30):**
   - **Titanic CSV Suite (25?27):** Parsing multi-field tabular records from disk, converting string tokens, and computing statistical survival ratios.
   - **Linear Algebra (28):** Matrix transformations and dot products.
   - **Binary Image Processing (29):** Decoding raw BMP binary headers and averaging RGB color channels into grayscale.
   - **CRUD Database App (30):** Struct-based persistent student management system.

---

## ?? Navigation
- [[00 - Index]]
- [[CLASS - Index]]
- [[ASG - Index]]
- [[PROJ - Index]]
- [[PRAC - Index]]
- [[BUET - Index]]
- [[ARCH - Index]]
- [[Tag Glossary]]
