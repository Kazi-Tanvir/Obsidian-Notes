---
tags:
- javascript
- canvas
- webgl
- offscreen-canvas
- web-workers
- gpu-rendering
- graphics
- performance
date: 2026-09-01
---

# Day 32 - Canvas API, WebGL Fundamentals, OffscreenCanvas & GPU Rendering Pipeline

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Browser Graphics Architecture: CPU Rasterization vs. GPU Acceleration

Modern web browsers split rendering across the **Main Thread (CPU)** and the **Compositor/GPU Thread**:

- **DOM & SVG**: Retained-mode graphics. Every element is an object in memory; complex scenes with 10,000+ DOM nodes saturate the layout tree and garbage collector.

- **Canvas 2D**: Immediate-mode graphics. Commands draw directly into a 2D pixel bitmap buffer on the CPU/GPU without retaining DOM nodes.

- **WebGL / WebGPU**: Direct low-level access to the GPU graphics pipeline via OpenGL ES / hardware shading languages (GLSL/WGSL), executing parallel vertex and fragment transformations across thousands of GPU cores simultaneously.

┌────────────────────────────────────── Browser Graphics Pipeline ──────────────────────────────────────┐

│ │

│ 1. JavaScript Code (App Logic / Physics) ──► CPU Main Thread or Web Worker │

│ │

│ 2. Draw Commands / Shaders ──► Skia (2D) or WebGL / WebGPU Drivers │

│ │

│ 3. GPU Pipeline: Vertex Shader ──► Rasterization ──► Fragment (Pixel) Shader ──► Framebuffer Buffer │

│ │

│ 4. Display Screen (VSync Refresh: 60Hz = 16.6ms budget / 120Hz = 8.3ms budget) │

│ │

└───────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. High-DPI Display Scaling & Delta-Timed Animation Loops

A common mistake is rendering on high-DPI (Retina/4K) displays without scaling the canvas backing store, causing blurry rendering.

```javascript
// High-DPI Sharp Rendering Setup
function setupHighDPICanvas(canvas, cssWidth, cssHeight) {
const dpr = window.devicePixelRatio || 1;
const ctx = canvas.getContext('2d');
// Set physical pixel resolution
canvas.width = cssWidth * dpr;
canvas.height = cssHeight * dpr;
// Maintain CSS layout dimensions
canvas.style.width = `${cssWidth}px`;
canvas.style.height = `${cssHeight}px`;
// Scale coordinate system so 1 unit = 1 CSS pixel
ctx.scale(dpr, dpr);
return ctx;
}
// Delta-Time Independent Render Loop
let lastTime = performance.now();
function renderLoop(currentTime) {
// Calculate delta time in seconds (e.g. 0.016s at 60fps)
const deltaTime = (currentTime - lastTime) / 1000;
lastTime = currentTime;
// Update physics with frame-rate independence: position += velocity * deltaTime
updatePhysics(deltaTime);
drawScene();
requestAnimationFrame(renderLoop);
}
requestAnimationFrame(renderLoop);
```

### 3. OffscreenCanvas & Multi-Threaded Worker Rendering

OffscreenCanvas completely decouples rendering from the DOM. By transferring control of a canvas to a **Web Worker**, the rendering loop runs at a steady 60--120 FPS without stuttering even when the main thread executes heavy JavaScript or DOM reflows.

```javascript
// main.js (Main UI Thread)
const canvas = document.getElementById('renderCanvas');
// Transfer canvas ownership to the worker (Canvas cannot be drawn on main thread anymore)
const offscreen = canvas.transferControlToOffscreen();
const worker = new Worker(new URL('./graphics.worker.js', import.meta.url), { type: 'module' });
// Pass offscreen canvas as a Transferable Object (zero-copy memory transfer)
worker.postMessage({ type: 'INIT', canvas: offscreen }, [offscreen]);
// Listen for user interactions and forward to worker
window.addEventListener('mousemove', (e) => {
worker.postMessage({ type: 'MOUSE_MOVE', x: e.clientX, y: e.clientY });
});
// graphics.worker.js (Dedicated Web Worker Thread)
let ctx;
let particles = [];
```

