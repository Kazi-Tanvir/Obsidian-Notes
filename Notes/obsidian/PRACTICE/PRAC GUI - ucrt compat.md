---
title: "PRAC GUI - ucrt compat"
aliases:
  - GUI ucrt compat
  - tutorial ucrt compat
tags:
  - type/practice
  - c/pointers
  - c/cli-args
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/image_editor/gui/ucrt_compat.c"
up: "[[PRAC - Index]]"
related:
  - "[[PROJ Image Editor - ucrt compat]]"
created: 2026-10-29
status: draft
---
# PRAC GUI - ucrt compat

> [!abstract] Summary
> Exports runtime argument pointers (`__imp___argc`, `__imp___argv`) to bridge modern MinGW UCRT linking with static IUP libraries in the GUI tutorial series.

**Source:** `PRACTICE/image_editor/gui/ucrt_compat.c`

## Problem
Resolve undefined reference linker errors when compiling the tutorial steps against precompiled `libiup.a`.

## Concepts used
- **Runtime Symbol Aliasing:** Creating global pointer shims satisfying MSVC CRT expectations from GCC runtime symbols.

## Code
```c
/* ucrt_compat.c
 * Compatibility shim for linking IUP 3.32 static libraries with modern
 * MinGW / UCRT on Windows. IUP's iupwindows_main.o references
 * __imp___argc and __imp___argv (old MSVCRT-style import symbols).
 * Modern GCC/UCRT no longer exposes __argc/__argv as linkable externals,
 * so we provide the symbols ourselves with harmless zero/null defaults.
 * IupOpen() receives the real argc/argv from our main() call anyway.
 */
static int    _compat_argc = 0;
static char  *_compat_argv_buf = "";
static char **_compat_argv = &_compat_argv_buf;

int    *__imp___argc = &_compat_argc;
char ***__imp___argv = (char ***)&_compat_argv;
```

## How it works
Exports pointers referencing MinGW's native `__argc` and `__argv`.

## My notes
> [!question]- My notes

## Related
- [[PROJ Image Editor - ucrt compat]]
