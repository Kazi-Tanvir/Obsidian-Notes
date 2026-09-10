---
tags:
  - c
  - week-2-synthesis
  - mega-project
  - dynamic-memory
  - structs-alignment
  - serialization
  - arena-allocator
  - json-parser
date: 2026-09-06
day: 15
---

# Day 15: Week 2 Synthesis & Mega Project — Custom Binary & JSON Serialization Engine with Arena Memory

---

## 1. Quick Reference & Cheat Sheet (Week 2 Synthesis)

### Dynamic Memory Management Invariants
* **`malloc(size)`:** Allocates uninitialized memory. Always check for `NULL`.
* **`calloc(n, size)`:** Allocates zero-initialized memory. Protects against integer overflow during multiplication.
* **`realloc(ptr, new_size)`:** Resizes existing block. Never assign directly back to `ptr` (`ptr \= realloc(ptr, ...)` leaks memory on failure).
* **Pointer Poisoning:** Always set pointers to `NULL` immediately after `free()` to prevent Use-After-Free (UAF) and Double-Free bugs.

### Structs, Alignment & Padding Rules
* **Natural Alignment:** Primitive types require memory addresses divisible by their size (`int` at multiple of 4, `double`/pointers at multiple of 8).
* **Internal Padding:** Injected between members to align subsequent fields.
* **Tail Padding:** Injected at the struct tail so that elements in an array (`struct T arr[N]`) preserve the largest member's alignment.
* **Optimization Rule:** Declare struct members in **descending order of size** (8-byte $\\to$ 4-byte $\\to$ 2-byte $\\to$ 1-byte) to eliminate internal padding holes.
* **Packed Structs (`__attribute__((packed))`):** Eliminates padding for network wire formats, but taking the address of unaligned members violates strict alignment and triggers bus errors (`SIGBUS`) on non-x86 architectures.

### Unions, Type Punning & Copying
* **Union Storage:** All members share base offset `0`. Size is determined by the largest member rounded to largest alignment.
* **Strict Aliasing Rule:** Reinterpreting memory via pointer casts (`*(int*)\&my_float`) causes undefined behavior under `-O2`/`-O3`. Use union punning or `memcpy`.
* **Tagged Unions:** Always bundle an explicit discriminator `enum` with a union to verify the active variant before access.
* **Shallow Copy:** Bitwise copy (`*dest \= *src`) duplicates pointer addresses, creating shared aliasing that causes double-free crashes.
* **Deep Copy:** Recursively duplicates every pointer target into fresh heap allocations.

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Binary vs Textual (JSON) Serialization
| Attribute | JSON / Textual Serialization | Packed Binary Wire Format |
| :--- | :--- | :--- |
| **Human Readability** | High (plain ASCII/UTF-8 text) | None (raw byte stream) |
| **Parsing Overhead** | High (string scans, float conversions, whitespace parsing) | Minimal (direct byte slicing and integer deserialization) |
| **Payload Size** | Bulky (e.g. integer `12345678` takes 8 ASCII bytes) | Compact (`uint32_t` takes exactly 4 raw bytes) |
| **Type Integrity** | Requires string-to-number lexical parsing | Fixed type tags / schemas embedded in stream |

---

### B. Arena Allocators in Serialization Engines
Tree structures (like JSON ASTs or nested configuration dictionaries) involve dozens or hundreds of tiny dynamic allocations (keys, strings, child nodes). Calling `malloc()` for every token causes:
1. **High Overhead:** Each 8-byte chunk incurs 8–16 bytes of heap metadata headers.
2. **Memory Fragmentation:** Freeing nodes individually leaves holes across the heap.
3. **Complex Error Cleanup:** If parsing fails mid-stream, unwinding and freeing partially allocated trees requires tedious recursive rollback code.

