---
tags:
  - c
  - hash-tables
  - data-structures
  - collision-resolution
  - fnv1a-hash
  - robin-hood-hashing
date: 2026-09-12
day: 21
---

# Day 21: High-Performance Hash Tables, Collision Resolution & Robin Hood Probing

---

## 1. Quick Reference & Cheat Sheet

### Core Concepts & Mechanics

- **Hash Function:** Maps an arbitrary key (e.g. string) to a uniform 32-bit or 64-bit integer.

- **Bucket Index Mapping:** For power-of-two capacity \$C = 2^k\$: \$\$\\text{index} = \\text{hash} \\ & \\ (C - 1)\$\$

- **Load Factor (\$\\alpha\$):** Ratio of stored elements to total capacity (\$\\alpha = \\frac{N}{C}\$).

  - When \$\\alpha \\ge 0.70\$, the table should allocate a new array of size \$2C\$ and rehash all active keys.

### Collision Resolution Comparison

-------------------------------------------------------------------------- Strategy       Memory Layout  Cache Locality Memory         Worst-Case Overhead       Search -------------- -------------- -------------- -------------- -------------- **Separate     Array of       **Poor         High (8--16    \$O(N)\$ (Long Chaining**     linked-list    (Pointer       bytes per      degenerate head pointers  chasing        node + list    lists) scattered in   pointers) heap)**

**Linear       Single flat    **Excellent    Zero pointer   \$O(N)\$ Probing**      contiguous     (Sequential    overhead       (Primary array          cache line                    clustering fetches)**                    causes long runs)

**Robin Hood   Single flat    **Excellent    1--2 bytes per \$O(1)\$ Hashing**      contiguous     (Sequential    entry for      amortized with array + Probe  cache line     Probe Sequence extremely low Count          fetches)**     Length         variance --------------------------------------------------------------------------

### The FNV-1a Hash Function (32-Bit)

Fast, compact, and exhibits excellent bit-dispersion (avalanche effect):#define FNV_OFFSET_BASIS 2166136261U

##define FNV_PRIME 16777619U

uint32_t hash_fnv1a(const char *str) {

uint32_t hash = FNV_OFFSET_BASIS;

while (*str) {

hash ^= (uint8_t)*str++;

hash *= FNV_PRIME;

}

return hash;

}

## 2. In-Depth Theory & Low-Level Mechanics

### A. Why Open Addressing Beats Separate Chaining on Modern CPUs

In traditional textbooks, **Separate Chaining** is favored because insertion is trivial (push_front to linked list) and deletion does not require tombstones. However, on modern computer hardware:

1.  **L1/L2/L3 Cache Lines:** The CPU fetches 64 bytes at a time into cache.

2.  **The Cache Miss Penalty:** Traversing a linked list forces the CPU to wait ~50--200 CPU cycles per pointer dereference because nodes are randomly scattered across heap RAM.

3.  **Contiguous Scanning:** In open addressing (Linear Probing / Robin Hood), all buckets reside in a single contiguous array. Probing adjacent slots hits the exact same 64-byte L1 cache line, making lookups up to **5x faster** than linked lists despite theoretical collisions!

### B. The Robin Hood Hashing Invariant

Standard linear probing suffers from **Primary Clustering**: long contiguous runs of occupied slots merge together, causing search times to degrade drastically for unlucky keys.

**Robin Hood Hashing** solves this by equalizing the Probe Sequence Length (PSL)---the distance in slots between an item's current position and its ideal hash bucket:*"Steal from the rich (short PSL) and give to the poor (long PSL)."*

#### Insertion Algorithm:

1.  Compute ideal bucket index: idx = hash & mask. Initial probe length: psl = 0.

2.  Step forward linearly through the table:

    - **If slot is empty:** Place the key/value and psl here. Done!

    - **If slot key matches:** Update existing value. Done!

    - **If occupant's PSL < incoming PSL:**

      - The incoming item has traveled further ("poorer") than the occupant ("richer").

      - **SWAP** the incoming item with the occupant!

      - Continue probing forward to find a new slot for the evicted occupant, incrementing psl on each step.

