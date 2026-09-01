---
tags:
- c
- control-flow
- storage-classes
- linkage
- jump-tables
date: 2026-08-26
day: 4
---

# Day 4: Control Flow Mechanics, Jump Tables, Scope, Storage Duration & Linkage

---

## 1. Quick Reference & Cheat Sheet

### Scope, Storage Duration & Linkage Matrix

| Keyword / Placement | Storage Duration | Scope | Linkage | Lifetime | Memory Section |

| :--- | :--- | :--- | :--- | :--- | :--- |

| `auto int x;` (inside block) | Automatic | Block | None | Function execution | Stack |

| `register int x;` (inside block) | Automatic | Block | None | Function execution | CPU Register / Stack |

| `static int x;` (inside block) | Static | Block | None | Entire program execution | `.data` or `.bss` |

| `static int x;` (file scope) | Static | File | **Internal** (only this `.c` translation unit) | Entire program execution | `.data` or `.bss` |

| `int x;` (file scope) | Static | File | **External** (visible across all `.o` files) | Entire program execution | `.data` or `.bss` |

| `extern int x;` (declaration) | Static | File / Block | **External** (defined elsewhere) | Entire program execution | Resolved by Linker |

### Control Flow Under the Hood

* **`if-else` Ladders:** Emits sequential comparison and conditional branch instructions (`cmp`, `je`, `jne`, `jle`). Complexity: $O(N)$ comparisons.

* **`switch` Statements:**

* **Sparse Cases:** Compiles to a binary search comparison tree ($O(\log N)$).

* **Dense Cases:** Compiles to an indirect **Jump Table** in `.rodata` ($O(1)$ dispatch via array indexing).

* **Fallthrough Trapping:** C allows case fallthrough by default. In modern C (C23), use `[[fallthrough]];` to document intended fallthrough and prevent compiler warnings.

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Jump Tables in `switch` Compilation

When a `switch` statement has dense integer cases, modern compilers avoid sequential comparisons entirely by generating an array of code label addresses in the `.rodata` (read-only data) section.

```c
switch (opcode) {
case 0: handle_add(); break;
case 1: handle_sub(); break;
case 2: handle_mul(); break;
case 3: handle_div(); break;
default: handle_err(); break;
}
```

#### Assembly Representation (x86_64):

```nasm
cmp edi, 3 ; Check upper bound
ja .L_default ; If opcode > 3, jump to default handler
mov rax, QWORD PTR .L_JUMP_TABLE[0 + rdi*8] ; O(1) table lookup
jmp rax ; Indirect jump to code label
.section .rodata
.L_JUMP_TABLE:
.quad .L_case_0
.quad .L_case_1
.quad .L_case_2
.quad .L_case_3
```

---

### B. Unconventional Control Flow: Duff's Device

Devised by Tom Duff in 1983, **Duff's Device** combines loop unrolling with an interlaced `switch-case` construct to minimize loop branching overhead during bulk memory copies without requiring a separate epilogue loop for remainder iterations.

```c
void duff_copy(char *to, const char *from, size_t count) {
if (count == 0) return;
size_t n = (count + 7) / 8; // Number of 8-byte iterations
switch (count % 8) {
case 0: do { *to++ = *from++;
case 7: *to++ = *from++;
case 6: *to++ = *from++;
case 5: *to++ = *from++;
case 4: *to++ = *from++;
case 3: *to++ = *from++;
case 2: *to++ = *from++;
case 1: *to++ = *from++;
} while (--n > 0);
}
}
```

*Note: While modern compilers optimize `memcpy` into SIMD vector instructions, Duff's Device illustrates the flexibility of C's syntactic grammar where `case` labels can nest inside arbitrary block statements.*

---

### C. The `goto` Error Cleanup Idiom (Simulating RAII in C)

While unrestricted `goto` creates spaghetti code, forward-jumping `goto` to an ordered cleanup block at the end of a function is the industry-standard error-handling pattern in the Linux kernel and high-reliability systems.

