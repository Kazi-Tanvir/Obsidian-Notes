---
tags:
  - c
  - function-pointers
  - callbacks
  - dispatch-tables
  - vtables
  - polymorphism
  - system-v-abi
date: 2026-09-07
day: 16
---

# Day 16: Function Pointers, Callback Interfaces & Generic Dispatch Tables

---

## 1. Quick Reference & Cheat Sheet

### Function Pointer Declarations & Syntax
A function pointer holds the virtual memory address of the first machine instruction of a function in the `.text` (code) segment.

| Construct | Syntax | Explanation |
| :--- | :--- | :--- |
| **Pointer Declaration** | `int (*func_ptr)(int, double);` | Pointer to a function taking `(int, double)` and returning `int`. |
| **Function Returning Ptr** | `int *not_a_func_ptr(int);` | Regular function returning a pointer to `int` (`*` binds to return type). |
| **`typedef` (Recommended)** | `typedef int (*BinOpFn)(int, int);` | Defines alias `BinOpFn` for clean, readable parameter types. |
| **Assignment** | `func_ptr \= \&my_func;` or `func_ptr \= my_func;` | Functions implicitly decay into pointers to themselves. |
| **Invocation** | `int res \= func_ptr(2, 3);` or `(*func_ptr)(2, 3);` | Both syntax forms are functionally and semantically identical in C. |
| **Array of Function Ptrs** | `void (*dispatch[16])(void *ctx);` | An array of 16 function pointers (Dispatch Table). |
| **Function Returning Ptr** | `BinOpFn get_op(char op);` | Function that selects and returns an appropriate function pointer. |

### The Universal Callback Idiom
**Always** bundle a `void *user_data` (context) pointer alongside the callback designator:
```c
// POOR DESIGN: Cannot pass instance-specific state; forces use of thread-unsafe globals.
typedef void (*PoorCallback)(int event_id);

// IDIOMATIC & ROBUST DESIGN: Contextual callback (reentrant, thread-safe, modular)
typedef void (*ContextCallback)(int event_id, void *user_data);
```

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Direct vs Indirect Function Calls at the CPU Level
When executing a standard direct function call, the target address is hardcoded or resolved as a static relative offset by the linker:
```c
void target(void);
target();
```
```nasm
; Direct Call (x86_64)
call target            ; E8 xx xx xx xx (5 bytes: opcode \+ 32-bit relative displacement)
```

When executing through a function pointer, the CPU performs an **Indirect Call**:
```c
void (*fp)(void) \= target;
fp();
```
```nasm
; Indirect Call (x86_64)
mov  rax, QWORD PTR [rbp \- 8]  ; Load 64-bit target address from memory/stack into register
call rax                       ; FF D0 (2 bytes: indirect call through register)
```
* **Performance Impact & Branch Prediction:** Direct calls are unconditionally resolved by the CPU decoder. Indirect calls require the CPU's **Branch Target Buffer (BTB)** to predict the target address. If the target changes frequently across loop iterations, BTB mispredictions stall the CPU instruction pipeline for 15–20 cycles.

---

### B. Virtual Method Tables (vtables) in Pure C
To achieve object-oriented runtime polymorphism in C (simulating C++ classes or Rust traits):
1. Define a `struct VTable` containing function pointers representing methods.
2. Embed a `const struct VTable *vptr` inside the object structure.
3. Every method receives an explicit `void *self` or `struct MyObject *self` as its first parameter.

```text
Object Instance in Heap:                     VTable in .rodata:
 ┌───────────────────────────┐                ┌───────────────────────────────────┐
 │ vptr ─────────────────────┼───────────────►│ area() ────► \&circle_area()       │
 ├───────────────────────────┤                │ draw() ────► \&circle_draw()       │
 │ double radius             │                └───────────────────────────────────┘
 └───────────────────────────┘
```

---

