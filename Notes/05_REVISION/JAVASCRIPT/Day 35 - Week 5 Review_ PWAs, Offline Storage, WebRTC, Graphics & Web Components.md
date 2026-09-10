---
tags:
  - javascript
  - web-components
  - service-workers
  - webrtc
  - indexeddb
  - webgl
  - canvas
  - pwa
  - architecture
  - performance
date: 2026-09-04
---

# Day 35 - Week 5 Review: PWAs, Offline Storage, WebRTC, Graphics & Web Components

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Week 5 Architectural Synthesis: The Modern Browser Platform

Week 5 examined the browser not merely as a document viewer, but as a full-fledged, multi-threaded operating system runtime. Integrating these foundational platform capabilities creates applications that are offline-resilient, GPU-accelerated, peer-to-peer capable, and modularly encapsulated:

┌────────────────────────────────────── Modern Web Platform Architecture ──────────────────────────────────────┐

│                                                                                                              │

│  UI / Component Layer (Main Thread)                                                                          │

│  • Autonomous Custom Elements & Shadow DOM (`<custom-element>`)                                              │

│  • Style & DOM Isolation (`attachShadow({ mode: 'open' })`) \+ Declarative Shadow DOM (SSR)                   │

│         │                                                                                                    │

│         ├───────────────────────────────┬──────────────────────────────────┬─────────────────────────────────┤

│         ▼                               ▼                                  ▼                                 │

│  Offline Persistence            Multi-Threaded Compute           Hardware Acceleration        Real-Time P2P  │

│  • IndexedDB (Object Stores)    • Web Workers (Dedicated)        • OffscreenCanvas & WebGL2   • WebRTC       │

│  • Service Worker (Cache API)   • Service Workers (Fetch/Sync)   • GPU Render Pipeline        • DataChannels │

│  • Background Sync Queue        • Atomics & SharedArrayBuffer    • Frame Delta Loops          • STUN / TURN  │

│                                                                                                              │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. High-Performance Integration: Offloading to OffscreenCanvas & Web Workers

To maintain a consistent 60/120 FPS frame budget ($\\le 16.6\\text{ms}$ or $8.3\\text{ms}$ per frame), CPU-heavy data parsing, physics simulation, or complex canvas painting must never block the main execution thread.

// Main Thread: Custom Element Binding with OffscreenCanvas

class GpuVisualizer extends HTMLElement {

  #worker;

  #canvas;

  connectedCallback() {

    const shadow \= this.attachShadow({ mode: 'open' });

    shadow.innerHTML \= `

      <style>

        :host { display: block; width: 100%; height: 100%; min-height: 400px; }

        canvas { width: 100%; height: 100%; display: block; }

      </style>

      <canvas id="gpu-canvas"></canvas>

    `;

    this.#canvas \= shadow.querySelector('#gpu-canvas');

    this.#canvas.width \= this.clientWidth * window.devicePixelRatio;

    this.#canvas.height \= this.clientHeight * window.devicePixelRatio;

    // Transfer control of canvas to a Dedicated Web Worker!

    const offscreen \= this.#canvas.transferControlToOffscreen();

    this.#worker \= new Worker(new URL('./render.worker.js', import.meta.url), { type: 'module' });



    // Transfer offscreen canvas memory ownership (Zero-copy transfer!)

    this.#worker.postMessage({ type: 'INIT', canvas: offscreen }, [offscreen]);

  }

  disconnectedCallback() {

    this.#worker?.terminate();

  }

}

customElements.define('gpu-visualizer', GpuVisualizer);

---

### 3. Resilient Offline-First Data Synchronization Loop

┌──────────────────────────────────── Offline-First Mutation Lifecycle ────────────────────────────────────┐

│                                                                                                          │

│  1. User Performs Action (e.g. Save Document / Draw Stroke)                                              │

│     │                                                                                                    │

│     ▼                                                                                                    │

│  2. Optimistic Local Persistence ──► Write to IndexedDB (Immediate local UI update)                      │

