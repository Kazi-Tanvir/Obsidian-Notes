---
tags:
- backend
- websockets
- sse
- redis
- realtime
- socket-io
- system-design
date: 2026-08-17
---

# Day 17 - Real-Time Architecture: WebSockets, Socket.io, SSE & Redis Pub-Sub Scaling

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Real-Time Protocol Landscape: SSE vs. WebSockets

Choosing the right communication protocol depends on data directionality, binary data needs, and firewall traversal.

| **Protocol Characteristic** | **Server-Sent Events (SSE)** | **WebSockets (ws://, wss://)** |
| --- | --- | --- |
| **Directionality** | Unidirectional (Server -> Client only) | ull-Duplex (Bidirectional Client <-> Server) |
| **Transport Protocol** | Standard HTTP/1.1 or HTTP/2 | Upgraded TCP connection (101 Switching Protocols) |
| **Data Format** | UTF-8 Text only (text/event-stream) | Text (UTF-8) and Binary (ArrayBuffer, Blob) |
| **Reconnection & IDs** | Built-in native browser auto-reconnect (Last-Event-ID) | Manual application-level heartbeat & reconnection |
| **Best Use Cases** | Stock tickers, AI LLM token streaming, notifications | Live chat, multi-player gaming, collaborative whiteboards |

### 2. Scaling WebSockets Horizontally with Redis Pub/Sub

WebSockets establish persistent, stateful TCP sockets tied to a specific server process. When scaling across multiple load-balanced instances, Client A connected to Server 1 cannot natively message Client B connected to Server 2.

#### Multi-Node Cluster Architecture with Redis Adapter:

[ Client A ] [ Client B ]

│ │

▼ (WebSocket) ▼ (WebSocket)

┌──────────────┐ ┌──────────────┐

│ API Server 1 │ │ API Server 2 │

└──────┬───────┘ └──────┬───────┘

│ ▲

▼ (PUBLISH 'room:101') │ (SUBSCRIBE 'room:101')

═════════════════════════════════════════

[ Redis Pub/Sub ]

═════════════════════════════════════════

1.  Client A sends message to Server 1.

2.  Server 1 publishes event to Redis channel (room:101).

3.  Redis broadcasts message to all subscribed server nodes (Server 2, Server 3).

4.  Server 2 receives message from Redis and pushes it down the active WebSocket connection to Client B.

### 3. Connection Health: Heartbeats, Ping/Pong & Zombie Connection Pruning

Mobile networks and NAT routers silently drop idle TCP sockets without sending FIN packets, creating **Zombie Sockets** that consume server memory and file descriptors.

```typescript
// Production WebSocket Heartbeat & Dead Socket Termination
import { WebSocketServer, WebSocket } from 'ws';
interface ExtendedWebSocket extends WebSocket {
isAlive: boolean;
userId?: string;
}
const wss = new WebSocketServer({ port: 8080 });
wss.on('connection', (ws: ExtendedWebSocket) => {
ws.isAlive = true;
// Client responds with 'pong' when pinged
ws.on('pong', () => {
ws.isAlive = true;
});
});
// Periodic Heartbeat Interval (Runs every 30 seconds)
const interval = setInterval(() => {
```

wss.clients.forEach((client) => {

```javascript
const ws = client as ExtendedWebSocket;
if (!ws.isAlive) {
console.log('[WebSocket]: Terminating unresponsive zombie socket.');
return ws.terminate(); // Force close broken connection
}
ws.isAlive = false;
ws.ping(); // Send ping frame to client
});
}, 30000);
wss.on('close', () => clearInterval(interval));
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Server-Sent Events (SSE) Response Headers:

HTTP/1.1 200 OK

Content-Type: text/event-stream

Cache-Control: no-cache, no-transform

Connection: keep-alive

X-Accel-Buffering: no

### SSE Event Stream Formatting:

event: price-update

id: 10492

data: {"symbol": "NVDA", "price": 142.50}

### Socket.io Redis Adapter Setup:

```javascript
import { Server } from 'socket.io';
import { createAdapter } from '@socket.io/redis-adapter';
import { createClient } from 'redis';
const pubClient = createClient({ url: 'redis://localhost:6379' });
const subClient = pubClient.duplicate();
await Promise.all([pubClient.connect(), subClient.connect()]);
const io = new Server(3000, {
```

adapter: createAdapter(pubClient, subClient)

```javascript
});
```

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Global Collaborative Real-Time Document Editor)

Design a horizontally scalable real-time collaborative workspace infrastructure (like Google Docs / Figma) supporting 500k concurrent active collaborators.

**Requirements**:

1.  Choose between WebSockets, SSE, and WebRTC for document cursor synchronization and text conflict resolution (Operational Transformation / CRDTs).

2.  Diagram the Load Balancer layer (HAProxy / AWS ALB with sticky session options vs stateless token-based WebSocket routing).

3.  Detail how Redis Pub/Sub or Redis Streams handles room partitioning so that only servers hosting users in Document #492 receive its updates.

### Problem 2: End-to-End Code Implementation Challenge

Build a production-grade **Real-Time Notification & Room Broadcast Hub** in Node.js / TypeScript.

**Requirements**:

1.  Implement a Fastify/ws server exposing:

    - GET /api/v1/events/stream: SSE endpoint for lightweight, read-only user alerts with Last-Event-ID resume capability.

    - WS /api/v1/realtime: Full-duplex WebSocket endpoint for bi-directional chat rooms.

2.  Integrate ioredis Pub/Sub so that messages sent into a room on one instance are broadcasted to users connected to other instances.

3.  Add a ping/pong heartbeat daemon that purges unresponsive sockets every 25 seconds.

4.  Include test scripts simulating multi-client room messaging across isolated mock WebSocket connections.
