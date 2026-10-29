---
title: "ARCH - Early prototypes"
aliases:
  - Early prototypes
  - Prototype archive
tags:
  - type/archive
  - c/image-processing
  - c/bmp-format
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "99_archive/"
up: "[[ARCH - Index]]"
related:
  - "[[LAB 29 - grayscale]]"
  - "[[PROJ Image Editor - Overview]]"
created: 2026-10-29
status: draft
---
# ARCH - Early prototypes

> [!abstract] Summary
> An inventory of early exploratory C programs, standalone BMP manipulation scripts, and scratchpad drafts developed during the initial prototyping phases of the semester.

**Source:** `99_archive/` (`grayscale.c`, `invert.c`, `invert_grayscale.c`, and `New folder/`)

## Prototype Inventory & Purpose

| File | Location | What it teaches | Evolution & Legacy |
|---|---|---|---|
| `grayscale.c` | `99_archive/` | Direct binary BMP luminance conversion using raw byte reads | Evolved into [[LAB 29 - grayscale]] and [[PROJ Image Editor - filter]] |
| `invert.c` | `99_archive/` | Inverting 24-bit RGB pixel channels ($255 - c$) directly in BMP streams | Evolved into [[PROJ Image Editor - filter]] |
| `invert_grayscale.c` | `99_archive/` | Combined pipeline: converting to grayscale and immediately inverting | Precursor to multi-filter pipelines |
| `dictionary.c` | `99_archive/New folder/` | Lexicographical word sorting using string comparisons | Precursor to [[ASG 05 - dictionary sort lexicographic]] |
| `discount_loop.c` | `99_archive/New folder/` | Tiered commercial discount logic inside interactive loops | Precursor to [[LAB 06 - discount]] and [[LAB 10 - discount budget]] |
| `hollow_triangle.c` | `99_archive/New folder/` | Coordinate boundary testing for triangular star borders | Precursor to [[LAB 07 - hollow triangle]] |
| `pascal.c` | `99_archive/New folder/` | Binomial combination generation of Pascal's triangle | Precursor to [[LAB 08 - pascal]] and [[BUET 2025 - pascal]] |
| `password.c` | `99_archive/New folder/` | Masked terminal password verification and retry limits | Precursor to [[LAB 09 - password]] |

---

## Pedagogical Notes
- **From Scripts to Applications:** The progression from standalone terminal scripts (`grayscale.c` writing `output.bmp`) to modular desktop applications (`PROJ Image Editor`) illustrates how software evolves from proof-of-concept scripts to maintainable architectures.
- **Safe Sandboxing:** Early drafts allowed verifying mathematical algorithms without the cognitive overhead of desktop GUI event loops.

## My notes
> [!question]- My notes

## Related
- [[LAB 29 - grayscale]]
- [[PROJ Image Editor - Overview]]
