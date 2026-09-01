tags:

- backend

- grpc

- protobuf

- microservices

- http2

- rpc date: 2026-08-15

# Day 15 - gRPC, Protocol Buffers & Inter-Service Microservice Communication

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Need for gRPC in Microservice Meshes

While REST over HTTP/1.1 with JSON payloads is common for public-facing client APIs, it introduces high latency and serialization overhead for internal microservice-to-microservice communication.

#### REST vs. gRPC Architectural Comparison:

  ---------------------------------------------------------------------------------------------------------------------------------
  **Architectural Metric**    **REST / JSON**                           **gRPC / Protocol Buffers**
  --------------------------- ----------------------------------------- -----------------------------------------------------------
  **Transport Layer**         HTTP/1.1 (or HTTP/2)                      HTTP/2 Native (Multiplexing, Header Compression)

  **Data Serialization**      Text-based JSON (Large overhead)          Binary Protocol Buffers (Compact, High-speed)

  **API Contract**            OpenAPI / Swagger (Optional, decoupled)   .proto IDL file (Strict, Required, Code-generated)

  **Streaming Support**       Unary (or WebSockets / SSE)               Unary, Client Streaming, Server Streaming, Bi-Directional

  **Browser Compatibility**   100% Native                               Requires gRPC-Web proxy / Envoy bridge
  ---------------------------------------------------------------------------------------------------------------------------------

### 2. Protocol Buffers (Protobuf) IDL & Binary Packing

Protocol Buffers define schemas in a language-agnostic .proto file. Each field is assigned a numbered tag (e.g. int32 id = 1;). Protobuf encodes field tags and raw bytes without repeating property names, reducing payload sizes by 60--80% compared to JSON.

// auth.proto

syntax = \"proto3\";

package auth;

service AuthService {

// 1. Unary RPC: Single request -\> Single response

rpc VerifyToken (TokenRequest) returns (TokenResponse);

// 2. Server Streaming RPC: Single request -\> Continuous Stream of events

rpc StreamSecurityEvents (EventFilter) returns (stream SecurityEvent);

}

message TokenRequest {

string token = 1;

string required_role = 2;

}

message TokenResponse {

bool is_valid = 1;

string user_id = 2;

repeated string permissions = 3;

}

message EventFilter {

string environment = 1;

}

message SecurityEvent {

string event_id = 1;

string timestamp = 2;

string severity = 3;

string description = 4;

}

### 3. Implementing a gRPC Server in Node.js / TypeScript

Using \@grpc/grpc-js and \@grpc/proto-loader, Node.js microservices compile .proto files dynamically or via static types.

// server.ts - High-Performance gRPC Microservice

import \* as grpc from \'@grpc/grpc-js\';

import \* as protoLoader from \'@grpc/proto-loader\';

path from \'path\';

const PROTO_PATH = path.resolve(\_\_dirname, \'auth.proto\');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {

keepCase: true,

longs: String,

enums: String,

defaults: true,

oneofs: true,

});

const authProto = (grpc.loadPackageDefinition(packageDefinition) as any).auth;

// Unary RPC Handler Implementation

function verifyToken(

call: grpc.ServerUnaryCall\<any, any\>,

callback: grpc.sendUnaryData\<any\>

) {

const { token, required_role } = call.request;

if (!token) {

return callback({

code: grpc.status.INVALID_ARGUMENT,

message: \'Token is required\',

});

}

// Simulated Verification

const isValid = token.startsWith(\'bearer\_\');

callback(null, {

is_valid: isValid,

user_id: \'usr_789\',

permissions: \[\'read:orders\', \'write:orders\'\],

});

}

// Server Initialization

const server = new grpc.Server();

server.addService(authProto.AuthService.service, { verifyToken });

server.bindAsync(

\'0.0.0.0:50051\',

grpc.ServerCredentials.createInsecure(),

(err, port) =\> {

if (err) throw err;

console.log(\`\[gRPC Service\]: Listening on port \${port}\`);

}

);

### 4. gRPC Deadlines, Timeouts & Metadata Context

Unlike REST where requests often hang indefinitely on slow backends, gRPC enforces strict **Deadlines**. Deadlines propagate across multi-tier microservice calls (Service A -\> Service B -\> Service C), automatically aborting downstream processing if the top-level timeout expires.

## SECTION 2: DOCUMENTATION CHEAT SHEET

  -------------------------------------------------------------------------------
  **gRPC Status Code**    **Name**                **Corresponding HTTP Status**
  ----------------------- ----------------------- -------------------------------
  **0**                   OK                      200 OK

  **3**                   INVALID_ARGUMENT        400 Bad Request

  **4**                   DEADLINE_EXCEEDED       504 Gateway Timeout

  **5**                   NOT_FOUND               404 Not Found

  **7**                   PERMISSION_DENIED       403 Forbidden

  **14**                  UNAVAILABLE             503 Service Unavailable

  **16**                  UNAUTHENTICATED         401 Unauthorized
  -------------------------------------------------------------------------------

### CLI Testing Commands (grpcurl)

\# List all services on a gRPC server with reflection enabled

grpcurl -plaintext localhost:50051 list

\# Invoke a Unary RPC method

grpcurl -plaintext -d \'{\"token\": \"bearer_abc\", \"required_role\": \"admin\"}\' \\

localhost:50051 auth.AuthService/VerifyToken

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (High-Throughput Financial Order Routing Mesh)

Design a low-latency gRPC-based microservice architecture for a High-Frequency Order Execution platform.

**Requirements**:

1.  Diagram the inter-service communication flow across 3 services: API Gateway (REST/Next.js) -\> Order Matching Engine (gRPC) -\> Risk Management Service (gRPC).

2.  Formulate .proto schema definitions for PlaceOrder, CancelOrder, and StreamLiveOrderBook (Server Streaming).

3.  Detail how gRPC Deadline propagation and Envoy Load Balancing prevent cascade failures during sudden market volatility volume spikes (100k requests/sec).

### Problem 2: End-to-End Code Implementation Challenge

Build a production-ready **gRPC User & Permission Verification Microservice** in Node.js / TypeScript.

**Requirements**:

1.  Write a .proto file defining UserService with:

    - GetUser(UserIdRequest) returns (UserResponse) (Unary).

    - StreamAuditLogs(AuditFilter) returns (stream AuditLogEntry) (Server Streaming).

2.  Implement the gRPC server handling requests with input validation, returning standard grpc.status codes (NOT_FOUND, INVALID_ARGUMENT).

3.  Build a client wrapper class UserServiceClient that configures a 2-second Deadline timeout, automated connection retry with exponential backoff, and a unary Promisified call wrapper.

4.  Include unit/integration tests verifying deadline timeout handling and successful protobuf serialization.
