---
tags:
  - c
  - error-handling
  - errno
  - setjmp-longjmp
  - return-codes
  - thread-local
date: 2026-09-16
day: 25
---

# Day 25: Robust Error Handling Architectures, errno & Non-Local Jumps

---

## 1. Quick Reference & Cheat Sheet

### Error Handling Paradigms in C

----------------------------------------------------------------------------- Pattern                 Implementation    Pros              Cons / Traps ----------------------- ----------------- ----------------- ----------------- **Status Enum +         Status res =      Explicit error    Verbose; requires Out-Pointer**           parse(src, &out); paths; forces     dual parameters caller handling

**Sentinel Values**     Returns NULL, -1, Simple, idiomatic In-band or EOF            in POSIX          signaling; error details lost

**Tagged Union          struct { bool ok; Type-safe; zero   Mild memory (Result)**              union { T val;    out-pointer       overhead of union Err err; }; }     boilerplate       size

**Global/Thread-Local   Sets thread-local Standard C        Must manually errno**                 integer flag      library standard  zero before call; easy to overwrite

**Non-Local Jumps       if (setjmp(buf)   Unwinds deeply    Leaks resources; (setjmp)**              == 0) \... else   nested call       registers lose \...              chains fast       state unless volatile -----------------------------------------------------------------------------

### The Rules of errno (<errno.h>)

- **Thread-Safety:** In modern POSIX systems, errno is **not** a shared global variable. It is a macro expanding to a function call returning a thread-local pointer:#define errno (*__errno_location())

- **Rule 1 (Zeroing):** Library functions **never** reset errno to 0 on success. You must set errno = 0; *before* the operation if checking errors (e.g. with strtol).

- **Rule 2 (Immediate Preservation):** If an error occurs and you call another function (even printf or free), that sub-call may overwrite errno. Always cache it:int saved_errno = errno;

> fprintf(stderr, "Failed: %s\\n", strerror(saved_errno));

- **Thread-Safe String Conversion:** Never use strerror() in multi-threaded code (returns a static buffer). Use strerror_r() (POSIX) or strerror_s() (C11).

### setjmp & longjmp Non-Local Jumps (<setjmp.h>)

##include <setjmp.h>

jmp_buf g_env;

void deeply_nested_func(void) {

// Abort and jump back to setjmp site, returning value 42

longjmp(g_env, 42);

}

int main(void) {

volatile int counter = 0; // MUST BE volatile to survive longjmp!

int val = setjmp(g_env);

if (val == 0) {

// Direct invocation (First time here)

counter = 10;

deeply_nested_func();

} else {

// Returned via longjmp! val == 42

printf("Recovered from error code %d. Counter = %d\\n", val, counter);

}

return 0;

}

## 2. In-Depth Theory & Low-Level Mechanics

### A. The Mechanics of errno & Thread-Local Storage (TLS)

In single-threaded C (K&R, C89), errno was declared as extern int errno;. When POSIX threads (pthreads) arrived, this created severe race conditions: Thread A's failed read() would be overwritten by Thread B's successful read() before Thread A could inspect it.

Modern C libraries solve this using **Thread-Local Storage (TLS)**:

- Each thread OS control block reserves an offset in the Thread Information Block (TIB / FS register on x86-64).

- The macro #define errno (*__errno_location()) accesses %fs:offset.

- In modern C11, this can be natively expressed via the _Thread_local storage duration specifier:_Thread_local int my_thread_errno = 0;

### B. Under the Hood of setjmp and longjmp

A standard function return pops the current stack frame by restoring %rsp and jumping to the saved return address %rip on the stack. But what if an unrecoverable failure occurs 15 function calls deep?

setjmp and longjmp provide an escape hatch across arbitrary stack frames:

1.  **setjmp(jmp_buf env) Execution:**

    - Reads CPU registers and stores them directly into the jmp_buf structure (typically an array of long or dedicated machine registers).

    - **Saved registers include:**

      - Stack Pointer (%rsp on x86-64)

      - Frame Pointer / Base Pointer (%rbp)

      - Instruction Pointer (%rip / Program Counter)

      - Callee-saved registers (%rbx, %r12--%r15)

    - Returns 0 to the caller.

