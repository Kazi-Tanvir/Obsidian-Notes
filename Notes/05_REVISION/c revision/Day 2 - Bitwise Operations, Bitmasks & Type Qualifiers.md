\-\--

tags:

\- c

\- bitwise-operations

\- bitmasks

\- type-qualifiers

\- const-volatile-restrict

date: 2026-08-24

day: 2

\-\--

\# Day 2: Bitwise Operations, Bitmasks, Shift Semantics & Type Qualifiers

\-\--

\## 1. Quick Reference & Cheat Sheet

\### Bitwise Operators

\| Operator \| Name \| Syntax \| Example (\`a = 0b0101\`, \`b = 0b0011\`) \| Result \|

\| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \|

\| \`&\` \| Bitwise AND \| \`a & b\` \| \`0101 & 0011\` \| \`0001\` \|

\| \`\\\|\` \| Bitwise OR \| \`a \\\| b\` \| \`0101 \\\| 0011\` \| \`0111\` \|

\| \`\^\` \| Bitwise XOR \| \`a \^ b\` \| \`0101 \^ 0011\` \| \`0110\` \|

\| \`\~\` \| Bitwise NOT (Complement) \| \`\~a\` \| \`\~0101\` (8-bit) \| \`1010\` (\`0xFA\`) \|

\| \`\<\<\` \| Left Shift \| \`a \<\< 1\` \| \`0101 \<\< 1\` \| \`1010\` (Multiply by 2) \|

\| \`\>\>\` \| Right Shift \| \`a \>\> 1\` \| \`0101 \>\> 1\` \| \`0010\` (Divide by 2) \|

\### Essential Bit Manipulation Idioms

\`\`\`c

// Assume x is uint32_t, k is bit index (0 to 31)

x \|= (1U \<\< k); // Set bit k

x &= \~(1U \<\< k); // Clear bit k

x \^= (1U \<\< k); // Toggle / flip bit k

bool is_set = (x & (1U \<\< k)) != 0; // Test bit k

x &= (x - 1); // Clear the lowest set bit (Brian Kernighan\'s Algorithm)

uint32_t lsb = x & (-x); // Isolate the lowest set bit

bool is_pow2 = (x != 0) && ((x & (x - 1)) == 0); // Check if power of 2

\`\`\`

\### Type Qualifiers Summary

\| Qualifier \| Core Purpose \| Compiler Impact \|

\| :\-\-- \| :\-\-- \| :\-\-- \|

\| \`const\` \| Declares an object read-only \| Prevents accidental modification; enables placement in \`.rodata\`. \|

\| \`volatile\` \| Informs compiler value can change outside code flow \| Disables register caching; forces memory read/write on every access. \|

\| \`restrict\` \| Guarantees pointer is the sole alias to target memory \| Enables aggressive loop unrolling, register caching, and SIMD vectorization. \|

\| \`register\` \| Suggests storing variable directly in CPU register \| Variable address cannot be taken (\`&var\` is illegal). \|

\-\--

\## 2. In-Depth Theory & Low-Level Mechanics

\### A. Shift Semantics: Logical vs Arithmetic Shifts

When shifting bits to the right (\`\>\>\`):

1\. \*\*Unsigned Types (\`uint32_t\`):\*\* Always perform a \*\*Logical Shift\*\* (\`shr\` instruction on x86). Zeroes are shifted into the most significant bit (MSB).

2\. \*\*Signed Types (\`int32_t\`):\*\* Almost universally perform an \*\*Arithmetic Shift\*\* (\`sar\` instruction on x86). The sign bit (MSB) is copied into vacated positions to preserve the two\'s complement sign.

\`\`\`text

Logical Shift (uint8_t: 0b10001100 \>\> 2):

10001100 -\> 00100011 (Vacated MSBs filled with 0)

Arithmetic Shift (int8_t: 0b10001100 \>\> 2):

10001100 -\> 11100011 (Vacated MSBs filled with Sign Bit 1)

\`\`\`

\#### Undefined Behavior (UB) Traps in Shifts:

\* \*\*Shift Count \$\\ge\$ Width:\*\* Shifting a 32-bit integer by 32 or more positions (\`x \<\< 32\`) is \*\*Undefined Behavior\*\*.

\* \*\*Negative Shift Count:\*\* \`x \<\< -1\` is \*\*Undefined Behavior\*\*.

\* \*\*Left Shifting Negative Signed Integers:\*\* In standard C, left-shifting a negative signed integer (\`(-5) \<\< 2\`) or shifting a positive signed integer such that it overflows into the sign bit is \*\*Undefined Behavior\*\*.

\* \*\*Rule of Thumb:\*\* Always use unsigned integer literals (\`1U \<\< k\`, \`1ULL \<\< k\`) when constructing bitmasks.

\-\--

\### B. Pointer \`const\` Semantics (The \"Clockwise / Right-to-Left\" Rule)

Decipher pointer declarations by reading from the variable name right-to-left:

\`\`\`c

int val = 10;

int other = 20;

// 1. Pointer to const int: Data cannot be changed through pointer; pointer can be redirected.

const int \*p1 = &val;

// \*p1 = 15; // ERROR: Assignment of read-only location

p1 = &other; // OK: Pointer itself is mutable

// 2. Const pointer to int: Data can be changed; pointer cannot be redirected.

int \* const p2 = &val;

\*p2 = 15; // OK: Target memory is mutable

// p2 = &other; // ERROR: Assignment of read-only variable

// 3. Const pointer to const int: Neither data nor pointer can change.

const int \* const p3 = &val;

// \*p3 = 15; // ERROR

// p3 = &other; // ERROR

\`\`\`

\-\--

\### C. \`volatile\` & Hardware Access

The \`volatile\` qualifier informs the compiler that the value of an object may be modified by external forces (hardware registers, interrupt service routines, multi-threaded memory-mapped I/O) without the compiler\'s knowledge.

\#### Why \`volatile\` is Critical:

\`\`\`c

// WITHOUT volatile:

int status_flag = 0;

void wait_for_hardware(void) {

// Compiler optimizer assumes \'status_flag\' cannot change inside this loop.

// Optimization: Loads \'status_flag\' into register once, turns into \"while(1)\" if 0!

while (status_flag == 0) {

// Wait

}

}

// WITH volatile:

volatile int status_flag = 0;

void wait_for_hardware(void) {

// Compiler generates explicit memory load instruction (e.g. MOV from RAM/bus) on EVERY iteration.

while (status_flag == 0) {

// Wait

}

}

\`\`\`

\-\--

\### D. The \`restrict\` Qualifier (C99) & Pointer Aliasing

When two pointers of the same type point to overlapping memory, they are \*\*aliased\*\*. The compiler must conservatively reload data across pointers because writes through one could affect reads from the other.

Declaring a pointer as \`int \* restrict ptr\` is a programmer\'s contract that throughout the pointer\'s lifetime, the object it points to will \*\*only\*\* be accessed through that specific pointer.

\`\`\`c

// Without restrict: Compiler must reload \*b on every loop iteration in case \'a\' and \'b\' overlap.

void add_arrays(size_t n, int \*a, const int \*b) {

for (size_t i = 0; i \< n; i++) {

a\[i\] += \*b;

}

}

// With restrict: Compiler caches \*b in a CPU register once and vectorizes the loop with SIMD!

void add_arrays_fast(size_t n, int \* restrict a, const int \* restrict b) {

for (size_t i = 0; i \< n; i++) {

a\[i\] += \*b;

}

}

\`\`\`

\-\--

\## 3. Thoughtful Mini-Project (\~1 Hour Scope)

\### Project Title: Hardware Device Register Emulator & Bitfield Protocol Frame Encoder (\`bitflags_proto\`)

\#### Objective

Build a modular C utility that models a 32-bit hardware status register using bitmasks and serializes/deserializes a packed 32-bit network telemetry frame without relying on non-portable compiler-dependent struct bit-fields.

\#### Functional Requirements

1\. \*\*Device Status Register Manager:\*\*

Model a 32-bit register with specific flag bits:

\* Bit 0: \`DEVICE_POWER_ON\`

\* Bit 1: \`DEVICE_TX_READY\`

\* Bit 2: \`DEVICE_RX_READY\`

\* Bit 3: \`DEVICE_IRQ_PENDING\`

\* Bits 4--7: \`DEVICE_ERROR_CODE\` (4-bit error state: 0 to 15)

\* Bits 8--11: \`DEVICE_MODE\` (4-bit mode selector)

Implement helper functions to set, clear, toggle, and read flags/fields with mask/shift macros.

2\. \*\*Telemetry Frame Bit-Packing Engine:\*\*

Pack a structured header into a single \`uint32_t\`:

\* Version (4 bits): Bits \[31:28\]

\* Priority (2 bits): Bits \[27:26\]

\* Command ID (6 bits): Bits \[25:20\]

\* Reserved (4 bits): Bits \[19:16\] (Must always be \`0b0000\`)

\* Checksum (16 bits): Bits \[15:0\] (XOR fold of payload)

3\. \*\*Validator & Decoder:\*\*

Implement unpacking functions that extract each field and assert validity of reserved bits and parity.

\#### Starter Code Structure

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<assert.h\>

// Register Bit Definitions

#define REG_POWER_ON (1U \<\< 0)

#define REG_TX_READY (1U \<\< 1)

#define REG_RX_READY (1U \<\< 2)

#define REG_IRQ_PENDING (1U \<\< 3)

#define REG_ERR_MASK (0x0FU \<\< 4)

#define REG_ERR_SHIFT 4

#define REG_MODE_MASK (0x0FU \<\< 8)

#define REG_MODE_SHIFT 8

// Frame Packing Macros

#define FRAME_VER_SHIFT 28

#define FRAME_PRIO_SHIFT 26

#define FRAME_CMD_SHIFT 20

#define FRAME_CKSUM_MASK 0xFFFFU

typedef struct {

uint8_t version; // 4-bit (0-15)

uint8_t priority; // 2-bit (0-3)

uint8_t cmd_id; // 6-bit (0-63)

uint16_t checksum; // 16-bit

} TelemetryFrame;

uint32_t pack_frame(const TelemetryFrame \*frame) {

assert(frame != NULL);

assert(frame-\>version \<= 0x0F);

assert(frame-\>priority \<= 0x03);

assert(frame-\>cmd_id \<= 0x3F);

uint32_t packed = 0;

packed \|= ((uint32_t)(frame-\>version & 0x0F)) \<\< FRAME_VER_SHIFT;

packed \|= ((uint32_t)(frame-\>priority & 0x03)) \<\< FRAME_PRIO_SHIFT;

packed \|= ((uint32_t)(frame-\>cmd_id & 0x3F)) \<\< FRAME_CMD_SHIFT;

// Reserved bits \[19:16\] remain 0

packed \|= ((uint32_t)frame-\>checksum) & FRAME_CKSUM_MASK;

return packed;

}

bool unpack_frame(uint32_t packed, TelemetryFrame \*out_frame) {

if (out_frame == NULL) return false;

// Validate reserved bits \[19:16\] are strictly zero

if ((packed & (0x0FU \<\< 16)) != 0) {

fprintf(stderr, \"Protocol Error: Reserved bits are not zero!\\n\");

return false;

}

out_frame-\>version = (uint8_t)((packed \>\> FRAME_VER_SHIFT) & 0x0F);

out_frame-\>priority = (uint8_t)((packed \>\> FRAME_PRIO_SHIFT) & 0x03);

out_frame-\>cmd_id = (uint8_t)((packed \>\> FRAME_CMD_SHIFT) & 0x3F);

out_frame-\>checksum = (uint16_t)(packed & FRAME_CKSUM_MASK);

return true;

}

int main(void) {

// 1. Test Register Manipulation

uint32_t reg = 0;

reg \|= REG_POWER_ON \| REG_TX_READY; // Enable power and TX

// Set error code 5 (0b0101)

reg = (reg & \~REG_ERR_MASK) \| ((5U \<\< REG_ERR_SHIFT) & REG_ERR_MASK);

printf(\"Register Value: 0x%08X\\n\", reg);

printf(\"Power On: %s\\n\", (reg & REG_POWER_ON) ? \"YES\" : \"NO\");

printf(\"Extracted Error Code: %u\\n\", (reg & REG_ERR_MASK) \>\> REG_ERR_SHIFT);

// 2. Test Frame Serialization

TelemetryFrame original = { .version = 1, .priority = 2, .cmd_id = 42, .checksum = 0xABCD };

uint32_t packet = pack_frame(&original);

printf(\"\\nSerialized Frame: 0x%08X\\n\", packet);

TelemetryFrame decoded = {0};

bool ok = unpack_frame(packet, &decoded);

assert(ok && decoded.cmd_id == 42 && decoded.checksum == 0xABCD);

printf(\"Frame unpacked and verified successfully!\\n\");

return 0;

}

\`\`\`

\-\--

\## 4. Error Handling & Defensive Programming Challenge

\### Scenario: The Signed Mask Inversion & Shift Overflow Trap

Examine the following buggy security permission check function:

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

// BUGGY IMPLEMENTATION

bool is_permission_granted(uint32_t user_flags, int8_t permission_bit_index) {

// Requirements:

// 1. Bit index must be valid (0 to 31).

// 2. Bit 31 represents SUPERUSER mode. If set, always grant.

// BUG 1: Left shift of signed 1 by 31 overflows signed 32-bit int -\> UB!

uint32_t superuser_mask = (1 \<\< 31);

if ((user_flags & superuser_mask) != 0) {

return true;

}

// BUG 2: Negative bit index or bit index \>= 32 causes Undefined Behavior in shift.

uint32_t target_mask = (1 \<\< permission_bit_index);

return (user_flags & target_mask) != 0;

}

\`\`\`

\### Analysis of Vulnerabilities:

1\. \*\*Signed Overflow in \`(1 \<\< 31)\`:\*\* In C, integer literal \`1\` is a signed \`int\` (32-bit). Shifting \`1\` left by 31 bits overflows the sign bit, which is \*\*Undefined Behavior\*\*.

2\. \*\*Missing Input Bounds:\*\* If \`permission_bit_index\` is negative (e.g. \`-1\`) or greater than 31, \`1 \<\< permission_bit_index\` invokes undefined behavior.

3\. \*\*Implicit Sign Extension in Mask Inversions:\*\* When working with types smaller than \`int\` (e.g. \`uint8_t mask = 0x01; \~mask\`), the operand is promoted to signed \`int\` before inversion, producing \`0xFFFFFFFE\`. If right shifted or compared incorrectly without casting, sign bits corrupt the result.

\### Defensive Fix:

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#define SUPERUSER_BIT_INDEX 31U

bool is_permission_granted_safe(uint32_t user_flags, uint8_t permission_bit_index, bool \*out_is_granted) {

if (out_is_granted == NULL) {

return false;

}

// Defensive Check: Validate bit index strictly within 32-bit boundary

if (permission_bit_index \> 31U) {

fprintf(stderr, \"Defensive Error: Permission bit index (%u) out of bounds \[0-31\]\\n\",

permission_bit_index);

return false;

}

// Fix: Explicitly use unsigned literal 1U to avoid UB

uint32_t superuser_mask = (1U \<\< SUPERUSER_BIT_INDEX);

if ((user_flags & superuser_mask) != 0U) {

\*out_is_granted = true;

return true;

}

uint32_t target_mask = (1U \<\< permission_bit_index);

\*out_is_granted = ((user_flags & target_mask) != 0U);

return true;

}

\`\`\`
