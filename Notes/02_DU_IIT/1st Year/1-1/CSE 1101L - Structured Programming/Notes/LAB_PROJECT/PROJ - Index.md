---
title: "PROJ - Index"
aliases:
  - Project Index
  - Lab Projects Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
up: "[[00 - Index]]"
prev: "[[ASG - Index]]"
next: "[[PRAC - Index]]"
created: 2026-10-29
status: draft
---
# PROJ - Index

The `LAB_PROJECT/` directory represents the capstone programming projects of the CSE 1101 coursework. It brings together modular game development, exam grading test harnesses, real-time interactive business simulations, full automated test suites, and an IUP 3.32 graphical desktop image manipulation software suite.

| # | Note | What it teaches | Tags |
|---|---|---|---|
| 01 | [[PROJ TicTacToe - array]] | Interactive 2-player board game with coordinate grid mapping and win condition scans | `c/game-logic`, `c/arrays`, `c/control-flow`, `level/intermediate` |
| 02 | [[PROJ TicTacToe - no array]] | Pure scalar game state architecture using 9 isolated variables and branching logic | `c/game-logic`, `c/control-flow`, `c/functions`, `level/basic` |
| 03 | [[PROJ - Hangman]] | Word guessing game with secret masking, ASCII gallows stage rendering, and letter tracking | `c/game-logic`, `c/strings`, `c/arrays`, `level/intermediate` |
| 04 | [[PROJ Midterm Exam - q1]] | Calendar date validation and leap year day counts under timed exam constraints | `c/control-flow`, `c/arrays`, `c/math`, `level/basic` |
| 05 | [[PROJ Midterm Exam - q2]] | Frequency histogram generation and asterisks rendering for sorted integer distributions | `c/sorting`, `c/arrays`, `c/loops`, `level/basic` |
| 06 | [[PROJ Midterm Exam - q3]] | Recursive digital root reduction via recursive digit summation down to single digits | `c/recursion`, `c/math`, `c/functions`, `level/basic` |
| 07 | [[PROJ Midterm Exam - grader]] | Automated Bash test runner harness compiling, executing, diffing, and scoring solutions | `c/testing`, `c/cli-args`, `level/intermediate` |
| 08 | [[PROJ Midterm Practice - hotel reservation]] | Multi-room hospitality reservation console tracking guest dates, rates, and occupancy | `c/arrays`, `c/strings`, `c/control-flow`, `level/intermediate` |
| 09 | [[PROJ Image Editor - Overview]] | Architecture overview of the modular IUP 3.32 64-bit desktop image manipulation suite | `c/gui-iup`, `c/image-processing`, `c/bmp-format`, `level/advanced` |
| 10 | [[PROJ Image Editor - main]] | IUP application lifecycle, event loop initialization, dialog binding, and resource teardown | `c/gui-iup`, `c/cli-args`, `level/intermediate` |
| 11 | [[PROJ Image Editor - image]] | Low-level 24-bit uncompressed BMP parsing, memory byte alignment, row padding, and file I/O | `c/bmp-format`, `c/binary-io`, `c/dynamic-memory`, `level/advanced` |
| 12 | [[PROJ Image Editor - filter]] | Comprehensive pixel processing engine: grayscale, brightness, inversion, flips, 90° rotation, crop, blur, and sharpening convolution | `c/image-processing`, `c/pointers`, `c/math`, `level/advanced` |
| 13 | [[PROJ Image Editor - gui]] | Native IUP desktop GUI: layout containers, button callbacks, preview canvas, and file dialogs | `c/gui-iup`, `c/pointers`, `c/structs`, `level/advanced` |
| 14 | [[PROJ Image Editor - ucrt compat]] | UCRT symbols compatibility layer bridging GCC MinGW with modern Microsoft Universal C Runtime | `c/pointers`, `c/cli-args`, `level/advanced` |
| 15 | [[PROJ Image Editor - build]] | Multi-file compilation and native Win32/IUP link script with automated cleanup and launch | `c/testing`, `c/cli-args`, `level/intermediate` |
| 16 | [[PROJ Final Exam - Overview]] | Comprehensive exam specification for the BSSE 18th batch Food Ordering System | `c/structs`, `c/file-io`, `c/testing`, `level/advanced` |
| 17 | [[PROJ Final Exam - food ordering system]] | Production-grade 900+ line terminal ordering engine managing discounts, items, deliveries, and database files | `c/structs`, `c/file-io`, `c/strings`, `level/advanced` |
| 18 | [[PROJ Final Exam - grader harness]] | High-precision automated test framework executing 76 unit tests and grading student code | `c/testing`, `c/file-io`, `c/structs`, `level/advanced` |

---

## 📈 Progression & Milestone Themes

1. **Terminal Game Engines (TicTacToe & Hangman):** Managing turns, state transitions, board rendering, user input validation, and win/loss terminal evaluation.
2. **Pedagogical Contrast (TicTacToe Array vs No Array):** Contrasting clean 2D matrix abstraction with primitive scalar state variables.
3. **Timed Assessments & Automated Evaluation (Midterm Exam):** Solving algorithmic challenges under exam conditions and verifying correctness against comprehensive Bash test runners (`grader.sh`).
4. **Stateful Console Information Systems (Hotel Reservation):** Modeling real-world booking transactions with multi-array entity relationships and financial accounting.
5. **Desktop GUI & Binary Systems Software (Image Editor):** The semester's capstone achievement: a multi-file modular C application combining low-level packed binary BMP I/O, mathematical matrix convolution filters, and the IUP GUI toolkit.
6. **Final Examination Benchmark (Food Ordering System):** Complete practical software engineering demonstration: file-backed database persistence (`db.txt`), complex struct hierarchies, pricing engines, and rigorous 76-point test validation (`grader.c`).

---

## 🧭 Navigation
- [[00 - Index]]
- [[CLASS - Index]]
- [[LAB - Index]]
- [[ASG - Index]]
- [[PRAC - Index]]
- [[BUET - Index]]
- [[ARCH - Index]]
- [[Tag Glossary]]
