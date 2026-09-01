tags:

- javascript

- service-workers

- pwa

- offline-first

- cache-api

- background-sync

- push-api date: 2026-08-29

# Day 29 - Service Workers, PWA Caching Strategies & Offline-First Architecture

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Service Worker Architecture & Lifecycle

A **Service Worker** is a client-side programmable network proxy running in a background worker thread separate from the DOM. It intercepts network requests, manages client-side caching, and enables offline capabilities, background synchronization, and push notifications.

┌─────────────────┐ HTTP Request ┌──────────────────────┐ Network Fetch ┌─────────────────┐

│ Browser / DOM │ ─────────────────────────► │ Service Worker Proxy │ ─────────────────────────► │ Origin Server │

│ Client Context │ ◄───────────────────────── │ (Fetch Event Handler)│ ◄───────────────────────── │ (Remote API/CDN)│

└─────────────────┘ HTTP Response └──────────┬───────────┘ HTTP Response └─────────────────┘

│

Read / Write Cache

│

▼

┌──────────────────────┐

│ Cache Storage API │

│ IndexedDB │

└──────────────────────┘

#### Service Worker Lifecycle States:

1.  **Registration**: The browser registers the worker script path via navigator.serviceWorker.register(\'/sw.js\', { scope: \'/\' }).

2.  **Installation (install event)**: Pre-caches critical static shell assets using event.waitUntil(). self.skipWaiting() forces an updated worker to skip the waiting state and activate immediately.

3.  **Activation (activate event)**: Cleans up obsolete caches from previous versions. self.clients.claim() enables the new worker to take control of all open pages immediately without requiring a page reload.

4.  **Idle / Functional Events (fetch, sync, push)**: Wakes up on demand to process network fetches, background syncs, or push events, then terminates when idle to save device resources.

// sw.js - Production Lifecycle Setup

const CACHE_NAME = \'app-shell-v2\';

const STATIC_ASSETS = \[\'/\', \'/index.html\', \'/styles.css\', \'/app.js\', \'/favicon.ico\'\];

// 1. Install Event: Cache Core App Shell

self.addEventListener(\'install\', (event) =\> {

event.waitUntil(

caches.open(CACHE_NAME).then((cache) =\> cache.addAll(STATIC_ASSETS))

);

self.skipWaiting(); // Bypass waiting state

});

// 2. Activate Event: Purge Outdated Caches

self.addEventListener(\'activate\', (event) =\> {

event.waitUntil(

caches.keys().then((cacheNames) =\>

Promise.all(

cacheNames

.filter((name) =\> name !== CACHE_NAME)

.map((name) =\> caches.delete(name))

)

)

);

self.clients.claim(); // Take control of open tabs

});

### 2. The 5 Core PWA Caching Strategies

#### A. Cache-First (Cache Falling Back to Network)

Best for static immutable assets (versioned CSS/JS bundles, images, fonts).

