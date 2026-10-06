---
tags:
  - javascript
  - security
  - trusted-types
  - csp
  - cross-origin-isolation
  - coop-coep
  - xss-prevention
  - browser-internals
date: 2026-09-24
---

# Day 55 - Browser Security Hardening: Content Security Policy (CSP Level 3), Trusted Types, Cross-Origin Isolation & Spectre Defenses

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Death of String-Based HTML & The Trusted Types Revolution

For three decades, DOM-based Cross-Site Scripting (DOM XSS) remained the most prevalent vulnerability in web applications. It occurs because the browser treats untrusted strings passed to **injection sinks** as executable code:

- **Dangerous Injection Sinks**: element.innerHTML, element.outerHTML, document.write(), window.eval(), scriptElement.src, setTimeout(string).

- **Why Traditional Sanitizers Fail**: Regular expressions and ad-hoc string escaping libraries frequently suffer from parser mismatch vulnerabilities (mutator XSS / mXSS) where the sanitizer's parsing rules diverge from the browser engine's live DOM parser.

**Trusted Types (W3C)** eliminates DOM XSS at the browser compiler level by locking down the DOM API. When enabled via CSP:

- The browser **strictly refuses to accept plain strings** in injection sinks!

- Passing a string (el.innerHTML = userInput) throws an immediate, fatal TypeError.

- Only blessed instances of TrustedHTML, TrustedScript, or TrustedScriptURL created through cryptographically audited policies are permitted.

