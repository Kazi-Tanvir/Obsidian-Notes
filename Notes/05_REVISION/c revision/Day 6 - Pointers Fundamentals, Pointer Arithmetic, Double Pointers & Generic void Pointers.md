---
tags:
- c
- pointers
- pointer-arithmetic
- double-pointers
- void-pointers
- memory-addressing
date: 2026-08-28
day: 6
---

# Day 6: Pointers Fundamentals, Pointer Arithmetic, Double Pointers & Generic void Pointers

---

## 1. Quick Reference & Cheat Sheet

### Core Pointer Concepts & Syntax

| Expression | Read As | Result / Effect |

| :--- | :--- | :--- |

| `int *p;` | Declaration | `p` is a pointer to an `int` (holds an address). |

| `p = &x;` | Address-of | Stores the memory address of `x` into `p`. |

| `*p = 20;` | Dereference | Writes `20` into the memory location pointed to by `p`. |

| `int **pp = &p;` | Pointer-to-Pointer | `pp` holds the memory address of pointer variable `p`. |

| `void *raw;` | Generic Pointer | Holds an address of unspecified type; cannot be directly dereferenced. |

| `NULL` | Null Pointer Constant | `((void *)0)`; indicates pointer does not point to valid memory. |

### Pointer Arithmetic Scaling Rules

In C, arithmetic on a pointer scales automatically by `sizeof(*ptr)`:

```c
Type *ptr = base_address;
ptr + n => (uintptr_t)base_address + (n * sizeof(Type))
```

* `int32_t *p` (+1 step advances **4 bytes**).

* `double *p` (+1 step advances **8 bytes**).

* `struct Node *p` (+1 step advances **`sizeof(struct Node)` bytes**).

* **Pointer Subtraction (`ptr2 - ptr1`):** Yields the number of elements of type `T` between the pointers, represented as a signed integer of type `ptrdiff_t` (`%td`), **NOT** raw byte distance.

### The Double Pointer Rule for Pass-by-Reference

* In C, **all function arguments are passed by value**.

* To mutate a variable of type `T` in the caller: pass `T*`.

* To mutate a pointer variable of type `T*` in the caller (e.g., allocating memory, advancing head pointer): pass `T**`.

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Memory Representation & Dereferencing in Assembly

A pointer is an unsigned integer (32-bit on x86, 64-bit on x86_64) that stores a virtual memory address.

```c
int x = 42;
int *p = &x;
int y = *p;
```

#### Corresponding x86_64 Assembly:

```nasm
mov DWORD PTR [rbp-12], 42 ; x = 42
lea rax, [rbp-12] ; rax = Address of x (Load Effective Address)
mov QWORD PTR [rbp-8], rax ; p = rax (&x stored as 64-bit pointer)
mov rax, QWORD PTR [rbp-8] ; rax = value of p (address of x)
mov eax, DWORD PTR [rax] ; eax = *p (Dereference: Read 4 bytes at [rax])
mov DWORD PTR [rbp-16], eax ; y = eax
```

---

### B. Valid Pointer Arithmetic & The One-Past-The-End Rule (C17 §6.5.6)

Pointer arithmetic is strictly defined only when navigating within the bounds of an array object or **exactly one element past the end** of the array.

```text
Array: int arr[4] -> [ arr[0] ] [ arr[1] ] [ arr[2] ] [ arr[3] ] | [ Past-the-end ]
Address: 0x1000 0x1004 0x1008 0x100C | 0x1010
Pointers: &arr[0] &arr[1] &arr[2] &arr[3] | arr + 4 (Valid to calculate, ILLEGAL to dereference!)
```

* Calculating `arr + 4` is legal and standard-compliant (frequently used as end-sentinel in loops like `for (int *p = arr; p < arr + 4; p++)`).

* Calculating `arr + 5` or `arr - 1` is **Undefined Behavior**, even if the pointer is never dereferenced!

---

### C. Double Pointers (`T**`) and Memory Allocation Interfaces

Consider allocating memory inside a helper function:

```c
// BROKEN: ptr is passed by value (copy of caller's pointer)
void allocate_broken(int *ptr, size_t n) {
ptr = (int *)malloc(n * sizeof(int)); // Modifies local copy; caller's pointer remains NULL!
}
// CORRECT: Pass pointer-to-pointer so we can mutate caller's original pointer variable
bool allocate_correct(int **out_ptr, size_t n) {
if (out_ptr == NULL || n == 0) return false;
*out_ptr = (int *)malloc(n * sizeof(int));
return (*out_ptr != NULL);
}
```

