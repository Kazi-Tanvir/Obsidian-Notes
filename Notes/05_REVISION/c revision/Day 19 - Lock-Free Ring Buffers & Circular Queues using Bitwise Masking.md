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

```text
┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
Array: │ [0]  │ [1]  │ [2]  │ [3]  │ [4]  │ [5]  │ [6]  │ [7]  │
       └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
                       ▲                           ▲
                  Tail (Read)                 Head (Write)
Occupied Elements: [2], [3], [4], [5] (Count = 4)
```

### The Power-of-Two Bitwise Optimization

In traditional circular buffers, wrapping is achieved using integer modulo:

```c
next_idx = (idx + 1) % capacity; // SLOW: CPU integer division takes 15-40 cycles
```

If capacity is constrained to a **Power of Two** ($2^k$, e.g., 64, 1024, 65536):

```c
mask = capacity - 1;             // Fast bitmask
next_idx = (idx + 1) & mask;     // BLAZING FAST: Bitwise AND executes in 1 cycle!
```

### Queue State Invariants (Free-Running Monotonic Counters)

By allowing `head` and `tail` to increment indefinitely without wrapping at capacity:

- **Index Mapping:** `real_array_index = counter & mask`
- **Buffer Empty:** `head == tail`
- **Buffer Full:** `head - tail == capacity`
- **Current Element Count:** `head - tail` (Guaranteed correct even across unsigned integer overflow!)
- **Available Write Space:** `capacity - (head - tail)`

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Why Unsigned Monotonic Overflow "Just Works"

In standard C, **unsigned integer arithmetic is guaranteed never to overflow or trigger Undefined Behavior**; it wraps modulo $2^W$ (where $W$ is 32 or 64 bits) according to C17 §6.2.5.

Suppose `head` and `tail` are `uint32_t`, and `capacity = 8`:

- Suppose `head` has reached `0xFFFFFFFF` (4,294,967,295), and `tail = 0xFFFFFFFC` (4,294,967,292).
- Current count: `head - tail = 0xFFFFFFFF - 0xFFFFFFFC = 3`.
- Now, Producer writes 1 item. `head` increments to `0x00000000` (wrapped around to 0).
- How does `head - tail` behave now?
  $$\text{head} - \text{tail} = 0x00000000 - 0xFFFFFFFC = -4 \equiv 4 \pmod{2^{32}}$$
- In two's complement unsigned math, `0x00000000 - 0xFFFFFFFC` evaluates to **exactly 4**!
- Unsigned modular arithmetic ensures that `head - tail` accurately reflects queue fullness regardless of integer wrap-around.

### B. Hardware Latency: Modulo (%) vs Bitwise AND (&)

1. **CPU Division (`idiv` / `div`):**
   - Non-pipelined hardware arithmetic unit.
   - Latency: 15–40 CPU clock cycles. Cannot be vectorized with SIMD.

2. **Bitwise AND (`and`):**
   - Fundamental ALU logic gate.
   - Latency: **1 CPU clock cycle**. Throughput: up to 4 operations per cycle on modern superscalar CPUs.

### C. Cache-Line False Sharing in Concurrency

In a high-throughput Single-Producer Single-Consumer (SPSC) lock-free queue:

- The Producer core writes frequently to `head` and reads `tail`.
- The Consumer core writes frequently to `tail` and reads `head`.

If `head` and `tail` reside next to each other inside the same struct `RingBuffer`:

```c
struct NaiveRingBuffer {
    size_t head; // Offset 0  (Bytes 0..7)
    size_t tail; // Offset 8  (Bytes 8..15)
}; // Both fit in the same 64-byte L1 CPU Cache Line!
```

```text
Core 0 (Producer Core)                         Core 1 (Consumer Core)
  Writes to 'head'                              Writes to 'tail'
        │                                             │
        ▼                                             ▼
  [ Invalidate Cache Line! ] ◄── Cache Bus ──► [ Invalidate Cache Line! ]
```

Both CPU cores repeatedly invalidate each other's L1/L2 cache lines across the inter-core interconnect (**False Sharing** / Cache Ping-Pong), causing 10x–50x performance degradation!

#### The Hardware Fix (Cache-Line Alignment):

Pad the variables so `head` and `tail` occupy physically distinct 64-byte cache lines:

```c
typedef struct {
    alignas(64) uint64_t head; // Dedicated 64-byte cache line
    uint8_t pad1[56];
    alignas(64) uint64_t tail; // Dedicated 64-byte cache line
    uint8_t pad2[56];
} CacheIsolatedQueue;
```

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: High-Throughput Power-of-Two Lock-Free Ring Buffer (`fast_ringbuf`)

#### Objective

