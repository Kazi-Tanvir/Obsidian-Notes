---
tags:
  - javascript
  - web-components
  - custom-elements
  - shadow-dom
  - html-templates
  - browser-architecture
  - encapsulation
date: 2026-09-03
---

# Day 34 - Shadow DOM, Web Components & Custom Elements Architecture

---

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. The 3 Pillars of the Web Components Standard

Web Components provide a native, framework-agnostic component model built directly into the browser. They rely on three foundational W3C standards:

1. **Custom Elements**: The JavaScript API (`customElements.define`) enabling developers to define custom HTML tags with lifecycle callbacks.
2. **Shadow DOM**: Provides true scoped CSS encapsulation and DOM tree isolation, preventing global styles and scripts from leaking in or out.
3. **HTML Templates (`<template>` & `<slot>`)**: User-defined HTML fragments parsed at page load but inert until cloned and rendered, with slots providing content projection.

┌────────────────────────────────────── Web Component DOM Hierarchy ──────────────────────────────────────┐

│                                                                                                         │

│  Light DOM (Document Scope)                                                                             │

│  ┌───────────────────────────────────────────────────────────────────────────────────────────────────┐  │

│  │ <user-card avatar="/img.png">                                                                     │  │

│  │   <span slot="username">Alice Walker</span> ──► Light DOM Slotted Element                         │  │

│  │                                                                                                   │  │

│  │   ┌─── #shadow-root (open) ────────────────────────────────────────────────────────────────────┐  │  │