```text
Traditional malloc() Tree:                   Arena-Allocated Tree:
 Heap:                                        Arena Contiguous Buffer (e.g. 64 KB):
 ┌────────┐   ┌────────┐   ┌────────┐        ┌─────────┬─────────┬─────────┬──────────────┐
 │ Node A │   │ Node B │   │ Node C │        │ Node A  │ Node B  │ Node C  │ Free Scratch │
 └────────┘   └────────┘   └────────┘        └─────────┴─────────┴─────────┴──────────────┘
 Scattered across RAM with metadata           ▲
                                              └── Bump pointer advances sequentially.
                                                  Deallocation is a single O(1) reset\!
```

---

### C. TLV (Type-Length-Value) Binary Encoding
A robust binary protocol formats every value into a **TLV tuple**:
* **Type (1 byte):** Discriminator identifying the data type (e.g., `0x01` \= Null, `0x02` \= Int64, `0x03` \= Double, `0x04` \= String, `0x05` \= Array, `0x06` \= Object).
* **Length (4 bytes):** Unsigned integer specifying the byte length of the payload.
* **Value (Variable):** Raw payload bytes (e.g. Little-Endian integer or raw UTF-8 characters).

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Compact Binary TLV Stream Packer & Validator (`tlv_stream`)

#### Objective
Build a binary serializer and deserializer that encodes primitive variables (`int32_t`, `double`, length-prefixed strings) into a contiguous TLV byte buffer and unpacks them with strict bounds-checking.

#### Complete Starter Code Implementation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#define TLV_INT32  0x01
#define TLV_DOUBLE 0x02
#define TLV_STRING 0x03

typedef struct {
    uint8_t *data;
    size_t capacity;
    size_t size;
} ByteBuffer;

ByteBuffer *bytebuf_create(size_t initial_cap) {
    ByteBuffer *b \= (ByteBuffer *)malloc(sizeof(ByteBuffer));
    b->data \= (uint8_t *)malloc(initial_cap);
    b->capacity \= initial_cap;
    b->size \= 0;
    return b;
}

void bytebuf_free(ByteBuffer *b) {
    if (\!b) return;
    free(b->data);
    free(b);
}

static bool bytebuf_ensure(ByteBuffer *b, size_t extra) {
    if (b->size \+ extra > b->capacity) {
        size_t new_cap \= (b->capacity * 2\) \+ extra;
        uint8_t *new_data \= (uint8_t *)realloc(b->data, new_cap);
        if (\!new_data) return false;
        b->data \= new_data;
        b->capacity \= new_cap;
    }
    return true;
}

bool tlv_pack_int32(ByteBuffer *b, int32_t val) {
    if (\!bytebuf_ensure(b, 1 \+ 4 \+ 4)) return false;
    b->data[b->size++] \= TLV_INT32;
    uint32_t len \= 4;
    memcpy(b->data \+ b->size, \&len, 4);
    b->size \+= 4;
    memcpy(b->data \+ b->size, \&val, 4);
    b->size \+= 4;
    return true;
}

bool tlv_pack_double(ByteBuffer *b, double val) {
    if (\!bytebuf_ensure(b, 1 \+ 4 \+ 8)) return false;
    b->data[b->size++] \= TLV_DOUBLE;
    uint32_t len \= 8;
    memcpy(b->data \+ b->size, \&len, 4);
    b->size \+= 4;
    memcpy(b->data \+ b->size, \&val, 8);
    b->size \+= 8;
    return true;
}

bool tlv_pack_string(ByteBuffer *b, const char *str) {
    size_t s_len \= strlen(str);
    if (\!bytebuf_ensure(b, 1 \+ 4 \+ s_len)) return false;
    b->data[b->size++] \= TLV_STRING;
    uint32_t len \= (uint32_t)s_len;
    memcpy(b->data \+ b->size, \&len, 4);
    b->size \+= 4;
    memcpy(b->data \+ b->size, str, s_len);
    b->size \+= s_len;
    return true;
}

