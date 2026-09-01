---
tags:
- c
- operators
- precedence
- sequence-points
- undefined-behavior
- order-of-evaluation
date: 2026-08-25
day: 3
---

# Day 3: Operators, Precedence, Sequence Points & Evaluation Order

---

## 1. Quick Reference & Cheat Sheet

### Critical Operator Precedence & Associativity Traps

| Precedence Level | Operators | Description | Associativity | Common Trap / Caveat |

| :--- | :--- | :--- | :--- | :--- |

| **1 (Highest)** | `()`, `[]`, `->`, `.`, `x++`, `x--` | Postfix expressions | Left-to-Right | `*p++` increments pointer `p`, returns old `*p`. |

| **2** | `++x`, `--x`, `*`, `&`, `!`, `~`, `sizeof`, `(type)` | Unary prefix | Right-to-Left | `*++p` increments `p` then dereferences; `++*p` increments value at `p`. |

| **3** | `*`, `/`, `%` | Multiplicative | Left-to-Right | Integer division truncates towards zero (`-5 / 2 == -2`). |

| **4** | `+`, `-` | Additive | Left-to-Right | `ptr + 1` scales by `sizeof(*ptr)` bytes. |

| **5** | `<<`, `>>` | Bitwise shifts | Left-to-Right | `1 << 2 + 1` evaluates as `1 << (2 + 1) == 8`, **NOT** `(1 << 2) + 1 == 5`! |

| **6** | `<`, `<=`, `>`, `>=` | Relational | Left-to-Right | `a < b < c` evaluates as `(a < b) < c` (comparing boolean 0/1 with `c`). |

| **7** | `==`, `!=` | Equality | Left-to-Right | `a & 1 == 0` evaluates as `a & (1 == 0)` because `==` > `&`! Always write `(a & 1) == 0`. |

| **8** | `&` | Bitwise AND | Left-to-Right | Lower precedence than equality and relational operators. |

| **9** | `\^` | Bitwise XOR | Left-to-Right | Lower precedence than `&`. |

| **10** | `|` | Bitwise OR | Left-to-Right | Lower precedence than `\^`. |

| **11** | `&&` | Logical AND | Left-to-Right | **Guaranteed short-circuit** evaluation order. |

| **12** | `||` | Logical OR | Left-to-Right | **Guaranteed short-circuit** evaluation order. |

| **13** | `?:` | Ternary conditional | Right-to-Left | `a ? b : c ? d : e` groups as `a ? b : (c ? d : e)`. |

| **14** | `=`, `+=`, `-=`, etc. | Compound Assignment | Right-to-Left | `a = b = c = 0` assigns from right to left. |

| **15 (Lowest)**| `,` | Comma operator | Left-to-Right | Evaluates left, discards result, evaluates and returns right. |

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Precedence vs Order of Evaluation (The Fundamental Distinction)

* **Precedence and Associativity:** Dictate how the compiler groups operands and operators into an Abstract Syntax Tree (AST).

* **Order of Evaluation:** Specifies the chronological sequence in which subexpressions, function calls, and side-effects are executed by the CPU.

```c
int result = f() + g() * h();
```

* **Grammar Grouping:** Due to precedence, `g() * h()` is grouped as the right operand of `+`.

* **Execution Order:** The C standard leaves the evaluation order of `f()`, `g()`, and `h()` **unspecified**. The compiler is completely free to call `f()` first, or `h()` first, or `g()` first depending on register allocation and CPU scheduling. If these functions modify shared global state, the program produces non-deterministic results.

---

### B. Sequence Points & The "Sequenced-Before" Relation (C11 §5.1.2.3)

A **Sequence Point** is a boundary in program execution where all side effects of previously evaluated expressions are guaranteed to be complete, and no side effects of subsequent evaluations have occurred.

#### Where Sequence Points Occur:

1. At the end of a full expression (marked by a semicolon `;` or controlling expression in `if`, `while`, `for`, `switch`, `return`).

2. After evaluating the left operand of `&&`, `||`, `? :`, and the comma operator `,`.

3. After evaluating all function arguments and the function designator, immediately before entering the function body.

#### The Golden Undefined Behavior Rule:

> Between two consecutive sequence points, if an object's value is modified more than once, or modified and also read for a purpose other than determining the new value, the behavior is **UNDEFINED BEHAVIOR (UB)**.

```c
// CLASSIC UNDEFINED BEHAVIOR EXAMPLES:
i = i++; // UB: 'i' modified twice without intervening sequence point
a[i] = i++; // UB: 'i' read to determine index and modified by ++ unsequenced
printf("%d %d\n", i++, i++); // UB: Argument evaluations are unsequenced
f(v = 1, v = 2); // UB: Unsequenced modifications
```

