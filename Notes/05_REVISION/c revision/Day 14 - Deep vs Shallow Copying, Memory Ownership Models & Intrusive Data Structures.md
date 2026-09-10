---
tags:
  - c
  - memory-ownership
  - deep-copy-shallow-copy
  - intrusive-data-structures
  - pointer-lifecycles
  - defensive-programming
date: 2026-09-05
day: 14
---

# Day 14: Deep vs Shallow Copying, Memory Ownership Models & Intrusive Data Structures

---

## 1. Quick Reference & Cheat Sheet

### Shallow Copy vs Deep Copy
* **Shallow Copy (`*dest \= *src` / `memcpy`):** Copies the raw bytes of a structure directly. If the structure contains pointers to heap memory, only the memory addresses are copied, resulting in two structs referencing the exact same allocated heap memory.
* **Deep Copy:** Allocates brand-new independent memory buffers for every pointer member and recursively duplicates all nested strings, arrays, and sub-objects.

| Operation | Implementation | Aliasing Hazard? | Double-Free Risk? | Performance |
| :--- | :--- | :--- | :--- | :--- |
| **Shallow Copy** | `*dest \= *src;` or `memcpy(dest, src, sizeof(T));` | **YES** (Pointers share buffer) | **CRITICAL** (Both callers free same ptr) | $O(1)$ |
| **Deep Copy** | Explicit allocation \+ member-by-member copy | **NO** (Independent memory) | **SAFE** (Separate lifecycles) | $O(N)$ allocations |

### Memory Ownership Contracts
1. **Borrowed Pointer:** The function receives a pointer to inspect or mutate during its execution scope, but **must not** store it globally or call `free()`.
2. **Owned Pointer (Transfer of Ownership):** The function takes full responsibility for the memory block and is obligated to free it or pass it to another owner.
3. **Out-Parameter Allocation:** Callee allocates, caller owns. Always pass `T**` and document the contract explicitly.

### The Linux Kernel `container_of` Macro
Converts a pointer to an intrusive struct member back into a pointer to the parent container struct:
```c
#include <stddef.h>

#define container_of(ptr, type, member) \\
    ((type *)((char *)(ptr) \- offsetof(type, member)))
```

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. The Mechanics of Shallow Struct Assignment
In C, assigning one struct variable to another (`struct A b \= a;`) is valid syntax. The compiler generates a fast memory block copy (typically inlined `rep movsq` on x86_64).

```c
typedef struct {
    int id;
    char *name; // Points to heap buffer
} User;

User u1;
u1.id \= 1;
u1.name \= strdup("Alice");

User u2 \= u1; // Bitwise shallow copy\!
```

```text
Stack Frame:                           Heap Memory:
 ┌────────────────────────┐
 │ u1.id   \= 1            │
 │ u1.name \= 0x55AA_1000  ├─────────────► ┌───────────────────────┐
 ├────────────────────────┤               │ "Alice\\0" (0x55AA_1000)│
 │ u2.id   \= 1            │               └───────────────────────┘
 │ u2.name \= 0x55AA_1000  ├─────────────►            ▲
 └────────────────────────┘                          │
                                    Shared pointer target\!
```

#### The Lifecycle Failure Sequence:
1. `u1` is destroyed or freed: `free(u1.name);`
2. `0x55AA_1000` is returned to the heap allocator.
3. `u2.name` is now a **Dangling Pointer**.
4. Later, `u2` is destroyed: `free(u2.name);` $\\implies$ **Heap Double-Free Abort (`SIGABRT`)**.

---

### B. Intrusive vs Non-Intrusive Data Structures
Standard computer science textbooks teach **Non-Intrusive (Wrapper)** data structures:
```c
// Non-Intrusive: Separate wrapper node wrapping payload pointer
typedef struct Node {
    void *data;
    struct Node *next;
} Node;
```
* **Disadvantages:** Requires 2 heap allocations per element (`malloc(sizeof(Node))` and `malloc(sizeof(Payload))`), doubles pointer indirection, and causes heavy cache misses.

