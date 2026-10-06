tags:

- javascript

- webassembly

- wasi

- wasm-components

- nodejs

- systems-programming

- performance

- sandboxing date: 2026-09-12

# Day 43 - WebAssembly WASI, Component Model, Bytecode Tooling & Host-Guest Communication

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. WebAssembly Beyond the Browser: The WASI Revolution

While WebAssembly (Wasm) was initially designed to execute
high-performance compiled code within browser sandboxes, its potential
as a universal, lightweight, secure serverless runtime is unlocked by
**WASI (WebAssembly System Interface)**.

Traditional operating system interfaces (POSIX) grant applications
ambient access to system calls (open(), socket(), fork()), leaving
runtimes vulnerable to supply-chain attacks. In contrast, WASI enforces
a **Capability-Based Security Model**:

- A Wasm module has **zero access** to the host filesystem, network, or
  clock by default.

- The host explicitly passes capabilities (pre-opened directories,
  environment variables, virtualized clocks) into the instance upon
  creation.

- A compromised dependency cannot traverse directories or open
  unauthorized network connections outside granted capabilities.

┌────────────────────────────────────── WASI Capability-Based Security
──────────────────────────────────────┐

│ │

│ Host Runtime (Node.js / Wasmer / Wasmtime) │

│
┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│

│ │ Explicit Capability Grants: │ │

│ │ • preopens: { \'/sandbox\': \'./data/tenant_1\' } ──► Host
explicitly restricts FS to tenant directory │ │

│ │ • env: { API_KEY: \'xxx\' } ──► No ambient host process.env access │
│

│ │ │ │

│ │ ┌─── WebAssembly Instance (Isolated Linear Memory)
─────────────────────────────────────────────┐ │ │

│ │ │ │ │ │

│ │ │ Guest Code (Compiled from Rust / C / AssemblyScript) │ │ │

│ │ │ • Sandboxed 64KB Linear Memory Pages (Hardware Bounds Checking) │
│ │

│ │ │ • System calls intercepted by WASI Imports: │ │ │

│ │ │ wasi_snapshot_preview1.fd_read() ──► Resolves strictly inside
\'/sandbox\' │ │ │

│ │ │ wasi_snapshot_preview1.fd_write() │ │ │

│ │ │ │ │ │

│ │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
│ │

│
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘
│

│ │

└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Node.js WASI Implementation with node:wasi

Node.js provides native WASI execution through the node:wasi built-in
module:

import { readFile } from \'node:fs/promises\';

import { WASI } from \'node:wasi\';

import { argv, env } from \'node:process\';

async function runWasmPlugin(wasmPath: string) {

// 1. Configure WASI instance with capability-based sandboxing

const wasi = new WASI({

version: \'preview1\',

args: argv,

env: { APP_ENV: \'sandbox\' },

// Restrict filesystem: Map virtual guest path \'/workspace\' to host
local folder

preopens: {

\'/workspace\': \'./isolated_storage\',

},

});

// 2. Load compiled WebAssembly bytecode

const wasmBuffer = await readFile(wasmPath);

const wasmModule = await WebAssembly.compile(wasmBuffer);

// 3. Inject WASI system call import table into the WebAssembly instance

const instance = await WebAssembly.instantiate(wasmModule, {

wasi_snapshot_preview1: wasi.wasiImport,

});

// 4. Start execution (invokes guest \`\_start\` / \`main\` entrypoint)

wasi.start(instance);

}

### 3. The WebAssembly Component Model & WIT (Wasm Interface Types)

The major historical limitation of WebAssembly was primitive data
marshalling: guest and host could only exchange raw integers and floats
(i32, i64, f32, f64). Passing strings or complex structs required manual
pointer offset math and memory allocation in linear memory.

The **Wasm Component Model** and **WIT (Wasm Interface Type)** eliminate
this hurdle:

- **WIT**: A declarative Interface Definition Language defining rich
  types (strings, records, variants, lists, resources).

- **Canonical ABI**: Automatically serializes and lifts complex data
  across guest and host memory boundaries with zero manual glue code.

// plugin.wit - Interface Definition

package enterprise:plugins@1.0.0;

interface data-transformer {

record user-record {

id: string,

email: string,

tier: string,

}

// Pure typed interface without raw memory pointers!

transform: func(input: user-record) -\> result\<user-record, string\>;

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

### WASI Configuration Options Reference (node:wasi):

  ------------------------------------------------------------------------
  **Option**        **Type**          **Default**       **Description**
  ----------------- ----------------- ----------------- ------------------
  version           \'preview1\'      Required          WASI specification
                                                        version

  args              string\[\]        \[\]              Command-line
                                                        arguments exposed
                                                        to guest

  env               Record\<string,   {}                Sandboxed
                    string\>                            environment
                                                        variables exposed
                                                        to guest

  preopens          Record\<string,   {}                Virtual guest path
                    string\>                            \$\\rightarrow\$
                                                        Real host path map

  stdin / stdout /  number            0, 1, 2           File descriptors
  stderr                                                for redirected
                                                        stream I/O
  ------------------------------------------------------------------------

### WebAssembly Memory Management APIs:

// Allocate memory: 1 page = 65,536 bytes (64 KB)

const memory = new WebAssembly.Memory({ initial: 2, maximum: 10 }); //
128 KB to 640 KB

// Grow memory dynamically (fails if exceeds maximum)

memory.grow(1); // Allocates +64 KB

// Direct byte access via typed views

const rawBytes = new Uint8Array(memory.buffer);

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Sandboxed Path Traversal Prevention

Analyze the following WASI capability setup:

const wasi = new WASI({

version: \'preview1\',

preopens: {

\'/data\': \'./tenant_files\',

},

});

*Question*: If the guest WebAssembly module attempts to open
../../etc/passwd or /etc/shadow, what exact WASI error code is returned
(\_\_WASI_ERRNO_NOTCAPABLE vs \_\_WASI_ERRNO_NOENT)? Explain how the
WASI runtime performs path canonicalization before translating virtual
paths to host file descriptors.

### Challenge 2: Host Callback Injection into a WASI Module

A guest WebAssembly module needs to report real-time progress
percentages to the host JavaScript application while computing a heavy
data transformation:

1.  Provide an imported host function host_report_progress(percent:
    number): void in the import object.

2.  Ensure this custom import coexists with standard
    wasi_snapshot_preview1 system imports without link-time collision.

3.  Call the guest exported function process_data() and verify progress
    updates stream back to the host console.

### Challenge 3: Enterprise Sandboxed Markdown Linter Engine in TypeScript

Build an Enterprise **WASI-Powered Plugin Sandbox Engine** in
TypeScript:

**Requirements**:

1.  **Capability Isolation**:

    - Accepts third-party untrusted linter plugins compiled to
      WebAssembly.

    - Restricts each plugin to an ephemeral sandbox directory (/sandbox)
      that is wiped after execution.

2.  **Resource & Memory Quotas**:

    - Restricts guest memory allocation to a maximum of 16 pages (1 MB
      maximum linear memory).

    - Enforces an execution timeout of 100ms using worker thread
      interrupts to guard against infinite loops.

3.  **Structured Result Parsing**:

    - Reads linting diagnostic reports written by the guest to
      /sandbox/report.json and parses them into strongly typed
      TypeScript diagnostic arrays with line and column coordinates.
