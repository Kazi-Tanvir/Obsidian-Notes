tags:

- javascript

- animations

- requestanimationframe

- web-animations-api

- waapi

- performance

- rendering-pipeline

- compositing date: 2026-09-09

# Day 40 - High-Performance Animation, requestAnimationFrame, Web Animations API & Layout Stability

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Browser Rendering Pipeline & Composited Layers

To engineer 60 FPS (and 120 FPS on ProMotion displays) animations
without frame drops (jank), developers must understand how the browser
processes visual updates:

1.  **JavaScript**: Script execution calculates layout properties or
    triggers style changes.

2.  **Style (Recalculate Styles)**: The engine matches CSS rules against
    DOM selectors to compute final element styling.

3.  **Layout (Reflow)**: Calculates geometric dimensions and screen
    coordinates for every visible element. (CPU intensive!)

4.  **Paint**: Fills pixel colors, text, borders, and shadows into
    rasterization drawing instructions across distinct layers. (CPU
    intensive!)

5.  **Composite**: Dispatches bitmap layers to the GPU to be positioned,
    scaled, and blended onto the physical display screen.

┌────────────────────────────────────── The Rendering Cost Spectrum
──────────────────────────────────────┐

│ │

│ Triggering Reflow (Avoid in loops! ⚠️) │

│ \[ JS / CSS \] ──► \[ Style \] ──► \[ Layout (Reflow) \] ──► \[ Paint
\] ──► \[ Composite \] │