---

### C. Short-Circuit Evaluation Under the Hood

In logical expressions (`&&` and `||`), the C standard strictly guarantees left-to-right evaluation with a sequence point after the left operand:

* `expr1 && expr2`: If `expr1` evaluates to `0` (`false`), `expr2` is **guaranteed never to execute**.

* `expr1 || expr2`: If `expr1` evaluates to non-zero (`true`), `expr2` is **guaranteed never to execute**.

#### Assembly Translation Pattern:

Compilers emit conditional branch instructions (`je`, `jne`, `test`) rather than evaluating both subexpressions:

```c
if (ptr != NULL && *ptr == 42) { ... }
```

```nasm
cmp qword ptr [rbp - 8], 0 ; Check if ptr == NULL
je .L_skip ; Short-circuit: Jump immediately to skip if NULL
mov rax, qword ptr [rbp - 8]
cmp dword ptr [rax], 42 ; Safe to dereference ptr here
jne .L_skip
; Body code...
.L_skip:
```

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Arithmetic Expression Tokenizer & Shunting-Yard AST Evaluator (`expr_eval`)

#### Objective

Build a robust mathematical expression parser and evaluator in C that parses infix arithmetic expressions containing operators with varying precedence and associativity (`+`, `-`, `*`, `/`, `%`, `\^`, parentheses), converting them to Reverse Polish Notation (RPN) via Dijkstra's Shunting-Yard Algorithm before computing the result safely.

#### Functional Requirements

1. **Operator Specification:**

* `+`, `-`: Precedence 1, Left-Associative

* `*`, `/`, `%`: Precedence 2, Left-Associative

* `\^` (Exponentiation): Precedence 3, Right-Associative

* `(`, `)`: Parenthetical subexpression overrides

2. **Shunting-Yard Parser:**

Implement an RPN converter with an operator stack and output queue.

3. **RPN Evaluator:**

Evaluate RPN tokens using an operand stack. Include defensive checks:

* Division/Modulo by zero detection (`EXIT_FAILURE` with meaningful diagnostic).

* Stack underflow/overflow bounds checking.

