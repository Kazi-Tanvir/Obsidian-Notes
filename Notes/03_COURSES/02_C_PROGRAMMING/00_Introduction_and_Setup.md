---
tags: [c-programming, setup, introduction]
---

# 00 Introduction and Setup

## What is Programming?
Computer programming is a medium for us to communicate with computers. Just like we use languages like 'Hindi' or 'English' to communicate with each other, programming is a way for us to deliver our instructions to the computer.

## What is C?
C is one of the oldest and finest programming languages. It was developed by Dennis Ritchie at AT&T’s Bell Labs, USA in 1972.

### Why C?
C is known for its efficiency and control, making it perfect for system-level programming. It is a low-level, compiled language that provides fine-grained control over hardware and memory.

### Uses of C
1. Major parts of Windows, Linux, and other operating systems are written in C.
2. C is used to write driver programs for devices like tablets, printers, etc.
3. C language is used to program embedded systems (Microwaves, Cameras, etc.).
4. C is used to develop games where low latency is crucial.

## Installation and Compilation
We use **VS Code** as our code editor and the **MinGW gcc** compiler to compile our C programs.

**Compilation** is the process of translating high-level source code written in C into machine code (binary instructions) that a computer's CPU can execute directly.

## Basic Structure of a C Program
All C programs follow a basic structure, starting with a `main()` function.

```c
#include <stdio.h>

int main() {
    printf("Hello, I am learning C with Harry");
    return 0;
}
```

### Key Rules:
- Execution starts from `main()`.
- Every instruction is terminated with a semicolon `;`.
- Instructions are case-sensitive.
- Instructions are executed in the order they are written.
