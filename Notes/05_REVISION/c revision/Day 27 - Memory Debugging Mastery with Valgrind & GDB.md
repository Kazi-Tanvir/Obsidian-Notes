---
tags:
  - c
  - memory-debugging
  - valgrind
  - gdb
  - core-dumps
  - heap-profiling
date: 2026-09-18
day: 27
---

# Day 27: Memory Debugging Mastery with Valgrind & GDB

---

## 1. Quick Reference & Cheat Sheet

---

### Compiler Flags for Deep Debugging

## Maximum debug symbols, zero optimization, preserved frame pointers

---

gcc -std=c17 -g3 -O0 -fno-omit-frame-pointer main.c -o app

### Essential GDB Command Matrix

----------------------------------------------------------------------------------------- Command           Shorthand         Description                       Example ----------------- ----------------- --------------------------------- ------------------- break [loc]     b                 Set breakpoint at line, function, b main.c:42 or b or address                        *0x4011a0

run [args]      r                 Start program execution with      r --config optional args                     app.conf

next              n                 Step over next line (does not     n enter functions)

step              s                 Step into function call           s

continue          c                 Resume execution until next       c breakpoint/signal

finish            fin               Execute until current function    fin returns

backtrace         bt                Print full call stack frames      bt full

frame [n]       f                 Switch to stack frame number n    f 2

print [expr]    p                 Evaluate and display variable or  p *my_ptr expression

examine           x                 Inspect raw memory at address     x/16xb ptr (x/[count][format][size])

watch [var]     wa                Hardware watchpoint: stop when    watch memory is modified                packet->checksum

rwatch [var]    rw                Hardware watchpoint: stop when    rwatch g_auth_token memory is read

info reg          i r               Display all CPU registers         info registers

layout src        tui               Toggle GDB Text User Interface    Ctrl + X, A (TUI split view) -----------------------------------------------------------------------------------------

### Valgrind Memcheck Reference

Run your program under Valgrind's synthetic CPU virtual machine:h\ valgrind --tool=memcheck\ --leak-check=full\ --show-leak-kinds=all\ --track-origins=yes\ --verbose\ ./app

##### The 4 Leak Categories Decoded

1\. **Definitely Lost:** Heap memory block that has **zero pointers** pointing to it anywhere in RAM or CPU registers. A true leak.

2\. **Indirectly Lost:** Heap memory pointed to **only** by another block that is *definitely lost* (e.g., child nodes in an orphaned linked list or binary tree).

3\. **Possibly Lost:** Memory where pointers point into the *middle* of the block rather than the start (an **interior pointer**).

4\. **Still Reachable:** Memory allocated and not freed before program exit, but pointers to it still exist (e.g. global caches).

#### Core Dump Post-Mortem Debugging

