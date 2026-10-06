---
tags:
  - c
  - file-io
  - streams
  - binary-io
  - file-buffering
  - atomic-io
date: 2026-09-09
day: 18
---

# Day 18: Low-Level Stream & Binary File I/O, Buffering Modes & Atomic File Operations

---

## 1. Quick Reference & Cheat Sheet

### Core Standard Stream I/O (`<stdio.h>`)

| Function | Prototype | Primary Purpose / Return Value |
| :--- | :--- | :--- |
| `fopen` | `FILE *fopen(const char *path, const char *mode);` | Opens a stream. Returns `NULL` on failure with `errno` set. |
| `fclose` | `int fclose(FILE *stream);` | Flushes userspace buffer, closes OS file descriptor. Returns `0` on success, `EOF` on failure. |
| `fread` | `size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);` | Reads up to `nmemb` elements of `size` bytes. **Returns number of full items read, NOT bytes.** |
| `fwrite` | `size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);` | Writes `nmemb` elements of `size` bytes. Returns number of full items written. |
| `fseek` | `int fseek(FILE *stream, long offset, int whence);` | Sets file position (`SEEK_SET`, `SEEK_CUR`, `SEEK_END`). Returns `0` on success. |
| `ftell` | `long ftell(FILE *stream);` | Returns current byte position offset, or `-1L` on error. |
| `fflush` | `int fflush(FILE *stream);` | Flushes C library userspace write buffer to OS kernel page cache. |

### Stream Open Modes

| Mode | Meaning | File Must Exist? | Initial Position | Truncates File? |
| :--- | :--- | :--- | :--- | :--- |
| `"r"` / `"rb"` | Read-only | **Yes** | Start | No |
| `"w"` / `"wb"` | Write-only | No (Creates if absent) | Start | **Yes (Zeros size)** |
| `"a"` / `"ab"` | Append-only | No (Creates if absent) | End | No (Writes always go to end) |
| `"r+"` / `"rb+"` | Read and Write | **Yes** | Start | No |
| `"w+"` / `"wb+"` | Read and Write | No (Creates if absent) | Start | **Yes (Zeros size)** |
| `"a+"` / `"ab+"` | Read and Append | No (Creates if absent) | End (Writes) | No |

* **Binary Flag (`"b"`):** Mandatory for portable binary files. On Windows, omitting `"b"` converts `\\n` to `\\r\\n` and treats byte `0x1A` (Ctrl-Z) as an immediate End-Of-File (EOF), corrupting binary payloads.

### Buffering Controls (`setvbuf`)

```c
int setvbuf(FILE *stream, char *buf, int mode, size_t size);
```

* `_IONBF` (Unbuffered): Each write operation directly issues a syscall (`write()`). Used for `stderr`.

* `_IOLBF` (Line Buffered): Flushes whenever `\\n` is encountered or buffer fills. Default for `stdout` when connected to a terminal.

* `_IOFBF` (Fully Buffered): Flushes only when buffer is completely saturated. Default for disk files (typically 4 KB or 8 KB).

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. The Anatomy of a `FILE` Pointer

A `FILE *` in C is an opaque handle to a runtime structure (e.g. `struct _IO_FILE` in GNU `glibc`). It wraps an OS-level integer file descriptor (`fd`) with a **userspace memory buffer**:

```text
User Application (C Code):

fwrite(data, size, nmemb, fp)

│

▼

C Runtime Userspace Buffer (e.g., 4096 bytes in Heap/BSS):

[ Data Byte 1 | Data Byte 2 | \... | Unfilled ] (Buffered until
full or fflush)

│

▼ (System Call: write(fd, buf, count))

Kernel Space / OS Page Cache:

[ OS Virtual Memory Page Cache ]

│

▼ (Kernel Flushes: fsync / disk controller commit)

Physical Storage Media (NVMe / SSD / HDD)
```

* **Why Buffering Matters:** System calls (`write`, `read`) incur a context switch from User Mode to Kernel Mode (~100--300 CPU cycles). Buffering aggregates thousands of small 4-byte writes into a single 4096-byte kernel write, speeding up I/O by orders of magnitude.

---

### B. Seeking, Offsets & The 2 GB Limit

* `fseek()` and `ftell()` take and return a signed `long`.

* On 32-bit platforms (or 64-bit Windows where `long` is 32 bits), `fseek()` cannot handle files larger than \$2^{31}-1\$ bytes (2 GB).

* **Portable Large File Support:** Use POSIX `fseeko()` and `ftello()`, which use `off_t` (64 bits on modern systems), or C99's `fgetpos()` and `fsetpos()`, which use the opaque `fpos_t` type.