2.  **longjmp(jmp_buf env, int val) Execution:**

    - Restores the CPU registers saved in env.

    - Sets %rsp directly back to the snapshot stack pointer.

    - If val == 0, it forces the return value to 1 (because 0 is reserved for the initial direct call).

    - Overwrites the CPU's register state and jumps execution to the address stored in %rip.

    - To the instruction pipeline, it appears as though setjmp() just returned a second time, this time evaluating to val!

Call Stack:

main() [setjmp saved: RSP_0, RBP_0, RIP_0]

│

└──► parse_request()

│

└──► decode_token()

│

└──► longjmp(env, ERR_CORRUPT)

│

│ [CPU Registers Overwritten: RSP=RSP_0, RBP=RBP_0, RIP=RIP_0]

▼

Jumps directly back to main(), unwinding parse_request and decode_token instantly!

### C. The volatile Variable Trap with setjmp

The ISO C standard contains a critical rule that catches even experienced systems engineers:**ISO C Standard Warning:** All local automatic variables in the function containing setjmp whose values change after setjmp has been called must be qualified as volatile; otherwise, their values after longjmp are **undefined**.

#### Why does this happen at assembly level?

- When optimizing with -O2 or -O3, the compiler allocates local variables into CPU registers (e.g. %ebx, %r12) rather than reading/writing to memory on the stack.

- If a variable is stored in a register that gets overwritten by intervening function calls, its modified value is never committed to stack RAM.

- When longjmp restores the old register state captured at the initial setjmp call, the variable's value silently rolls back to whatever it was before the modification!

- Declaring the variable volatile instructs the compiler: **"Never cache this value across instructions in a register; always write it through to the physical stack frame."**

### D. The Kernel "Goto Cleanup" Pattern (C's Idiomatic RAII)

Because C lacks C++ destructors or Java finally blocks, functions allocating multiple resources (locks, heap memory, file descriptors, sockets) suffer from the "Arrow Anti-Pattern" of nested if statements.

The idiomatic industry standard (championed by the Linux kernel) is the **Single-Exit Reverse Cleanup (goto cleanup)**:int process_transaction(const char *path) {

int status = -1;

FILE *fp = NULL;

char *buffer = NULL;

void *lock = NULL;

fp = fopen(path, "rb");

if (!fp) goto cleanup_file;

buffer = (char *)malloc(4096);

if (!buffer) goto cleanup_buf;

lock = acquire_mutex();

if (!lock) goto cleanup_lock;

// Perform actual work\...

status = 0; // Success!

cleanup_lock:

if (lock) release_mutex(lock);

cleanup_buf:

free(buffer);

cleanup_file:

if (fp) fclose(fp);

return status;

}

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Lightweight Exception & Try-Catch-Finally Framework for C (cexcept)

#### Objective

Build a nested, thread-safe exception handling system in pure C using preprocessor macros, setjmp/longjmp, and a linked-list execution context stack that supports TRY, CATCH, FINALLY, and THROW.

#### Architecture Overview

- **Exception Frame:** A linked-list node on the stack storing a jmp_buf, error code, error message string, and pointer to the outer enclosing frame.

- **Thread-Local Head Pointer:** A _Thread_local pointer tracking the innermost active TRY block.

- **Clean Unwinding:** Re-throwing unhandled exceptions up the chain to higher-level handlers, or terminating gracefully if uncaught.

#### Complete Implementation (cexcept.c)

##include <stdio.h>

##include <stdlib.h>

##include <stdint.h>

##include <stdbool.h>

##include <string.h>

##include <setjmp.h>

##include <threads.h>

/* ========================================================================= */

/* EXCEPTION CORE ENGINE TYPES */

/* ========================================================================= */

