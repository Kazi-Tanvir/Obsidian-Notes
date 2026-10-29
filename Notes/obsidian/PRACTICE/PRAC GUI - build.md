---
title: "PRAC GUI - build"
aliases:
  - GUI build script
  - tutorial build
tags:
  - type/practice
  - c/testing
  - c/cli-args
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/image_editor/gui/build.bat"
up: "[[PRAC - Index]]"
related:
  - "[[PROJ Image Editor - build]]"
created: 2026-10-29
status: draft
---
# PRAC GUI - build

> [!abstract] Summary
> Windows Batch script automating compilation and linking of tutorial GUI examples with IUP and native Win32 libraries.

**Source:** `PRACTICE/image_editor/gui/build.bat`

## Problem
Automate the compilation of GUI tutorial programs, linking `-liup`, `-lgdi32`, and associated Windows libraries.

## Concepts used
- **Batch Linking Script:** GCC command-line configuration with include and library flags.

## Code
```bat
@echo off
setlocal

echo ====================================================
echo   Building Image Manipulation Software (Win64)
echo ====================================================
taskkill /F /IM ImageEditor.exe >nul 2>nul

gcc main.c ucrt_compat.c ^
    -o ImageEditor.exe ^
    -I./include -L./lib ^
    -liup -lgdi32 -lcomdlg32 -lcomctl32 -luuid -loleaut32 -lole32 -luxtheme ^
    -Wall -Wextra

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] ImageEditor.exe built successfully!
    echo Launching ImageEditor.exe...
    .\ImageEditor.exe
) else (
    echo.
    echo [ERROR] Build failed! Please review compiler errors above.
)

pause
```

## How it works
Invokes GCC with required search paths and libraries, terminating with interactive `pause`.

## My notes
> [!question]- My notes

## Related
- [[PROJ Image Editor - build]]
