**Tags:** c, defensive-programming, undefined-behavior, sanitizers,
addresssanitizer, ubsan\
**Date:** 2026-09-17\
**Day:** 26

Day 26: Defensive Programming, Undefined Behavior (UB) Pitfalls,
Compiler Sanitizers & Static Analysis

# 1. Quick Reference & Cheat Sheet

## Behavior Classifications in C (ISO C11 / C17)

- **Undefined Behavior (UB):** The standard imposes **no requirements**.
  The compiler assumes UB never happens; if it does, the compiler can
  crash, emit random machine code, reorder memory operations, or
  optimize away security checks.

  - *Examples:* Signed integer overflow, dereferencing NULL,
    use-after-free, out-of-bounds pointer indexing, uninitialized
    variable reads.

- **Unspecified Behavior:** Two or more valid behaviors allowed; the
  implementation is **not required to document** which it chooses.

  - *Example:* Function argument evaluation order (f(g(), h())), memory
    layout order of non-consecutive allocations.

- **Implementation-Defined Behavior:** The compiler must choose one
  behavior and **document it in the compiler manual**.

  - *Examples:* Size of int and pointer width, representation of
    negative numbers (two\'s complement), endianness, right-shift of
    negative signed integers (arithmetic vs logical shift).

## Modern Compiler Sanitizers (GCC & Clang)

Compile and link with these flags during development and testing:# Core
Sanitizer Suite (Address + Leak + Undefined Behavior)

CFLAGS += -fsanitize=address,undefined,leak -fno-omit-frame-pointer -g
-O1

\# Thread Sanitizer (Data race detection - MUTUALLY EXCLUSIVE with
AddressSanitizer!)

CFLAGS += -fsanitize=thread -fno-omit-frame-pointer -g -O1

  -----------------------------------------------------------------------
  Sanitizer Flag          Target Bugs Detected    Performance Overhead
  ----------------------- ----------------------- -----------------------
  -fsanitize=address      Out-of-bounds           \~2x CPU slowdown,
  (ASan)                  heap/stack/global,      \~2-3x memory
                          use-after-free,         
                          double-free             

  -fsanitize=undefined    Signed integer          \~5-20% CPU slowdown
  (UBSan)                 overflow, misalignment, 
                          invalid shift, null     
                          dereference             

  -fsanitize=leak (LSan)  Memory leaks on process Minimal
                          termination (integrated 
                          into ASan on Linux)     

  -fsanitize=thread       Data races, deadlocks,  \~3-5x CPU slowdown,
  (TSan)                  lock order inversion    \~5-10x memory
                          between threads         
  -----------------------------------------------------------------------

## Hardening Flags for Production Builds

HARDENING_FLAGS := -Wall -Wextra -Wpedantic \\

-Wconversion -Wsign-conversion \\

-Wshadow -Wstrict-prototypes \\

-Werror=implicit-function-declaration \\

-Wformat=2 -Wformat-security \\

-fstack-protector-strong \\

-D_FORTIFY_SOURCE=2 \\

-fPIE -pie -Wl,-z,relro,-z,now

# 2. In-Depth Theory & Low-Level Mechanics

## A. How Compilers Exploit Undefined Behavior (The Optimization Paradox)

Modern optimizing compilers (GCC, Clang) operate on a fundamental axiom:
The programmer writes strictly conforming code that will never trigger
Undefined Behavior.

If a code path triggers UB, the compiler reasons:*\"Because UB is not
allowed to occur, this execution path is mathematically impossible.
Therefore, I can eliminate all branches that assume it happens.\"*

### Case Study: The Vanishing Buffer Check

Consider this innocent-looking bounds check:void process_packet(char
\*buffer, int offset) {

// Programmer thinks: \"Check if offset wrapped around backwards\"

if (buffer + offset \< buffer) { // BUG: UB in C!

abort(); // Danger: Security check

}

buffer\[offset\] = 0xAA;

}

- **Low-Level Reality:** The ISO C standard states that pointer
  arithmetic is only valid within the bounds of an allocated object
  (plus one past the end). Adding an offset that wraps around the 64-bit
  address space is **Undefined Behavior**.

- **Compiler Transformation:** Since buffer + offset \< buffer can only
  be true if pointer arithmetic wrapped around, and wrapping around is
  UB, the compiler deduces that buffer + offset \< buffer is **always
  FALSE**.

- **Resulting Assembly:** The entire if condition and the call to
  abort() are completely deleted from the binary under -O2/-O3! The
  security gate vanishes.