typedef enum {

EX_NONE = 0,

EX_OUT_OF_MEMORY,

EX_IO_FAILURE,

EX_PARSING_ERROR,

EX_DIVIDE_BY_ZERO

} ExceptionCode;

typedef struct ExceptionFrame {

jmp_buf env;

struct ExceptionFrame *prev;

ExceptionCode exception_code;

const char *error_message;

const char *file;

int line;

bool caught;

} ExceptionFrame;

// Thread-local stack head for exception nesting

static _Thread_local ExceptionFrame *t_current_exception_frame = NULL;

static inline const char *exception_code_str(ExceptionCode code) {

switch (code) {

case EX_NONE: return "EX_NONE";

case EX_OUT_OF_MEMORY: return "EX_OUT_OF_MEMORY";

case EX_IO_FAILURE: return "EX_IO_FAILURE";

case EX_PARSING_ERROR: return "EX_PARSING_ERROR";

case EX_DIVIDE_BY_ZERO: return "EX_DIVIDE_BY_ZERO";

default: return "EX_UNKNOWN";

}

}

/* ========================================================================= */

/* MACRO-BASED SYNTAX CONSTRUCTS */

/* ========================================================================= */

##define TRY 

do {

ExceptionFrame __ex_frame;

__ex_frame.exception_code = EX_NONE;

__ex_frame.error_message = NULL;

__ex_frame.caught = false;

__ex_frame.prev = t_current_exception_frame;

t_current_exception_frame = &__ex_frame;

int __ex_sig = setjmp(__ex_frame.env);

if (__ex_sig == 0) {

##define CATCH(code_var, msg_var) 

} else {

__ex_frame.caught = true;

ExceptionCode code_var = __ex_frame.exception_code;

const char *msg_var = __ex_frame.error_message;

##define FINALLY 

} {

t_current_exception_frame = __ex_frame.prev;

##define END_TRY 

}

if (!__ex_frame.caught && __ex_frame.exception_code != EX_NONE) {

/* Re-throw uncaught exception up to next outer handler */

cexcept_throw(__ex_frame.exception_code, __ex_frame.error_message,

__ex_frame.file, __ex_frame.line);

}

} while (0)

void cexcept_throw(ExceptionCode code, const char *msg, const char *file, int line) {

if (t_current_exception_frame == NULL) {

fprintf(stderr, "\\n[FATAL] Uncaught Exception: %s (%s) at %s:%d\\n",

exception_code_str(code), msg ? msg : "No details", file, line);

exit(EXIT_FAILURE);

}

t_current_exception_frame->exception_code = code;

t_current_exception_frame->error_message = msg;

t_current_exception_frame->file = file;

t_current_exception_frame->line = line;

longjmp(t_current_exception_frame->env, (int)code);

}

##define THROW(code, msg) cexcept_throw((code), (msg), __FILE__,
__LINE__)

/* ========================================================================= */

/* APPLICATION DEMONSTRATION */

/* ========================================================================= */

double safe_divide(double numerator, double denominator) {

if (denominator == 0.0) {

THROW(EX_DIVIDE_BY_ZERO, "Attempted division by zero floating-point value");

}

return numerator / denominator;

}

void parse_record_deep(const char *raw_data) {

if (!raw_data || strlen(raw_data) == 0) {

THROW(EX_PARSING_ERROR, "Empty payload passed to record parser");

}

printf(" [Parser] Successfully processed payload: \\"%s\\"\\n", raw_data);

}

void business_logic_pipeline(const char *input_data) {

printf(" --> Entering business_logic_pipeline\...\\n");

TRY {

parse_record_deep(input_data);

double result = safe_divide(100.0, 0.0);

printf("Result: %f\\n", result);

}

CATCH(err, err_msg) {

printf(" [PIPELINE RECOVERY] Caught Inner Exception: %s => \\"%s\\"\\n",

exception_code_str(err), err_msg);

// Clean recovery or rethrow demonstration

}

FINALLY {

printf(" [PIPELINE FINALLY] Cleaning up inner pipeline resources.\\n");

} END_TRY;

printf(" <-- Exiting business_logic_pipeline normally.\\n");

}

