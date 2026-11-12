---
title: "ARCH - Image editor logs"
aliases:
  - Image editor logs
  - logs.md
tags:
  - type/archive
  - c/testing
  - c/bmp-format
  - c/image-processing
  - level/advanced
course: "CSE 1101"
semester: "1.1"
source: "99_archive/Image Manipulation Software/Image Manipulation Software/logs.md"
up: "[[ARCH - Index]]"
related:
  - "[[ARCH - Image editor bugs]]"
  - "[[PROJ Image Editor - Overview]]"
created: 2026-10-29
status: draft
---
# ARCH - Image editor logs

> [!abstract] Summary
> Comprehensive engineering change log detailing the exact root cause analyses, code diffs, and verification steps applied to resolve all defects cataloged in `BUGS.md`.

**Source:** `99_archive/Image Manipulation Software/Image Manipulation Software/logs.md`

## Overview
This change log documents the systematic resolution of all 11 defects found during the image editor audit. For each bug, it records the underlying computational failure, the naive vs correct solution, and the exact code modifications applied to achieve stability in [[PROJ Image Editor - Overview]].

## Key Fix Summaries

### Fix #1: BUG-1 (BMP Row Padding Misplacement)
- **Problem:** `bmp.c` skipped padding bytes *inside* the column loop (`for (w = 0; w < width; w++)`). For a 512x512 image requiring padding, this skipped bytes between individual pixels rather than at the end of the scanline.
- **Resolution:** Moved `fseek(file, padding, SEEK_CUR)` strictly outside the inner width loop, executing once per scanline.

### Fix #2: BUG-3 & BUG-4 (Double-Buffered Kernel Convolution)
- **Problem:** `blur()` and `sharpen()` modified `img->data` while still calculating neighbor averages, polluting subsequent pixel calculations, and failed to clamp neighbor coordinates at edges.
- **Resolution:** Allocated an auxiliary buffer `Pixel *temp = malloc(...)`, read strictly from `img->data`, clamped boundary lookups with `clamp_coord(x, 0, width - 1)`, wrote to `temp`, and replaced the buffer atomically.

### Fix #3: BUG-5 (UCRT Runtime Compatibility)
- **Problem:** MinGW GCC linker failed on static IUP library references to `__imp___argc` and `__imp___argv`.
- **Resolution:** Authored `ucrt_compat.c` exporting pointer shims referencing GCC's native `__argc` and `__argv`.

### Fix #4: BUG-2 (GDI Resource Cleanup)
- **Problem:** The canvas update routine allocated fresh `IupImageRGB` objects without destroying old instances, exhausting system GDI handles.
- **Resolution:** Added `if (old_iup_img) IupDestroy(old_iup_img);` immediately prior to assigning new bitmap handles.

### Fix #5: BUG-11 (Build Tooling Process Termination)
- **Problem:** Re-running `build.bat` while `app.exe` was running failed with `Permission Denied`.
- **Resolution:** Added `taskkill /F /IM ImageEditor.exe >nul 2>nul` to the start of `build.bat`.

## Key takeaways
- Tracking bug fixes with formal root-cause logs prevents recurring regressions.
- Double-buffering is the universal solution for spatial neighborhood mutations in grid architectures.
- Production software engineering requires iterating through systematic audits rather than relying on unguided trial and error.

## My notes
> [!question]- My notes

## Related
- [[ARCH - Image editor bugs]]
- [[PROJ Image Editor - Overview]]
