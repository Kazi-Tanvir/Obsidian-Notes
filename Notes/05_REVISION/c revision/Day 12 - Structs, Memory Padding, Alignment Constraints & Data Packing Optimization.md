---
tags:
  - c
  - structs
  - memory-alignment
  - padding
  - packed-structs
  - data-layout
  - cache-locality
date: 2026-09-03
day: 12
---

# Day 12: Structs, Memory Padding, Alignment Constraints & Data Packing Optimization

---

## 1. Quick Reference & Cheat Sheet

### Alignment & Padding Rules
1. **Natural Alignment:** Every primitive type requires its memory address to be a multiple of its size ($k \\times \\text{sizeof}(T)$):
   * `char` (1 byte): Any address.
   * `short` (2 bytes): Address divisible by 2.
   * `int`, `float` (4 bytes): Address divisible by 4.
   * `double`, pointers, `int64_t` (8 bytes on 64-bit): Address divisible by 8.
2. **Member Placement:** Members are allocated in declaration order. If the next member's offset does not satisfy its natural alignment, the compiler injects **Internal Padding** bytes.
3. **Structure Total Size & Tail Padding:** The total struct size must be a multiple of its **largest member's alignment requirement**. The compiler injects **Tail Padding** at the end of the struct to ensure every element in an array of that struct starts at an aligned address.

### Inspection Macros & Type Qualifiers
```c
#include <stddef.h>    // For offsetof
#include <stdalign.h>  // For alignof, alignas (C11)

size_t offset \= offsetof(struct MyStruct, member_name);
size_t req_align \= alignof(struct MyStruct); // Or _Alignof
```

### Struct Layout Optimization Rule of Thumb
> **Arrange struct members in descending order of size** (e.g. 8-byte pointers/doubles first, then 4-byte ints/floats, then 2-byte shorts, then 1-byte chars). This automatically minimizes or completely eliminates internal padding holes.

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Step-by-Step Memory Padding Walkthrough
Consider this unoptimized struct on an x86_64 system:

```c
struct Unoptimized {
    char   a; // 1 byte
    int    b; // 4 bytes
    char   c; // 1 byte
    double d; // 8 bytes
};
```

Let's trace the offsets assigned by the compiler:
* `a` placed at offset `0` (1 byte).
* Next member `b` requires 4-byte alignment. Offset 1 is not divisible by 4 $\\implies$ **3 bytes of internal padding** added.
* `b` placed at offset `4` through `7` (4 bytes).
* `c` placed at offset `8` (1 byte).
* Next member `d` requires 8-byte alignment. Offset 9 is not divisible by 8 $\\implies$ **7 bytes of internal padding** added.
* `d` placed at offset `16` through `23` (8 bytes).
* Total bytes used: 24 bytes. Largest member alignment is 8 (`double`). 24 is divisible by 8, so 0 tail padding bytes needed.

```text
Memory Layout of struct Unoptimized (24 Bytes):
 ┌──────┬───────────────────────┬──────────────┬──────┬───────────────────────────────┬──────────────┐
 │ a    │ [Padding: 3 Bytes]    │ b            │ c    │ [Padding: 7 Bytes]            │ d            │
 │ (1B) │ (0x00, 0x00, 0x00)    │ (4B)         │ (1B) │ (0x00, 0x00, 0x00, 0x00, ...) │ (8B)         │
 └──────┴───────────────────────┴──────────────┴──────┴───────────────────────────────┴──────────────┘
 Byte 0  Byte 1           Byte 3 Byte 4 Byte 7 Byte 8 Byte 9                  Byte 15 Byte 16 Byte 23
```
* **Payload data:** $1 \+ 4 \+ 1 \+ 8 \= 14$ bytes.
* **Wasted memory:** 10 bytes of padding (**41.6% memory wasted\!**).

#### Reordered Layout:
```c
struct Optimized {
    double d; // 8 bytes (Offset 0\)
    int    b; // 4 bytes (Offset 8\)
    char   a; // 1 byte  (Offset 12\)
    char   c; // 1 byte  (Offset 13\)
              // 2 bytes of tail padding to make total size 16 (multiple of 8\)
};
```
* **Total size:** 16 bytes.
* **Wasted memory:** Only 2 bytes (12.5% tail padding). Memory footprint reduced by **33.3%**\!

