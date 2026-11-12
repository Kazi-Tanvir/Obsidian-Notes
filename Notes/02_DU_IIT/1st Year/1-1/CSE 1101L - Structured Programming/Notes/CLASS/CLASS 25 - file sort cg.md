---
title: "CLASS 25 - file sort cg"
aliases:
  - file sort cg
  - 25_file_sort_cg
tags:
  - type/lecture
  - c/file-io
  - c/sorting
  - c/arrays
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/25_file_sort_cg.c"
number: 25
up: "[[CLASS - Index]]"
prev: "[[CLASS 24 - take cg file]]"
next: "[[CLASS 26 - struct student info]]"
related:
  - "[[CLASS 24 - take cg file]]"
  - "[[ASG 04 - sort student by cgpa]]"
  - "[[ASG 09 - file marksheet]]"
created: 2026-10-29
status: draft
---
# CLASS 25 - file sort cg

> [!abstract] Summary
> Reads student records from disk and sorts them in descending order of CGPA using an indirect merit index array, preserving original data while generating ranked reports.

**Source:** `CLASS/25_file_sort_cg.c`

## Problem
Sort 50 student records by academic performance (CGPA in descending order) and write the ranked merit list to a new output file `data/sorted_cg.txt`. The original input data order should not be destructively rearranged in memory.

## Concepts used
- **Indirect Index Sorting (`merit[i]`)**: Instead of physically swapping large multi-byte records in memory (moving 100-byte strings, integers, floats), an auxiliary array of small integers `merit[i] = i` is sorted. Swapping two 4-byte integers changes the view order without touching the raw data!
- **Selection / Bubble Comparison**: Comparing `cgpa[merit[i]] < cgpa[merit[j]]` and swapping the pointer indices `merit[i]` and `merit[j]`.
- **Formatted File Writing (`fprintf`)**: Writing the ranked results (`Rank, Roll, Name, CGPA`) out to a fresh file stream.

## Code
```c
#include <stdio.h>

int main() {
    FILE *input = fopen("data/name_cg.txt", "r");
    FILE *output = fopen("data/sorted_cg.txt", "w"); 

    if (input == NULL || output == NULL) {
        printf("Unable to open the file\n");
        if (input) fclose(input);
        if (output) fclose(output);
        return 1;
    }

    int roll[50];
    float cgpa[50];
    char name[50][100];
    int merit[50];

    for (int i = 0; i < 50; i++) {
        fscanf(input, " %d %s %f", &roll[i], name[i], &cgpa[i]);
    }

    for (int i = 0; i < 50; i++) {
        merit[i] = i;
    }

    for (int i = 0; i < 50; i++) {
        for (int j = i + 1; j < 50; j++) {
            if (cgpa[merit[i]] < cgpa[merit[j]]) {
                int temp = merit[i];
                merit[i] = merit[j];
                merit[j] = merit[j];
                merit[j] = temp;
            }
        }
    }

    for (int i = 0; i < 50; i++) {
        fprintf(output, "%d %d %s %.2f\n", i + 1, roll[merit[i]], name[merit[i]], cgpa[merit[i]]);
    }

    fclose(input);
    fclose(output);

    return 0;
}
```

## How it works
1. **File Opening**: Opens `"data/name_cg.txt"` for reading and `"data/sorted_cg.txt"` for writing.
2. **Ingestion**: Reads 50 records into parallel arrays `roll`, `name`, and `cgpa`.
3. **Index Initialization**:
   - `for (int i = 0; i < 50; i++) merit[i] = i;`
   - Initially, rank 0 points to student 0, rank 1 to student 1, etc.
4. **Indirect Sorting Loops**:
   - Nested loops compare CGPAs via the index array: `if (cgpa[merit[i]] < cgpa[merit[j]])`.
   - If student `merit[j]` has a higher CGPA than `merit[i]`, their indices in `merit[]` are swapped.
5. **Formatted Output Generation**:
   - Iterates through the sorted `merit` array:
   - `fprintf(output, "%d %d %s %.2f\n", i + 1, roll[merit[i]], name[merit[i]], cgpa[merit[i]]);`
   - Writes the 1-based rank (`i + 1`), student roll, name, and CGPA into `data/sorted_cg.txt`.
6. **Cleanup**: Closes both streams.

## Diagram / trace
```mermaid
flowchart TD
    subgraph Original Parallel Arrays (Untouched)
        A0["[0] Roll: 101, Name: Bob, CGPA: 3.20"]
        A1["[1] Roll: 102, Name: Alice, CGPA: 3.95"]
        A2["[2] Roll: 103, Name: Charlie, CGPA: 3.80"]
    end
    subgraph Sorted Merit Index Array
        M0["merit[0] = 1 (Alice - 3.95)"]
        M1["merit[1] = 2 (Charlie - 3.80)"]
        M2["merit[2] = 0 (Bob - 3.20)"]
    end
    M0 -.-> A1
    M1 -.-> A2
    M2 -.-> A0
```

## Sample run
```text
[Rank 1]  102 Alice    3.95
[Rank 2]  103 Charlie  3.80
[Rank 3]  101 Bob      3.20
...
-> Written to data/sorted_cg.txt
```

## Gotchas
> [!warning] Redundant Self-Assignment in Swap Logic
> Examine the swap block on lines 33?38:
> ```c
> int temp = merit[i];
> merit[i] = merit[j];
> merit[j] = merit[j]; // <-- Redundant self-assignment!
> merit[j] = temp;
> ```
> Line 35 contains a redundant typo statement `merit[j] = merit[j];`. Fortunately, line 36 immediately overwrites `merit[j] = temp;`, so the swap remains mathematically correct, but the redundant instruction represents unnecessary dead code.

## Possible improvements
- Modernize data representation using `struct Student` instead of parallel arrays.
- Upgrade the $O(n^2)$ selection sort to an $O(n \log n)$ Merge Sort or standard `qsort()`.
- Add secondary sorting criteria (e.g., breaking CGPA ties by roll number).

## Key takeaways
- Indirect index sorting is computationally superior to physical record swapping when records contain large strings or structures.
- Original data records remain unmodified in memory, allowing multiple different sorting views (by CGPA, by Roll, by Name) simultaneously.
- Always cleanly close both input and output file handles.

## My notes
> [!question]- My notes

## Related
- [[CLASS 24 - take cg file]] - Ingesting student records from disk
- [[ASG 04 - sort student by cgpa]] - Homework implementation of student ranking
- [[ASG 09 - file marksheet]] - Generating multi-course marksheet reports
