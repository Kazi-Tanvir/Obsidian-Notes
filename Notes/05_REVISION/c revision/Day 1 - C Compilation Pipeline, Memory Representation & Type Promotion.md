\-\--

tags:

\- c

\- compilation-pipeline

\- memory-layout

\- integer-promotion

\- types

date: 2026-08-23

day: 1

\-\--

\# Day 1: C Compilation Pipeline, Memory Representation & Type Promotion

\-\--

\## 1. Quick Reference & Cheat Sheet

\### The 4-Stage Compilation Pipeline

\`\`\`text

Source Code (.c, .h)

│ \[Preprocessing: cpp / gcc -E\] (Expands #include, #define, strips comments)

▼

Preprocessed Source (.i)

│ \[Compilation: cc1 / gcc -S\] (Syntax analysis, AST, IR, Assembly generation)

▼

Assembly Code (.s)

│ \[Assembly: as / gcc -c\] (Translates mnemonics to machine code opcodes)

▼

Relocatable Object File (.o)

│ \[Linking: ld / gcc -o\] (Resolves symbols, static/dynamic libc, relocation)

▼

Executable Binary (a.out / ELF)

\`\`\`

\### Essential Compiler Flags (Strict Modern C Standards)

\`\`\`bash

gcc -std=c17 -Wall -Wextra -Wpedantic -Wconversion -Werror -fsanitize=address,undefined -g source.c -o program

\`\`\`

\* \`-Wall -Wextra -Wpedantic\`: Enable comprehensive compiler warnings for standard conformance.

\* \`-Wconversion\`: Warns on implicit conversions that may alter a value (critical for finding sign/truncation bugs).

\* \`-fsanitize=address,undefined\`: Runtime instrumentation for memory bugs, out-of-bounds access, and undefined behavior (UB).

\* \`-g\`: Generates DWARF debugging info for GDB / LLDB.

\### Primitive Types, Sizes & Typical Ranges (x86_64 / LP64 Data Model)

\| Type \| Bytes \| Bits \| Signed Range \| Unsigned Range \| Format Specifier \|

\| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \| :\-\-- \|

\| \`char\` / \`int8_t\` \| 1 \| 8 \| -128 to 127 \| 0 to 255 \| \`%c\` / \`%hhd\` / \`%hhu\` \|

\| \`short\` / \`int16_t\` \| 2 \| 16 \| -32,768 to 32,767 \| 0 to 65,535 \| \`%hd\` / \`%hu\` \|

\| \`int\` / \`int32_t\` \| 4 \| 32 \| -2,147,483,648 to 2,147,483,647 \| 0 to 4,294,967,295 \| \`%d\` / \`%u\` \|

\| \`long\` / \`int64_t\` \| 8 \| 64 \| \~ -9.22 × 10¹⁸ to 9.22 × 10¹⁸ \| 0 to \~ 1.84 × 10¹⁹ \| \`%ld\` / \`%lu\` \|

\| \`long long\` \| 8 \| 64 \| \~ -9.22 × 10¹⁸ to 9.22 × 10¹⁸ \| 0 to \~ 1.84 × 10¹⁹ \| \`%lld\` / \`%llu\` \|

\| \`size_t\` \| 8 \| 64 \| N/A (Unsigned) \| 0 to 2⁶⁴ - 1 \| \`%zu\` \|

\| \`ptrdiff_t\` \| 8 \| 64 \| -2⁶³ to 2⁶³ - 1 \| N/A (Signed) \| \`%td\` \|

\| \`float\` \| 4 \| 32 \| IEEE 754 Single Precision (\~7 decimal digits) \| N/A \| \`%f\` / \`%g\` \|

\| \`double\` \| 8 \| 64 \| IEEE 754 Double Precision (\~15-17 decimal digits) \| N/A \| \`%lf\` / \`%g\` \|

\-\--

\## 2. In-Depth Theory & Low-Level Mechanics

\### A. Two\'s Complement Integer Representation

Modern processors represent signed integers using \*\*Two\'s Complement\*\* arithmetic.

\* \*\*Positive Numbers:\*\* Represented as standard binary with the Most Significant Bit (MSB) as \`0\`.

\* \*\*Negative Numbers:\*\* Computed via \`(\~X) + 1\` (Bitwise NOT plus one).

\* \*\*Properties:\*\*

\* Only one representation for zero (\`00000000\`).

\* Arithmetic addition and subtraction use the exact same CPU logic gates regardless of sign.

\* Range is asymmetric: For an \$N\$-bit integer, range is \$\[-2\^{N-1}, 2\^{N-1} - 1\]\$.

\`\`\`text

Example: int8_t (-5)

+5 in binary: 0000 0101

Invert bits (\~): 1111 1010

Add 1 (+1): 1111 1011 -\> 0xFB (stored in memory)

\`\`\`

\### B. Endianness (Byte Ordering in RAM)

When a primitive type occupies multiple contiguous bytes in memory:

\* \*\*Little-Endian (x86_64, ARM default):\*\* The \*\*Least Significant Byte (LSB)\*\* is stored at the lowest memory address.

\* \*\*Big-Endian (Network Byte Order, SPARC):\*\* The \*\*Most Significant Byte (MSB)\*\* is stored at the lowest memory address.

\`\`\`text

Value: uint32_t val = 0x12345678;

Memory Address: 0x1000 0x1001 0x1002 0x1003

Little-Endian: 0x78 0x56 0x34 0x12 \<\-- Lowest byte first

Big-Endian: 0x12 0x34 0x56 0x78 \<\-- Highest byte first

\`\`\`

\### C. Integer Promotion & Usual Arithmetic Conversions

Whenever an expression involves types smaller than \`int\` (\`char\`, \`short\`, \`\_Bool\`, \`enum\`), C automatically applies \*\*Integer Promotion\*\*:

1\. If \`int\` can represent all values of the original type, the value is converted to \`int\`.

2\. Otherwise, it is converted to \`unsigned int\`.

When two operands of different types are evaluated in a binary operation (e.g. \`+\`, \`-\`, \`\*\`, \`==\`, \`\<\`, \`\>\`):

1\. Both operands are converted to a common type according to the \*\*Usual Arithmetic Conversions Hierarchy\*\*:

\`int\` \< \`unsigned int\` \< \`long\` \< \`unsigned long\` \< \`long long\` \< \`unsigned long long\` \< \`float\` \< \`double\` \< \`long double\`.

2\. \*\*The Classic Signed-Unsigned Comparison Trap:\*\*

\`\`\`c

int a = -1;

unsigned int b = 1;

if (a \< b) {

// This branch is NOT taken!

} else {

// This branch IS taken!

// Reason: \'a\' is implicitly promoted to unsigned int.

// In 32-bit two\'s complement, -1 becomes 0xFFFFFFFF (4,294,967,295).

// 4294967295 \< 1 evaluates to FALSE!

}

\`\`\`

\-\--

\## 3. Thoughtful Mini-Project (\~1 Hour Scope)

\### Project Title: Memory Hex Dump & Endianness Inspector CLI (\`memdump\`)

\#### Objective

Build a modular CLI tool in C that inspects the exact in-memory representation of any arbitrary variable, data structure, or pointer buffer, printing its memory address, raw hexadecimal bytes, and binary bit pattern, while detecting the CPU endianness dynamically.

\#### Functional Requirements

1\. \*\*Runtime Endianness Detector:\*\*

Implement a function \`int is_little_endian(void)\` that checks byte placement using a \`uint16_t\` or \`uint32_t\` test value cast to \`uint8_t\*\`.

2\. \*\*Byte-Level Memory Dumper:\*\*

Implement \`void dump_memory(const void \*ptr, size_t size, const char \*label)\`:

\* Print the variable label and starting memory address.

\* Output each byte in hex (\`0x%02X\`).

\* Output the 8-bit binary representation of each byte (\`0b\...\`).

\* Handle multi-byte primitives (\`int\`, \`double\`, negative values, arrays).

3\. \*\*Interactive Demo:\*\*

Dump and compare:

\* \`int32_t positive = 1048576;\` vs \`int32_t negative = -1048576;\`

\* \`float f_val = 3.1415926f;\` (showing IEEE 754 sign, exponent, and mantissa distribution)

\* A 4-character string vs a 32-bit integer with identical hex bytes.

\#### Starter Code Structure

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

void print_byte_binary(uint8_t byte) {

for (int i = 7; i \>= 0; i\--) {

putchar((byte & (1 \<\< i)) ? \'1\' : \'0\');

}

}

bool is_little_endian(void) {

uint16_t test = 0x0001;

uint8_t \*byte_ptr = (uint8_t \*)&test;

return byte_ptr\[0\] == 0x01;

}

void dump_memory(const void \*ptr, size_t size, const char \*label) {

const uint8_t \*bytes = (const uint8_t \*)ptr;

printf(\"\\n=== Memory Dump: %s (%zu bytes at %p) ===\\n\", label, size, ptr);

for (size_t i = 0; i \< size; i++) {

printf(\" \[+%02zu\] Addr: %p \| Hex: 0x%02X \| Bin: \", i, (void \*)(bytes + i), bytes\[i\]);

print_byte_binary(bytes\[i\]);

printf(\"\\n\");

}

}

int main(void) {

printf(\"Host System Architecture: %s-Endian\\n\", is_little_endian() ? \"Little\" : \"Big\");

int32_t signed_pos = 42;

int32_t signed_neg = -42;

float pi = 3.14159f;

dump_memory(&signed_pos, sizeof(signed_pos), \"int32_t (+42)\");

dump_memory(&signed_neg, sizeof(signed_neg), \"int32_t (-42)\");

dump_memory(&pi, sizeof(pi), \"float (3.14159)\");

return 0;

}

\`\`\`

\-\--

\## 4. Error Handling & Defensive Programming Challenge

\### Scenario: The Network Packet Length Validation Flaw

Examine the following buggy code snippet extracted from a packet parser:

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#define MAX_PAYLOAD_SIZE 1024

// BUGGY IMPLEMENTATION

bool process_packet(int16_t packet_header_len, int16_t total_packet_len) {

// The payload length is derived by subtracting the header length

// Requirement: Payload must not exceed MAX_PAYLOAD_SIZE and must be greater than 0.

if (total_packet_len - packet_header_len \> MAX_PAYLOAD_SIZE) {

printf(\"Error: Payload exceeds maximum allowed size!\\n\");

return false;

}

// Allocate / process buffer

size_t payload_len = total_packet_len - packet_header_len;

printf(\"Allocating payload buffer of size: %zu bytes\\n\", payload_len);

return true;

}

\`\`\`

\### Problems in the Buggy Code:

1\. \*\*Negative Value Vulnerability:\*\* If a malformed or malicious packet sends \`total_packet_len = 10\` and \`packet_header_len = 20\`, \`10 - 20 = -10\`.

\- The condition \`-10 \> 1024\` evaluates to \`false\` (it passes validation!).

\- In \`size_t payload_len = total_packet_len - packet_header_len;\`, \`-10\` is cast to unsigned \`size_t\` (64-bit), becoming \`18446744073709551606\` bytes, causing an enormous out-of-bounds allocation or crash.

2\. \*\*Integer Truncation & Sign Mismatch:\*\* Mixing signed \`int16_t\` with unsigned \`size_t\` without explicit range verification.

\### Defensive Fix:

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<limits.h\>

#define MAX_PAYLOAD_SIZE 1024

bool process_packet_safe(uint16_t packet_header_len, uint16_t total_packet_len, size_t \*out_payload_len) {

if (out_payload_len == NULL) {

return false;

}

// Defensive Check 1: Ensure total length is strictly greater than header length

if (total_packet_len \<= packet_header_len) {

fprintf(stderr, \"Defensive Error: Total packet length (%u) must be greater than header length (%u)\\n\",

total_packet_len, packet_header_len);

return false;

}

uint16_t payload_len = total_packet_len - packet_header_len;

// Defensive Check 2: Explicit upper bounds validation against maximum allowed size

if (payload_len \> MAX_PAYLOAD_SIZE) {

fprintf(stderr, \"Defensive Error: Payload length (%u) exceeds MAX_PAYLOAD_SIZE (%u)\\n\",

payload_len, MAX_PAYLOAD_SIZE);

return false;

}

\*out_payload_len = (size_t)payload_len;

return true;

}

\`\`\`

\-\--

\## 5. Week 1 Roadmap & Kickoff Note

Welcome to Day 1! Over the next 7 days, we establish an unbreakable foundation in memory mechanics, pointers, and data representation. By Sunday (Day 8), you will build a complete \*\*Custom Virtual Memory Inspector & Disassembler Bridge\*\* as your first weekly Mega Project.
