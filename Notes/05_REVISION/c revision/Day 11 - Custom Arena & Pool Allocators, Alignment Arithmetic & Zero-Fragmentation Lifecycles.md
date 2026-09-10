---
tags:
  - c
  - memory-management
  - arena-allocator
  - pool-allocator
  - alignment-arithmetic
  - low-level-systems
date: 2026-09-02
day: 11
---

# Day 11: Custom Arena & Pool Allocators, Alignment Arithmetic & Zero-Fragmentation Lifecycles

---

## 1. Quick Reference & Cheat Sheet

### Why Custom Allocators?
Standard `malloc` and `free` are general-purpose:
* **Overhead:** Impose 8 to 16 bytes of metadata per allocation chunk.
* **Latency:** Non-deterministic execution time ($O(1)$ amortized, but can trigger locks, list traversal, or kernel syscalls).
* **Fragmentation:** Frequent allocations of disparate sizes inevitably fragment the heap.

Custom allocators provide **deterministic $O(1)$ speed**, **zero per-allocation metadata overhead**, and **batch reclamation**.

| Allocator Type | Allocation Time | Deallocation Time | Per-Object Overhead | Supports Individual `free`? | Ideal Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Arena (Bump / Linear)** | $O(1)$ (Pointer addition) | $O(1)$ (Batch reset) | **0 Bytes** | **No** (Batch reset only) | Per-frame scratch memory, HTTP request lifecycle, AST building. |
| **Pool (Fixed-Size Blocks)** | $O(1)$ (Pop from list) | $O(1)$ (Push to list) | **0 Bytes** (Intrusive list) | **Yes** (Arbitrary order) | Game entity pools, network packet buffers, connection nodes. |
| **Buddy Allocator** | $O(\\log N)$ | $O(\\log N)$ | Header per block | **Yes** | Operating system kernel physical page frame allocators. |

### Alignment Bitwise Formula
For any alignment $A$ that is a **power of 2** (e.g. 4, 8, 16, 64):
```c
// Align an unsigned integer or address upwards to multiple of A:
#define ALIGN_UP(addr, align) (((addr) \+ ((align) \- 1)) & \~((align) \- 1))

// Calculate padding bytes needed to align an address:
#define ALIGN_PAD(addr, align) (((align) \- ((addr) & ((align) \- 1))) & ((align) \- 1))
```

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Alignment Arithmetic: The Power-of-Two Bit Trick
Modern CPUs read and write memory via multi-byte buses (64 bits / 8 bytes on x86_64 and ARM64). When a type's address is an exact multiple of its size (e.g., an 8-byte `double` placed at an address divisible by 8):
* The hardware accesses the data in a single CPU bus cycle.
* Unaligned access requires two memory cycles, cache-line crossing splits, or raises a hardware alignment fault (`SIGBUS`).

#### Why `(addr + (A - 1)) & ~(A - 1)` Works:
If $A \= 8$ (`0b00001000`):
* $A \- 1 \= 7$ (`0b00000111`): The mask of bits that must be cleared.
* $\\sim(A \- 1\) \= \\text{bitwise NOT}(7) \=$ `0b11111000`: Clears the lowest 3 bits.
* Adding $A \- 1$ ensures that any value with non-zero lower bits carries into the next multiple of $A$ before the lower bits are stripped.

```text
Example: Aligning addr \= 17 (0b00010001) to 8-byte boundary:
  1. addr \+ (8 \- 1\) \= 17 \+ 7 \= 24  (0b00011000)
  2. \~(8 \- 1\)       \= \~7      \=    (0b11111000)
  3. 24 & \~7        \= 24           (0b00011000) \-> 24 is divisible by 8\!
```

---

### B. Arena (Linear / Bump) Allocator Mechanics
An **Arena** allocates a single large, contiguous block of heap memory upfront (`malloc` or OS `mmap`).
* A single variable, `offset`, tracks the watermark.
* Allocation merely advances (`bumps`) the offset pointer by `size \+ padding`.
* Individual allocations cannot be freed. Instead, memory is reclaimed en masse by setting `offset \= 0`\!

```text
Arena Memory Buffer (Total Capacity \= 64 KB):
 ┌──────────────────┬──────────────────┬──────────────┬───────────────────────────────┐
 │ Allocation A     │ Allocation B     │ Allocation C │ Unallocated Free Space        │
 │ (32 Bytes)       │ (128 Bytes)      │ (64 Bytes)   │ (Available for bump alloc)    │
 └──────────────────┴──────────────────┴──────────────┴───────────────────────────────┘
 0x1000             0x1020             0x10A0         0x10E0                          0x11000
                                                      ▲
                                                      └── current arena->offset (Bump Pointer)
```

