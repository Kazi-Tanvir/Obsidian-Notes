---
tags:
- c
- strings
- buffer-overflow
- string-safety
- dynamic-strings
- defensive-programming
date: 2026-09-01
day: 10
---

# Day 10: Safe String Manipulation, Custom String Engines & Buffer Overflow Prevention

---

## 1. Quick Reference & Cheat Sheet

### C-String Fundamentals & Standard Library Pitfalls

A standard C-string is a contiguous sequence of `char` values terminated by a null character (`'\0'`, ASCII 0).

| Function | Safety Status | Main Pitfall / Behavioral Quirk | Safe Modern Alternative |

| :--- | :--- | :--- | :--- |

| `gets()` | **FATAL (Removed in C11)** | No buffer boundary limit; always overflows. | `fgets()` |

| `strcpy()` | **UNSAFE** | No destination bounds check; overflows if source is larger. | `snprintf()` or explicit bounds copy |

| `strncpy()` | **DECEPTIVELY UNSAFE** | **Does NOT null-terminate** if source length $\ge n$; zero-pads remaining bytes if source $< n$. | `snprintf(dest, sizeof(dest), "%s", src)` |

| `strcat()` | **UNSAFE** | Scans for `\0` every call ($O(N)$ time); no destination capacity check. | `snprintf()` or custom dynamic string builder |

| `strncat()` | **PARTIALLY SAFE** | Third parameter is *max remaining characters to append*, NOT total buffer size. | `snprintf()` or length-tracked builder |

| `sprintf()` | **UNSAFE** | Unbounded formatted write into destination buffer. | `snprintf()` |

| `snprintf()` | **SAFE** | Always null-terminates if buffer size $> 0$; returns total characters that *would have been written*. | `snprintf()` with truncation check |

### The `snprintf` Idiom for Truncation Detection

```c
char buffer[32];
int written = snprintf(buffer, sizeof(buffer), "User: %s (ID: %d)", username, user_id);
// Robust Truncation & Encoding Error Check:
if (written < 0) {
// Encoding / output error
} else if ((size_t)written >= sizeof(buffer)) {
// Output was truncated! Only 'sizeof(buffer) - 1' characters were written.
} else {
// String was written completely and safely null-terminated.
}
```

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Memory Placement: String Literals vs Character Arrays

```c
// 1. Pointer to String Literal:
const char *str_lit = "Hello World";
// Resides in .rodata (Read-Only Data Segment).
// Attempting to write: str_lit[0] = 'h'; triggers a hardware Segmentation Fault (SIGSEGV).
// 2. Character Array (Stack Buffer):
char str_stack[] = "Hello World";
// Copies the 12 bytes ("Hello World\0") from .rodata into the function's stack frame.
// Modifiable: str_stack[0] = 'h'; is perfectly legal.
```

### B. The `strncpy` Fallacy

Many developers mistakenly believe `strncpy(dest, src, n)` is a safe version of `strcpy`.

In reality, `strncpy` was designed in early Unix for fixed-width 14-byte directory entries (`struct direct`), not null-terminated C-strings.

```c
char buf[4];
strncpy(buf, "abcd", 4);
// Memory in buf: ['a', 'b', 'c', 'd'] <-- NO NULL TERMINATOR!
printf("%s\n", buf); // Reads past buffer into stack memory until a random 0x00 is found -> UB!
```

### C. Length-Prefixed Strings (SDS / Fat String Architecture)

To eliminate $O(N)$ `strlen` scanning, buffer overflows, and binary-incompatibility (handling strings containing null bytes `\0`), high-performance systems like Redis use length-prefixed strings:

```text
Memory Layout of a Length-Prefixed Safe String:
┌───────────────────────────┬────────────────────────────────────────────┬──────┐
│ Header: struct StringHdr │ User String Data Buffer │ '\0' │
│ - size_t len │ (Binary payload or characters) │ Null │
│ - size_t capacity │ │ Term │
└───────────────────────────┴────────────────────────────────────────────┴──────┘
▲
└── Pointer exposed to user (compatible with standard printf!)
```