void tlv_unpack_and_print(const uint8_t *buf, size_t total_len) {
    printf("--- Unpacking TLV Stream (%zu Bytes) \---\\n", total_len);
    size_t cursor \= 0;
    while (cursor < total_len) {
        if (cursor \+ 5 > total_len) {
            fprintf(stderr, "Error: Truncated header\!\\n");
            return;
        }
        uint8_t type \= buf[cursor++];
        uint32_t len \= 0;
        memcpy(\&len, buf \+ cursor, 4);
        cursor \+= 4;

        if (cursor \+ len > total_len) {
            fprintf(stderr, "Error: Payload exceeds buffer boundary\!\\n");
            return;
        }

        switch (type) {
            case TLV_INT32: {
                int32_t v;
                memcpy(\&v, buf \+ cursor, 4);
                printf("  [TAG: INT32]  Length: %u | Value: %d\\n", len, v);
                break;
            }
            case TLV_DOUBLE: {
                double v;
                memcpy(\&v, buf \+ cursor, 8);
                printf("  [TAG: DOUBLE] Length: %u | Value: %f\\n", len, v);
                break;
            }
            case TLV_STRING: {
                printf("  [TAG: STRING] Length: %u | Value: \\"%.*s\\"\\n", len, (int)len, buf \+ cursor);
                break;
            }
            default:
                printf("  [TAG: UNKNOWN (0x%02X)] Length: %u\\n", type, len);
                break;
        }
        cursor \+= len;
    }
    printf("--- Stream Parsing Successfully Complete \---\\n\\n");
}