self.onmessage = (event) => {

```javascript
const { type, canvas, x, y } = event.data;
if (type === 'INIT') {
ctx = canvas.getContext('2d');
initParticles(10000);
requestAnimationFrame(workerLoop);
} else if (type === 'MOUSE_MOVE') {
updateMousePosition(x, y);
}
};
function workerLoop(time) {
ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
// Render 10,000 particles at 60fps on separate thread!
for (let i = 0; i < particles.length; i++) {
const p = particles[i];
p.x += p.vx;
p.y += p.vy;
ctx.fillStyle = p.color;
ctx.fillRect(p.x, p.y, p.size, p.size);
}
requestAnimationFrame(workerLoop);
}
```

### 4. WebGL2 Fundamentals & GLSL Shaders

WebGL allows executing raw C-like **GLSL (OpenGL Shading Language)** programs on the GPU:

- **Vertex Shader**: Runs once per vertex; computes 3D-to-2D clip-space coordinates (gl_Position).

- **Fragment Shader**: Runs once per pixel/fragment; calculates final RGBA pixel colors (outColor).

```javascript
// Minimal WebGL2 Shader Compilation Boilerplate
function createWebGLProgram(gl, vertexSource, fragmentSource) {
function compileShader(gl, type, source) {
const shader = gl.createShader(type);
gl.shaderSource(shader, source);
gl.compileShader(shader);
if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
throw new Error(`Shader compile error: ${gl.getShaderInfoLog(shader)}`);
}
return shader;
}
const vertexShader = compileShader(gl, gl.VERTEX_SHADER, vertexSource);
const fragmentShader = compileShader(gl, gl.FRAGMENT_SHADER, fragmentSource);
const program = gl.createProgram();
gl.attachShader(program, vertexShader);
gl.attachShader(program, fragmentShader);
gl.linkProgram(program);
if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
throw new Error(`Program link error: ${gl.getProgramInfoLog(program)}`);
}
return program;
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Canvas 2D vs. WebGL / WebGPU Comparison:

| **Feature** | **Canvas 2D** | **WebGL2** | **WebGPU** |
| --- | --- | --- | --- |
| **API Paradigm** | Immediate high-level drawing | OpenGL ES 3.0 state machine | Modern low-overhead explicit pipeline |
| **Shaders** | None (Fixed CPU/GPU raster) | GLSL ES 3.00 (Vertex/Fragment) | WGSL (Vertex/Fragment/Compute) |
| **3D & Custom Shading** | Impossible / Limited | Yes | Yes (Direct GPU Compute support) |
| **Best Used For** | 2D Charts, Simple UI, Diagrams | 3D Scenes, 2D Games, Shaders | Compute tasks, High-End 3D, ML in browser |

### Canvas State Stack APIs:

```javascript
ctx.save(); // Pushes current transformations, clip paths, and styles to internal stack
ctx.translate(x, y);
ctx.rotate(angle);
ctx.fillStyle = 'red';
ctx.fillRect(-25, -25, 50, 50);
ctx.restore(); // Restores previous transformation matrix and styles cleanly
```

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Retina Canvas Blurriness & Coordinate Alignment

Analyze the snippet below:

```javascript
const canvas = document.createElement('canvas');
canvas.style.width = '400px';
canvas.style.height = '300px';
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';
ctx.fillRect(50, 50, 100, 100);
```

*Question*: On a device with window.devicePixelRatio = 2 (e.g. MacBook Retina / 4K display), why is the blue box blurry? What are the exact default values of canvas.width and canvas.height if not explicitly specified?

*Hint*: Understand the difference between CSS layout pixel dimensions and backing store bitmap pixel buffer dimensions.

### Challenge 2: Memory-Bounded Canvas Particle Engine with Zero GC Churn

Refactor an un-optimized particle engine that creates 5,000 new object instances (new Particle()) per second into an allocation-free engine using **TypedArrays** (Float32Array) and an **Object Pool** pattern to prevent Garbage Collection frame drops.

### Challenge 3: Real-Time WebGL Color-Grading Filter Engine in TypeScript

Build an End-to-End **WebGL2 Post-Processing Image & Video Shader Filter Engine** in TypeScript:

**Requirements**:

1.  **Shader Pipeline (WebGLFilterEngine)**:

    - Compiles a Fullscreen Quad Vertex Shader and a dynamic Fragment Shader in GLSL ES 3.00.

    - Accepts real-time Uniform parameters: u_brightness (float), u_contrast (float), u_saturation (float), u_tint (vec3).

2.  **Texture Management**:

    - Uploads an HTMLImageElement, HTMLVideoElement, or ImageBitmap to a WebGL 2D Texture (gl.texImage2D).

    - Renders the post-processed result at 60 FPS.

3.  **OffscreenCanvas Web Worker Mode**:

    - Includes support for running inside an OffscreenCanvas worker receiving live video frames from a MediaStreamTrackProcessor.
