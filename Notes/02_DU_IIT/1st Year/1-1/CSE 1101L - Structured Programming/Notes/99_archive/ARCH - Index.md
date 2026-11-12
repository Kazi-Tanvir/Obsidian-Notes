---
title: "ARCH - Index"
aliases:
  - Archive Index
  - Historical Archives Index
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "99_archive/"
up: "[[00 - Index]]"
prev: "[[BUET - Index]]"
created: 2026-10-29
status: draft
---
# ARCH - Index

The `99_archive/` directory preserves the developmental evolution of the coursework, housing early single-file prototypes, developmental change logs, historical bug audits, and comprehensive learning architecture guides for the desktop image editor.

| # | Note | What it teaches | Tags |
|---|---|---|---|
| 01 | [[ARCH - Learning guide]] | Complete educational guide to understanding and rebuilding the IUP desktop Image Editor | `c/gui-iup`, `c/image-processing`, `c/bmp-format`, `level/advanced` |
| 02 | [[ARCH - Project documentation]] | Technical reference manual for image processing APIs, data structures, and architecture | `c/gui-iup`, `c/image-processing`, `c/structs`, `level/advanced` |
| 03 | [[ARCH - Image editor bugs]] | Retrospective code audit detailing 11 real-world systems bugs and their root causes | `c/testing`, `c/bmp-format`, `c/image-processing`, `level/advanced` |
| 04 | [[ARCH - Image editor logs]] | Comprehensive change log documenting bug-fix evolutions and verification steps | `c/testing`, `c/bmp-format`, `c/image-processing`, `level/advanced` |
| 05 | [[ARCH - Early prototypes]] | Inventory of early experimental drafts (standalone grayscale, invert, and lab prototypes) | `c/image-processing`, `c/bmp-format`, `c/loops`, `level/basic` |

---

## 📈 Developmental Evolution

1. **Monolithic Standalone Prototypes:** Before constructing a modular desktop application, early experiments (`grayscale.c`, `invert.c`, `invert_grayscale.c`) proved the mathematics of binary BMP parsing and color channel transformation in isolated terminal scripts.
2. **The First Application Prototype:** The early multi-file software in `Image Manipulation Software/` brought these algorithms into an IUP GUI, encountering real-world systems hurdles: row stride padding corruption, linker symbol collisions, and memory leaks.
3. **Rigorous Auditing and Fix Logging:** Documented in `BUGS.md` and `logs.md`, 11 critical defects were cataloged, root-caused, and resolved, paving the way for the production-grade `LAB_PROJECT/FINAL_PROJECT`.
4. **Pedagogical Crystallization:** The extensive technical documentation and learning guide synthesize these lessons into an enduring reference for C software engineering.

---

## 🧭 Navigation
- [[00 - Index]]
- [[CLASS - Index]]
- [[LAB - Index]]
- [[ASG - Index]]
- [[PROJ - Index]]
- [[PRAC - Index]]
- [[BUET - Index]]
- [[Tag Glossary]]