---

### C. The Atomic File Replacement Pattern

Databases (SQLite, PostgreSQL) and text editors never overwrite active data files in-place directly. If a power failure or system crash occurs mid-write, the file becomes permanently corrupted.

#### The 3-Step Atomic Guarantee:

1\. **Write to Temp File:** Write data completely to `filename.tmp`.

2\. **Commit to Physical Disk:** Call `fflush()` followed by POSIX `fsync(fileno(fp))` to force the OS kernel to flush physical controller caches.

3\. **Atomic Rename:** Call `rename("filename.tmp", "filename.dat")`.

* Under POSIX, `rename()` is an atomic directory metadata update. The old file is atomically replaced by the new file in a single filesystem transaction with zero risk of partial file states.

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Binary Write-Ahead Log (WAL) with CRC32 Verification
& Crash Recovery (`bin_wal`)

#### Objective

Build a durable Write-Ahead Logging system in C that:

1\. Appends framed binary records containing a Magic word, 64-bit Log Sequence Number (LSN), timestamp, payload size, CRC32 checksum, and payload.

2\. Performs automated recovery on startup: scans sequential records, validates CRC32 integrity, and safely truncates or isolates partially written/corrupted tail records.

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define SAFE_BUFFER_SIZE 4096
bool copy_file_safe(const char *src_path, const char *dst_path) {
    if (!src_path || !dst_path) return false;
    // Fix 1: Explicit binary mode ("rb", "wb")
    FILE *in = fopen(src_path, "rb");
    if (!in) {
        perror("Defensive Error: Failed to open source file");
        return false;
    }
    FILE *out = fopen(dst_path, "wb");
    if (!out) {
        perror("Defensive Error: Failed to open destination file");
        fclose(in);
        return false;
    }
    char buffer[SAFE_BUFFER_SIZE];
    size_t bytes_read = 0;
    bool success = true;
    // Fix 2: Condition loop directly on fread() return value
    while ((bytes_read = fread(buffer, 1, SAFE_BUFFER_SIZE, in)) > 0) {
        // Fix 3: Write exactly the number of bytes read
        size_t bytes_written = fwrite(buffer, 1, bytes_read, out);
        if (bytes_written != bytes_read) {
            perror("Defensive Error: Incomplete write or disk full");
            success = false;
            break;
        }
    }
    // Fix 4: Differentiate between normal EOF and read error
    if (ferror(in)) {
        perror("Defensive Error: An I/O error occurred while reading source");
        success = false;
    }
    fclose(in);
    if (fclose(out) != 0) {
        perror("Defensive Error: Failed to flush/close destination file");
        success = false;
    }
    return success;
}
```
    fclose(in);
    fclose(out);
}
``` WalHeader;
/* ========================================================================= */
/*                          1. CRC-32 IMPLEMENTATION                         */
/* ========================================================================= */
uint32_t compute_crc32(const uint8_t *data, size_t len) {
    uint32_t crc = 0xFFFFFFFFU;
    for (size_t i = 0; i < len; i++) {
        crc ^= data[i];
        for (int b = 0; b < 8; b++) {
            if (crc & 1) {
                crc = (crc >> 1) ^ 0xEDB88320U;
            } else {
                crc >>= 1;
            }
        }
    }
    return ~crc;
}
/* ========================================================================= */
/*                       2. WAL MANAGEMENT ENGINE                            */
/* ========================================================================= */
typedef struct {
    FILE *fp;
    char filename[256];
    uint64_t next_lsn;
} WriteAheadLog;
WriteAheadLog *wal_open(const char *filename) {
    WriteAheadLog *wal = (WriteAheadLog *)malloc(sizeof(WriteAheadLog));
    if (!wal) return NULL;
    strncpy(wal->filename, filename, sizeof(wal->filename) - 1);
    wal->filename[sizeof(wal->filename) - 1] = '\0';
    wal->next_lsn = 1;
    // Open for append & read in binary mode
    wal->fp = fopen(filename, "ab+");
    if (!wal->fp) {
        free(wal);
        return NULL;
    }
    return wal;
}
void wal_close(WriteAheadLog *wal) {
    if (!wal) return;
    if (wal->fp) {
        fflush(wal->fp);
        fclose(wal->fp);
    }
    free(wal);
}
// Append a record with CRC32 framing
bool wal_append(WriteAheadLog *wal, const void *payload, size_t len, uint64_t ts) {
    if (!wal || !wal->fp || !payload || len == 0) return false;
    WalHeader hdr;
    hdr.magic = WAL_MAGIC;
    hdr.lsn = wal->next_lsn;
    hdr.timestamp_sec = ts;
    hdr.payload_len = (uint32_t)len;
    hdr.crc32 = compute_crc32((const uint8_t *)payload, len);
    // Write Header
    if (fwrite(&hdr, sizeof(WalHeader), 1, wal->fp) != 1) {
        return false;
    }
    // Write Payload
    if (fwrite(payload, 1, len, wal->fp) != len) {
        return false;
    }
    // Flush to OS cache
    fflush(wal->fp);
    wal->next_lsn++;
    return true;
}
// Recovery Callback Signature
typedef void (*WalReplayFn)(uint64_t lsn, uint64_t ts, const uint8_t *data, size_t len, void *ctx);
// Read and recover all valid WAL records, reporting any corrupted tail
size_t wal_recover(const char *filename, WalReplayFn replay_cb, void *ctx) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) return 0;
    size_t valid_records = 0;
    WalHeader hdr;
    while (fread(&hdr, sizeof(WalHeader), 1, fp) == 1) {
        if (hdr.magic != WAL_MAGIC) {
            fprintf(stderr, "[Recovery] Invalid magic 0x%08X at record #%zu! Halting scan.\n", 
                    hdr.magic, valid_records + 1);
            break;
        }
        uint8_t *payload = (uint8_t *)malloc(hdr.payload_len);
        if (!payload) break;
        size_t bytes_read = fread(payload, 1, hdr.payload_len, fp);
        if (bytes_read != hdr.payload_len) {
            fprintf(stderr, "[Recovery] Incomplete payload read (%zu of %u bytes). Truncated record!\n",
                    bytes_read, hdr.payload_len);
            free(payload);
            break;
        }
        uint32_t check_crc = compute_crc32(payload, hdr.payload_len);
        if (check_crc != hdr.crc32) {
            fprintf(stderr, "[Recovery] CRC32 Mismatch on LSN %llu! Data corrupted.\n", (unsigned long long)hdr.lsn);
            free(payload);
            break;
        }
        if (replay_cb) {
            replay_cb(hdr.lsn, hdr.timestamp_sec, payload, hdr.payload_len, ctx);
        }
        free(payload);
        valid_records++;
    }
    fclose(fp);
    return valid_records;
}
/* ========================================================================= */
/*                               DRIVER MAIN                                 */
/* ========================================================================= */
void sample_replay_handler(uint64_t lsn, uint64_t ts, const uint8_t *data, size_t len, void *ctx) {
    (void)ctx;
    printf("  [REPLAY] LSN: %llu | TS: %llu | Data: \"%.*s\" (%zu bytes)\n", 
           (unsigned long long)lsn, (unsigned long long)ts, (int)len, data, len);
}
int main(void) {
    const char *log_file = "test_transaction.wal";
    printf("=== Testing Binary Write-Ahead Log (WAL) Engine ===\n\n");
    // 1. Initialize and write records
    WriteAheadLog *wal = wal_open(log_file);
    assert(wal != NULL);
    printf("[1] Appending transaction records...\n");
    wal_append(wal, "TX_BEGIN: Account=1001", strlen("TX_BEGIN: Account=1001"), 1725880000ULL);
    wal_append(wal, "TX_DEBIT: Account=1001 Amount=250.00", strlen("TX_DEBIT: Account=1001 Amount=250.00"), 1725880001ULL);
    wal_append(wal, "TX_CREDIT: Account=2002 Amount=250.00", strlen("TX_CREDIT: Account=2002 Amount=250.00"), 1725880002ULL);
    wal_append(wal, "TX_COMMIT: Account=1001", strlen("TX_COMMIT: Account=1001"), 1725880003ULL);
    wal_close(wal);
    printf("    4 transactions committed and flushed to disk.\n\n");
    // 2. Perform Recovery Scan
    printf("[2] Executing WAL Recovery & Replay Scan:\n");
    size_t recovered = wal_recover(log_file, sample_replay_handler, NULL);
    printf("    Recovery Complete: %zu valid records verified.\n\n", recovered);
    assert(recovered == 4);
    // Clean up temporary log file
    remove(log_file);
    printf("WAL file cleanly removed. Zero leaks!\n");
    return 0;
}
``` WalHeader;

/*
=========================================================================
*/

/* 1. CRC-32 IMPLEMENTATION */

/*
=========================================================================
*/

uint32_t compute_crc32(const uint8_t *data, size_t len) {

uint32_t crc = 0xFFFFFFFFU;

for (size_t i = 0; i < len; i++) {

crc ^= data[i];

for (int b = 0; b < 8; b++) {

if (crc & 1) {

crc = (crc >> 1) ^ 0xEDB88320U;

} else {

crc >>= 1;

}

}

}

return ~crc;

}

/*
=========================================================================
*/

/* 2. WAL MANAGEMENT ENGINE */

/*
=========================================================================
*/

typedef struct {

FILE *fp;

char filename[256];

uint64_t next_lsn;

} WriteAheadLog;

WriteAheadLog *wal_open(const char *filename) {

WriteAheadLog *wal = (WriteAheadLog *)malloc(sizeof(WriteAheadLog));

if (!wal) return NULL;

strncpy(wal->filename, filename, sizeof(wal->filename) - 1);

wal->filename[sizeof(wal->filename) - 1] = '\\0';

wal->next_lsn = 1;

// Open for append & read in binary mode

wal->fp = fopen(filename, "ab+");

if (!wal->fp) {

free(wal);

return NULL;

}

return wal;

}

void wal_close(WriteAheadLog *wal) {

if (!wal) return;

if (wal->fp) {

fflush(wal->fp);

fclose(wal->fp);

}

free(wal);

}

// Append a record with CRC32 framing

bool wal_append(WriteAheadLog *wal, const void *payload, size_t len,
uint64_t ts) {

if (!wal || !wal->fp || !payload || len == 0) return false;

WalHeader hdr;

hdr.magic = WAL_MAGIC;

hdr.lsn = wal->next_lsn;

hdr.timestamp_sec = ts;

hdr.payload_len = (uint32_t)len;

hdr.crc32 = compute_crc32((const uint8_t *)payload, len);

// Write Header

if (fwrite(&hdr, sizeof(WalHeader), 1, wal->fp) != 1) {

return false;

}

// Write Payload

if (fwrite(payload, 1, len, wal->fp) != len) {

return false;

}

// Flush to OS cache

fflush(wal->fp);

wal->next_lsn++;

return true;

}

// Recovery Callback Signature

typedef void (*WalReplayFn)(uint64_t lsn, uint64_t ts, const uint8_t
*data, size_t len, void *ctx);

// Read and recover all valid WAL records, reporting any corrupted tail

size_t wal_recover(const char *filename, WalReplayFn replay_cb, void
*ctx) {

FILE *fp = fopen(filename, "rb");

if (!fp) return 0;

size_t valid_records = 0;

WalHeader hdr;

while (fread(&hdr, sizeof(WalHeader), 1, fp) == 1) {

if (hdr.magic != WAL_MAGIC) {

fprintf(stderr, "[Recovery] Invalid magic 0x%08X at record #%zu!
Halting scan.\\n",

hdr.magic, valid_records + 1);

break;

}

uint8_t *payload = (uint8_t *)malloc(hdr.payload_len);

if (!payload) break;

size_t bytes_read = fread(payload, 1, hdr.payload_len, fp);

if (bytes_read != hdr.payload_len) {

fprintf(stderr, "[Recovery] Incomplete payload read (%zu of %u
bytes). Truncated record!\\n",

bytes_read, hdr.payload_len);

free(payload);

break;

}

uint32_t check_crc = compute_crc32(payload, hdr.payload_len);

if (check_crc != hdr.crc32) {

fprintf(stderr, "[Recovery] CRC32 Mismatch on LSN %llu! Data
corrupted.\\n", (unsigned long long)hdr.lsn);

free(payload);

break;

}

if (replay_cb) {

replay_cb(hdr.lsn, hdr.timestamp_sec, payload, hdr.payload_len, ctx);

}

free(payload);

valid_records++;

}

fclose(fp);

return valid_records;

}

/*
=========================================================================
*/

/* DRIVER MAIN */

/*
=========================================================================
*/

void sample_replay_handler(uint64_t lsn, uint64_t ts, const uint8_t
*data, size_t len, void *ctx) {

(void)ctx;

printf(" [REPLAY] LSN: %llu | TS: %llu | Data: \\"%.*s\\" (%zu
bytes)\\n",

(unsigned long long)lsn, (unsigned long long)ts, (int)len, data, len);

}

int main(void) {

const char *log_file = "test_transaction.wal";

printf("=== Testing Binary Write-Ahead Log (WAL) Engine ===\\n\\n");

// 1. Initialize and write records

WriteAheadLog *wal = wal_open(log_file);

assert(wal != NULL);

printf("[1] Appending transaction records\...\\n");

wal_append(wal, "TX_BEGIN: Account=1001", strlen("TX_BEGIN:
Account=1001"), 1725880000ULL);

wal_append(wal, "TX_DEBIT: Account=1001 Amount=250.00",
strlen("TX_DEBIT: Account=1001 Amount=250.00"), 1725880001ULL);

wal_append(wal, "TX_CREDIT: Account=2002 Amount=250.00",
strlen("TX_CREDIT: Account=2002 Amount=250.00"), 1725880002ULL);

wal_append(wal, "TX_COMMIT: Account=1001", strlen("TX_COMMIT:
Account=1001"), 1725880003ULL);

wal_close(wal);

printf(" 4 transactions committed and flushed to disk.\\n\\n");

// 2. Perform Recovery Scan

printf("[2] Executing WAL Recovery & Replay Scan:\\n");

size_t recovered = wal_recover(log_file, sample_replay_handler, NULL);

printf(" Recovery Complete: %zu valid records verified.\\n\\n",
recovered);

assert(recovered == 4);

// Clean up temporary log file

remove(log_file);

printf("WAL file cleanly removed. Zero leaks!\\n");

return 0;

}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The `feof()` Loop Condition Fallacy & Unchecked Write Truncation

Examine the following buggy file replication routine:

```c
#include <stdio.h>

