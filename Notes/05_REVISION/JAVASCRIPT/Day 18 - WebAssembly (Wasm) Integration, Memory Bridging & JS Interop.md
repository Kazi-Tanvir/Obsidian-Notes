---
tags:
- javascript
- webassembly
- wasm
- memory-management
- performance
- linear-memory
- c-cpp-rust
date: 2026-08-18
---

# Day 18 - WebAssembly (Wasm) Integration, Memory Bridging & JS Interop

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. What is WebAssembly (Wasm)?

**WebAssembly (Wasm)** is a low-level, binary instruction format designed as a portable compilation target for high-performance languages (Rust, C++, Go, Zig) running alongside JavaScript in the browser and Node.js.

#### Architecture Highlights:

- **Stack Machine Execution**: Instructions push and pop values from an implicit evaluation stack.

- **Predictable Performance**: Executes at near-native CPU speed without JIT warm-up cycles or unexpected GC pauses.

- **Sandboxed Security**: Executes within the same security sandbox and memory boundaries as the host JavaScript runtime.

### 2. The Wasm Linear Memory Model

WebAssembly code does not access the host JavaScript heap directly. Instead, it operates on a contiguous, resizable array of raw bytes known as **Linear Memory**, represented in JavaScript by WebAssembly.Memory.

- **Page Sizing**: Wasm memory is allocated in fixed **64 KB pages** ($1 \text{ page} = 65,536 \text{ bytes}$).

- **Memory Growth**: The memory buffer can dynamically expand via memory.grow(numPages).

- **TypedArray Views**: JavaScript accesses Wasm linear memory by mapping typed views (Uint8Array, Float32Array, DataView) over memory.buffer.

```javascript
// Initializing Wasm Linear Memory in JavaScript
// Initial: 2 pages (128 KB), Maximum: 10 pages (640 KB)
const memory = new WebAssembly.Memory({ initial: 2, maximum: 10 });
const view = new Uint8Array(memory.buffer);
view[0] = 42; // Writing byte into Wasm memory address 0
console.log(`Memory size: ${memory.buffer.byteLength} bytes`); // 131072
```

### 3. JavaScript & WebAssembly Interoperability

By default, Wasm functions only exchange primitive numerical types: i32, i64, f32, f64. Passing complex data structures (strings, JSON objects, arrays) requires manual serialization across linear memory using pointers and byte offsets.

#### Streaming Instantiation Pattern:

The optimal way to compile and load Wasm modules over the network is WebAssembly.instantiateStreaming(), which compiles bytecode in parallel as network chunks arrive.

```javascript
// Fast Streaming Compilation & String Passing Example
async function loadWasmModule() {
const memory = new WebAssembly.Memory({ initial: 2 });
const importObject = {
```

env: {

memory,

logOffset: (ptr, length) => {

```javascript
// Decode UTF-8 string directly from Wasm linear memory pointer
const bytes = new Uint8Array(memory.buffer, ptr, length);
const text = new TextDecoder("utf-8").decode(bytes);
console.log(`[Wasm Log]: ${text}`);
}
}
};
const { instance } = await WebAssembly.instantiateStreaming(
```

fetch("/module.wasm"),

importObject

```javascript
);
return { instance, memory };
}
```

#### Writing Strings from JS into Wasm Memory:

```javascript
function writeStringToWasmMemory(wasmMemory, offset, str) {
const encoder = new TextEncoder();
const encodedBytes = encoder.encode(str);
const memoryView = new Uint8Array(wasmMemory.buffer);
memoryView.set(encodedBytes, offset);
return { ptr: offset, length: encodedBytes.length };
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Global WebAssembly API Methods:

- WebAssembly.instantiateStreaming(responsePromise, importObject): Compiles & instantiates Wasm directly from a network stream.

- WebAssembly.instantiate(bytesOrModule, importObject): Compiles & instantiates from an ArrayBuffer.

- WebAssembly.compileStreaming(responsePromise): Compiles into a WebAssembly.Module without instantiating.

- new WebAssembly.Memory({ initial, maximum?, shared? }): Creates resizable linear memory instance.

- new WebAssembly.Table({ element: "anyfunc", initial, maximum? }): Creates function pointer tables for dynamic dispatch.

### Memory Constants & Formula:

- **1 Wasm Page** = $64 \text{ KiB} = 65,536 \text{ bytes}$.

- **Byte Offset Formula**: $\text{Address} = (\text{Page Index} \times 65536) + \text{Local Offset}$.

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Memory Buffer Invalidation Prediction on grow()

Examine the code snippet below. Predict what error occurs on the final line and explain the underlying V8/Wasm memory detachment mechanics.

```javascript
const memory = new WebAssembly.Memory({ initial: 1, maximum: 5 });
const initialView = new Uint8Array(memory.buffer);
initialView[0] = 100;
// Memory grows by 1 page (64 KB)
memory.grow(1);
// What happens here?
console.log(initialView[0]);
```

*Hint*: When memory.grow() is invoked, what happens to the previous underlying ArrayBuffer instance and all existing TypedArray views attached to it?

### Challenge 2: Refactoring CPU-Bound Image Inversion to Wasm Linear Memory

Given a 4K RGBA image ($3840 \times 2160 \times 4$ bytes $\approx 33.17 \text{ MB}$):

1.  Calculate the minimum number of 64 KB Wasm pages required to allocate the full pixel buffer.

2.  Write a JavaScript helper that transfers the ImageData pixel array into Wasm linear memory, invokes an exported invertPixels(ptr, length) Wasm function, and writes the transformed pixels back to a canvas context without intermediate object allocations.

*Hint*: Use memory.grow() to allocate $\ge 33.2 \text{ MB}$ and map a Uint8ClampedArray directly to the pointer offset.

### Challenge 3: Building a Zero-Copy Struct Serializer & Bridge in TypeScript

Build a high-performance **WasmStructBridge** in TypeScript:

1.  Define a C-compatible struct format for 3D Game Entities:

    - id: Uint32 (4 bytes, offset 0)

    - x, y, z: Float32 (12 bytes, offsets 4, 8, 12)

    - health: Uint8 (1 byte, offset 16)

    - padding: 3 bytes (alignment to 20-byte boundary)

2.  Implement writeEntities(entities: Entity[]): { ptr: number; count: number } that packs 10,000 entity records into a contiguous block in Wasm linear memory.

3.  Implement readEntities(ptr: number, count: number): Entity[] that reads back entity records by reference using DataView without cloning memory.

*Hint*: Ensure byte alignments follow 4-byte struct padding rules.
