\---  
tags:  
  \- c  
  \- unions  
  \- type-punning  
  \- tagged-unions  
  \- bit-fields  
  \- memory-representation  
  \- strict-aliasing  
date: 2026-09-04  
day: 13  
\---

\# Day 13: Unions, Type Punning, Tagged (Discriminated) Unions & Bit-Fields

\---

\#\# 1\. Quick Reference & Cheat Sheet

\#\#\# Union Characteristics  
\* \*\*Shared Storage:\*\* All members share the exact same starting memory address (\`offset \= 0\`).  
\* \*\*Memory Footprint:\*\* Size equals the largest member's size, rounded up to the largest alignment requirement.  
\* \*\*Active Member:\*\* Only one member's value is intended to be stored and accessed at any given time.

\`\`\`c  
union Data {  
    uint32\_t i;     // 4 bytes  
    float    f;     // 4 bytes  
    uint8\_t  b\[4\];  // 4 bytes  
}; // sizeof(union Data) \== 4 bytes  
\`\`\`

\#\#\# Type Punning Comparison  
| Method | C Standard Status | C++ Status | Assembly / Performance | Safety Verdict |  
| :--- | :--- | :--- | :--- | :--- |  
| \*\*Union Punning (\`u.f \= 1.0f; return u.i;\`)\*\* | \*\*Defined & Valid (C99/C11/C17 §6.5.2.3)\*\* | Undefined Behavior | Zero-cost (\`movd\` register copy) | \*\*Idiomatic in C\*\* |  
| \*\*Pointer Casting (\`\*(int\*)\&my\_float\`)\*\* | \*\*Undefined Behavior (Strict Aliasing)\*\* | Undefined Behavior | Compiler may reorder loads/stores | \*\*DANGEROUS BUG\*\* |  
| \*\*\`memcpy(\&my\_int, \&my\_float, 4)\`\*\* | \*\*Fully Defined & Portable\*\* | Fully Defined | Optimized away to 0 instructions | \*\*Recommended & Portable\*\* |

\#\#\# Bit-Fields Essentials & Gotchas  
\`\`\`c  
struct Flags {  
    unsigned int is\_active   : 1;  // 1 bit: values 0 or 1  
    unsigned int mode        : 3;  // 3 bits: values 0 to 7  
    int          signed\_flag : 1;  // TRAP: 1-bit signed holds values 0 and \-1, NOT 1\!  
};  
\`\`\`  
\* \*\*Cannot take address:\*\* \`\&flags.is\_active\` is illegal (CPU cannot address fractional bytes).  
\* \*\*Endian / Compiler Dependent:\*\* Bit-field ordering within a storage unit is implementation-defined. Do not use for binary wire protocols across architectures.

\---

\#\# 2\. In-Depth Theory & Low-Level Mechanics

\#\#\# A. Memory Overlap & Union Storage Layout  
In a union, every field begins at base address \`0x0000\`. Writing to one field modifies the overlapping bit patterns of all other fields.

\`\`\`text  
Memory Layout of union FloatInspector:  
 ┌────────────────────────────────────────────────────────────────────────┐  
 │ Byte 0          │ Byte 1          │ Byte 2          │ Byte 3          │  
 ├────────────────────────────────────────────────────────────────────────┤  
 │ uint32\_t raw\_bits                                                      │  
 ├────────────────────────────────────────────────────────────────────────┤  
 │ float    f32                                                           │  
 ├─────────────────┼─────────────────┼─────────────────┼──────────────────┤  
 │ bytes\[0\]        │ bytes\[1\]        │ bytes\[2\]        │ bytes\[3\]         │  
 └─────────────────┴─────────────────┴─────────────────┴──────────────────┘  
 0x1000            0x1001            0x1002            0x1003  
\`\`\`

\#\#\# B. Strict Aliasing & Why Pointer Punning Fails  
The \*\*Strict Aliasing Rule\*\* (C17 §6.5) states that two pointers of different types (with few exceptions, such as \`char\*\`) cannot point to the same memory location. The compiler's optimizer assumes writes through one pointer type cannot affect reads from another pointer type.

\#\#\#\# The Optimizer Breakdown Bug:  
\`\`\`c  
// BROKEN: Strict Aliasing Violation  
uint32\_t swap\_endian\_faulty(float f) {  
    uint32\_t \*u\_ptr \= (uint32\_t \*)\&f; // VIOLATION\!  
    // Compiler optimizer under \-O2 assumes \*u\_ptr and f cannot alias.  
    // It may hoist or reorder reads and writes, returning stale CPU register values.  
    return \*u\_ptr;  
}  
\`\`\`

\#\#\#\# The Safe Alternatives:  
1\. \*\*Union-Based Punning:\*\* The ISO C standard explicitly guarantees that reading from a different union member than the one most recently written to reads the underlying object representation.  
2\. \*\*\`memcpy\`:\*\* Completely avoids aliasing issues. Modern compilers (GCC/Clang/MSVC) detect \`memcpy\` of scalar types and optimize it directly into CPU register moves without memory round-trips.

\---

\#\#\# C. The 1-Bit Signed Bit-Field Trap  
Consider:  
\`\`\`c  
struct Trap {  
    int flag : 1; // Signed 1-bit integer  
};

struct Trap t;  
t.flag \= 1;  
if (t.flag \== 1\) {  
    printf("Condition Met\!\\n");  
} else {  
    printf("TRAP: Condition NOT Met\!\\n");  
}  
\`\`\`  
\* \*\*Explanation:\*\* A signed 1-bit integer in two's complement has 1 sign bit and 0 magnitude bits. Its possible values are \`0\` and \`-1\`.  
\* Storing \`1\` into \`t.flag\` sets the bit to \`1\`. When evaluated, the MSB is sign-extended, producing \`-1\`.  
\* \`-1 \== 1\` evaluates to \*\*false\*\*\!  
\* \*\*Golden Rule:\*\* Always declare bit-fields as \`unsigned int\`, \`uint32\_t\`, or \`\_Bool\`.

\---

\#\#\# D. Tagged (Discriminated) Unions: Sum Types in C  
Because a bare union does not know which member is currently valid, a \*\*Tagged Union\*\* bundles an explicit discriminator \`enum\` with the union inside an outer struct.

\`\`\`text  
Tagged Union (Variant) Memory Structure:  
 ┌───────────────────────────┬────────────────────────────────────────────┐  
 │ Discriminator (Tag)       │ Union Payload Area                         │  
 │ enum VariantType tag      │ union { int64\_t i; double f; char \*str; }  │  
 └───────────────────────────┴────────────────────────────────────────────┘  
\`\`\`  
This is the standard architectural pattern for building AST nodes, dynamic interpreters, and message dispatchers.

\---

\#\# 3\. Thoughtful Mini-Project (\~1 Hour Scope)

\#\#\# Project Title: Tagged-Union Dynamic Variant & IEEE-754 Float Bit Inspector (\`variant\_inspector\`)

\#\#\#\# Objective  
Build a C utility that:  
1\. Implements an \*\*IEEE-754 Single-Precision Float Inspector\*\* using union type-punning to extract the Sign bit, Biased Exponent, and Mantissa fraction.  
2\. Implements a safe \*\*Tagged Union (Variant)\*\* system supporting dynamic types (\`NULL\`, \`INT\`, \`FLOAT\`, \`STRING\`) with strict type-safety accessors.

\#\#\#\# Complete Starter Code Implementation  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<stdbool.h\>  
\#include \<string.h\>  
\#include \<assert.h\>

/\* \========================================================================= \*/  
/\*               1\. IEEE-754 SINGLE-PRECISION FLOAT INSPECTOR                \*/  
/\* \========================================================================= \*/

typedef union {  
    float f;  
    uint32\_t bits;  
    struct {  
        uint32\_t mantissa : 23;  
        uint32\_t exponent : 8;  
        uint32\_t sign     : 1;  
    } parts; // Architecture-specific bitfield layout  
} FloatPunningUnion;

void inspect\_float(float value) {  
    FloatPunningUnion pun;  
    pun.f \= value;

    uint32\_t sign \= (pun.bits \>\> 31\) & 0x01;  
    uint32\_t exp  \= (pun.bits \>\> 23\) & 0xFF;  
    uint32\_t mant \= pun.bits & 0x7FFFFF;

    int unbiased\_exp \= (exp \== 0\) ? \-126 : (int)exp \- 127;

    printf("====================================================================\\n");  
    printf(" IEEE-754 FLOAT INSPECTION: %f\\n", value);  
    printf(" Raw 32-bit Hex: 0x%08X\\n", pun.bits);  
    printf(" Sign Bit:       %u (%s)\\n", sign, sign ? "Negative \[-\]" : "Positive \[+\]");  
    printf(" Exponent (Raw): %u (0x%02X) | Unbiased Exponent: %d (Bias: 127)\\n", exp, exp, unbiased\_exp);  
    printf(" Mantissa (Raw): 0x%06X (Bits: 0b", mant);  
    for (int i \= 22; i \>= 0; i--) {  
        putchar((mant & (1 \<\< i)) ? '1' : '0');  
    }  
    printf(")\\n====================================================================\\n\\n");  
}

/\* \========================================================================= \*/  
/\*                   2\. TAGGED UNION (DYNAMIC VARIANT)                       \*/  
/\* \========================================================================= \*/

typedef enum {  
    VAR\_TYPE\_NULL,  
    VAR\_TYPE\_BOOL,  
    VAR\_TYPE\_INT64,  
    VAR\_TYPE\_DOUBLE,  
    VAR\_TYPE\_STRING  
} VariantType;

typedef struct {  
    VariantType type;  
    union {  
        bool    b\_val;  
        int64\_t i\_val;  
        double  d\_val;  
        char   \*s\_val; // Heap-allocated string  
    } as;  
} Variant;

Variant var\_make\_null(void) {  
    return (Variant){ .type \= VAR\_TYPE\_NULL };  
}

Variant var\_make\_bool(bool b) {  
    Variant v;  
    v.type \= VAR\_TYPE\_BOOL;  
    v.as.b\_val \= b;  
    return v;  
}

Variant var\_make\_int(int64\_t i) {  
    Variant v;  
    v.type \= VAR\_TYPE\_INT64;  
    v.as.i\_val \= i;  
    return v;  
}

Variant var\_make\_double(double d) {  
    Variant v;  
    v.type \= VAR\_TYPE\_DOUBLE;  
    v.as.d\_val \= d;  
    return v;  
}

Variant var\_make\_string(const char \*str) {  
    Variant v;  
    v.type \= VAR\_TYPE\_STRING;  
    v.as.s\_val \= str ? strdup(str) : NULL;  
    return v;  
}

void var\_free(Variant \*v) {  
    if (\!v) return;  
    if (v-\>type \== VAR\_TYPE\_STRING && v-\>as.s\_val) {  
        free(v-\>as.s\_val);  
        v-\>as.s\_val \= NULL;  
    }  
    v-\>type \= VAR\_TYPE\_NULL;  
}

void var\_print(const Variant \*v) {  
    if (\!v) return;  
    switch (v-\>type) {  
        case VAR\_TYPE\_NULL:  
            printf("Variant(Null)\\n");  
            break;  
        case VAR\_TYPE\_BOOL:  
            printf("Variant(Bool: %s)\\n", v-\>as.b\_val ? "true" : "false");  
            break;  
        case VAR\_TYPE\_INT64:  
            printf("Variant(Int64: %lld)\\n", (long long)v-\>as.i\_val);  
            break;  
        case VAR\_TYPE\_DOUBLE:  
            printf("Variant(Double: %f)\\n", v-\>as.d\_val);  
            break;  
        case VAR\_TYPE\_STRING:  
            printf("Variant(String: \\"%s\\")\\n", v-\>as.s\_val ? v-\>as.s\_val : "(null)");  
            break;  
    }  
}

// Type-Safe Accessor with Tag Assertion  
bool var\_get\_int(const Variant \*v, int64\_t \*out\_val) {  
    if (\!v || v-\>type \!= VAR\_TYPE\_INT64 || \!out\_val) return false;  
    \*out\_val \= v-\>as.i\_val;  
    return true;  
}

int main(void) {  
    // 1\. Inspect Float Representations  
    inspect\_float(-13.625f);  
    inspect\_float(0.15625f);

    // 2\. Test Tagged Union System  
    printf("=== Demonstrating Tagged Union Variant \===\\n");  
    Variant list\[4\];  
    list\[0\] \= var\_make\_int(42);  
    list\[1\] \= var\_make\_double(3.1415926535);  
    list\[2\] \= var\_make\_string("C Programming Mastery");  
    list\[3\] \= var\_make\_bool(true);

    for (size\_t i \= 0; i \< 4; i++) {  
        printf("  \[%zu\] ", i);  
        var\_print(\&list\[i\]);  
    }

    int64\_t extracted\_int \= 0;  
    bool ok \= var\_get\_int(\&list\[0\], \&extracted\_int);  
    assert(ok && extracted\_int \== 42);

    // Clean up heap-allocated variants  
    for (size\_t i \= 0; i \< 4; i++) {  
        var\_free(\&list\[i\]);  
    }

    printf("All variant memory cleanly released\!\\n");  
    return 0;  
}  
\`\`\`

\---

\#\# 4\. Error Handling & Defensive Programming Challenge

\#\#\# Scenario: The Untagged Union Access & Signed Bit-Field Evaluation Flaw  
Examine the following buggy device telemetry parser:

\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdint.h\>

struct DeviceConfig {  
    // BUG 1: Signed 1-bit bitfield  
    int is\_enabled : 1;   
    int is\_encrypted : 1;  
    unsigned int baud\_rate\_code : 4;  
};

union Payload {  
    uint32\_t raw\_ip;  
    char text\[16\];  
    double coordinate;  
};

// BUGGY IMPLEMENTATION  
void process\_packet\_faulty(const union Payload \*p, int packet\_type) {  
    // BUG 2: No discriminator verification\!  
    // Accessing union member without validating that it was the active member written  
    printf("Interpreted as IP: 0x%08X\\n", p-\>raw\_ip);  
    printf("Interpreted as Text: %s\\n", p-\>text); // If coordinate was stored, text may lack null-terminator\!  
}

void test\_config(void) {  
    struct DeviceConfig cfg;  
    cfg.is\_enabled \= 1;

    // BUG 1 Manifestation:  
    if (cfg.is\_enabled \== 1\) {  
        printf("Device Enabled\!\\n");  
    } else {  
        printf("Device Disabled\!\\n"); // PRINTS THIS\!  
    }  
}  
\`\`\`

\#\#\# Analysis of Vulnerabilities:  
1\. \*\*Signed Bit-Field Equality Failure:\*\* \`cfg.is\_enabled\` is signed. Assigning \`1\` yields \`-1\`. Testing \`cfg.is\_enabled \== 1\` fails.  
2\. \*\*Buffer Over-read in Untagged Union:\*\* Reading \`p-\>text\` when \`p-\>coordinate\` was populated reads raw 64-bit IEEE-754 bytes as a C-string. If the bytes contain no null terminator, \`printf("%s")\` reads out-of-bounds stack/heap memory until a random \`0x00\` is encountered.

\#\#\# Defensive Fix:  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdint.h\>  
\#include \<stdbool.h\>  
\#include \<string.h\>

// Fix 1: Always use unsigned or explicit bool for bit-fields  
struct SafeDeviceConfig {  
    unsigned int is\_enabled   : 1;  
    unsigned int is\_encrypted : 1;  
    unsigned int baud\_rate    : 4;  
};

// Fix 2: Wrap union with discriminator tag  
typedef enum {  
    PAYLOAD\_TYPE\_IP,  
    PAYLOAD\_TYPE\_TEXT,  
    PAYLOAD\_TYPE\_COORD  
} SafePayloadType;

typedef struct {  
    SafePayloadType type;  
    union {  
        uint32\_t raw\_ip;  
        char text\[16\];  
        double coordinate;  
    } data;  
} SafePacket;

bool process\_packet\_safe(const SafePacket \*p) {  
    if (\!p) return false;

    switch (p-\>type) {  
        case PAYLOAD\_TYPE\_IP:  
            printf("Safe IP Address: 0x%08X\\n", p-\>data.raw\_ip);  
            return true;

        case PAYLOAD\_TYPE\_TEXT: {  
            // Defensive guarantee: ensure null termination within fixed buffer  
            char safe\_str\[17\];  
            memcpy(safe\_str, p-\>data.text, 16);  
            safe\_str\[16\] \= '\\0';  
            printf("Safe Text: %s\\n", safe\_str);  
            return true;  
        }

        case PAYLOAD\_TYPE\_COORD:  
            printf("Safe Coordinate: %f\\n", p-\>data.coordinate);  
            return true;

        default:  
            fprintf(stderr, "Error: Unknown payload type\!\\n");  
            return false;  
    }  
}  
\`\`\`  
