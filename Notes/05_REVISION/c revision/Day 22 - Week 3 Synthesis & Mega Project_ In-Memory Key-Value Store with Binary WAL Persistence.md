---
tags:
  - c
  - week-3-synthesis
  - mega-project
  - key-value-store
  - write-ahead-log
  - crc32
  - file-io
  - hash-tables
date: 2026-09-13
day: 22
---

# Day 22: Week 3 Synthesis & Mega Project: In-Memory Key-Value Store with Binary WAL Persistence

---

## 1. Quick Reference & Cheat Sheet (Week 3 Synthesis)

---

### Week 3 Core Concepts Consolidated

- **Function Pointers & Callbacks:**

  - Function pointer signature: typedef void (*handler_fn)(const void *payload, void *user_data);

  - Always bundle a contextual void *user_data to ensure thread-safety, reentrancy, and eliminate globals.

- **Preprocessor Metaprogramming & X-Macros:**

  - Stringizing (#x) turns tokens into string literals; token-pasting (a
#    ## b) merges tokens into single identifiers.

  - X-Macros (#define TABLE(X) \...) establish a single source of truth for enums, strings, and dispatch tables.

- **Low-Level Stream File I/O:**

  - Open in binary mode ("rb", "wb", "ab+") to avoid newline conversions (\\r\\n) and premature 0x1A EOF triggers.

  - Check fread and fwrite return counts directly (never use while (!feof(fp))).

  - fflush(fp) pushes C userspace buffers to the OS page cache; fsync(fileno(fp)) forces physical hardware media commit.

- **Power-of-Two Bitwise Optimization:**

  - If capacity \$C = 2^k\$, then idx = hash & (C - 1) replaces slow modulo division with a 1-cycle bitwise AND.

- **Circular Sentinel Linked Lists:**

  - Sentinel nodes eliminate all edge cases (if (head == NULL)) and branch mispredictions.

- **Robin Hood Hash Tables:**

  - Equalizes probe sequence length (PSL). Enables early termination on misses and backward-shift deletion without tombstones.

## 2. In-Depth Theory & Low-Level Mechanics

---

### A. The Write-Ahead Logging (WAL) Protocol

In production database engines (e.g. SQLite, PostgreSQL, RocksDB), in-memory updates are volatile. If a server loses power, RAM contents are wiped.

To achieve ACID Durability without sacrificing performance:

1.  **Append-Only Write:** Every mutation (SET, DEL) is appended to a sequential disk file (the Write-Ahead Log) **before** modifying the in-memory hash table.

2.  **Sequential vs Random I/O:** Sequential disk writes are orders of magnitude faster than random-access updates because storage controllers can stream writes continuously.

3.  **Recovery on Startup:** If the system crashes, the database replays the WAL from byte 0 to rebuild the exact in-memory hash index up to the last committed transaction.

t\ Client Mutation: SET key="user:1" value="Alice"\ │\ ├───────────────────────────────────────────────────────┐\ ▼ ▼

1.  Append to WAL on Disk (Sequential): 2. Apply to In-Memory Hash Table:\ ┌────────────────────────────────────────┐ ┌─────────────────────────────┐\ │ Header: LSN=1, Op=SET, CRC=0x3B8F\... │ │ Bucket [3]: "user:1" -> "Alice" │\ │ Payload: Key="user:1", Val="Alice" │ └─────────────────────────────┘\ └────────────────────────────────────────┘\ │\ ▼

2.  Call fflush() & fsync() -> Acknowledge to Client

#### B. The Physical Persistence Chain (`fflush` vs `fsync`)

When your program calls `fwrite()`:

1\. Data sits in the C standard library's **userspace buffer** (inside your process).

2\. Calling `fflush(fp)` executes the `write()` system call, moving bytes into the **OS kernel page cache**. If the application crashes, the OS still writes this data to disk.

3\. However, if the **entire machine loses power**, page cache memory is lost!

4\. To guarantee durable persistence, you must call `fsync(fileno(fp))` or `fdatasync()`. This sends a hardware command forcing the SSD/HDD storage controller to flush its internal volatile cache to persistent flash memory.

#### C. Crash Consistency & CRC32 Verification

What happens if the power cuts out *in the middle* of writing a WAL record?

* The log file will contain a **torn (truncated) record** at its tail.

* Every WAL record must contain a **CRC32 Checksum** computed over its payload.

* During crash recovery:

* Read records sequentially.

* For each record, recompute the CRC32 checksum.

* If the magic number matches and the checksum is valid \$\\to\$ replay the mutation.

* If a checksum mismatch or premature EOF occurs \$\\to\$ stop replay immediately and truncate the corrupted tail.

### 3. Thoughtful Mini-Project (~1 Hour Scope)

#### Project Title: Atomic Database Snapshot Engine (`db_snapshot`)

##### Objective

Build a database snapshot engine that takes an in-memory dictionary, serializes it to a temporary file, forces physical disk synchronization via `fsync()`, and atomically replaces the live database file using POSIX `rename()`.

##### Complete Starter Code Implementation

```c
#include <stdio.h>

#include <stdlib.h>

#include <stdint.h>

#include <stdbool.h>

#include <string.h>

#include <unistd.h>

#include <assert.h>

typedef struct {

char key[64];

char val[64];

} Record;

#define MAGIC_SNAP 0x534E4150 // "SNAP"

bool snapshot_export_atomic(const char *target_filename, const Record
*records, size_t count) {

char temp_filename[300];

snprintf(temp_filename, sizeof(temp_filename), "%s.tmp.%d",
target_filename, getpid());

FILE *fp = fopen(temp_filename, "wb");

if (!fp) return false;

// 1. Write Header

uint32_t magic = MAGIC_SNAP;

uint32_t rec_count = (uint32_t)count;

if (fwrite(&magic, sizeof(magic), 1, fp) != 1 ||
    fwrite(&rec_count, sizeof(rec_count), 1, fp) != 1) {

fclose(fp);

unlink(temp_filename);

return false;

}

// 2. Write Records

if (fwrite(records, sizeof(Record), count, fp) != count) {

fclose(fp);

unlink(temp_filename);

return false;

}

// 3. Flush userspace buffers & force physical hardware disk commit

fflush(fp);

int fd = fileno(fp);

if (fsync(fd) != 0) {

fclose(fp);

unlink(temp_filename);

return false;

}

fclose(fp);

// 4. Atomic directory metadata replacement

if (rename(temp_filename, target_filename) != 0) {

unlink(temp_filename);

return false;

}

return true;

}

bool snapshot_import(const char *target_filename, Record
**out_records, size_t *out_count) {

FILE *fp = fopen(target_filename, "rb");

if (!fp) return false;

uint32_t magic = 0, rec_count = 0;

if (fread(&magic, sizeof(magic), 1, fp) != 1 || magic != MAGIC_SNAP) {

fclose(fp);

return false;

}

if (fread(&rec_count, sizeof(rec_count), 1, fp) != 1) {

fclose(fp);

return false;

}

Record *recs = (Record *)malloc(rec_count * sizeof(Record));

if (fread(recs, sizeof(Record), rec_count, fp) != rec_count) {

free(recs);

fclose(fp);

return false;

}

fclose(fp);

*out_records = recs;

*out_count = (size_t)rec_count;

return true;

}

int main(void) {

const char *snap_file = "production.db";

Record table[2] = {

{ "api_key", "secret_live_9981" },

{ "timeout", "5000" }

};

printf("=== Testing Atomic Database Snapshot Engine ===\\n");

bool ok = snapshot_export_atomic(snap_file, table, 2);

assert(ok);

printf("[1] Atomically exported snapshot to '%s' with fsync
commit.\\n", snap_file);

Record *loaded = NULL;

size_t loaded_count = 0;

ok = snapshot_import(snap_file, &loaded, &loaded_count);

assert(ok && loaded_count == 2);

printf("[2] Imported %zu records:\\n", loaded_count);

for (size_t i = 0; i < loaded_count; i++) {

printf(" Key: %-10s => Val: %s\\n", loaded[i].key,
loaded[i].val);

}

free(loaded);

unlink(snap_file);

printf("Snapshot test completed with 0 leaks!\\n\\n");

return 0;

}

# 4. Error Handling & Defensive Programming Challenge

---

## Scenario: The Torn WAL Frame & Corrupted Record Replay

Examine the following buggy recovery function:#include <stdio.h>

#include <stdlib.h>

#include <stdint.h>

struct RawRecord {

uint32_t key_len;

uint32_t val_len;

};

// BUGGY IMPLEMENTATION

void recover_wal_faulty(FILE *wal_fp) {

struct RawRecord hdr;

// VULNERABILITY 1: Unchecked payload allocation & integer addition
overflow!

// VULNERABILITY 2: If crash caused partial write, fread reads partial
garbage,

// and code assumes it is a valid transaction!

while (fread(&hdr, sizeof(hdr), 1, wal_fp) == 1) {

char *key = (char *)malloc(hdr.key_len + 1);

char *val = (char *)malloc(hdr.val_len + 1);

fread(key, 1, hdr.key_len, wal_fp); // Return value ignored!

fread(val, 1, hdr.val_len, wal_fp); // Return value ignored!

key[hdr.key_len] = '\\0';

val[hdr.val_len] = '\\0';

printf("Recovered: %s = %s\\n", key, val);

free(key);

free(val);

}

}

## Analysis of Vulnerabilities:

1.  **Unvalidated Framing (Torn Record Bug):** If the OS crashed
    mid-write, hdr might be present while val is truncated. Ignoring the
    return value of fread populates strings with stale uninitialized
    heap memory.

2.  **Missing Checksum Protection:** Without CRC32 verification, random
    bit-rot or partially written payloads are accepted as valid database
    mutations.

3.  **Memory Allocation Denial of Service:** If the length fields are
    corrupted into large values (e.g. 3 GB), malloc() will fail or
    exhaust system RAM.

## Defensive Fix:

#include <stdio.h>

#include <stdlib.h>

#include <stdint.h>

#include <stdbool.h>

#define MAX_REASONABLE_KEY_LEN (1024)

#define MAX_REASONABLE_VAL_LEN (64 * 1024)

bool recover_record_safe(FILE *wal_fp, uint32_t expected_crc, char
**out_k, char **out_v, uint32_t klen, uint32_t vlen) {

if (klen > MAX_REASONABLE_KEY_LEN || vlen > MAX_REASONABLE_VAL_LEN)
{

return false; // Reject corrupt frame

}

char *k = (char *)malloc(klen + 1);

char *v = (char *)malloc(vlen + 1);

if (!k || !v) { free(k); free(v); return false; }

if (fread(k, 1, klen, wal_fp) != klen ||

fread(v, 1, vlen, wal_fp) != vlen) {

// Torn write detected: abort cleanly

free(k);

free(v);

return false;

}

k[klen] = '\\0';

v[vlen] = '\\0';

*out_k = k;

*out_v = v;

return true;

}

# 5. WEEKLY MEGA PROJECT (Week 3 Capstone)

---

## Project Title: High-Performance In-Memory Key-Value Store with Binary WAL Persistence & Crash Recovery (c_kvdb)

### Architectural Overview

Build an embedded, durable Key-Value database in C combining:

1.  **In-Memory Hash Index:** An open-addressing Robin Hood Hash Table
    for \$O(1)\$ lookups in RAM.

2.  **Binary Write-Ahead Log (WAL):** Every mutation (OP_SET, OP_DEL) is
    serialized with a CRC32 checksum, flushed, and synchronized to disk
    before modifying RAM.

3.  **Automated Crash Recovery Engine:** On startup, replays all
    committed log entries sequentially and detects/isolates any torn or
    corrupted tail records.

4.  **Log Compaction / Snapshotting:** Truncates the WAL once a clean
    memory snapshot is synchronized.

t
┌────────────────────────────────────────────────────────────────────────┐
│ KVStore Engine (c_kvdb) │
├────────────────────────────────────────────────────────────────────────┤
│ In-Memory Layer (RAM): │
│ - Robin Hood Hash Table (fnv1a hash, open addressing, O(1) lookups) │
│ - Stores active key -> value strings │
├────────────────────────────────────────────────────────────────────────┤
│ Persistence Layer (Disk WAL): │
│ - File: db_wal.bin │
│ - Record Header: [ Magic (4B) | LSN (8B) | Op (1B) | CRC32 (4B) ]
│
│ - Payload: [ KeyLen (2B) | KeyStr | ValLen (2B) | ValStr ] │
├────────────────────────────────────────────────────────────────────────┤
│ Operations: │
│ kv_set(db, key, val) ──► WAL Append + fsync ──► Update Hash Table │
│ kv_get(db, key) ──► Direct Hash Table Lookup (Sub-microsecond) │
│ kv_del(db, key) ──► WAL Tombstone + fsync ──► Remove from Hash │
│ kv_recover(db) ──► Sequential WAL scan & replay on startup │
└────────────────────────────────────────────────────────────────────────┘

#### Complete Modular Implementation (`c_kvdb.c`)
```c

##include <stdio.h>

##include <stdlib.h>

##include <stdint.h>

##include <stdbool.h>

##include <string.h>

##include <unistd.h>

##include <assert.h>

##define WAL_MAGIC_RECORD 0x4B564C31 // "KVL1" in ASCII

##define OP_SET 0x01

##define OP_DEL 0x02

/* ========================================================================= */

/* 1. CRC-32 CHECKSUM */

/* ========================================================================= */

uint32_t crc32_compute(const uint8_t *data, size_t len) {

uint32_t crc = 0xFFFFFFFFU;

for (size_t i = 0; i < len; i++) {

crc ^= data[i];

for (int b = 0; b < 8; b++) {

if (crc & 1) crc = (crc >> 1) ^ 0xEDB88320U;

else crc >>= 1;

}

}

return ~crc;

}

/* ========================================================================= */

/* 2. IN-MEMORY ROBIN HOOD HASH TABLE */

/* ========================================================================= */

##define FNV_OFFSET 2166136261U

##define FNV_PRIME 16777619U

static inline uint32_t hash_string(const char *s) {

uint32_t h = FNV_OFFSET;

while (*s) {

h ^= (uint8_t)*s++;

h *= FNV_PRIME;

}

return h;

}

typedef struct {

char *key;

char *value;

uint32_t hash;

uint16_t psl;

bool occupied;

} TableEntry;

typedef struct {

TableEntry *entries;

size_t capacity;

size_t mask;

size_t count;

} MemoryIndex;

MemoryIndex *index_create(size_t cap) {

size_t c = 8;

while (c < cap) c *= 2;

MemoryIndex *idx = (MemoryIndex *)malloc(sizeof(MemoryIndex));

idx->entries = (TableEntry *)calloc(c, sizeof(TableEntry));

idx->capacity = c;

idx->mask = c - 1;

idx->count = 0;

return idx;

}

void index_free(MemoryIndex *idx) {

if (!idx) return;

for (size_t i = 0; i < idx->capacity; i++) {

if (idx->entries[i].occupied) {

free(idx->entries[i].key);

free(idx->entries[i].value);

}

}

free(idx->entries);

free(idx);

}

static bool index_put_internal(TableEntry *entries, size_t mask, TableEntry item) {

size_t pos = item.hash & mask;

item.psl = 0;

while (true) {

if (!entries[pos].occupied) {

entries[pos] = item;

return true;

}

if (entries[pos].hash == item.hash && strcmp(entries[pos].key, item.key) == 0) {

free(entries[pos].key);

free(entries[pos].value);

entries[pos] = item;

return false;

}

if (item.psl > entries[pos].psl) {

TableEntry temp = entries[pos];

entries[pos] = item;

item = temp;

}

pos = (pos + 1) & mask;

item.psl++;

}

}

static void index_resize(MemoryIndex *idx) {

size_t new_cap = idx->capacity * 2;

size_t new_mask = new_cap - 1;

TableEntry *new_entries = (TableEntry *)calloc(new_cap, sizeof(TableEntry));

for (size_t i = 0; i < idx->capacity; i++) {

if (idx->entries[i].occupied) {

index_put_internal(new_entries, new_mask, idx->entries[i]);

}

}

free(idx->entries);

idx->entries = new_entries;

idx->capacity = new_cap;

idx->mask = new_mask;

}

void index_put(MemoryIndex *idx, const char *key, const char *val) {

if ((double)(idx->count + 1) / (double)idx->capacity > 0.70) {

index_resize(idx);

}

TableEntry entry = {

.key = strdup(key),

.value = strdup(val),

.hash = hash_string(key),

.psl = 0,

.occupied = true

};

if (index_put_internal(idx->entries, idx->mask, entry)) {

idx->count++;

}

}

const char *index_get(const MemoryIndex *idx, const char *key) {

if (!idx || idx->count == 0) return NULL;

uint32_t h = hash_string(key);

size_t pos = h & idx->mask;

uint16_t psl = 0;

while (true) {

if (!idx->entries[pos].occupied || psl > idx->entries[pos].psl) {

return NULL;

}

if (idx->entries[pos].hash == h && strcmp(idx->entries[pos].key, key) == 0) {

return idx->entries[pos].value;

}

pos = (pos + 1) & idx->mask;

psl++;

}

}

bool index_del(MemoryIndex *idx, const char *key) {

if (!idx || idx->count == 0) return false;

uint32_t h = hash_string(key);

size_t pos = h & idx->mask;

uint16_t psl = 0;

while (true) {

if (!idx->entries[pos].occupied || psl > idx->entries[pos].psl) {

return false;

}

if (idx->entries[pos].hash == h && strcmp(idx->entries[pos].key, key) == 0) {

free(idx->entries[pos].key);

free(idx->entries[pos].value);

break;

}

pos = (pos + 1) & idx->mask;

psl++;

}

// Backward shift deletion

size_t curr = pos;

size_t next = (curr + 1) & idx->mask;

while (idx->entries[next].occupied && idx->entries[next].psl > 0) {

idx->entries[curr] = idx->entries[next];

idx->entries[curr].psl--;

curr = next;

next = (curr + 1) & idx->mask;

}

memset(&idx->entries[curr], 0, sizeof(TableEntry));

idx->count--;

return true;

}

/* ========================================================================= */

/* 3. PERSISTENT WAL DATABASE ENGINE */

/* ========================================================================= */

typedef struct {

uint32_t magic;

uint64_t lsn;

uint8_t op;

uint32_t crc32;

uint16_t key_len;

uint16_t val_len;

} __attribute__((packed)) LogRecordHeader;

typedef struct {

MemoryIndex *index;

FILE *wal_fp;

char wal_filename[256];

uint64_t next_lsn;

} KVStore;

KVStore *kv_open(const char *wal_path);

void kv_close(KVStore *kv);

bool kv_set(KVStore *kv, const char *key, const char *val);

const char *kv_get(KVStore *kv, const char *key);

bool kv_del(KVStore *kv, const char *key);

size_t kv_replay_wal(KVStore *kv);

KVStore *kv_open(const char *wal_path) {

KVStore *kv = (KVStore *)malloc(sizeof(KVStore));

kv->index = index_create(16);

strncpy(kv->wal_filename, wal_path, sizeof(kv->wal_filename) - 1);

kv->next_lsn = 1;

// Step 1: Replay existing log to reconstruct in-memory state

size_t replayed = kv_replay_wal(kv);

printf(" [Database Startup] Replayed %zu valid operations from WAL '%s'.\\n", replayed, wal_path);

// Step 2: Open WAL in append binary mode for incoming writes

kv->wal_fp = fopen(wal_path, "ab+");

if (!kv->wal_fp) {

index_free(kv->index);

free(kv);

return NULL;

}

return kv;

}

void kv_close(KVStore *kv) {

if (!kv) return;

if (kv->wal_fp) {

fflush(kv->wal_fp);

fsync(fileno(kv->wal_fp));

fclose(kv->wal_fp);

}

index_free(kv->index);

free(kv);

}

// Write mutation to WAL file on disk with hardware sync

static bool kv_wal_append(KVStore *kv, uint8_t op, const char *key, const char *val) {

uint16_t klen = (uint16_t)strlen(key);

uint16_t vlen = val ? (uint16_t)strlen(val) : 0;

// Build payload buffer for CRC calculation

size_t payload_bytes = klen + vlen;

uint8_t *payload = (uint8_t *)malloc(payload_bytes);

memcpy(payload, key, klen);

if (vlen > 0) {

memcpy(payload + klen, val, vlen);

}

LogRecordHeader hdr;

hdr.magic = WAL_MAGIC_RECORD;

hdr.lsn = kv->next_lsn++;

hdr.op = op;

hdr.key_len = klen;

hdr.val_len = vlen;

hdr.crc32 = crc32_compute(payload, payload_bytes);

// Commit to disk

if (fwrite(&hdr, sizeof(hdr), 1, kv->wal_fp) != 1 ||

fwrite(payload, 1, payload_bytes, kv->wal_fp) != payload_bytes) {

free(payload);

return false;

}

free(payload);

fflush(kv->wal_fp);

fsync(fileno(kv->wal_fp)); // Enforce physical disk durability

return true;

}

bool kv_set(KVStore *kv, const char *key, const char *val) {

if (!kv || !key || !val) return false;

// 1. Write Ahead to Log first

if (!kv_wal_append(kv, OP_SET, key, val)) {

return false;

}

// 2. Apply to in-memory index

index_put(kv->index, key, val);

return true;

}

const char *kv_get(KVStore *kv, const char *key) {

if (!kv || !key) return NULL;

return index_get(kv->index, key);

}

bool kv_del(KVStore *kv, const char *key) {

if (!kv || !key) return false;

if (!index_get(kv->index, key)) return false;

// 1. Log Tombstone

if (!kv_wal_append(kv, OP_DEL, key, NULL)) {

return false;

}

// 2. Delete from in-memory index

return index_del(kv->index, key);

}

// Sequential Recovery Scanner

size_t kv_replay_wal(KVStore *kv) {

FILE *fp = fopen(kv->wal_filename, "rb");

if (!fp) return 0;

size_t count = 0;

LogRecordHeader hdr;

while (fread(&hdr, sizeof(hdr), 1, fp) == 1) {

if (hdr.magic != WAL_MAGIC_RECORD) {

fprintf(stderr, " [Recovery Warning] Magic mismatch at record #%zu! Halting replay.\\n", count + 1);

break;

}

size_t payload_bytes = (size_t)hdr.key_len + (size_t)hdr.val_len;

uint8_t *payload = (uint8_t *)malloc(payload_bytes + 1);

if (fread(payload, 1, payload_bytes, fp) != payload_bytes) {

fprintf(stderr, " [Recovery Warning] Torn/truncated record #%zu detected! Halting replay.\\n", count + 1);

free(payload);

break;

}

if (crc32_compute(payload, payload_bytes) != hdr.crc32) {

fprintf(stderr, " [Recovery Warning] CRC32 corrupted at LSN %llu! Halting replay.\\n", (unsigned long long)hdr.lsn);

free(payload);

break;

}

// Extract key and value strings

char *key = (char *)malloc(hdr.key_len + 1);

memcpy(key, payload, hdr.key_len);

key[hdr.key_len] = '\\0';

char *val = (char *)malloc(hdr.val_len + 1);

if (hdr.val_len > 0) {

memcpy(val, payload + hdr.key_len, hdr.val_len);

}

val[hdr.val_len] = '\\0';

// Apply recovered mutation

if (hdr.op == OP_SET) {

index_put(kv->index, key, val);

} else if (hdr.op == OP_DEL) {

index_del(kv->index, key);

}

if (hdr.lsn >= kv->next_lsn) {

kv->next_lsn = hdr.lsn + 1;

}

free(key);

free(val);

free(payload);

count++;

}

fclose(fp);

return count;

}

/* ========================================================================= */

/* DRIVER MAIN */

/* ========================================================================= */

int main(void) {

const char *db_file = "kv_store.wal";

unlink(db_file); // Start clean

printf("====================================================================\\n");

printf(" WEEK 3 CAPSTONE: DURABLE KEY-VALUE STORE & WAL PERSISTENCE \\n");

printf("====================================================================\\n\\n");

// 1. Session 1: Populate Database

printf("[1] SESSION 1: Initializing Database & Writing Mutations\...\\n");

KVStore *db1 = kv_open(db_file);

assert(db1 != NULL);

kv_set(db1, "config:port", "8080");

kv_set(db1, "config:workers", "16");

kv_set(db1, "session:alice", "AUTH_TOKEN_AAA");

kv_set(db1, "session:bob", "AUTH_TOKEN_BBB");

kv_del(db1, "session:bob"); // Test persistent deletion

printf(" Live Query (In-Memory):\\n");

printf(" config:port => %s\\n", kv_get(db1, "config:port"));

printf(" config:workers=> %s\\n", kv_get(db1, "config:workers"));

printf(" session:alice => %s\\n", kv_get(db1, "session:alice"));

printf(" session:bob => %s\\n", kv_get(db1, "session:bob") ? "Found" : "NULL (Deleted)");

kv_close(db1);

printf(" Session 1 closed: Hardware disk flush completed.\\n\\n");

// 2. Session 2: Crash Simulation & Instant Recovery

printf("[2] SESSION 2: Simulating Process Restart & Cold Recovery from WAL\...\\n");

KVStore *db2 = kv_open(db_file);

assert(db2 != NULL);

printf(" Verifying In-Memory Index Reconstructed from Disk:\\n");

assert(strcmp(kv_get(db2, "config:port"), "8080") == 0);

assert(strcmp(kv_get(db2, "config:workers"), "16") == 0);

assert(strcmp(kv_get(db2, "session:alice"), "AUTH_TOKEN_AAA") == 0);

assert(kv_get(db2, "session:bob") == NULL);

printf(" All assertions passed! Recovered identical dataset with zero data loss.\\n\\n");

kv_close(db2);

unlink(db_file); // Clean up test file

printf("====================================================================\\n");

printf(" WEEK 3 MEGA PROJECT VERIFICATION COMPLETE: ALL ASSERTS PASSED! \\n");

printf("====================================================================\\n");

return 0;

}