#### Scoped / Scratchpad Arenas (Rewind Marks):
To use an arena for temporary computations without leaking memory:
1. Record current offset: `size_t mark \= arena->offset;`
2. Perform arbitrary allocations within the function.
3. Rewind to mark before returning: `arena->offset \= mark;`

---

### C. Fixed-Size Block Pool & Intrusive Free Lists
When you need to allocate and free individual objects of the **same size** in arbitrary order, a **Pool Allocator** avoids fragmentation using an **Intrusive Free List**.

#### The Zero-Overhead Memory Trick:
When a block is free, the client is not using its data. Therefore, the allocator reuses the first 8 bytes of the block itself to store a pointer to the next free block\!

```text
Free Pool Memory Layout (Intrusive Singly-Linked List):
  [FreeBlock 1]  ───►  [FreeBlock 2]  ───►  [FreeBlock 3]  ───►  NULL
  ┌────────────┐       ┌────────────┐       ┌────────────┐
  │ next ptr   │       │ next ptr   │       │ next ptr   │
  ├────────────┤       ├────────────┤       ├────────────┤
  │ unused mem │       │ unused mem │       │ unused mem │
  └────────────┘       └────────────┘       └────────────┘
```
* **Allocation (`pool_alloc`):** Pop head of free list ($O(1)$).
* **Deallocation (`pool_free`):** Push returned block onto head of free list ($O(1)$).

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Dual-Strategy Memory Engine: Bump Arena & Intrusive Pool Allocator (`mem_subsystem`)

#### Objective
Build a memory subsystem in C featuring:
1. An **Arena Allocator** with strict byte alignment and savepoint/rewind capabilities for transient/per-frame scratch memory.
2. A **Fixed-Size Block Pool** utilizing an intrusive singly-linked list for fast object allocation and individual deallocation.
3. A driver program simulating a server request loop allocating transient request buffers alongside persistent session entities.

#### Complete Starter Code Implementation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#define DEFAULT_ALIGNMENT (sizeof(void *)) // 8 bytes on 64-bit

/* \========================================================================= */
/*                          1. ARENA ALLOCATOR                               */
/* \========================================================================= */

typedef struct {
    uint8_t *buffer;
    size_t capacity;
    size_t offset;
} MemoryArena;

typedef struct {
    MemoryArena *arena;
    size_t saved_offset;
} ArenaTemp;

MemoryArena *arena_create(size_t capacity) {
    MemoryArena *arena \= (MemoryArena *)malloc(sizeof(MemoryArena));
    if (\!arena) return NULL;

    arena->buffer \= (uint8_t *)malloc(capacity);
    if (\!arena->buffer) {
        free(arena);
        return NULL;
    }

    arena->capacity \= capacity;
    arena->offset \= 0;
    return arena;
}

void arena_destroy(MemoryArena *arena) {
    if (\!arena) return;
    free(arena->buffer);
    free(arena);
}

void *arena_alloc_align(MemoryArena *arena, size_t size, size_t alignment) {
    assert((alignment & (alignment \- 1)) \== 0 && "Alignment must be a power of 2");

    uintptr_t current_addr \= (uintptr_t)(arena->buffer \+ arena->offset);
    uintptr_t aligned_addr \= (current_addr \+ (alignment \- 1)) & \~(uintptr_t)(alignment \- 1);
    size_t padding \= (size_t)(aligned_addr \- current_addr);

    if (arena->offset \+ padding \+ size > arena->capacity) {
        fprintf(stderr, "[Arena Error] Out of Memory\! Requested %zu bytes (Padding: %zu, Cap: %zu)\\n",
                size, padding, arena->capacity);
        return NULL;
    }

    arena->offset \+= padding \+ size;
    return (void *)aligned_addr;
}

void *arena_alloc(MemoryArena *arena, size_t size) {
    return arena_alloc_align(arena, size, DEFAULT_ALIGNMENT);
}

void arena_reset(MemoryArena *arena) {
    arena->offset \= 0;
}

// Scoped scratchpad snapshot
ArenaTemp arena_temp_begin(MemoryArena *arena) {
    return (ArenaTemp){ .arena \= arena, .saved_offset \= arena->offset };
}

void arena_temp_end(ArenaTemp temp) {
    temp.arena->offset \= temp.saved_offset;
}