**Intrusive Data Structures** (used in Linux Kernel, FreeBSD, high-performance game engines) embed the list linkage node directly **inside** the payload struct:
```c
typedef struct ListNode {
    struct ListNode *next;
    struct ListNode *prev;
} ListNode;

typedef struct Task {
    int task_id;
    int priority;
    ListNode list_hook; // Embedded directly in payload\!
} Task;
```
* **Advantages:** 0 extra allocations, contiguous memory layout, high cache locality, and an object can belong to multiple lists simultaneously by embedding multiple `ListNode` hooks.

---

### C. Dissecting the `container_of` Macro
```c
#define container_of(ptr, type, member) \\
    ((type *)((char *)(ptr) \- offsetof(type, member)))
```
1. `offsetof(type, member)`: Determines the compile-time byte distance of `member` from the beginning of `type`.
2. `(char *)(ptr)`: Casts the member pointer to a 1-byte pointer to enable precise byte-level pointer arithmetic.
3. `(char *)(ptr) \- offset`: Subtracts the offset, stepping backwards in memory to the exact starting byte of the enclosing struct.
4. `(type *)`: Casts the base address back to the container struct type.

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Intrusive Linked Task Queue with Deep Cloning Engine (`intrusive_tasks`)

#### Objective
Build a C scheduling queue that:
1. Implements an **Intrusive Doubly-Linked List** using the `container_of` macro pattern.
2. Supports **Deep Cloning** of task payloads containing dynamic heap-allocated descriptions and metadata.
3. Implements **Recursive Safe Deallocation** ensuring zero memory leaks.

#### Complete Starter Code Implementation
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stddef.h>
#include <assert.h>

/* \========================================================================= */
/*                    1. INTRUSIVE DOUBLY-LINKED LIST                        */
/* \========================================================================= */

#define container_of(ptr, type, member) \\
    ((type *)((char *)(ptr) \- offsetof(type, member)))

typedef struct ListNode {
    struct ListNode *next;
    struct ListNode *prev;
} ListNode;

static inline void list_init(ListNode *head) {
    head->next \= head;
    head->prev \= head;
}

static inline void list_add_tail(ListNode *head, ListNode *new_node) {
    ListNode *prev \= head->prev;
    prev->next \= new_node;
    new_node->prev \= prev;
    new_node->next \= head;
    head->prev \= new_node;
}

static inline void list_del(ListNode *node) {
    node->prev->next \= node->next;
    node->next->prev \= node->prev;
    node->next \= NULL;
    node->prev \= NULL;
}

static inline bool list_empty(const ListNode *head) {
    return head->next \== head;
}

/* \========================================================================= */
/*                     2. TASK PAYLOAD & DEEP CLONING                        */
/* \========================================================================= */

typedef struct Task {
    uint32_t id;
    int priority;
    char *title;        // Dynamic string (must be deep copied)
    char *description;  // Dynamic string (must be deep copied)
    ListNode queue_hook; // Intrusive list node embedded in payload
} Task;

// Allocate and initialize a task
Task *task_create(uint32_t id, int priority, const char *title, const char *desc) {
    Task *t \= (Task *)malloc(sizeof(Task));
    if (\!t) return NULL;

    t->id \= id;
    t->priority \= priority;
    t->title \= title ? strdup(title) : NULL;
    t->description \= desc ? strdup(desc) : NULL;
    t->queue_hook.next \= NULL;
    t->queue_hook.prev \= NULL;

    return t;
}

// Deep Copy: Creates an entirely independent task with cloned strings
Task *task_deep_clone(const Task *src) {
    if (\!src) return NULL;
    return task_create(src->id, src->priority, src->title, src->description);
}

// Release all resources owned by the task
void task_destroy(Task *t) {
    if (\!t) return;
    if (t->title) free(t->title);
    if (t->description) free(t->description);
    free(t);
}

/* \========================================================================= */
/*                               DRIVER MAIN                                 */
/* \========================================================================= */

