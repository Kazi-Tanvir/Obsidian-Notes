---
tags:
  - javascript
  - local-first
  - sqlite
  - webassembly
  - opfs
  - web-locks
  - indexeddb
  - architecture
date: 2026-09-23
---

# Day 54 - Local-First Architecture, SQLite in WebAssembly, Origin Private File System (OPFS) & Web Locks API

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Local-First Software Revolution

For two decades, web applications operated on the **Cloud-First Thin-Client model**: the browser acts as a dumb terminal, sending every user keystroke across the network to a central server.

- **The Cloud-First Failure Modes**: When a user goes offline or suffers network latency spikes, the UI freezes, spinners appear, and unsaved work is lost.

- **The Local-First Philosophy (Kleppmann et al.)**:

  1.  **Zero-Latency Interactions**: All reads and writes execute against an in-browser local database instantly (\$<1\\text{ms}\$).

  2.  **Offline by Default**: The application retains full read/write functionality with zero network connectivity.

  3.  **Multi-Device Synchronization**: Data synchronizes asynchronously in the background via event-driven replication or CRDTs.

  4.  **User Data Ownership**: Data lives in durable, local storage on the user's hardware.

```text
┌────────────────────────────────────── Cloud-First vs. Local-First ──────────────────────────────────────┐
│                                                                                                         │
│  Cloud-First (Traditional SPA) ⚠️:                                                                      │
│  UI Event ──► Network Request (HTTP/RPC) ──► Central Cloud DB ──► Network Response ──► UI Updates       │
│  • High latency (50-300ms), spinner fatigue, breaks completely when offline.                           │
│                                                                                                         │
│  Local-First (Modern Reactive Client) 🚀:                                                               │
│  UI Event ──► Local Wasm SQLite / OPFS ──► Instant UI Update (<1ms!) ⚡                                 │
│                     │                                                                                   │
│                     └──► Asynchronous Background Sync ──► Cloud Edge Replica                            │
│                                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The Storage Engine Bottleneck: Why IndexedDB Fails & OPFS Succeeds

Historically, client-side browser storage relied on **IndexedDB**:

- **IndexedDB Bottlenecks**: High transaction overhead, structured clone serialization costs for large objects, and asynchronous JavaScript event loop hops on every single read/write. Querying complex relational joins or running full-text search in IndexedDB is painfully slow.

- **The Origin Private File System (OPFS)**: A specialized, highly optimized sandboxed private filesystem accessible only to the origin.

- **FileSystemSyncAccessHandle**: On dedicated **Web Workers**, OPFS provides synchronous in-place byte operations (read(), write(), flush(), truncate()). It completely bypasses the main thread's asynchronous message queue, granting WebAssembly near-native NVMe disk I/O performance!

```text
┌────────────────────────────────────── OPFS High-Speed Architecture ──────────────────────────────────────┐
│                                                                                                          │
│  Web Worker Thread (Off-Main-Thread Sandbox)                                                             │
│  ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐    │
│  │ SQLite / PostgreSQL (PGlite) compiled to WebAssembly                                             │    │
│  │                                                                                                  │    │
│  │  Virtual File System (VFS) Layer (C/Wasm POSIX Calls)                                            │    │
│  └───────────────────────────────────┬──────────────────────────────────────────────────────────────┘    │
│                                      │ Synchronous read() / write() (Raw Binary Pointers)                │
│                                      ▼                                                                   │
│  FileSystemSyncAccessHandle (OPFS File Descriptor)                                                       │
│  • Executes synchronous in-place byte modifications on NVMe disk!                                        │
│  • 100x faster than IndexedDB transactions! ⚡                                                           │
│                                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3. Native OPFS Worker Access Handles

To obtain an exclusive, high-performance synchronous access handle:

// worker.js (Dedicated Web Worker)

async function initializeOPFSStorage() {

```typescript
  // 1. Obtain root directory of the Origin Private File System
  const root = await navigator.storage.getDirectory();
  // 2. Open or create a binary database file handle
  const fileHandle = await root.getFileHandle('enterprise_core.db', { create: true });
  // 3. Create a synchronous access handle (EXCLUSIVE TO WEB WORKERS!)
  // Note: Only one sync access handle can be open per file concurrently.
  const accessHandle = await fileHandle.createSyncAccessHandle();
  // 4. In-place binary I/O (Synchronous execution, zero async tick overhead!)
  const writeBuffer = new TextEncoder().encode('SQLITE_HEADER_BYTES_V1');
  const bytesWritten = accessHandle.write(writeBuffer, { at: 0 });
  // 5. Force write barrier to physical persistent storage
  accessHandle.flush();
  // 6. Read back from arbitrary byte offset
  const readBuffer = new Uint8Array(bytesWritten);
  accessHandle.read(readBuffer, { at: 0 });
  console.log('Read back:', new TextDecoder().decode(readBuffer));
  // Close handle when finished
  accessHandle.close();
```

}

### 4. Multi-Tab Concurrency via Web Locks API (navigator.locks)

Because OPFS createSyncAccessHandle() requires an **exclusive lock** on the underlying file, two browser tabs trying to open the same local SQLite database simultaneously will throw an InvalidStateError.

We resolve multi-tab coordination using the **Web Locks API** combined with BroadcastChannel:

- **Leader Tab**: Acquires an exclusive Web Lock, mounts the OPFS Wasm SQLite engine, and serves queries.

- **Follower Tabs**: Connect to the Leader tab via BroadcastChannel or MessageChannel, sending RPC queries and receiving streaming results.

- **Failover**: If the Leader tab is closed, another tab immediately acquires the lock and mounts the database seamlessly!

// multi-tab-coordination.js