```text
Caller Stack Frame Callee Stack Frame
┌─────────────────────────┐ ┌─────────────────────────┐
│ int *my_array = NULL; │◄──────┼── int **out_ptr │
│ (Address: 0x7fff_0010) │ │ (Value: 0x7fff_0010) │
└─────────────────────────┘ └─────────────────────────┘
│
▼
*out_ptr = malloc(...)
(Writes heap address into 0x7fff_0010)
```

---

### D. Generic Polymorphism with `void*`

A `void*` is a generic pointer to an untyped memory chunk.

* Standard C forbids direct arithmetic or dereferencing of `void*` because `sizeof(void)` is undefined.

* To perform byte-level arithmetic or memory copies on `void*`, explicitly cast to `uint8_t*` or `unsigned char*` (guaranteed by C standard to have `sizeof == 1` and no padding).

```c
void generic_mem_swap(void *a, void *b, size_t size) {
uint8_t *p1 = (uint8_t *)a;
uint8_t *p2 = (uint8_t *)b;
for (size_t i = 0; i < size; i++) {
uint8_t temp = p1[i];
p1[i] = p2[i];
p2[i] = temp;
}
}
```

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Generic Byte-Level Circular Ring Buffer (`generic_ringbuf`)

#### Objective

Build a type-agnostic, generic circular ring buffer in pure C using `void*` payload storage, dynamic double-pointer lifecycle allocation, and byte-level memory strides.

#### Functional Requirements

1. **Lifecycle Management:**

* `bool ringbuf_create(RingBuffer **out_rb, size_t capacity, size_t elem_size)`: Allocates the container and internal raw byte array.

* `void ringbuf_destroy(RingBuffer **rb_ptr)`: Frees internal memory and sets the caller's pointer to `NULL`.

2. **Buffer Operations:**

* `bool ringbuf_push(RingBuffer *rb, const void *elem_data)`: Copies `elem_size` bytes into the head index. Fails if buffer is full.

* `bool ringbuf_pop(RingBuffer *rb, void *out_data)`: Copies `elem_size` bytes from the tail index into destination. Fails if buffer is empty.

* `bool ringbuf_peek(const RingBuffer *rb, void *out_data)`: Inspects tail element without consuming.