int main(void) {
    printf("=== Demonstrating Intrusive Lists & Deep Copy Engine \===\\n\\n");

    ListNode task_queue;
    list_init(\&task_queue);

    // 1. Create original tasks
    Task *t1 \= task_create(101, 1, "Initialize Database", "Connect to MySQL cluster on port 3306");
    Task *t2 \= task_create(102, 2, "Start HTTP Server", "Bind socket listener on port 8080");

    list_add_tail(\&task_queue, \&t1->queue_hook);
    list_add_tail(\&task_queue, \&t2->queue_hook);

    // 2. Iterate intrusive list using container_of
    printf("[1] Tasks in Active Queue:\\n");
    ListNode *curr \= task_queue.next;
    while (curr \!= \&task_queue) {
        Task *task \= container_of(curr, Task, queue_hook);
        printf("    Task \#%u [Prio: %d]: \\"%s\\"\\n      Desc: %s\\n",
               task->id, task->priority, task->title, task->description);
        curr \= curr->next;
    }

    // 3. Perform Deep Clone
    printf("\\n[2] Performing Deep Clone of Task \#101...\\n");
    Task *cloned_task \= task_deep_clone(t1);

    // Mutate the clone's string to prove memory isolation
    free(cloned_task->title);
    cloned_task->title \= strdup("MUTATED: Backup Database");

    printf("    Original Task \#101 Title: %s (Address: %p)\\n", t1->title, (void *)t1->title);
    printf("    Cloned Task \#101 Title:   %s (Address: %p)\\n", cloned_task->title, (void *)cloned_task->title);
    assert(strcmp(t1->title, cloned_task->title) \!= 0);
    printf("    Verified: Clone and Original maintain completely separate heap buffers\!\\n\\n");

    // 4. Teardown and cleanup
    printf("[3] Dequeuing and Freeing Tasks...\\n");
    while (\!list_empty(\&task_queue)) {
        ListNode *node \= task_queue.next;
        list_del(node);
        Task *task \= container_of(node, Task, queue_hook);
        task_destroy(task);
    }

    task_destroy(cloned_task);
    printf("All task queue allocations cleanly freed with 0 leaks\!\\n");

    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Shallow Return & Alias Double-Free Flaw
Examine the following faulty profile management function:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int user_id;
    char *auth_token;
} Session;

// BUGGY IMPLEMENTATION
Session duplicate_session_faulty(Session s) {
    // BUG 1: Parameter 's' was passed by value (shallow copy of struct)
    // BUG 2: Returning 's' directly performs another shallow copy.
    // 's.auth_token' still points to the original caller's heap buffer\!
    return s;
}

void test_sessions(void) {
    Session original;
    original.user_id \= 42;
    original.auth_token \= strdup("secret_token_xyz_9988");

    Session clone \= duplicate_session_faulty(original);

    // Caller cleans up original session
    free(original.auth_token);

    // Caller later cleans up cloned session:
    // FATAL BUG: auth_token is already freed \-> DOUBLE-FREE ABORT\!
    free(clone.auth_token);
}
```

### Analysis of Vulnerabilities:
1. **Pass-by-Value Shallow Copy:** When a struct containing pointer members is passed by value or returned by value without explicit cloning, the pointers are copied bit-for-bit.
2. **Hidden Aliasing:** Both `original.auth_token` and `clone.auth_token` point to the same 22-byte block in heap RAM. Modifying or freeing through one pointer corrupts or invalidates the other.

### Defensive Fix:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int user_id;
    char *auth_token;
} SafeSession;

// Defensive Deep Clone Constructor
bool session_clone_safe(const SafeSession *src, SafeSession *out_dest) {
    if (\!src || \!out_dest) return false;

    out_dest->user_id \= src->user_id;

    if (src->auth_token) {
        out_dest->auth_token \= strdup(src->auth_token);
        if (\!out_dest->auth_token) {
            return false; // Out of Memory
        }
    } else {
        out_dest->auth_token \= NULL;
    }

    return true;
}

void session_destroy(SafeSession *s) {
    if (\!s) return;
    if (s->auth_token) {
        free(s->auth_token);
        s->auth_token \= NULL; // Prevent dangling pointer
    }
    s->user_id \= 0;
}
```