### C. The Incompatible Signature Trap (System V AMD64 ABI)
Under modern 64-bit ABIs:
* The first 6 integer/pointer arguments are passed in registers: `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, `%r9`.
* Floating-point arguments are passed in `%xmm0` through `%xmm7`.
* If you cast a function expecting `(double, double)` to `(int, int)` and call it, the callee attempts to read `%xmm0` (uninitialized), while the caller placed arguments in `%rdi` and `%rsi`.
* **Casting function pointers to incompatible prototypes and invoking them is UNDEFINED BEHAVIOR.**

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Asynchronous Event Bus & Opcode Dispatch Engine (`event_bus`)

#### Objective
Build a decoupled publish-subscribe event broker and command dispatch table in C featuring:
1. Dynamic listener registration with stateful contextual user payloads (`void *user_data`).
2. An $O(1)$ opcode jump table for instant command routing.
3. Thread-safe reentrant architecture with zero global variables.

#### Complete Starter Code Implementation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

#define MAX_HANDLERS_PER_EVENT 8
#define MAX_OPCODES 16

typedef enum {
    EVENT_SENSOR_UPDATE \= 0,
    EVENT_NETWORK_ALERT  \= 1,
    EVENT_SYSTEM_SHUTDOWN \= 2,
    EVENT_COUNT
} EventType;

// Universal Callback Signature
typedef void (*EventHandlerFn)(const void *event_data, void *user_data);

typedef struct {
    EventHandlerFn fn;
    void *user_data;
} Subscription;

typedef struct {
    Subscription subscribers[EVENT_COUNT][MAX_HANDLERS_PER_EVENT];
    size_t subscriber_counts[EVENT_COUNT];
} EventBus;

/* \========================================================================= */
/*                          1. EVENT BUS SUBSYSTEM                           */
/* \========================================================================= */

EventBus *event_bus_create(void) {
    EventBus *bus \= (EventBus *)calloc(1, sizeof(EventBus));
    return bus;
}

void event_bus_destroy(EventBus *bus) {
    if (\!bus) return;
    free(bus);
}

bool event_bus_subscribe(EventBus *bus, EventType type, EventHandlerFn fn, void *user_data) {
    if (\!bus || \!fn || type >= EVENT_COUNT) return false;

    size_t count \= bus->subscriber_counts[type];
    if (count >= MAX_HANDLERS_PER_EVENT) {
        fprintf(stderr, "Subscription Limit Exceeded for Event Type %d\!\\n", type);
        return false;
    }

    bus->subscribers[type][count].fn \= fn;
    bus->subscribers[type][count].user_data \= user_data;
    bus->subscriber_counts[type]++;
    return true;
}

void event_bus_publish(EventBus *bus, EventType type, const void *event_data) {
    if (\!bus || type >= EVENT_COUNT) return;

    size_t count \= bus->subscriber_counts[type];
    for (size_t i \= 0; i < count; i++) {
        Subscription *sub \= \&bus->subscribers[type][i];
        if (sub->fn) {
            // Invoke callback passing event payload and subscriber's private context
            sub->fn(event_data, sub->user_data);
        }
    }
}

/* \========================================================================= */
/*                   2. OPCODE COMMAND DISPATCH TABLE                        */
/* \========================================================================= */

typedef struct CommandContext {
    int register_a;
    int register_b;
    bool halted;
} CommandContext;

typedef void (*CommandHandlerFn)(CommandContext *ctx, int argument);

typedef struct {
    CommandHandlerFn handlers[MAX_OPCODES];
} DispatchTable;

void dispatch_register(DispatchTable *table, uint8_t opcode, CommandHandlerFn handler) {
    assert(opcode < MAX_OPCODES);
    table->handlers[opcode] \= handler;
}

bool dispatch_execute(const DispatchTable *table, CommandContext *ctx, uint8_t opcode, int arg) {
    if (opcode >= MAX_OPCODES || \!table->handlers[opcode]) {
        fprintf(stderr, "Unknown or Unregistered Opcode: 0x%02X\\n", opcode);
        return false;
    }
    table->handlers[opcode](ctx, arg); // O(1) Indirect Dispatch
    return true;
}

/* \========================================================================= */
/*                          SAMPLE HANDLERS & DRIVER                         */
/* \========================================================================= */

typedef struct {
    double temperature;
    int sensor_id;
} SensorEvent;

// Stateful Listener Context
typedef struct {
    double temp_threshold;
    int alert_count;
} AlertMonitor;

void on_sensor_reading(const void *event_data, void *user_data) {
    const SensorEvent *ev \= (const SensorEvent *)event_data;
    AlertMonitor *mon \= (AlertMonitor *)user_data;

    printf("  [Sensor Handler] Sensor \#%d reported: %.2f C\\n", ev->sensor_id, ev->temperature);
    if (ev->temperature > mon->temp_threshold) {
        mon->alert_count++;
        printf("  [ALERT TRIGGERED] Temperature exceeds threshold (%.2f C)\! Total Alerts: %d\\n",
               mon->temp_threshold, mon->alert_count);
    }
}

void on_system_shutdown(const void *event_data, void *user_data) {
    (void)event_data;
    const char *service_name \= (const char *)user_data;
    printf("  [Shutdown Handler] Service '%s' received shutdown broadcast. Flushing buffers.\\n", service_name);
}

// Opcode Handlers
void op_set_a(CommandContext *ctx, int arg) { ctx->register_a \= arg; }
void op_add_b(CommandContext *ctx, int arg) { ctx->register_a \+= arg; }
void op_halt(CommandContext *ctx, int arg)  { (void)arg; ctx->halted \= true; }

int main(void) {
    printf("=== Testing Function Pointer Event Bus & Dispatch Table \===\\n\\n");

    // 1. Initialize Event Bus
    EventBus *bus \= event_bus_create();
    AlertMonitor monitor \= { .temp_threshold \= 75.0, .alert_count \= 0 };

    event_bus_subscribe(bus, EVENT_SENSOR_UPDATE, on_sensor_reading, \&monitor);
    event_bus_subscribe(bus, EVENT_SYSTEM_SHUTDOWN, on_system_shutdown, "TelemetryWorkerService");

    // 2. Publish Events
    printf("[1] Publishing Normal Sensor Event:\\n");
    SensorEvent s1 \= { .sensor_id \= 1, .temperature \= 68.5 };
    event_bus_publish(bus, EVENT_SENSOR_UPDATE, \&s1);

    printf("\\n[2] Publishing Critical Sensor Event:\\n");
    SensorEvent s2 \= { .sensor_id \= 2, .temperature \= 84.2 };
    event_bus_publish(bus, EVENT_SENSOR_UPDATE, \&s2);
    assert(monitor.alert_count \== 1);

    printf("\\n[3] Publishing Shutdown Event:\\n");
    event_bus_publish(bus, EVENT_SYSTEM_SHUTDOWN, NULL);

    // 3. Test Opcode Dispatch Table
    printf("\\n[4] Executing Opcode Dispatch Table:\\n");
    DispatchTable vm;
    memset(\&vm, 0, sizeof(vm));
    dispatch_register(\&vm, 0x01, op_set_a);
    dispatch_register(\&vm, 0x02, op_add_b);
    dispatch_register(\&vm, 0xFF % MAX_OPCODES, op_halt);

    CommandContext vm_ctx \= { .register_a \= 0, .register_b \= 0, .halted \= false };
    dispatch_execute(\&vm, \&vm_ctx, 0x01, 50); // Set A \= 50
    dispatch_execute(\&vm, \&vm_ctx, 0x02, 25); // Add 25 \-> A \= 75
    printf("    VM Register A Result: %d\\n", vm_ctx.register_a);
    assert(vm_ctx.register_a \== 75);

    event_bus_destroy(bus);
    printf("\\nAll components tested cleanly with zero leaks\!\\n");
    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Dangling Callback Target & ABI Prototype Mismatch
Examine the following faulty event callback system:

```c
#include <stdio.h>
#include <stdlib.h>