#include <stdlib.h>

#define CHUNK_SIZE 512

// BUGGY IMPLEMENTATION

void copy_file_faulty(const char *src_path, const char *dst_path) {

FILE *in = fopen(src_path, "r"); // BUG 1: Text mode on potential
binary files!

FILE *out = fopen(dst_path, "w"); // BUG 2: Unchecked fopen failure!

char buffer[CHUNK_SIZE];

// BUG 3: feof() as a loop controlling condition!

// feof() only becomes true AFTER a read attempts to read past EOF.

// The final loop iteration executes with partial or stale buffer data!

while (!feof(in)) {

fread(buffer, 1, CHUNK_SIZE, in);

// BUG 4: Unchecked fwrite, writing full CHUNK_SIZE even if partial
read!

fwrite(buffer, 1, CHUNK_SIZE, out);

}

fclose(in);

fclose(out);

}
```

### Analysis of Vulnerabilities:

1\. **The `feof()` Anti-Pattern:** `feof()` does not predict EOF; it only checks if an EOF indicator was set by a *prior* failed read. On the last iteration, `fread()` reads 0 bytes, but `fwrite(buffer, 1, CHUNK_SIZE, out)` executes anyway, duplicating the last chunk and corrupting destination file size.

2\. **Missing `fopen()` Return Verification:** If `src_path` does not exist or `dst_path` is unwritable, dereferencing `in` or `out` causes an instant segmentation fault (`SIGSEGV`).

3\. **Missing Binary Mode:** In text mode (`"r"`, `"w"`), carriage return conversions (`\\r\\n`) and character `0x1A` corrupt binary streams.

4\. **Unchecked Return of `fwrite()`:** If the target disk runs out of space (`ENOSPC`), `fwrite()` silently fails without detection.

### Defensive Fix:

```c
#include <stdio.h>