/* \========================================================================= */
/*                        2. FIXED-SIZE POOL ALLOCATOR                       */
/* \========================================================================= */

typedef struct PoolNode {
    struct PoolNode *next;
} PoolNode;

typedef struct {
    uint8_t *buffer;
    size_t block_size;
    size_t capacity_blocks;
    PoolNode *free_list;
} MemoryPool;

MemoryPool *pool_create(size_t block_size, size_t capacity_blocks) {
    // Each block must be at least large enough to store an intrusive pointer
    if (block_size < sizeof(PoolNode)) {
        block_size \= sizeof(PoolNode);
    }

    // Align block size to 8-byte boundary
    block_size \= (block_size \+ (DEFAULT_ALIGNMENT \- 1)) & \~(DEFAULT_ALIGNMENT \- 1);

    MemoryPool *pool \= (MemoryPool *)malloc(sizeof(MemoryPool));
    if (\!pool) return NULL;

    pool->buffer \= (uint8_t *)malloc(block_size * capacity_blocks);
    if (\!pool->buffer) {
        free(pool);
        return NULL;
    }

    pool->block_size \= block_size;
    pool->capacity_blocks \= capacity_blocks;
    pool->free_list \= NULL;

    // Link all blocks into the intrusive free list
    for (size_t i \= 0; i < capacity_blocks; i++) {
        PoolNode *node \= (PoolNode *)(pool->buffer \+ (i * block_size));
        node->next \= pool->free_list;
        pool->free_list \= node;
    }

    return pool;
}

void pool_destroy(MemoryPool *pool) {
    if (\!pool) return;
    free(pool->buffer);
    free(pool);
}

void *pool_alloc(MemoryPool *pool) {
    if (\!pool->free_list) {
        fprintf(stderr, "[Pool Error] All blocks exhausted\!\\n");
        return NULL;
    }

    // Pop head node from free list (O(1))
    PoolNode *node \= pool->free_list;
    pool->free_list \= node->next;

    return (void *)node;
}

void pool_free(MemoryPool *pool, void *ptr) {
    if (\!ptr) return;

    // Optional bounds assertion: ensure ptr is within pool buffer
    assert((uint8_t *)ptr >= pool->buffer &&
           (uint8_t *)ptr < pool->buffer \+ (pool->block_size * pool->capacity_blocks));

    // Push node back to head of free list (O(1))
    PoolNode *node \= (PoolNode *)ptr;
    node->next \= pool->free_list;
    pool->free_list \= node;
}

/* \========================================================================= */
/*                               DRIVER MAIN                                 */
/* \========================================================================= */

typedef struct {
    uint32_t session_id;
    char username[24];
    uint64_t last_active_ts;
} UserSession;

