\-\--

tags:

\- c

\- dynamic-memory

\- malloc-calloc-realloc-free

\- heap-internals

\- memory-fragmentation

\- defensive-allocation

date: 2026-08-31

day: 9

\-\--

\# Day 9: Dynamic Memory Allocation Mechanics, Heap Metadata, Fragmentation & Safe Reallocation

\-\--

\## 1. Quick Reference & Cheat Sheet

\### Dynamic Memory Allocation Functions (\`\<stdlib.h\>\`)

\| Function \| Prototype \| Description \| Return Value on Failure \|

\| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \|

\| \`malloc\` \| \`void \*malloc(size_t size);\` \| Allocates \`size\` uninitialized bytes on heap. \| \`NULL\` \|

\| \`calloc\` \| \`void \*calloc(size_t num, size_t size);\` \| Allocates and \*\*zero-initializes\*\* memory for \`num\` items of \`size\` bytes. Built-in multiplication overflow check. \| \`NULL\` \|

\| \`realloc\` \| \`void \*realloc(void \*ptr, size_t new_size);\` \| Resizes existing block. Copies existing data. May move block to new address. \| \`NULL\` (Original block \*\*remains valid\*\*) \|

\| \`free\` \| \`void free(void \*ptr);\` \| Releases memory block back to the allocator. \`free(NULL)\` is a safe no-op. \| \`void\` \|

\### Critical Golden Rules for Dynamic Memory

1\. \*\*Always Check for \`NULL\`:\*\* Every allocation call can fail if the operating system is out of memory or address space.

2\. \*\*Never Direct-Assign \`realloc\`:\*\*

\`\`\`c

// FATAL BUG: If realloc fails, ptr is overwritten with NULL, leaking the original block!

ptr = realloc(ptr, new_size);

// CORRECT IDIOM:

void \*temp = realloc(ptr, new_size);

if (!temp) {

// Handle out-of-memory error; original \'ptr\' is still valid and must be preserved/freed

} else {

ptr = temp;

}

\`\`\`

3\. \*\*Pointer Poisoning:\*\* Set pointers to \`NULL\` immediately after \`free()\` to prevent \*\*Use-After-Free (UAF)\*\* and \*\*Double-Free\*\* vulnerabilities.

4\. \*\*Exact Base Pointers:\*\* Never pass an interior pointer offset (e.g. \`free(ptr + 2)\`) or stack/static address to \`free()\`.

\-\--

\## 2. In-Depth Theory & Low-Level Mechanics

\### A. How Allocators Work Internally (\`ptmalloc\` / \`dlmalloc\`)

When you request memory via \`malloc(32)\`, the memory allocator does not ask the operating system for exactly 32 bytes. Instead, it reserves an aligned chunk consisting of \*\*Chunk Metadata (Header)\*\* followed by the \*\*User Payload\*\*.

\`\`\`text

Physical Memory Layout of an Allocated Chunk (x86_64, 16-byte alignment):

┌──────────────────────────────────────────────────────────────────┐

│ Prev Chunk Size (8 Bytes) - Used when previous chunk is FREE │

├──────────────────────────────────────────────────────────────────┤

│ Chunk Size & Flags (8 Bytes) │

│ - Size of this chunk (including headers & padding) │

│ - Bit 0: PREV_INUSE (1 if previous physical chunk is allocated) │

│ - Bit 1: IS_MMAPPED (1 if allocated via mmap) │

├──────────────────────────────────────────────────────────────────┤ ◄── Pointer returned by malloc()

│ │

│ User Payload Area (Requested size, e.g., 32 Bytes) │

│ │

├──────────────────────────────────────────────────────────────────┤

│ Padding / Alignment Bytes (to satisfy 16-byte boundary) │

└──────────────────────────────────────────────────────────────────┘

\`\`\`

\#### System Call Interfaces:

\* \*\*\`brk\` / \`sbrk\`:\*\* Used for small to medium allocations. Adjusts the process \"program break\" address, growing the contiguous heap segment upwards.

\* \*\*\`mmap\` / \`munmap\`:\*\* Used for large allocations (typically \$\\ge 128\\text{ KB}\$). Requests independent, anonymous virtual memory pages directly from the kernel. When freed, memory is immediately returned to the OS.

\-\--

\### B. Internal vs External Fragmentation

1\. \*\*Internal Fragmentation:\*\* Memory wasted inside an allocated chunk because the allocator rounds up requests to fixed alignment boundaries (e.g. requesting 5 bytes allocates a minimum chunk of 24 or 32 bytes).

2\. \*\*External Fragmentation:\*\* Total free memory in the heap is sufficient to satisfy an allocation request, but the free memory is split into small, non-contiguous blocks surrounded by active allocations.

\`\`\`text

Heap Address Space:

┌──────────┬──────────┬──────────┬──────────┬──────────┐

│ Allocated│ Free │ Allocated│ Free │ Allocated│

│ 16 KB │ 8 KB │ 32 KB │ 8 KB │ 16 KB │

└──────────┴──────────┴──────────┴──────────┴──────────┘

Total Free Memory = 16 KB (8 KB + 8 KB).

A request for malloc(12 KB) FAILS because there is no single contiguous 12 KB block!

\`\`\`

\-\--

\### C. \`realloc\` Mechanics & In-Place Growth

When resizing memory via \`realloc(ptr, new_size)\`:

1\. \*\*Shrink in Place:\*\* If \`new_size \< old_size\`, the allocator may split the chunk, mark the remainder as a free chunk, and return the same \`ptr\`.

2\. \*\*Expand in Place:\*\* If \`new_size \> old_size\` and the physically adjacent chunk in memory is free and large enough, the allocator merges them and returns the same \`ptr\`.

3\. \*\*Relocate & Copy:\*\* If adjacent space is unavailable, the allocator allocates a new chunk elsewhere on the heap, executes \`memcpy(new_ptr, old_ptr, old_size)\`, automatically frees \`old_ptr\`, and returns \`new_ptr\`.

\-\--

\## 3. Thoughtful Mini-Project (\~1 Hour Scope)

\### Project Title: Debugging Memory Allocator & Leak Detector Wrapper (\`memguard\`)

\#### Objective

Build a lightweight memory safety wrapper in C that tracks all active heap allocations, detects buffer overflows/underflows via boundary canaries, prevents double-free errors, and generates an allocation leak report on exit.

\#### Architectural Design

Every allocation wraps user memory with a \`GuardHeader\` and a trailing \`GuardTrailer\`:

\`\`\`text

┌──────────────────────────────┬──────────────────────────┬──────────────────────────────┐

│ GuardHeader (Metadata) │ User Payload Buffer │ GuardTrailer (Canary) │

│ Magic: 0xDEADBEEF │ (Requested Size Bytes) │ Magic: 0xCAFEBABE │

└──────────────────────────────┴──────────────────────────┴──────────────────────────────┘

\`\`\`

\#### Complete Starter Code Implementation

\`\`\`c

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<string.h\>

#include \<assert.h\>

#define CANARY_START 0xDEADBEEFU

#define CANARY_END 0xCAFEBABEU

typedef struct GuardHeader {

uint32_t magic_start;

size_t payload_size;

const char \*file;

int line;

struct GuardHeader \*prev;

struct GuardHeader \*next;

} GuardHeader;

typedef struct {

uint32_t magic_end;

} GuardTrailer;

static GuardHeader \*g_alloc_list_head = NULL;

static size_t g_total_allocated_bytes = 0;

static size_t g_active_allocations_count = 0;

void \*memguard_malloc_internal(size_t size, const char \*file, int line) {

if (size == 0) return NULL;

size_t total_size = sizeof(GuardHeader) + size + sizeof(GuardTrailer);

uint8_t \*raw = (uint8_t \*)malloc(total_size);

if (!raw) return NULL;

GuardHeader \*hdr = (GuardHeader \*)raw;

hdr-\>magic_start = CANARY_START;

hdr-\>payload_size = size;

hdr-\>file = file;

hdr-\>line = line;

hdr-\>prev = NULL;

hdr-\>next = g_alloc_list_head;

if (g_alloc_list_head) {

g_alloc_list_head-\>prev = hdr;

}

g_alloc_list_head = hdr;

uint8_t \*payload = raw + sizeof(GuardHeader);

GuardTrailer \*trailer = (GuardTrailer \*)(payload + size);

trailer-\>magic_end = CANARY_END;

g_total_allocated_bytes += size;

g_active_allocations_count++;

return (void \*)payload;

}

void memguard_free_internal(void \*ptr, const char \*file, int line) {

if (!ptr) return;

uint8_t \*raw = (uint8_t \*)ptr - sizeof(GuardHeader);

GuardHeader \*hdr = (GuardHeader \*)raw;

// Check Underflow Canary

if (hdr-\>magic_start != CANARY_START) {

fprintf(stderr, \"\[MEMGUARD CRITICAL\] Buffer Underflow or Double Free detected at %s:%d!\\n\", file, line);

abort();

}

// Check Overflow Canary

GuardTrailer \*trailer = (GuardTrailer \*)((uint8_t \*)ptr + hdr-\>payload_size);

if (trailer-\>magic_end != CANARY_END) {

fprintf(stderr, \"\[MEMGUARD CRITICAL\] Buffer OVERFLOW detected on block allocated at %s:%d (Freed at %s:%d)!\\n\",

hdr-\>file, hdr-\>line, file, line);

abort();

}

// Unlink from active tracking list

if (hdr-\>prev) hdr-\>prev-\>next = hdr-\>next;

if (hdr-\>next) hdr-\>next-\>prev = hdr-\>prev;

if (g_alloc_list_head == hdr) g_alloc_list_head = hdr-\>next;

g_total_allocated_bytes -= hdr-\>payload_size;

g_active_allocations_count\--;

// Poison canaries to catch double-free

hdr-\>magic_start = 0x00000000;

trailer-\>magic_end = 0x00000000;

free(raw);

}

void memguard_report_leaks(void) {

printf(\"\\n========================================================================\\n\");

printf(\" MEMGUARD ALLOCATION LEAK REPORT \\n\");

printf(\"========================================================================\\n\");

if (g_active_allocations_count == 0) {

printf(\" NO LEAKS DETECTED! All allocated heap blocks cleanly released.\\n\");

} else {

printf(\" ALERT: %zu memory leak(s) detected! Total leaked: %zu bytes\\n\",

g_active_allocations_count, g_total_allocated_bytes);

GuardHeader \*curr = g_alloc_list_head;

size_t idx = 1;

while (curr) {

printf(\" \[%zu\] %zu Bytes allocated at %s:%d\\n\", idx++, curr-\>payload_size, curr-\>file, curr-\>line);

curr = curr-\>next;

}

}

printf(\"========================================================================\\n\\n\");

}

#define mg_malloc(sz) memguard_malloc_internal(sz, \_\_FILE\_\_, \_\_LINE\_\_)

#define mg_free(p) memguard_free_internal(p, \_\_FILE\_\_, \_\_LINE\_\_)

int main(void) {

printf(\"=== Testing MemGuard Dynamic Tracking Allocator ===\\n\");

int \*scores = (int \*)mg_malloc(5 \* sizeof(int));

for (int i = 0; i \< 5; i++) {

scores\[i\] = (i + 1) \* 10;

}

char \*leaked_buffer = (char \*)mg_malloc(64);

strcpy(leaked_buffer, \"This memory buffer was intentionally leaked for testing.\");

mg_free(scores);

// Generate Leak Report (Expects 64-byte leak from leaked_buffer)

memguard_report_leaks();

// Clean up leaked buffer

mg_free(leaked_buffer);

return 0;

}

\`\`\`

\-\--

\## 4. Error Handling & Defensive Programming Challenge

\### Scenario: Integer Multiplication Overflow & Realloc Pointer Invalidation

Examine the following buggy dynamic array resizing function:

\`\`\`c

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdint.h\>

typedef struct {

int \*data;

size_t capacity;

size_t count;

} DynamicArray;

// BUGGY IMPLEMENTATION

void resize_array_faulty(DynamicArray \*arr, size_t new_capacity) {

// VULNERABILITY 1: Integer Multiplication Overflow

// If \'new_capacity\' is huge (e.g. 2\^62), \'new_capacity \* sizeof(int)\' wraps around to a tiny value.

// malloc/realloc allocates a small buffer, subsequent indexing causes heap corruption!

// VULNERABILITY 2: realloc Assignment Leak

// If realloc fails, arr-\>data becomes NULL, permanently leaking the previously allocated array!

arr-\>data = (int \*)realloc(arr-\>data, new_capacity \* sizeof(int));

arr-\>capacity = new_capacity;

}

\`\`\`

\### Analysis of Vulnerabilities:

1\. \*\*Size Calculation Overflow:\*\* In 64-bit systems, passing \`new_capacity = SIZE_MAX / 2\` to \`new_capacity \* sizeof(int)\` overflows \`size_t\`, producing a tiny integer. \`realloc\` allocates a truncated buffer, and subsequent array writes corrupt adjacent heap metadata.

2\. \*\*Reallocation Pointer Loss:\*\* When \`realloc\` fails due to insufficient memory, it returns \`NULL\`, but the original memory block remains allocated. Assigning \`arr-\>data = realloc(\...)\` destroys the reference to the original block.

\### Defensive Fix:

\`\`\`c

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdbool.h\>

#include \<stdint.h\>

typedef struct {

int \*data;

size_t capacity;

size_t count;

} DynamicArray;

bool resize_array_safe(DynamicArray \*arr, size_t new_capacity) {

if (!arr \|\| new_capacity == 0) return false;

// Defensive Check 1: Check for multiplication overflow

if (new_capacity \> SIZE_MAX / sizeof(int)) {

fprintf(stderr, \"Defensive Error: Requested capacity calculation overflows size_t!\\n\");

return false;

}

size_t bytes_to_allocate = new_capacity \* sizeof(int);

// Defensive Check 2: Safe realloc idiom using temporary pointer

int \*new_data = (int \*)realloc(arr-\>data, bytes_to_allocate);

if (!new_data) {

fprintf(stderr, \"Defensive Error: Failed to reallocate %zu bytes (Out of Memory)!\\n\", bytes_to_allocate);

return false; // arr-\>data remains valid and intact

}

arr-\>data = new_data;

arr-\>capacity = new_capacity;

return true;

}

void dynamic_array_free(DynamicArray \*arr) {

if (!arr) return;

if (arr-\>data) {

free(arr-\>data);

arr-\>data = NULL; // Prevent dangling pointer

}

arr-\>capacity = 0;

arr-\>count = 0;

}

\`\`\`
