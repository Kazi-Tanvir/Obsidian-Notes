---
tags: [theme, css, aesthetics, visuals, styles, frontend]
---

# Design System & Aesthetics: Routine Planner

This website features a custom, premium **sketchy, hand-written notebook/paper aesthetic** designed to evoke a retro school binder. It does not use component libraries or TailwindCSS for layout, but rather relies on a unified core stylesheet located at `src/app/globals.css` containing custom variables, layouts, and hand-drawn utility animations.

---

## 1. Typography

The design system loads three Google Fonts to distinguish standard UI controls from handwritten notebook contents:

```css
@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Caveat:wght@400;600;700&family=Outfit:wght@300;400;500;600;700&display=swap');
```

1. **`--font-ui`**: `'Outfit', sans-serif` — Used for layout wrappers, header bars, and utility buttons where clarity is key.
2. **`--font-hand`**: `'Caveat', cursive` — Used for user inputs, notes, descriptions, and class detail text to simulate a student's handwriting.
3. **`--font-sketch`**: `'Architects Daughter', cursive` — Used for main headings, subheadings, and badges to give a drawing/sketch outline appearance.

---

## 2. Color Palette & CSS Variables

The website features custom curated variables to match paper, ink, highlighter pens, and tape styles:

| CSS Variable | Value | Description |
| :--- | :--- | :--- |
| `--ink-charcoal` | `#2d3748` | Main text color, simulating charcoal pencil or dark pen ink. |
| `--ink-blue` | `#1a365d` | Secondary text color, simulating dark blue ballpoint pen ink. |
| `--ink-red` | `#742a2a` | Warning/Alert text, simulating red correcting pen ink. |
| `--paper-cream` | `#faf7f2` | Primary background color of notebook pages. |
| `--paper-line-blue` | `#e2ebf0` | Blue horizontal ruling lines for paper sheets. |
| `--margin-red` | `#ff8b8b` | Vertical red margin line on lined notebook sheets. |
| `--tape-yellow` | `rgba(24ef, 230, 150, 0.45)` | Washi tape background highlight. |
| `--hl-yellow` | `rgba(254, 240, 138, 0.6)` | Soft yellow highlighter overlay. |
| `--hl-green` | `rgba(187, 247, 208, 0.6)` | Soft green highlighter for active statuses (e.g. `PRESENT`). |
| `--hl-pink` | `rgba(254, 205, 211, 0.6)` | Soft pink highlighter for negative/inactive statuses (e.g. `ABSENT`). |

Each student can also customize their primary theme color using `user.color`, which gets injected into the DOM as `--user-theme-accent`.

---

## 3. Custom CSS Layout Classes

To recreate the binder design from scratch, implement these classes:

### Notebook Page Wrapper (`.notebook-page`)
Creates the wobbly rectangular sheet of paper with a shadow. It uses complex border radius division to give an organic, uneven shape:
```css
.notebook-page {
  background-color: var(--paper-cream);
  box-shadow: 6px 8px 0px rgba(0, 0, 0, 0.8);
  border: 3px solid var(--ink-charcoal);
  border-radius: 255px 15px 225px 15px/15px 225px 15px 255px; /* organic corners */
  padding: 2.5rem 2.5rem 2.5rem 4rem;
  position: relative;
  overflow: hidden;
}
```

### Lined Paper Rule (`.paper-lined`)
Generates the horizontal blue lines. Needs to align exactly with line heights:
```css
.paper-lined {
  background-image: linear-gradient(var(--paper-line-blue) 1px, transparent 1px);
  background-size: 100% 2.2rem;
  line-height: 2.2rem;
}
.paper-lined::before {
  content: '';
  position: absolute;
  top: 0;
  left: 3.2rem;
  width: 2px;
  height: 100%;
  background-color: var(--margin-red);
}
```

### Binder Ring Spiral (`.notebook-spiral` & `.spiral-ring`)
Sits in between pages to link them together:
```css
.spiral-ring {
  width: 45px;
  height: 22px;
  background: linear-gradient(180deg, #a0aec0 0%, #4a5568 50%, #1a202c 100%);
  border: 2px solid var(--ink-charcoal);
  border-radius: 12px;
  box-shadow: 2px 3px 0px rgba(0, 0, 0, 0.4);
}
```

### Wobbly Form Fields & Buttons (`.wobbly-box`, `.wobbly-input`)
All inputs, buttons, and panels must have unequal sketch borders:
```css
.wobbly-box {
  border: 2px solid var(--ink-charcoal);
  border-radius: 255px 12px 225px 15px/15px 225px 12px 255px;
  box-shadow: 3px 4px 0px var(--ink-charcoal);
}

.sketchy-btn {
  font-family: var(--font-sketch);
  border: 2px solid var(--ink-charcoal);
  border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
  background: white;
  cursor: pointer;
  transition: transform 0.1s ease;
}
.sketchy-btn:active {
  transform: translate(2px, 2px);
}
```

---

## 4. UI States & Highlighter Codes

State indicators mimic felt highlighter marker strokes:
- **PRESENT**: Wrapped in `.hl-green` (`background: var(--hl-green)`).
- **ABSENT**: Wrapped in `.hl-pink` (`background: var(--hl-pink)`).
- **CANCELLED / VACATION**: Marked with a strike-through (`text-decoration: line-through`) and highlighted using `--hl-yellow`.

---

## 5. Micro-Animations & Responsive Design

- **Wobbly bounce**: Buttons and cards slightly rotate or shift on hover to maintain the hand-drawn feeling.
- **Responsive Binder ring display**: On mobile views (`@media (max-width: 768px)`), the binder rings (`.notebook-spiral`) hide, and the pages layout transitions from side-by-side sheets to a stacked vertical sheet format.
- **Dynamic theme injection**:
  ```tsx
  <style jsx global>{`
    :root {
      --user-theme-accent: ${userColor};
    }
  `}</style>
  ```
