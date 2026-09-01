tags:

- javascript

- web-apis

- intersection-observer

- resize-observer

- performance

- core-web-vitals date: 2026-08-10

# Day 10 - Web APIs, IntersectionObserver, ResizeObserver & Performance Metrics (Core Web Vitals)

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Death of Scroll Listeners & The Rise of Observer APIs

Traditional DOM scroll/resize event listeners execute on the main thread during every frame, frequently causing frame drops, jank, and forced synchronous layouts.

Modern **Observer APIs** offload target geometry and viewport calculations to the browser\'s compositor thread asynchronously, notifying JavaScript only when thresholds are crossed.

### 2. IntersectionObserver: Viewport & Element Visibility

IntersectionObserver tracks when a target element enters or exits an ancestor element (or top-level viewport).

// Production Infinite Scroll / Lazy Load Observer

const observerOptions = {

root: null, // Viewport

rootMargin: \'200px 0px\', // Pre-fetch 200px before scrolling into view

threshold: 0.1 // Triggers when 10% visible

};

const imageObserver = new IntersectionObserver((entries, observer) =\> {

entries.forEach(entry =\> {

if (entry.isIntersecting) {

const img = entry.target;

img.src = img.dataset.src; // Lazy load image

img.classList.remove(\'blur-placeholder\');

observer.unobserve(img); // Clean up memory!

}

});

}, observerOptions);

document.querySelectorAll(\'img\[data-src\]\').forEach(img =\> imageObserver.observe(img));

### 3. ResizeObserver: Container Geometry Monitoring

Unlike window.onresize which only fires on global window changes, ResizeObserver detects dimension updates on specific DOM elements (e.g., sidebar collapses, dynamic content injection).

const chartContainer = document.querySelector(\'#responsive-chart\');

const resizeObserver = new ResizeObserver(entries =\> {

for (const entry of entries) {

// Access contentBoxSize or borderBoxSize

const { inlineSize: width, blockSize: height } = entry.contentBoxSize\[0\];

redrawChart(width, height);

}

});

resizeObserver.observe(chartContainer);

### 4. PerformanceObserver & Core Web Vitals

Core Web Vitals measure real-user experience metrics:

- **LCP (Largest Contentful Paint)**: Loading performance (Target: \<= 2.5s).

- **INP (Interaction to Next Paint)**: Responsiveness to user input (Target: \<= 200ms).

- **CLS (Cumulative Layout Shift)**: Visual stability (Target: \<= 0.1).

// PerformanceObserver for Largest Contentful Paint (LCP)

const lcpObserver = new PerformanceObserver((entryList) =\> {

const entries = entryList.getEntries();

const lastEntry = entries\[entries.length - 1\]; // Latest LCP candidate

console.log(\'LCP Score (ms):\', lastEntry.startTime, lastEntry);

});

lcpObserver.observe({ type: \'largest-contentful-paint\', buffered: true });

// PerformanceObserver for Cumulative Layout Shift (CLS)

let clsScore = 0;

const clsObserver = new PerformanceObserver((entryList) =\> {

for (const entry of entryList.getEntries()) {

if (!entry.hadRecentInput) { // Ignore shifts caused by direct user clicks

clsScore += entry.value;

console.log(\'Current CLS:\', clsScore);

}

}

});

clsObserver.observe({ type: \'layout-shift\', buffered: true });

## SECTION 2: DOCUMENTATION CHEAT SHEET

  ---------------------------------------------------------------------------------------------------------------------------------
  **Web API**                **Options / Entry Types**                **Purpose / Use Case**
  -------------------------- ---------------------------------------- -------------------------------------------------------------
  **IntersectionObserver**   root, rootMargin, threshold              Infinite scroll, image lazy loading, ad impression tracking

  **ResizeObserver**         box: \'content-box\' \| \'border-box\'   Responsive component layout, canvas/chart auto-resizing

  **PerformanceObserver**    type: \'largest-contentful-paint\'       Measures page load speed candidate

  **PerformanceObserver**    type: \'layout-shift\'                   Tracks unexpected layout shifts (CLS)

  **PerformanceObserver**    type: \'event\'                          Tracks user input latency (INP)
  ---------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Intersection Observer Threshold Prediction

Analyze the following code snippet and predict when callback will be triggered as an element scrolls into view. Explain the difference between threshold: 0 and threshold: 1.

const observer = new IntersectionObserver(callback, {

rootMargin: \'-50px 0px\',

threshold: \[0, 0.5, 1.0\]

});

observer.observe(document.querySelector(\'.hero-banner\'));

*Hint*: Pay attention to how negative rootMargin shrinks the effective bounding box.

### Challenge 2: Refactoring Scroll-based Infinite Scroll

Refactor the following main-thread blocking scroll event listener into a memory-safe IntersectionObserver infinite scroll sentinel component.

// Anti-pattern: High CPU overhead on every scroll event

window.addEventListener(\'scroll\', () =\> {

if (window.innerHeight + window.scrollY \>= document.body.offsetHeight - 500) {

fetchNextPage();

}

});

*Hint*: Append a \<div id=\"scroll-sentinel\"\> at the bottom of the list and observe it.

### Challenge 3: Building a Real-User Web Vitals Analytics Tracker

Write a custom JS module initWebVitalsTracker(endpointUrl) that:

1.  Uses PerformanceObserver to track LCP, CLS, and INP.

2.  Buffers metrics locally and sends them to endpointUrl using navigator.sendBeacon() when the page unloads/visibility changes to hidden.

3.  Ensures zero impact on main thread responsiveness and handles unobserve cleanup gracefully.

*Hint*: Combine buffered: true on PerformanceObserver with document.addEventListener(\'visibilitychange\').