│  │   │  Scoped CSS: :host { display: block; border: 1px solid #ccc; }                             │  │  │

│  │   │  <div class="card-inner">                                                                  │  │  │

│  │   │    <img class="avatar" src="/img.png" />                                                   │  │  │

│  │   │    <slot name="username"></slot> ◄── Projected from Light DOM!                             │  │  │

│  │   │  </div>                                                                                    │  │  │

│  │   └────────────────────────────────────────────────────────────────────────────────────────────┘  │  │

│  │ </user-card>                                                                                      │  │

│  └───────────────────────────────────────────────────────────────────────────────────────────────────┘  │

│                                                                                                         │

└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. Custom Element Lifecycle & Attribute Reflection

Autonomous Custom Elements extend `HTMLElement`. State synchronization between HTML attributes (strings) and JavaScript class properties requires explicit attribute reflection.

class DynamicCounter extends HTMLElement {

  static get observedAttributes() {

    return ['count', 'step'];

  }

  #count \= 0;

  #shadowRoot;

  constructor() {

    super();

    // Attach Shadow DOM tree in 'open' mode (accessible via this.shadowRoot)

    this.#shadowRoot \= this.attachShadow({ mode: 'open' });

  }

  // 1. Invoked when element is inserted into the document DOM tree

  connectedCallback() {

    this.#render();

    this.#shadowRoot.querySelector('#inc-btn').addEventListener('click', () \=> this.increment());

  }

  // 2. Invoked when element is removed from document DOM tree (Memory Cleanup!)

  disconnectedCallback() {

    // Remove global event listeners, disconnect observers, abort fetch controllers

  }

  // 3. Invoked whenever an observed attribute changes

  attributeChangedCallback(name, oldValue, newValue) {

    if (oldValue !== newValue) {

      if (name \=== 'count') this.#count \= parseInt(newValue, 10\) || 0;

      this.#updateDisplay();

    }

  }

  // Getter/Setter Property-to-Attribute Reflection

  get count() { return this.#count; }

  set count(val) {

    this.setAttribute('count', String(val));

  }

  increment() {

    const step \= parseInt(this.getAttribute('step'), 10\) || 1;

    this.count \+= step;

    // Dispatch Custom Event crossing Shadow DOM boundaries!

    this.dispatchEvent(new CustomEvent('count-change', {

      detail: { count: this.count },

      bubbles: true,   // Bubble up DOM tree

      composed: true,  // Crosses Shadow DOM boundary into Light DOM!

    }));

  }

  #render() {

    this.#shadowRoot.innerHTML \= `

      <style>

        :host { display: inline-flex; align-items: center; gap: 8px; font-family: sans-serif; }

        :host([disabled]) { opacity: 0.5; pointer-events: none; }

        .display { font-weight: bold; font-size: 1.2rem; }

        button { padding: 4px 12px; cursor: pointer; border-radius: 4px; border: 1px solid #777; }

      </style>

      <button id="inc-btn">+</button>

      <span class="display" id="val">${this.#count}</span>

    `;

  }

  #updateDisplay() {

    const valEl \= this.#shadowRoot?.querySelector('#val');

    if (valEl) valEl.textContent \= String(this.#count);

  }

}

customElements.define('dynamic-counter', DynamicCounter);

---

### 3. Event Retargeting & Boundary Crossing

When an event originates inside a Shadow DOM tree:

- If `composed: false`: The event stops at the shadow boundary and **never** reaches the document.
- If `composed: true`: The event crosses the shadow boundary into the Light DOM, but the browser **retargets** `event.target` to the custom host element (`<dynamic-counter>`) to preserve internal encapsulation.
- `event.composedPath()`: Returns an array of every node the event traversed, starting from the original internal element up to the `window`.

// Event Retargeting Demonstration

document.addEventListener('count-change', (event) \=> {

  console.log(event.target); // <dynamic-counter> (Retargeted! Internal button is hidden)

  console.log(event.composedPath()); // [button#inc-btn, shadow-root, dynamic-counter, body, html, document, window]

});

---

### 4. Declarative Shadow DOM (DSD) for SSR

Traditionally, Web Components required client-side JavaScript execution before the shadow root was created, causing Layout Shifts (CLS) in Server-Side Rendered (SSR) environments like Next.js.

**Declarative Shadow DOM** allows the backend to stream the shadow root directly as HTML:

<!-- Server-Rendered HTML (Zero Client-Side JavaScript required for initial render!) -->

<user-card avatar="/alice.png">

  <template shadowrootmode="open">

    <style>

      :host { display: block; padding: 16px; border: 1px solid #ddd; }

    </style>

    <div class="profile">

      <img src="/alice.png" alt="Avatar" />

      <slot name="username"></slot>

    </div>

  </template>

  <span slot="username">Alice Walker</span>

</user-card>

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Custom Element Lifecycle Callbacks Reference:

| Callback | Trigger Condition | Common Tasks |
| :---- | :---- | :---- |
| `connectedCallback()` | Element appended to document DOM | Attach event listeners, fetch initial data, render DOM |
| `disconnectedCallback()` | Element removed from document DOM | Remove listeners, abort fetch controllers, cleanup timers |
| `adoptedCallback()` | Element moved to a new document (e.g. `iframe`) | Rebind context, update environment-specific configs |
| `attributeChangedCallback()` | Observed attribute changed | Update internal state, trigger targeted re-renders |

### Shadow DOM Scoped CSS Pseudo-Selectors:

- `:host`: Targets the custom host element itself (`<user-card>`).
- `:host([theme="dark"])`: Matches host element when it possesses the `theme="dark"` attribute.
- `:host-context(.dark-mode)`: Matches host element if any ancestor in the Light DOM matches `.dark-mode`.
- `::slotted(selector)`: Styles elements projected into a `<slot>` from the Light DOM (can only style top-level slotted nodes).

---

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Event Boundary Leakage & Retargeting Prediction

Analyze the component implementation below:

class InternalWidget extends HTMLElement {

  connectedCallback() {

    const shadow \= this.attachShadow({ mode: 'open' });

    shadow.innerHTML \= `<input type="text" id="secret-input" />`;

    shadow.querySelector('#secret-input').addEventListener('input', (e) \=> {

      // Dispatches custom event

      this.dispatchEvent(new CustomEvent('data-input', {

        detail: { value: e.target.value },

        bubbles: true,

        composed: false // Note: composed is FALSE!

      }));

    });

  }

}

customElements.define('internal-widget', InternalWidget);

<div id="parent-container">

  <internal-widget></internal-widget>

</div>

*Question*: If a listener is attached to `document.getElementById('parent-container')` for `'data-input'`, does it fire when a user types into `#secret-input`? What if the listener listens for native `'input'` events instead? Explain why.

---

### Challenge 2: Autonomous Custom Form-Associated Element with ElementInternals

Refactor a custom styled switch toggle `<toggle-switch>` so that it seamlessly participates in standard HTML `<form>` submissions using the modern `ElementInternals` API (`this.attachInternals()`):

**Requirements**:

1. Form submission automatically includes the toggle's `name` and `value` when checked.
2. Supports form validation methods (`internals.setValidity()`).
3. Resets to default state when the parent form triggers `form.reset()`.

---

### Challenge 3: Accessible Design System Modal Dialog in TypeScript

Build an Enterprise-Grade **Autonomous Accessible Modal Dialog Web Component** (`<accessible-modal>`) in TypeScript:

**Requirements**:

1. **Encapsulation & Slots**:
   - Uses Shadow DOM (`mode: 'open'`).
   - Supports `<slot name="header">`, default `<slot>` for body content, and `<slot name="footer">` for actions.
2. **Focus Management & Accessibility**:
   - Implements a keyboard focus trap (Tab / Shift+Tab cycles strictly between internal interactive modal elements).
   - Closes on `Escape` key and clicks on backdrop overlay.
   - Automatically restores keyboard focus to the triggering element in the Light DOM when closed.
3. **Declarative Shadow DOM**:
   - Implements SSR hydration fallback allowing it to be prerendered with `<template shadowrootmode="open">`.