// Expected callback: returns void, accepts (int, int)
typedef void (*CalcCallback)(int a, int b);

struct Service {
    CalcCallback cb;
};

// Target function has completely different prototype: returns double, takes (double, double)
double multiply_doubles(double x, double y) {
    return x * y;
}

// BUGGY REGISTRATION
void register_faulty(struct Service *s) {
    // BUG 1: Incompatible function pointer cast\!
    // Forces compiler to ignore prototype mismatch via (CalcCallback).
    // Caller passes integers in %edi and %esi, callee looks for floats in %xmm0 and %xmm1\!
    s->cb \= (CalcCallback)multiply_doubles;
}

void trigger_faulty(struct Service *s) {
    // BUG 2: Dereferencing without NULL guard\!
    s->cb(10, 20); // Invokes Undefined Behavior / Crash
}
```

### Analysis of Vulnerabilities:
1. **ABI Register Incoherence:** Casting `double (*)(double, double)` to `void (*)(int, int)` violates the System V AMD64 ABI. The caller places integer values into general-purpose registers (`%rdi`, `%rsi`), while the function expects floating-point registers (`%xmm0`, `%xmm1`). Calling this yields garbage values or corrupted registers.
2. **Missing `NULL` Assertion:** Invoking an uninitialized or reset function pointer (`s->cb \== NULL`) triggers an immediate segmentation fault trying to execute address `0x00000000`.

### Defensive Fix:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

// Uniform, type-safe callback contract
typedef void (*SafeCallback)(int a, int b, void *user_data);

typedef struct {
    SafeCallback cb;
    void *user_data;
} CallbackSlot;

// Type-safe adapter function matching the expected contract
static void multiply_doubles_adapter(int a, int b, void *user_data) {
    double *out_result \= (double *)user_data;
    double res \= (double)a * (double)b;
    if (out_result) {
        *out_result \= res;
    }
    printf("Defensive Adapter: %d * %d \= %.2f\\n", a, b, res);
}

bool register_callback_safe(CallbackSlot *slot, SafeCallback cb, void *user_data) {
    if (\!slot || \!cb) return false;
    slot->cb \= cb;
    slot->user_data \= user_data;
    return true;
}

bool invoke_callback_safe(const CallbackSlot *slot, int a, int b) {
    // Defensive Check 1: Ensure slot and target function pointer are non-NULL
    if (\!slot || \!slot->cb) {
        fprintf(stderr, "Defensive Error: Attempted to invoke NULL function pointer\!\\n");
        return false;
    }

    // Safe invocation using guaranteed matching ABI signature
    slot->cb(a, b, slot->user_data);
    return true;
}
```
