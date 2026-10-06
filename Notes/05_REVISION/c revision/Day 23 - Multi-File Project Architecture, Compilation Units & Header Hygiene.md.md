\-\--\<line-break/\>tags:\<line-break/\> - c\<line-break/\> -
multi-file-projects\<line-break/\> - makefiles\<line-break/\> -
compilation-units\<line-break/\> - header-hygiene\<line-break/\> -
symbols-linkage\<line-break/\>date: 2026-09-14\<line-break/\>day:
23\<line-break/\>\-\--

# Day 23: Multi-File Project Architecture, Compilation Units, Header Hygiene \&amp; Custom Makefiles

\-\--

## 1. Quick Reference \&amp; Cheat Sheet

### Compilation Units \&amp; Linkage Fundamentals

- **Translation Unit (TU):** A single preprocessed .c source file
  combined with all #include directives expanded into one flat stream.

- **Object File (.o):** The compiled machine code for a single TU,
  containing an ELF symbol table (.symtab) and relocation tables
  (.rel.text).

- **Header Files (.h):** Interface contracts. **Must contain only
  declarations, types, and macros**, never non-static variable
  definitions.

### Declarations vs Definitions

  -------------------------------------------------------------------------
  **Construct**    **In Header File    **In Source File    **Scope \&amp;
                   (.h)**              (.c)**              Linkage**
  ---------------- ------------------- ------------------- ----------------
  **Function**     int compute(int x); int compute(int x)  Global /
                   (Declaration)       { return x \* 2; }  External Linkage
                                       (Definition)        

  **Global         extern int          int g_total_count = Global /
  Variable**       g_total_count;      0; (Definition)     External Linkage
                   (Declaration)                           

  **Internal       *Avoid in headers!* static int          Local to TU /
  Variable**                           s_local_counter =   Internal Linkage
                                       0;                  

  **Inline         static inline int   *N/A* (Inlined in   Internal Linkage
  Function**       min(int a, int b) { caller)             (Per-TU copy)
                   return a \&lt; b ?                      
                   a : b; }                                

  **Constant**     #define MAX_BUF     const int MAX_BUF = Compile-time
                   1024 or enum {      1024;               Constant
                   MAX_BUF = 1024 };                       
  -------------------------------------------------------------------------

### Makefile Automatic Variables \&amp; Syntax

# Target: Prerequisites

\# Recipe (Must be indented with TAB!)

\$@ \# The target file name being generated

\$\&lt; \# The FIRST prerequisite (usually source file)

\$\^ \# ALL prerequisites (separated by spaces)

\$? \# Prerequisites newer than the target

\# Automatic Dependency Generation (GCC/Clang)

CFLAGS += -MMD -MP

-include \$(DEPS)



\-\--

## 2. In-Depth Theory \&amp; Low-Level Mechanics

### A. How the Linker Works: Symbol Resolution \&amp; Relocation

When you compile a multi-file project with gcc -c main.c -o main.o and
gcc -c math.c -o math.o:

1.  **Unresolved References:** In main.o, calls to math_add() cannot
    know the actual memory address of math_add because math.c has not
    been linked yet. The compiler emits a placeholder address 0x00000000
    and adds an entry in the .rela.text section: *\&quot;Fix up call at
    offset 0x14 with symbol math_add\&quot;*.

2.  **Symbol Table (.symtab):** math.o exports a symbol entry: math_add
    marked as GLOBAL in its .text section.

3.  **Linker Stage (ld):** The linker reads all .o files, merges
    corresponding sections (.text with .text, .data with .data),
    computes final virtual addresses, and patches all placeholder
    offsets (**Relocation**).

 main.o Merged Executable (ELF):

┌─────────────────────────┐ ┌─────────────────────────┐

│ .text: │ │ .text: │

│ call 0x00000000 \[?\] │ ───┐ │ main() starts 0x401000 │

│ .rela.text: │ │ │ call 0x401120 ─────────┼──┐

│ Fixup: math_add @ 0x14 │ │ │ │ │

└─────────────────────────┘ │ Linker (ld) │ math_add() @ 0x401120 ◄┼──┘

math.o ├── Resolves Symbols │ │

┌─────────────────────────┐ │ \&amp; Relocates Addrs
└─────────────────────────┘

│ .text: │ │

