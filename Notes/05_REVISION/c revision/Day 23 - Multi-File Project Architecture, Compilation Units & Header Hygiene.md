---
tags:
  - c
  - multi-file-projects
  - makefiles
  - compilation-units
  - header-hygiene
  - symbols-linkage
date: 2026-09-14
day: 23
---

# Day 23: Multi-File Project Architecture, Compilation Units, Header Hygiene & Custom Makefiles

---

## 1. Quick Reference & Cheat Sheet

### Compilation Units & Linkage Fundamentals

Translation Unit (TU): A single preprocessed .c source file combined with all #include directives expanded into one flat stream.
Object File (.o): The compiled machine code for a single TU, containing an ELF symbol table (.symtab) and relocation tables (.rel.text).
Header Files (.h): Interface contracts. Must contain only declarations, types, and macros, never non-static variable definitions.

### Declarations vs Definitions

Construct
In Header File (.h)
In Source File (.c)
Scope & Linkage
Function
int compute(int x); (Declaration)
int compute(int x) { return x * 2; } (Definition)
Global / External Linkage
Global Variable
extern int g_total_count; (Declaration)
int g_total_count = 0; (Definition)
Global / External Linkage
Internal Variable
Avoid in headers!
static int s_local_counter = 0;
Local to TU / Internal Linkage
Inline Function
static inline int min(int a, int b) { return a < b ? a : b; }
N/A (Inlined in caller)
Internal Linkage (Per-TU copy)
Constant
#define MAX_BUF 1024 or enum { MAX_BUF = 1024 };
const int MAX_BUF = 1024;
Compile-time Constant

### Makefile Automatic Variables & Syntax

```makefile
# Target: Prerequisites
# Recipe (Must be indented with TAB!)
$@  # The target file name being generated
$<  # The FIRST prerequisite (usually source file)
$^  # ALL prerequisites (separated by spaces)
$?  # Prerequisites newer than the target
# Automatic Dependency Generation (GCC/Clang)
CFLAGS += -MMD -MP
-include $(DEPS)
```
---

---

## 2. In-Depth Theory & Low-Level Mechanics

A. How the Linker Works: Symbol Resolution & Relocation
When you compile a multi-file project with gcc -c main.c -o main.o and gcc -c math.c -o math.o:
Unresolved References: In main.o, calls to math_add() cannot know the actual memory address of math_add because math.c has not been linked yet. The compiler emits a placeholder address 0x00000000 and adds an entry in the .rela.text section: "Fix up call at offset 0x14 with symbol math_add".
Symbol Table (.symtab): math.o exports a symbol entry: math_add marked as GLOBAL in its .text section.
Linker Stage (ld): The linker reads all .o files, merges corresponding sections (.text with .text, .data with .data), computes final virtual addresses, and patches all placeholder offsets (Relocation).
```text
       main.o                                             Merged Executable (ELF):
  ┌─────────────────────────┐                               ┌─────────────────────────┐
  │ .text:                  │                               │ .text:                  │
  │  call 0x00000000 [?]    │ ───┐                          │  main() starts 0x401000 │
  │ .rela.text:             │    │                          │  call 0x401120 ─────────┼──┐
  │  Fixup: math_add @ 0x14 │    │                          │                         │  │
  └─────────────────────────┘    │  Linker (ld)             │  math_add() @ 0x401120 ◄┼──┘
       math.o                    ├── Resolves Symbols       │                         │
  ┌─────────────────────────┐    │   & Relocates Addrs      └─────────────────────────┘
  │ .text:                  │    │
  │  math_add: [machine code│ ───┘
  │ .symtab:                │
  │  math_add (GLOBAL)      │
  └─────────────────────────┘
```
---
B. Strong vs Weak Symbols & The "Multiple Definition" Trap
In standard ELF object files:
Strong Symbol: Functions and initialized global variables (int g_val = 10;).
Weak / Tentative Symbol: Uninitialized global variables (int g_val; without extern).
The Linker Conflict Rules:
Multiple strong symbols with the same identifier ⇒ FATAL LINKER ERROR: multiple definition of 'symbol'.
One strong symbol and multiple weak symbols ⇒ Linker chooses the strong symbol.
Multiple weak symbols ⇒ Linker merges them into a single uninitialized BSS space.
Crucial Takeaway: If you write int config_timeout = 30; in a header file config.h, every .c file that includes config.h generates a strong symbol in its .o file. Linking them will always fail!
---
C. Header Hygiene & Include Guards
To prevent duplicate type definitions when headers include other headers:
```c
#ifndef MY_MODULE_H
#define MY_MODULE_H
// Declarations here...
#endif // MY_MODULE_H
```
#pragma once vs Header Guards: #pragma once is supported by virtually all modern compilers (GCC, Clang, MSVC) and avoids macro naming collisions, while traditional #ifndef guards remain strictly ISO C standard-compliant.
Forward Declarations: If module_a.h only uses a pointer to struct Buffer, do not #include "buffer.h". Instead, use a forward declaration:
```c
struct Buffer; // Forward declaration
void process_buffer(struct Buffer *buf);
```
This completely breaks circular dependency loops and drastically speeds up compile times!
---

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Production-Grade Multi-Module Build Architecture (make_sys)