Robin Hood Invariant Enforcement:

Slot: [0] [1] [2] [3]

Occupant: (A, PSL=0) (B, PSL=1) (C, PSL=0) (Empty)

Incoming: (X, PSL=2)

Step at Slot [2]:

Incoming X has PSL=2. Occupant C has PSL=0.

X is poorer than C (2 > 0) -> SWAP!

Slot [2] becomes X (PSL=2). C is evicted with PSL=0.

Step at Slot [3]:

C advances to Slot [3] with PSL=1. Slot [3] is empty -> Insert C!

#### Early-Termination Search Advantage:

When searching for a key, if you encounter an occupant whose occupant_psl < current_search_psl, the key is guaranteed not to exist in the table. You can terminate the search immediately without scanning to the next empty slot!

### C. Deletion Without Tombstones (Backward Shift Deletion)

Traditional linear probing marks deleted slots with **Tombstones** (DELETED), which wastes capacity and degrades future lookups.

Robin Hood hashing supports **Backward Shift Deletion**:

1.  Remove the target element.

2.  Shift subsequent elements backward by 1 slot as long as their PSL > 0.

3.  Stop shifting when you encounter an empty slot or an element with PSL == 0 (which is already in its ideal bucket).

4.  Zero out the final vacated slot. This completely eliminates tombstones and leaves the table in an optimally packed state!

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: High-Performance Robin Hood Hash Table with FNV-1a & Dynamic Resizing (robin_hash)

#### Objective

Build an open-addressing Hash Table in C that implements:

1.  32-bit FNV-1a string hashing with \$O(1)\$ power-of-two bitwise indexing.

2.  Robin Hood probe-sequence swapping on insertion.

3.  Early search termination on lookup.

4.  Backward-shift deletion (zero tombstones).

5.  Dynamic \$2\\times\$ resizing when load factor exceeds 70%.

#### Complete Starter Code Implementation

##include <stdio.h>

##include <stdlib.h>

##include <stdint.h>

##include <stdbool.h>

##include <string.h>

##include <assert.h>

##define INITIAL_CAPACITY 8

##define MAX_LOAD_FACTOR 0.70

##define FNV_OFFSET_BASIS 2166136261U

##define FNV_PRIME 16777619U

static uint32_t hash_str(const char *str) {

uint32_t h = FNV_OFFSET_BASIS;

while (*str) {

h ^= (uint8_t)*str++;

h *= FNV_PRIME;

}

return h;

}

typedef struct {

char *key;

void *value;

uint32_t hash;

uint16_t psl; // Probe Sequence Length

bool occupied;

} HashEntry;

typedef struct {

HashEntry *entries;

size_t capacity;

size_t mask;

size_t count;

} HashTable;

HashTable *ht_create(size_t initial_cap) {

// Ensure power of 2

size_t cap = 8;

while (cap < initial_cap) cap *= 2;

HashTable *ht = (HashTable *)malloc(sizeof(HashTable));

ht->entries = (HashEntry *)calloc(cap, sizeof(HashEntry));

ht->capacity = cap;

ht->mask = cap - 1;

ht->count = 0;

return ht;

}

void ht_free(HashTable *ht) {

if (!ht) return;

for (size_t i = 0; i < ht->capacity; i++) {

if (ht->entries[i].occupied) {

free(ht->entries[i].key);

}

}

free(ht->entries);

free(ht);

}

static bool ht_insert_internal(HashEntry *entries, size_t mask, size_t capacity,

HashEntry incoming) {

size_t idx = incoming.hash & mask;

incoming.psl = 0;

while (true) {

if (!entries[idx].occupied) {

entries[idx] = incoming;

return true;

}

// Key match: update value

if (entries[idx].hash == incoming.hash && strcmp(entries[idx].key, incoming.key) == 0) {

free(entries[idx].key);

entries[idx] = incoming;

return false; // Updated existing key, count did not increase

}

// Robin Hood Swap: Steal from rich, give to poor

if (incoming.psl > entries[idx].psl) {

HashEntry temp = entries[idx];

entries[idx] = incoming;

incoming = temp;

}

idx = (idx + 1) & mask;

incoming.psl++;

}

}