│ math_add: \[machine code│ ───┘

│ .symtab: │

│ math_add (GLOBAL) │

└─────────────────────────┘



\-\--

### B. Strong vs Weak Symbols \&amp; The \&quot;Multiple Definition\&quot; Trap

In standard ELF object files:

- **Strong Symbol:** Functions and initialized global variables (int
  g_val = 10;).

- **Weak / Tentative Symbol:** Uninitialized global variables (int
  g_val; without extern).

**The Linker Conflict Rules:**

1.  Multiple strong symbols with the same identifier ⇒ **FATAL LINKER
    ERROR: multiple definition of \&apos;symbol\&apos;**.

2.  One strong symbol and multiple weak symbols ⇒ Linker chooses the
    strong symbol.

3.  Multiple weak symbols ⇒ Linker merges them into a single
    uninitialized BSS space.

**Crucial Takeaway:** If you write int config_timeout = 30; in a header
file config.h, every .c file that includes config.h generates a strong
symbol in its .o file. Linking them will always fail!

\-\--

### C. Header Hygiene \&amp; Include Guards

To prevent duplicate type definitions when headers include other
headers:

#ifndef MY_MODULE_H

#define MY_MODULE_H

// Declarations here\...

#endif // MY_MODULE_H

- **#pragma once vs Header Guards:** #pragma once is supported by
  virtually all modern compilers (GCC, Clang, MSVC) and avoids macro
  naming collisions, while traditional #ifndef guards remain strictly
  ISO C standard-compliant.

- **Forward Declarations:** If module_a.h only uses a pointer to struct
  Buffer, do **not** #include \&quot;buffer.h\&quot;. Instead, use a
  forward declaration:

struct Buffer; // Forward declaration

void process_buffer(struct Buffer \*buf);

This completely breaks circular dependency loops and drastically speeds
up compile times!

\-\--

## 3. Thoughtful Mini-Project (\~1 Hour Scope)

### Project Title: Production-Grade Multi-Module Build Architecture (make_sys)

#### Objective

Set up a modular, multi-file C architecture with proper header hygiene,
internal vs external symbols, automatic dependency tracking, and a
production-grade Makefile.

#### Project Directory Structure

project_root/

├── Makefile

├── include/

│ ├── common.h

│ ├── math_engine.h

│ └── logger.h

└── src/

├── math_engine.c

├── logger.c

└── main.c



#### 1. Header \&amp; Source Files

#### include/common.h

#ifndef COMMON_H

#define COMMON_H

#include \&lt;stdint.h\&gt;

#include \&lt;stdbool.h\&gt;

#include \&lt;stddef.h\&gt;

typedef enum {

STATUS_OK = 0,

STATUS_ERROR_INVALID_ARG = -1,

STATUS_ERROR_OVERFLOW = -2

} StatusCode;

#endif // COMMON_H



#### include/logger.h

#ifndef LOGGER_H

#define LOGGER_H

#include \&quot;common.h\&quot;

typedef enum {

LOG_LEVEL_DEBUG,

LOG_LEVEL_INFO,

LOG_LEVEL_WARN,

LOG_LEVEL_ERROR

} LogLevel;

void logger_init(LogLevel min_level);

void logger_log(LogLevel level, const char \*fmt, \...);

#endif // LOGGER_H



#### src/logger.c

#include \&quot;logger.h\&quot;

#include \&lt;stdio.h\&gt;

#include \&lt;stdarg.h\&gt;

// Static internal variable: Invisible outside this translation unit!

static LogLevel s_min_level = LOG_LEVEL_INFO;

void logger_init(LogLevel min_level) {

s_min_level = min_level;

}

void logger_log(LogLevel level, const char \*fmt, \...) {

if (level \&lt; s_min_level) return;

const char \*level_str = \&quot;INFO\&quot;;

if (level == LOG_LEVEL_DEBUG) level_str = \&quot;DEBUG\&quot;;

if (level == LOG_LEVEL_WARN) level_str = \&quot;WARN\&quot;;

if (level == LOG_LEVEL_ERROR) level_str = \&quot;ERROR\&quot;;

printf(\&quot;\[%s\] \&quot;, level_str);

va_list args;

va_start(args, fmt);

vprintf(fmt, args);

va_end(args);

putchar(\&apos;\\n\&apos;);

}



#### include/math_engine.h

#ifndef MATH_ENGINE_H

#define MATH_ENGINE_H

#include \&quot;common.h\&quot;

// Exported global variable declaration

extern uint64_t g_operation_count;

StatusCode math_safe_add(int32_t a, int32_t b, int32_t \*out_result);

StatusCode math_safe_mul(int32_t a, int32_t b, int32_t \*out_result);

#endif // MATH_ENGINE_H



#### src/math_engine.c

#include \&quot;math_engine.h\&quot;

#include \&lt;limits.h\&gt;

// Definition of exported global variable (Exactly ONCE in .c file!)

uint64_t g_operation_count = 0;

StatusCode math_safe_add(int32_t a, int32_t b, int32_t \*out_result) {

g_operation_count++;

if (!out_result) return STATUS_ERROR_INVALID_ARG;

if ((b \&gt; 0 \&amp;\&amp; a \&gt; INT32_MAX - b) \|\| (b \&lt; 0
\&amp;\&amp; a \&lt; INT32_MIN - b)) {

return STATUS_ERROR_OVERFLOW;

}

\*out_result = a + b;

return STATUS_OK;

}

StatusCode math_safe_mul(int32_t a, int32_t b, int32_t \*out_result) {

g_operation_count++;

if (!out_result) return STATUS_ERROR_INVALID_ARG;

int64_t prod = (int64_t)a \* (int64_t)b;

if (prod \&gt; INT32_MAX \|\| prod \&lt; INT32_MIN) {

return STATUS_ERROR_OVERFLOW;

}

\*out_result = (int32_t)prod;

return STATUS_OK;

}



#### src/main.c

#include \&quot;common.h\&quot;

#include \&quot;logger.h\&quot;

#include \&quot;math_engine.h\&quot;

#include \&lt;stdio.h\&gt;

int main(void) {

logger_init(LOG_LEVEL_DEBUG);

logger_log(LOG_LEVEL_INFO, \&quot;Multi-module application booted
successfully.\&quot;);

int32_t sum = 0;

StatusCode st = math_safe_add(1500000000, 1000000000, \&amp;sum);

if (st == STATUS_ERROR_OVERFLOW) {

logger_log(LOG_LEVEL_WARN, \&quot;Detected integer overflow during
addition!\&quot;);

} else {

logger_log(LOG_LEVEL_INFO, \&quot;Sum: %d\&quot;, sum);

}

int32_t prod = 0;

math_safe_mul(25, 4, \&amp;prod);

logger_log(LOG_LEVEL_INFO, \&quot;Product: %d\&quot;, prod);

logger_log(LOG_LEVEL_DEBUG, \&quot;Total Math Operations Tracked:
%llu\&quot;, (unsigned long long)g_operation_count);

return 0;

}



#### 2. The Production-Grade Makefile

# Compiler and Toolchain Definitions

CC := gcc

CFLAGS := -std=c17 -Wall -Wextra -Wpedantic -Wconversion -Werror
-D_GNU_SOURCE

CPPFLAGS := -Iinclude -MMD -MP \# Auto-generate header dependencies

LDFLAGS :=

LDLIBS :=

\# Build Mode: make DEBUG=1

ifeq (\$(DEBUG), 1)

CFLAGS += -g -O0 -fsanitize=address,undefined

else

CFLAGS += -O3 -DNDEBUG

endif

\# Directory Layout

SRC_DIR := src

BUILD_DIR := build

OBJ_DIR := \$(BUILD_DIR)/obj

BIN_DIR := \$(BUILD_DIR)/bin

TARGET := \$(BIN_DIR)/app

\# Locate all source files and map to object files

SRCS := \$(wildcard \$(SRC_DIR)/\*.c)

OBJS := \$(patsubst \$(SRC_DIR)/%.c, \$(OBJ_DIR)/%.o, \$(SRCS))

DEPS := \$(OBJS:.o=.d)

.PHONY: all clean run

all: \$(TARGET)

\# Link executable

\$(TARGET): \$(OBJS) \| \$(BIN_DIR)

\@echo \&quot;\[LINK\] \$@\&quot;

\$(CC) \$(CFLAGS) \$(LDFLAGS) \$\^ \$(LDLIBS) -o \$@

\# Compile Translation Units

\$(OBJ_DIR)/%.o: \$(SRC_DIR)/%.c \| \$(OBJ_DIR)

\@echo \&quot;\[CC\] \$\&lt;\&quot;

\$(CC) \$(CPPFLAGS) \$(CFLAGS) -c \$\&lt; -o \$@

\# Create Build Directories

\$(BIN_DIR) \$(OBJ_DIR):

\@mkdir -p \$@

\# Run Target

run: \$(TARGET)

@./\$(TARGET)

\# Clean Target

clean:

\@echo \&quot;\[CLEAN\] Removing \$(BUILD_DIR)\&quot;

\@rm -rf \$(BUILD_DIR)

\# Include automatically generated header dependencies

-include \$(DEPS)



\-\--

## 4. Error Handling \&amp; Defensive Programming Challenge

### Scenario: The Header Variable Definition Linker Collision

Examine the following buggy header file included across multiple .c
files in a large project:

// config.h

#ifndef CONFIG_H

#define CONFIG_H

// BUG 1: Initialized non-static variable defined inside a header!

int max_connection_retries = 5;

// BUG 2: Non-static function implementation inside a header!

int get_default_timeout(void) {

return 30;

}

#endif // CONFIG_H



### Analysis of Vulnerabilities:

1.  **Multiple Definition Linker Collision:** When config.h is included
    by client.c and server.c, both .o files emit strong symbols for
    max_connection_retries and get_default_timeout. The linker fails
    immediately:\<line-break/\>multiple definition of
    \&apos;max_connection_retries\&apos;; client.o: first defined here.

2.  **Include Guards Do NOT Prevent This:** Include guards only prevent
    duplicate inclusions **within the same translation unit**. They do
    nothing across different .c files.

### Defensive Fix:

// config.h (DEFENSIVE FIX)

#ifndef CONFIG_H

#define CONFIG_H

// Fix 1: Declare as \&apos;extern\&apos; in the header\...

extern int g_max_connection_retries;

// Fix 2: Inline functions in headers MUST be declared \&apos;static
inline\&apos;

static inline int get_default_timeout(void) {

return 30;

}

#endif // CONFIG_H



// config.c (EXACTLY ONCE IN A SOURCE FILE)

#include \&quot;config.h\&quot;

// Define the variable in exactly one source file:

int g_max_connection_retries = 5;

### 

### 

- 

#### 

#### 

#### 

#### 

#### 

#### 

### 

if ((b \> 0 && a \> INT32_MAX - b) \|\| (b \< 0 && a \< INT32_MIN - b))
{
