---
tags:
  - c
  - ring-buffer
  - circular-queue
  - bitwise-masking
  - lock-free
  - concurrency
date: 2026-09-10
day: 19
---

# Day 19: Lock-Free Ring Buffers & Circular Queues using Bitwise Masking

---

## 1. Quick Reference & Cheat Sheet

### Ring Buffer Fundamentals

A **Ring Buffer (Circular Queue)** is a fixed-size First-In, First-Out (FIFO) data structure implemented over a contiguous array. Two indices track the queue:

- **Head (Write Index):** Where the producer writes new incoming elements.

- **Tail (Read Index):** Where the consumer reads/removes elements.

t
```text
t┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐Array: │ [0]  │ [1]  │ [2]  │ [3]  │ [4]  │ [5]  │ [6]  │ [7]  │└──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘▲                           ▲Tail (Read)                 Head (Write)Occupied Elements: [2], [3], [4], [5] (Count = 4)
```
▲ ▲ Tail (Read) Head (Write) Occupied Elements: [2], [3], [4], [5] (Count = 4)

#### The Power-of-Two Bitwise Optimization

In traditional circular buffers, wrapping is achieved using integer modulo:

```c
next_idx = (idx + 1) % capacity; // SLOW: CPU integer division takes
15-40 cycles
If capacity is constrained to a **Power of Two** (\$2^k\$, e.g., 64,
1024, 65536):mask = capacity - 1; // Fast bitmask
next_idx = (idx + 1) & mask; // BLAZING FAST: Bitwise AND executes in 1
cycle!
## Queue State Invariants (Free-Running Monotonic Counters)
By allowing head and tail to increment indefinitely without wrapping at
capacity:
- **Index Mapping:** real_array_index = counter & mask
- **Buffer Empty:** head == tail
- **Buffer Full:** head - tail == capacity
- **Current Element Count:** head - tail (Guaranteed correct even across
  unsigned integer overflow!)
- **Available Write Space:** capacity - (head - tail)
# 2. In-Depth Theory & Low-Level Mechanics
## A. Why Unsigned Monotonic Overflow "Just Works"
In standard C, **unsigned integer arithmetic is guaranteed never to
overflow or trigger Undefined Behavior**; it wraps modulo \$2^W\$
(where \$W\$ is 32 or 64 bits) according to C17 §6.2.5.
Suppose head and tail are uint32_t, and capacity = 8:
- Suppose head has reached 0xFFFFFFFF (4,294,967,295), and tail =
  0xFFFFFFFC (4,294,967,292).
- Current count: head - tail = 0xFFFFFFFF - 0xFFFFFFFC = 3.
- Now, Producer writes 1 item. head increments to 0x00000000 (wrapped
  around to 0).
- How does head - tail behave now?
  \$\$\\text{head} - \\text{tail} = 0x00000000 - 0xFFFFFFFC = -4 \\equiv
  4 \\pmod{2^{32}}\$\$
- In two's complement unsigned math, 0x00000000 - 0xFFFFFFFC evaluates
  to **exactly 4**!
- Unsigned modular arithmetic ensures that head - tail accurately
  reflects queue fullness regardless of integer wrap-around.
## B. Hardware Latency: Modulo (%) vs Bitwise AND (&)
1.  **CPU Division (idiv / div):**
    - Non-pipelined hardware arithmetic unit.
    - Latency: 15--40 CPU clock cycles. Cannot be vectorized with SIMD.
2.  **Bitwise AND (and):**
    - Fundamental ALU logic gate.
    - Latency: **1 CPU clock cycle**. Throughput: up to 4 operations per
      cycle on modern superscalar CPUs.
## C. Cache-Line False Sharing in Concurrency
In a high-throughput Single-Producer Single-Consumer (SPSC) lock-free
queue:
- The Producer core writes frequently to head and reads tail.
- The Consumer core writes frequently to tail and reads head.
If head and tail reside next to each other inside the same struct
RingBuffer:struct NaiveRingBuffer {
size_t head; // Offset 0 (Bytes 0..7)
size_t tail; // Offset 8 (Bytes 8..15)
}; // Both fit in the same 64-byte L1 CPU Cache Line!
Core 0 (Producer Core) Core 1 (Consumer Core)
Writes to 'head' Writes to 'tail'
│ │
▼ ▼
[ Invalidate Cache Line! ] ◄── Cache Bus ──► [ Invalidate Cache Line!
]
Both CPU cores repeatedly invalidate each other's L1/L2 cache lines
across the inter-core interconnect (**False Sharing** / Cache
Ping-Pong), causing 10x--50x performance degradation!
### The Hardware Fix (Cache-Line Alignment):
Pad the variables so head and tail occupy physically distinct 64-byte
cache lines:typedef struct {
alignas(64) uint64_t head; // Dedicated 64-byte cache line
uint8_t pad1[56];
alignas(64) uint64_t tail; // Dedicated 64-byte cache line
uint8_t pad2[56];
} CacheIsolatedQueue;
# 3. Thoughtful Mini-Project (~1 Hour Scope)
## Project Title: High-Throughput Power-of-Two Lock-Free Ring Buffer (fast_ringbuf)
### Objective
Build a cache-isolated, power-of-two ring buffer in C supporting:
1.  Automatic power-of-two capacity rounding.
2.  Free-running monotonic counters with \$O(1)\$ single-cycle masking.
3.  Zero-copy bulk chunk writes (ringbuf_write) and reads (ringbuf_read)
    supporting contiguous split-buffer operations without extra memory
    copying.
### Complete Starter Code Implementation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
typedef struct {
    char *buffer;
    size_t capacity;
    size_t mask;
    uint64_t head;
    uint64_t tail;
} SafeQueue;
static inline bool is_pow2(size_t x) {
    return (x != 0) && ((x & (x - 1)) == 0);
}
SafeQueue *queue_create_safe(size_t cap) {
    // Defensive Check 1: Enforce strict power-of-two requirement
    if (!is_pow2(cap)) {
        fprintf(stderr, "Defensive Error: Capacity %zu is not a power of 2!\n", cap);
        return NULL;
    }
    SafeQueue *q = (SafeQueue *)malloc(sizeof(SafeQueue));
    if (!q) return NULL;
    q->buffer = (char *)malloc(cap);
    if (!q->buffer) {
        free(q);
        return NULL;
    }
    q->capacity = cap;
    q->mask = cap - 1;
    q->head = 0;
    q->tail = 0;
    return q;
}
bool queue_push_safe(SafeQueue *q, char item) {
    if (!q) return false;
    // Defensive Check 2: Check if full using monotonic distance
    if ((size_t)(q->head - q->tail) >= q->capacity) {
        fprintf(stderr, "Defensive Warning: Queue full! Rejecting push.\n");
        return false; // Backpressure / drop notification
    }
    q->buffer[q->head & q->mask] = item;
    q->head++;
    return true;
}
bool queue_pop_safe(SafeQueue *q, char *out_item) {
    if (!q || !out_item) return false;
```
|---|
// Defensive Check 3: Check if empty
if (q->head == q->tail) {
return false;
}
*out_item = q->buffer[q->tail & q->mask];
q->tail++;
return true;
}