```bash

# 1. Enable core dumps in Linux shell

---

ulimit -c unlimited

# 2. Reproduce crash (generates 'core' or 'core.<pid>')

---

./app

# 3. Load core dump directly into GDB for instant crash site inspection

---

gdb ./app core

(gdb) bt

(gdb) info registers

# 2. In-Depth Theory & Low-Level Mechanics

---

## A. How GDB Operates: Software Breakpoints & ptrace

How can GDB freeze a running compiled C program at a precise machine
instruction?

1.  **The ptrace(2) System Call:**

- When you launch a program under GDB, GDB executes fork(), the child
  calls ptrace(PTRACE_TRACEME, \...), and then calls execve("./app").

- The Linux kernel grants the parent debugger full control to inspect
  and mutate the child's CPU registers and virtual memory space
  (PTRACE_PEEKTEXT, PTRACE_POKETEXT).

2.  **The INT 3 (0xCC) Opcode Swap:**

- When you type break main.c:20:

  a.  GDB determines the virtual memory address of that source line
      (e.g. 0x00401124).

  b.  GDB reads the original machine instruction byte at that address
      (e.g., 0x55 for push %rbp) and saves it in an internal table.

  c.  GDB overwrites that byte in the target process with 0xCC (the x86
      single-byte INT 3 instruction).

  d.  When the CPU hits 0xCC, it triggers an interrupt, stopping
      execution.

  e.  The kernel sends a SIGTRAP signal to the child process and halts
      it.

  f.  GDB wakes up, restores the original byte (0x55), steps back %rip
      by 1 byte, and yields control to the interactive prompt.

3.  **Hardware Watchpoints (Debug Registers):**

- Breakpoints halt at instructions; **watchpoints** halt on memory
  reads/writes.

- Instead of slowing down every instruction, x86-64 CPUs provide
  dedicated **Hardware Debug Registers (DR0 through DR3)**.

- GDB programs DR0 with the target variable's 64-bit physical address
  and sets flags in DR7 to monitor writes.

- When any CPU core executes a write instruction to that memory address,
  the hardware CPU itself generates an exception before committing the
  write, allowing GDB to intercept it with zero execution overhead!

## B. Inside Valgrind: Dynamic Binary Instrumentation (DBI)

Valgrind **does not run your program directly on physical hardware**. It
is a Just-In-Time (JIT) compiler and virtual machine:

1.  It translates x86 machine code into an architecture-neutral
    Intermediate Representation (**VEX IR**).

2.  It injects instrumentation code into the IR.

3.  It re-compiles the instrumented IR back into native machine code and
    executes it on a synthetic CPU.

### Shadow Memory: A-Bits and V-Bits

For every single byte and bit in your application's address space,
Valgrind maintains two sets of shadow metadata:

- **A-Bits (Addressability):** 1 bit per byte of memory. Tells whether
  the program has legally allocated that memory (stack, heap chunk,
  global data). If you read/write where the A-bit is 0, it triggers an
  **Invalid read / write**.

- **V-Bits (Validity):** 1 bit per bit of data. Tells whether that bit
  contains meaningful, initialized data.

  - When malloc(100) is called, all 100 bytes have A-bits = 1 (valid
    address), but V-bits = 0 (uninitialized data!).

  - Performing arithmetic on uninitialized data simply propagates V-bits
    = 0.

  - The error is triggered only when an uninitialized bit is used in a
    **semantic decision**, such as a conditional jump.

## C. Heap Profiling with Massif

To diagnose memory bloat and peak memory consumption over time:valgrind
--tool=massif --time-unit=B ./app

ms_print massif.out.<pid>

Massif periodically samples the heap and generates an ASCII memory
profile graph displaying allocation spikes, call-graph trees, and exact
allocation sites responsible for peak RAM consumption.

# 3. Thoughtful Mini-Project (~1 Hour Scope)

---

## Project Title: Custom Debug Memory Allocator & Leak Sentinel (dbg_malloc)

### Objective

Build a drop-in debug memory allocator in pure C that wraps malloc,
calloc, realloc, and free. The system detects:

1.  **Buffer Overruns / Underruns:** Protects user memory using 64-bit
    redzone canaries (0xDEADBEEFCAFEBABE).

2.  **Double Frees & Wild Frees:** Validates block registration in an
    internal doubly-linked tracker.

3.  **Memory Leaks:** Generates a detailed memory leak report on exit
    with file name, line number, and un-freed byte sizes.

### Complete Implementation (dbg_alloc.c)

```c
#include <stdio.h>
```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
char *extract_token(const char *input) {
    char *buf = (char *)malloc(strlen(input) + 1);
    if (!buf) return NULL;
    strcpy(buf, input);
    while (isspace((unsigned char)*buf)) {
        buf++; // FATAL BUG: Base pointer lost!
    }
    return buf;
}
int main(void) {
    char *tok = extract_token("    Authorization: Bearer secret_99");
    printf("Token: %s\n", tok);
    free(tok); // CRASH: Passing interior pointer to free()
    return 0;
}
``` DebugBlock;
#define GET_TAIL_CANARY(block) \
    ((uint64_t *)((uint8_t *)(block + 1) + (block)->requested_size))
