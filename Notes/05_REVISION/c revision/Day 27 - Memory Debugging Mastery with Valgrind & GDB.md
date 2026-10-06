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

### Compiler Flags for Deep Debugging

```bash
# Maximum debug symbols, zero optimization, preserved frame pointers
gcc -std=c17 -g3 -O0 -fno-omit-frame-pointer main.c -o app
```

### Essential GDB Command Matrix

| Command | Shorthand | Purpose / Mechanics |
| :--- | :--- | :--- |
| `run [args]` | `r` | Start execution with specified CLI arguments. |
| `break [loc]` | `b` | Set breakpoint at function name, line number, or address (`*0x401122`). |
| `watch [expr]` | `w` | Hardware watchpoint: interrupts CPU on memory write to address. |
| `rwatch [expr]` | `rw` | Hardware watchpoint: interrupts CPU on memory read from address. |
| `backtrace full`| `bt full` | Display complete stack frame trace including local variable values. |
| `print /x val` | `p /x` | Inspect variable or expression formatted as Hexadecimal. |
| `x/16xb ptr` | `x` | Examine raw memory: 16 hex bytes starting at pointer address `ptr`. |
| `next` / `step` | `n` / `s` | Step over next line / step into function call. |
| `continue` | `c` | Resume execution until next breakpoint or process termination. |

### The 4 Leak Categories Decoded

Valgrind Memcheck classifies unreferenced memory into 4 precise categories:

1. **Definitely Lost:** Serious bug. No pointers exist to the allocated block. Memory is completely unreachable and leaked.
2. **Indirectly Lost:** Memory pointed to by a block that is itself lost (e.g. child nodes of a lost root binary tree).
3. **Possibly Lost:** A pointer exists, but it points to the *middle* of the allocated block (an *interior pointer*), not the base header.
4. **Still Reachable:** Pointers still reference the memory on program exit (e.g. global caches not freed prior to `exit(0)`).

### Core Dump Post-Mortem Debugging

```bash
# 1. Enable core dumps in Linux shell
ulimit -c unlimited
# 2. Reproduce crash (generates 'core' or 'core.<pid>')
./app
# 3. Load core dump directly into GDB for instant crash site inspection
gdb ./app core
(gdb) bt
(gdb) info registers
```

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. How GDB Operates: Software Breakpoints & ptrace

When you set a breakpoint (`break main`):
1. GDB issues the Linux `ptrace(PTRACE_POKETEXT, pid, addr, ...)` system call.
2. It reads the original instruction opcode byte at that address and stores it in an internal table.
3. It overwrites that byte with `0xCC`, the x86 `INT 3` software interrupt opcode.
4. When the CPU hits `0xCC`, the kernel traps execution, raises `SIGTRAP`, halts the debugee, and notifies GDB.
5. To resume, GDB restores the original byte, single-steps the CPU, and re-inserts `0xCC`.

### B. How Valgrind Memcheck Works: Synthetic CPU & Shadow Bits

Valgrind does not run your program natively. It executes your binary inside a dynamic binary translation JIT engine (VEX) with a simulated synthetic CPU.

Memcheck maintains **Shadow Memory** tracking two bits for every single bit of RAM:
1. **A-bit (Addressability):** Has this byte been allocated via `malloc` or stack frame setup? If you read/write a byte with `A=0`, Memcheck raises `Invalid read/write of size X`.
2. **V-bit (Validity):** Does this bit contain initialized, meaningful data? When memory is allocated, `V=0`. Once written, `V=1`. Accessing `V=0` bits inside an arithmetic or branching expression raises `Conditional jump or move depends on uninitialised value(s)`.

### C. Heap Memory Profiling with Massif

Massif periodically samples heap memory allocations and writes snapshot files:

```bash
valgrind --tool=massif --pages-as-heap=yes ./app
ms_print massif.out.<pid>
```

Massif produces an ASCII memory visualizer displaying peak allocation spikes and stack trees responsible for RAM consumption.

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Custom Debug Memory Allocator & Leak Sentinel (`dbg_alloc`)

#### Objective

Build a drop-in debug memory allocator in pure C that wraps `malloc` and `free` with:
1. **Buffer Overrun / Underrun Protection:** Protects user memory using 64-bit redzone canaries (`0xDEADBEEFCAFEBABE`).
2. **Double Frees & Wild Frees:** Validates block registration in an internal hash/linked-list tracking registry.
3. **Memory Leaks:** Generates a detailed memory leak report on exit with file names and allocation line numbers.

#### Complete Implementation (`dbg_alloc.c`)

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
#define CANARY_PATTERN 0xDEADBEEFCAFEBABEU
typedef struct DebugBlock {
    uint64_t head_canary;
    size_t requested_size;
    const char *file;
    int line;
    struct DebugBlock *prev;
    struct DebugBlock *next;
} DebugBlock;
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
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Interior Pointer & "Possibly Lost" Trap

Examine the following string parser:

```c
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
    char *tok = extract_token("    Authorization: Bearer secret_99");
    printf("Token: %s\n", tok);
    free(tok); // CRASH: Passing interior pointer to free()
    return 0;
}
```

### Analysis of Vulnerabilities:

1. **Loss of Base Allocation Pointer:** In `extract_token`, `buf++` advances the pointer past leading whitespace. The original base address returned by `malloc` is permanently lost.
2. **Valgrind Flags:** Valgrind flags this block as *Possibly Lost* because a pointer exists into the interior of the buffer, but no pointer exists to byte 0.
3. **Heap Header Corruption:** Passing an interior pointer causes `free()` to look for chunk metadata before the token instead of before the actual block, resulting in instant crash (`SIGSEGV` or `free(): invalid pointer`).

### Defensive Fix:

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
```
