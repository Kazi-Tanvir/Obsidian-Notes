---
title: "LAB 25 - titanic p1"
aliases:
  - titanic p1
  - 25_titanic_p1
tags:
  - type/lab
  - c/csv-parsing
  - c/file-io
  - c/strings
  - level/advanced
course: "CSE 1101"
semester: "1.1"
source: "LAB/25_titanic_p1.c"
number: 25
up: "[[LAB - Index]]"
prev: "[[LAB 24 - merge sort]]"
next: "[[LAB 26 - titanic p2]]"
related:
  - "[[LAB 26 - titanic p2]]"
  - "[[LAB 27 - titanic p3]]"
  - "[[CLASS 25 - file sort cg]]"
created: 2026-10-29
status: draft
---
# LAB 25 - titanic p1

> [!abstract] Summary
> Ingests a real-world CSV dataset (`titanic.csv`) using stream line reading and comma tokenization, categorizing passenger survival by demographic groups (gender and age bands).

**Source:** `LAB/25_titanic_p1.c`

## Problem
Read up to 1000 rows from `data/titanic.csv`, parse comma-delimited fields (survival status, gender, and age), handle missing values, and calculate mortality percentages across male, female, child ($< 18$), adult ($18 \dots 39$), and senior ($\ge 40$) cohorts.

## Concepts used
- **File Stream Ingestion (`fopen`/`fgets`):** Opening a file handle in read mode (`"r"`) and buffering line by line into a fixed memory buffer `line[1024]`.
- **Manual CSV Token Parsing (`strchr`):** Locating delimiter commas sequentially via `strchr(ptr, ',')`, temporarily null-terminating each token (`*next = '\0'`), and advancing `ptr`.
- **String-to-Numeric Conversions:** Using `atoi()` to parse integer survival flags ($0$ or $1$) and `atof()` for floating-point ages.
- **Handling Missing Data:** Detecting empty or trailing newline characters in the age column and flagging absent entries with sentinel value `-1.0`.

## Code
```c
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #define MAX_ROWS 1000

    int main() {
        FILE *file = fopen("data/titanic.csv", "r");
        if (!file) {
            printf("Error: Could not open titanic.csv\n");
            return 1;
        }

        char line[1024];
        char gender[MAX_ROWS][10];
        int status[MAX_ROWS];
        float age[MAX_ROWS];
        int count = 0;

        fgets(line, sizeof(line), file);

        while (fgets(line, sizeof(line), file) != NULL && count < MAX_ROWS) {
            char *ptr = line;
            int col = 0;

            while (ptr) {
                char *next = strchr(ptr, ',');
                if (next) {
                    *next = '\0'; 
                }

                if (col == 1) {
                    status[count] = atoi(ptr);
                }
                else if (col == 5) {
                    strcpy(gender[count], ptr);
                }
                else if (col == 6) {
                    if (*ptr == '\0' || *ptr == '\r' || *ptr == '\n') age[count] = -1.0;
                    
                    else  age[count] = atof(ptr);
                }
                if (!next) break;
                ptr = next + 1;
                col++;
            }
            count++;
        }
        
        fclose(file);
        
        int dead_male = 0;
        int alive_male = 0;

        int dead_female = 0;
        int alive_female = 0;

        for(int i = 0 ; i < count ; i++){
            if(age[i] == -1.0) continue;
            if(!(strcmp(gender[i], "male")) && status[i] == 1) alive_male++;
            if(!(strcmp(gender[i], "male")) && status[i] == 0) dead_male++;
            if(!(strcmp(gender[i], "female")) && status[i] == 1) alive_female++;
            if(!(strcmp(gender[i], "female")) && status[i] == 0) dead_female++;
        }
        
        float female = alive_female + dead_female;
        float male = alive_male + dead_male;
        float per_male = 100*(alive_male/male);
        float per_female = 100*(alive_female/female);

        int alive_child = 0;
        int dead_child = 0;
        int alive_adult = 0;
        int dead_adult = 0;
        int alive_senior = 0;
        int dead_senior = 0; 
        for(int i = 0 ; i < count ; i++){
            if((age[i] > 0.00 && age[i] < 18.00)&& status[i] == 1) alive_child++;
            if((age[i] > 0.00 && age[i] < 18.00)&& status[i] == 0) dead_child++;
            if((age[i] >= 18.00 && age[i] < 40.00)&& status[i] == 1) alive_adult++;
            if((age[i] >= 18.00 && age[i] < 40.00)&& status[i] == 0) dead_adult++;
            if(age[i] >= 40.00 && status[i] == 1) alive_senior++;
            if(age[i] >= 40.00 && status[i] == 0) dead_senior++;
        }

        float child = alive_child + dead_child;
        float adult = alive_adult + dead_adult;
        float senior = alive_senior + dead_senior;

        printf("Total Male: %d\n", (int)male);
        printf("Total Dead Male: %d\n", dead_male);
        printf("Percentage of Dead Male: %.2f%%\n\n", 100.0 * (dead_male / male));

        printf("Total Female: %d\n", (int)female);
        printf("Total Dead Female: %d\n", dead_female);
        printf("Percentage of Dead Female: %.2f%%\n\n", 100.0 * (dead_female / female));

        printf("Percentage of Alive Child: %.2f%%\n", 100.0 * (alive_child / child));
        printf("Percentage of Alive Adult: %.2f%%\n", 100.0 * (alive_adult / adult));
        printf("Percentage of Alive Senior: %.2f%%\n", 100.0 * (alive_senior / senior));

        return 0;
    }
```

