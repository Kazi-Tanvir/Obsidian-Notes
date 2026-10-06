tags:

- javascript

- micro-frontends

- module-federation

- webpack

- vite

- architecture

- sandbox

- performance date: 2026-09-14

# Day 45 - Micro-Frontends Architecture, Module Federation, Webpack 5 vs Vite & Sandbox Isolation

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The Monolithic Frontend Bottleneck & The Micro-Frontend Paradigm

As engineering organizations scale past 50+ developers, frontend
single-page applications (SPAs) become organizational bottlenecks:

- Giant repositories trigger multi-hour build pipelines.

- Tight coupling means a bug in the settings page can prevent shipping
  the checkout flow.

- Deployment velocity grinds to a halt.

**Micro-Frontends** decompose monolithic frontends into autonomous,
independently deployable web applications that co-exist in a single
unified user experience.

┌────────────────────────────────────── Micro-Frontend Integration
Styles ──────────────────────────────────────┐

│ │

│ Build-Time Integration (npm Packages) ⚠️ │

│ • Components published as private npm modules. │

│ • Disadvantage: Host app must be rebuilt and redeployed whenever a
package updates (Coupled release cycles!).│

│ │

│ Run-Time Integration: iframes ⚠️ │

│ • Perfect CSS and JS isolation. │

│ • Disadvantage: High memory overhead, broken UX (modals trapped in
iframe), slow routing, deep linking pain. │

│ │

│ Modern Run-Time Integration: Module Federation (Webpack 5 / Vite) 🚀 │

│ • Independent deployments load dynamic remote JS bundles directly in
browser memory. │

│ • Shared dependency negotiation (Single copy of React / UI library
across remotes!). │

│ • Full native browser performance, shared routing, and seamless DOM
composition. │

│ │

└───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Webpack 5 Module Federation Architecture

Module Federation allows a JavaScript application to dynamically load
code from another build at runtime.

- **Host (Shell)**: The root container application that orchestrates
  routing and mounts remotes.

- **Remote**: An independent application exposing specific modules
  (exposes).

- **Shared Scope (shared)**: Defines dependencies that can be shared
  between the host and remotes to prevent downloading duplicate
  libraries.

// host/webpack.config.js

