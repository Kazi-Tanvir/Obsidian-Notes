---
title: "CLASS 20 - cmd arg"
aliases:
  - cmd arg
  - 20_cmd_arg
tags:
  - type/lecture
  - c/cli-args
  - c/strings
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/20_cmd_arg.c"
number: 20
up: "[[CLASS - Index]]"
prev: "[[CLASS 19 - pointer row sum]]"
next: "[[CLASS 21 - file basic]]"
related:
  - "[[PROJ Midterm Exam - grader]]"
  - "[[CLASS 28 - shift encryption]]"
created: 2026-10-29
status: draft
---
# CLASS 20 - cmd arg

> [!abstract] Summary
> Accesses and parses command-line arguments passed from the operating system shell via `argc` and `argv`.

**Source:** `CLASS/20_cmd_arg.c`

## Problem
Enable C programs to receive configuration parameters, file names, or command flags directly when executed from the terminal shell without prompting interactively.

## Concepts used
- **`argc` (Argument Count)**: An integer holding the total number of command-line arguments provided, including the program name itself ($	ext{argc} \ge 1$).
- **`argv` (Argument Vector)**: An array of character pointers (`char *argv[]`) where `argv[0]` is the program name or path, `argv[1]` is the first user argument, and `argv[argc - 1]` is the final argument.
- **Null Sentinel**: The C standard guarantees that `argv[argc]` is always a `NULL` pointer.

## Code
```c
#include<stdio.h>

int main(int argc,char *argv[]){
    printf("Number of arguments: %d\n", argc);
    for(int i=0; i<argc; i++){
        printf("Argument %d: %s\n", i, argv[i]);
    }
    return 0;
}
```

## How it works
1. **Entry Point Signature**: `int main(int argc, char *argv[])` receives parameters initialized by the OS runtime environment during process startup.
2. **Argument Count Display**: Prints `printf("Number of arguments: %d\n", argc)`.
3. **Vector Iteration**: A `for` loop runs from `i = 0` to `i < argc`, printing each argument index and string value:
   `printf("Argument %d: %s\n", i, argv[i]);`.

## Sample run
```text
$ ./prog arg1 hello world
Number of arguments: 4
Argument 0: C:\path\to\prog.exe
Argument 1: arg1
Argument 2: hello
Argument 3: world
```

## Gotchas
> [!warning] Arguments are Always Strings & Zero-Index Offsets
> 1. **String Conversion Required**: Numerical arguments passed from the CLI (e.g. `./prog 42`) are received as strings (`"42"`), not numbers! To perform math on them, they must be converted using `atoi(argv[i])` or `strtol(argv[i], NULL, 10)`.
> 2. **Index Offset**: Beginners often forget that `argv[0]` is the program name. If a user supplies one argument, `argc` is 2, and the argument is at `argv[1]`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 28 - shift encryption]] - Using CLI arguments to pass encryption shift keys
- [[PROJ Midterm Exam - grader]] - Bash script passing parameters to automated graders
