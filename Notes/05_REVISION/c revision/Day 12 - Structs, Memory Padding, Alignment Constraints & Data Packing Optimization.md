\---  
tags:  
  \- c  
  \- structs  
  \- memory-alignment  
  \- padding  
  \- packed-structs  
  \- data-layout  
  \- cache-locality  
date: 2026-09-03  
day: 12  
\---

\# Day 12: Structs, Memory Padding, Alignment Constraints & Data Packing Optimization

\---

\#\# 1\. Quick Reference & Cheat Sheet

\#\#\# Alignment & Padding Rules  
1\. \*\*Natural Alignment:\*\* Every primitive type requires its memory address to be a multiple of its size ($k \\times \\text{sizeof}(T)$):  
   \* \`char\` (1 byte): Any address.  
   \* \`short\` (2 bytes): Address divisible by 2\.  
   \* \`int\`, \`float\` (4 bytes): Address divisible by 4\.  
   \* \`double\`, pointers, \`int64\_t\` (8 bytes on 64-bit): Address divisible by 8\.  
2\. \*\*Member Placement:\*\* Members are allocated in declaration order. If the next member's offset does not satisfy its natural alignment, the compiler injects \*\*Internal Padding\*\* bytes.  
3\. \*\*Structure Total Size & Tail Padding:\*\* The total struct size must be a multiple of its \*\*largest member's alignment requirement\*\*. The compiler injects \*\*Tail Padding\*\* at the end of the struct to ensure every element in an array of that struct starts at an aligned address.

\#\#\# Inspection Macros & Type Qualifiers  
\`\`\`c  
\#include \<stddef.h\>    // For offsetof  
\#include \<stdalign.h\>  // For alignof, alignas (C11)

size\_t offset \= offsetof(struct MyStruct, member\_name);  
size\_t req\_align \= alignof(struct MyStruct); // Or \_Alignof  
\`\`\`

\#\#\# Struct Layout Optimization Rule of Thumb  
\> \*\*Arrange struct members in descending order of size\*\* (e.g. 8-byte pointers/doubles first, then 4-byte ints/floats, then 2-byte shorts, then 1-byte chars). This automatically minimizes or completely eliminates internal padding holes.

\---

\#\# 2\. In-Depth Theory & Low-Level Mechanics

\#\#\# A. Step-by-Step Memory Padding Walkthrough  
Consider this unoptimized struct on an x86\_64 system:

\`\`\`c  
struct Unoptimized {  
    char   a; // 1 byte  
    int    b; // 4 bytes  
    char   c; // 1 byte  
    double d; // 8 bytes  
};  
\`\`\`

Let's trace the offsets assigned by the compiler:  
\* \`a\` placed at offset \`0\` (1 byte).  
\* Next member \`b\` requires 4-byte alignment. Offset 1 is not divisible by 4 $\\implies$ \*\*3 bytes of internal padding\*\* added.  
\* \`b\` placed at offset \`4\` through \`7\` (4 bytes).  
\* \`c\` placed at offset \`8\` (1 byte).  
\* Next member \`d\` requires 8-byte alignment. Offset 9 is not divisible by 8 $\\implies$ \*\*7 bytes of internal padding\*\* added.  
\* \`d\` placed at offset \`16\` through \`23\` (8 bytes).  
\* Total bytes used: 24 bytes. Largest member alignment is 8 (\`double\`). 24 is divisible by 8, so 0 tail padding bytes needed.

\`\`\`text  
Memory Layout of struct Unoptimized (24 Bytes):  
 ┌──────┬───────────────────────┬──────────────┬──────┬───────────────────────────────┬──────────────┐  
 │ a    │ \[Padding: 3 Bytes\]    │ b            │ c    │ \[Padding: 7 Bytes\]            │ d            │  
 │ (1B) │ (0x00, 0x00, 0x00)    │ (4B)         │ (1B) │ (0x00, 0x00, 0x00, 0x00, ...) │ (8B)         │  
 └──────┴───────────────────────┴──────────────┴──────┴───────────────────────────────┴──────────────┘  
 Byte 0  Byte 1           Byte 3 Byte 4 Byte 7 Byte 8 Byte 9                  Byte 15 Byte 16 Byte 23  
\`\`\`  
\* \*\*Payload data:\*\* $1 \+ 4 \+ 1 \+ 8 \= 14$ bytes.  
\* \*\*Wasted memory:\*\* 10 bytes of padding (\*\*41.6% memory wasted\!\*\*).

\#\#\#\# Reordered Layout:  
\`\`\`c  
struct Optimized {  
    double d; // 8 bytes (Offset 0\)  
    int    b; // 4 bytes (Offset 8\)  
    char   a; // 1 byte  (Offset 12\)  
    char   c; // 1 byte  (Offset 13\)  
              // 2 bytes of tail padding to make total size 16 (multiple of 8\)  
};  
\`\`\`  
\* \*\*Total size:\*\* 16 bytes.  
\* \*\*Wasted memory:\*\* Only 2 bytes (12.5% tail padding). Memory footprint reduced by \*\*33.3%\*\*\!

\---

\#\#\# B. Why Tail Padding Exists (Array Alignment Guarantees)  
Suppose \`struct Optimized\` lacked its 2 tail padding bytes, making it 14 bytes in size.  
If you declared an array:  
\`\`\`c  
struct Optimized arr\[2\];  
\`\`\`  
\* \`\&arr\[0\]\` is at address \`0x1000\` (divisible by 8 $\\implies$ \`arr\[0\].d\` is aligned).  
\* \`\&arr\[1\]\` would be at address \`0x1000 \+ 14 \= 0x100E\`.  
\* \`0x100E\` is \*\*NOT divisible by 8\*\*\! Accessing \`arr\[1\].d\` would trigger an unaligned memory access.  
\* Tail padding ensures that every element in an array satisfies the struct's maximum alignment.

\---

\#\#\# C. Packed Structs: Use Cases & Hazards  
Compilers allow suppressing all padding bytes using vendor extensions:  
\* GCC/Clang: \`\_\_attribute\_\_((packed))\`  
\* MSVC: \`\#pragma pack(push, 1)\`

\`\`\`c  
struct \_\_attribute\_\_((packed)) WireHeader {  
    uint8\_t  type;      // 1 byte  
    uint32\_t length;    // 4 bytes (starts at offset 1\!)  
    uint16\_t checksum;  // 2 bytes (starts at offset 5\!)  
}; // Total size: Exactly 7 bytes.  
\`\`\`

\#\#\#\# The Dangers of Packed Structs:  
1\. \*\*Bus Faults (\`SIGBUS\`):\*\* On RISC architectures (ARM, MIPS, SPARC) without hardware unaligned access support, dereferencing an unaligned multi-byte member triggers a CPU fault.  
2\. \*\*Severe CPU Penalties:\*\* On x86, unaligned loads split across two cache lines take 2 to 3 times longer than aligned loads.  
3\. \*\*Pointer Aliasing Violation:\*\*  
   \`\`\`c  
   struct WireHeader hdr;  
   uint32\_t \*len\_ptr \= \&hdr.length; // GCC Warning: taking address of packed member may result in an unaligned pointer value  
   \*len\_ptr \= 42; // Undefined Behavior on many platforms\!  
   \`\`\`

\---

\#\#\# D. Data-Oriented Design: Array-of-Structs (AoS) vs Struct-of-Arrays (SoA)  
In high-throughput systems (game physics, database scans, machine learning):

\`\`\`text  
Array-of-Structs (AoS): \[X Y Z Mass\] \[X Y Z Mass\] \[X Y Z Mass\] ...  
Struct-of-Arrays (SoA): X: \[X1 X2 X3 ...\]  
                         Y: \[Y1 Y2 Y3 ...\]  
                         Z: \[Z1 Z2 Z3 ...\]  
                         Mass: \[M1 M2 M3 ...\]  
\`\`\`  
\* \*\*AoS:\*\* Poor cache utilization if you only need to update \`X\` and \`Y\` positions (CPU still loads \`Z\` and \`Mass\` into L1/L2 cache lines).  
\* \*\*SoA:\*\* Vectorization-friendly (SIMD). CPU cache lines load purely sequential \`X\` coordinates, enabling 4x to 8x throughput using AVX instructions.

\---

\#\# 3\. Thoughtful Mini-Project (\~1 Hour Scope)

\#\#\# Project Title: Struct Memory Layout Visualizer & Wire-Frame Serializer (\`struct\_inspector\`)

\#\#\#\# Objective  
Build a C utility that:  
1\. Programmatically analyzes and prints a visual ASCII memory map of a structure's members and padding gaps using \`offsetof()\` and \`sizeof()\`.  
2\. Implements a safe serialization and deserialization function that packs in-memory structs into canonical wire formats without unaligned pointer dereferences.

\#\#\#\# Complete Starter Code Implementation  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<stddef.h\>  
\#include \<stdbool.h\>  
\#include \<string.h\>  
\#include \<assert.h\>

typedef struct {  
    const char \*name;  
    size\_t offset;  
    size\_t size;  
} MemberInfo;

// Inspect and print byte layout  
void inspect\_struct\_layout(const char \*struct\_name, size\_t total\_size,   
                           const MemberInfo \*members, size\_t member\_count) {  
    printf("====================================================================\\n");  
    printf("  MEMORY LAYOUT VISUALIZER: %s (Total: %zu Bytes)\\n", struct\_name, total\_size);  
    printf("====================================================================\\n");  
    printf(" Offset | Size | Type / Member Name       | Status\\n");  
    printf("--------+------+--------------------------+-------------------------\\n");

    size\_t current\_cursor \= 0;  
    size\_t total\_padding \= 0;

    for (size\_t i \= 0; i \< member\_count; i++) {  
        // Detect internal padding hole before member  
        if (members\[i\].offset \> current\_cursor) {  
            size\_t pad\_size \= members\[i\].offset \- current\_cursor;  
            printf("  \+%04zu |   %2zu | \[INTERNAL PADDING HOLE\]  | WASTED GAP (%zu bytes)\\n",  
                   current\_cursor, pad\_size, pad\_size);  
            total\_padding \+= pad\_size;  
            current\_cursor \= members\[i\].offset;  
        }

        printf("  \+%04zu |   %2zu | %-24s | PAYLOAD DATA\\n",  
               members\[i\].offset, members\[i\].size, members\[i\].name);  
        current\_cursor \+= members\[i\].size;  
    }

    // Detect tail padding hole  
    if (current\_cursor \< total\_size) {  
        size\_t tail\_pad \= total\_size \- current\_cursor;  
        printf("  \+%04zu |   %2zu | \[TAIL PADDING HOLE\]      | WASTED GAP (%zu bytes)\\n",  
               current\_cursor, tail\_pad, tail\_pad);  
        total\_padding \+= tail\_pad;  
    }

    double waste\_pct \= ((double)total\_padding / (double)total\_size) \* 100.0;  
    printf("--------------------------------------------------------------------\\n");  
    printf(" Summary: %zu bytes payload | %zu bytes padding (%.1f%% wasted space)\\n",  
           total\_size \- total\_padding, total\_padding, waste\_pct);  
    printf("====================================================================\\n\\n");  
}

/\* \========================================================================= \*/  
/\*                   DEMO STRUCTURES FOR COMPARISON                          \*/  
/\* \========================================================================= \*/

struct SensorDataUnoptimized {  
    char     sensor\_type; // 1 byte  
    uint64\_t timestamp;   // 8 bytes  
    uint16\_t reading\_id;  // 2 bytes  
    double   value;       // 8 bytes  
    uint8\_t  battery\_pct; // 1 byte  
};

struct SensorDataOptimized {  
    uint64\_t timestamp;   // 8 bytes  
    double   value;       // 8 bytes  
    uint16\_t reading\_id;  // 2 bytes  
    char     sensor\_type; // 1 byte  
    uint8\_t  battery\_pct; // 1 byte  
};

/\* \========================================================================= \*/  
/\*         PORTABLE SERIALIZATION WITHOUT UNALIGNED POINTER CASTS            \*/  
/\* \========================================================================= \*/

// Serializes SensorDataOptimized to packed 20-byte binary wire payload  
void serialize\_sensor\_data(const struct SensorDataOptimized \*src, uint8\_t \*dest\_buf) {  
    // Write timestamp (8 bytes)  
    memcpy(dest\_buf \+ 0, \&src-\>timestamp, sizeof(src-\>timestamp));  
    // Write value (8 bytes)  
    memcpy(dest\_buf \+ 8, \&src-\>value, sizeof(src-\>value));  
    // Write reading\_id (2 bytes)  
    memcpy(dest\_buf \+ 16, \&src-\>reading\_id, sizeof(src-\>reading\_id));  
    // Write sensor\_type (1 byte)  
    dest\_buf\[18\] \= (uint8\_t)src-\>sensor\_type;  
    // Write battery\_pct (1 byte)  
    dest\_buf\[19\] \= src-\>battery\_pct;  
}

void deserialize\_sensor\_data(const uint8\_t \*src\_buf, struct SensorDataOptimized \*dest) {  
    memcpy(\&dest-\>timestamp, src\_buf \+ 0, sizeof(dest-\>timestamp));  
    memcpy(\&dest-\>value, src\_buf \+ 8, sizeof(dest-\>value));  
    memcpy(\&dest-\>reading\_id, src\_buf \+ 16, sizeof(dest-\>reading\_id));  
    dest-\>sensor\_type \= (char)src\_buf\[18\];  
    dest-\>battery\_pct \= src\_buf\[19\];  
}

int main(void) {  
    // 1\. Analyze Unoptimized Struct  
    MemberInfo unopt\_members\[\] \= {  
        { "char sensor\_type", offsetof(struct SensorDataUnoptimized, sensor\_type), sizeof(char) },  
        { "uint64\_t timestamp", offsetof(struct SensorDataUnoptimized, timestamp), sizeof(uint64\_t) },  
        { "uint16\_t reading\_id", offsetof(struct SensorDataUnoptimized, reading\_id), sizeof(uint16\_t) },  
        { "double value", offsetof(struct SensorDataUnoptimized, value), sizeof(double) },  
        { "uint8\_t battery\_pct", offsetof(struct SensorDataUnoptimized, battery\_pct), sizeof(uint8\_t) }  
    };  
    inspect\_struct\_layout("struct SensorDataUnoptimized", sizeof(struct SensorDataUnoptimized),  
                          unopt\_members, sizeof(unopt\_members) / sizeof(MemberInfo));

    // 2\. Analyze Optimized Struct  
    MemberInfo opt\_members\[\] \= {  
        { "uint64\_t timestamp", offsetof(struct SensorDataOptimized, timestamp), sizeof(uint64\_t) },  
        { "double value", offsetof(struct SensorDataOptimized, value), sizeof(double) },  
        { "uint16\_t reading\_id", offsetof(struct SensorDataOptimized, reading\_id), sizeof(uint16\_t) },  
        { "char sensor\_type", offsetof(struct SensorDataOptimized, sensor\_type), sizeof(char) },  
        { "uint8\_t battery\_pct", offsetof(struct SensorDataOptimized, battery\_pct), sizeof(uint8\_t) }  
    };  
    inspect\_struct\_layout("struct SensorDataOptimized", sizeof(struct SensorDataOptimized),  
                          opt\_members, sizeof(opt\_members) / sizeof(MemberInfo));

    // 3\. Test Serialization  
    struct SensorDataOptimized orig \= {  
        .timestamp \= 1725364800ULL,  
        .value \= 98.6,  
        .reading\_id \= 404,  
        .sensor\_type \= 'T',  
        .battery\_pct \= 95  
    };

    uint8\_t wire\_packet\[20\];  
    serialize\_sensor\_data(\&orig, wire\_packet);

    struct SensorDataOptimized restored \= {0};  
    deserialize\_sensor\_data(wire\_packet, \&restored);

    assert(orig.timestamp \== restored.timestamp);  
    assert(orig.value \== restored.value);  
    assert(orig.reading\_id \== restored.reading\_id);  
    assert(orig.sensor\_type \== restored.sensor\_type);  
    assert(orig.battery\_pct \== restored.battery\_pct);

    printf("Serialization & Deserialization verified successfully (Wire Size: 20 bytes)\!\\n");  
    return 0;  
}  
\`\`\`

\---

\#\# 4\. Error Handling & Defensive Programming Challenge

\#\#\# Scenario: The Unaligned Pointer Cast in Network Deserialization  
Examine the following faulty network message handler:

\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdint.h\>

struct \_\_attribute\_\_((packed)) PacketHeader {  
    uint8\_t  magic;  
    uint32\_t packet\_id; // Offset 1\! Unaligned\!  
    uint16\_t payload\_len; // Offset 5\! Unaligned\!  
};

// BUGGY IMPLEMENTATION  
void process\_incoming\_packet\_faulty(const uint8\_t \*raw\_network\_buffer) {  
    // BUG 1: Casting arbitrary byte stream to struct pointer  
    // If raw\_network\_buffer is not aligned, or when accessing 'packet\_id':  
    const struct PacketHeader \*hdr \= (const struct PacketHeader \*)raw\_network\_buffer;

    // BUG 2: Passing address of packed member to function expecting aligned pointer  
    // 'hdr-\>packet\_id' is at offset 1\. Taking '\&hdr-\>packet\_id' yields an unaligned uint32\_t\*  
    printf("Received Packet ID: %u\\n", hdr-\>packet\_id); // Undefined Behavior on non-x86\!  
}  
\`\`\`

\#\#\# Analysis of Vulnerabilities:  
1\. \*\*Unaligned Access Fault:\*\* \`hdr-\>packet\_id\` begins at offset 1\. Dereferencing this field requires reading a 4-byte integer from an odd address (\`0x...1\`). On hardware architectures requiring natural alignment, the CPU raises an alignment exception (\`SIGBUS\`).  
2\. \*\*Pointer Aliasing Violation:\*\* Taking the address of an unaligned member (\`uint32\_t \*p \= \&hdr-\>packet\_id\`) violates standard C pointer alignment rules. The compiler may emit instructions assuming 4-byte alignment, causing runtime crashes.

\#\#\# Defensive Fix:  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdint.h\>  
\#include \<string.h\>  
\#include \<stdbool.h\>

\#define PACKET\_MAGIC 0x5A

typedef struct {  
    uint8\_t  magic;  
    uint32\_t packet\_id;  
    uint16\_t payload\_len;  
} SafePacketHeader;

bool parse\_packet\_header\_safe(const uint8\_t \*buf, size\_t buf\_len, SafePacketHeader \*out\_hdr) {  
    if (\!buf || \!out\_hdr || buf\_len \< 7\) {  
        return false;  
    }

    out\_hdr-\>magic \= buf\[0\];  
    if (out\_hdr-\>magic \!= PACKET\_MAGIC) {  
        fprintf(stderr, "Protocol Error: Invalid magic byte (0x%02X)\!\\n", out\_hdr-\>magic);  
        return false;  
    }

    // Defensive Fix: Use memcpy to safely extract unaligned fields without UB or SIGBUS  
    memcpy(\&out\_hdr-\>packet\_id, buf \+ 1, sizeof(uint32\_t));  
    memcpy(\&out\_hdr-\>payload\_len, buf \+ 5, sizeof(uint16\_t));

    return true;  
}  
\`\`\`  