const { ModuleFederationPlugin } = require(\'webpack\').container;

module.exports = {

plugins: \[

new ModuleFederationPlugin({

name: \'shell_app\',

remotes: {

// Points to the remote entry bundle published by team Checkout:

checkout:
\'checkout_app@https://checkout.enterprise.com/remoteEntry.js\',

},

shared: {

react: { singleton: true, requiredVersion: \'\^18.2.0\', eager: false },

\'react-dom\': { singleton: true, requiredVersion: \'\^18.2.0\' },

},

}),

\],

};

// checkout-remote/webpack.config.js

const { ModuleFederationPlugin } = require(\'webpack\').container;

module.exports = {

plugins: \[

new ModuleFederationPlugin({

name: \'checkout_app\',

filename: \'remoteEntry.js\',

exposes: {

// Exposes internal component for consumption by Host:

\'./CartWidget\': \'./src/components/CartWidget\',

},

shared: {

react: { singleton: true, requiredVersion: \'\^18.2.0\' },

\'react-dom\': { singleton: true, requiredVersion: \'\^18.2.0\' },

},

}),

\],

};

#### Shared Scope Resolution & The Singleton Rule:

When multiple federated apps request react, Webpack\'s runtime
initializes \_\_webpack_share_scopes\_\_.default.

- If singleton: true is configured, only the highest compatible semver
  instance is loaded into memory.

- If versions conflict and strictVersion: true is enabled, Webpack
  rejects the mismatch; if strictVersion: false, it falls back to
  loading separate versions with a runtime warning.

### 3. Dynamic Remote Loading at Runtime

Hardcoding remote URLs in Webpack configs prevents multi-environment
deployments (staging vs. production). Modern hosts load remotes
dynamically by URL at runtime:

// Dynamic Remote Script Injector & Initializer

export async function loadDynamicRemote(remoteUrl: string, scope:
string, module: string) {

// 1. Inject script tag if not already present

if (!document.querySelector(\`script\[src=\"\${remoteUrl}\"\]\`)) {

await new Promise\<void\>((resolve, reject) =\> {

const script = document.createElement(\'script\');

script.src = remoteUrl;

script.type = \'text/javascript\';

script.async = true;

script.onload = () =\> resolve();

script.onerror = () =\> reject(new Error(\`Failed to load remote:
\${remoteUrl}\`));

document.head.appendChild(script);

});

}

// 2. Initialize the container with the shared scope

// \@ts-ignore

const container = window\[scope\];

// \@ts-ignore

await container.init(\_\_webpack_share_scopes\_\_.default);

// 3. Obtain factory and resolve module

const factory = await container.get(module);

return factory();

}

### 4. Client Sandbox Isolation via Window Proxy

When micro-frontends are not encapsulated inside Shadow DOM, an errant
remote can pollute window (e.g. window.currentUser = \...), breaking
neighboring remotes.

A **Proxy Sandbox** provides each micro-app with a virtualized window
object:

export class WindowProxySandbox {

private fakeWindow: Record\<string, any\> = {};

public proxy: Window;

public active = false;

constructor() {

const rawWindow = window;

this.proxy = new Proxy(rawWindow, {

get: (target, prop: string) =\> {

if (this.fakeWindow.hasOwnProperty(prop)) {

return this.fakeWindow\[prop\];

}

return (target as any)\[prop\];

},

set: (target, prop: string, value: any) =\> {

if (this.active) {

this.fakeWindow\[prop\] = value; // Trap writes locally!

}

return true;

},

});

}

activate() { this.active = true; }

deactivate() { this.active = false; this.fakeWindow = {}; }

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Module Federation shared Flags Reference:

  -----------------------------------------------------------------------
  **Flag**                **Type**                **Description**
  ----------------------- ----------------------- -----------------------
  singleton               boolean                 Allows only a single
                                                  version of the shared
                                                  module across all
                                                  remotes (Required for
                                                  React).

  requiredVersion         string                  Semver range (\^18.0.0)
                                                  acceptable for this
                                                  application.

  strictVersion           boolean                 If true, throws runtime
                                                  error if required
                                                  semver cannot be
                                                  satisfied.

  eager                   boolean                 If true, bundles module
                                                  into initial chunk
                                                  instead of lazy-loading
                                                  (Avoid on remotes).
  -----------------------------------------------------------------------

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: The \"Invalid Hook Call\" Singleton Crash

Analyze why the following error occurs in a Module Federation setup:

Error: Invalid hook call. Hooks can only be called inside the body of a
function component.

1\. You might have mismatching versions of React and the renderer (such
as React DOM).

2\. You might be breaking the Rules of Hooks.

3\. You might have more than one copy of React in the same app.

*Question*: Explain how a failure to configure { singleton: true } on
react and react-dom in both the Host and Remote configurations causes
two distinct React dispatcher instances to load into memory, triggering
this fatal crash.

### Challenge 2: Dynamic Fallback Error Boundary for Offline Remotes

Build a React Error Boundary component (\<RemoteFederationBoundary\>)
that wraps dynamic federated components:

1.  Catches network failures when a remote\'s server is down
    (remoteEntry.js 404/500).

2.  Renders a branded fallback card informing the user that the specific
    sub-service is temporarily unavailable.

3.  Provides an automated retry trigger button that purges the cached
    script tag and attempts re-fetching the remote container.

### Challenge 3: Enterprise Micro-Frontend Orchestrator Engine in TypeScript

Build an Enterprise **Micro-Frontend Lifecycle Orchestrator** in
TypeScript:

**Requirements**:

1.  **App Registry**:

    - Manages an array of registered micro-apps { name, entryUrl,
      routePrefix, scope }.

2.  **Route Matching & Lazy Mount**:

    - Listens to browser popstate and hashchange events.

    - Automatically loads and mounts the active micro-frontend into a
      designated container DOM node when the URL matches routePrefix.

3.  **Multi-Tenant Proxy Sandboxing**:

    - Isolates each micro-app using a WindowProxySandbox so global
      variables defined by App A do not leak into App B.

    - Cleans up event listeners and DOM nodes when navigating away from
      the app\'s route prefix.