static DebugBlock *g_head = NULL;
static size_t g_total_allocated = 0;
static size_t g_current_allocated = 0;
void *dbg_malloc_internal(size_t size, const char *file, int line) {
    if (size == 0) size = 1;
    size_t total_size = sizeof(DebugBlock) + size + sizeof(uint64_t);
    uint8_t *raw = (uint8_t *)malloc(total_size);
    if (!raw) return NULL;
    DebugBlock *block = (DebugBlock *)raw;
    block->head_canary = CANARY_PATTERN;
    block->requested_size = size;
    block->file = file;
    block->line = line;
    uint64_t *tail = GET_TAIL_CANARY(block);
    *tail = CANARY_PATTERN;
    block->prev = NULL;
    block->next = g_head;
    if (g_head) g_head->prev = block;
    g_head = block;
    g_total_allocated += size;
    g_current_allocated += size;
    return (void *)(block + 1);
}
void dbg_free_internal(void *ptr, const char *file, int line) {
    if (!ptr) return;
    DebugBlock *block = ((DebugBlock *)ptr) - 1;
    DebugBlock *curr = g_head;
    bool found = false;
    while (curr) {
        if (curr == block) { found = true; break; }
        curr = curr->next;
    }
    if (!found) {
        fprintf(stderr, "\n[CRITICAL MEMORY FAULT] Invalid or Double Free at %s:%d!\n", file, line);
        abort();
    }
    if (block->head_canary != CANARY_PATTERN || *GET_TAIL_CANARY(block) != CANARY_PATTERN) {
        fprintf(stderr, "\n[CRITICAL MEMORY FAULT] Corruption detected at %s:%d!\n", file, line);
        abort();
    }
    if (block->prev) block->prev->next = block->next;
    if (block->next) block->next->prev = block->prev;
    if (g_head == block) g_head = block->next;
    g_current_allocated -= block->requested_size;
    memset(block, 0x55, sizeof(DebugBlock) + block->requested_size + sizeof(uint64_t));
    free(block);
}
void dbg_print_leak_report(void) {
    printf("\n=======================================================\n");
    printf("            DEBUG HEAP ALLOCATION REPORT               \n");
    printf("=======================================================\n");
    if (g_head == NULL) {
        printf("  STATUS: CLEAN! Zero memory leaks detected.\n");
        return;
    }
    printf("  STATUS: LEAKS DETECTED!\n");
    DebugBlock *curr = g_head;
    while (curr) {
        printf("  [Leak] Address: %p | Size: %zu | Allocated at: %s:%d\n",
               (void *)(curr + 1), curr->requested_size, curr->file, curr->line);
        curr = curr->next;
    }
    printf("=======================================================\n");
}
#define malloc(sz) dbg_malloc_internal(sz, __FILE__, __LINE__)
#define free(p) dbg_free_internal(p, __FILE__, __LINE__)
int main(void) {
    printf("=== Starting Custom Debug Allocator Suite ===\n\n");
    char *clean_buf = (char *)malloc(32);
    strcpy(clean_buf, "Secure Data 2026");
    free(clean_buf);
    int *leaked_array = (int *)malloc(10 * sizeof(int));
    dbg_print_leak_report();
    free(leaked_array);
    return 0;
}
``` DebugBlock;

#define GET_TAIL_CANARY(block) 

((uint64_t *)((uint8_t *)(block + 1) + (block)->requested_size))

static DebugBlock *g_head = NULL;

static size_t g_total_allocated = 0;

static size_t g_current_allocated = 0;

void *dbg_malloc_internal(size_t size, const char *file, int line) {

if (size == 0) size = 1;

size_t total_size = sizeof(DebugBlock) + size + sizeof(uint64_t);

uint8_t *raw = (uint8_t *)malloc(total_size);

if (!raw) return NULL;

DebugBlock *block = (DebugBlock *)raw;

block->head_canary = CANARY_PATTERN;

block->requested_size = size;

block->file = file;

block->line = line;

uint64_t *tail = GET_TAIL_CANARY(block);

*tail = CANARY_PATTERN;

block->prev = NULL;

block->next = g_head;

if (g_head) g_head->prev = block;

g_head = block;

g_total_allocated += size;

g_current_allocated += size;

return (void *)(block + 1);

}

void dbg_free_internal(void *ptr, const char *file, int line) {

if (!ptr) return;

DebugBlock *block = ((DebugBlock *)ptr) - 1;

DebugBlock *curr = g_head;

bool found = false;

while (curr) {

if (curr == block) { found = true; break; }

curr = curr->next;

}

if (!found) {

fprintf(stderr, "\\n[CRITICAL MEMORY FAULT] Invalid or Double Free at
%s:%d!\\n", file, line);

abort();

}

if (block->head_canary != CANARY_PATTERN || *GET_TAIL_CANARY(block)
!= CANARY_PATTERN) {

fprintf(stderr, "\\n[CRITICAL MEMORY FAULT] Corruption detected at
%s:%d!\\n", file, line);

abort();

}

if (block->prev) block->prev->next = block->next;

if (block->next) block->next->prev = block->prev;

if (g_head == block) g_head = block->next;

g_current_allocated -= block->requested_size;

memset(block, 0x55, sizeof(DebugBlock) + block->requested_size +
sizeof(uint64_t));

free(block);

}

void dbg_print_leak_report(void) {

printf("\\n=======================================================\\n");

printf(" DEBUG HEAP ALLOCATION REPORT \\n");

printf("=======================================================\\n");

if (g_head == NULL) {

printf(" STATUS: CLEAN! Zero memory leaks detected.\\n");

return;

}

printf(" STATUS: LEAKS DETECTED!\\n");

DebugBlock *curr = g_head;

while (curr) {

printf(" [Leak] Address: %p | Size: %zu | Allocated at: %s:%d\\n",

(void *)(curr + 1), curr->requested_size, curr->file, curr->line);

curr = curr->next;

}

printf("=======================================================\\n");

}

#define malloc(sz) dbg_malloc_internal(sz, __FILE__, __LINE__)

#define free(p) dbg_free_internal(p, __FILE__, __LINE__)

int main(void) {

printf("=== Starting Custom Debug Allocator Suite ===\\n\\n");

char *clean_buf = (char *)malloc(32);

strcpy(clean_buf, "Secure Data 2026");

free(clean_buf);

int *leaked_array = (int *)malloc(10 * sizeof(int));

dbg_print_leak_report();

free(leaked_array);

return 0;

}

# 4. Error Handling & Defensive Programming Challenge

---

## Scenario: The Interior Pointer & "Possibly Lost" Trap

Examine the following string parser:#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <ctype.h>

char *extract_token(const char *input) {

char *buf = (char *)malloc(strlen(input) + 1);

if (!buf) return NULL;

strcpy(buf, input);

while (isspace((unsigned char)*buf)) {

buf++; // FATAL BUG: Base pointer lost!

}

return buf;

}

int main(void) {

char *tok = extract_token(" Authorization: Bearer secret_99");

printf("Token: %s\\n", tok);

free(tok); // CRASH: Passing interior pointer to free()

return 0;

}

## Analysis of Vulnerabilities

1.  **Loss of Base Allocation Pointer:** In extract_token, buf++
    advances the pointer past leading spaces. The original base address
    returned by malloc is permanently discarded.

2.  **Valgrind Flags:** Valgrind flags this block as Possibly Lost
    because an interior pointer exists but the start of the block is no
    longer reachable.

3.  **Heap Header Corruption:** Passing an interior pointer causes
    free() to read random payload data as heap metadata, causing an
    immediate abort.

## Defensive Fix

```c
typedef struct {
    char *base_ptr;      
    const char *start;   
    size_t length;
} TokenSlice;
TokenSlice extract_token_safe(const char *input) {
    TokenSlice slice = {0};
    if (!input) return slice;
    slice.base_ptr = (char *)malloc(strlen(input) + 1);
    if (!slice.base_ptr) return slice;
    strcpy(slice.base_ptr, input);
    const char *p = slice.base_ptr;
    while (isspace((unsigned char)*p)) p++;
    slice.start = p;
    slice.length = strlen(p);
    return slice;
}
void token_slice_destroy(TokenSlice *slice) {
    if (slice && slice->base_ptr) {
        free(slice->base_ptr); 
        slice->base_ptr = NULL;
    }
}
``` TokenSlice;

TokenSlice extract_token_safe(const char *input) {

TokenSlice slice = {0};

if (!input) return slice;

slice.base_ptr = (char *)malloc(strlen(input) + 1);

if (!slice.base_ptr) return slice;

strcpy(slice.base_ptr, input);

const char *p = slice.base_ptr;

while (isspace((unsigned char)*p)) p++;

slice.start = p;

slice.length = strlen(p);

return slice;

}

void token_slice_destroy(TokenSlice *slice) {

if (slice && slice->base_ptr) {

free(slice->base_ptr);

slice->base_ptr = NULL;

}

}