int main(void) {

printf("===================================================================\\n");

printf(" C EXCEPTIONS: TRY / CATCH / FINALLY via setjmp & TLS frames \\n");

printf("===================================================================\\n\\n");

// Test Case 1: Handled Nested Exception with Cleanup

printf("[1] Test Case 1: Division by zero inside nested call frame:\\n");

business_logic_pipeline("valid_data_token_99");

printf("\\n[2] Test Case 2: Outer Catch Catching Unhandled Inner Exception:\\n");

TRY {

printf(" --> Outer block: Triggering invalid payload\...\\n");

parse_record_deep(""); // Throws EX_PARSING_ERROR

printf(" This line will NEVER be reached.\\n");

}

CATCH(code, msg) {

printf(" [OUTER RECOVERY] Handled top-level exception: %s (\\"%s\\")\\n",

exception_code_str(code), msg);

}

FINALLY {

printf(" [OUTER FINALLY] Global cleanup and logging finalized.\\n");

} END_TRY;

printf("\\nAll structured exception tests completed successfully!\\n");

return 0;

}

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Register Caching Trap & Leaked Handle in setjmp

Examine the following buggy file processing function:#include <stdio.h>

##include <stdlib.h>

##include <setjmp.h>

jmp_buf g_err_env;

void step_two(void) {

longjmp(g_err_env, 1); // Signal abort

}

// BUGGY CODE: Look for undefined behavior and memory leaks

void process_records_faulty(const char *filename) {

int records_processed = 0; // BUG 1: Non-volatile local variable modified after setjmp!

FILE *fp = fopen(filename, "r");

char *scratch_buffer = (char *)malloc(1024);

if (setjmp(g_err_env) == 0) {

records_processed += 10;

step_two(); // Jumps back!

records_processed += 20;

} else {

// Returned via longjmp

// BUG 2: Reading 'records_processed' here is UNDEFINED BEHAVIOR under -O2/-O3!

printf("Error occurred! Records count was: %d\\n", records_processed);

// BUG 3: 'fp' and 'scratch_buffer' are permanently LEAKED!

// Neither fclose() nor free() is invoked during the longjmp escape!

}

}

### Analysis of Vulnerabilities:

1.  **Undefined Behavior on Register Restoration:** records_processed is an automatic variable whose value changed (+= 10) after setjmp was called. Because it is not qualified with volatile, an optimizing compiler (gcc -O2) will retain its value in a CPU register (like %ebx). When longjmp restores the registers saved at setjmp, %ebx is reverted to 0. Accessing it produces unspecified or corrupted results.

2.  **Permanent Resource Leaks:** longjmp resets the stack pointer directly. Any resource allocated between setjmp and longjmp (or held prior to setjmp that was slated for destruction) will never be freed unless explicit unwinding logic or cleanup blocks catch it.

### Defensive Fix:

##include <stdio.h>

##include <stdlib.h>

##include <setjmp.h>

jmp_buf g_err_env;

void process_records_defensive(const char *filename) {

// FIX 1: Explicitly qualify locals modified after setjmp as 'volatile'

volatile int records_processed = 0;

FILE * volatile fp = NULL;

char * volatile scratch_buffer = NULL;

fp = fopen(filename, "r");

scratch_buffer = (char *)malloc(1024);

if (setjmp(g_err_env) == 0) {

records_processed += 10;

// Simulate safe execution or jump

if (!fp || !scratch_buffer) {

longjmp(g_err_env, 1);

}

} else {

printf("[Defensive Handler] Interrupted. Correct recorded count = %d\\n",

records_processed);

}

// FIX 2: Guaranteed unified cleanup block executed in all control paths

if (scratch_buffer) {

free(scratch_buffer);

scratch_buffer = NULL;

}

if (fp) {

fclose(fp);

fp = NULL;

}

}