async function cacheFirst(request) {

const cachedResponse = await caches.match(request);

if (cachedResponse) return cachedResponse;

try {

const networkResponse = await fetch(request);

if (networkResponse.ok) {

const cache = await caches.open(CACHE_NAME);

cache.put(request, networkResponse.clone());

}

return networkResponse;

} catch (error) {

return new Response(\'Network error occurred\', { status: 408 });

}

}

#### B. Network-First (Network Falling Back to Cache)

Best for real-time frequently changing data where freshness is paramount (user profile, stock prices), falling back to cached state if offline.

async function networkFirst(request) {

try {

const networkResponse = await fetch(request);

if (networkResponse.ok) {

const cache = await caches.open(CACHE_NAME);

cache.put(request, networkResponse.clone());

}

return networkResponse;

} catch (error) {

const cachedResponse = await caches.match(request);

if (cachedResponse) return cachedResponse;

return new Response(JSON.stringify({ error: \'Offline and un-cached\' }), {

headers: { \'Content-Type\': \'application/json\' },

status: 503,

});

}

}

#### C. Stale-While-Revalidate (SWR)

Returns cached response immediately for instantaneous rendering, while asynchronously fetching a fresh copy from the network and updating the cache in the background. Best for social feeds, product catalogs, and dashboard summaries.

async function staleWhileRevalidate(request) {

const cache = await caches.open(CACHE_NAME);

const cachedResponse = await cache.match(request);

const fetchPromise = fetch(request).then((networkResponse) =\> {

if (networkResponse.ok) {

cache.put(request, networkResponse.clone());

}

return networkResponse;

}).catch(() =\> null);

return cachedResponse \|\| (await fetchPromise);

}

### 3. Background Sync & Offline Mutation Replays

The **Background Sync API** allows web applications to defer server-state mutations (e.g. submitting a form, posting a comment) until the user has a stable network connection.

// Main Thread: Registering Background Sync

async function submitCommentOffline(commentData) {

await saveToIndexedDB(\'offline_comments\', commentData);

const registration = await navigator.serviceWorker.ready;

if (\'sync\' in registration) {

await registration.sync.register(\'sync-comments\');

} else {

// Fallback if background sync is unsupported

await syncCommentsImmediately();

}

}

// Service Worker: Processing Sync Event

self.addEventListener(\'sync\', (event) =\> {

if (event.tag === \'sync-comments\') {

event.waitUntil(replayOfflineComments());

}

});

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Caching Strategy Decision Matrix:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Strategy**                 **Network Latency**               **Data Freshness**           **Offline Support**   **Recommended Resource Type**
  ---------------------------- --------------------------------- ---------------------------- --------------------- ---------------------------------------------------
  **Cache-First**              Ultra-Fast (\$\<10\\text{ms}\$)   Stale (until version bump)   Complete              Fingerprinted JS/CSS, Web Fonts, Static Icons

  **Network-First**            High (Network-bound)              Immediate                    Fallback Only         Account Balances, Real-Time Telemetry

  **Stale-While-Revalidate**   Ultra-Fast (\$\<10\\text{ms}\$)   Eventually Consistent        Complete              Articles, Dashboard Cards, Social Feeds

  **Network-Only**             High (Network-bound)              Immediate                    None                  Payment Transactions, Live Authentication

  **Cache-Only**               Ultra-Fast (\$\<5\\text{ms}\$)    Static                       Complete              Pre-cached Offline Fallback Pages (/offline.html)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Service Worker Scope & Activation Lifecycle Prediction

Analyze the registration and scope setup below. Predict whether the Service Worker will intercept the fetch requests made by the page:

// In /admin/dashboard/index.html:

navigator.serviceWorker.register(\'/admin/sw.js\', { scope: \'/admin/\' });

// In Page Script:

fetch(\'/admin/api/metrics\'); // Request A

fetch(\'/api/v1/users\'); // Request B

fetch(\'/assets/style.css\'); // Request C

*Question*: Which requests (A, B, C) are intercepted by /admin/sw.js and why? What header must the server send to allow /admin/sw.js to control the root scope /?

*Hint*: Research the Service-Worker-Allowed HTTP response header and scope directory restrictions.

### Challenge 2: Memory-Bounded LRU Cache Storage Wrapper

The standard CacheStorage API has no built-in max-item or time-to-live (TTL) limits, leading to potential storage quota exhaustion (QuotaExceededError).

Refactor the following un-bounded cache handler into a **Max-Item LRU Cache Storage Wrapper**:

1.  Enforces a maximum limit of 50 cached entries per cache bucket.

2.  Evicts the oldest accessed entry when inserting item 51.

// Unbounded Vulnerable Cache Routine

async function cacheResourceUnbounded(cacheName, request, response) {

const cache = await caches.open(cacheName);

await cache.put(request, response); // Can grow indefinitely!

}

*Hint*: Use cache.keys() to inspect existing requests and delete the oldest key (cache.delete(keys\[0\])).

### Challenge 3: End-to-End Offline-First Background Sync Queue

Build a production-grade **Offline-First Mutation Synchronizer** in TypeScript:

**Requirements**:

1.  **Client Interceptor (offlineApiClient)**: Intercepts POST, PUT, DELETE requests. If navigator.onLine === false or fetch fails with a network exception:

    - Serializes the request (URL, Method, Headers, JSON Body, UUID, timestamp).

    - Stores it into an IndexedDB store (pending_mutations).

    - Registers a background sync tag \'sync-mutations\' on ServiceWorkerRegistration.

2.  **Service Worker Sync Handler (sw.ts)**:

    - Listens to self.addEventListener(\'sync\', \...) matching \'sync-mutations\'.

    - Iterates through pending mutations in chronological order.

    - Replays requests with custom X-Idempotency-Key and X-Offline-Replay: true headers.

    - Deletes successfully processed records from IndexedDB and notifies open window clients via postMessage().

    - Implements exponential backoff retry and Dead-Letter Queue (DLQ) if the server returns 4xx/5xx responses.
