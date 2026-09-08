\---  
tags:  
  \- c  
  \- week-2-synthesis  
  \- mega-project  
  \- dynamic-memory  
  \- structs-alignment  
  \- serialization  
  \- arena-allocator  
  \- json-parser  
date: 2026-09-06  
day: 15  
\---

\# Day 15: Week 2 Synthesis & Mega Project — Custom Binary & JSON Serialization Engine with Arena Memory

\---

\#\# 1\. Quick Reference & Cheat Sheet (Week 2 Synthesis)

\#\#\# Dynamic Memory Management Invariants  
\* \*\*\`malloc(size)\`:\*\* Allocates uninitialized memory. Always check for \`NULL\`.  
\* \*\*\`calloc(n, size)\`:\*\* Allocates zero-initialized memory. Protects against integer overflow during multiplication.  
\* \*\*\`realloc(ptr, new\_size)\`:\*\* Resizes existing block. Never assign directly back to \`ptr\` (\`ptr \= realloc(ptr, ...)\` leaks memory on failure).  
\* \*\*Pointer Poisoning:\*\* Always set pointers to \`NULL\` immediately after \`free()\` to prevent Use-After-Free (UAF) and Double-Free bugs.

\#\#\# Structs, Alignment & Padding Rules  
\* \*\*Natural Alignment:\*\* Primitive types require memory addresses divisible by their size (\`int\` at multiple of 4, \`double\`/pointers at multiple of 8).  
\* \*\*Internal Padding:\*\* Injected between members to align subsequent fields.  
\* \*\*Tail Padding:\*\* Injected at the struct tail so that elements in an array (\`struct T arr\[N\]\`) preserve the largest member's alignment.  
\* \*\*Optimization Rule:\*\* Declare struct members in \*\*descending order of size\*\* (8-byte $\\to$ 4-byte $\\to$ 2-byte $\\to$ 1-byte) to eliminate internal padding holes.  
\* \*\*Packed Structs (\`\_\_attribute\_\_((packed))\`):\*\* Eliminates padding for network wire formats, but taking the address of unaligned members violates strict alignment and triggers bus errors (\`SIGBUS\`) on non-x86 architectures.

\#\#\# Unions, Type Punning & Copying  
\* \*\*Union Storage:\*\* All members share base offset \`0\`. Size is determined by the largest member rounded to largest alignment.  
\* \*\*Strict Aliasing Rule:\*\* Reinterpreting memory via pointer casts (\`\*(int\*)\&my\_float\`) causes undefined behavior under \`-O2\`/\`-O3\`. Use union punning or \`memcpy\`.  
\* \*\*Tagged Unions:\*\* Always bundle an explicit discriminator \`enum\` with a union to verify the active variant before access.  
\* \*\*Shallow Copy:\*\* Bitwise copy (\`\*dest \= \*src\`) duplicates pointer addresses, creating shared aliasing that causes double-free crashes.  
\* \*\*Deep Copy:\*\* Recursively duplicates every pointer target into fresh heap allocations.

\---

\#\# 2\. In-Depth Theory & Low-Level Mechanics

\#\#\# A. Binary vs Textual (JSON) Serialization  
| Attribute | JSON / Textual Serialization | Packed Binary Wire Format |  
| :--- | :--- | :--- |  
| \*\*Human Readability\*\* | High (plain ASCII/UTF-8 text) | None (raw byte stream) |  
| \*\*Parsing Overhead\*\* | High (string scans, float conversions, whitespace parsing) | Minimal (direct byte slicing and integer deserialization) |  
| \*\*Payload Size\*\* | Bulky (e.g. integer \`12345678\` takes 8 ASCII bytes) | Compact (\`uint32\_t\` takes exactly 4 raw bytes) |  
| \*\*Type Integrity\*\* | Requires string-to-number lexical parsing | Fixed type tags / schemas embedded in stream |

\---

\#\#\# B. Arena Allocators in Serialization Engines  
Tree structures (like JSON ASTs or nested configuration dictionaries) involve dozens or hundreds of tiny dynamic allocations (keys, strings, child nodes). Calling \`malloc()\` for every token causes:  
1\. \*\*High Overhead:\*\* Each 8-byte chunk incurs 8–16 bytes of heap metadata headers.  
2\. \*\*Memory Fragmentation:\*\* Freeing nodes individually leaves holes across the heap.  
3\. \*\*Complex Error Cleanup:\*\* If parsing fails mid-stream, unwinding and freeing partially allocated trees requires tedious recursive rollback code.

\`\`\`text  
Traditional malloc() Tree:                   Arena-Allocated Tree:  
 Heap:                                        Arena Contiguous Buffer (e.g. 64 KB):  
 ┌────────┐   ┌────────┐   ┌────────┐        ┌─────────┬─────────┬─────────┬──────────────┐  
 │ Node A │   │ Node B │   │ Node C │        │ Node A  │ Node B  │ Node C  │ Free Scratch │  
 └────────┘   └────────┘   └────────┘        └─────────┴─────────┴─────────┴──────────────┘  
 Scattered across RAM with metadata           ▲  
                                              └── Bump pointer advances sequentially.  
                                                  Deallocation is a single O(1) reset\!  
\`\`\`

\---

\#\#\# C. TLV (Type-Length-Value) Binary Encoding  
A robust binary protocol formats every value into a \*\*TLV tuple\*\*:  
\* \*\*Type (1 byte):\*\* Discriminator identifying the data type (e.g., \`0x01\` \= Null, \`0x02\` \= Int64, \`0x03\` \= Double, \`0x04\` \= String, \`0x05\` \= Array, \`0x06\` \= Object).  
\* \*\*Length (4 bytes):\*\* Unsigned integer specifying the byte length of the payload.  
\* \*\*Value (Variable):\*\* Raw payload bytes (e.g. Little-Endian integer or raw UTF-8 characters).

\---

\#\# 3\. Thoughtful Mini-Project (\~1 Hour Scope)

\#\#\# Project Title: Compact Binary TLV Stream Packer & Validator (\`tlv\_stream\`)

\#\#\#\# Objective  
Build a binary serializer and deserializer that encodes primitive variables (\`int32\_t\`, \`double\`, length-prefixed strings) into a contiguous TLV byte buffer and unpacks them with strict bounds-checking.

\#\#\#\# Complete Starter Code Implementation  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<stdbool.h\>  
\#include \<string.h\>  
\#include \<assert.h\>

\#define TLV\_INT32  0x01  
\#define TLV\_DOUBLE 0x02  
\#define TLV\_STRING 0x03

typedef struct {  
    uint8\_t \*data;  
    size\_t capacity;  
    size\_t size;  
} ByteBuffer;

ByteBuffer \*bytebuf\_create(size\_t initial\_cap) {  
    ByteBuffer \*b \= (ByteBuffer \*)malloc(sizeof(ByteBuffer));  
    b-\>data \= (uint8\_t \*)malloc(initial\_cap);  
    b-\>capacity \= initial\_cap;  
    b-\>size \= 0;  
    return b;  
}

void bytebuf\_free(ByteBuffer \*b) {  
    if (\!b) return;  
    free(b-\>data);  
    free(b);  
}

static bool bytebuf\_ensure(ByteBuffer \*b, size\_t extra) {  
    if (b-\>size \+ extra \> b-\>capacity) {  
        size\_t new\_cap \= (b-\>capacity \* 2\) \+ extra;  
        uint8\_t \*new\_data \= (uint8\_t \*)realloc(b-\>data, new\_cap);  
        if (\!new\_data) return false;  
        b-\>data \= new\_data;  
        b-\>capacity \= new\_cap;  
    }  
    return true;  
}

bool tlv\_pack\_int32(ByteBuffer \*b, int32\_t val) {  
    if (\!bytebuf\_ensure(b, 1 \+ 4 \+ 4)) return false;  
    b-\>data\[b-\>size++\] \= TLV\_INT32;  
    uint32\_t len \= 4;  
    memcpy(b-\>data \+ b-\>size, \&len, 4);  
    b-\>size \+= 4;  
    memcpy(b-\>data \+ b-\>size, \&val, 4);  
    b-\>size \+= 4;  
    return true;  
}

bool tlv\_pack\_double(ByteBuffer \*b, double val) {  
    if (\!bytebuf\_ensure(b, 1 \+ 4 \+ 8)) return false;  
    b-\>data\[b-\>size++\] \= TLV\_DOUBLE;  
    uint32\_t len \= 8;  
    memcpy(b-\>data \+ b-\>size, \&len, 4);  
    b-\>size \+= 4;  
    memcpy(b-\>data \+ b-\>size, \&val, 8);  
    b-\>size \+= 8;  
    return true;  
}

bool tlv\_pack\_string(ByteBuffer \*b, const char \*str) {  
    size\_t s\_len \= strlen(str);  
    if (\!bytebuf\_ensure(b, 1 \+ 4 \+ s\_len)) return false;  
    b-\>data\[b-\>size++\] \= TLV\_STRING;  
    uint32\_t len \= (uint32\_t)s\_len;  
    memcpy(b-\>data \+ b-\>size, \&len, 4);  
    b-\>size \+= 4;  
    memcpy(b-\>data \+ b-\>size, str, s\_len);  
    b-\>size \+= s\_len;  
    return true;  
}

void tlv\_unpack\_and\_print(const uint8\_t \*buf, size\_t total\_len) {  
    printf("--- Unpacking TLV Stream (%zu Bytes) \---\\n", total\_len);  
    size\_t cursor \= 0;  
    while (cursor \< total\_len) {  
        if (cursor \+ 5 \> total\_len) {  
            fprintf(stderr, "Error: Truncated header\!\\n");  
            return;  
        }  
        uint8\_t type \= buf\[cursor++\];  
        uint32\_t len \= 0;  
        memcpy(\&len, buf \+ cursor, 4);  
        cursor \+= 4;

        if (cursor \+ len \> total\_len) {  
            fprintf(stderr, "Error: Payload exceeds buffer boundary\!\\n");  
            return;  
        }

        switch (type) {  
            case TLV\_INT32: {  
                int32\_t v;  
                memcpy(\&v, buf \+ cursor, 4);  
                printf("  \[TAG: INT32\]  Length: %u | Value: %d\\n", len, v);  
                break;  
            }  
            case TLV\_DOUBLE: {  
                double v;  
                memcpy(\&v, buf \+ cursor, 8);  
                printf("  \[TAG: DOUBLE\] Length: %u | Value: %f\\n", len, v);  
                break;  
            }  
            case TLV\_STRING: {  
                printf("  \[TAG: STRING\] Length: %u | Value: \\"%.\*s\\"\\n", len, (int)len, buf \+ cursor);  
                break;  
            }  
            default:  
                printf("  \[TAG: UNKNOWN (0x%02X)\] Length: %u\\n", type, len);  
                break;  
        }  
        cursor \+= len;  
    }  
    printf("--- Stream Parsing Successfully Complete \---\\n\\n");  
}

int main(void) {  
    ByteBuffer \*b \= bytebuf\_create(32);  
    tlv\_pack\_int32(b, 42);  
    tlv\_pack\_double(b, 3.1415926535);  
    tlv\_pack\_string(b, "Hello TLV Protocol\!");

    tlv\_unpack\_and\_print(b-\>data, b-\>size);  
    bytebuf\_free(b);  
    return 0;  
}  
\`\`\`

\---

\#\# 4\. Error Handling & Defensive Programming Challenge

\#\#\# Scenario: The Untrusted Payload Length & Integer Wrap-Around Deserialization Bug  
Examine the following faulty binary deserializer:

\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<string.h\>

// BUGGY IMPLEMENTATION  
char \*extract\_string\_faulty(const uint8\_t \*packet, size\_t packet\_len, size\_t \*cursor) {  
    // Read 32-bit length directly from untrusted network byte stream  
    uint32\_t str\_len;  
    memcpy(\&str\_len, packet \+ \*cursor, 4);  
    \*cursor \+= 4;

    // BUG 1: Integer overflow on addition\! If str\_len \== UINT32\_MAX, str\_len \+ 1 wraps to 0\.  
    // malloc(0) allocates minimal chunk; subsequent memcpy causes Massive Heap Overflow.  
    char \*str \= (char \*)malloc(str\_len \+ 1);

    // BUG 2: Unbounded memory read\! If \*cursor \+ str\_len \> packet\_len,  
    // memcpy reads out-of-bounds process memory into string buffer (Heartbleed style).  
    memcpy(str, packet \+ \*cursor, str\_len);  
    str\[str\_len\] \= '\\0';  
    \*cursor \+= str\_len;

    return str;  
}  
\`\`\`

\#\#\# Analysis of Vulnerabilities:  
1\. \*\*Integer Wrap-Around:\*\* If \`str\_len \= 0xFFFFFFFF\`, \`str\_len \+ 1\` wraps to \`0\`. Allocator returns a tiny block. \`memcpy\` then copies 4 GB of data, crashing the process or enabling arbitrary code execution.  
2\. \*\*Out-of-Bounds Buffer Over-Read:\*\* The length field is trusted without verifying that \`packet\_len \- \*cursor \>= str\_len\`.

\#\#\# Defensive Fix:  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<string.h\>  
\#include \<stdbool.h\>

\#define MAX\_SAFE\_STRING\_LEN (1024 \* 1024\) // Cap strings to 1 MB

bool extract\_string\_safe(const uint8\_t \*packet, size\_t packet\_len, size\_t \*cursor, char \*\*out\_str) {  
    if (\!packet || \!cursor || \!out\_str) return false;

    // Defensive Check 1: Ensure length field itself is within packet  
    if (\*cursor \> packet\_len || packet\_len \- \*cursor \< sizeof(uint32\_t)) {  
        fprintf(stderr, "Defensive Error: Truncated packet, cannot read length prefix\!\\n");  
        return false;  
    }

    uint32\_t str\_len;  
    memcpy(\&str\_len, packet \+ \*cursor, sizeof(uint32\_t));

    // Defensive Check 2: Cap length to maximum realistic threshold to prevent DoS  
    if (str\_len \> MAX\_SAFE\_STRING\_LEN) {  
        fprintf(stderr, "Defensive Error: String length (%u) exceeds maximum safe size\!\\n", str\_len);  
        return false;  
    }

    // Defensive Check 3: Check remaining bytes using safe subtraction  
    size\_t offset\_after\_len \= \*cursor \+ sizeof(uint32\_t);  
    if (str\_len \> packet\_len \- offset\_after\_len) {  
        fprintf(stderr, "Defensive Error: Payload length (%u) exceeds packet boundary (%zu remaining)\!\\n",  
                str\_len, packet\_len \- offset\_after\_len);  
        return false;  
    }

    // Allocate with checked size  
    char \*str \= (char \*)malloc((size\_t)str\_len \+ 1);  
    if (\!str) return false;

    memcpy(str, packet \+ offset\_after\_len, str\_len);  
    str\[str\_len\] \= '\\0'; // Guarantee null-termination

    \*cursor \= offset\_after\_len \+ str\_len;  
    \*out\_str \= str;  
    return true;  
}  
\`\`\`

\---

\#\# 5\. WEEKLY MEGA PROJECT (Week 2 Capstone)

\#\#\# Project Title: Dual Binary & JSON Serialization Engine with Arena Memory Pool (\`arena\_serializer\`)

\#\#\#\# Architectural Overview  
Build an end-to-end Serialization Engine that models a polymorphic JSON/Document Value AST, provides zero-leak memory management via a \*\*Custom Memory Arena\*\*, and serializes/deserializes between human-readable JSON text and compact binary wire formats.

\`\`\`text  
┌────────────────────────────────────────────────────────────────────────┐  
│                        MemoryArena (Bump Allocator)                    │  
│   Allocates all AST Nodes, String Literals, Array & Object Buckets     │  
├────────────────────────────────────────────────────────────────────────┤  
│                       JsonValue AST (Tagged Union)                     │  
│  \- JSON\_NULL                                                           │  
│  \- JSON\_BOOL   (bool)                                                  │  
│  \- JSON\_INT    (int64\_t)                                               │  
│  \- JSON\_DOUBLE (double)                                                │  
│  \- JSON\_STRING (char\*)                                                 │  
│  \- JSON\_ARRAY  (JsonValue\*\*, count, capacity)                          │  
│  \- JSON\_OBJECT (JsonKeyValue\*, count, capacity)                        │  
├────────────────────────────────────────────────────────────────────────┤  
│ Engines:                                                               │  
│  1\. JSON Text Stringifier: json\_stringify(val, out\_buf)                │  
│  2\. Binary Wire Serializer: json\_to\_binary(val, out\_bytebuf)            │  
│  3\. Binary Wire Unpacker: binary\_to\_json(arena, bytebuf)               │  
└────────────────────────────────────────────────────────────────────────┘  
\`\`\`

\#\#\#\# Complete Modular Implementation (\`arena\_serializer.c\`)  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<stdbool.h\>  
\#include \<string.h\>  
\#include \<inttypes.h\>  
\#include \<assert.h\>

/\* \========================================================================= \*/  
/\*                          1\. CUSTOM MEMORY ARENA                           \*/  
/\* \========================================================================= \*/

typedef struct {  
    uint8\_t \*buffer;  
    size\_t capacity;  
    size\_t offset;  
} MemoryArena;

MemoryArena \*arena\_create(size\_t capacity) {  
    MemoryArena \*a \= (MemoryArena \*)malloc(sizeof(MemoryArena));  
    a-\>buffer \= (uint8\_t \*)malloc(capacity);  
    a-\>capacity \= capacity;  
    a-\>offset \= 0;  
    return a;  
}

void arena\_destroy(MemoryArena \*a) {  
    if (\!a) return;  
    free(a-\>buffer);  
    free(a);  
}

void \*arena\_alloc(MemoryArena \*a, size\_t size) {  
    // 8-byte natural alignment  
    size\_t aligned\_size \= (size \+ 7\) & \~7ULL;  
    if (a-\>offset \+ aligned\_size \> a-\>capacity) {  
        fprintf(stderr, "Arena OOM: Exceeded %zu bytes\!\\n", a-\>capacity);  
        return NULL;  
    }  
    void \*ptr \= a-\>buffer \+ a-\>offset;  
    a-\>offset \+= aligned\_size;  
    memset(ptr, 0, aligned\_size);  
    return ptr;  
}

char \*arena\_strdup(MemoryArena \*a, const char \*s) {  
    if (\!s) return NULL;  
    size\_t len \= strlen(s);  
    char \*copy \= (char \*)arena\_alloc(a, len \+ 1);  
    memcpy(copy, s, len);  
    copy\[len\] \= '\\0';  
    return copy;  
}

/\* \========================================================================= \*/  
/\*                          2\. JSON AST DATA MODEL                           \*/  
/\* \========================================================================= \*/

typedef enum {  
    JSON\_NULL \= 0x00,  
    JSON\_BOOL \= 0x01,  
    JSON\_INT  \= 0x02,  
    JSON\_DOUBLE \= 0x03,  
    JSON\_STRING \= 0x04,  
    JSON\_ARRAY  \= 0x05,  
    JSON\_OBJECT \= 0x06  
} JsonType;

typedef struct JsonValue JsonValue;  
typedef struct JsonKeyValue JsonKeyValue;

struct JsonKeyValue {  
    const char \*key;  
    JsonValue  \*value;  
};

struct JsonValue {  
    JsonType type;  
    union {  
        bool b\_val;  
        int64\_t i\_val;  
        double d\_val;  
        const char \*s\_val;  
        struct {  
            JsonValue \*\*items;  
            size\_t count;  
            size\_t capacity;  
        } arr;  
        struct {  
            JsonKeyValue \*pairs;  
            size\_t count;  
            size\_t capacity;  
        } obj;  
    } as;  
};

// Node Constructors using Arena Memory  
JsonValue \*json\_null(MemoryArena \*a) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_NULL;  
    return v;  
}

JsonValue \*json\_bool(MemoryArena \*a, bool b) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_BOOL;  
    v-\>as.b\_val \= b;  
    return v;  
}

JsonValue \*json\_int(MemoryArena \*a, int64\_t i) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_INT;  
    v-\>as.i\_val \= i;  
    return v;  
}

JsonValue \*json\_double(MemoryArena \*a, double d) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_DOUBLE;  
    v-\>as.d\_val \= d;  
    return v;  
}

JsonValue \*json\_string(MemoryArena \*a, const char \*s) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_STRING;  
    v-\>as.s\_val \= arena\_strdup(a, s);  
    return v;  
}

JsonValue \*json\_array(MemoryArena \*a, size\_t initial\_cap) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_ARRAY;  
    v-\>as.arr.count \= 0;  
    v-\>as.arr.capacity \= initial\_cap ? initial\_cap : 4;  
    v-\>as.arr.items \= (JsonValue \*\*)arena\_alloc(a, v-\>as.arr.capacity \* sizeof(JsonValue \*));  
    return v;  
}

void json\_array\_append(MemoryArena \*a, JsonValue \*arr, JsonValue \*item) {  
    assert(arr-\>type \== JSON\_ARRAY);  
    if (arr-\>as.arr.count \>= arr-\>as.arr.capacity) {  
        size\_t new\_cap \= arr-\>as.arr.capacity \* 2;  
        JsonValue \*\*new\_items \= (JsonValue \*\*)arena\_alloc(a, new\_cap \* sizeof(JsonValue \*));  
        memcpy(new\_items, arr-\>as.arr.items, arr-\>as.arr.count \* sizeof(JsonValue \*));  
        arr-\>as.arr.items \= new\_items;  
        arr-\>as.arr.capacity \= new\_cap;  
    }  
    arr-\>as.arr.items\[arr-\>as.arr.count++\] \= item;  
}

JsonValue \*json\_object(MemoryArena \*a, size\_t initial\_cap) {  
    JsonValue \*v \= (JsonValue \*)arena\_alloc(a, sizeof(JsonValue));  
    v-\>type \= JSON\_OBJECT;  
    v-\>as.obj.count \= 0;  
    v-\>as.obj.capacity \= initial\_cap ? initial\_cap : 4;  
    v-\>as.obj.pairs \= (JsonKeyValue \*)arena\_alloc(a, v-\>as.obj.capacity \* sizeof(JsonKeyValue));  
    return v;  
}

void json\_object\_set(MemoryArena \*a, JsonValue \*obj, const char \*key, JsonValue \*val) {  
    assert(obj-\>type \== JSON\_OBJECT);  
    if (obj-\>as.obj.count \>= obj-\>as.obj.capacity) {  
        size\_t new\_cap \= obj-\>as.obj.capacity \* 2;  
        JsonKeyValue \*new\_pairs \= (JsonKeyValue \*)arena\_alloc(a, new\_cap \* sizeof(JsonKeyValue));  
        memcpy(new\_pairs, obj-\>as.obj.pairs, obj-\>as.obj.count \* sizeof(JsonKeyValue));  
        obj-\>as.obj.pairs \= new\_pairs;  
        obj-\>as.obj.capacity \= new\_cap;  
    }  
    obj-\>as.obj.pairs\[obj-\>as.obj.count\].key \= arena\_strdup(a, key);  
    obj-\>as.obj.pairs\[obj-\>as.obj.count\].value \= val;  
    obj-\>as.obj.count++;  
}

/\* \========================================================================= \*/  
/\*                       3\. JSON TEXT STRINGIFIER                            \*/  
/\* \========================================================================= \*/

void json\_stringify(const JsonValue \*v, char \*buf, size\_t max\_len) {  
    if (\!v) {  
        snprintf(buf, max\_len, "null");  
        return;  
    }  
    switch (v-\>type) {  
        case JSON\_NULL: snprintf(buf, max\_len, "null"); break;  
        case JSON\_BOOL: snprintf(buf, max\_len, "%s", v-\>as.b\_val ? "true" : "false"); break;  
        case JSON\_INT:  snprintf(buf, max\_len, "%" PRId64, v-\>as.i\_val); break;  
        case JSON\_DOUBLE: snprintf(buf, max\_len, "%.4f", v-\>as.d\_val); break;  
        case JSON\_STRING: snprintf(buf, max\_len, "\\"%s\\"", v-\>as.s\_val); break;  
        case JSON\_ARRAY: {  
            size\_t off \= snprintf(buf, max\_len, "\[");  
            for (size\_t i \= 0; i \< v-\>as.arr.count; i++) {  
                if (off \< max\_len) {  
                    json\_stringify(v-\>as.arr.items\[i\], buf \+ off, max\_len \- off);  
                    off \= strlen(buf);  
                }  
                if (i \+ 1 \< v-\>as.arr.count && off \< max\_len) {  
                    off \+= snprintf(buf \+ off, max\_len \- off, ", ");  
                }  
            }  
            if (off \< max\_len) snprintf(buf \+ off, max\_len \- off, "\]");  
            break;  
        }  
        case JSON\_OBJECT: {  
            size\_t off \= snprintf(buf, max\_len, "{");  
            for (size\_t i \= 0; i \< v-\>as.obj.count; i++) {  
                if (off \< max\_len) {  
                    off \+= snprintf(buf \+ off, max\_len \- off, "\\"%s\\": ", v-\>as.obj.pairs\[i\].key);  
                }  
                if (off \< max\_len) {  
                    json\_stringify(v-\>as.obj.pairs\[i\].value, buf \+ off, max\_len \- off);  
                    off \= strlen(buf);  
                }  
                if (i \+ 1 \< v-\>as.obj.count && off \< max\_len) {  
                    off \+= snprintf(buf \+ off, max\_len \- off, ", ");  
                }  
            }  
            if (off \< max\_len) snprintf(buf \+ off, max\_len \- off, "}");  
            break;  
        }  
    }  
}

/\* \========================================================================= \*/  
/\*                 4\. COMPACT BINARY WIRE SERIALIZER                         \*/  
/\* \========================================================================= \*/

typedef struct {  
    uint8\_t \*data;  
    size\_t size;  
    size\_t capacity;  
} BinaryStream;

BinaryStream \*bin\_create(size\_t cap) {  
    BinaryStream \*s \= (BinaryStream \*)malloc(sizeof(BinaryStream));  
    s-\>data \= (uint8\_t \*)malloc(cap);  
    s-\>size \= 0;  
    s-\>capacity \= cap;  
    return s;  
}

void bin\_free(BinaryStream \*s) {  
    if (\!s) return;  
    free(s-\>data);  
    free(s);  
}

static void bin\_write(BinaryStream \*s, const void \*src, size\_t len) {  
    if (s-\>size \+ len \> s-\>capacity) {  
        s-\>capacity \= (s-\>capacity \* 2\) \+ len;  
        s-\>data \= (uint8\_t \*)realloc(s-\>data, s-\>capacity);  
    }  
    memcpy(s-\>data \+ s-\>size, src, len);  
    s-\>size \+= len;  
}

void json\_to\_binary(const JsonValue \*v, BinaryStream \*s) {  
    uint8\_t type\_tag \= (uint8\_t)v-\>type;  
    bin\_write(s, \&type\_tag, 1);

    switch (v-\>type) {  
        case JSON\_NULL: break;  
        case JSON\_BOOL: {  
            uint8\_t b \= v-\>as.b\_val ? 1 : 0;  
            bin\_write(s, \&b, 1);  
            break;  
        }  
        case JSON\_INT: {  
            bin\_write(s, \&v-\>as.i\_val, sizeof(int64\_t));  
            break;  
        }  
        case JSON\_DOUBLE: {  
            bin\_write(s, \&v-\>as.d\_val, sizeof(double));  
            break;  
        }  
        case JSON\_STRING: {  
            uint32\_t len \= (uint32\_t)strlen(v-\>as.s\_val);  
            bin\_write(s, \&len, sizeof(uint32\_t));  
            bin\_write(s, v-\>as.s\_val, len);  
            break;  
        }  
        case JSON\_ARRAY: {  
            uint32\_t count \= (uint32\_t)v-\>as.arr.count;  
            bin\_write(s, \&count, sizeof(uint32\_t));  
            for (size\_t i \= 0; i \< v-\>as.arr.count; i++) {  
                json\_to\_binary(v-\>as.arr.items\[i\], s);  
            }  
            break;  
        }  
        case JSON\_OBJECT: {  
            uint32\_t count \= (uint32\_t)v-\>as.obj.count;  
            bin\_write(s, \&count, sizeof(uint32\_t));  
            for (size\_t i \= 0; i \< v-\>as.obj.count; i++) {  
                uint32\_t klen \= (uint32\_t)strlen(v-\>as.obj.pairs\[i\].key);  
                bin\_write(s, \&klen, sizeof(uint32\_t));  
                bin\_write(s, v-\>as.obj.pairs\[i\].key, klen);  
                json\_to\_binary(v-\>as.obj.pairs\[i\].value, s);  
            }  
            break;  
        }  
    }  
}

/\* \========================================================================= \*/  
/\*                 5\. BINARY WIRE DESERIALIZER (ARENA-POWERED)               \*/  
/\* \========================================================================= \*/

JsonValue \*binary\_to\_json(MemoryArena \*a, const uint8\_t \*stream, size\_t total\_len, size\_t \*cursor) {  
    if (\*cursor \>= total\_len) return NULL;

    uint8\_t type\_tag \= stream\[(\*cursor)++\];  
    switch (type\_tag) {  
        case JSON\_NULL: return json\_null(a);  
        case JSON\_BOOL: {  
            if (\*cursor \>= total\_len) return NULL;  
            bool b \= stream\[(\*cursor)++\] \!= 0;  
            return json\_bool(a, b);  
        }  
        case JSON\_INT: {  
            if (\*cursor \+ sizeof(int64\_t) \> total\_len) return NULL;  
            int64\_t val;  
            memcpy(\&val, stream \+ \*cursor, sizeof(int64\_t));  
            \*cursor \+= sizeof(int64\_t);  
            return json\_int(a, val);  
        }  
        case JSON\_DOUBLE: {  
            if (\*cursor \+ sizeof(double) \> total\_len) return NULL;  
            double val;  
            memcpy(\&val, stream \+ \*cursor, sizeof(double));  
            \*cursor \+= sizeof(double);  
            return json\_double(a, val);  
        }  
        case JSON\_STRING: {  
            if (\*cursor \+ sizeof(uint32\_t) \> total\_len) return NULL;  
            uint32\_t slen;  
            memcpy(\&slen, stream \+ \*cursor, sizeof(uint32\_t));  
            \*cursor \+= sizeof(uint32\_t);  
            if (\*cursor \+ slen \> total\_len) return NULL;

            char \*s \= (char \*)arena\_alloc(a, slen \+ 1);  
            memcpy(s, stream \+ \*cursor, slen);  
            s\[slen\] \= '\\0';  
            \*cursor \+= slen;  
            return json\_string(a, s);  
        }  
        case JSON\_ARRAY: {  
            if (\*cursor \+ sizeof(uint32\_t) \> total\_len) return NULL;  
            uint32\_t count;  
            memcpy(\&count, stream \+ \*cursor, sizeof(uint32\_t));  
            \*cursor \+= sizeof(uint32\_t);

            JsonValue \*arr \= json\_array(a, count);  
            for (uint32\_t i \= 0; i \< count; i++) {  
                JsonValue \*child \= binary\_to\_json(a, stream, total\_len, cursor);  
                if (\!child) return NULL;  
                json\_array\_append(a, arr, child);  
            }  
            return arr;  
        }  
        case JSON\_OBJECT: {  
            if (\*cursor \+ sizeof(uint32\_t) \> total\_len) return NULL;  
            uint32\_t count;  
            memcpy(\&count, stream \+ \*cursor, sizeof(uint32\_t));  
            \*cursor \+= sizeof(uint32\_t);

            JsonValue \*obj \= json\_object(a, count);  
            for (uint32\_t i \= 0; i \< count; i++) {  
                if (\*cursor \+ sizeof(uint32\_t) \> total\_len) return NULL;  
                uint32\_t klen;  
                memcpy(\&klen, stream \+ \*cursor, sizeof(uint32\_t));  
                \*cursor \+= sizeof(uint32\_t);  
                if (\*cursor \+ klen \> total\_len) return NULL;

                char \*k \= (char \*)arena\_alloc(a, klen \+ 1);  
                memcpy(k, stream \+ \*cursor, klen);  
                k\[klen\] \= '\\0';  
                \*cursor \+= klen;

                JsonValue \*val \= binary\_to\_json(a, stream, total\_len, cursor);  
                if (\!val) return NULL;  
                json\_object\_set(a, obj, k, val);  
            }  
            return obj;  
        }  
        default:  
            return NULL;  
    }  
}

/\* \========================================================================= \*/  
/\*                               DRIVER MAIN                                 \*/  
/\* \========================================================================= \*/

int main(void) {  
    printf("====================================================================\\n");  
    printf("   WEEK 2 CAPSTONE: ARENA-BACKED BINARY & JSON SERIALIZATION ENGINE  \\n");  
    printf("====================================================================\\n\\n");

    // 1\. Initialize Arena (64 KB capacity)  
    MemoryArena \*arena \= arena\_create(64 \* 1024);

    // 2\. Construct Polymorphic AST Document  
    printf("\[1\] Constructing Document AST in Arena...\\n");  
    JsonValue \*root \= json\_object(arena, 8);  
    json\_object\_set(arena, root, "service", json\_string(arena, "telemetry\_gateway"));  
    json\_object\_set(arena, root, "port", json\_int(arena, 8080));  
    json\_object\_set(arena, root, "uptime\_hours", json\_double(arena, 142.75));  
    json\_object\_set(arena, root, "active", json\_bool(arena, true));

    JsonValue \*nodes \= json\_array(arena, 3);  
    json\_array\_append(arena, nodes, json\_string(arena, "worker-us-east-1"));  
    json\_array\_append(arena, nodes, json\_string(arena, "worker-eu-central-1"));  
    json\_array\_append(arena, nodes, json\_string(arena, "worker-ap-south-1"));  
    json\_object\_set(arena, root, "cluster\_nodes", nodes);

    printf("    Arena Memory Used for AST: %zu Bytes\\n\\n", arena-\>offset);

    // 3\. Stringify to JSON  
    printf("\[2\] Generating Human-Readable JSON Text:\\n");  
    char json\_text\[1024\];  
    json\_stringify(root, json\_text, sizeof(json\_text));  
    printf("    %s\\n    (Text Length: %zu Bytes)\\n\\n", json\_text, strlen(json\_text));

    // 4\. Pack into Binary Stream  
    printf("\[3\] Packing AST into Binary Wire Stream:\\n");  
    BinaryStream \*stream \= bin\_create(128);  
    json\_to\_binary(root, stream);  
    printf("    Binary Payload Size: %zu Bytes (%.1f%% of JSON Text Size\!)\\n",   
           stream-\>size, ((double)stream-\>size / (double)strlen(json\_text)) \* 100.0);

    // 5\. Unpack Binary Stream into a Second Arena  
    printf("\\n\[4\] Unpacking Binary Stream into New Scratch Arena...\\n");  
    MemoryArena \*scratch\_arena \= arena\_create(64 \* 1024);  
    size\_t cursor \= 0;  
    JsonValue \*restored\_root \= binary\_to\_json(scratch\_arena, stream-\>data, stream-\>size, \&cursor);  
    assert(restored\_root \!= NULL && cursor \== stream-\>size);

    char verified\_json\[1024\];  
    json\_stringify(restored\_root, verified\_json, sizeof(verified\_json));  
    printf("    Restored AST JSON:\\n    %s\\n", verified\_json);  
    assert(strcmp(json\_text, verified\_json) \== 0);  
    printf("    Verification: Restored document perfectly matches original AST\!\\n\\n");

    // 6\. Instant Zero-Leak Teardown  
    printf("\[5\] Reclaiming Memory:\\n");  
    bin\_free(stream);  
    arena\_destroy(scratch\_arena);  
    arena\_destroy(arena);  
    printf("    Both Arenas destroyed instantly with single free() calls (0 Fragmentation, 0 Leaks)\!\\n");

    printf("====================================================================\\n");  
    printf("  WEEK 2 MEGA PROJECT VERIFICATION COMPLETE: ALL CHECKS PASSED\!\\n");  
    printf("====================================================================\\n");  
    return 0;  
}  
\`\`\`  
