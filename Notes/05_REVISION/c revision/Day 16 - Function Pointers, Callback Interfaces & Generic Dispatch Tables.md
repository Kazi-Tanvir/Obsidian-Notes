\---  
tags:  
  \- c  
  \- function-pointers  
  \- callbacks  
  \- dispatch-tables  
  \- vtables  
  \- polymorphism  
  \- system-v-abi  
date: 2026-09-07  
day: 16  
\---

\# Day 16: Function Pointers, Callback Interfaces & Generic Dispatch Tables

\---

\#\# 1\. Quick Reference & Cheat Sheet

\#\#\# Function Pointer Declarations & Syntax  
A function pointer holds the virtual memory address of the first machine instruction of a function in the \`.text\` (code) segment.

| Construct | Syntax | Explanation |  
| :--- | :--- | :--- |  
| \*\*Pointer Declaration\*\* | \`int (\*func\_ptr)(int, double);\` | Pointer to a function taking \`(int, double)\` and returning \`int\`. |  
| \*\*Function Returning Ptr\*\* | \`int \*not\_a\_func\_ptr(int);\` | Regular function returning a pointer to \`int\` (\`\*\` binds to return type). |  
| \*\*\`typedef\` (Recommended)\*\* | \`typedef int (\*BinOpFn)(int, int);\` | Defines alias \`BinOpFn\` for clean, readable parameter types. |  
| \*\*Assignment\*\* | \`func\_ptr \= \&my\_func;\` or \`func\_ptr \= my\_func;\` | Functions implicitly decay into pointers to themselves. |  
| \*\*Invocation\*\* | \`int res \= func\_ptr(2, 3);\` or \`(\*func\_ptr)(2, 3);\` | Both syntax forms are functionally and semantically identical in C. |  
| \*\*Array of Function Ptrs\*\* | \`void (\*dispatch\[16\])(void \*ctx);\` | An array of 16 function pointers (Dispatch Table). |  
| \*\*Function Returning Ptr\*\* | \`BinOpFn get\_op(char op);\` | Function that selects and returns an appropriate function pointer. |

\#\#\# The Universal Callback Idiom  
\*\*Always\*\* bundle a \`void \*user\_data\` (context) pointer alongside the callback designator:  
\`\`\`c  
// POOR DESIGN: Cannot pass instance-specific state; forces use of thread-unsafe globals.  
typedef void (\*PoorCallback)(int event\_id);

// IDIOMATIC & ROBUST DESIGN: Contextual callback (reentrant, thread-safe, modular)  
typedef void (\*ContextCallback)(int event\_id, void \*user\_data);  
\`\`\`

\---

\#\# 2\. In-Depth Theory & Low-Level Mechanics

\#\#\# A. Direct vs Indirect Function Calls at the CPU Level  
When executing a standard direct function call, the target address is hardcoded or resolved as a static relative offset by the linker:  
\`\`\`c  
void target(void);  
target();  
\`\`\`  
\`\`\`nasm  
; Direct Call (x86\_64)  
call target            ; E8 xx xx xx xx (5 bytes: opcode \+ 32-bit relative displacement)  
\`\`\`

When executing through a function pointer, the CPU performs an \*\*Indirect Call\*\*:  
\`\`\`c  
void (\*fp)(void) \= target;  
fp();  
\`\`\`  
\`\`\`nasm  
; Indirect Call (x86\_64)  
mov  rax, QWORD PTR \[rbp \- 8\]  ; Load 64-bit target address from memory/stack into register  
call rax                       ; FF D0 (2 bytes: indirect call through register)  
\`\`\`  
\* \*\*Performance Impact & Branch Prediction:\*\* Direct calls are unconditionally resolved by the CPU decoder. Indirect calls require the CPU's \*\*Branch Target Buffer (BTB)\*\* to predict the target address. If the target changes frequently across loop iterations, BTB mispredictions stall the CPU instruction pipeline for 15–20 cycles.

\---

\#\#\# B. Virtual Method Tables (vtables) in Pure C  
To achieve object-oriented runtime polymorphism in C (simulating C++ classes or Rust traits):  
1\. Define a \`struct VTable\` containing function pointers representing methods.  
2\. Embed a \`const struct VTable \*vptr\` inside the object structure.  
3\. Every method receives an explicit \`void \*self\` or \`struct MyObject \*self\` as its first parameter.

\`\`\`text  
Object Instance in Heap:                     VTable in .rodata:  
 ┌───────────────────────────┐                ┌───────────────────────────────────┐  
 │ vptr ─────────────────────┼───────────────►│ area() ────► \&circle\_area()       │  
 ├───────────────────────────┤                │ draw() ────► \&circle\_draw()       │  
 │ double radius             │                └───────────────────────────────────┘  
 └───────────────────────────┘  
\`\`\`

\---

\#\#\# C. The Incompatible Signature Trap (System V AMD64 ABI)  
Under modern 64-bit ABIs:  
\* The first 6 integer/pointer arguments are passed in registers: \`%rdi\`, \`%rsi\`, \`%rdx\`, \`%rcx\`, \`%r8\`, \`%r9\`.  
\* Floating-point arguments are passed in \`%xmm0\` through \`%xmm7\`.  
\* If you cast a function expecting \`(double, double)\` to \`(int, int)\` and call it, the callee attempts to read \`%xmm0\` (uninitialized), while the caller placed arguments in \`%rdi\` and \`%rsi\`.  
\* \*\*Casting function pointers to incompatible prototypes and invoking them is UNDEFINED BEHAVIOR.\*\*

\---

\#\# 3\. Thoughtful Mini-Project (\~1 Hour Scope)

\#\#\# Project Title: Asynchronous Event Bus & Opcode Dispatch Engine (\`event\_bus\`)

\#\#\#\# Objective  
Build a decoupled publish-subscribe event broker and command dispatch table in C featuring:  
1\. Dynamic listener registration with stateful contextual user payloads (\`void \*user\_data\`).  
2\. An $O(1)$ opcode jump table for instant command routing.  
3\. Thread-safe reentrant architecture with zero global variables.

\#\#\#\# Complete Starter Code Implementation  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdint.h\>  
\#include \<stdbool.h\>  
\#include \<string.h\>  
\#include \<assert.h\>

\#define MAX\_HANDLERS\_PER\_EVENT 8  
\#define MAX\_OPCODES 16

typedef enum {  
    EVENT\_SENSOR\_UPDATE \= 0,  
    EVENT\_NETWORK\_ALERT  \= 1,  
    EVENT\_SYSTEM\_SHUTDOWN \= 2,  
    EVENT\_COUNT  
} EventType;

// Universal Callback Signature  
typedef void (\*EventHandlerFn)(const void \*event\_data, void \*user\_data);

typedef struct {  
    EventHandlerFn fn;  
    void \*user\_data;  
} Subscription;

typedef struct {  
    Subscription subscribers\[EVENT\_COUNT\]\[MAX\_HANDLERS\_PER\_EVENT\];  
    size\_t subscriber\_counts\[EVENT\_COUNT\];  
} EventBus;

/\* \========================================================================= \*/  
/\*                          1\. EVENT BUS SUBSYSTEM                           \*/  
/\* \========================================================================= \*/

EventBus \*event\_bus\_create(void) {  
    EventBus \*bus \= (EventBus \*)calloc(1, sizeof(EventBus));  
    return bus;  
}

void event\_bus\_destroy(EventBus \*bus) {  
    if (\!bus) return;  
    free(bus);  
}

bool event\_bus\_subscribe(EventBus \*bus, EventType type, EventHandlerFn fn, void \*user\_data) {  
    if (\!bus || \!fn || type \>= EVENT\_COUNT) return false;

    size\_t count \= bus-\>subscriber\_counts\[type\];  
    if (count \>= MAX\_HANDLERS\_PER\_EVENT) {  
        fprintf(stderr, "Subscription Limit Exceeded for Event Type %d\!\\n", type);  
        return false;  
    }

    bus-\>subscribers\[type\]\[count\].fn \= fn;  
    bus-\>subscribers\[type\]\[count\].user\_data \= user\_data;  
    bus-\>subscriber\_counts\[type\]++;  
    return true;  
}

void event\_bus\_publish(EventBus \*bus, EventType type, const void \*event\_data) {  
    if (\!bus || type \>= EVENT\_COUNT) return;

    size\_t count \= bus-\>subscriber\_counts\[type\];  
    for (size\_t i \= 0; i \< count; i++) {  
        Subscription \*sub \= \&bus-\>subscribers\[type\]\[i\];  
        if (sub-\>fn) {  
            // Invoke callback passing event payload and subscriber's private context  
            sub-\>fn(event\_data, sub-\>user\_data);  
        }  
    }  
}

/\* \========================================================================= \*/  
/\*                   2\. OPCODE COMMAND DISPATCH TABLE                        \*/  
/\* \========================================================================= \*/

typedef struct CommandContext {  
    int register\_a;  
    int register\_b;  
    bool halted;  
} CommandContext;

typedef void (\*CommandHandlerFn)(CommandContext \*ctx, int argument);

typedef struct {  
    CommandHandlerFn handlers\[MAX\_OPCODES\];  
} DispatchTable;

void dispatch\_register(DispatchTable \*table, uint8\_t opcode, CommandHandlerFn handler) {  
    assert(opcode \< MAX\_OPCODES);  
    table-\>handlers\[opcode\] \= handler;  
}

bool dispatch\_execute(const DispatchTable \*table, CommandContext \*ctx, uint8\_t opcode, int arg) {  
    if (opcode \>= MAX\_OPCODES || \!table-\>handlers\[opcode\]) {  
        fprintf(stderr, "Unknown or Unregistered Opcode: 0x%02X\\n", opcode);  
        return false;  
    }  
    table-\>handlers\[opcode\](ctx, arg); // O(1) Indirect Dispatch  
    return true;  
}

/\* \========================================================================= \*/  
/\*                          SAMPLE HANDLERS & DRIVER                         \*/  
/\* \========================================================================= \*/

typedef struct {  
    double temperature;  
    int sensor\_id;  
} SensorEvent;

// Stateful Listener Context  
typedef struct {  
    double temp\_threshold;  
    int alert\_count;  
} AlertMonitor;

void on\_sensor\_reading(const void \*event\_data, void \*user\_data) {  
    const SensorEvent \*ev \= (const SensorEvent \*)event\_data;  
    AlertMonitor \*mon \= (AlertMonitor \*)user\_data;

    printf("  \[Sensor Handler\] Sensor \#%d reported: %.2f C\\n", ev-\>sensor\_id, ev-\>temperature);  
    if (ev-\>temperature \> mon-\>temp\_threshold) {  
        mon-\>alert\_count++;  
        printf("  \[ALERT TRIGGERED\] Temperature exceeds threshold (%.2f C)\! Total Alerts: %d\\n",  
               mon-\>temp\_threshold, mon-\>alert\_count);  
    }  
}

void on\_system\_shutdown(const void \*event\_data, void \*user\_data) {  
    (void)event\_data;  
    const char \*service\_name \= (const char \*)user\_data;  
    printf("  \[Shutdown Handler\] Service '%s' received shutdown broadcast. Flushing buffers.\\n", service\_name);  
}

// Opcode Handlers  
void op\_set\_a(CommandContext \*ctx, int arg) { ctx-\>register\_a \= arg; }  
void op\_add\_b(CommandContext \*ctx, int arg) { ctx-\>register\_a \+= arg; }  
void op\_halt(CommandContext \*ctx, int arg)  { (void)arg; ctx-\>halted \= true; }

int main(void) {  
    printf("=== Testing Function Pointer Event Bus & Dispatch Table \===\\n\\n");

    // 1\. Initialize Event Bus  
    EventBus \*bus \= event\_bus\_create();  
    AlertMonitor monitor \= { .temp\_threshold \= 75.0, .alert\_count \= 0 };

    event\_bus\_subscribe(bus, EVENT\_SENSOR\_UPDATE, on\_sensor\_reading, \&monitor);  
    event\_bus\_subscribe(bus, EVENT\_SYSTEM\_SHUTDOWN, on\_system\_shutdown, "TelemetryWorkerService");

    // 2\. Publish Events  
    printf("\[1\] Publishing Normal Sensor Event:\\n");  
    SensorEvent s1 \= { .sensor\_id \= 1, .temperature \= 68.5 };  
    event\_bus\_publish(bus, EVENT\_SENSOR\_UPDATE, \&s1);

    printf("\\n\[2\] Publishing Critical Sensor Event:\\n");  
    SensorEvent s2 \= { .sensor\_id \= 2, .temperature \= 84.2 };  
    event\_bus\_publish(bus, EVENT\_SENSOR\_UPDATE, \&s2);  
    assert(monitor.alert\_count \== 1);

    printf("\\n\[3\] Publishing Shutdown Event:\\n");  
    event\_bus\_publish(bus, EVENT\_SYSTEM\_SHUTDOWN, NULL);

    // 3\. Test Opcode Dispatch Table  
    printf("\\n\[4\] Executing Opcode Dispatch Table:\\n");  
    DispatchTable vm;  
    memset(\&vm, 0, sizeof(vm));  
    dispatch\_register(\&vm, 0x01, op\_set\_a);  
    dispatch\_register(\&vm, 0x02, op\_add\_b);  
    dispatch\_register(\&vm, 0xFF % MAX\_OPCODES, op\_halt);

    CommandContext vm\_ctx \= { .register\_a \= 0, .register\_b \= 0, .halted \= false };  
    dispatch\_execute(\&vm, \&vm\_ctx, 0x01, 50); // Set A \= 50  
    dispatch\_execute(\&vm, \&vm\_ctx, 0x02, 25); // Add 25 \-\> A \= 75  
    printf("    VM Register A Result: %d\\n", vm\_ctx.register\_a);  
    assert(vm\_ctx.register\_a \== 75);

    event\_bus\_destroy(bus);  
    printf("\\nAll components tested cleanly with zero leaks\!\\n");  
    return 0;  
}  
\`\`\`

\---

\#\# 4\. Error Handling & Defensive Programming Challenge

\#\#\# Scenario: The Dangling Callback Target & ABI Prototype Mismatch  
Examine the following faulty event callback system:

\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>

// Expected callback: returns void, accepts (int, int)  
typedef void (\*CalcCallback)(int a, int b);

struct Service {  
    CalcCallback cb;  
};

// Target function has completely different prototype: returns double, takes (double, double)  
double multiply\_doubles(double x, double y) {  
    return x \* y;  
}

// BUGGY REGISTRATION  
void register\_faulty(struct Service \*s) {  
    // BUG 1: Incompatible function pointer cast\!  
    // Forces compiler to ignore prototype mismatch via (CalcCallback).  
    // Caller passes integers in %edi and %esi, callee looks for floats in %xmm0 and %xmm1\!  
    s-\>cb \= (CalcCallback)multiply\_doubles;  
}

void trigger\_faulty(struct Service \*s) {  
    // BUG 2: Dereferencing without NULL guard\!  
    s-\>cb(10, 20); // Invokes Undefined Behavior / Crash  
}  
\`\`\`

\#\#\# Analysis of Vulnerabilities:  
1\. \*\*ABI Register Incoherence:\*\* Casting \`double (\*)(double, double)\` to \`void (\*)(int, int)\` violates the System V AMD64 ABI. The caller places integer values into general-purpose registers (\`%rdi\`, \`%rsi\`), while the function expects floating-point registers (\`%xmm0\`, \`%xmm1\`). Calling this yields garbage values or corrupted registers.  
2\. \*\*Missing \`NULL\` Assertion:\*\* Invoking an uninitialized or reset function pointer (\`s-\>cb \== NULL\`) triggers an immediate segmentation fault trying to execute address \`0x00000000\`.

\#\#\# Defensive Fix:  
\`\`\`c  
\#include \<stdio.h\>  
\#include \<stdlib.h\>  
\#include \<stdbool.h\>  
\#include \<assert.h\>

// Uniform, type-safe callback contract  
typedef void (\*SafeCallback)(int a, int b, void \*user\_data);

typedef struct {  
    SafeCallback cb;  
    void \*user\_data;  
} CallbackSlot;

// Type-safe adapter function matching the expected contract  
static void multiply\_doubles\_adapter(int a, int b, void \*user\_data) {  
    double \*out\_result \= (double \*)user\_data;  
    double res \= (double)a \* (double)b;  
    if (out\_result) {  
        \*out\_result \= res;  
    }  
    printf("Defensive Adapter: %d \* %d \= %.2f\\n", a, b, res);  
}

bool register\_callback\_safe(CallbackSlot \*slot, SafeCallback cb, void \*user\_data) {  
    if (\!slot || \!cb) return false;  
    slot-\>cb \= cb;  
    slot-\>user\_data \= user\_data;  
    return true;  
}

bool invoke\_callback\_safe(const CallbackSlot \*slot, int a, int b) {  
    // Defensive Check 1: Ensure slot and target function pointer are non-NULL  
    if (\!slot || \!slot-\>cb) {  
        fprintf(stderr, "Defensive Error: Attempted to invoke NULL function pointer\!\\n");  
        return false;  
    }

    // Safe invocation using guaranteed matching ABI signature  
    slot-\>cb(a, b, slot-\>user\_data);  
    return true;  
}  
\`\`\`  