static void ht_resize(HashTable *ht) {

size_t new_cap = ht->capacity * 2;

size_t new_mask = new_cap - 1;

HashEntry *new_entries = (HashEntry *)calloc(new_cap, sizeof(HashEntry));

for (size_t i = 0; i < ht->capacity; i++) {

if (ht->entries[i].occupied) {

ht_insert_internal(new_entries, new_mask, new_cap, ht->entries[i]);

}

}

free(ht->entries);

ht->entries = new_entries;

ht->capacity = new_cap;

ht->mask = new_mask;

}

bool ht_insert(HashTable *ht, const char *key, void *value) {

if ((double)(ht->count + 1) / (double)ht->capacity > MAX_LOAD_FACTOR) {

ht_resize(ht);

}

HashEntry entry;

entry.key = strdup(key);

entry.value = value;

entry.hash = hash_str(key);

entry.psl = 0;

entry.occupied = true;

bool is_new = ht_insert_internal(ht->entries, ht->mask, ht->capacity, entry);

if (is_new) {

ht->count++;

}

return is_new;

}

void *ht_get(const HashTable *ht, const char *key) {

if (!ht || ht->count == 0) return NULL;

uint32_t h = hash_str(key);

size_t idx = h & ht->mask;

uint16_t current_psl = 0;

while (true) {

if (!ht->entries[idx].occupied) {

return NULL; // Empty slot: key doesn't exist

}

// Early Termination Invariant:

// If current search PSL exceeds the occupant's PSL, the key CANNOT exist!

if (current_psl > ht->entries[idx].psl) {

return NULL;

}

if (ht->entries[idx].hash == h && strcmp(ht->entries[idx].key, key) == 0) {

return ht->entries[idx].value;

}

idx = (idx + 1) & ht->mask;

current_psl++;

}

}

// Backward Shift Deletion (Zero Tombstones!)

bool ht_delete(HashTable *ht, const char *key) {

if (!ht || ht->count == 0) return false;

uint32_t h = hash_str(key);

size_t idx = h & ht->mask;

uint16_t current_psl = 0;

while (true) {

if (!ht->entries[idx].occupied || current_psl > ht->entries[idx].psl) {

return false; // Key not found

}

if (ht->entries[idx].hash == h && strcmp(ht->entries[idx].key, key) == 0) {

// Found item to delete

free(ht->entries[idx].key);

break;

}

idx = (idx + 1) & ht->mask;

current_psl++;

}

// Shift subsequent entries backward until an entry with PSL==0 or empty slot is reached

size_t curr = idx;

size_t next = (curr + 1) & ht->mask;

while (ht->entries[next].occupied && ht->entries[next].psl > 0) {

ht->entries[curr] = ht->entries[next];

ht->entries[curr].psl--; // Decrement PSL as it moved 1 slot closer to ideal

curr = next;

next = (curr + 1) & ht->mask;

}

// Mark last vacated slot empty

ht->entries[curr].occupied = false;

ht->entries[curr].key = NULL;

ht->entries[curr].value = NULL;

ht->entries[curr].psl = 0;

ht->count--;

return true;

}