* **$O(1)$ Length:** `hdr->len` accessed instantly via negative pointer offset: `((StringHdr*)ptr - 1)->len`.

* **Binary Safe:** Can store arbitrary byte arrays, images, and network frames containing internal `0x00` bytes.

* **C Compatible:** Maintains an automatic trailing `\0` so it can be passed directly to standard C APIs (`printf`, `fopen`, etc.).

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: High-Performance Memory-Safe Dynamic String Engine (`safestr`)

#### Objective

Build a lightweight, binary-safe dynamic string library in C that stores length and capacity headers before the data buffer, automatically resizes exponentially, guarantees null-termination, and prevents buffer overflows.

#### Functional Requirements

1. `safestr_create(const char *init)`: Allocates string header + payload with initial content.

2. `safestr_free(char *s)`: Frees the entire string chunk using header offset.

3. `safestr_len(const char *s)`: Returns length in $O(1)$ time.

4. `safestr_cat(char **s, const char *append_str)`: Appends text, automatically growing capacity via `realloc` if needed.

5. `safestr_cat_buf(char **s, const void *buf, size_t len)`: Binary-safe buffer append.

6. `safestr_substr(const char *s, size_t start, size_t len)`: Creates a new safe substring.

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
typedef struct {
size_t len; // Active string length (excluding null-terminator)
size_t capacity; // Total allocated payload capacity (excluding header & null-terminator)
} SafeStrHeader;
#define SAFESTR_HDR(s) ((SafeStrHeader *)((char *)(s) - sizeof(SafeStrHeader)))
// Create a new SafeStr
char *safestr_create(const char *init) {
size_t init_len = init ? strlen(init) : 0;
size_t initial_cap = init_len < 16 ? 16 : init_len * 2;
size_t total_alloc = sizeof(SafeStrHeader) + initial_cap + 1; // +1 for trailing '\0'
SafeStrHeader *hdr = (SafeStrHeader *)malloc(total_alloc);
if (!hdr) return NULL;
hdr->len = init_len;
hdr->capacity = initial_cap;
char *data = (char *)hdr + sizeof(SafeStrHeader);
if (init && init_len > 0) {
memcpy(data, init, init_len);
}
data[init_len] = '\0'; // Always guarantee null-termination
return data;
}
// Free SafeStr
void safestr_free(char *s) {
if (!s) return;
SafeStrHeader *hdr = SAFESTR_HDR(s);
free(hdr);
}
// O(1) Length Retrieval
static inline size_t safestr_len(const char *s) {
if (!s) return 0;
return SAFESTR_HDR(s)->len;
}
// O(1) Capacity Retrieval
static inline size_t safestr_capacity(const char *s) {
if (!s) return 0;
return SAFESTR_HDR(s)->capacity;
}
// Ensure capacity for upcoming operations (Exponential Growth)
static bool safestr_grow(char **s_ptr, size_t additional_len) {
char *s = *s_ptr;
SafeStrHeader *hdr = SAFESTR_HDR(s);
size_t required_capacity = hdr->len + additional_len;
if (required_capacity <= hdr->capacity) {
return true; // Space already available
}
size_t new_capacity = hdr->capacity * 2;
if (new_capacity < required_capacity) {
new_capacity = required_capacity + 16;
}
size_t total_alloc = sizeof(SafeStrHeader) + new_capacity + 1;
SafeStrHeader *new_hdr = (SafeStrHeader *)realloc(hdr, total_alloc);
if (!new_hdr) {
return false;
}
new_hdr->capacity = new_capacity;
*s_ptr = (char *)new_hdr + sizeof(SafeStrHeader);
return true;
}
// Append C-string to SafeStr
bool safestr_cat(char **s_ptr, const char *append_str) {
if (!s_ptr || !*s_ptr || !append_str) return false;
size_t append_len = strlen(append_str);
if (!safestr_grow(s_ptr, append_len)) {
return false;
}
char *s = *s_ptr;
SafeStrHeader *hdr = SAFESTR_HDR(s);
memcpy(s + hdr->len, append_str, append_len);
hdr->len += append_len;
s[hdr->len] = '\0'; // Guarantee null-terminator
return true;
}
// Binary-Safe Append
bool safestr_cat_buf(char **s_ptr, const void *buf, size_t len) {
if (!s_ptr || !*s_ptr || !buf || len == 0) return false;
if (!safestr_grow(s_ptr, len)) {
return false;
}
char *s = *s_ptr;
SafeStrHeader *hdr = SAFESTR_HDR(s);
memcpy(s + hdr->len, buf, len);
hdr->len += len;
s[hdr->len] = '\0';
return true;
}
int main(void) {
printf("=== Testing SafeStr Dynamic String Engine ===\n");
char *msg = safestr_create("Engine: Initialized");
printf("[1] Created: "%s" (Length: %zu, Capacity: %zu)\n",
msg, safestr_len(msg), safestr_capacity(msg));
safestr_cat(&msg, " | Status: RUNNING");
safestr_cat(&msg, " | Worker Threads: 8");
printf("[2] Appended: "%s"\n (Length: %zu, Capacity: %zu)\n",
msg, safestr_len(msg), safestr_capacity(msg));
// Test binary data append with internal null bytes
uint8_t raw_bytes[] = { 0x41, 0x00, 0x42, 0x00, 0x43 }; // 'A', '\0', 'B', '\0', 'C'
safestr_cat_buf(&msg, raw_bytes, sizeof(raw_bytes));
printf("[3] Binary-Safe Append: Total Length is now %zu bytes.\n", safestr_len(msg));
safestr_free(msg);
printf("Memory cleanly released!\n");
return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Path Concatenator & Off-by-One Buffer Overflow

Examine the following faulty filesystem path generation function:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// BUGGY IMPLEMENTATION
char *build_file_path_faulty(const char *dir, const char *filename) {
// BUG 1: Off-by-one allocation error (Forgot +1 for '/' separator, only added +1 for '\0')
size_t total_len = strlen(dir) + strlen(filename) + 1;
char *path = (char *)malloc(total_len);
if (!path) return NULL;
// BUG 2: Unsafe strcpy / strcat without capacity tracking
strcpy(path, dir);
strcat(path, "/");
strcat(path, filename); // WRITES BEYOND ALLOCATED BOUNDS -> Heap Corruption!
return path;
}
```

### Analysis of Vulnerabilities:

1. **Off-by-One Heap Overflow:** `strlen(dir) + strlen(filename) + 1` only accounts for the characters and the null terminator. The path delimiter `'/'` adds an extra byte. Writing the final null terminator writes outside the allocated block.

2. **Missing Trailing Slash Normalization:** If `dir` already ends with `'/'` (e.g. `"/var/log/"`), the code naively produces `"/var/log//filename"`.

3. **No Parameter Validation:** Calling with `dir = NULL` or `filename = NULL` triggers immediate segmentation faults in `strlen()`.

### Defensive Fix:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
char *build_file_path_safe(const char *dir, const char *filename) {
if (!dir || !filename) return NULL;
size_t dir_len = strlen(dir);
size_t file_len = strlen(filename);
// Defensive Check: Determine if separator '/' is needed
bool needs_slash = (dir_len > 0 && dir[dir_len - 1] != '/');
size_t sep_len = needs_slash ? 1 : 0;
// Allocate exact capacity: dir + separator + filename + '\0'
size_t total_size = dir_len + sep_len + file_len + 1;
char *path = (char *)malloc(total_size);
if (!path) return NULL;
// Safe construction via snprintf
int written = snprintf(path, total_size, "%s%s%s", dir, needs_slash ? "/" : "", filename);
if (written < 0 || (size_t)written >= total_size) {
free(path);
return NULL;
}
return path;
}
```
