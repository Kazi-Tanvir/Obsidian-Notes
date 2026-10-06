---
tags:
  - c
  - data-structures
  - linked-list
  - sentinel-nodes
  - intrusive-list
  - linux-kernel
date: 2026-09-11
day: 20
---

# Day 20: Generic Doubly Linked Lists & Sentinel Node Patterns

---

## 1. Quick Reference & Cheat Sheet

### The Sentinel Node Advantage

In a traditional linked list, every insertion and deletion requires branching conditional checks to handle edge cases:

- Is the list currently empty (head == NULL)?

- Are we inserting at the front or the back?

- Are we deleting the very first or very last element?

A **Circular Doubly Linked List with a Dummy Sentinel Node** completely eliminates all edge cases.t Empty List (Sentinel points to itself):
┌──────────────────────┐
▼ │
┌──────┐ │
│ Head │ ─── next/prev ───┘
└──────┘

Populated List with 2 Elements:
┌──────┐ next ┌──────┐ next ┌──────┐ next
│ Head │ ─────► │ Elm1 │ ─────► │ Elm2 │ ─────┐
│ (Dum)│ ◄───── │ │ ◄───── │ │ ◄───┘
└──────┘ prev └──────┘ prev └──────┘ prev
▲ │
└─────────────────────────────────────────┘

#### Core Operations (Zero Branching, \$O(1)\$ Time)

