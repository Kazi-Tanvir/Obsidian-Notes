---
tags:
- javascript
- web-workers
- service-workers
- websockets
- browser-architecture
- realtime
date: 2026-08-11
---

# Day 11 - Web Workers, Service Workers, WebSockets & Real-Time Browser Architecture

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Multithreading in JavaScript & Browser Threads

While JavaScript executes code on a single thread per event loop, modern browsers provide dedicated background threads to execute heavy computations without blocking UI rendering or user interactions.

- **Main Thread**: Handles DOM manipulation, CSS layout, rendering, and UI events.

- **Dedicated Web Workers**: Run background scripts in isolated global scopes (self), communicating via postMessage.

- **Service Workers**: Act as programmable network proxy agents intercepting network requests, enabling offline caching and background sync.

- **Shared Workers**: Shared across multiple browser tabs/windows from the same origin.

### 2. Dedicated Web Workers & Zero-Copy Memory Transfers

Data passed between the Main Thread and Workers undergoes the **Structured Clone Algorithm** by default (deep copy). For high-performance applications handling large datasets (e.g. image manipulation, video encoding), **Transferable Objects** transfer underlying memory ownership instantly ($O(1)$ zero-copy).

```javascript
// main.js - Zero-Copy Memory Transfer
const worker = new Worker('image-processor.js');
// Create 50MB ArrayBuffer
const buffer = new ArrayBuffer(50 * 1024 * 1024);
console.log('Main thread buffer size before transfer:', buffer.byteLength); // 52428800
// Transfer memory ownership (second argument specifies transferables)
worker.postMessage({ imageBuffer: buffer }, [buffer]);
console.log('Main thread buffer size after transfer:', buffer.byteLength); // 0 (Memory detached!)
```

worker.onmessage = (event) => {

```javascript
console.log('Processed buffer received from worker');
};
// image-processor.js (Worker Scope)
```

self.onmessage = (event) => {

```javascript
const { imageBuffer } = event.data;
const view = new Uint8Array(imageBuffer);
// Perform heavy CPU image filter manipulation...
for (let i = 0; i < view.length; i += 4) {
view[i] = 255 - view[i]; // Invert red channel
}
// Transfer back to main thread
self.postMessage({ processedBuffer: imageBuffer }, [imageBuffer]);
};
```

### 3. Service Workers & PWA Offline Caching

Service Workers run independently of web pages, intercepting network requests via the fetch event.

```javascript
// service-worker.js - Stale-While-Revalidate Strategy
const CACHE_NAME = 'app-v1';
self.addEventListener('fetch', (event) => {
event.respondWith(
caches.match(event.request).then((cachedResponse) => {
const fetchPromise = fetch(event.request).then((networkResponse) => {
caches.open(CACHE_NAME).then((cache) => {
cache.put(event.request, networkResponse.clone());
});
return networkResponse;
});
// Return cached version immediately if available, otherwise wait for network
return cachedResponse || fetchPromise;
})
);
});
```

### 4. Real-Time Full-Duplex WebSockets

Unlike HTTP request-response cycles, **WebSockets** establish a single, long-lived, full-duplex TCP connection.

```javascript
// Resilient WebSocket Connection Pattern
class ResilientWebSocket {
constructor(url) {
this.url = url;
this.reconnectInterval = 1000;
this.connect();
}
connect() {
this.ws = new WebSocket(this.url);
```

this.ws.onopen = () => {

```javascript
console.log('Connected to WebSocket server');
this.reconnectInterval = 1000; // Reset backoff
};
```

this.ws.onclose = () => {

```javascript
console.warn(`Connection closed. Reconnecting in ${this.reconnectInterval}ms...`);
```

setTimeout(() => {

```javascript
this.reconnectInterval = Math.min(this.reconnectInterval * 2, 30000); // Exponential backoff
this.connect();
}, this.reconnectInterval);
};
}
send(data) {
if (this.ws.readyState === WebSocket.OPEN) {
this.ws.send(JSON.stringify(data));
}
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **API / Feature** | **Syntax / Method** | **Purpose / Behavior** |
| --- | --- | --- |
| **Worker Instantiation** | const w = new Worker('script.js')                 C | eates background thread |
| **Memory Transfer** | w.postMessage(data, [buffer])                     T | ansfers ownership without copying ($O(1)$) |
| **Service Worker Register** | navigator.serviceWorker.register('/sw.js')        R | gisters network proxy worker |
| **SW Fetch Intercept** | self.addEventListener('fetch', fn)                I | tercepts HTTP requests for offline caching |
| **WebSocket ReadyState** | 0 (CONNECTING), 1 (OPEN), 2 (CLOSING), 3 (CLOSED) | Connection status flags |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Structured Cloning vs Transferable Memory Output Prediction

Analyze the code below and predict the output of console.log statements on both the main thread and worker scope. Explain why data.buffer.byteLength changes.

```javascript
// Main Thread
const data = { buffer: new ArrayBuffer(1024) };
worker.postMessage(data, [data.buffer]);
console.log(data.buffer.byteLength);
// What happens if we attempt to access data.buffer on the main thread after postMessage?
```

*Hint*: Focus on how memory ownership detachment affects ArrayBuffers.

### Challenge 2: Refactoring Blocking Image Filters to Web Workers

Refactor a blocking $10000 \times 10000$ pixel canvas image filter function so that it processes in a Web Worker using OffscreenCanvas or ArrayBuffer transferables, preventing the UI from freezing.

```javascript
// Blocking Main-Thread Code
function applyGrayscale(canvas) {
const ctx = canvas.getContext('2d');
const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
const data = imgData.data;
for (let i = 0; i < data.length; i += 4) {
const avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
data[i] = avg; data[i + 1] = avg; data[i + 2] = avg;
}
ctx.putImageData(imgData, 0, 0); // Causes 500ms UI freeze!
}
```

*Hint*: Pass imgData.data.buffer to the worker as a Transferable.

### Challenge 3: Building a Real-Time Resilient WebSocket Message Queue Manager

Write a production JavaScript class RealtimeSyncEngine(wsUrl) that:

1.  Maintains a WebSocket connection with heartbeat ping/pong to detect stale connections.

2.  Implements an offline message queue that buffers outbound messages when offline (readyState !== OPEN) and flushes them sequentially upon reconnection.

3.  Uses exponential backoff with jitter for automatic reconnection.

*Hint*: Store pending messages in an internal array queue and process with while (queue.length) on onopen.
