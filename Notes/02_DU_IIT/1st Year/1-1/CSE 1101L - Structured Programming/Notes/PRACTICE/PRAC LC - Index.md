---
title: "PRAC LC - Index"
aliases:
  - LeetCode Index
  - LeetCode Practice
tags:
  - type/index
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/LEETCODE/"
up: "[[PRAC - Index]]"
related:
  - "[[PRAC CW 07 - pointer move zero end]]"
  - "[[PRAC CW 06 - pointer reverse string]]"
created: 2026-10-29
status: draft
---
# PRAC LC - Index

The `PRACTICE/LEETCODE/` directory contains solutions to standard competitive programming challenges implemented in C using pointer arithmetic and two-pointer traversal techniques.

| Problem # | Title | File | What it teaches | Tags |
|---|---|---|---|---|
| 283 | Move Zeroes | `283_move_zeroes.c` | In-place two-pointer array compaction shifting non-zeros forward in $O(n)$ time | `c/arrays`, `c/pointers`, `c/searching` |
| 344 | Reverse String | `344_reverse_string.c` | In-place character array inversion using two converging pointers | `c/strings`, `c/pointers`, `c/functions` |

---

## File Summaries

### 1. LeetCode 283: Move Zeroes (`283_move_zeroes.c`)
- **Problem:** Given an integer array `nums`, move all `0`s to the end while maintaining the relative order of non-zero elements, in place without allocating extra arrays.
- **Approach:** Maintains a write pointer `lastNonZeroFoundAt`. Iterates through `nums`; whenever `nums[i] != 0`, writes it to `nums[lastNonZeroFoundAt++]`. Once finished, fills all remaining cells from `lastNonZeroFoundAt` to `numsSize - 1` with `0`.
- **Complexity:** $O(n)$ time, $O(1)$ auxiliary space.

### 2. LeetCode 344: Reverse String (`344_reverse_string.c`)
- **Problem:** Invert an array of characters in place using $O(1)$ extra memory.
- **Approach:** Converging two-pointer technique: sets `left = 0` and `right = sSize - 1`. While `left < right`, swaps characters `s[left]` and `s[right]`, advancing `left++` and decrementing `right--`.
- **Complexity:** $O(n)$ time, $O(1)$ auxiliary space.

---

## 🧭 Navigation
- [[PRAC - Index]]
- [[00 - Index]]
