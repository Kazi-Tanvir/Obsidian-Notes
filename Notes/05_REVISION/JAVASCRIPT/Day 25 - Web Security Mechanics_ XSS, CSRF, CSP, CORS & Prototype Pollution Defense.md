---
tags:
- javascript
- security
- xss
- csrf
- csp
- cors
- prototype-pollution
- web-security
date: 2026-08-25
---

# Day 25 - Web Security Mechanics: XSS, CSRF, CSP, CORS & Prototype Pollution Defense

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Client-Side & Runtime Vulnerability Mechanics

Modern JavaScript applications execute in hostile client environments. Securing the runtime requires understanding browser sandbox boundaries, execution contexts, and object prototype integrity.

### 2. Core Security Attack Vectors & Defenses

#### A. Cross-Site Scripting (XSS)

Occurs when an attacker injects malicious executable scripts into a trusted web application.

- **Stored XSS**: Injected script is permanently stored in the database and served to all users.

- **Reflected XSS**: Injected script is reflected off the web server via URL query parameters or form inputs.

- **DOM-based XSS**: Attack occurs entirely in the browser when untrusted user input is written to dangerous execution sinks.

```javascript
// Vulnerable DOM Sink
const userInput = new URLSearchParams(window.location.search).get("profile");
document.getElementById("bio").innerHTML = userInput; // DOM XSS if userInput contains <img src=x onerror=alert(1)>
// Secure DOM Alternative (Safe Text Node Assignment)
document.getElementById("bio").textContent = userInput;
// Secure HTML Sanitization via DOMPurify & Trusted Types API
import DOMPurify from 'dompurify';
if (window.trustedTypes && window.trustedTypes.createPolicy) {
const sanitizePolicy = window.trustedTypes.createPolicy('default', {
```

createHTML: (string) => DOMPurify.sanitize(string, { RETURN_TRUSTED_TYPE: true }),

```javascript
});
document.getElementById("bio").innerHTML = sanitizePolicy.createHTML(userInput);
}
```

#### B. Prototype Pollution

A JavaScript vulnerability where an attacker modifies Object.prototype via property paths like __proto__, constructor.prototype, causing injected properties to be inherited by all plain objects across the entire application runtime.

```javascript
// Vulnerable Recursive Merge Function
function mergeVulnerable(target, source) {
for (let key in source) {
if (typeof source[key] === "object" && source[key] !== null) {
if (!target[key]) target[key] = {};
mergeVulnerable(target[key], source[key]);
} else {
target[key] = source[key];
}
}
return target;
}
// Attack Payload:
// JSON.parse('{"__proto__": {"isAdmin": true}}')
// After merge, ({}).isAdmin === true (Global Prototype Polluted!)
// Secure Merge Defense (Key Filtering & Null-Prototype Dictionaries)
function mergeSecure(target, source) {
for (let key of Object.keys(source)) {
// Block prototype pollution vectors
if (key === "__proto__" || key === "constructor" || key === "prototype") {
continue;
}
if (typeof source[key] === "object" && source[key] !== null && !Array.isArray(source[key])) {
if (!target[key] || typeof target[key] !== "object") {
target[key] = Object.create(null); // Null prototype prevents prototype inheritance lookup
}
mergeSecure(target[key], source[key]);
} else {
target[key] = source[key];
}
}
return target;
}
```

#### C. Cross-Site Request Forgery (CSRF) & SameSite Cookies

Forces an authenticated end user to execute unwanted actions on a web application where they are currently authenticated.

**Defenses**:

1.  **SameSite Cookie Policies**:

    - SameSite=Strict: Cookie is never sent on cross-site requests (e.g. following links).

    - SameSite=Lax: Cookie is withheld on cross-site sub-requests (images, iframes) but sent on top-level navigation GET requests.

    - SameSite=None; Secure: Sent on cross-site requests, requires HTTPS.

2.  **Anti-CSRF Synchronizer Tokens / Double Submit Cookie Pattern**: State-changing requests (POST, PUT, DELETE) require a cryptographically random token in custom headers (X-CSRF-Token).

#### D. Content Security Policy (CSP) & CORS

- **CSP**: HTTP response header restricting the sources from which scripts, styles, and images can load.

  - Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-rAnd0m123' 'strict-dynamic'; object-src 'none'; base-uri 'none'; frame-ancestors 'none';

- **CORS (Cross-Origin Resource Sharing)**: Browser security mechanism that enforces the Same-Origin Policy (SOP). Non-simple requests trigger a preflight OPTIONS request validating Access-Control-Allow-Origin, Access-Control-Allow-Methods, and Access-Control-Allow-Headers.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Security Directives & Protection Matrix:

| **Protection Mechanism** | **Type** | **Syntax / Header** | **Defense Target** |
| --- | --- | --- | --- |
| **Content Security Policy** | HTTP Header | Content-Security-Policy: default-src 'self'; script-src 'nonce-{RANDOM}'   XSS | Data Exfiltration, Clickjacking |
| **SameSite Cookies** | Cookie Flag | Set-Cookie: session=xyz; Secure; HttpOnly; SameSite=Strict | CSRF, Session Hijacking |
| **Prototype Immunity** | JS Pattern | Object.create(null) or Object.freeze(Object.prototype) | Prototype Pollution |
| **Frame Ancestors** | CSP Header | frame-ancestors 'none' (replaces legacy X-Frame-Options)                     U | Redressing / Clickjacking |
| **Strict-Transport-Security** | HTTP Header | Strict-Transport-Security: max-age=63072000; includeSubDomains; preload | SSL-Stripping & MITM attacks |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Prototype Pollution Exploitation & Leakage Analysis

Analyze the snippet below. Predict the evaluated result of user.isAdmin and explain the exact V8 prototype chain traversal step that occurs:

```javascript
const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
function cloneConfig(target, src) {
for (let key in src) {
if (typeof src[key] === "object") {
target[key] = cloneConfig(target[key] || {}, src[key]);
} else {
target[key] = src[key];
}
}
return target;
}
const config = cloneConfig({}, payload);
const user = {};
console.log(user.isAdmin);
console.log(Object.prototype.hasOwnProperty("isAdmin"));
```

*Hint*: Determine whether target[key] resolution when key === "__proto__" references the internal prototype pointer of target.

### Challenge 2: Refactoring Unsafe Template Rendering to Trusted Types

Refactor the following vulnerable user comment notification renderer into a secure, CSP-compliant implementation that enforces the **Trusted Types API** and sanitizes untrusted input using strict schema validation:

```javascript
// Vulnerable Component
function renderNotification(container, notification) {
```

container.innerHTML = `

<div class="notification">

<h4>${notification.title}</h4>

<p>${notification.message}</p>

<a href="${notification.actionUrl}">View Details</a>

</div>

```javascript
`;
}
```

*Hint*: Handle dangerous javascript: pseudo-protocols in href attributes in addition to HTML entity escaping.

### Challenge 3: Advanced Prototype Pollution & Security Guard Suite

Build a comprehensive **Runtime Security Guard Utility** in TypeScript:

1.  createSafeDictionary<T>(): Returns an object completely immune to prototype pollution using null prototypes and proxy access controls.

2.  deepCloneSecure<T>(obj: T): A high-performance recursive deep clone function that actively strips and ignores __proto__, constructor, and prototype keys without throwing errors.

3.  freezeGlobalPrototypes(): Freezes core built-in prototypes (Object.prototype, Array.prototype, Function.prototype) while logging any attempted monkey-patching in development mode.