#include <stdlib.h>

#include <stdbool.h>

#define SAFE_BUFFER_SIZE 4096

bool copy_file_safe(const char *src_path, const char *dst_path) {

if (!src_path || !dst_path) return false;

// Fix 1: Explicit binary mode ("rb", "wb")

FILE *in = fopen(src_path, "rb");

if (!in) {

perror("Defensive Error: Failed to open source file");

return false;

}

FILE *out = fopen(dst_path, "wb");

if (!out) {

perror("Defensive Error: Failed to open destination file");

fclose(in);

return false;

}

char buffer[SAFE_BUFFER_SIZE];

size_t bytes_read = 0;

bool success = true;

// Fix 2: Condition loop directly on fread() return value

while ((bytes_read = fread(buffer, 1, SAFE_BUFFER_SIZE, in)) > 0) {

// Fix 3: Write exactly the number of bytes read

size_t bytes_written = fwrite(buffer, 1, bytes_read, out);

if (bytes_written != bytes_read) {

perror("Defensive Error: Incomplete write or disk full");

success = false;

break;

}

}

// Fix 4: Differentiate between normal EOF and read error

if (ferror(in)) {

perror("Defensive Error: An I/O error occurred while reading source");

success = false;

}

fclose(in);

if (fclose(out) != 0) {

perror("Defensive Error: Failed to flush/close destination file");

success = false;

}

return success;

}
```