int main(void) {
    ByteBuffer *b \= bytebuf_create(32);
    tlv_pack_int32(b, 42);
    tlv_pack_double(b, 3.1415926535);
    tlv_pack_string(b, "Hello TLV Protocol\!");

    tlv_unpack_and_print(b->data, b->size);
    bytebuf_free(b);
    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Untrusted Payload Length & Integer Wrap-Around Deserialization Bug
Examine the following faulty binary deserializer:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

// BUGGY IMPLEMENTATION
char *extract_string_faulty(const uint8_t *packet, size_t packet_len, size_t *cursor) {
    // Read 32-bit length directly from untrusted network byte stream
    uint32_t str_len;
    memcpy(\&str_len, packet \+ *cursor, 4);
    *cursor \+= 4;

    // BUG 1: Integer overflow on addition\! If str_len \== UINT32_MAX, str_len \+ 1 wraps to 0.
    // malloc(0) allocates minimal chunk; subsequent memcpy causes Massive Heap Overflow.
    char *str \= (char *)malloc(str_len \+ 1);

    // BUG 2: Unbounded memory read\! If *cursor \+ str_len > packet_len,
    // memcpy reads out-of-bounds process memory into string buffer (Heartbleed style).
    memcpy(str, packet \+ *cursor, str_len);
    str[str_len] \= '\\0';
    *cursor \+= str_len;

    return str;
}
```

### Analysis of Vulnerabilities:
1. **Integer Wrap-Around:** If `str_len \= 0xFFFFFFFF`, `str_len \+ 1` wraps to `0`. Allocator returns a tiny block. `memcpy` then copies 4 GB of data, crashing the process or enabling arbitrary code execution.
2. **Out-of-Bounds Buffer Over-Read:** The length field is trusted without verifying that `packet_len \- *cursor >= str_len`.

### Defensive Fix:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SAFE_STRING_LEN (1024 * 1024\) // Cap strings to 1 MB

bool extract_string_safe(const uint8_t *packet, size_t packet_len, size_t *cursor, char **out_str) {
    if (\!packet || \!cursor || \!out_str) return false;

    // Defensive Check 1: Ensure length field itself is within packet
    if (*cursor > packet_len || packet_len \- *cursor < sizeof(uint32_t)) {
        fprintf(stderr, "Defensive Error: Truncated packet, cannot read length prefix\!\\n");
        return false;
    }

    uint32_t str_len;
    memcpy(\&str_len, packet \+ *cursor, sizeof(uint32_t));

    // Defensive Check 2: Cap length to maximum realistic threshold to prevent DoS
    if (str_len > MAX_SAFE_STRING_LEN) {
        fprintf(stderr, "Defensive Error: String length (%u) exceeds maximum safe size\!\\n", str_len);
        return false;
    }

    // Defensive Check 3: Check remaining bytes using safe subtraction
    size_t offset_after_len \= *cursor \+ sizeof(uint32_t);
    if (str_len > packet_len \- offset_after_len) {
        fprintf(stderr, "Defensive Error: Payload length (%u) exceeds packet boundary (%zu remaining)\!\\n",
                str_len, packet_len \- offset_after_len);
        return false;
    }

    // Allocate with checked size
    char *str \= (char *)malloc((size_t)str_len \+ 1);
    if (\!str) return false;

    memcpy(str, packet \+ offset_after_len, str_len);
    str[str_len] \= '\\0'; // Guarantee null-termination

    *cursor \= offset_after_len \+ str_len;
    *out_str \= str;
    return true;
}
```

---

## 5. WEEKLY MEGA PROJECT (Week 2 Capstone)

### Project Title: Dual Binary & JSON Serialization Engine with Arena Memory Pool (`arena_serializer`)

#### Architectural Overview
Build an end-to-end Serialization Engine that models a polymorphic JSON/Document Value AST, provides zero-leak memory management via a **Custom Memory Arena**, and serializes/deserializes between human-readable JSON text and compact binary wire formats.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        MemoryArena (Bump Allocator)                    │
│   Allocates all AST Nodes, String Literals, Array & Object Buckets     │
├────────────────────────────────────────────────────────────────────────┤
│                       JsonValue AST (Tagged Union)                     │
│  \- JSON_NULL                                                           │
│  \- JSON_BOOL   (bool)                                                  │
│  \- JSON_INT    (int64_t)                                               │
│  \- JSON_DOUBLE (double)                                                │
│  \- JSON_STRING (char*)                                                 │
│  \- JSON_ARRAY  (JsonValue**, count, capacity)                          │
│  \- JSON_OBJECT (JsonKeyValue*, count, capacity)                        │
├────────────────────────────────────────────────────────────────────────┤
│ Engines:                                                               │
│  1. JSON Text Stringifier: json_stringify(val, out_buf)                │
│  2. Binary Wire Serializer: json_to_binary(val, out_bytebuf)            │
│  3. Binary Wire Unpacker: binary_to_json(arena, bytebuf)               │
└────────────────────────────────────────────────────────────────────────┘
```

#### Complete Modular Implementation (`arena_serializer.c`)
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <inttypes.h>
#include <assert.h>

/* \========================================================================= */
/*                          1. CUSTOM MEMORY ARENA                           */
/* \========================================================================= */

typedef struct {
    uint8_t *buffer;
    size_t capacity;
    size_t offset;
} MemoryArena;

MemoryArena *arena_create(size_t capacity) {
    MemoryArena *a \= (MemoryArena *)malloc(sizeof(MemoryArena));
    a->buffer \= (uint8_t *)malloc(capacity);
    a->capacity \= capacity;
    a->offset \= 0;
    return a;
}

void arena_destroy(MemoryArena *a) {
    if (\!a) return;
    free(a->buffer);
    free(a);
}

void *arena_alloc(MemoryArena *a, size_t size) {
    // 8-byte natural alignment
    size_t aligned_size \= (size \+ 7\) & \~7ULL;
    if (a->offset \+ aligned_size > a->capacity) {
        fprintf(stderr, "Arena OOM: Exceeded %zu bytes\!\\n", a->capacity);
        return NULL;
    }
    void *ptr \= a->buffer \+ a->offset;
    a->offset \+= aligned_size;
    memset(ptr, 0, aligned_size);
    return ptr;
}

char *arena_strdup(MemoryArena *a, const char *s) {
    if (\!s) return NULL;
    size_t len \= strlen(s);
    char *copy \= (char *)arena_alloc(a, len \+ 1);
    memcpy(copy, s, len);
    copy[len] \= '\\0';
    return copy;
}

/* \========================================================================= */
/*                          2. JSON AST DATA MODEL                           */
/* \========================================================================= */

typedef enum {
    JSON_NULL \= 0x00,
    JSON_BOOL \= 0x01,
    JSON_INT  \= 0x02,
    JSON_DOUBLE \= 0x03,
    JSON_STRING \= 0x04,
    JSON_ARRAY  \= 0x05,
    JSON_OBJECT \= 0x06
} JsonType;

typedef struct JsonValue JsonValue;
typedef struct JsonKeyValue JsonKeyValue;

struct JsonKeyValue {
    const char *key;
    JsonValue  *value;
};

struct JsonValue {
    JsonType type;
    union {
        bool b_val;
        int64_t i_val;
        double d_val;
        const char *s_val;
        struct {
            JsonValue **items;
            size_t count;
            size_t capacity;
        } arr;
        struct {
            JsonKeyValue *pairs;
            size_t count;
            size_t capacity;
        } obj;
    } as;
};

// Node Constructors using Arena Memory
JsonValue *json_null(MemoryArena *a) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_NULL;
    return v;
}

JsonValue *json_bool(MemoryArena *a, bool b) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_BOOL;
    v->as.b_val \= b;
    return v;
}

JsonValue *json_int(MemoryArena *a, int64_t i) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_INT;
    v->as.i_val \= i;
    return v;
}

JsonValue *json_double(MemoryArena *a, double d) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_DOUBLE;
    v->as.d_val \= d;
    return v;
}

JsonValue *json_string(MemoryArena *a, const char *s) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_STRING;
    v->as.s_val \= arena_strdup(a, s);
    return v;
}

JsonValue *json_array(MemoryArena *a, size_t initial_cap) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_ARRAY;
    v->as.arr.count \= 0;
    v->as.arr.capacity \= initial_cap ? initial_cap : 4;
    v->as.arr.items \= (JsonValue **)arena_alloc(a, v->as.arr.capacity * sizeof(JsonValue *));
    return v;
}

void json_array_append(MemoryArena *a, JsonValue *arr, JsonValue *item) {
    assert(arr->type \== JSON_ARRAY);
    if (arr->as.arr.count >= arr->as.arr.capacity) {
        size_t new_cap \= arr->as.arr.capacity * 2;
        JsonValue **new_items \= (JsonValue **)arena_alloc(a, new_cap * sizeof(JsonValue *));
        memcpy(new_items, arr->as.arr.items, arr->as.arr.count * sizeof(JsonValue *));
        arr->as.arr.items \= new_items;
        arr->as.arr.capacity \= new_cap;
    }
    arr->as.arr.items[arr->as.arr.count++] \= item;
}

JsonValue *json_object(MemoryArena *a, size_t initial_cap) {
    JsonValue *v \= (JsonValue *)arena_alloc(a, sizeof(JsonValue));
    v->type \= JSON_OBJECT;
    v->as.obj.count \= 0;
    v->as.obj.capacity \= initial_cap ? initial_cap : 4;
    v->as.obj.pairs \= (JsonKeyValue *)arena_alloc(a, v->as.obj.capacity * sizeof(JsonKeyValue));
    return v;
}

void json_object_set(MemoryArena *a, JsonValue *obj, const char *key, JsonValue *val) {
    assert(obj->type \== JSON_OBJECT);
    if (obj->as.obj.count >= obj->as.obj.capacity) {
        size_t new_cap \= obj->as.obj.capacity * 2;
        JsonKeyValue *new_pairs \= (JsonKeyValue *)arena_alloc(a, new_cap * sizeof(JsonKeyValue));
        memcpy(new_pairs, obj->as.obj.pairs, obj->as.obj.count * sizeof(JsonKeyValue));
        obj->as.obj.pairs \= new_pairs;
        obj->as.obj.capacity \= new_cap;
    }
    obj->as.obj.pairs[obj->as.obj.count].key \= arena_strdup(a, key);
    obj->as.obj.pairs[obj->as.obj.count].value \= val;
    obj->as.obj.count++;
}

/* \========================================================================= */
/*                       3. JSON TEXT STRINGIFIER                            */
/* \========================================================================= */

void json_stringify(const JsonValue *v, char *buf, size_t max_len) {
    if (\!v) {
        snprintf(buf, max_len, "null");
        return;
    }
    switch (v->type) {
        case JSON_NULL: snprintf(buf, max_len, "null"); break;
        case JSON_BOOL: snprintf(buf, max_len, "%s", v->as.b_val ? "true" : "false"); break;
        case JSON_INT:  snprintf(buf, max_len, "%" PRId64, v->as.i_val); break;
        case JSON_DOUBLE: snprintf(buf, max_len, "%.4f", v->as.d_val); break;
        case JSON_STRING: snprintf(buf, max_len, "\\"%s\\"", v->as.s_val); break;
        case JSON_ARRAY: {
            size_t off \= snprintf(buf, max_len, "[");
            for (size_t i \= 0; i < v->as.arr.count; i++) {
                if (off < max_len) {
                    json_stringify(v->as.arr.items[i], buf \+ off, max_len \- off);
                    off \= strlen(buf);
                }
                if (i \+ 1 < v->as.arr.count && off < max_len) {
                    off \+= snprintf(buf \+ off, max_len \- off, ", ");
                }
            }
            if (off < max_len) snprintf(buf \+ off, max_len \- off, "]");
            break;
        }
        case JSON_OBJECT: {
            size_t off \= snprintf(buf, max_len, "{");
            for (size_t i \= 0; i < v->as.obj.count; i++) {
                if (off < max_len) {
                    off \+= snprintf(buf \+ off, max_len \- off, "\\"%s\\": ", v->as.obj.pairs[i].key);
                }
                if (off < max_len) {
                    json_stringify(v->as.obj.pairs[i].value, buf \+ off, max_len \- off);
                    off \= strlen(buf);
                }
                if (i \+ 1 < v->as.obj.count && off < max_len) {
                    off \+= snprintf(buf \+ off, max_len \- off, ", ");
                }
            }
            if (off < max_len) snprintf(buf \+ off, max_len \- off, "}");
            break;
        }
    }
}

/* \========================================================================= */
/*                 4. COMPACT BINARY WIRE SERIALIZER                         */
/* \========================================================================= */

typedef struct {
    uint8_t *data;
    size_t size;
    size_t capacity;
} BinaryStream;

BinaryStream *bin_create(size_t cap) {
    BinaryStream *s \= (BinaryStream *)malloc(sizeof(BinaryStream));
    s->data \= (uint8_t *)malloc(cap);
    s->size \= 0;
    s->capacity \= cap;
    return s;
}

void bin_free(BinaryStream *s) {
    if (\!s) return;
    free(s->data);
    free(s);
}

static void bin_write(BinaryStream *s, const void *src, size_t len) {
    if (s->size \+ len > s->capacity) {
        s->capacity \= (s->capacity * 2\) \+ len;
        s->data \= (uint8_t *)realloc(s->data, s->capacity);
    }
    memcpy(s->data \+ s->size, src, len);
    s->size \+= len;
}

void json_to_binary(const JsonValue *v, BinaryStream *s) {
    uint8_t type_tag \= (uint8_t)v->type;
    bin_write(s, \&type_tag, 1);

    switch (v->type) {
        case JSON_NULL: break;
        case JSON_BOOL: {
            uint8_t b \= v->as.b_val ? 1 : 0;
            bin_write(s, \&b, 1);
            break;
        }
        case JSON_INT: {
            bin_write(s, \&v->as.i_val, sizeof(int64_t));
            break;
        }
        case JSON_DOUBLE: {
            bin_write(s, \&v->as.d_val, sizeof(double));
            break;
        }
        case JSON_STRING: {
            uint32_t len \= (uint32_t)strlen(v->as.s_val);
            bin_write(s, \&len, sizeof(uint32_t));
            bin_write(s, v->as.s_val, len);
            break;
        }
        case JSON_ARRAY: {
            uint32_t count \= (uint32_t)v->as.arr.count;
            bin_write(s, \&count, sizeof(uint32_t));
            for (size_t i \= 0; i < v->as.arr.count; i++) {
                json_to_binary(v->as.arr.items[i], s);
            }
            break;
        }
        case JSON_OBJECT: {
            uint32_t count \= (uint32_t)v->as.obj.count;
            bin_write(s, \&count, sizeof(uint32_t));
            for (size_t i \= 0; i < v->as.obj.count; i++) {
                uint32_t klen \= (uint32_t)strlen(v->as.obj.pairs[i].key);
                bin_write(s, \&klen, sizeof(uint32_t));
                bin_write(s, v->as.obj.pairs[i].key, klen);
                json_to_binary(v->as.obj.pairs[i].value, s);
            }
            break;
        }
    }
}

/* \========================================================================= */
/*                 5. BINARY WIRE DESERIALIZER (ARENA-POWERED)               */
/* \========================================================================= */

JsonValue *binary_to_json(MemoryArena *a, const uint8_t *stream, size_t total_len, size_t *cursor) {
    if (*cursor >= total_len) return NULL;

    uint8_t type_tag \= stream[(*cursor)++];
    switch (type_tag) {
        case JSON_NULL: return json_null(a);
        case JSON_BOOL: {
            if (*cursor >= total_len) return NULL;
            bool b \= stream[(*cursor)++] \!= 0;
            return json_bool(a, b);
        }
        case JSON_INT: {
            if (*cursor \+ sizeof(int64_t) > total_len) return NULL;
            int64_t val;
            memcpy(\&val, stream \+ *cursor, sizeof(int64_t));
            *cursor \+= sizeof(int64_t);
            return json_int(a, val);
        }
        case JSON_DOUBLE: {
            if (*cursor \+ sizeof(double) > total_len) return NULL;
            double val;
            memcpy(\&val, stream \+ *cursor, sizeof(double));
            *cursor \+= sizeof(double);
            return json_double(a, val);
        }
        case JSON_STRING: {
            if (*cursor \+ sizeof(uint32_t) > total_len) return NULL;
            uint32_t slen;
            memcpy(\&slen, stream \+ *cursor, sizeof(uint32_t));
            *cursor \+= sizeof(uint32_t);
            if (*cursor \+ slen > total_len) return NULL;

            char *s \= (char *)arena_alloc(a, slen \+ 1);
            memcpy(s, stream \+ *cursor, slen);
            s[slen] \= '\\0';
            *cursor \+= slen;
            return json_string(a, s);
        }
        case JSON_ARRAY: {
            if (*cursor \+ sizeof(uint32_t) > total_len) return NULL;
            uint32_t count;
            memcpy(\&count, stream \+ *cursor, sizeof(uint32_t));
            *cursor \+= sizeof(uint32_t);

            JsonValue *arr \= json_array(a, count);
            for (uint32_t i \= 0; i < count; i++) {
                JsonValue *child \= binary_to_json(a, stream, total_len, cursor);
                if (\!child) return NULL;
                json_array_append(a, arr, child);
            }
            return arr;
        }
        case JSON_OBJECT: {
            if (*cursor \+ sizeof(uint32_t) > total_len) return NULL;
            uint32_t count;
            memcpy(\&count, stream \+ *cursor, sizeof(uint32_t));
            *cursor \+= sizeof(uint32_t);

            JsonValue *obj \= json_object(a, count);
            for (uint32_t i \= 0; i < count; i++) {
                if (*cursor \+ sizeof(uint32_t) > total_len) return NULL;
                uint32_t klen;
                memcpy(\&klen, stream \+ *cursor, sizeof(uint32_t));
                *cursor \+= sizeof(uint32_t);
                if (*cursor \+ klen > total_len) return NULL;

                char *k \= (char *)arena_alloc(a, klen \+ 1);
                memcpy(k, stream \+ *cursor, klen);
                k[klen] \= '\\0';
                *cursor \+= klen;

                JsonValue *val \= binary_to_json(a, stream, total_len, cursor);
                if (\!val) return NULL;
                json_object_set(a, obj, k, val);
            }
            return obj;
        }
        default:
            return NULL;
    }
}

/* \========================================================================= */
/*                               DRIVER MAIN                                 */
/* \========================================================================= */

int main(void) {
    printf("====================================================================\\n");
    printf("   WEEK 2 CAPSTONE: ARENA-BACKED BINARY & JSON SERIALIZATION ENGINE  \\n");
    printf("====================================================================\\n\\n");

    // 1. Initialize Arena (64 KB capacity)
    MemoryArena *arena \= arena_create(64 * 1024);

    // 2. Construct Polymorphic AST Document
    printf("[1] Constructing Document AST in Arena...\\n");
    JsonValue *root \= json_object(arena, 8);
    json_object_set(arena, root, "service", json_string(arena, "telemetry_gateway"));
    json_object_set(arena, root, "port", json_int(arena, 8080));
    json_object_set(arena, root, "uptime_hours", json_double(arena, 142.75));
    json_object_set(arena, root, "active", json_bool(arena, true));

    JsonValue *nodes \= json_array(arena, 3);
    json_array_append(arena, nodes, json_string(arena, "worker-us-east-1"));
    json_array_append(arena, nodes, json_string(arena, "worker-eu-central-1"));
    json_array_append(arena, nodes, json_string(arena, "worker-ap-south-1"));
    json_object_set(arena, root, "cluster_nodes", nodes);

    printf("    Arena Memory Used for AST: %zu Bytes\\n\\n", arena->offset);

    // 3. Stringify to JSON
    printf("[2] Generating Human-Readable JSON Text:\\n");
    char json_text[1024];
    json_stringify(root, json_text, sizeof(json_text));
    printf("    %s\\n    (Text Length: %zu Bytes)\\n\\n", json_text, strlen(json_text));

    // 4. Pack into Binary Stream
    printf("[3] Packing AST into Binary Wire Stream:\\n");
    BinaryStream *stream \= bin_create(128);
    json_to_binary(root, stream);
    printf("    Binary Payload Size: %zu Bytes (%.1f%% of JSON Text Size\!)\\n",
           stream->size, ((double)stream->size / (double)strlen(json_text)) * 100.0);

    // 5. Unpack Binary Stream into a Second Arena
    printf("\\n[4] Unpacking Binary Stream into New Scratch Arena...\\n");
    MemoryArena *scratch_arena \= arena_create(64 * 1024);
    size_t cursor \= 0;
    JsonValue *restored_root \= binary_to_json(scratch_arena, stream->data, stream->size, \&cursor);
    assert(restored_root \!= NULL && cursor \== stream->size);

    char verified_json[1024];
    json_stringify(restored_root, verified_json, sizeof(verified_json));
    printf("    Restored AST JSON:\\n    %s\\n", verified_json);
    assert(strcmp(json_text, verified_json) \== 0);
    printf("    Verification: Restored document perfectly matches original AST\!\\n\\n");

    // 6. Instant Zero-Leak Teardown
    printf("[5] Reclaiming Memory:\\n");
    bin_free(stream);
    arena_destroy(scratch_arena);
    arena_destroy(arena);
    printf("    Both Arenas destroyed instantly with single free() calls (0 Fragmentation, 0 Leaks)\!\\n");

    printf("====================================================================\\n");
    printf("  WEEK 2 MEGA PROJECT VERIFICATION COMPLETE: ALL CHECKS PASSED\!\\n");
    printf("====================================================================\\n");
    return 0;
}
```
