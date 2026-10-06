---
tags:
  - backend
  - realtime
  - crdt
  - yjs
  - websockets
  - collaborative-editing
  - system-design
  - architecture
date: 2026-09-14
---

# Day 45 - Real-Time Collaborative Editing, CRDTs (Yjs / Automerge), Operational Transformation & WebSockets

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Distributed Collaborative Editing Challenge

Enabling multiple users to type, edit, and draw in real-time across high-latency, unreliable networks (e.g. Google Docs, Figma, Notion) introduces fundamental consistency challenges:

- **Concurrency**: User A inserts a character at index 5 while User B deletes character at index 4 simultaneously.

- **Latency & Jitter**: Messages arrive out of order, delayed, or duplicated across distributed client nodes.

- **Offline Resynchronization**: A user edits a document offline on a flight for 3 hours, then reconnects to a document that has undergone hundreds of peer modifications.

```text
┌────────────────────────────────────── OT vs. CRDT Architecture ──────────────────────────────────────┐
│                                                                                                       │
│  Operational Transformation (OT) - Centralized Server Model ⚠️                                        │
│  • Client sends raw index operations: Insert(pos: 5, char: 'A').                                      │
│  • Requires a central authoritative server to transform operations against all concurrent edits.      │
│  • Severe weakness: High computational complexity ($O(N^2)$ transformation matrix),                   │
│    fails in peer-to-peer networks, fragile offline reconciliation.                                    │
│                                                                                                       │
│  Conflict-Free Replicated Data Types (CRDT) - Decentralized Math 🚀                                   │
│  • Data structures designed mathematically so that any two replicas that have received the same set  │
│    of updates in ANY order are guaranteed to arrive at the EXACT same state!                         │
│  • Strong Eventual Consistency (SEC): Operations are Commutative, Associative, and Idempotent.        │
│  • Functions peer-to-peer, offline-first, client-server, and scales seamlessly.                      │
│                                                                                                       │
└───────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Anatomy of a Sequence CRDT (Yjs / YATA Algorithm)

Modern collaborative text systems rely on Sequence CRDTs. **Yjs** implements the **YATA (Yet Another Transformation Approach)** algorithm:

1.  **Unique Character Identity**: Every character/item is assigned a globally unique, immutable ID composed of { client: number, clock: number } (a Lamport timestamp).

2.  **Linked List Structure**: Rather than relying on fragile array indices (index 5), characters are stored as a double-linked list linked by reference to their left and right neighbors: { origin: ID_left, right: ID_right, content: 'x' }.

3.  **Deterministic Conflict Resolution**: When two users insert a character at the exact same location, the tie is broken deterministically by comparing client IDs (client_A < client_B), ensuring mathematical convergence across all nodes without a central server.

```text
┌────────────────────────────────────── Yjs State Vector Synchronization ──────────────────────────────────────┐
│                                                                                                              │
│  Peer A (Client 1)                                                               Peer B (Client 2)           │
│  ┌─────────────────────────────────┐                                            ┌─────────────────────────┐  │
│  │ State: Clocks { 1: 15, 2: 8 }   │                                            │ State: Clocks { 1: 10 } │  │
│  └────────────────┬────────────────┘                                            └────────────┬────────────┘  │
│                   │                                                                          │               │
│                   │ 1. Step 1: Send State Vector [ Client 2 has processed up to clock 10 ]   │               │
│                   │ ◄────────────────────────────────────────────────────────────────────────┤               │
│                   │                                                                          │               │
│                   │ 2. Step 2: Compute Delta (Send only updates for Client 1 > 10 & Client 2)│               │
│                   ├─────────────────────────────────────────────────────────────────────────►│               │
│                   │    Binary Encoded Update Payload                                         │               │
│                   │                                                                          │               │
│                   ▼                                                                          ▼               │
│             [ Both Peers Converge to Identical Cryptographic State in O(N) Time! ⚡ ]                        │
│                                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3. Production Node.js WebSocket CRDT Sync Server

import { WebSocketServer, WebSocket } from 'ws';

import * as Y from 'yjs';

// In-Memory Document Room Registry