int main(void) {
    printf("=== Demonstrating Custom Memory Subsystem \===\\n\\n");

    // 1. Initialize Arena (64 KB for transient work) and Pool (for UserSession nodes)
    MemoryArena *scratch_arena \= arena_create(64 * 1024);
    MemoryPool *session_pool \= pool_create(sizeof(UserSession), 4);

    // 2. Allocate persistent session entities from Pool
    printf("[1] Allocating 3 UserSession blocks from Memory Pool...\\n");
    UserSession *s1 \= (UserSession *)pool_alloc(session_pool);
    UserSession *s2 \= (UserSession *)pool_alloc(session_pool);
    UserSession *s3 \= (UserSession *)pool_alloc(session_pool);

    s1->session_id \= 101; strcpy(s1->username, "Alice");
    s2->session_id \= 102; strcpy(s2->username, "Bob");
    s3->session_id \= 103; strcpy(s3->username, "Charlie");

    printf("    Active: [%u: %s], [%u: %s], [%u: %s]\\n",
           s1->session_id, s1->username, s2->session_id, s2->username, s3->session_id, s3->username);

    // Free Bob (s2) back to pool
    printf("    Freeing session '%s' back to pool (O(1))...\\n", s2->username);
    pool_free(session_pool, s2);

    // Re-allocate: should immediately reuse s2's memory block
    UserSession *s4 \= (UserSession *)pool_alloc(session_pool);
    s4->session_id \= 104; strcpy(s4->username, "Diana");
    printf("    Allocated new session: [%u: %s] (Reused block at %p)\\n\\n",
           s4->session_id, s4->username, (void *)s4);

    // 3. Demonstrate Scoped Scratchpad Arena Allocation
    printf("[2] Processing Batch Request using Scoped Scratch Arena...\\n");
    printf("    Arena offset before request: %zu bytes\\n", scratch_arena->offset);

    {
        ArenaTemp scratch \= arena_temp_begin(scratch_arena);

        // Allocate temporary buffers for a request
        char *query_buf \= (char *)arena_alloc(scratch_arena, 512);
        int *temp_ids \= (int *)arena_alloc_align(scratch_arena, 100 * sizeof(int), 16);

        snprintf(query_buf, 512, "SELECT * FROM logs WHERE session=%u", s1->session_id);
        temp_ids[0] \= 42;

        printf("    Executed query: \\"%s\\"\\n", query_buf);
        printf("    Arena offset during request: %zu bytes\\n", scratch_arena->offset);

        // Reclaim scratch memory instantly\!
        arena_temp_end(scratch);
    }

    printf("    Arena offset after request scope end: %zu bytes (Zero Leaks\!)\\n\\n", scratch_arena->offset);

    // Clean up
    pool_free(session_pool, s1);
    pool_free(session_pool, s3);
    pool_free(session_pool, s4);
    pool_destroy(session_pool);
    arena_destroy(scratch_arena);

    printf("Memory Subsystem successfully destroyed with 0 fragmentation\!\\n");
    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Alignment Padding Integer Overflow Trap
Examine the following buggy custom arena allocator function:

```c
#include <stdint.h>
#include <stddef.h>

typedef struct {
    uint8_t *buffer;
    size_t capacity;
    size_t offset;
} NaiveArena;

// BUGGY IMPLEMENTATION
void *naive_arena_alloc(NaiveArena *arena, size_t size, size_t align) {
    // BUG 1: Non-power-of-2 alignment causes infinite loop or corrupted bitmasking.
    // BUG 2: Unchecked addition overflow\!
    // If 'size' is passed as SIZE_MAX \- 4, 'current_addr \+ align \- 1' wraps around to a small number,
    // bypassing the boundary check\!
    uintptr_t current_addr \= (uintptr_t)(arena->buffer \+ arena->offset);
    uintptr_t aligned_addr \= (current_addr \+ (align \- 1)) & \~(align \- 1);

    size_t padding \= aligned_addr \- current_addr;

    // BUG 3: 'arena->offset \+ padding \+ size' can overflow size_t\!
    if (arena->offset \+ padding \+ size > arena->capacity) {
        return NULL;
    }

    arena->offset \+= padding \+ size;
    return (void *)aligned_addr;
}
```

### Analysis of Vulnerabilities:
1. **Unchecked Non-Power-of-2 Alignment:** The identity `\~(align \- 1)` only generates an address-clearing bitmask if `align` is an exact power of 2. Passing an arbitrary number (e.g. `align \= 7`) corrupts pointer alignment.
2. **Integer Wrap-Around in Boundary Checks:** When `arena->offset \+ padding \+ size` exceeds `SIZE_MAX`, it wraps around to a tiny positive integer. The condition `< arena->capacity` evaluates to `true`, and the allocator returns a pointer pointing far outside the allocated buffer into unmapped memory.

### Defensive Fix:
```c
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <stdio.h>

typedef struct {
    uint8_t *buffer;
    size_t capacity;
    size_t offset;
} SafeArena;

static inline bool is_power_of_two(size_t x) {
    return (x \!= 0\) && ((x & (x \- 1)) \== 0);
}

void *safe_arena_alloc(SafeArena *arena, size_t size, size_t align) {
    if (\!arena || size \== 0 || \!is_power_of_two(align)) {
        return NULL;
    }

    uintptr_t current_addr \= (uintptr_t)(arena->buffer \+ arena->offset);

    // Calculate padding without risking pointer overflow
    size_t modulo \= (size_t)(current_addr & (uintptr_t)(align \- 1));
    size_t padding \= (modulo \== 0\) ? 0 : (align \- modulo);

    // Defensive Check 1: Ensure padding \+ size does not overflow size_t
    if (size > SIZE_MAX \- padding) {
        fprintf(stderr, "Defensive Error: Allocation size \+ padding overflows size_t\!\\n");
        return NULL;
    }

    size_t total_needed \= padding \+ size;

    // Defensive Check 2: Check remaining capacity using safe subtraction
    if (total_needed > arena->capacity \- arena->offset) {
        fprintf(stderr, "Defensive Error: Arena capacity exceeded\!\\n");
        return NULL;
    }

    void *aligned_ptr \= (void *)(arena->buffer \+ arena->offset \+ padding);
    arena->offset \+= total_needed;
    return aligned_ptr;
}
```
