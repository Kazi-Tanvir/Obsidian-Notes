---
tags:
- design
- figma
- ui-ux
---
# Figma Basics

## What's the Actual Use?
Figma is a collaborative web-based design tool used for creating user interfaces (UI) and user experiences (UX). It allows developers to see exactly how a website should look (colors, spacing, fonts) before they start writing any code.

## Real-Life Analogy
Figma is like a digital architect's drawing for a building. You wouldn't start laying bricks without a blueprint; similarly, you shouldn't start writing CSS without a Figma design. It shows you exactly where the "windows" and "doors" go so you don't have to guess.

## Other Common Use Cases
- Creating interactive prototypes to show how a user would click through an app.
- Handing over designs to developers (Dev Mode shows CSS properties for elements).
- Creating assets like icons, logos, and banners for websites.

## Documentation & Code
While Figma isn't code, developers use the **Inspect Panel** (or Dev Mode) to extract CSS values:

```css
/* Example values a developer might copy from Figma */
.hero-button {
  width: 200px;
  height: 50px;
  background: #6200EE;
  border-radius: 8px;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  color: #FFFFFF;
}
```

**Key Shortcuts:**
- `V`: Move Tool
- `F`: Frame Tool (creates a screen)
- `Alt + Mouse Move`: Measure distance between elements.