\-\--

tags:

\- c

\- memory-layout

\- stack-frame

\- call-stack

\- bss-data-text

\- activation-records

date: 2026-08-27

day: 5

\-\--

\# Day 5: Memory Layout of a C Program, Stack Frames & Segments

\-\--

\## 1. Quick Reference & Cheat Sheet

\### Virtual Memory Address Space Layout (Linux x86_64)

\`\`\`text

High Memory (0x7FFF_FFFF_FFFF)

┌────────────────────────────────────────────────────────┐

│ Kernel Space (Protected, inaccessible to user code) │

├────────────────────────────────────────────────────────┤

│ Stack Segment (Grows DOWNWARDS towards lower memory) │

│ - Local variables, activation records, return addrs │

│ │ │

│ ▼ │

├────────────────────────────────────────────────────────┤

│ Memory Mapping Segment (Shared libs, mmap files) │

├────────────────────────────────────────────────────────┤

│ ▲ │

│ │ │

│ Heap Segment (Grows UPWARDS via brk / sbrk / mmap) │

│ - Dynamic allocations (malloc, calloc, realloc) │

├────────────────────────────────────────────────────────┤

│ BSS Segment (Uninitialized / 0-initialized globals) │

├────────────────────────────────────────────────────────┤

│ Data Segment (Initialized non-zero globals & statics) │

├────────────────────────────────────────────────────────┤

│ Text / Code Segment (.text, .rodata) \[Read-Only, Exec\] │

└────────────────────────────────────────────────────────┘

Low Memory (0x0000_0000_0000 - NULL pointer trap area)

\`\`\`

\### Memory Segments Summary

\| Segment \| Content \| Permissions \| Lifetime \| Binary Footprint \|

\| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \|

\| \*\*\`.text\`\*\* \| Machine code instructions \| Read-Only, Executable (\`r-x\`) \| Program runtime \| Stored in ELF binary file \|

\| \*\*\`.rodata\`\*\*\| String literals, \`const\` globals \| Read-Only (\`r\--\`) \| Program runtime \| Stored in ELF binary file \|

\| \*\*\`.data\`\*\* \| Initialized non-zero global/static variables \| Read/Write (\`rw-\`) \| Program runtime \| Stored in ELF binary file \|

\| \*\*\`.bss\`\*\* \| Uninitialized or zero-initialized globals/statics \| Read/Write (\`rw-\`) \| Program runtime \| \*\*0 bytes\*\* in binary (only records size in ELF header; kernel zeroes at load) \|

\| \*\*Heap\*\* \| Dynamic memory (\`malloc\`, \`calloc\`) \| Read/Write (\`rw-\`) \| Until \`free()\` or exit \| Allocated at runtime \|

\| \*\*Stack\*\* \| Function frames, local variables, parameters \| Read/Write (\`rw-\`) \| Function execution \| Allocated dynamically by CPU \`\$rsp\` pointer \|

\-\--

\## 2. In-Depth Theory & Low-Level Mechanics

\### A. The Anatomy of a Stack Frame (Activation Record)

Each time a function is invoked in C, a new \*\*Stack Frame\*\* is pushed onto the stack. On x86_64 (System V AMD64 ABI):

1\. \*\*Parameter Passing:\*\* The first 6 integer/pointer arguments are passed in registers (\`rdi\`, \`rsi\`, \`rdx\`, \`rcx\`, \`r8\`, \`r9\`). Any additional arguments are pushed onto the caller\'s stack in reverse order.

2\. \*\*\`call\` Instruction:\*\* Pushes the 64-bit Return Address (instruction pointer \`\$rip\` of the caller) onto the stack and jumps to the callee.

3\. \*\*Function Prologue:\*\*

\`\`\`nasm

push rbp ; Save caller\'s base pointer

mov rbp, rsp ; Establish new base pointer for current frame

sub rsp, 32 ; Allocate 32 bytes on stack for local variables

\`\`\`

4\. \*\*Function Epilogue:\*\*

\`\`\`nasm

mov rsp, rbp ; Deallocate local variables

pop rbp ; Restore caller\'s base pointer

ret ; Pop return address into \$rip and jump back

\`\`\`

\`\`\`text

Stack Frame Layout:

High Addresses

┌──────────────────────────────┐

│ Function Arguments (7th+) │

├──────────────────────────────┤

│ Return Address (Saved \$rip) │ \<\-- Pushed by \'call\'

├──────────────────────────────┤

│ Saved Frame Pointer (\$rbp) │ \<\-- Base of current frame

├──────────────────────────────┤

│ Local Variables & Arrays │

│ (e.g. char buf\[16\], int x) │

├──────────────────────────────┤

│ Saved Registers (rbx, r12..) │

└──────────────────────────────┘ \<\-- Current Stack Pointer (\$rsp)

Low Addresses

\`\`\`

\-\--

\### B. Deep Recursion & Stack Overflow Dynamics

The OS allocates a fixed stack size per process (typically \*\*8 MB\*\* on Linux, checkable via \`ulimit -s\`).

\* Each recursive call consumes stack space for return address, frame pointer, parameters, and local variables.

\* When recursive depth exhausts available stack memory, the stack pointer \`\$rsp\` collides with the guard page at the boundary of the stack segment, triggering an unrecoverable \*\*Segmentation Fault (\`SIGSEGV\`)\*\*.

\#### Tail Call Optimization (TCO):

When a recursive call is in the \*\*tail position\*\* (i.e. the function simply returns the result of the recursive call without further arithmetic), modern compilers with \`-O2\` replace the \`call\` with a \`jmp\`, reusing the existing stack frame and executing in \$O(1)\$ stack space.

\`\`\`c

// Non-tail recursive: Cannot be optimized without frame reuse

uint64_t factorial(uint64_t n) {

if (n \<= 1) return 1;

return n \* factorial(n - 1); // Must wait for result before multiplying

}

// Tail recursive: Optimizes to an in-place loop with 0 additional stack frames

uint64_t factorial_tail(uint64_t n, uint64_t accumulator) {

if (n \<= 1) return accumulator;

return factorial_tail(n - 1, n \* accumulator); // Tail call!

}

\`\`\`

\-\--

\## 3. Thoughtful Mini-Project (\~1 Hour Scope)

\### Project Title: Runtime Virtual Memory Layout & Stack Dynamics Probe (\`mem_layout_probe\`)

\#### Objective

Write a modular C introspection utility that maps its own memory layout at runtime by printing pointer addresses across different memory segments and dynamically measures stack frame consumption per recursive call.

\#### Functional Requirements

1\. \*\*Segment Address Map:\*\*

\* Print addresses of functions in \`.text\`

\* Print addresses of string literals in \`.rodata\`

\* Print addresses of initialized globals in \`.data\`

\* Print addresses of uninitialized statics in \`.bss\`

\* Print addresses of dynamically allocated buffers in \`Heap\`

\* Print addresses of stack variables in \`Stack\`

2\. \*\*Stack Growth & Frame Size Probe:\*\*

\* Implement a recursive function \`probe_stack(int depth, uintptr_t prev_addr)\` that tracks address differences between stack frames across 5 invocation levels.

\* Dynamically calculate and display the direction of stack growth (Downwards towards lower memory vs Upwards).

\* Calculate average stack frame overhead in bytes.

\#### Complete Starter Code Implementation

\`\`\`c

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

// Global Segment Variables

const char \*rodata_str = \"Read-Only String Literal (.rodata)\";

int initialized_global = 0x12345678; // .data

int uninitialized_global; // .bss

static int static_zero_global = 0; // .bss

void dummy_function(void) {

// .text reference

}

void probe_stack_growth(int depth, uintptr_t prev_stack_addr) {

int local_var = depth;

uintptr_t current_stack_addr = (uintptr_t)&local_var;

printf(\" \[Frame %d\] Local variable at: %p\", depth, (void \*)current_stack_addr);

if (prev_stack_addr != 0) {

ptrdiff_t diff = (ptrdiff_t)(current_stack_addr - prev_stack_addr);

printf(\" \| Delta: %+td bytes (%s)\",

diff,

diff \< 0 ? \"Growing Downward\" : \"Growing Upward\");

}

printf(\"\\n\");

if (depth \< 4) {

probe_stack_growth(depth + 1, current_stack_addr);

}

}

int main(void) {

int main_local_stack = 42;

int \*heap_alloc_1 = (int \*)malloc(sizeof(int) \* 64);

int \*heap_alloc_2 = (int \*)malloc(sizeof(int) \* 1024);

if (!heap_alloc_1 \|\| !heap_alloc_2) {

fprintf(stderr, \"Heap allocation failed!\\n\");

return 1;

}

printf(\"========================================================\\n\");

printf(\" C RUNTIME MEMORY SEGMENT INSPECTOR \\n\");

printf(\"========================================================\\n\\n\");

printf(\"\[1\] .text Segment (Code / Instructions):\\n\");

printf(\" main() function address: %p\\n\", (void \*)(uintptr_t)main);

printf(\" dummy_function() address: %p\\n\\n\", (void \*)(uintptr_t)dummy_function);

printf(\"\[2\] .rodata Segment (Read-Only Data):\\n\");

printf(\" String literal pointer: %p\\n\\n\", (void \*)rodata_str);

printf(\"\[3\] .data Segment (Initialized Globals):\\n\");

printf(\" initialized_global address: %p\\n\\n\", (void \*)&initialized_global);

printf(\"\[4\] .bss Segment (Uninitialized / Zero Globals):\\n\");

printf(\" uninitialized_global address: %p\\n\", (void \*)&uninitialized_global);

printf(\" static_zero_global address: %p\\n\\n\", (void \*)&static_zero_global);

printf(\"\[5\] Heap Segment (Dynamic Allocations):\\n\");

printf(\" Heap chunk 1 (256 B): %p\\n\", (void \*)heap_alloc_1);

printf(\" Heap chunk 2 (4096 B): %p\\n\", (void \*)heap_alloc_2);

printf(\" Heap Growth Delta: %+td bytes\\n\\n\",

(ptrdiff_t)((uintptr_t)heap_alloc_2 - (uintptr_t)heap_alloc_1));

printf(\"\[6\] Stack Segment (Activation Records & Local Vars):\\n\");

printf(\" main() local variable: %p\\n\\n\", (void \*)&main_local_stack);

printf(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\\n\");

printf(\" STACK FRAME DYNAMICS & RECURSION PROBE \\n\");

printf(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\\n\");

probe_stack_growth(1, (uintptr_t)&main_local_stack);

free(heap_alloc_1);

free(heap_alloc_2);

return 0;

}

\`\`\`

\-\--

\## 4. Error Handling & Defensive Programming Challenge

\### Scenario: The Unbounded Stack Allocation (VLA) Crash Vulnerability

Examine the following file processing function written using Variable Length Arrays (VLAs):

\`\`\`c

#include \<stdio.h\>

#include \<string.h\>

// BUGGY IMPLEMENTATION

void process_network_payload(const char \*raw_data, size_t data_len) {

// VULNERABILITY: Variable Length Array (VLA) allocated on the STACK based on untrusted input length.

// If an attacker sends data_len = 10 \* 1024 \* 1024 (10 MB), the stack (8 MB max) instantly overflows,

// crashing the program without any opportunity to catch an error or return NULL!

char local_buffer\[data_len + 1\];

memcpy(local_buffer, raw_data, data_len);

local_buffer\[data_len\] = \'\\0\';

printf(\"Processed payload safely: %s\\n\", local_buffer);

}

\`\`\`

\### Analysis of Vulnerabilities:

1\. \*\*Unchecked Stack Growth via VLAs:\*\* Unlike \`malloc()\`, which returns \`NULL\` on failure, stack allocations adjust \`\$rsp\` directly without runtime bounds checking. Allocating an unbounded VLA on the stack bypasses stack guards and immediately triggers a segmentation fault or security compromise.

2\. \*\*VLA Portability & Safety:\*\* In ISO C11, Variable Length Arrays were made optional (\`\_\_STDC_NO_VLA\_\_\`) and are banned in the Linux Kernel due to stack exhaustion risks.

\### Defensive Fix (Dual-Strategy Stack Cache with Heap Fallback):

\`\`\`c

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<string.h\>

#include \<stdbool.h\>

#define STACK_THRESHOLD_BYTES 1024U // Safe fixed size for stack allocation

#define MAX_PAYLOAD_LIMIT (4U \* 1024U \* 1024U) // 4 MB hard safety ceiling

bool process_network_payload_safe(const char \*raw_data, size_t data_len) {

if (raw_data == NULL \|\| data_len == 0) {

return false;

}

if (data_len \> MAX_PAYLOAD_LIMIT) {

fprintf(stderr, \"Defensive Error: Payload size (%zu bytes) exceeds maximum limit (%u bytes)\\n\",

data_len, MAX_PAYLOAD_LIMIT);

return false;

}

char stack_buffer\[STACK_THRESHOLD_BYTES\];

char \*working_buffer = NULL;

bool is_heap_allocated = false;

// Fast path: Use pre-allocated safe stack buffer if within threshold

if (data_len + 1 \<= STACK_THRESHOLD_BYTES) {

working_buffer = stack_buffer;

} else {

// Slow path: Dynamically allocate on heap if size is large

working_buffer = (char \*)malloc(data_len + 1);

if (working_buffer == NULL) {

fprintf(stderr, \"Defensive Error: Failed to allocate %zu bytes on heap\\n\", data_len + 1);

return false;

}

is_heap_allocated = true;

}

memcpy(working_buffer, raw_data, data_len);

working_buffer\[data_len\] = \'\\0\';

printf(\"Successfully processed %zu bytes of payload.\\n\", data_len);

// Guaranteed cleanup

if (is_heap_allocated) {

free(working_buffer);

working_buffer = NULL;

}

return true;

}

\`\`\`