3. **Byte Stride Arithmetic:** Calculate element offsets using `(uint8_t *)rb->buffer + (index * rb->elem_size)` with `memcpy`.

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
typedef struct {
uint8_t *data; // Raw contiguous byte storage
size_t elem_size; // Size of each individual element in bytes
size_t capacity; // Maximum number of elements
size_t head; // Write index
size_t tail; // Read index
size_t count; // Current item count
} RingBuffer;
bool ringbuf_create(RingBuffer **out_rb, size_t capacity, size_t elem_size) {
if (out_rb == NULL || capacity == 0 || elem_size == 0) {
return false;
}
RingBuffer *rb = (RingBuffer *)malloc(sizeof(RingBuffer));
if (rb == NULL) return false;
rb->data = (uint8_t *)malloc(capacity * elem_size);
if (rb->data == NULL) {
free(rb);
return false;
}
rb->capacity = capacity;
rb->elem_size = elem_size;
rb->head = 0;
rb->tail = 0;
rb->count = 0;
*out_rb = rb;
return true;
}
void ringbuf_destroy(RingBuffer **rb_ptr) {
if (rb_ptr == NULL || *rb_ptr == NULL) return;
RingBuffer *rb = *rb_ptr;
if (rb->data != NULL) {
free(rb->data);
rb->data = NULL;
}
free(rb);
*rb_ptr = NULL; // Defensively zero out caller pointer
}
bool ringbuf_push(RingBuffer *rb, const void *elem_data) {
if (rb == NULL || elem_data == NULL || rb->count == rb->capacity) {
return false; // Buffer full or invalid
}
uint8_t *dest = rb->data + (rb->head * rb->elem_size);
memcpy(dest, elem_data, rb->elem_size);
rb->head = (rb->head + 1) % rb->capacity;
rb->count++;
return true;
}
bool ringbuf_pop(RingBuffer *rb, void *out_data) {
if (rb == NULL || out_data == NULL || rb->count == 0) {
return false; // Buffer empty or invalid
}
const uint8_t *src = rb->data + (rb->tail * rb->elem_size);
memcpy(out_data, src, rb->elem_size);
rb->tail = (rb->tail + 1) % rb->capacity;
rb->count--;
return true;
}
typedef struct {
int id;
double reading;
char label[16];
} SensorPacket;
int main(void) {
printf("=== Testing Generic Ring Buffer with Structs ===\n");
RingBuffer *sensor_queue = NULL;
bool ok = ringbuf_create(&sensor_queue, 4, sizeof(SensorPacket));
assert(ok && sensor_queue != NULL);
SensorPacket p1 = { .id = 1, .reading = 23.5, .label = "TEMP_SENS_1" };
SensorPacket p2 = { .id = 2, .reading = 99.1, .label = "PRESS_SENS_2" };
SensorPacket p3 = { .id = 3, .reading = 14.2, .label = "HUMID_SENS_3" };
ringbuf_push(sensor_queue, &p1);
ringbuf_push(sensor_queue, &p2);
ringbuf_push(sensor_queue, &p3);
SensorPacket popped;
while (ringbuf_pop(sensor_queue, &popped)) {
printf("[Popped Packet] ID: %d | Val: %.2f | Label: %s\n",
popped.id, popped.reading, popped.label);
}
ringbuf_destroy(&sensor_queue);
assert(sensor_queue == NULL);
printf("Ring buffer destroyed and pointer nullified safely.\n");
return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The `realloc` Leak, Unsafe `void*` Stride & Wild Pointer Flaw

Examine the following buggy dynamic array resizing function:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// BUGGY IMPLEMENTATION
void resize_and_insert(void *array_ptr, size_t *capacity, size_t elem_size, const void *new_item) {
// BUG 1: Overwriting array_ptr directly with realloc.
// If realloc fails, it returns NULL, and the original allocated memory address is lost -> Irreversible Memory Leak!
array_ptr = realloc(array_ptr, (*capacity * 2) * elem_size);
// BUG 2: Caller passed array_ptr by VALUE.
// Even if realloc moves memory to a new address, the caller's pointer is NEVER updated!
// BUG 3: Arithmetic on void* directly (array_ptr + offset) is non-standard ISO C!
void *target_slot = array_ptr + (*capacity * elem_size);
memcpy(target_slot, new_item, elem_size);
*capacity *= 2;
}
```

### Analysis of Vulnerabilities:

1. **The `realloc` Pointer Nullification Trap:** When `p = realloc(p, new_size)` fails, it returns `NULL`, but the original memory block at `p` remains allocated. Assigning the return value directly to `p` destroys the only reference to that block, causing an immediate memory leak.

2. **Missing Indirection (`void**`):** `realloc` frequently moves the memory block to a new base address. Passing `void *array_ptr` only modifies a local copy on the stack, leaving the caller holding a dangling pointer to deallocated memory.

3. **Invalid `void*` Arithmetic:** Arithmetic on `void*` violates ISO C rules because `sizeof(void)` is incomplete.

### Defensive Fix:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
bool resize_and_insert_safe(void **array_ptr_addr, size_t *capacity, size_t elem_size, const void *new_item) {
if (array_ptr_addr == NULL || capacity == NULL || elem_size == 0 || new_item == NULL) {
return false;
}
size_t current_cap = *capacity;
size_t new_cap = (current_cap == 0) ? 4 : current_cap * 2;
// Check for potential integer overflow during size multiplication
if (new_cap > SIZE_MAX / elem_size) {
fprintf(stderr, "Defensive Error: Requested capacity overflow!\n");
return false;
}
// Fix 1 & 2: Use temporary pointer and update through pointer-to-pointer
void *new_block = realloc(*array_ptr_addr, new_cap * elem_size);
if (new_block == NULL) {
fprintf(stderr, "Defensive Error: realloc failed! Original buffer preserved.\n");
return false;
}
// Update caller's pointer to the newly allocated block
*array_ptr_addr = new_block;
// Fix 3: Perform standard-compliant byte offset arithmetic using uint8_t*
uint8_t *target_slot = (uint8_t *)new_block + (current_cap * elem_size);
memcpy(target_slot, new_item, elem_size);
*capacity = new_cap;
return true;
}
```