│ Mutating \`width\`, \`height\`, \`margin\`, \`top\`, \`left\`,
\`fontSize\` recomputes the entire render tree! │

│ │

│ Triggering Repaint (Medium Cost ⚠️) │

│ \[ JS / CSS \] ──► \[ Style \] ──► \[ Paint \] ──► \[ Composite \] │

│ Mutating \`background-color\`, \`color\`, \`box-shadow\`,
\`border-radius\` bypasses layout but rerasters! │

│ │

│ GPU Compositor-Only (Ultra-Fast 60/120 FPS! 🚀) │

│ \[ JS / CSS \] ──► \[ Style \] ──► \[ Composite (GPU) \] │

│ Mutating \`transform\` and \`opacity\` runs strictly on the GPU
compositor thread without touching CPU! │

│ │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

#### Promoting Elements with will-change:

Informing the browser ahead of time allows it to promote an element to
its own GPU compositor layer:

.animated-card {

will-change: transform, opacity;

}

*Architecture Rule*: Never apply will-change globally to many elements,
as each compositor layer consumes dedicated VRAM. Remove it once
animation concludes.

### 2. requestAnimationFrame (rAF) vs. Timer Inaccuracies

Using setTimeout or setInterval for animations is inherently flawed:

- Timers run on the macro-task queue without synchronization to hardware
  display refresh cycles (vsync).

- If a timer fires mid-frame, frame tearing and dropped frames occur.

- requestAnimationFrame(callback) synchronizes execution immediately
  before the browser\'s next vertical refresh pulse, automatically
  pausing when the user switches tabs to conserve device battery.

let startTimestamp: number \| null = null;

const durationMs = 1000;

const element = document.getElementById(\'ball\')!;

function animate(timestamp: number) {

if (!startTimestamp) startTimestamp = timestamp;

const elapsed = timestamp - startTimestamp;

const progress = Math.min(elapsed / durationMs, 1);

// Smooth easing function: easeOutCubic

const easeProgress = 1 - Math.pow(1 - progress, 3);

const translateX = easeProgress \* 400;

// GPU composited transform

element.style.transform = \`translate3d(\${translateX}px, 0, 0)\`;

if (progress \< 1) {

requestAnimationFrame(animate);

}

}

requestAnimationFrame(animate);

### 3. The Web Animations API (WAAPI): Native Off-Main-Thread Power

The **Web Animations API (WAAPI)** bridges CSS animations with
imperative JavaScript control. Unlike requestAnimationFrame (which
executes on the main thread), WAAPI animations can run **completely off
the main thread on the GPU compositor thread**, ensuring fluid 60 FPS
movement even if heavy JavaScript blocks the main thread.

const heroElement = document.querySelector(\'.hero-banner\')!;

// Native WAAPI Execution

const animation = heroElement.animate(

\[

{ transform: \'translateY(50px) scale(0.95)\', opacity: 0 },

{ transform: \'translateY(0px) scale(1)\', opacity: 1 }

\],

{

duration: 600,

easing: \'cubic-bezier(0.16, 1, 0.3, 1)\',

fill: \'forwards\'

}

);

// Programmatic Playback Control:

animation.pause();

animation.currentTime = 300; // Seek to 50%

animation.reverse();

await animation.finished;

## SECTION 2: DOCUMENTATION CHEAT SHEET

### CSS Properties & Rendering Trigger Matrix:

  -------------------------------------------------------------------------------
  **CSS Property**   **Triggers     **Triggers     **Compositor   **Performance
                     Layout?**      Paint?**       Thread Only?** Rating**
  ------------------ -------------- -------------- -------------- ---------------
  transform          ❌ No          ❌ No          ✅ **Yes       🟢 **Ultra
  (translate, scale,                               (GPU)**        Fast**
  rotate)                                                         

  opacity            ❌ No          ❌ No          ✅ **Yes       🟢 **Ultra
                                                   (GPU)**        Fast**

  filter (blur,      ❌ No          ❌ No          ✅ **Yes       🟡 Moderate
  brightness)                                      (GPU)**        (GPU VRAM)

  background-color / ❌ No          ✅ **Yes**     ❌ No          🟠 Repaint Cost
  color                                                           

  top / left / right ✅ **Yes**     ✅ **Yes**     ❌ No          🔴 **Jank
  / bottom                                                        Warning**

  width / height /   ✅ **Yes**     ✅ **Yes**     ❌ No          🔴 **Jank
  margin / padding                                                Warning**
  -------------------------------------------------------------------------------

### WAAPI Keyframe Animation Timing Options:

interface KeyframeAnimationOptions {

duration?: number; // In milliseconds

delay?: number; // Start delay in ms

easing?: \'linear\' \| \'ease\' \| \'ease-in-out\' \| string; // e.g.
\'cubic-bezier(\...)\'

iterations?: number; // e.g. Infinity

direction?: \'normal\' \| \'reverse\' \| \'alternate\';

fill?: \'none\' \| \'forwards\' \| \'backwards\' \| \'both\';

composite?: \'replace\' \| \'add\' \| \'accumulate\';

}

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Diagnosing Layout Thrashing in an Animation Loop

Analyze the following loop attempting to animate 500 DOM cards:

function updateCards() {

const cards = document.querySelectorAll(\'.card\');

for (let i = 0; i \< cards.length; i++) {

const currentTop = cards\[i\].offsetTop; // Reading geometry

cards\[i\].style.top = (currentTop + 2) + \'px\'; // Mutating geometry

}

requestAnimationFrame(updateCards);

}

*Question*: Explain why this code causes severe **Forced Synchronous
Layout (Layout Thrashing)**. How many reflow calculations are triggered
per frame? Refactor the loop to batch reads and writes using composited
transform styling.

### Challenge 2: Interruptible Spring Gesture Controller using WAAPI

Build an **Interruptible Gesture Animation Controller** in TypeScript:

1.  Listens to drag gestures on an element using Pointer Events
    (pointerdown, pointermove, pointerup).

2.  When dragged and released, calculates velocity and launches a
    decelerating spring-back animation using WAAPI.

3.  If the user touches the element mid-flight while the spring
    animation is running, it must seamlessly **freeze/pause** the
    animation at animation.currentTime, capture the current matrix
    coordinates, and transition back into direct touch tracking without
    visual snapping.

### Challenge 3: 60-FPS Virtualized Parallax Physics Engine

Build an Enterprise **Virtualized Parallax Physics Engine** in
TypeScript:

**Requirements**:

1.  **Delta-Timing Physics**:

    - Computes movement using delta timestamps (timestamp -
      lastTimestamp) ensuring identical physics behavior on 60 Hz, 120
      Hz, and 144 Hz displays.

2.  **Multi-Layer GPU Parallax**:

    - Manages 5 independent visual depth planes with custom speed
      multipliers (\$0.2\\times, 0.5\\times, 1.0\\times, 1.8\\times,
      2.5\\times\$).

    - Applies updates exclusively using translate3d() on pre-promoted
      compositor layers.

3.  **Automated Layer Allocation & Performance Monitoring**:

    - Automatically attaches will-change: transform upon scroll
      initiation and cleans it up after 200ms of inactivity to conserve
      GPU memory.

    - Monitors internal frame execution time; if a frame exceeds 16.6ms,
      it logs telemetry and gracefully lowers parallax sample precision.