---

### B. Why Tail Padding Exists (Array Alignment Guarantees)
Suppose `struct Optimized` lacked its 2 tail padding bytes, making it 14 bytes in size.
If you declared an array:
```c
struct Optimized arr[2];
```
* `\&arr[0]` is at address `0x1000` (divisible by 8 $\\implies$ `arr[0].d` is aligned).
* `\&arr[1]` would be at address `0x1000 \+ 14 \= 0x100E`.
* `0x100E` is **NOT divisible by 8**\! Accessing `arr[1].d` would trigger an unaligned memory access.
* Tail padding ensures that every element in an array satisfies the struct's maximum alignment.

---

### C. Packed Structs: Use Cases & Hazards
Compilers allow suppressing all padding bytes using vendor extensions:
* GCC/Clang: `__attribute__((packed))`
* MSVC: `\#pragma pack(push, 1)`

```c
struct __attribute__((packed)) WireHeader {
    uint8_t  type;      // 1 byte
    uint32_t length;    // 4 bytes (starts at offset 1\!)
    uint16_t checksum;  // 2 bytes (starts at offset 5\!)
}; // Total size: Exactly 7 bytes.
```

#### The Dangers of Packed Structs:
1. **Bus Faults (`SIGBUS`):** On RISC architectures (ARM, MIPS, SPARC) without hardware unaligned access support, dereferencing an unaligned multi-byte member triggers a CPU fault.
2. **Severe CPU Penalties:** On x86, unaligned loads split across two cache lines take 2 to 3 times longer than aligned loads.
3. **Pointer Aliasing Violation:**
   ```c
   struct WireHeader hdr;
   uint32_t *len_ptr \= \&hdr.length; // GCC Warning: taking address of packed member may result in an unaligned pointer value
   *len_ptr \= 42; // Undefined Behavior on many platforms\!
   ```

---

### D. Data-Oriented Design: Array-of-Structs (AoS) vs Struct-of-Arrays (SoA)
In high-throughput systems (game physics, database scans, machine learning):

```text
Array-of-Structs (AoS): [X Y Z Mass] [X Y Z Mass] [X Y Z Mass] ...
Struct-of-Arrays (SoA): X: [X1 X2 X3 ...]
                         Y: [Y1 Y2 Y3 ...]
                         Z: [Z1 Z2 Z3 ...]
                         Mass: [M1 M2 M3 ...]
```
* **AoS:** Poor cache utilization if you only need to update `X` and `Y` positions (CPU still loads `Z` and `Mass` into L1/L2 cache lines).
* **SoA:** Vectorization-friendly (SIMD). CPU cache lines load purely sequential `X` coordinates, enabling 4x to 8x throughput using AVX instructions.

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Struct Memory Layout Visualizer & Wire-Frame Serializer (`struct_inspector`)

#### Objective
Build a C utility that:
1. Programmatically analyzes and prints a visual ASCII memory map of a structure's members and padding gaps using `offsetof()` and `sizeof()`.
2. Implements a safe serialization and deserialization function that packs in-memory structs into canonical wire formats without unaligned pointer dereferences.

#### Complete Starter Code Implementation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

typedef struct {
    const char *name;
    size_t offset;
    size_t size;
} MemberInfo;