int main(void) {

printf("====================================================================\\n");

printf(" DEMONSTRATING ROBIN HOOD HASH TABLE WITH ZERO-TOMBSTONE DELETION \\n");

printf("====================================================================\\n\\n");

HashTable *ht = ht_create(8);

printf("[1] Inserting Key-Value Pairs\...\\n");

ht_insert(ht, "alpha", (void *)101);

ht_insert(ht, "bravo", (void *)102);

ht_insert(ht, "charlie", (void *)103);

ht_insert(ht, "delta", (void *)104);

ht_insert(ht, "echo", (void *)105);

ht_insert(ht, "foxtrot", (void *)106);

printf(" Inserted 6 elements. Table Capacity: %zu, Count: %zu (Load: %.2f)\\n\\n",

ht->capacity, ht->count, (double)ht->count / (double)ht->capacity);

printf("[2] Querying Values:\\n");

printf(" Value for 'alpha': %td\\n", (intptr_t)ht_get(ht, "alpha"));

printf(" Value for 'delta': %td\\n", (intptr_t)ht_get(ht, "delta"));

printf(" Value for 'foxtrot': %td\\n", (intptr_t)ht_get(ht, "foxtrot"));

printf(" Value for 'zulu': %s\\n\\n", ht_get(ht, "zulu") ? "Found" : "NULL (Correct)");

assert((intptr_t)ht_get(ht, "alpha") == 101);

assert((intptr_t)ht_get(ht, "echo") == 105);

printf("[3] Deleting Key 'bravo' (testing backward shift)\...\\n");

bool deleted = ht_delete(ht, "bravo");

assert(deleted);

printf(" 'bravo' deleted. Lookup 'bravo' => %s\\n", ht_get(ht, "bravo") ? "Found" : "NULL");

assert(ht_get(ht, "bravo") == NULL);

assert((intptr_t)ht_get(ht, "charlie") == 103);

assert((intptr_t)ht_get(ht, "foxtrot") == 106);

printf(" Verified: Subsequent elements shifted backward and accessible!\\n\\n");

ht_free(ht);

printf("Hash Table cleanly destroyed with zero memory leaks!\\n");

return 0;

}

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Tombstone Accumulation & Infinite Lookup Loop Bug

Examine the following faulty linear-probing hash table lookup and insertion:#include <stdio.h>

##include <stdlib.h>

##include <string.h>

##define TOMBSTONE ((char *)-1)

typedef struct {

char **keys;

int *values;

size_t capacity;

size_t active_count; // Tracks only live keys!

} BuggyTable;

// BUGGY IMPLEMENTATION

int *table_find_faulty(BuggyTable *t, const char *key, size_t hash) {

size_t idx = hash % t->capacity;

// VULNERABILITY 1: Infinite Loop on Full Table!

while (t->keys[idx] != NULL) {

if (t->keys[idx] != TOMBSTONE && strcmp(t->keys[idx], key) == 0) {

return &t->values[idx];

}

idx = (idx + 1) % t->capacity;

}

return NULL;

}

### Analysis of Vulnerabilities:

1.  **Infinite Search Loop:** Linear probing relies on encountering NULL (empty bucket) to know when an item does not exist. If insertions and deletions fill all slots with either live keys or tombstones, looking up a missing key loops indefinitely around the ring buffer at 100% CPU utilization.

2.  **Tombstone Capacity Saturation:** Tracking only active_count ignores tombstones. If 70% of slots are tombstones and 20% are live, the load factor appears to be 0.20, but 90% of slots are occupied, causing severe clustering and performance collapse.

### Defensive Fix:

##include <stdio.h>

##include <stdlib.h>

##include <string.h>

##include <stdbool.h>

##define TOMBSTONE_PTR ((char *)0x1)

typedef struct {

char **keys;

int *values;

size_t capacity;

size_t mask;

size_t live_count;

size_t occupied_count; // Tracks live keys + tombstones!

} SafeLinearTable;

int *table_find_safe(const SafeLinearTable *t, const char *key, uint32_t hash) {

if (!t || t->live_count == 0) return NULL;

size_t idx = hash & t->mask;

size_t probes = 0;

// Defensive Fix: Bound search by capacity to strictly guarantee no infinite loops

while (t->keys[idx] != NULL && probes < t->capacity) {

if (t->keys[idx] != TOMBSTONE_PTR) {

if (strcmp(t->keys[idx], key) == 0) {

return &t->values[idx];

}

}

idx = (idx + 1) & t->mask;

probes++;

}

return NULL;

}
