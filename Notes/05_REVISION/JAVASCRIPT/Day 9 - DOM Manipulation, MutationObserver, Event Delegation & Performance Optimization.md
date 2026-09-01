---
tags:
- javascript
- dom
- events
- event-delegation
- mutation-observer
- performance
date: 2026-08-09
---

# Day 9 - DOM Manipulation, MutationObserver, Event Delegation & Performance Optimization

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Critical Rendering Path & Layout Thrashing

When JavaScript modifies the DOM or queries geometry, the browser runs through the **Critical Rendering Path**: DOM + CSSOM -> Render Tree -> Layout (Reflow) -> Paint -> Composite.

- **Reflow (Layout)**: Recalculates position and dimensions of elements.

- **Repaint**: Re-draws visual attributes (colors, background) without changing geometry.

- **Layout Thrashing**: Occurs when JavaScript interleaves DOM writes and DOM reads in a loop, forcing synchronous forced reflows.

```javascript
// Anti-Pattern: Layout Thrashing (Forced Synchronous Layout)
const boxes = document.querySelectorAll('.box');
for (let i = 0; i < boxes.length; i++) {
// READ (forces layout calculation) -> WRITE (invalidates layout) -> READ (forces recalculation)
const width = boxes[i].offsetWidth;
boxes[i].style.width = `${width + 10}px`;
}
// Optimized Pattern: Read-first, then Batch Writes using requestAnimationFrame
const widths = Array.from(boxes).map(box => box.offsetWidth); // Batch READs
```

requestAnimationFrame(() => {

```javascript
boxes.forEach((box, i) => {
box.style.width = `${widths[i] + 10}px`; // Batch WRITEs
});
});
```

### 2. Event Propagation & Event Delegation Pattern

Browser events flow in three distinct phases:

1.  **Capturing Phase**: Descends from window down to the target parent.

2.  **Target Phase**: Reaches the target element.

3.  **Bubbling Phase**: Ascends back up to window.

**Event Delegation** leverages event bubbling by attaching a single listener to a common ancestor rather than binding listeners to hundreds of individual child nodes.

```javascript
// Event Delegation on a Dynamic Data Table
const table = document.querySelector('#data-table');
table.addEventListener('click', (event) => {
// Use .closest() to find matching element even if child icon is clicked
const actionBtn = event.target.closest('.delete-btn');
if (!actionBtn) return;
const rowId = actionBtn.dataset.id;
deleteRow(rowId);
});
```

### 3. Asynchronous DOM Monitoring: MutationObserver

MutationObserver monitors DOM tree modifications asynchronously without blocking the rendering thread or polling.

```javascript
const targetNode = document.querySelector('#dynamic-container');
const observer = new MutationObserver((mutationsList, observer) => {
for (const mutation of mutationsList) {
if (mutation.type === 'childList') {
console.log('Child nodes added/removed:', mutation.addedNodes);
} else if (mutation.type === 'attributes') {
console.log(`Attribute ${mutation.attributeName} modified.`);
}
}
});
observer.observe(targetNode, {
```

childList: true,

subtree: true,

attributes: true,

attributeFilter: ['class', 'data-status']

```javascript
});
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **DOM API / Concept** | **Syntax / Option** | **Description** |
| --- | --- | --- |
| **addEventListener** | el.addEventListener(type, fn, { passive: true, once: true }) | passive: true prevents preventDefault(), boosting scroll performance |
| **DocumentFragment** | const frag = document.createDocumentFragment() | Off-screen memory node container; appends in a single reflow |
| **closest()** | el.closest('.selector')                                      T | averses up DOM tree to find matching ancestor |
| **MutationObserver** | obs.observe(node, { childList, subtree, attributes }) | Asynchronously monitors DOM mutations |
| **Layout Triggers** | offsetWidth, offsetHeight, getBoundingClientRect() | Triggers synchronous layout (Reflow) when called after writes |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Layout Thrashing Analysis & Refactoring

Analyze the following code snippet, identify how many forced reflows occur during execution, and refactor it into an $O(1)$ reflow operation.

```javascript
function resizeCards() {
const cards = document.querySelectorAll('.card');
for (let i = 0; i < cards.length; i++) {
const currentHeight = cards[i].getBoundingClientRect().height;
if (currentHeight < 200) {
cards[i].style.height = '200px';
cards[i].style.backgroundColor = 'lightgreen';
}
}
}
```

*Hint*: Separate geometry queries from style mutations.

### Challenge 2: Refactoring High-Node List Rendering

A dynamic messaging app appends 10,000 message nodes individually in a for loop, causing browser freeze. Refactor it using DocumentFragment and implement Event Delegation for message click handlers.

```javascript
// Buggy Code causing 10,000 Reflows
function renderMessages(messages) {
const list = document.querySelector('#message-list');
messages.forEach(msg => {
const li = document.createElement('li');
li.textContent = msg.text;
li.addEventListener('click', () => markAsRead(msg.id)); // 10,000 listeners!
list.appendChild(li); // 10,000 DOM appends!
});
}
```

*Hint*: Build nodes inside a single fragment and attach one click handler on #message-list.

### Challenge 3: Building a Reactive DOM Form Auto-Save Watcher

Write a custom JS module createFormWatcher(formElement, onSaveCallback) using MutationObserver and Event Delegation that:

1.  Listens for input changes across dynamically added input fields.

2.  Uses MutationObserver to automatically bind change listeners when new form input elements are dynamically injected.

3.  Debounces saves by 500ms before calling onSaveCallback(formData).

*Hint*: Combine MutationObserver for childList additions with debounced event delegation.
