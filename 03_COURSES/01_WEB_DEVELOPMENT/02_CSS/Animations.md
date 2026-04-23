---
tags:
- css
- animation
- keyframes
---
# Animations

## What's the Actual Use?
Animations allow for complex, multi-step movements using `@keyframes`. Unlike transitions, animations can start automatically and loop infinitely.

## Real-Life Analogy
If a **Transition** is a light dimmer (smoothly going from off to on), an **Animation** is a choreographed dance (a series of specific movements over time).

## Other Common Use Cases
- Creating loading spinners.
- Making a "bounce" effect on a call-to-action button.

## Documentation & Code
Define the animation with `@keyframes` and apply it with the `animation` property.

````css
@keyframes slideIn {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
}

.sidebar {
    animation: slideIn 0.5s ease-out forwards;
}
````