```text
┌────────────────────────────────────── Trusted Types Compiler Gatekeeper ──────────────────────────────────────┐
│                                                                                                                │
│  Traditional DOM (Vulnerable to XSS) ⚠️:                                                                       │
│  userInput (String) ──► element.innerHTML ──► Browser Parses String as Executable DOM ──► 🚨 XSS Execution!   │
│                                                                                                                │
│  Trusted Types Enforced (Zero-Trust DOM) 🛡️:                                                                   │
│  userInput (String) ──► element.innerHTML ──► 🛑 Uncaught TypeError: Failed to set 'innerHTML':               │
│                                                  This document requires 'TrustedHTML' assignment.              │
│                                                                                                                │
│  Blessed Policy Path:                                                                                          │
│  userInput ──► trustedTypes.createPolicy('dom-purify', { createHTML }) ──► TrustedHTML Token ──► innerHTML ⚡ │
│                                                                                                                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Implementing a Compliant Trusted Types Policy:

// Registering a strictly controlled policy

if (window.trustedTypes && window.trustedTypes.createPolicy) {

const sanitizePolicy = trustedTypes.createPolicy('app-security-policy', {

createHTML: (dirtyString) => {

// Pass through an industry-standard DOMPurify sanitizer

return DOMPurify.sanitize(dirtyString, { RETURN_TRUSTED_TYPE: false });

},

createScriptURL: (url) => {

// Whitelist permitted CDN script origins

const parsed = new URL(url, document.baseURI);

if (parsed.origin === 'https://cdn.enterprise.com') {

return parsed.href;

}

throw new SecurityError(`Untrusted script URL blocked: \${url}`);

},

});

// Assigning via blessed token

const container = document.getElementById('content');

container.innerHTML = sanitizePolicy.createHTML('<h1>Safe Content</h1>');

}

### 2. Modern Content Security Policy (CSP Level 3): Strict Nonces & 'strict-dynamic'

Legacy CSP configurations relied on broad domain whitelists (script-src https://*.googleapis.com https://cdnjs.cloudflare.com).

- **The Whitelist Bypass Flaw**: Whitelisted domains frequently host legacy libraries with JSONP endpoints, allowing attackers to construct payloads like <script src="https://cdnjs.cloudflare.com/\.../angular.js?callback=alert(1)"></script>.

**CSP Level 3** abandons domain whitelists in favor of **Cryptographic Nonces** and 'strict-dynamic':

Content-Security-Policy:

script-src 'nonce-rAnd0m12345' 'strict-dynamic' 'unsafe-inline' https: http:;

object-src 'none';

base-uri 'none';

require-trusted-types-for 'script';

- **Cryptographic Nonce**: Every server response generates an unguessable 128-bit Base64 nonce injected into the header and script tags: <script nonce="rAnd0m12345">.

- **'strict-dynamic'**: Instructs the browser that any script already authorized by the valid nonce is trusted to dynamically load auxiliary scripts (e.g. Webpack bundle chunks) via document.createElement('script') without needing nonces on every chunk!

- **Fallbacks**: 'unsafe-inline' https: http: are ignored by modern browsers when a nonce is present, providing backward compatibility for legacy browsers.

### 3. Cross-Origin Isolation & Microarchitectural Spectre Mitigations

In 2018, the **Spectre** vulnerability revealed that speculative execution in modern CPU hardware allows malicious JavaScript code to read arbitrary bytes of host memory across process boundaries.

- **The Attack Vector**: Attackers measure the execution time of CPU cache line hits versus misses with extreme precision using high-resolution timers (performance.now()).

- **The Browser Defense Response**: Browsers degraded timer precision (rounding performance.now() from sub-microsecond to \$100\\mu\\text{s}\$) and completely disabled SharedArrayBuffer by default to eliminate multi-threaded concurrent memory access.

#### Unlocking High-Performance Web Features:

To re-enable SharedArrayBuffer, high-precision timers, and WebAssembly multi-threading, the server must declare **Cross-Origin Isolation**:

Cross-Origin-Opener-Policy: same-origin

Cross-Origin-Embedder-Policy: require-corp

Cross-Origin-Resource-Policy: same-origin

1.  **COOP (same-origin)**: Forces the browser to isolate your application's browsing context into a dedicated, sandboxed operating system process, breaking any window.opener references from external tabs.

2.  **COEP (require-corp)**: Guarantees that the document cannot load any cross-origin resource (images, scripts, styles) unless the resource explicitly consents via CORP (Cross-Origin-Resource-Policy: cross-origin).

3.  **Verification**: In JavaScript, window.crossOriginIsolated === true confirms that high-precision hardware clocks and SharedArrayBuffer can be safely instantiated.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Browser Security Headers Matrix:

---------------------------------------------------------------------------------- **HTTP Header**                **Directive / Value**       **Defensive Purpose** ------------------------------ --------------------------- ----------------------- Content-Security-Policy        require-trusted-types-for   Enforces strict 'script'                  TrustedHTML tokens; blocks string-based DOM injection.

Content-Security-Policy        script-src 'nonce-\...'   Modern nonce-based 'strict-dynamic'          execution with transitive trust for dynamic loaders.

Content-Security-Policy        frame-ancestors 'none'    Prevents clickjacking attacks (replaces legacy X-Frame-Options: DENY).

Cross-Origin-Opener-Policy     same-origin (COOP)          Isolates top-level browsing context into an exclusive OS process.

Cross-Origin-Embedder-Policy   require-corp (COEP)         Blocks loading any cross-origin subresource without explicit CORP headers.

Cross-Origin-Resource-Policy   same-origin (CORP)          Prevents external domains from embedding your assets. ----------------------------------------------------------------------------------

### Trusted Types API Methods:

// Check browser support

if (window.trustedTypes) {

// Create immutable policy

const policy = trustedTypes.createPolicy('my-policy', {

createHTML: (input: string) => sanitize(input),

createScript: (input: string) => validateScript(input),

createScriptURL: (input: string) => validateURL(input),

});

// Verify type

console.log(trustedTypes.isHTML(policy.createHTML('<div></div>'))); // true

console.log(trustedTypes.isHTML('<div></div>')); // false

}

## SECTION 3: PRACTICAL PROBLEMS

### Problem 1 (Basic): Trusted Types Policy with Fallback Shims

**Context**: An enterprise application is migrating to strict Trusted Types enforcement. However, legacy browsers (or development environments without CSP headers) throw errors if window.trustedTypes is accessed blindly.

**Challenge**: Implement a robust SecurityTypeFactory wrapper:

1.  Detects native window.trustedTypes. If present and not locked, creates or retrieves a singleton policy 'app-sanitizer'.

2.  If Trusted Types is unsupported by the browser, provides a transparent pass-through shim returning string primitives with identical method signatures (createHTML, createScriptURL).

3.  If an attacker attempts to define a duplicate policy with malicious overrides, handle TypeError and fail closed by throwing a PolicyTamperingError.

*Hint: Use trustedTypes.getPolicyNames() to check if the policy already exists before calling createPolicy().*

### Problem 2 (Intermediate): Security Policy Violation Telemetry Dispatcher

**Context**: When rolling out a strict CSP and Trusted Types configuration across millions of users, unexpected third-party scripts or legacy plugins trigger violations that must be captured in real time without impacting page performance.

**Challenge**: Build a CSPViolationReporter class in TypeScript:

1.  Listens for securitypolicyviolation events on the window object:

    - Captures: blockedURI, violatedDirective, originalPolicy, sample (the offending payload prefix), lineNumber, and sourceFile.

2.  Debounces and aggregates violations into an in-memory queue.

3.  Transmits telemetry payloads via navigator.sendBeacon('/api/csp-reports', payload) when the batch reaches 10 items or during visibilitychange (page unload).

4.  Verifies that the reporter itself never violates CSP (uses zero inline scripts or dynamic code evaluation).

*Hint: Remember to handle event.sample safely, as it may contain truncated attack vectors.*

### Problem 3 (Advanced): High-Precision Benchmark Isolation Harness

**Context**: High-performance WebAssembly cryptographic libraries require sub-microsecond latency benchmarks (performance.now()) and multithreaded worker coordination (SharedArrayBuffer), which fail completely unless the environment is cross-origin isolated.

**Challenge**: Develop an execution gatekeeper and diagnostic harness IsolatedEnvironmentHarness:

1.  Checks window.crossOriginIsolated.

2.  If false, inspects the current document's execution context:

    - Tests whether high-resolution timers are artificially jittered/rounded.

    - Probes for the presence of COOP and COEP headers via diagnostic fetch requests.

    - Emits a structured diagnostic report detailing which specific headers are missing (COOP: same-origin or COEP: require-corp).

3.  If true:

    - Instantiates a SharedArrayBuffer of 1MB.

    - Spawns two dedicated Web Workers.

    - Coordinates an atomic lock using Atomics.wait() and Atomics.notify() without throwing security exceptions.

    - Measures clock resolution by computing the minimum non-zero delta of performance.now(), verifying sub-microsecond precision.

*Hint: In a cross-origin isolated environment, performance.now() can provide precision down to 5 microseconds, whereas non-isolated browsers quantize it to 100 microseconds.*
