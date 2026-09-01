---
tags:
- javascript
- indexeddb
- offline-storage
- dexie
- browser-database
- storage-api
- performance
date: 2026-08-31
---

# Day 31 - IndexedDB Architecture, Dexie.js, Object Stores & Offline Relational Storage

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Client-Side Storage Hierarchy: Why IndexedDB?

While localStorage and sessionStorage provide simple synchronous key-value stores, they are limited to 5 MB of string data and block the main UI thread during read/write cycles.

**IndexedDB** is an asynchronous, transactional, object-oriented database built into the browser. It supports multi-gigabyte storage (governed by browser disk quotas), structured cloning (objects, Arrays, Blob, ArrayBuffer, File, CryptoKey), compound indexing, and transactional guarantees.

┌────────────────────────────────────── Browser Storage Comparison ──────────────────────────────────────┐

│ │

│ Storage API │ Execution Model │ Capacity │ Data Types │ Indexing / Transactions │

│ ─────────────────┼─────────────────┼────────────────┼──────────────────┼───────────────────────────── │

│ localStorage │ Synchronous (UI)│ ~5 MB │ Strings only │ None / No transactions │

│ Cache Storage │ Asynchronous │ % of Disk (GB) │ Request/Response │ URL matching only │

│ IndexedDB │ Asynchronous │ % of Disk (GB) │ Structured Clone │ Multi-Index, ACID Transact. │

│ │

└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Core IndexedDB Architecture & Database Lifecycle

IndexedDB operates on **Object Stores** (analogous to tables in SQL or collections in MongoDB) containing records indexed by primary keys.

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐

│ IndexedDB Database: "AppDB" (v2) │

│ │

│ ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐ │

│ │ Object Store: "documents" (keyPath: "id", autoIncrement: false) │ │

│ │ │ │

│ │ Indexes: │ │

│ │ • "by_folder" (keyPath: "folderId", unique: false) │ │

│ │ • "by_tags" (keyPath: "tags", multiEntry: true) ──► Indexes individual array items! │ │

│ │ • "by_updated"(keyPath: "updatedAt", unique: false) │ │

│ └──────────────────────────────────────────────────────────────────────────────────────────────────┘ │

└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

#### Lifecycle & Schema Migrations (onupgradeneeded):

Schema modifications (creating/deleting object stores or indexes) can **only** occur inside a versionchange transaction triggered by opening the database with an incremented version number.

```javascript
// Native IndexedDB Initialization with Version Migration
function openAppDatabase() {
return new Promise((resolve, reject) => {
const DB_NAME = 'OfflineWorkspaceDB';
const DB_VERSION = 2; // Incremented triggers onupgradeneeded
const request = indexedDB.open(DB_NAME, DB_VERSION);
```