Objective
Set up a modular, multi-file C architecture with proper header hygiene, internal vs external symbols, automatic dependency tracking, and a production-grade Makefile.
Project Directory Structure
```text
project_root/
├── Makefile
├── include/
│   ├── common.h
│   ├── math_engine.h
│   └── logger.h
└── src/
    ├── math_engine.c
    ├── logger.c
    └── main.c
```
1. Header & Source Files
include/common.h
```c
#ifndef COMMON_H
#define COMMON_H
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
typedef enum {
    STATUS_OK = 0,
    STATUS_ERROR_INVALID_ARG = -1,
    STATUS_ERROR_OVERFLOW    = -2
} StatusCode;
#endif // COMMON_H
```
include/logger.h
```c
#ifndef LOGGER_H
#define LOGGER_H
#include "common.h"
typedef enum {
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_INFO,
    LOG_LEVEL_WARN,
    LOG_LEVEL_ERROR
} LogLevel;
void logger_init(LogLevel min_level);
void logger_log(LogLevel level, const char *fmt, ...);
#endif // LOGGER_H
```
src/logger.c
```c
#include "logger.h"
#include <stdio.h>
#include <stdarg.h>
// Static internal variable: Invisible outside this translation unit!
static LogLevel s_min_level = LOG_LEVEL_INFO;
void logger_init(LogLevel min_level) {
    s_min_level = min_level;
}
void logger_log(LogLevel level, const char *fmt, ...) {
    if (level < s_min_level) return;
    const char *level_str = "INFO";
    if (level == LOG_LEVEL_DEBUG) level_str = "DEBUG";
    if (level == LOG_LEVEL_WARN)  level_str = "WARN";
    if (level == LOG_LEVEL_ERROR) level_str = "ERROR";
    printf("[%s] ", level_str);
    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
    putchar('\n');
}
```
include/math_engine.h
```c
#ifndef MATH_ENGINE_H
#define MATH_ENGINE_H
#include "common.h"
// Exported global variable declaration
extern uint64_t g_operation_count;
StatusCode math_safe_add(int32_t a, int32_t b, int32_t *out_result);
StatusCode math_safe_mul(int32_t a, int32_t b, int32_t *out_result);
#endif // MATH_ENGINE_H
```
src/math_engine.c
```c
#include "math_engine.h"
#include <limits.h>
// Definition of exported global variable (Exactly ONCE in .c file!)
uint64_t g_operation_count = 0;
StatusCode math_safe_add(int32_t a, int32_t b, int32_t *out_result) {
    g_operation_count++;
    if (!out_result) return STATUS_ERROR_INVALID_ARG;
    if ((b > 0 && a > INT32_MAX - b) || (b < 0 && a < INT32_MIN - b)) {
        return STATUS_ERROR_OVERFLOW;
    }
    *out_result = a + b;
    return STATUS_OK;
}
StatusCode math_safe_mul(int32_t a, int32_t b, int32_t *out_result) {
    g_operation_count++;
    if (!out_result) return STATUS_ERROR_INVALID_ARG;
    int64_t prod = (int64_t)a * (int64_t)b;
    if (prod > INT32_MAX || prod < INT32_MIN) {
        return STATUS_ERROR_OVERFLOW;
    }
    *out_result = (int32_t)prod;
    return STATUS_OK;
}
```
src/main.c
```c
#include "common.h"
#include "logger.h"
#include "math_engine.h"
#include <stdio.h>
int main(void) {
    logger_init(LOG_LEVEL_DEBUG);
    logger_log(LOG_LEVEL_INFO, "Multi-module application booted successfully.");
    int32_t sum = 0;
    StatusCode st = math_safe_add(1500000000, 1000000000, &sum);
    if (st == STATUS_ERROR_OVERFLOW) {
        logger_log(LOG_LEVEL_WARN, "Detected integer overflow during addition!");
    } else {
        logger_log(LOG_LEVEL_INFO, "Sum: %d", sum);
    }
    int32_t prod = 0;
    math_safe_mul(25, 4, &prod);
    logger_log(LOG_LEVEL_INFO, "Product: %d", prod);
    logger_log(LOG_LEVEL_DEBUG, "Total Math Operations Tracked: %llu", (unsigned long long)g_operation_count);
    return 0;
}
```
2. The Production-Grade Makefile
```makefile
# Compiler and Toolchain Definitions
CC       := gcc
CFLAGS   := -std=c17 -Wall -Wextra -Wpedantic -Wconversion -Werror -D_GNU_SOURCE
CPPFLAGS := -Iinclude -MMD -MP # Auto-generate header dependencies
LDFLAGS  := 
LDLIBS   := 
# Build Mode: make DEBUG=1
ifeq ($(DEBUG), 1)
    CFLAGS += -g -O0 -fsanitize=address,undefined
else
    CFLAGS += -O3 -DNDEBUG
endif
# Directory Layout
SRC_DIR   := src
BUILD_DIR := build
OBJ_DIR   := $(BUILD_DIR)/obj
BIN_DIR   := $(BUILD_DIR)/bin
TARGET    := $(BIN_DIR)/app
# Locate all source files and map to object files
SRCS := $(wildcard $(SRC_DIR)/*.c)
OBJS := $(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))
DEPS := $(OBJS:.o=.d)
.PHONY: all clean run
all: $(TARGET)
# Link executable
$(TARGET): $(OBJS) | $(BIN_DIR)
@echo "[LINK] $@"
$(CC) $(CFLAGS) $(LDFLAGS) $^ $(LDLIBS) -o $@
# Compile Translation Units
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
@echo "[CC]   $<"
$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
# Create Build Directories
$(BIN_DIR) $(OBJ_DIR):
@mkdir -p $@
# Run Target
run: $(TARGET)
@./$(TARGET)
# Clean Target
clean:
@echo "[CLEAN] Removing $(BUILD_DIR)"
@rm -rf $(BUILD_DIR)
# Include automatically generated header dependencies
-include $(DEPS)
```
---

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Header Variable Definition Linker Collision

