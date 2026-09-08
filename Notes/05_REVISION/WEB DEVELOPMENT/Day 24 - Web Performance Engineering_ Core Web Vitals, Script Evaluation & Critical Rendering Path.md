---
tags:
  - frontend
  - performance
  - core-web-vitals
  - browser
  - critical-rendering-path
  - optimization
  - architecture
date: 2026-08-24
---

# Day 24 - Web Performance Engineering: Core Web Vitals, Script Evaluation & Critical Rendering Path

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Critical Rendering Path (CRP) Deep Dive

The Critical Rendering Path is the sequence of steps the browser takes to convert HTML, CSS, and JavaScript into actual visual pixels on the screen.

HTML Bytes ──► Tokenizer ──► DOM Tree ────────┐

```typescript
                                               ├──► Render Tree ──► Layout / Reflow ──► Paint ──► Composite
```

CSS Bytes  ──► Tokenizer ──► CSSOM Tree ──────┘

#### Step-by-Step Breakdown:

- **DOM Construction**: Incremental and streaming. HTML parser constructs the DOM tree token by token.

- **CSSOM Construction**: **Render-blocking**. The browser cannot render anything until the entire CSSOM is constructed, because CSS cascades and rules override earlier definitions.

- **Render Tree**: Intersects DOM and CSSOM, ignoring hidden nodes (`display: none`, `<head>`, `<script>`).

- **Layout (Reflow)**: Computes exact geometry, coordinates, and bounding box sizes for all visible nodes.

- **Paint**: Fills pixels with text, colors, shadows, and borders into separate raster layers.

- **Compositing**: GPU combines separate layers to avoid re-painting the entire viewport during animations (`transform`, `opacity`).

### 2. Script Loading & Evaluation Mechanics

<!-- Parser Blocking: Halts DOM parsing while downloading & executing -->

<script src="bundle.js"></script>

<!-- Async: Downloads in parallel; executes IMMEDIATELY when downloaded (Interrupts DOM parser) -->

<script async src="analytics.js"></script>

<!-- Defer: Downloads in parallel; executes only AFTER DOM parsing completes (Guarantees order) -->

<script defer src="app.js"></script>

<!-- ES Module: Deferred by default; supports top-level await and tree-shaking -->

<script type="module" src="main.js"></script>

#### Resource Hints Hierarchy:

- `<link rel="preload" as="image" href="..." fetchpriority="high">`: High-priority resource required for the current navigation (e.g., LCP Hero image).

- `<link rel="preconnect" href="https://api.example.com">`: Pre-warms DNS resolution, TCP handshake, and TLS negotiation.

- `<link rel="prefetch" href="...">`: Low-priority fetch for resources likely needed on the *next* page transition.

### 3. Core Web Vitals (2026 Standards)

#### A. Largest Contentful Paint (LCP) — Target: $\le 2.5\text{s}$

Measures perceived loading speed by recording when the largest visual block (hero image, video poster, or large text heading) renders.

**The 4 Sub-parts of LCP**:

- **Time to First Byte (TTFB)**: Server response time.

- **Resource Load Delay**: Time between TTFB and when the browser starts fetching the LCP asset (minimize via `<link rel="preload">` and `fetchpriority="high"`).

- **Resource Load Duration**: Download duration of the asset (minimize via WebP/AVIF compression and CDN edge caching).

- **Element Render Delay**: Time between asset download and DOM paint (minimize by eliminating render-blocking CSS/JS).

#### B. Interaction to Next Paint (INP) — Target: $\le 200\text{ms}$

Measures overall page responsiveness across all user clicks, taps, and keypresses throughout the entire session.

**Mitigating Long Tasks (>50ms)**: Break large JavaScript execution blocks using cooperative scheduling (`scheduler.yield()` or `requestAnimationFrame`):

```typescript
async function processLargeDataSet(items: string[]) {
  for (let i = 0; i < items.length; i++) {
    heavyComputation(items[i]);
    // Yield main thread every 50 items so user input can process immediately
    if (i % 50 === 0 && 'scheduler' in window && 'yield' in window.scheduler) {
      await window.scheduler.yield();
    }
  }
}
```

#### C. Cumulative Layout Shift (CLS) — Target: $\le 0.1$

Measures visual stability by calculating unexpected layout position shifts of visible elements.

**Prevention Rules**:

- Always specify `width` and `height` (or CSS `aspect-ratio: 16/9`) on `<img>`, `<video>`, and `<iframe>`.

- Reserve space for dynamic ad banners and modals using CSS `min-height` or `contain-intrinsic-size`.

- Use `font-display: swap` paired with CSS size-adjust overrides to eliminate layout shifts when web fonts load.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Core Web Vitals Benchmarks:

| **Metric** | **Full Name** | **Good Threshold** | **Needs Improvement** | **Poor** | **Primary Root Cause** |
| --- | --- | --- | --- | --- | --- |
| **LCP** | Largest Contentful Paint | $\le 2.5\text{s}$ | $2.5\text{s} - 4.0\text{s}$ | $> 4.0\text{s}$ | Slow server TTFB, uncompressed hero images, render-blocking CSS |
| **INP** | Interaction to Next Paint | $\le 200\text{ms}$ | $200\text{ms} - 500\text{ms}$ | $> 500\text{ms}$ | Long JS execution tasks (>50ms) blocking main thread on click |
| **CLS** | Cumulative Layout Shift | $\le 0.1$ | $0.1 - 0.25$ | $> 0.25$ | Unsized images, dynamic client-side DOM insertions, web font layout shifts |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: High-Performance E-Commerce Product Listing Page Architecture

Design an enterprise-scale E-Commerce Product Listing Page (PLP) architecture serving 50,000 products with strict Core Web Vitals guarantees:

- Target: Mobile **LCP $\le 1.2\text{s}$**, **INP $\le 80\text{ms}$**, **CLS $= 0.0$**.

**Requirements**:

- Detail the critical resource hints, image optimization (responsive `srcset`, AVIF formats, `fetchpriority="high"`), and font loading strategies.

- Formulate a CSS delivery architecture separating Critical Inlined CSS from Asynchronous Non-Critical CSS.

- Design the client-side JavaScript hydration strategy (Selective Hydration with React Server Components / Islands architecture) ensuring the main thread is never blocked during search/filter operations.

### Problem 2: End-to-End Code Implementation Challenge

Build a standalone **Cooperative Main-Thread Task Scheduler** in TypeScript:

**Requirements**:

- Implement `runTaskQueue<T>(items: T[], processFn: (item: T) => void, options: { maxBudgetMs?: number }): Promise<void>`.

- Continuously measure elapsed task execution time using high-resolution performance timers (`performance.now()`).

- If processing exceeds the time budget (default $16\text{ms}$), yield the main thread using modern `scheduler.yield()` (with fallback to `MessageChannel` / `setTimeout(0)`) so pending user clicks and scroll inputs process with zero INP latency.

- Provide unit tests verifying:

- Synchronous processing within budget.

- Main-thread yielding when task durations exceed the frame budget.