request.onupgradeneeded = (event) => {

```javascript
const db = request.result;
const oldVersion = event.oldVersion;
// Version 1 Migration: Create documents store
if (oldVersion < 1) {
const docStore = db.createObjectStore('documents', { keyPath: 'id' });
docStore.createIndex('by_folder', 'folderId', { unique: false });
docStore.createIndex('by_updated', 'updatedAt', { unique: false });
}
// Version 2 Migration: Add multiEntry index for array tags
if (oldVersion < 2) {
const transaction = request.transaction;
const docStore = transaction.objectStore('documents');
// multiEntry: true creates a separate index entry for every tag in the array!
docStore.createIndex('by_tags', 'tags', { unique: false, multiEntry: true });
}
};
request.onsuccess = () => resolve(request.result);
request.onerror = () => reject(request.error);
request.onblocked = () => console.warn('Database upgrade blocked by open tabs');
});
}
```

### 3. Transactions & The Auto-Commit Trap

IndexedDB transactions are strictly scoped and auto-commit as soon as the current event loop turn finishes with no active requests remaining in the transaction.

```javascript
// THE AUTO-COMMIT TRAP:
async function vulnerableTransaction(db, docId) {
const tx = db.transaction(['documents'], 'readwrite');
const store = tx.objectStore('documents');
const doc = await promisifyRequest(store.get(docId));
// Anti-Pattern: Calling an async fetch or setTimeout breaks the transaction!
const remoteValidation = await fetch('/api/validate', { method: 'POST', body: JSON.stringify(doc) });
// THROWS: InvalidStateError: The transaction has already finished / auto-committed!
store.put({ ...doc, validated: true });
}
// CORRECT PATTERN: Perform async network I/O FIRST, then execute atomic transaction
async function safeTransaction(db, docId) {
// 1. Fetch remote validation before starting the transaction
const response = await fetch('/api/validate');
const metadata = await response.json();
// 2. Open transaction and commit atomically without inter-turn async pauses
const tx = db.transaction(['documents'], 'readwrite');
const store = tx.objectStore('documents');
const doc = await promisifyRequest(store.get(docId));
doc.metadata = metadata;
await promisifyRequest(store.put(doc));
}
```

### 4. Advanced Range Queries & Storage Persistence

Querying subsets of data using IDBKeyRange and requesting persistent storage to prevent browser eviction under low disk space:

```javascript
// Querying documents updated between two timestamps
async function getRecentDocuments(db, startTimestamp, endTimestamp) {
const tx = db.transaction(['documents'], 'readonly');
const index = tx.objectStore('documents').index('by_updated');
// IDBKeyRange.bound(lower, upper, lowerOpen, upperOpen)
const range = IDBKeyRange.bound(startTimestamp, endTimestamp, false, false);
const results = [];
return new Promise((resolve, reject) => {
const request = index.openCursor(range, 'prev'); // 'prev' = descending order
```

request.onsuccess = (event) => {

```javascript
const cursor = event.target.result;
if (cursor) {
results.push(cursor.value);
cursor.continue(); // Advance cursor to next record
} else {
resolve(results); // Cursor iteration complete
}
};
request.onerror = () => reject(request.error);
});
}
// Request Persistent Storage Quota
async function requestPersistence() {
if (navigator.storage && navigator.storage.persist) {
const isPersisted = await navigator.storage.persist();
const estimate = await navigator.storage.estimate();
console.log(`Persistent: ${isPersisted}, Quota: ${(estimate.quota / 1e9).toFixed(2)} GB`);
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### IndexedDB Key Range & Cursor Reference:

| **Method** | **Matches** | **Example** |
| --- | --- | --- |
| IDBKeyRange.only(val) | Exactly equal to val | IDBKeyRange.only("folder_123") |
| IDBKeyRange.lowerBound(val, open) | $\ge val$ (or $> val$ if open: true)   IDBKe | Range.lowerBound(100, true) |
| IDBKeyRange.upperBound(val, open) | $\le val$ (or $< val$ if open: true)   IDBKe | Range.upperBound(500, false) |
| IDBKeyRange.bound(low, high, lOpen, uOpen) | Between low and high | IDBKeyRange.bound(100, 200, false, false) |

### Storage Persistence API:

```javascript
// Check quota and usage
const { usage, quota } = await navigator.storage.estimate();
const percentUsed = ((usage / quota) * 100).toFixed(2);
// Request persistent storage (prevents automatic LRU browser eviction)
const isPersisted = await navigator.storage.persist();
const isAlreadyPersisted = await navigator.storage.persisted();
```

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Multi-Entry Array Index Query Prediction

Analyze the schema and records below:

```javascript
// Object Store: 'tasks' (keyPath: 'id')
// Index: 'by_assignees' (keyPath: 'assignees', multiEntry: true)
// Records in Store:
// Task 1: { id: 1, title: 'Auth', assignees: ['alice', 'bob'] }
// Task 2: { id: 2, title: 'DB', assignees: ['bob', 'charlie'] }
// Task 3: { id: 3, title: 'UI', assignees: ['alice'] }
const tx = db.transaction(['tasks'], 'readonly');
const index = tx.objectStore('tasks').index('by_assignees');
const results = await promisifyRequest(index.getAll('bob'));
```

*Question*: What is the exact array returned in results? What would happen if multiEntry: false was set instead when querying 'bob'?

*Hint*: Understand the difference between matching an exact array instance vs indexing individual scalar elements within an array.

### Challenge 2: Typesafe Promise-Based IndexedDB Transaction Engine

Refactor the verbose callback-based IndexedDB API into a clean, modern, typesafe Promise utility createDatabaseClient<TSchema>:

**Requirements**:

1.  Supports atomic read(storeName, key) and write(storeName, value).

2.  Automatically handles transaction aborts, errors, and promise resolution on tx.oncomplete.

3.  Ensures transactions cleanly rollback if any operation within the batch throws.

```javascript
// Legacy Callback Hell:
const tx = db.transaction(['users'], 'readwrite');
const store = tx.objectStore('users');
const req = store.put({ id: 'u1', name: 'Alice' });
req.onsuccess = () => { /* ... */ };
```

### Challenge 3: Encrypted Offline Document Vault in TypeScript

Build an **Offline-First Encrypted Document Store** using IndexedDB and Web Crypto API:

**Requirements**:

1.  **Schema**:

    - Store 'vault' with primary key 'id', index 'by_folder', and multiEntry index 'by_tags'.

2.  **Encryption Engine**:

    - Accepts a user master passphrase and derives a 256-bit AES-GCM key using PBKDF2 (100,000 iterations).

    - Automatically encrypts the content (large markdown/binary text) with a unique 12-byte IV before storing in IndexedDB.

    - Leaves search metadata (id, folderId, tags, updatedAt) in unencrypted plaintext so IndexedDB indexes continue to function.

3.  **Query Engine**:

    - searchByTag(tag: string): Queries the by_tags index and decrypts all matching documents in parallel.

    - exportBackup(): Dumps the entire encrypted store as a single exportable JSON backup file.
