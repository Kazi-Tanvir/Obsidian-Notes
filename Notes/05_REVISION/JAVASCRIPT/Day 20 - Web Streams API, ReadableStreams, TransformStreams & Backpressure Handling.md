tags:

- javascript

- streams

- web-streams

- backpressure

- async-js

- performance

- memory-optimization date: 2026-08-20

# Day 20 - Web Streams API, ReadableStreams, TransformStreams & Backpressure Handling

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The WHATWG Web Streams API Standard

The **Web Streams API** provides a standardized, runtime-agnostic (browsers, Node.js 18+, Deno, Cloudflare Workers) abstraction for reading, transforming, and writing streaming data chunk-by-chunk without loading entire payloads into RAM.

#### Core Stream Primitives:

- **ReadableStream**: Represents a source of data chunks you can consume sequentially.

- **WritableStream**: Represents a destination sink that receives data chunks.

- **TransformStream**: Chains a readable and writable stream together to mutate or filter chunks on the fly (e.g., decompression, encryption, JSON parsing).

\[ Data Source \] ──► ReadableStream ──► TransformStream ──► WritableStream ──► \[ Destination Sink \]

### 2. Lockers, Readers & Stream Consumption

A ReadableStream can only have **one active reader (lock)** at a time to prevent conflicting consumption positions.

// Consuming a ReadableStream chunk-by-chunk

const response = await fetch(\"https://api.example.com/stream-data\");

const reader = response.body.getReader(); // Locks the stream

try {

while (true) {

const { done, value } = await reader.read(); // value is Uint8Array

if (done) {

console.log(\"\[Stream\]: All chunks consumed.\");

break;

}

console.log(\`\[Stream\]: Received \${value.byteLength} bytes.\`);

}

} finally {

reader.releaseLock(); // Releases lock for other consumers

}

### 3. Understanding & Enforcing Backpressure

**Backpressure** is the flow-control mechanism where a slow consumer signals a fast producer to slow down or pause generation, preventing memory buffer bloat and Out-Of-Memory (OOM) application crashes.

#### Queuing Strategies & desiredSize:

- Streams use an internal queue governed by a **highWaterMark** (HWM).

- **controller.desiredSize**: Indicates how many more bytes/chunks the stream can accept before exceeding capacity.

  - \$\\text{desiredSize} \> 0\$: Producer can keep enqueueing data.

  - \$\\text{desiredSize} \\le 0\$: Producer **must pause** and await drain signals.

// Custom ReadableStream with explicit Backpressure Flow Control

const stream = new ReadableStream({

start(controller) {

console.log(\"\[Stream\]: Started\");

},

async pull(controller) {

// pull() is invoked automatically by the engine ONLY when desiredSize \> 0!

const chunk = await fetchNextChunkFromHardware();

if (chunk) {

controller.enqueue(chunk);

} else {

controller.close();

}

},

cancel(reason) {

console.log(\"\[Stream\]: Consumer aborted stream:\", reason);

}

}, new ByteLengthQueuingStrategy({ highWaterMark: 1024 \* 64 })); // 64 KB HighWaterMark

### 4. TransformStreams & Real-Time AI LLM Streaming

// Real-time Text Decoding Transform Stream

const textDecoderStream = new TextDecoderStream();

const response = await fetch(\"https://api.openai.com/v1/chat/completions\", {

method: \"POST\",

body: JSON.stringify({ stream: true })

});

// Piping chunks seamlessly through transform layers

const readableTextStream = response.body.pipeThrough(textDecoderStream);

for await (const textChunk of readableTextStream) {

process.stdout.write(textChunk);

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

### ReadableStream Controller Methods:

- controller.enqueue(chunk): Pushes a chunk into the stream\'s internal queue.

- controller.close(): Closes the stream, signaling EOF (End of File).

- controller.error(err): Immediately faults the stream with an error.

- controller.desiredSize: Returns integer capacity remaining in the queue.

### Stream Piping & Branching Methods:

- readable.pipeThrough(transformStream): Chains readable into transform and returns new readable.

- readable.pipeTo(writableStream): Pumps readable into writable and manages backpressure automatically.

- const \[branchA, branchB\] = readable.tee(): Splits a single readable stream into two identical branches.

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Stream Lock Conflict & Teeing Prediction

Predict the console output and thrown error in the code below. Explain why the second read fails and how stream.tee() resolves the issue.

const stream = new ReadableStream({

start(c) { c.enqueue(\"Chunk 1\"); c.close(); }

});

const reader1 = stream.getReader();

const reader2 = stream.getReader(); // What happens here?

*Hint*: Focus on the stream\'s internal \[\[disturbed\]\] and \[\[locked\]\] boolean state flags.

### Challenge 2: Custom Line-Delimited JSON (NDJSON) TransformStream

Build a robust NDJSONTransformStream class using TransformStream in TypeScript:

1.  Accepts raw string chunks containing partial/fragmented JSON lines separated by \\n.

2.  Buffers leftover text across chunk boundaries.

3.  Emits fully parsed JavaScript objects downstream as soon as a newline delimiter is encountered.

*Hint*: Maintain an internal buffer string in the transform state and split by \\n.

### Challenge 3: Building a Backpressure-Aware Rate-Limited File Compressor

Build a high-performance Stream Pipeline compressAndUploadStream(readableSource, uploadEndpoint) in TypeScript:

1.  Pipes an incoming binary ReadableStream through CompressionStream(\"gzip\").

2.  Intercepts chunks with a custom rate-limiting TransformStream that caps throughput to \$5 \\text{ MB/s}\$ using controller.desiredSize and timestamp delays.

3.  Pipes the compressed output into a destination WritableStream that simulates slow network uploads without exceeding memory limits.

*Hint*: Use await new Promise(r =\> setTimeout(r, delay)) inside the transform() handler to throttle chunk throughput.