Examine the following buggy header file included across multiple .c files in a large project:
```c
// config.h
#ifndef CONFIG_H
#define CONFIG_H
// BUG 1: Initialized non-static variable defined inside a header!
int max_connection_retries = 5; 
// BUG 2: Non-static function implementation inside a header!
int get_default_timeout(void) {
    return 30;
}
#endif // CONFIG_H
```

### Analysis of Vulnerabilities:

Multiple Definition Linker Collision: When config.h is included by client.c and server.c, both .o files emit strong symbols for max_connection_retries and get_default_timeout. The linker fails immediately:
multiple definition of 'max_connection_retries'; client.o: first defined here.
Include Guards Do NOT Prevent This: Include guards only prevent duplicate inclusions within the same translation unit. They do nothing across different .c files.

### Defensive Fix:

```c
// config.h (DEFENSIVE FIX)
#ifndef CONFIG_H
#define CONFIG_H
// Fix 1: Declare as 'extern' in the header...
extern int g_max_connection_retries;
// Fix 2: Inline functions in headers MUST be declared 'static inline'
static inline int get_default_timeout(void) {
    return 30;
}
#endif // CONFIG_H
```
```c
// config.c (EXACTLY ONCE IN A SOURCE FILE)
#include "config.h"
// Define the variable in exactly one source file:
int g_max_connection_retries = 5;
```
if ((b > 0 && a > INT32_MAX - b) || (b < 0 && a < INT32_MIN - b)) {