## B. The Strict Aliasing Rule & Safe Type Punning

The **Strict Aliasing Rule** (ISO C11 §6.5/7) specifies that two
pointers of different types cannot point to the same memory location,
with two notable exceptions:

1.  Pointers to char, unsigned char, or signed char (the universal byte
    aliases).

2.  Pointers to structs or unions containing the type.

### The Violation:

// ILLEGAL: Violates Strict Aliasing

float f = 5.0f;

uint32_t \*u = (uint32_t \*)&f; // UB!

\*u = 0x41200000;

printf(\"f = %f\\n\", f); // Compiler may optimize this to print
5.000000!

Under -O3, the compiler assumes writes through u cannot affect f because
their types cannot alias. It caches f in a SIMD/FPU register (%xmm0) and
never reloads it from RAM.

### The Safe, Modern Solutions:

// Method 1: memcpy (Zero-overhead: modern compilers optimize this to a
single MOV instruction!)

float f = 5.0f;

uint32_t u;

memcpy(&u, &f, sizeof(u));

// Method 2: Union Punning (Explicitly guaranteed valid in ISO C99/C11
§6.5.2.3, unlike C++)

union FloatBits {

float f;

uint32_t u;

};

union FloatBits fb;

fb.f = 5.0f;

uint32_t bits = fb.u; // Fully legal in standard C

## C. Anatomy of AddressSanitizer (ASan): Shadow Memory

How does -fsanitize=address detect an out-of-bounds write without
slowing down the code by 100x?

- **Virtual Address Space Division:** ASan maps every 8 bytes of
  application memory to **1 byte of Shadow Memory**:\
  \$\$\\text{Shadow Address} = (\\text{Address} \\gg 3) +
  \\text{Offset}\$\$

- **Shadow Byte Encoding:**

  - 0x00: All 8 bytes of application memory are addressable.

  - 0x01--0x07: The first \$k\$ bytes are addressable; the rest are
    poisoned.

  - Negative / High values (0xF1, 0xF2, 0xF3, etc.): Redzones, freed
    heap memory, stack buffer overflows.

Application Memory (8 Bytes): Shadow Memory (1 Byte):

┌───┬───┬───┬───┬───┬───┬───┬───┐ ┌────────┐

│ B0│ B1│ B2│ B3│ B4│ B5│ B6│ B7│ ───────► │ 0x00 │ (Valid)

└───┴───┴───┴───┴───┴───┴───┴───┘ └────────┘

Heap Allocation with Redzones:

┌────────────────────┬───────────────────────┬────────────────────┐

│ Redzone (Poisoned) │ User Object (8 Bytes) │ Redzone (Poisoned) │

│ Shadow: 0xFA │ Shadow: 0x00 │ Shadow: 0xFA │

└────────────────────┴───────────────────────┴────────────────────┘

- **Instruction Instrumentation:**\
  Before every 1-byte read or store, the compiler inserts:movq %rax,
  %rcx

> shrq \$3, %rcx
>
> movb 0x7fff8000(%rcx), %dl ; Read shadow byte
>
> testb %dl, %dl
>
> jnz .report_asan_error ; Fast path is a single branch!
>
> movb (%rax), %bl ; Original application load

# 3. Thoughtful Mini-Project (\~1 Hour Scope)

## Project Title: Defensive Memory-Safe Dynamic Buffer (safe_buffer)

### Objective

Build a memory-hardened dynamic byte and string buffer in C that
proactively prevents integer overflow during allocation scaling, guards
against NULL dereferencing, detects boundary violations, and securely
zeroes out memory upon deallocation.

### Requirements

1.  **Overflow-Resistant Resizing:** Use compiler built-ins
    (\_\_builtin_mul_overflow / \_\_builtin_add_overflow) or portable
    saturation arithmetic to prevent memory allocation integer wrapping.

2.  **Explicit Bounds Checking:** All read/write operations must return
    a strict BufferStatus enum.

3.  **Secure Scrubbing:** Memory deallocation must scrub heap bytes
    using a compiler-memory-barrier zeroing function (memset_s or
    explicit volatile scrub) to prevent use-after-free data leaks.

4.  **Compile-Time Static Assertions:** Enforce structural alignment and
    pointer width invariants.

### Complete Implementation (safe_buffer.c)

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<string.h\>

#include \<assert.h\>

/\* Compile-time architectural invariants \*/