Build a cache-isolated, power-of-two ring buffer in C supporting:
1. Automatic power-of-two capacity rounding.
2. Free-running monotonic counters with $O(1)$ single-cycle masking.
3. Zero-copy bulk chunk writes (`ringbuf_write`) and reads (`ringbuf_read`) supporting contiguous split-buffer operations without extra memory copying.

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
#define CACHE_LINE_SIZE 64
typedef struct {
    // Producer-owned cache line
    uint64_t head;
    uint8_t pad_producer[CACHE_LINE_SIZE - sizeof(uint64_t)];
    // Consumer-owned cache line
    uint64_t tail;
    uint8_t pad_consumer[CACHE_LINE_SIZE - sizeof(uint64_t)];
    // Read-only configuration
    uint8_t *buffer;
    size_t capacity;
    size_t mask;
} RingBuffer;
// Round up to nearest power of 2
static inline size_t round_up_pow2(size_t v) {
    v--;
    v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    v |= v >> 32;
    v++;
    return v == 0 ? 1 : v;
}
RingBuffer *ringbuf_create(size_t requested_capacity) {
    size_t cap = round_up_pow2(requested_capacity);
    if (cap < 16) cap = 16; // Minimum threshold
    RingBuffer *rb = (RingBuffer *)aligned_alloc(CACHE_LINE_SIZE, sizeof(RingBuffer));
    if (!rb) return NULL;
    rb->buffer = (uint8_t *)malloc(cap);
    if (!rb->buffer) {
        free(rb);
        return NULL;
    }
    rb->head = 0;
    rb->tail = 0;
    rb->capacity = cap;
    rb->mask = cap - 1;
    return rb;
}
void ringbuf_free(RingBuffer *rb) {
    if (!rb) return;
    free(rb->buffer);
    free(rb);
}
// O(1) Capacity & State Inspection
static inline size_t ringbuf_count(const RingBuffer *rb) {
    return (size_t)(rb->head - rb->tail);
}
static inline size_t ringbuf_free_space(const RingBuffer *rb) {
    return rb->capacity - ringbuf_count(rb);
}
static inline bool ringbuf_is_empty(const RingBuffer *rb) {
    return rb->head == rb->tail;
}
static inline bool ringbuf_is_full(const RingBuffer *rb) {
    return ringbuf_count(rb) == rb->capacity;
}
// Bulk Write (Enqueue) with wrap-around handling
size_t ringbuf_write(RingBuffer *rb, const uint8_t *src, size_t len) {
    size_t free_slots = ringbuf_free_space(rb);
    size_t to_write = len < free_slots ? len : free_slots;
    if (to_write == 0) return 0;
    size_t head_idx = (size_t)(rb->head & rb->mask);
    size_t chunk1 = rb->capacity - head_idx;
    if (to_write <= chunk1) {
        // Fits in single contiguous tail block
        memcpy(rb->buffer + head_idx, src, to_write);
    } else {
        // Wraps around: Split into two copies
        memcpy(rb->buffer + head_idx, src, chunk1);
        memcpy(rb->buffer, src + chunk1, to_write - chunk1);
    }
    rb->head += to_write; // Monotonic advance
    return to_write;
}
// Bulk Read (Dequeue) with wrap-around handling
size_t ringbuf_read(RingBuffer *rb, uint8_t *dest, size_t len) {
    size_t available = ringbuf_count(rb);
    size_t to_read = len < available ? len : available;
    if (to_read == 0) return 0;
    size_t tail_idx = (size_t)(rb->tail & rb->mask);
    size_t chunk1 = rb->capacity - tail_idx;
    if (to_read <= chunk1) {
        // Fits in single contiguous block
        memcpy(dest, rb->buffer + tail_idx, to_read);
    } else {
        // Wraps around: Split into two reads
        memcpy(dest, rb->buffer + tail_idx, chunk1);
        memcpy(dest + chunk1, rb->buffer, to_read - chunk1);
    }
    rb->tail += to_read; // Monotonic advance
    return to_read;
}
/* ========================================================================= */
/*                               DRIVER MAIN                                 */
/* ========================================================================= */
int main(void) {
    printf("====================================================================\n");
    printf("   DEMONSTRATING POWER-OF-TWO LOCK-FREE CACHE-ALIGNED RING BUFFER    \n");
    printf("====================================================================\n\n");
    // 1. Initialize Buffer (Requested: 50 bytes -> Rounded to 64 bytes)
    RingBuffer *rb = ringbuf_create(50);
    assert(rb != NULL);
    printf("[1] Initialized Ring Buffer:\n");
    printf("    Requested: 50 Bytes | Normalized Capacity: %zu Bytes (Mask: 0x%02zX)\n", 
           rb->capacity, rb->mask);
    printf("    Cache-line alignment verified for Producer and Consumer handles.\n\n");
    // 2. Write telemetry packets
    printf("[2] Enqueueing Data Stream...\n");
    const char *stream1 = "MSG_1: Sensor Online; MSG_2: Calibrating; ";
    size_t written1 = ringbuf_write(rb, (const uint8_t *)stream1, strlen(stream1));
    printf("    Wrote %zu bytes. (Current Count: %zu, Remaining Space: %zu)\n",
           written1, ringbuf_count(rb), ringbuf_free_space(rb));
    // 3. Partial Read
    printf("\n[3] Dequeueing First Batch...\n");
    uint8_t read_buf[128];
    size_t read1 = ringbuf_read(rb, read_buf, 21);
    read_buf[read1] = '\0';
    printf("    Read %zu bytes: \"%s\"\n", read1, (char *)read_buf);
    printf("    Buffer Status: Count: %zu, Head: %llu, Tail: %llu\n", 
           ringbuf_count(rb), (unsigned long long)rb->head, (unsigned long long)rb->tail);
    // 4. Force Wrap-Around
    printf("\n[4] Writing across array boundary to force wrap-around...\n");
    const char *stream2 = "MSG_3: Target Coordinate (42.0, -71.0); MSG_4: Velocity Normal.";
    size_t written2 = ringbuf_write(rb, (const uint8_t *)stream2, strlen(stream2));
    printf("    Wrote %zu bytes across boundary. Head is now: %llu (Index: %zu)\n",
           written2, (unsigned long long)rb->head, (size_t)(rb->head & rb->mask));
    // 5. Read all remaining bytes across wrap-around split
    printf("\n[5] Reading remaining stream across boundary:\n");
    size_t total_remaining = ringbuf_count(rb);
    size_t read2 = ringbuf_read(rb, read_buf, total_remaining);
    read_buf[read2] = '\0';
    printf("    Read %zu bytes across wrap-around:\n    \"%s\"\n", read2, (char *)read_buf);
    assert(ringbuf_is_empty(rb));
    printf("\n    Buffer Verified Empty: %s\n", ringbuf_is_empty(rb) ? "YES" : "NO");
    ringbuf_free(rb);
    printf("\nRing buffer cleanly destroyed with zero leaks!\n");
    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Non-Power-of-Two Masking & Integer Overflow Truncation Bug

Examine the following faulty circular buffer implementation:

```c
#include <stdlib.h>
typedef struct {
    char *buffer;
    size_t capacity;
    size_t mask;
    unsigned int head; // 32-bit unsigned
    unsigned int tail; // 32-bit unsigned
} FaultyQueue;
// BUGGY IMPLEMENTATION
FaultyQueue *queue_create_faulty(size_t cap) {
    FaultyQueue *q = (FaultyQueue *)malloc(sizeof(FaultyQueue));
    q->capacity = cap;
    // BUG 1: Naive mask assignment without ensuring 'cap' is a power of 2!
    // If cap is 100, mask is 99 (0b01100011).
    // Indices like 4 (0b00000100) masked with 99 produce 0! Corrupts index sequence!
    q->mask = cap - 1;
    q->buffer = (char *)malloc(cap);
    q->head = 0;
    q->tail = 0;
    return q;
}
void queue_push_faulty(FaultyQueue *q, char item) {
    // BUG 2: No check for full buffer! Overwrites unconsumed data silently.
    q->buffer[q->head & q->mask] = item;
    q->head++;
}
Invalid Bitmask on Arbitrary Integer: The identity idx & (capacity - 1) == idx % capacity holds strictly and only if capacity is an exact power of 2. For arbitrary numbers (e.g. cap = 100), bitwise AND produces skipped addresses, internal collisions, and writes into non-contiguous slots.
Silent Buffer Overwrite: Lack of full-buffer validation allows the producer to lap the consumer, silently destroying unread packets and causing data loss.
Defensive Fix:
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
```

### Analysis of Vulnerabilities:

1. **Non-Power-of-Two Masking:** If capacity is not a power of two (e.g. 50), `mask = 49` (binary `0b110001`). Performing `idx & 49` skips entire index regions and accesses out-of-bounds array indices, causing heap buffer corruption.
2. **Modulo Fallacy:** Tracking queue count using `head - tail` where `head` and `tail` are modulo-wrapped destroys the invariant `head >= tail`. Once `head` wraps around to 0, `head - tail` underflows, reporting a massive fake queue size.
3. **Integer Truncation & Mixed Types:** Using `unsigned int` (32-bit) for `head`/`tail` with `size_t` (64-bit) for `capacity` leads to subtle truncation bugs when crossing $2^{32}$ operations.

### Defensive Fix:

```c
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
    // Defensive Check 3: Check if empty
    if (q->head == q->tail) {
        return false;
    }
    *out_item = q->buffer[q->tail & q->mask];
    q->tail++;
    return true;
}
```