```c
int initialize_subsystem(void) {
int status = -1;
void *res_a = allocate_resource_a();
if (!res_a) goto cleanup_none;
void *res_b = allocate_resource_b();
if (!res_b) goto cleanup_a;
void *res_c = allocate_resource_c();
if (!res_c) goto cleanup_b;
// Core logic...
status = 0; // Success
cleanup_b:
free_resource_b(res_b);
cleanup_a:
free_resource_a(res_a);
cleanup_none:
return status;
}
```

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Finite State Machine (FSM) Tokenizer & Config Parser (`fsm_config`)

#### Objective

Build a robust, table-driven Finite State Machine in C that parses INI/Key-Value configuration streams containing comments, quoted strings with escape sequences, integer values, and error states.

#### State Transition Diagram

```text
[STATE_START] ──── (Whitespace) ───────────► [STATE_START]
[STATE_START] ──── ('#', ';') ─────────────► [STATE_COMMENT]
[STATE_START] ──── (Alpha / '_') ──────────► [STATE_KEY]
[STATE_KEY] ──── ('=') ──────────────────► [STATE_ASSIGN]
[STATE_ASSIGN]─── ('"') ──────────────────► [STATE_QUOTED_VAL]
[STATE_ASSIGN]─── (Digit / '-') ───────────► [STATE_NUMERIC_VAL]
[STATE_QUOTED_VAL] ── ('"') ───────────────► [STATE_EMIT]
[STATE_NUMERIC_VAL] ── (Whitespace / '\n') ─► [STATE_EMIT]
[Any State] ──── (Unexpected Char) ──────► [STATE_ERROR]
```

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>
#define MAX_TOKEN_LEN 128
typedef enum {
STATE_START,
STATE_KEY,
STATE_ASSIGN,
STATE_VAL_UNQUOTED,
STATE_VAL_QUOTED,
STATE_COMMENT,
STATE_ERROR
} FsmState;
typedef struct {
char key[MAX_TOKEN_LEN];
char value[MAX_TOKEN_LEN];
bool is_valid;
} ConfigPair;
bool parse_config_line(const char *line, ConfigPair *out_pair) {
if (line == NULL || out_pair == NULL) return false;
FsmState state = STATE_START;
size_t k_idx = 0;
size_t v_idx = 0;
out_pair->key[0] = '\0';
out_pair->value[0] = '\0';
out_pair->is_valid = false;
const char *p = line;
while (*p != '\0' && *p != '\n') {
char c = *p;
switch (state) {
case STATE_START:
if (isspace((unsigned char)c)) {
// Skip leading whitespace
} else if (c == '#' || c == ';') {
state = STATE_COMMENT;
} else if (isalpha((unsigned char)c) || c == '_') {
if (k_idx < MAX_TOKEN_LEN - 1) out_pair->key[k_idx++] = c;
state = STATE_KEY;
} else {
state = STATE_ERROR;
}
break;
case STATE_KEY:
if (isalnum((unsigned char)c) || c == '_') {
if (k_idx < MAX_TOKEN_LEN - 1) out_pair->key[k_idx++] = c;
} else if (c == '=') {
out_pair->key[k_idx] = '\0';
state = STATE_ASSIGN;
} else if (isspace((unsigned char)c)) {
// Key ended, waiting for '='
out_pair->key[k_idx] = '\0';
} else {
state = STATE_ERROR;
}
break;
case STATE_ASSIGN:
if (isspace((unsigned char)c)) {
// Skip whitespace between '=' and value
} else if (c == '"') {
state = STATE_VAL_QUOTED;
} else if (c == '#' || c == ';') {
state = STATE_ERROR; // Missing value before comment
} else {
if (v_idx < MAX_TOKEN_LEN - 1) out_pair->value[v_idx++] = c;
state = STATE_VAL_UNQUOTED;
}
break;
case STATE_VAL_UNQUOTED:
if (isspace((unsigned char)c) || c == '#' || c == ';') {
out_pair->value[v_idx] = '\0';
out_pair->is_valid = true;
return true;
} else {
if (v_idx < MAX_TOKEN_LEN - 1) out_pair->value[v_idx++] = c;
}
break;
case STATE_VAL_QUOTED:
if (c == '"') {
out_pair->value[v_idx] = '\0';
out_pair->is_valid = true;
return true;
} else if (c == '' && *(p + 1) != '\0') {
// Escape sequence handler
p++;
if (v_idx < MAX_TOKEN_LEN - 1) out_pair->value[v_idx++] = *p;
} else {
if (v_idx < MAX_TOKEN_LEN - 1) out_pair->value[v_idx++] = c;
}
break;
case STATE_COMMENT:
// Ignore rest of line
return false;
case STATE_ERROR:
default:
return false;
}
p++;
}
if (state == STATE_VAL_UNQUOTED && v_idx > 0) {
out_pair->value[v_idx] = '\0';
out_pair->is_valid = true;
return true;
}
return false;
}
int main(void) {
const char *test_lines[] = {
"# Server Configuration File",
"port = 8080",
"hostname = "app.local.dev"",
"enable_tls = 1 ; enable HTTPS",
"invalid line without delimiter"
};
printf("=== FSM Configuration Parser Output ===\n");
for (size_t i = 0; i < 5; i++) {
ConfigPair pair;
bool ok = parse_config_line(test_lines[i], &pair);
if (ok && pair.is_valid) {
printf("[Parsed] KEY: %-15s => VALUE: %s\n", pair.key, pair.value);
} else {
printf("[Ignored/Error] Line: %s\n", test_lines[i]);
}
}
return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Dangling Stack Pointer & Static Reentrancy Bug

Examine the following faulty utility functions:

```c
#include <stdio.h>
#include <string.h>
// BUG 1: Returning address of local variable with automatic storage duration!
char *get_formatted_timestamp(int epoch_sec) {
char buffer[64];
snprintf(buffer, sizeof(buffer), "TIMESTAMP: %d", epoch_sec);
return buffer; // Stack frame destroyed on return -> Dangling Pointer!
}
// BUG 2: Non-reentrant static buffer in shared/multi-call context
const char *format_ip_address(int a, int b, int c, int d) {
static char ip_str[32]; // Shared across all calls
snprintf(ip_str, sizeof(ip_str), "%d.%d.%d.%d", a, b, c, d);
return ip_str;
}
void test_ip_comparison(void) {
// Problem: Both calls return the same pointer pointing to the same static memory!
const char *ip1 = format_ip_address(192, 168, 1, 1);
const char *ip2 = format_ip_address(10, 0, 0, 1);
// ip1 was overwritten by the second call to format_ip_address!
printf("IP1: %s | IP2: %s\n", ip1, ip2); // Prints: IP1: 10.0.0.1 | IP2: 10.0.0.1
}
```

### Analysis of Vulnerabilities:

1. **Dangling Stack Reference:** Automatic local variables cease to exist once the function's stack frame unwinds. Returning `buffer` returns an invalid pointer; subsequent memory accesses cause undefined behavior or security exploits.

2. **Reentrancy and Concurrency Failure with `static`:** Using a static buffer inside a function means that subsequent invocations overwrite data currently being used by prior callers.

### Defensive Fix:

```c
#include <stdio.h>
#include <stdbool.h>
// Fix 1: Caller-allocated buffer idiom (Standard in POSIX / C standard library)
bool get_formatted_timestamp_safe(int epoch_sec, char *out_buf, size_t buf_size) {
if (out_buf == NULL || buf_size == 0) {
return false;
}
int written = snprintf(out_buf, buf_size, "TIMESTAMP: %d", epoch_sec);
return (written >= 0 && (size_t)written < buf_size);
}
// Fix 2: Explicit caller memory contract for IP formatting
bool format_ip_address_safe(int a, int b, int c, int d, char *out_ip, size_t max_len) {
if (out_ip == NULL || max_len < 16) {
return false;
}
if (a < 0 || a > 255 || b < 0 || b > 255 || c < 0 || c > 255 || d < 0 || d > 255) {
return false;
}
int written = snprintf(out_ip, max_len, "%d.%d.%d.%d", a, b, c, d);
return (written >= 0 && (size_t)written < max_len);
}
```