async function runWithDatabaseLock(callback) {

```typescript
// Request an exclusive lock across all tabs of this origin
await navigator.locks.request('sqlite-db-exclusive-lock', async (lock) => {
  console.log('Acquired exclusive lock! Initializing SQLite Wasm on OPFS...');
  const worker = new Worker('sqlite-worker.js', { type: 'module' });
  const channel = new BroadcastChannel('db-sync-channel');

  // Leader processes query requests from follower tabs
  channel.onmessage = async (event) => {
    const { queryId, sql } = event.data;
    const result = await dispatchToWorker(worker, sql);
    channel.postMessage({ queryId, result });
  };

  // Keep lock alive until tab closes or execution terminates
  await new Promise((_, reject) => {
    window.addEventListener('beforeunload', () => reject(new Error('Tab closed')));
  });
});
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### OPFS Core APIs & Synchronous Methods:

----------------------------------------------------------------------------------------------------------------- **API / Method**                      **Context**       **Return Type**                         **Description & Performance Rule** ------------------------------------- ----------------- --------------------------------------- ----------------- navigator.storage.getDirectory()      Window / Worker   Promise<FileSystemDirectoryHandle>    Gets root directory of Origin Private File System.

dirHandle.getFileHandle(name,         Window / Worker   Promise<FileSystemFileHandle>         Opens or creates {create})                                                                                       a file pointer in the private sandbox.

fileHandle.createSyncAccessHandle()   **Web Worker      Promise<FileSystemSyncAccessHandle>   **Synchronous Only**                                                    binary file descriptor**. Requires exclusive lock.

accessHandle.read(buffer, {at})       Web Worker        number                                  Synchronous in-place byte read from specified offset.

accessHandle.write(buffer, {at})      Web Worker        number                                  Synchronous in-place byte write to specified offset.

accessHandle.flush()                  Web Worker        void                                    Forces write barrier flush from OS cache to physical disk.

accessHandle.truncate(newSize)        Web Worker        void                                    Resizes file on disk immediately.

accessHandle.close()                  Web Worker        void                                    Releases physical file lock, allowing other processes access. -----------------------------------------------------------------------------------------------------------------

### Web Locks API Cheat Sheet:

```javascript
// Exclusive Lock (One tab at a time)
await navigator.locks.request('my-resource', async (lock) => {
  /* Critical Section */
});
```

// Shared Read Lock (Multiple readers allowed concurrently)

await navigator.locks.request('my-resource', { mode: 'shared' }, async (lock) => {

/* Read Section */

});

## SECTION 3: PRACTICAL PROBLEMS

### Problem 1 (Basic): High-Performance Atomic OPFS Blob Cache

**Context**: Heavy web assets (like 3D GLTF models, audio files, or AI tensor weights) suffer when repeatedly downloaded or stored as base64 strings in IndexedDB.

**Challenge**: Implement an OPFSBlobCache class:

1.  set(key: string, blob: Blob): Promise<void>:

    - Creates a file with a hashed key name in OPFS.

    - Streams the blob data into a FileSystemWritableFileStream or access handle.

2.  get(key: string): Promise<Blob | null>:

    - Reads the file and returns a native Blob object without loading the entire payload into the V8 string heap.

3.  has(key: string): Promise<boolean> and delete(key: string): Promise<void>.

4.  Include quota verification checking navigator.storage.estimate().

*Hint: Use fileHandle.getFile() which creates a lazy native Blob pointing directly to the underlying disk file without memory copies!*

### Problem 2 (Intermediate): Resilient Multi-Tab Leader Election & RPC Bridge

**Context**: When multiple browser tabs open a local-first application, only one tab can hold the synchronous OPFS access handle. Other tabs must transparently forward their database queries to the leader.

**Challenge**: Build a MultiTabDatabaseCoordinator class:

1.  Uses navigator.locks.request('opfs-db-leader') to attempt to become the leader.

2.  If the lock is held by another tab:

    - Sets role to FOLLOWER.

    - Sends queries across a BroadcastChannel with unique correlation IDs (crypto.randomUUID()).

    - Awaits responses with a 5-second timeout.

3.  If the active leader tab crashes or closes:

    - The Web Lock is automatically released by the browser.

    - The next waiting tab promotes itself to LEADER, initializes the worker, and begins servicing requests.

*Hint: Use new Promise((resolve, reject) => { \... }) and maintain an in-memory pendingQueries map keyed by correlation ID.*

### Problem 3 (Advanced): Custom WAL (Write-Ahead Logging) Engine on OPFS

**Context**: Embedded databases achieve ACID crash-recovery guarantees by writing mutations to an append-only Write-Ahead Log (WAL) before updating main table files.

**Challenge**: Develop a complete binary **WAL Engine** in a Web Worker using FileSystemSyncAccessHandle:

1.  Binary Frame Structure:

    - Header (16 bytes): [Magic: 4B ('WAL1')][TransactionID: 4B][DataLength: 4B][CRC32 Checksum: 4B]

    - Payload: Raw binary mutation bytes.

2.  Implements methods:

    - appendTransaction(txId: number, payload: Uint8Array): void: Synchronously appends the frame to the end of the log and executes accessHandle.flush().

    - recover(): Array<{ txId: number, payload: Uint8Array }>: Sequentially scans the file from byte 0, validates CRC32 checksums, and returns all uncorrupted committed transactions.

    - checkpoint(): void: Truncates the WAL file to 0 bytes via accessHandle.truncate(0) once transactions are applied to the main store.

3.  Simulate crash recovery: deliberately truncate a frame midway through writing and verify that recover() cleanly ignores the partial corrupted trailing frame without crashing.

*Hint: Calculate CRC32 using standard bitwise polynomials or crypto.subtle.digest('SHA-256').*