const rooms = new Map<string, Y.Doc>();

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (socket: WebSocket, req) => {

const roomName = new URL(req.url!, 'http://localhost').searchParams.get('room') || 'default';

let doc = rooms.get(roomName);

if (!doc) {

doc = new Y.Doc();

rooms.set(roomName, doc);

}

// 1. Send initial sync step 1: Server sends its state vector to client

const serverStateVector = Y.encodeStateVector(doc);

socket.send(Buffer.concat([Buffer.from([0]), Buffer.from(serverStateVector)]));

// 2. Listen to incoming binary updates from client

socket.on('message', (message: Buffer) => {

const messageType = message[0];

const payload = message.subarray(1);

if (messageType === 0) {

// Client sent its state vector -> Server computes delta and returns missing updates

const diff = Y.encodeStateAsUpdate(doc, payload);

socket.send(Buffer.concat([Buffer.from([1]), Buffer.from(diff)]));

} else if (messageType === 1) {

// Client sent updates -> Apply to server document!

Y.applyUpdate(doc, payload);

// Broadcast binary update to all other connected clients in the room

wss.clients.forEach((client) => {

if (client !== socket && client.readyState === WebSocket.OPEN) {

client.send(Buffer.concat([Buffer.from([1]), payload]));

}

});

}

});

});

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Operational Transformation (OT) vs. CRDTs:

----------------------------------------------------------------------- **Feature**             **Operational           **CRDT (Yjs / Transformation (OT)**   Automerge)** ----------------------- ----------------------- ----------------------- **Server Architecture** Centralized             Decentralized / authoritative sequencer Peer-to-Peer / Hybrid

**Offline Editing**     Extremely complex       **Native (\$100%\$ (Rebase hell)           seamless)**

**Convergence           Dependent on server     **Mathematical proof Guarantee**             sequencing              (SEC)**

**Memory Efficiency**   High (Small in-memory   High in Yjs (Binary state)                  packed structs)

**Network Protocol**    Strict in-order         Out-of-order, messaging required      at-least-once tolerant -----------------------------------------------------------------------

### Yjs Binary Protocol Core APIs:

// Calculate state vector of known client clocks

const stateVector = Y.encodeStateVector(doc);

// Encode all updates in `doc` missing from `remoteStateVector`

const updateDiff = Y.encodeStateAsUpdate(doc, remoteStateVector);

// Apply binary update chunk to local document

Y.applyUpdate(doc, updateDiff);

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Enterprise Collaborative Workspace Architecture (Figma/Notion-Scale)

Architect a real-time collaborative workspace supporting 500,000 documents with 100 simultaneous concurrent editors per room:

**Requirements**:

1.  **Low-Latency Hybrid Network Mesh**:

    - WebSocket clusters for real-time live presence (user cursor tracking, active selections) and CRDT document mutations.

    - Redis Pub/Sub backplane routing document updates across multiple WebSocket node instances.

2.  **Persistence & Garbage Collection (Snapshots)**:

    - Persisting millions of granular CRDT updates causes document bloat. Design a snapshot compaction worker that compiles historical Yjs updates into a single compact binary blob written to PostgreSQL / S3 every 5 minutes.

3.  **Offline Sync & Reconnection Storm Defense**:

    - Throttling and batching state vector diffs when 50,000 clients reconnect simultaneously following a regional network blip.

### Problem 2: Production-Grade Collaborative Sync Server in TypeScript

Build an Enterprise **Yjs WebSocket Collaboration Server** in TypeScript:

**Requirements**:

1.  **Room Multiplexing & Awareness**:

    - Manages multiple isolated document rooms (/rooms/:roomId).

    - Supports ephemeral user presence (mouse cursor coordinates, user name, avatar) using Yjs Awareness protocol.

2.  **PostgreSQL Checkpointing**:

    - Persists document updates into a PostgreSQL document_updates table.

    - Periodically merges updates into a single base snapshot using Y.mergeUpdates() to maintain fast room initialization times.

3.  **Graceful Connection Cleanup**:

    - Automatically unbinds and cleans up in-memory room documents when all participants disconnect from a room after a 10-minute grace period.