│     │                                                                                                    │

│     ├──[Online]────────► Dispatch fetch() request with Idempotency Key ──► Remote Server Success        │

│     │                                                                                                    │

│     └──[Offline]───────► Register Service Worker Background Sync ('sync-mutations')                     │

│                            │                                                                             │

│                            ▼ (Network Connectivity Restores)                                             │

│                          Service Worker wakes up in background ──► Reads IndexedDB Pending Queue         │

│                            └──► Replays HTTP requests with Idempotency Key ──► Mark Synced               │

│                                                                                                          │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Browser Platform Capabilities Matrix:

| Technology | Thread Context | Persistence Type | Primary Benefit | Key APIs |
| :---- | :---- | :---- | :---- | :---- |
| **Custom Elements** | Main Thread | DOM Scope | Encapsulated UI components | `customElements.define`, `ElementInternals` |
| **Shadow DOM** | Main Thread | DOM Scope | Scoped CSS & boundary isolation | `attachShadow`, `composedPath()` |
| **Service Workers** | Worker Thread | Cache Storage | Offline caching, background sync | `caches.open`, `self.skipWaiting()`, `SyncManager` |
| **IndexedDB** | Async (Main/Worker) | Disk (Structured) | Multi-GB transactional client database | `indexedDB.open`, `IDBKeyRange`, `onupgradeneeded` |
| **WebRTC** | Native Media Stack | Ephemeral | Sub-100ms P2P audio/video/data mesh | `RTCPeerConnection`, `RTCDataChannel` |
| **OffscreenCanvas** | Worker Thread | VRAM / GPU | 60 FPS graphics off main thread | `transferControlToOffscreen()`, WebGL2 |

---

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Lifecycle & Context Leaks in Complex Web Components

Analyze the potential memory leak in the Web Component below:

class LiveDataGraph extends HTMLElement {

  connectedCallback() {

    const shadow \= this.attachShadow({ mode: 'open' });

    const canvas \= document.createElement('canvas');

    shadow.appendChild(canvas);

    window.addEventListener('resize', () \=> this.resizeCanvas(canvas));

    this.channel \= new BroadcastChannel('telemetry');

    this.channel.onmessage \= (e) \=> this.draw(canvas, e.data);

  }

}

customElements.define('live-data-graph', LiveDataGraph);

*Question*: What happens when an instance of `<live-data-graph>` is removed from the DOM? Identify the 2 major memory leaks and rewrite the component to guarantee garbage collection via `disconnectedCallback()`.

---

### Challenge 2: P2P Offline Mesh Synchronization

Design a data synchronization mechanism for two peer browsers sharing an encrypted document over WebRTC:

1. If both peers are online, mutations stream across `RTCDataChannel` with low latency.
2. If the receiving peer goes offline, the sending peer queues changes in local `IndexedDB`.
3. When the peer reconnects, reconcile the document versions using vector clocks or CRDTs without loss of concurrent edits.

---

### Challenge 3: Autonomous Real-Time Collaborative Whiteboard Component

Build an Enterprise **Autonomous Collaborative Whiteboard Component** (`<p2p-whiteboard>`) in TypeScript:

**Requirements**:

1. **Encapsulation & Graphics**:
   - Custom Element using Shadow DOM.
   - Renders drawing paths using HTML5 Canvas or `OffscreenCanvas` with smooth quadratic bezier curves and sub-pixel touch/pointer support.
2. **P2P Synchronization (`RTCDataChannel`)**:
   - Broadcasts real-time stroke coordinates (`x`, `y`, `pressure`, `color`) to connected peers over an active `RTCDataChannel`.
   - Regulates network backpressure by monitoring `dataChannel.bufferedAmount`.
3. **Offline Persistence & Replay**:
   - Persists all local and remote drawing strokes into **IndexedDB**.
   - On page reload while offline, instantly rehydrates and redraws the whiteboard state from IndexedDB.

