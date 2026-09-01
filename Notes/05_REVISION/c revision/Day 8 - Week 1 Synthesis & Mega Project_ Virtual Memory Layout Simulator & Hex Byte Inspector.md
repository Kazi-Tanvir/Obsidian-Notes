\-\--

tags:

\- c

\- week-1-synthesis

\- mega-project

\- virtual-memory

\- pointer-architecture

\- hex-inspector

\- memory-simulator

date: 2026-08-30

day: 8

\-\--

\# Day 8: Week 1 Synthesis & Mega Project --- Virtual Memory Layout Simulator & Byte Inspector

\-\--

\## 1. Quick Reference & Cheat Sheet (Week 1 Synthesis)

\### Core C Memory & Pointer Foundations

\`\`\`text

Compilation: Source (.c) ──\[cpp\]──► Preprocessed (.i) ──\[cc1\]──► Assembly (.s) ──\[as\]──► Object (.o) ──\[ld\]──► ELF Binary

Address Space: Low \[ .text \| .rodata \| .data \| .bss \| Heap ──► \... ◄── Stack \| Kernel Space \] High

Memory Units: 1 Byte = 8 bits \| 32-bit Ptr = 4 Bytes \| 64-bit Ptr = 8 Bytes

\`\`\`

\### Essential Rules & Idioms Cheat Sheet

\* \*\*Integer Promotion:\*\* Types smaller than \`int\` (\`char\`, \`short\`, \`bool\`) are automatically promoted to \`int\` in expressions.

\* \*\*Signed vs Unsigned Comparison:\*\* Mixing signed and unsigned implicitly promotes signed to unsigned, turning negative numbers into huge positive numbers (e.g. \`-1 \> 1U\` evaluates to \`true\`).

\* \*\*Bitwise Idioms:\*\*

\* Set: \`x \|= (1U \<\< k)\` \| Clear: \`x &= \~(1U \<\< k)\` \| Toggle: \`x \^= (1U \<\< k)\` \| Test: \`(x & (1U \<\< k)) != 0\`

\* Clear lowest set bit: \`x &= (x - 1)\` \| Isolate lowest set bit: \`x & (-x)\`

\* \*\*Type Qualifiers:\*\* \`const\` (read-only), \`volatile\` (disables register caching, forces memory load), \`restrict\` (sole pointer alias contract for compiler SIMD optimization).

\* \*\*Precedence vs Evaluation Order:\*\* Precedence defines tree grouping (AST), \*\*not\*\* execution order. Function argument evaluation order is unspecified.

\* \*\*Sequence Points Rule:\*\* Modifying an object more than once between sequence points (e.g. \`i = i++\`, \`a\[i\] = i++\`) is \*\*Undefined Behavior\*\*.

\* \*\*Pointer Arithmetic:\*\* \`ptr + n\` advances memory address by \`n \* sizeof(\*ptr)\` bytes.

\* \*\*Array Decay:\*\* \`T\[N\]\` decays to \`T\*\` pointing to \`&arr\[0\]\`, except as operand of \`sizeof\`, operand of \`&\` (\`&arr\` has type \`T (\*)\[N\]\`), or string literal initializer.

\* \*\*2D Array Stride:\*\* In \`T matrix\[R\]\[C\]\`, address of \`matrix\[r\]\[c\]\` = \$\\text{Base} + (r \\times C + c) \\times \\text{sizeof}(T)\$.

\* \*\*Double Pointer Rule:\*\* Pass \`T\*\` to modify a value; pass \`T\*\*\` to modify a pointer address (e.g., dynamic allocation inside a callee).

\-\--

\## 2. In-Depth Theory & Low-Level Mechanics

\### A. Virtual Memory Architecture & Page Table Translation

Modern operating systems and CPUs enforce process isolation using \*\*Virtual Memory\*\*. User applications never interact with physical RAM addresses directly; every pointer address is a virtual address translated by the CPU\'s Memory Management Unit (MMU) backed by the Translation Lookaside Buffer (TLB).

\`\`\`text

64-bit Canonical Virtual Address (48-bit active):

63 47 38 29 20 11 0

┌─────────────┬──────────┬──────────┬──────────┬──────────┬─────────────┐

│ Sign Extend │ PML4 Idx │ PDPT │ Page Dir │ Page Tbl │ Page Offset │

│ (16 bit) │ (9 bit) │ (9 bit) │ (9 bit) │ (9 bit) │ (12 bit) │

└─────────────┴──────────┴──────────┴──────────┴──────────┴─────────────┘

│

Page Size = 4096 B (2¹² Bytes)

\`\`\`

\### B. Segment Permissions & Memory Protection Bits

The OS kernel marks virtual pages with hardware protection flags in the Page Table Entries:

\* \*\*\`PROT_READ\` (\`r\`):\*\* Allows CPU read access.

\* \*\*\`PROT_WRITE\` (\`w\`):\*\* Allows CPU write/store operations.

\* \*\*\`PROT_EXEC\` (\`x\`):\*\* Allows instruction execution (NX / DEP bit prevents executing data on Stack/Heap).

\#### Hardware Fault Triggers:

1\. \*\*Segmentation Fault (\`SIGSEGV\` / \`SEGV_ACCERR\`):\*\* Attempting to write to a read-only page (e.g., modifying a string literal in \`.rodata\`).

2\. \*\*Segmentation Fault (\`SEGV_MAPERR\`):\*\* Attempting to access an unmapped address (e.g., dereferencing \`NULL\` or a wild pointer).

3\. \*\*Bus Error (\`SIGBUS\`):\*\* Hardware alignment fault or non-existent physical address mapping.

\-\--

\## 3. Thoughtful Mini-Project (\~1 Hour Scope)

\### Project Title: Zero-Copy Binary Telemetry Stream Unpacker & CRC-16 Validator (\`telemetry_slice\`)

\#### Objective

Implement a lightweight zero-copy binary parser that extracts telemetry header blocks from a raw network byte stream using pointer offsets and validates integrity via CRC-16-CCITT.

\#### Starter Code Implementation

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<string.h\>

#include \<assert.h\>

#define PACKET_MAGIC 0xA55A

// Packed wire header format (Big-Endian network order)

typedef struct {

uint16_t magic;

uint16_t seq_id;

uint32_t timestamp;

uint16_t payload_len;

uint16_t crc16;

} WireHeader;

// CRC-16-CCITT (Polynomial: 0x1021, Initial: 0xFFFF)

uint16_t compute_crc16(const uint8_t \*data, size_t len) {

uint16_t crc = 0xFFFF;

for (size_t i = 0; i \< len; i++) {

crc \^= (uint16_t)(data\[i\] \<\< 8);

for (int b = 0; b \< 8; b++) {

if (crc & 0x8000) {

crc = (uint16_t)((crc \<\< 1) \^ 0x1021);

} else {

crc \<\<= 1;

}

}

}

return crc;

}

static inline uint16_t read_be16(const uint8_t \*buf) {

return (uint16_t)((buf\[0\] \<\< 8) \| buf\[1\]);

}

static inline uint32_t read_be32(const uint8_t \*buf) {

return ((uint32_t)buf\[0\] \<\< 24) \| ((uint32_t)buf\[1\] \<\< 16) \|

((uint32_t)buf\[2\] \<\< 8) \| (uint32_t)buf\[3\];

}

bool parse_telemetry_packet(const uint8_t \*stream, size_t stream_len,

WireHeader \*out_hdr, const uint8_t \*\*out_payload) {

if (!stream \|\| !out_hdr \|\| !out_payload \|\| stream_len \< 12) return false;

out_hdr-\>magic = read_be16(stream);

if (out_hdr-\>magic != PACKET_MAGIC) {

fprintf(stderr, \"Invalid Magic Word: 0x%04X\\n\", out_hdr-\>magic);

return false;

}

out_hdr-\>seq_id = read_be16(stream + 2);

out_hdr-\>timestamp = read_be32(stream + 4);

out_hdr-\>payload_len = read_be16(stream + 8);

out_hdr-\>crc16 = read_be16(stream + 10);

if (stream_len \< 12 + out_hdr-\>payload_len) {

fprintf(stderr, \"Packet truncated! Expected %u, got %zu\\n\", 12 + out_hdr-\>payload_len, stream_len);

return false;

}

// Validate CRC over payload

\*out_payload = stream + 12; // Zero-copy pointer slice!

uint16_t calc_crc = compute_crc16(\*out_payload, out_hdr-\>payload_len);

if (calc_crc != out_hdr-\>crc16) {

fprintf(stderr, \"CRC Mismatch! Calculated: 0x%04X, Expected: 0x%04X\\n\", calc_crc, out_hdr-\>crc16);

return false;

}

return true;

}

int main(void) {

// Construct test wire frame

const char \*payload_text = \"SENSOR_OK:TEMP=24.5C;PRESSURE=1013HPA\";

uint16_t payload_len = (uint16_t)strlen(payload_text);

uint16_t crc = compute_crc16((const uint8_t \*)payload_text, payload_len);

uint8_t packet\[128\];

packet\[0\] = 0xA5; packet\[1\] = 0x5A; // Magic

packet\[2\] = 0x00; packet\[3\] = 0x01; // Seq 1

packet\[4\] = 0x00; packet\[5\] = 0x00; packet\[6\] = 0x03; packet\[7\] = 0xE8; // Timestamp 1000

packet\[8\] = (uint8_t)(payload_len \>\> 8); packet\[9\] = (uint8_t)(payload_len & 0xFF);

packet\[10\] = (uint8_t)(crc \>\> 8); packet\[11\] = (uint8_t)(crc & 0xFF);

memcpy(packet + 12, payload_text, payload_len);

WireHeader header;

const uint8_t \*payload_ptr = NULL;

bool ok = parse_telemetry_packet(packet, 12 + payload_len, &header, &payload_ptr);

assert(ok);

printf(\"Successfully parsed packet #%u (Timestamp: %u ms, Payload: %u bytes)\\n\",

header.seq_id, header.timestamp, header.payload_len);

printf(\"Payload Data (Zero-Copy View): %.\*s\\n\", header.payload_len, payload_ptr);

return 0;

}

\`\`\`

\-\--

\## 4. Error Handling & Defensive Programming Challenge

\### Scenario: Unaligned Memory Access & Strict Aliasing Violation

Examine the following code intended to read 32-bit integers from a byte stream:

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

// BUGGY IMPLEMENTATION

uint32_t read_uint32_unaligned_faulty(const uint8_t \*buffer, size_t offset) {

// VULNERABILITY 1: Strict Aliasing Violation

// Accessing uint8_t array through uint32_t\* violates ISO C aliasing rules (UB).

// VULNERABILITY 2: Unaligned Pointer Dereference

// If \'buffer + offset\' is not aligned to a 4-byte boundary, some architectures (ARM, SPARC, MIPS)

// trigger a hardware BUS ERROR (SIGBUS) or CPU exception!

const uint32_t \*ptr = (const uint32_t \*)(buffer + offset);

return \*ptr;

}

\`\`\`

\### Analysis:

1\. \*\*Strict Aliasing Rule (C17 §6.5):\*\* Compilers assume pointers of different types (e.g. \`int\*\` and \`float\*\` or \`uint32_t\*\` and \`uint8_t\*\`) cannot point to the same memory location. Casting \`uint8_t\*\` to \`uint32_t\*\` breaks this assumption, allowing the optimizer to reorder or eliminate memory loads.

2\. \*\*Alignment Faults:\*\* On x86_64, unaligned loads incur performance penalties; on ARM/embedded architectures without hardware unaligned handlers, it triggers an immediate crash.

\### Defensive Fix:

\`\`\`c

#include \<stdio.h\>

#include \<stdint.h\>

#include \<string.h\>

// Method 1: memcpy (Compiler optimizes this into a single unaligned load instruction with 0 overhead!)

static inline uint32_t read_uint32_safe_native(const uint8_t \*buffer, size_t offset) {

uint32_t val;

memcpy(&val, buffer + offset, sizeof(val));

return val;

}

// Method 2: Explicit byte-shift (Endian-independent and 100% portable)

static inline uint32_t read_uint32_safe_be(const uint8_t \*b) {

return ((uint32_t)b\[0\] \<\< 24) \|

((uint32_t)b\[1\] \<\< 16) \|

((uint32_t)b\[2\] \<\< 8) \|

((uint32_t)b\[3\]);

}

\`\`\`

\-\--

\## 5. WEEKLY MEGA PROJECT (Week 1 Capstone)

\### Project Title: Virtual Memory Layout Simulator & Interactive Hex Byte Inspector (\`vmem_sim\`)

\#### Architectural Overview

Build an end-to-end, modular Virtual Memory Management and Byte Inspection Engine in C. The simulator models a complete process address space containing segmented memory regions (\`.text\`, \`.rodata\`, \`.data\`, \`.bss\`, \`Heap\`, \`Stack\`), enforces segment-level permission bitmasks (\`READ\`, \`WRITE\`, \`EXEC\`), tracks activation records/stack frames, and provides an interactive hex dump analyzer with ASCII sidebar formatting.

\`\`\`text

┌────────────────────────────────────────────────────────────────────────┐

│ VirtualMemorySystem (VMS) │

├────────────────────────────────────────────────────────────────────────┤

│ Segment Registry: │

│ - \[0x0040_0000 - 0x0040_0FFF\] .text (PROT_READ \| PROT_EXEC) │

│ - \[0x0040_1000 - 0x0040_1FFF\] .rodata (PROT_READ) │

│ - \[0x0060_0000 - 0x0060_1FFF\] .data (PROT_READ \| PROT_WRITE) │

│ - \[0x0060_2000 - 0x0060_3FFF\] .bss (PROT_READ \| PROT_WRITE) │

│ - \[0x0100_0000 - 0x010F_FFFF\] Heap (PROT_READ \| PROT_WRITE, ▲) │

│ - \[0x7FFF_E000 - 0x7FFF_FFFF\] Stack (PROT_READ \| PROT_WRITE, ▼) │

├────────────────────────────────────────────────────────────────────────┤

│ MMU Core & Protection Gate: │

│ vms_read(addr, buf, len) ──► Checks PROT_READ ──► Copies bytes │

│ vms_write(addr, buf, len) ──► Checks PROT_WRITE ──► Stores bytes │

│ vms_exec(addr) ──► Checks PROT_EXEC ──► Runs instruction │

│ \* Throws VM_ERR_SEGFAULT / VM_ERR_PROT on violation │

├────────────────────────────────────────────────────────────────────────┤

│ Stack Frame Manager: │

│ vms_stack_push_frame(func_name, ret_addr, args) │

│ vms_stack_pop_frame() │

├────────────────────────────────────────────────────────────────────────┤

│ Hex Dump & Memory Visualizer: │

│ vms_dump_hex(addr, length) ──► Formats Hex, Offsets, ASCII & Segment │

└────────────────────────────────────────────────────────────────────────┘

\`\`\`

\#### Complete Modular Implementation (\`vmem_sim.c\`)

\`\`\`c

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<string.h\>

#include \<ctype.h\>

#include \<assert.h\>

#define PROT_NONE 0x0U

#define PROT_READ 0x1U

#define PROT_WRITE 0x2U

#define PROT_EXEC 0x4U

typedef enum {

VM_OK = 0,

VM_ERR_UNMAPPED_ADDRESS,

VM_ERR_PERMISSION_DENIED,

VM_ERR_STACK_OVERFLOW,

VM_ERR_HEAP_EXHAUSTED,

VM_ERR_INVALID_ARG

} VmStatus;

const char \*vm_status_str(VmStatus s) {

switch (s) {

case VM_OK: return \"SUCCESS\";

case VM_ERR_UNMAPPED_ADDRESS: return \"SEGFAULT: Unmapped Memory Address (SEGV_MAPERR)\";

case VM_ERR_PERMISSION_DENIED: return \"SEGFAULT: Memory Protection Violation (SEGV_ACCERR)\";

case VM_ERR_STACK_OVERFLOW: return \"STACK OVERFLOW: Stack Pointer collided with boundary\";

case VM_ERR_HEAP_EXHAUSTED: return \"OUT OF MEMORY: Heap break exceeded capacity\";

default: return \"UNKNOWN ERROR\";

}

}

typedef struct {

const char \*name;

uint64_t base_addr;

size_t size;

uint8_t permissions; // Bitmask of PROT_READ, PROT_WRITE, PROT_EXEC

uint8_t \*host_buffer; // Actual allocated memory block in simulator

} VmSegment;

#define MAX_SEGMENTS 8

#define MAX_STACK_FRAMES 16

typedef struct {

char func_name\[32\];

uint64_t frame_base_addr; // Saved \$rbp

uint64_t return_addr; // Saved \$rip

size_t local_var_bytes;

} VmStackFrame;

typedef struct {

VmSegment segments\[MAX_SEGMENTS\];

size_t num_segments;

uint64_t heap_start;

uint64_t heap_brk;

uint64_t heap_limit;

uint64_t stack_base;

uint64_t stack_ptr; // \$rsp

uint64_t stack_limit;

VmStackFrame call_stack\[MAX_STACK_FRAMES\];

size_t call_stack_depth;

} VirtualMemorySystem;

// Initialize Virtual Memory Subsystem

VirtualMemorySystem \*vms_create(void) {

VirtualMemorySystem \*vm = (VirtualMemorySystem \*)calloc(1, sizeof(VirtualMemorySystem));

assert(vm != NULL);

return vm;

}

bool vms_add_segment(VirtualMemorySystem \*vm, const char \*name, uint64_t base, size_t size, uint8_t perms) {

if (vm-\>num_segments \>= MAX_SEGMENTS) return false;

VmSegment \*seg = &vm-\>segments\[vm-\>num_segments++\];

seg-\>name = name;

seg-\>base_addr = base;

seg-\>size = size;

seg-\>permissions = perms;

seg-\>host_buffer = (uint8_t \*)calloc(1, size);

assert(seg-\>host_buffer != NULL);

return true;

}

void vms_destroy(VirtualMemorySystem \*vm) {

if (!vm) return;

for (size_t i = 0; i \< vm-\>num_segments; i++) {

free(vm-\>segments\[i\].host_buffer);

}

free(vm);

}

// Find segment containing virtual address

static VmSegment \*vms_find_segment(VirtualMemorySystem \*vm, uint64_t addr) {

for (size_t i = 0; i \< vm-\>num_segments; i++) {

VmSegment \*seg = &vm-\>segments\[i\];

if (addr \>= seg-\>base_addr && addr \< (seg-\>base_addr + seg-\>size)) {

return seg;

}

}

return NULL;

}

// Memory Write with Permission Checking

VmStatus vms_write(VirtualMemorySystem \*vm, uint64_t vaddr, const void \*src, size_t len) {

if (len == 0) return VM_OK;

VmSegment \*seg = vms_find_segment(vm, vaddr);

if (!seg \|\| (vaddr + len \> seg-\>base_addr + seg-\>size)) {

return VM_ERR_UNMAPPED_ADDRESS;

}

if (!(seg-\>permissions & PROT_WRITE)) {

return VM_ERR_PERMISSION_DENIED;

}

size_t offset = (size_t)(vaddr - seg-\>base_addr);

memcpy(seg-\>host_buffer + offset, src, len);

return VM_OK;

}

// Memory Read with Permission Checking

VmStatus vms_read(VirtualMemorySystem \*vm, uint64_t vaddr, void \*dest, size_t len) {

if (len == 0) return VM_OK;

VmSegment \*seg = vms_find_segment(vm, vaddr);

if (!seg \|\| (vaddr + len \> seg-\>base_addr + seg-\>size)) {

return VM_ERR_UNMAPPED_ADDRESS;

}

if (!(seg-\>permissions & PROT_READ)) {

return VM_ERR_PERMISSION_DENIED;

}

size_t offset = (size_t)(vaddr - seg-\>base_addr);

memcpy(dest, seg-\>host_buffer + offset, len);

return VM_OK;

}

// Dynamic Heap Allocation (brk-based)

VmStatus vms_malloc(VirtualMemorySystem \*vm, size_t size, uint64_t \*out_vaddr) {

// 8-byte alignment

size_t aligned_size = (size + 7) & \~7ULL;

if (vm-\>heap_brk + aligned_size \> vm-\>heap_limit) {

return VM_ERR_HEAP_EXHAUSTED;

}

\*out_vaddr = vm-\>heap_brk;

vm-\>heap_brk += aligned_size;

return VM_OK;

}

// Stack Frame Push

VmStatus vms_push_frame(VirtualMemorySystem \*vm, const char \*func, uint64_t ret_addr, size_t local_bytes) {

if (vm-\>call_stack_depth \>= MAX_STACK_FRAMES) {

return VM_ERR_STACK_OVERFLOW;

}

size_t frame_bytes = ((sizeof(uint64_t) \* 2 + local_bytes) + 15) & \~15ULL; // 16-byte stack align

if (vm-\>stack_ptr - frame_bytes \< vm-\>stack_limit) {

return VM_ERR_STACK_OVERFLOW;

}

vm-\>stack_ptr -= frame_bytes;

VmStackFrame \*frame = &vm-\>call_stack\[vm-\>call_stack_depth++\];

strncpy(frame-\>func_name, func, sizeof(frame-\>func_name) - 1);

frame-\>frame_base_addr = vm-\>stack_ptr;

frame-\>return_addr = ret_addr;

frame-\>local_var_bytes = local_bytes;

// Write saved return address and frame pointer to stack segment memory

vms_write(vm, vm-\>stack_ptr, &ret_addr, sizeof(ret_addr));

return VM_OK;

}

// Stack Frame Pop

VmStatus vms_pop_frame(VirtualMemorySystem \*vm) {

if (vm-\>call_stack_depth == 0) return VM_ERR_INVALID_ARG;

VmStackFrame \*frame = &vm-\>call_stack\[\--vm-\>call_stack_depth\];

size_t frame_bytes = ((sizeof(uint64_t) \* 2 + frame-\>local_var_bytes) + 15) & \~15ULL;

vm-\>stack_ptr += frame_bytes;

return VM_OK;

}

// Interactive Hex Dump Engine

void vms_dump_hex(VirtualMemorySystem \*vm, uint64_t vaddr, size_t len) {

VmSegment \*seg = vms_find_segment(vm, vaddr);

printf(\"\\n========================================================================================\\n\");

printf(\" MEMORY HEX DUMP: 0x%016llX (%zu bytes) \| Segment: \[%s\]\\n\",

(unsigned long long)vaddr, len, seg ? seg-\>name : \"UNMAPPED\");

printf(\" Permissions: %c%c%c\\n\",

(seg && (seg-\>permissions & PROT_READ)) ? \'R\' : \'-\',

(seg && (seg-\>permissions & PROT_WRITE)) ? \'W\' : \'-\',

(seg && (seg-\>permissions & PROT_EXEC)) ? \'X\' : \'-\');

printf(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\\n\");

printf(\" Virtual Address \| 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F \| ASCII View \\n\");

printf(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\\n\");

uint8_t buffer\[16\];

for (size_t row = 0; row \< len; row += 16) {

uint64_t row_addr = vaddr + row;

size_t chunk = (len - row \< 16) ? (len - row) : 16;

VmStatus st = vms_read(vm, row_addr, buffer, chunk);

if (st != VM_OK) {

printf(\" 0x%016llX \| \[!! %s !!\]\\n\", (unsigned long long)row_addr, vm_status_str(st));

break;

}

printf(\" 0x%016llX \| \", (unsigned long long)row_addr);

for (size_t i = 0; i \< 16; i++) {

if (i \< chunk) {

printf(\"%02X \", buffer\[i\]);

} else {

printf(\" \");

}

if (i == 7) printf(\" \");

}

printf(\"\| \");

for (size_t i = 0; i \< chunk; i++) {

putchar(isprint(buffer\[i\]) ? buffer\[i\] : \'.\');

}

printf(\"\\n\");

}

printf(\"========================================================================================\\n\\n\");

}

// Display Active Stack Frames

void vms_dump_call_stack(VirtualMemorySystem \*vm) {

printf(\"\\n\-\-- ACTIVATION RECORDS & CALL STACK (\$rsp: 0x%016llX) \-\--\\n\", (unsigned long long)vm-\>stack_ptr);

if (vm-\>call_stack_depth == 0) {

printf(\" (Call stack is empty)\\n\\n\");

return;

}

for (int i = (int)vm-\>call_stack_depth - 1; i \>= 0; i\--) {

VmStackFrame \*f = &vm-\>call_stack\[i\];

printf(\" \[Frame #%d\] %-16s \| Base (\$rbp): 0x%016llX \| Ret (\$rip): 0x%016llX \| Locals: %zu B\\n\",

i, f-\>func_name, (unsigned long long)f-\>frame_base_addr,

(unsigned long long)f-\>return_addr, f-\>local_var_bytes);

}

printf(\"\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--\\n\\n\");

}

// Test Harness & Simulation Demo

int main(void) {

printf(\"\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\n\");

printf(\" WEEK 1 CAPSTONE: VIRTUAL MEMORY LAYOUT SIMULATOR \\n\");

printf(\"\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\n\\n\");

VirtualMemorySystem \*vm = vms_create();

// 1. Configure Linux Process Memory Segments

vms_add_segment(vm, \".text\", 0x00400000, 4096, PROT_READ \| PROT_EXEC);

vms_add_segment(vm, \".rodata\", 0x00401000, 4096, PROT_READ);

vms_add_segment(vm, \".data\", 0x00600000, 4096, PROT_READ \| PROT_WRITE);

vms_add_segment(vm, \".bss\", 0x00601000, 4096, PROT_READ \| PROT_WRITE);

// Heap: 64 KB

vms_add_segment(vm, \"Heap\", 0x01000000, 65536, PROT_READ \| PROT_WRITE);

vm-\>heap_start = 0x01000000;

vm-\>heap_brk = 0x01000000;

vm-\>heap_limit = 0x01000000 + 65536;

// Stack: 64 KB (Grows downwards from 0x7FFF_FFFF)

vms_add_segment(vm, \"Stack\", 0x7FFF0000, 65536, PROT_READ \| PROT_WRITE);

vm-\>stack_base = 0x7FFFFFFF;

vm-\>stack_ptr = 0x7FFFFFFF;

vm-\>stack_limit = 0x7FFF0000;

printf(\"\[1\] Initializing Simulated Memory Segments:\\n\");

for (size_t i = 0; i \< vm-\>num_segments; i++) {

VmSegment \*s = &vm-\>segments\[i\];

printf(\" Segment \[%-7s\]: Base: 0x%016llX \| Size: %5zu B \| Perms: %c%c%c\\n\",

s-\>name, (unsigned long long)s-\>base_addr, s-\>size,

(s-\>permissions & PROT_READ) ? \'R\' : \'-\',

(s-\>permissions & PROT_WRITE) ? \'W\' : \'-\',

(s-\>permissions & PROT_EXEC) ? \'X\' : \'-\');

}

// 2. Populate .rodata and .data

const char \*greeting = \"Hello, World! Virtual Memory Simulator v1.0\";

vms_write(vm, 0x00401000, greeting, strlen(greeting) + 1);

uint32_t global_counter = 0xDEADBEEF;

vms_write(vm, 0x00600000, &global_counter, sizeof(global_counter));

// 3. Demonstrate Hex Dump of .rodata

vms_dump_hex(vm, 0x00401000, 48);

// 4. Test Memory Protection Fault (Writing to .rodata)

printf(\"\[2\] Testing Memory Protection Enforcement:\\n\");

char hack\[\] = \"Overwrite Attempt\";

VmStatus st = vms_write(vm, 0x00401000, hack, sizeof(hack));

printf(\" Attempt write to .rodata (0x00401000) =\> Status: %s\\n\", vm_status_str(st));

assert(st == VM_ERR_PERMISSION_DENIED);

// 5. Test Heap Dynamic Allocation

printf(\"\\n\[3\] Testing Dynamic Heap Allocator:\\n\");

uint64_t heap_chunk1, heap_chunk2;

vms_malloc(vm, 32, &heap_chunk1);

vms_malloc(vm, 64, &heap_chunk2);

uint8_t heap_payload\[\] = { 0x01, 0x02, 0x03, 0x04, 0xAA, 0xBB, 0xCC, 0xDD };

vms_write(vm, heap_chunk1, heap_payload, sizeof(heap_payload));

printf(\" Allocated Heap Chunk 1 at: 0x%016llX\\n\", (unsigned long long)heap_chunk1);

printf(\" Allocated Heap Chunk 2 at: 0x%016llX\\n\", (unsigned long long)heap_chunk2);

vms_dump_hex(vm, heap_chunk1, 32);

// 6. Test Stack Frame Management & Activation Records

printf(\"\[4\] Testing Call-Stack & Activation Records:\\n\");

vms_push_frame(vm, \"main()\", 0x00000000, 16);

vms_push_frame(vm, \"process_payload()\", 0x00400050, 64);

vms_push_frame(vm, \"compute_hash()\", 0x00400120, 32);

vms_dump_call_stack(vm);

// Write a local variable inside compute_hash stack frame

uint64_t hash_val = 0x8877665544332211ULL;

vms_write(vm, vm-\>stack_ptr + 16, &hash_val, sizeof(hash_val));

vms_dump_hex(vm, vm-\>stack_ptr, 48);

// Unwind frames

vms_pop_frame(vm);

vms_pop_frame(vm);

printf(\" Unwound 2 frames:\\n\");

vms_dump_call_stack(vm);

vms_destroy(vm);

printf(\"========================================================================\\n\");

printf(\" WEEK 1 MEGA PROJECT VERIFICATION COMPLETE: ALL ASSERTS PASSED!\\n\");

printf(\"========================================================================\\n\");

return 0;

}

\`\`\`