* Mismatched parentheses detection.

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <assert.h>
#define MAX_TOKENS 128
#define STACK_CAPACITY 64
typedef enum {
TOKEN_NUMBER,
TOKEN_OP,
TOKEN_LPAREN,
TOKEN_RPAREN
} TokenType;
typedef struct {
TokenType type;
double value;
char op;
} Token;
int get_precedence(char op) {
switch (op) {
case '+': case '-': return 1;
case '*': case '/': case '%': return 2;
case '\^': return 3;
default: return 0;
}
}
bool is_right_associative(char op) {
return op == '\^';
}
// Shunting-Yard algorithm: Infix -> RPN
bool infix_to_rpn(const char *expr, Token *output, size_t *out_count) {
char op_stack[STACK_CAPACITY];
int op_top = -1;
size_t count = 0;
const char *p = expr;
while (*p != '\0') {
if (isspace((unsigned char)*p)) {
p++;
continue;
}
if (isdigit((unsigned char)*p) || *p == '.') {
char *end;
double val = strtod(p, &end);
output[count++] = (Token){ .type = TOKEN_NUMBER, .value = val };
p = end;
} else if (*p == '(') {
if (op_top >= STACK_CAPACITY - 1) return false;
op_stack[++op_top] = *p;
p++;
} else if (*p == ')') {
while (op_top >= 0 && op_stack[op_top] != '(') {
output[count++] = (Token){ .type = TOKEN_OP, .op = op_stack[op_top--] };
}
if (op_top < 0) return false; // Mismatched parentheses
op_top--; // Pop '('
p++;
} else if (strchr("+-*/%\^", *p)) {
char current_op = *p;
int prec = get_precedence(current_op);
bool right_assoc = is_right_associative(current_op);
while (op_top >= 0 && op_stack[op_top] != '(') {
int top_prec = get_precedence(op_stack[op_top]);
if ((!right_assoc && prec <= top_prec) || (right_assoc && prec < top_prec)) {
output[count++] = (Token){ .type = TOKEN_OP, .op = op_stack[op_top--] };
} else {
break;
}
}
if (op_top >= STACK_CAPACITY - 1) return false;
op_stack[++op_top] = current_op;
p++;
} else {
return false; // Invalid character
}
}
while (op_top >= 0) {
if (op_stack[op_top] == '(') return false; // Mismatched parentheses
output[count++] = (Token){ .type = TOKEN_OP, .op = op_stack[op_top--] };
}
*out_count = count;
return true;
}
// Evaluate RPN Tokens
bool evaluate_rpn(const Token *tokens, size_t count, double *out_result) {
double eval_stack[STACK_CAPACITY];
int eval_top = -1;
for (size_t i = 0; i < count; i++) {
if (tokens[i].type == TOKEN_NUMBER) {
if (eval_top >= STACK_CAPACITY - 1) return false;
eval_stack[++eval_top] = tokens[i].value;
} else if (tokens[i].type == TOKEN_OP) {
if (eval_top < 1) return false; // Underflow
double b = eval_stack[eval_top--];
double a = eval_stack[eval_top--];
double res = 0.0;
switch (tokens[i].op) {
case '+': res = a + b; break;
case '-': res = a - b; break;
case '*': res = a * b; break;
case '/':
if (fabs(b) < 1e-9) {
fprintf(stderr, "Evaluation Error: Division by zero!\n");
return false;
}
res = a / b;
break;
case '%':
if ((long)b == 0) return false;
res = (double)((long)a % (long)b);
break;
case '\^': res = pow(a, b); break;
default: return false;
}
eval_stack[++eval_top] = res;
}
}
if (eval_top != 0) return false;
*out_result = eval_stack[0];
return true;
}
int main(void) {
const char *expressions[] = {
"3 + 4 * 2", // Expect 11 (precedence test)
"2 \^ 3 \^ 2", // Expect 512 (right-associativity: 2\^(3\^2) = 2\^9)
"(3 + 4) * 2 / (1 - 5) \^ 2", // Expect 0.875
"100 & 1 == 0" // Not valid arithmetic, demonstrating C precedence trap in comments
};
for (size_t i = 0; i < 3; i++) {
Token rpn[MAX_TOKENS];
size_t count = 0;
double result = 0.0;
if (infix_to_rpn(expressions[i], rpn, &count) && evaluate_rpn(rpn, count, &result)) {
printf("Expression: %-30s => Result: %.4f\n", expressions[i], result);
} else {
printf("Failed to evaluate: %s\n", expressions[i]);
}
}
return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Unsequenced State Machine & Macro Side-Effect Bug

Examine the following faulty telemetry logging function from an embedded data logger:

```c
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#define MAX_ENTRIES 16
#define SQUARE(x) ((x) * (x))
static uint32_t sensor_log[MAX_ENTRIES];
static size_t log_head = 0;
// BUGGY IMPLEMENTATION
void log_sensor_data(uint32_t raw_reading, int multiplier) {
// BUG 1: Double expansion of side effects in macro!
// If passed 'raw_reading++', 'raw_reading' is incremented TWICE.
uint32_t energy = SQUARE(raw_reading++);
// BUG 2: Unsequenced modification and read of 'log_head'!
// Modifying 'log_head' via post-increment while reading it in array indexing -> UB!
sensor_log[log_head++] = energy + (log_head * multiplier);
}
```

### Analysis of Vulnerabilities:

1. **Unsafe Macro Argument Reuse:** `#define SQUARE(x) ((x) * (x))` evaluates the expression `x` twice. When called with `raw_reading++`, `raw_reading` is post-incremented twice, leading to incorrect calculations and subtle off-by-one errors.

2. **Unsequenced Access & Modification in Array Assignment:** `sensor_log[log_head++] = energy + (log_head * multiplier);` attempts to modify `log_head` with `++` while simultaneously reading `log_head` in the right-hand subexpression without an intervening sequence point. This is **Undefined Behavior**.

### Defensive Fix:

```c
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#define MAX_ENTRIES 16U
static uint32_t sensor_log[MAX_ENTRIES];
static size_t log_head = 0;
// Fix 1: Use an inline static function instead of a function-like macro to prevent double evaluation
static inline uint32_t square_u32(uint32_t val) {
return val * val;
}
bool log_sensor_data_safe(uint32_t raw_reading, int32_t multiplier) {
// Fix 2: Bounds checking on circular or bounded buffer
if (log_head >= MAX_ENTRIES) {
fprintf(stderr, "Defensive Error: Sensor log buffer capacity exceeded!\n");
return false;
}
// Fix 3: Isolate side effects into distinct, strictly sequenced statements
uint32_t energy = square_u32(raw_reading);
// Read state before mutating index
size_t current_index = log_head;
uint32_t log_entry = energy + (uint32_t)((int64_t)current_index * multiplier);
sensor_log[current_index] = log_entry;
// Explicit mutation on a separate line
log_head++;
return true;
}
```