```c

// Empty condition:

bool is_empty = (head->next == head);

// Insert 'new_node' between 'prev' and 'next':

new_node->next = next;

new_node->prev = prev;

prev->next = new_node;

next->prev = new_node;

// Delete 'entry' from list:

entry->prev->next = entry->next;

entry->next->prev = entry->prev;

Notice that **not a single if statement** is required to insert, remove,
or splice nodes!

# 2. In-Depth Theory & Low-Level Mechanics

## A. The Linux Kernel list_head Architecture

Rather than writing separate linked-list implementations for processes,
network sockets, file buffers, and timers, the Linux kernel uses an
**intrusive** struct:struct list_head {

struct list_head *next;

struct list_head *prev;

};

By embedding struct list_head directly inside any parent data structure,
that structure instantly becomes a doubly linked list node without
requiring dedicated memory wrappers or generic void* pointer
indirection.

### Retrieving the Enclosing Struct (container_of):

#define list_entry(ptr, type, member) 

((type *)((char *)(ptr) - offsetof(type, member)))

## B. Branch Elimination & CPU Instruction Pipelines

On modern superscalar processors, conditional branch instructions (je,
jne, jg) are evaluated by speculative execution branch predictors.

- If a branch mispredicts, the CPU must flush its execution pipeline,
  incurring a **15--20 cycle latency penalty**.

- Traditional linked-list insertions execute 2 to 4 branches per call:if
  (head == NULL) { head = node; }

> else { node->next = head; head->prev = node; head = node; }

- A circular sentinel list executes **zero conditional branches**. The
  machine code is purely linear register loads and stores (mov [rax],
  rdx), allowing the CPU pipeline to run at peak throughput.

## C. The Iteration-Deletion Race (Why list_for_each_safe is Mandatory)

Consider traversing a list to free elements:// FATAL BUG: Use-After-Free

struct list_head *curr;

for (curr = head->next; curr != head; curr = curr->next) {

MyNode *item = list_entry(curr, MyNode, link);

free(item); // Memory at 'curr' is now deallocated!

// Next loop iteration: 'curr = curr->next' reads deallocated heap
memory!

}

### The Safe Two-Pointer Solution:

Cache the pointer to the next element **before** entering the loop
body:#define list_for_each_safe(pos, n, head) 

for (pos = (head)->next, n = pos->next; pos != (head); 

pos = n, n = pos->next)

# 3. Thoughtful Mini-Project (~1 Hour Scope)

## Project Title: Kernel-Style Intrusive Doubly Linked List with Safe Iteration & In-Place Merge Sort (klist_engine)

### Objective

Build a circular doubly linked list library in C that:

1.  Implements circular sentinel manipulation primitives with zero
    branching (list_init, list_add, list_add_tail, list_del,
    list_splice).

2.  Provides the safe iteration macro list_for_each_safe.

3.  Implements an **in-place, non-recursive, stable \$O(N \\log N)\$
    Merge Sort** directly over intrusive list_head nodes.

4.  Manages an active process priority table, sorts tasks, and allows
    deleting tasks during iteration without crashes.

### Complete Starter Code Implementation

#include <stdio.h>

#include <stdlib.h>

#include <stdint.h>

#include <stdbool.h>

#include <string.h>

#include <stddef.h>

#include <assert.h>

/*
=========================================================================
*/

/* 1. INTRUSIVE SENTINEL LIST ENGINE */

/*
=========================================================================
*/

struct list_head {

struct list_head *next;

struct list_head *prev;

};

#define LIST_HEAD_INIT(name) { &(name), &(name) }

#define LIST_HEAD(name) 

struct list_head name = LIST_HEAD_INIT(name)

static inline void INIT_LIST_HEAD(struct list_head *list) {

list->next = list;

list->prev = list;

}

#define list_entry(ptr, type, member) 

((type *)((char *)(ptr) - offsetof(type, member)))

#define list_for_each(pos, head) 

for (pos = (head)->next; pos != (head); pos = pos->next)

#define list_for_each_safe(pos, n, head) 

for (pos = (head)->next, n = pos->next; pos != (head); 

pos = n, n = pos->next)

// Internal insertion helper (Zero branches!)

static inline void __list_add(struct list_head *new_node,

struct list_head *prev,

struct list_head *next) {

next->prev = new_node;

new_node->next = next;

new_node->prev = prev;

prev->next = new_node;

}

// Add after head (Stack / LIFO order)

static inline void list_add(struct list_head *new_node, struct
list_head *head) {

__list_add(new_node, head, head->next);

}

// Add to tail (Queue / FIFO order)

static inline void list_add_tail(struct list_head *new_node, struct
list_head *head) {

__list_add(new_node, head->prev, head);

}

// Internal delete helper

static inline void __list_del(struct list_head *prev, struct
list_head *next) {

next->prev = prev;

prev->next = next;

}

static inline void list_del(struct list_head *entry) {

__list_del(entry->prev, entry->next);

entry->next = NULL;

entry->prev = NULL;

}

static inline bool list_empty(const struct list_head *head) {

return head->next == head;

}

// Splice an entire list into another

static inline void list_splice_tail(struct list_head *list, struct
list_head *head) {

if (!list_empty(list)) {

struct list_head *first = list->next;

struct list_head *last = list->prev;

struct list_head *at = head->prev;

first->prev = at;

at->next = first;

last->next = head;

head->prev = last;

INIT_LIST_HEAD(list); // Empty original list

}

}

/*
=========================================================================
*/

/* 2. IN-PLACE INTRUSIVE MERGE SORT */

/*
=========================================================================
*/

typedef int (*list_cmp_fn)(const struct list_head *a, const struct
list_head *b);

// Merge two sorted linear null-terminated lists

static struct list_head *merge_nodes(struct list_head *a, struct
list_head *b, list_cmp_fn cmp) {

struct list_head dummy;

struct list_head *tail = &dummy;

while (a && b) {

if (cmp(a, b) <= 0) {

tail->next = a;

a = a->next;

} else {

tail->next = b;

b = b->next;

}

tail = tail->next;

}

tail->next = a ? a : b;

return dummy.next;

}

// Stable In-Place Merge Sort on Circular Doubly Linked List (O(N log
N))

void list_sort(struct list_head *head, list_cmp_fn cmp) {

if (list_empty(head) || head->next->next == head) {

|---|

}

// Step 1: Break circular link into linear null-terminated list

head->prev->next = NULL;

struct list_head *list = head->next;

// Step 2: Bottom-Up Non-Recursive Merge Sort using sublist array (max
2^64 elements)

struct list_head *part[64];

memset(part, 0, sizeof(part));

while (list) {

struct list_head *curr = list;

list = list->next;

curr->next = NULL;

int i = 0;

while (part[i]) {

curr = merge_nodes(part[i], curr, cmp);

part[i] = NULL;

i++;

}

part[i] = curr;

}

// Merge remaining partitions

struct list_head *result = NULL;

for (int i = 0; i < 64; i++) {

if (part[i]) {

result = merge_nodes(part[i], result, cmp);

}

}

// Step 3: Reconstruct circular doubly linked invariants

struct list_head *prev = head;

struct list_head *curr = result;

while (curr) {

prev->next = curr;

curr->prev = prev;

prev = curr;

curr = curr->next;

}

prev->next = head;

head->prev = prev;

}

/*
=========================================================================
*/

/* 3. DRIVER APPLICATION */

/*
=========================================================================
*/

typedef struct Process {

uint32_t pid;

int priority; // Lower integer = Higher priority

uint32_t cpu_time_ms;

struct list_head link;

} Process;

int compare_process_priority(const struct list_head *a, const struct
list_head *b) {

const Process *p1 = list_entry(a, Process, link);

const Process *p2 = list_entry(b, Process, link);

return p1->priority - p2->priority;

}

Process *process_create(uint32_t pid, int priority, uint32_t cpu_time)
{

Process *p = (Process *)malloc(sizeof(Process));

p->pid = pid;

p->priority = priority;

p->cpu_time_ms = cpu_time;

p->link.next = NULL;

p->link.prev = NULL;

return p;

}

int main(void) {

printf("====================================================================\\n");

printf(" DEMONSTRATING INTRUSIVE SENTINEL LINKED LIST & IN-PLACE MERGE
SORT \\n");

printf("====================================================================\\n\\n");

LIST_HEAD(proc_queue);

// 1. Enqueue processes

list_add_tail(&process_create(1001, 10, 250)->link, &proc_queue);

list_add_tail(&process_create(1002, 2, 120)->link, &proc_queue);

list_add_tail(&process_create(1003, 20, 80)->link, &proc_queue);

list_add_tail(&process_create(1004, 1, 45)->link, &proc_queue);

list_add_tail(&process_create(1005, 5, 310)->link, &proc_queue);

printf("[1] Initial Process Queue (Unsorted):\\n");

struct list_head *pos;

list_for_each(pos, &proc_queue) {

Process *p = list_entry(pos, Process, link);

printf(" PID: %4u | Priority: %2d | CPU Time: %3u ms\\n",

p->pid, p->priority, p->cpu_time_ms);

}

// 2. Sort queue in-place

printf("\\n[2] Sorting Queue In-Place by Priority (O(N log
N))\...\\n");

list_sort(&proc_queue, compare_process_priority);

printf(" Sorted Queue Result:\\n");

list_for_each(pos, &proc_queue) {

Process *p = list_entry(pos, Process, link);

printf(" PID: %4u | Priority: %2d | CPU Time: %3u ms\\n",

p->pid, p->priority, p->cpu_time_ms);

}

// 3. Safe Deletion during Iteration

printf("\\n[3] Purging High-Priority Processes (Priority <= 5)
during Safe Traversal:\\n");

struct list_head *n;

list_for_each_safe(pos, n, &proc_queue) {

Process *p = list_entry(pos, Process, link);

if (p->priority <= 5) {

printf(" Retiring PID: %u (Priority %d)\\n", p->pid, p->priority);

list_del(&p->link);

free(p);

}

}

printf("\\n[4] Remaining Queue After Purge:\\n");

list_for_each(pos, &proc_queue) {

Process *p = list_entry(pos, Process, link);

printf(" PID: %4u | Priority: %2d\\n", p->pid, p->priority);

}

// Clean up remaining nodes

list_for_each_safe(pos, n, &proc_queue) {

Process *p = list_entry(pos, Process, link);

list_del(&p->link);

free(p);

}

assert(list_empty(&proc_queue));

printf("\\nAll nodes cleanly deleted with zero memory leaks!\\n");

return 0;

}

# 4. Error Handling & Defensive Programming Challenge

## Scenario: The Dangling Next Pointer in Unsafe Node Deletion

Examine the following buggy queue purge function:#include <stdio.h>

#include <stdlib.h>

struct Node {

int id;

struct Node *next;

struct Node *prev;

};

// BUGGY IMPLEMENTATION

void purge_inactive_nodes_faulty(struct Node *head) {

// VULNERABILITY: Use-After-Free during list traversal!

// 'curr' is freed inside the loop body.

// The loop progression expression 'curr = curr->next' reads
deallocated memory!

for (struct Node *curr = head->next; curr != head; curr = curr->next)
{

if (curr->id < 0) {

curr->prev->next = curr->next;

curr->next->prev = curr->prev;

free(curr); // CRASH: Next iteration dereferences curr->next on a freed
pointer!

}

}

}

## Analysis of Vulnerabilities:

1.  **Use-After-Free in Loop Progression:** Once free(curr) executes,
    the operating system's heap allocator reclaims or poisons the
    memory chunk. When the for statement computes curr = curr->next, it
    dereferences curr, reading arbitrary garbage or triggering an
    immediate segmentation fault (SIGSEGV).

2.  **Dangling Pointers on Deleted Node:** Leaving curr->next and
    curr->prev pointing to active nodes after deletion increases the
    risk of double-unlinking.

## Defensive Fix (Pre-Caching & Node Poisoning):

#include <stdio.h>

#include <stdlib.h>

#include <stdbool.h>

#define POISON_POINTER_1 ((struct SafeNode *)0xDEADBEEF00000001ULL)

#define POISON_POINTER_2 ((struct SafeNode *)0xDEADBEEF00000002ULL)

struct SafeNode {

int id;

struct SafeNode *next;

struct SafeNode *prev;

};

void purge_inactive_nodes_safe(struct SafeNode *head) {

if (!head) return;

// Defensive Fix 1: Cache 'next' pointer BEFORE the loop body executes

struct SafeNode *curr = head->next;

struct SafeNode *next_cache = curr->next;

while (curr != head) {

if (curr->id < 0) {

// Unlink node

curr->prev->next = curr->next;

curr->next->prev = curr->prev;

// Defensive Fix 2: Poison pointers to trap any subsequent invalid
accesses

curr->next = POISON_POINTER_1;

curr->prev = POISON_POINTER_2;

free(curr);

}

// Safely advance using cached next pointer

curr = next_cache;

next_cache = curr->next;

}

}