\_Static_assert(sizeof(void \*) == 8, \"This engine strictly targets
64-bit architecture\");

\_Static_assert(sizeof(size_t) \>= 8, \"size_t must be at least 64
bits\");

typedef enum {

BUF_OK = 0,

BUF_ERR_NULL_PTR = -1,

BUF_ERR_OUT_OF_BOUNDS = -2,

BUF_ERR_OVERFLOW = -3,

BUF_ERR_OUT_OF_MEMORY = -4

} BufferStatus;

typedef struct {

uint8_t \*data;

size_t size;

size_t capacity;

uint32_t canary_head;

uint32_t canary_tail;

} SafeBuffer;

#define BUFFER_CANARY 0xDEADBEEF

/\* Secure memory scrubbing that the optimizer cannot eliminate \*/

static void secure_zero(void \*ptr, size_t len) {

if (!ptr \|\| len == 0) return;

volatile uint8_t \*p = (volatile uint8_t \*)ptr;

while (len\--) {

\*p++ = 0;

}

}

BufferStatus buffer_init(SafeBuffer \*buf, size_t initial_cap) {

if (!buf) return BUF_ERR_NULL_PTR;

if (initial_cap == 0) initial_cap = 16;

if (initial_cap \> (SIZE_MAX / 2)) return BUF_ERR_OVERFLOW;

buf-\>data = (uint8_t \*)malloc(initial_cap);

if (!buf-\>data) return BUF_ERR_OUT_OF_MEMORY;

buf-\>size = 0;

buf-\>capacity = initial_cap;

buf-\>canary_head = BUFFER_CANARY;

buf-\>canary_tail = BUFFER_CANARY;

return BUF_OK;

}

static BufferStatus buffer_grow_checked(SafeBuffer \*buf, size_t
required_capacity) {

if (required_capacity \<= buf-\>capacity) return BUF_OK;

size_t new_cap = buf-\>capacity;

while (new_cap \< required_capacity) {

size_t doubled_cap;

// Check for integer multiplication overflow

#if defined(\_\_has_builtin) &&
\_\_has_builtin(\_\_builtin_mul_overflow)

if (\_\_builtin_mul_overflow(new_cap, 2, &doubled_cap)) {

return BUF_ERR_OVERFLOW;

}

#else

if (new_cap \> (SIZE_MAX / 2)) {

return BUF_ERR_OVERFLOW;

}

doubled_cap = new_cap \* 2;

#endif

new_cap = doubled_cap;

}

uint8_t \*new_data = (uint8_t \*)realloc(buf-\>data, new_cap);

if (!new_data) return BUF_ERR_OUT_OF_MEMORY;

buf-\>data = new_data;

buf-\>capacity = new_cap;

return BUF_OK;

}

BufferStatus buffer_append(SafeBuffer \*buf, const void \*src, size_t
len) {

if (!buf \|\| !src) return BUF_ERR_NULL_PTR;

if (buf-\>canary_head != BUFFER_CANARY \|\| buf-\>canary_tail !=
BUFFER_CANARY) {

fprintf(stderr, \"\[FATAL\] Buffer canary corruption detected!\\n\");

abort();

}

size_t needed;

#if defined(\_\_has_builtin) &&
\_\_has_builtin(\_\_builtin_add_overflow)

if (\_\_builtin_add_overflow(buf-\>size, len, &needed)) {

return BUF_ERR_OVERFLOW;

}

#else

if (len \> SIZE_MAX - buf-\>size) {

return BUF_ERR_OVERFLOW;

}

needed = buf-\>size + len;

#endif

BufferStatus st = buffer_grow_checked(buf, needed);

if (st != BUF_OK) return st;

memcpy(buf-\>data + buf-\>size, src, len);

buf-\>size = needed;

return BUF_OK;

}

BufferStatus buffer_read_at(const SafeBuffer \*buf, size_t offset, void
\*dest, size_t len) {

if (!buf \|\| !dest) return BUF_ERR_NULL_PTR;

size_t end_offset;

#if defined(\_\_has_builtin) &&
\_\_has_builtin(\_\_builtin_add_overflow)

if (\_\_builtin_add_overflow(offset, len, &end_offset)) {

return BUF_ERR_OVERFLOW;

}

#else

if (len \> SIZE_MAX - offset) return BUF_ERR_OVERFLOW;

end_offset = offset + len;

#endif

if (end_offset \> buf-\>size) {

return BUF_ERR_OUT_OF_BOUNDS;

}

memcpy(dest, buf-\>data + offset, len);

return BUF_OK;

}

void buffer_destroy(SafeBuffer \*buf) {

if (!buf) return;

if (buf-\>data) {

secure_zero(buf-\>data, buf-\>capacity);

free(buf-\>data);

buf-\>data = NULL;

}

buf-\>size = 0;

buf-\>capacity = 0;

buf-\>canary_head = 0;

buf-\>canary_tail = 0;

}

int main(void) {

printf(\"===================================================================\\n\");

printf(\" DEFENSIVE C BUFFER: OVERFLOW GUARDS & ASAN/UBSAN COMPATIBLE
\\n\");

printf(\"===================================================================\\n\\n\");

SafeBuffer buf;

BufferStatus st = buffer_init(&buf, 8);

assert(st == BUF_OK);

const char \*msg = \"Systems Programming with C17 Defensive
Architecture\";

st = buffer_append(&buf, msg, strlen(msg));

assert(st == BUF_OK);

printf(\"\[1\] Successfully appended %zu bytes. Current Capacity: %zu
bytes.\\n\",

buf.size, buf.capacity);

// Test 1: Out of Bounds Guard

char test_read\[64\];

st = buffer_read_at(&buf, 1000, test_read, sizeof(test_read));

assert(st == BUF_ERR_OUT_OF_BOUNDS);

printf(\"\[2\] Out-of-bounds read at offset 1000 safely rejected
(BUF_ERR_OUT_OF_BOUNDS).\\n\");

// Test 2: Arithmetic Overflow Injection

st = buffer_append(&buf, msg, SIZE_MAX - 5);

assert(st == BUF_ERR_OVERFLOW);

printf(\"\[3\] Extreme allocation size gracefully rejected with
BUF_ERR_OVERFLOW.\\n\");

buffer_destroy(&buf);

printf(\"\[4\] Buffer scrubbed with secure_zero() and destroyed cleanly
with zero leaks.\\n\");

return 0;

}

# 4. Error Handling & Defensive Programming Challenge

## Scenario: The \"Optimized-Away\" Bounds Check (Signed Overflow UB)

Examine this security check written for a network protocol packet
validator:#include \<stdio.h\>

#include \<stdlib.h\>

#include \<limits.h\>

// VULNERABLE FUNCTION: Used in an authentication token parser

int validate_and_allocate(int current_payload_len, int extension_len) {

// Programmer intent: Verify that adding extension_len does not overflow

if (current_payload_len + extension_len \< current_payload_len) { //
BUG: Signed Integer Overflow is UB!

fprintf(stderr, \"\[Security Alert\] Payload length overflow
detected!\\n\");

return -1;

}

int total_len = current_payload_len + extension_len;

char \*packet = (char \*)malloc((size_t)total_len);

if (!packet) return -1;

// Process packet\...

free(packet);

return 0;

}

## Analysis of Vulnerabilities:

1.  **The Optimization Trap:** In ISO C, signed integer addition
    overflow (current_payload_len + extension_len) is **Undefined
    Behavior**.

2.  Because UB is assumed never to happen, modern compilers (gcc -O2
    -O3) deduce that for any positive extension_len \>= 0,
    current_payload_len + extension_len **must be \$\\ge\$
    current_payload_len**.

3.  The compiler completely deletes the if (current_payload_len +
    extension_len \< current_payload_len) branch!

4.  When an attacker passes current_payload_len = 2,000,000,000 and
    extension_len = 500,000,000, the sum overflows to a negative integer
    (-1,794,967,296).

5.  Casting negative integer -1,794,967,296 to size_t inside malloc
    converts it to an astronomical positive number
    (18,446,744,071,914,584,320 bytes), causing allocation failure, or
    heap memory corruption if wrapped.

## Defensive Fix:

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<limits.h\>

int validate_and_allocate_defensive(int current_payload_len, int
extension_len) {

// DEFENSIVE RULE: Never allow the overflow operation to execute!

// Rearrange the algebra so overflow is impossible:

if (current_payload_len \< 0 \|\| extension_len \< 0) {

return -1; // Reject negative bounds immediately

}

// Check: current_payload_len + extension_len \> INT_MAX

// Rewritten without overflow: extension_len \> INT_MAX -
current_payload_len

if (extension_len \> INT_MAX - current_payload_len) {

fprintf(stderr, \"\[Security Fixed\] Prevented integer overflow before
arithmetic!\\n\");

return -1;

}

int total_len = current_payload_len + extension_len;

char \*packet = (char \*)malloc((size_t)total_len);

if (!packet) return -1;

free(packet);

return 0;

}