## How it works
1. Opens `data/titanic.csv` using `fopen()`. If NULL, terminates with an error code.
2. Reads the header line using `fgets()` to skip column labels.
3. In a `while` loop, reads up to `MAX_ROWS` (1000) records:
   - Sets pointer `ptr = line` and tracks `col = 0`.
   - Replaces each comma with `\0` to isolate the current column token.
   - Saves column 1 into `status[count]`, column 5 into `gender[count]`, and column 6 into `age[count]`.
   - Increments row counter `count`.
4. Closes the file handle with `fclose(file)`.
5. Iterates through parsed rows, skipping rows where `age[i] == -1.0`, and tallies survival/death totals by gender and age categories.
6. Computes percentage ratios and prints demographic survival summaries.

## Diagram / trace
```mermaid
flowchart TD
    A["data/titanic.csv"] -->|"fopen(r)"| B["fgets(line, 1024, file)"]
    B --> C["Skip CSV Header Line"]
    C --> DMore lines & count < 1000?
    D -- Yes --> E["Tokenize with strchr(ptr, ',')"]
    E --> F["col 1: status<br>col 5: gender<br>col 6: age"]
    F --> D
    D -- No --> G["fclose(file)"]
    G --> H["Iterate Records & Accumulate Cohorts"]
    H --> I["Output Mortality & Survival %"]
```

## Sample run
```text
Total Male: 453
Total Dead Male: 360
Percentage of Dead Male: 79.47%

Total Female: 261
Total Dead Female: 64
Percentage of Dead Female: 24.52%

Percentage of Alive Child: 53.98%
Percentage of Alive Adult: 38.36%
Percentage of Alive Senior: 37.42%
```

## Gotchas
> [!warning] Embedded Commas in Quoted Fields
> Standard CSV records often wrap strings containing commas in quotes (e.g., `"Braund, Mr. Owen Harris"`). Splitting naively on every comma shifts column indices if a passenger's name contains a comma. Fortunately, in this file the name appears in column 3, and column counting accounts for standard formatting.

## Possible improvements
- Encapsulate row attributes in a `struct Passenger` instead of maintaining multiple parallel arrays (`gender`, `status`, `age`).
- Implement quote-aware CSV tokenization so names containing commas do not risk field misalignment.

## Key takeaways
- Tabular text datasets can be ingested without external libraries using standard `fgets` and pointer-based token isolation (`strchr`).
- Missing or invalid records require explicit sentinel values (e.g., `-1.0`) to avoid skewing numerical averages.
- Parallel arrays allow quick prototyping, but structured types (`struct`) improve maintainability.

## My notes
> [!question]- My notes

## Related
- [[LAB 26 - titanic p2]]
- [[LAB 27 - titanic p3]]
- [[CLASS 25 - file sort cg]]