// Inspect and print byte layout
void inspect_struct_layout(const char *struct_name, size_t total_size,
                           const MemberInfo *members, size_t member_count) {
    printf("====================================================================\\n");
    printf("  MEMORY LAYOUT VISUALIZER: %s (Total: %zu Bytes)\\n", struct_name, total_size);
    printf("====================================================================\\n");
    printf(" Offset | Size | Type / Member Name       | Status\\n");
    printf("--------+------+--------------------------+-------------------------\\n");

    size_t current_cursor \= 0;
    size_t total_padding \= 0;

    for (size_t i \= 0; i < member_count; i++) {
        // Detect internal padding hole before member
        if (members[i].offset > current_cursor) {
            size_t pad_size \= members[i].offset \- current_cursor;
            printf("  \+%04zu |   %2zu | [INTERNAL PADDING HOLE]  | WASTED GAP (%zu bytes)\\n",
                   current_cursor, pad_size, pad_size);
            total_padding \+= pad_size;
            current_cursor \= members[i].offset;
        }

        printf("  \+%04zu |   %2zu | %-24s | PAYLOAD DATA\\n",
               members[i].offset, members[i].size, members[i].name);
        current_cursor \+= members[i].size;
    }

    // Detect tail padding hole
    if (current_cursor < total_size) {
        size_t tail_pad \= total_size \- current_cursor;
        printf("  \+%04zu |   %2zu | [TAIL PADDING HOLE]      | WASTED GAP (%zu bytes)\\n",
               current_cursor, tail_pad, tail_pad);
        total_padding \+= tail_pad;
    }

    double waste_pct \= ((double)total_padding / (double)total_size) * 100.0;
    printf("--------------------------------------------------------------------\\n");
    printf(" Summary: %zu bytes payload | %zu bytes padding (%.1f%% wasted space)\\n",
           total_size \- total_padding, total_padding, waste_pct);
    printf("====================================================================\\n\\n");
}

/* \========================================================================= */
/*                   DEMO STRUCTURES FOR COMPARISON                          */
/* \========================================================================= */

struct SensorDataUnoptimized {
    char     sensor_type; // 1 byte
    uint64_t timestamp;   // 8 bytes
    uint16_t reading_id;  // 2 bytes
    double   value;       // 8 bytes
    uint8_t  battery_pct; // 1 byte
};

struct SensorDataOptimized {
    uint64_t timestamp;   // 8 bytes
    double   value;       // 8 bytes
    uint16_t reading_id;  // 2 bytes
    char     sensor_type; // 1 byte
    uint8_t  battery_pct; // 1 byte
};

/* \========================================================================= */
/*         PORTABLE SERIALIZATION WITHOUT UNALIGNED POINTER CASTS            */
/* \========================================================================= */

// Serializes SensorDataOptimized to packed 20-byte binary wire payload
void serialize_sensor_data(const struct SensorDataOptimized *src, uint8_t *dest_buf) {
    // Write timestamp (8 bytes)
    memcpy(dest_buf \+ 0, \&src->timestamp, sizeof(src->timestamp));
    // Write value (8 bytes)
    memcpy(dest_buf \+ 8, \&src->value, sizeof(src->value));
    // Write reading_id (2 bytes)
    memcpy(dest_buf \+ 16, \&src->reading_id, sizeof(src->reading_id));
    // Write sensor_type (1 byte)
    dest_buf[18] \= (uint8_t)src->sensor_type;
    // Write battery_pct (1 byte)
    dest_buf[19] \= src->battery_pct;
}

void deserialize_sensor_data(const uint8_t *src_buf, struct SensorDataOptimized *dest) {
    memcpy(\&dest->timestamp, src_buf \+ 0, sizeof(dest->timestamp));
    memcpy(\&dest->value, src_buf \+ 8, sizeof(dest->value));
    memcpy(\&dest->reading_id, src_buf \+ 16, sizeof(dest->reading_id));
    dest->sensor_type \= (char)src_buf[18];
    dest->battery_pct \= src_buf[19];
}

int main(void) {
    // 1. Analyze Unoptimized Struct
    MemberInfo unopt_members[] \= {
        { "char sensor_type", offsetof(struct SensorDataUnoptimized, sensor_type), sizeof(char) },
        { "uint64_t timestamp", offsetof(struct SensorDataUnoptimized, timestamp), sizeof(uint64_t) },
        { "uint16_t reading_id", offsetof(struct SensorDataUnoptimized, reading_id), sizeof(uint16_t) },
        { "double value", offsetof(struct SensorDataUnoptimized, value), sizeof(double) },
        { "uint8_t battery_pct", offsetof(struct SensorDataUnoptimized, battery_pct), sizeof(uint8_t) }
    };
    inspect_struct_layout("struct SensorDataUnoptimized", sizeof(struct SensorDataUnoptimized),
                          unopt_members, sizeof(unopt_members) / sizeof(MemberInfo));

    // 2. Analyze Optimized Struct
    MemberInfo opt_members[] \= {
        { "uint64_t timestamp", offsetof(struct SensorDataOptimized, timestamp), sizeof(uint64_t) },
        { "double value", offsetof(struct SensorDataOptimized, value), sizeof(double) },
        { "uint16_t reading_id", offsetof(struct SensorDataOptimized, reading_id), sizeof(uint16_t) },
        { "char sensor_type", offsetof(struct SensorDataOptimized, sensor_type), sizeof(char) },
        { "uint8_t battery_pct", offsetof(struct SensorDataOptimized, battery_pct), sizeof(uint8_t) }
    };
    inspect_struct_layout("struct SensorDataOptimized", sizeof(struct SensorDataOptimized),
                          opt_members, sizeof(opt_members) / sizeof(MemberInfo));

    // 3. Test Serialization
    struct SensorDataOptimized orig \= {
        .timestamp \= 1725364800ULL,
        .value \= 98.6,
        .reading_id \= 404,
        .sensor_type \= 'T',
        .battery_pct \= 95
    };

    uint8_t wire_packet[20];
    serialize_sensor_data(\&orig, wire_packet);

    struct SensorDataOptimized restored \= {0};
    deserialize_sensor_data(wire_packet, \&restored);

    assert(orig.timestamp \== restored.timestamp);
    assert(orig.value \== restored.value);
    assert(orig.reading_id \== restored.reading_id);
    assert(orig.sensor_type \== restored.sensor_type);
    assert(orig.battery_pct \== restored.battery_pct);

    printf("Serialization & Deserialization verified successfully (Wire Size: 20 bytes)\!\\n");
    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Unaligned Pointer Cast in Network Deserialization
Examine the following faulty network message handler:

```c
#include <stdio.h>
#include <stdint.h>

struct __attribute__((packed)) PacketHeader {
    uint8_t  magic;
    uint32_t packet_id; // Offset 1\! Unaligned\!
    uint16_t payload_len; // Offset 5\! Unaligned\!
};

// BUGGY IMPLEMENTATION
void process_incoming_packet_faulty(const uint8_t *raw_network_buffer) {
    // BUG 1: Casting arbitrary byte stream to struct pointer
    // If raw_network_buffer is not aligned, or when accessing 'packet_id':
    const struct PacketHeader *hdr \= (const struct PacketHeader *)raw_network_buffer;

    // BUG 2: Passing address of packed member to function expecting aligned pointer
    // 'hdr->packet_id' is at offset 1. Taking '\&hdr->packet_id' yields an unaligned uint32_t*
    printf("Received Packet ID: %u\\n", hdr->packet_id); // Undefined Behavior on non-x86\!
}
```

### Analysis of Vulnerabilities:
1. **Unaligned Access Fault:** `hdr->packet_id` begins at offset 1. Dereferencing this field requires reading a 4-byte integer from an odd address (`0x...1`). On hardware architectures requiring natural alignment, the CPU raises an alignment exception (`SIGBUS`).
2. **Pointer Aliasing Violation:** Taking the address of an unaligned member (`uint32_t *p \= \&hdr->packet_id`) violates standard C pointer alignment rules. The compiler may emit instructions assuming 4-byte alignment, causing runtime crashes.

### Defensive Fix:
```c
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define PACKET_MAGIC 0x5A

typedef struct {
    uint8_t  magic;
    uint32_t packet_id;
    uint16_t payload_len;
} SafePacketHeader;

bool parse_packet_header_safe(const uint8_t *buf, size_t buf_len, SafePacketHeader *out_hdr) {
    if (\!buf || \!out_hdr || buf_len < 7\) {
        return false;
    }

    out_hdr->magic \= buf[0];
    if (out_hdr->magic \!= PACKET_MAGIC) {
        fprintf(stderr, "Protocol Error: Invalid magic byte (0x%02X)\!\\n", out_hdr->magic);
        return false;
    }

    // Defensive Fix: Use memcpy to safely extract unaligned fields without UB or SIGBUS
    memcpy(\&out_hdr->packet_id, buf \+ 1, sizeof(uint32_t));
    memcpy(\&out_hdr->payload_len, buf \+ 5, sizeof(uint16_t));

    return true;
}
```
