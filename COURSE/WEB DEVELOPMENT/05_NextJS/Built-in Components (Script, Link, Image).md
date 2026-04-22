---
tags:
- nextjs
- optimization
- web-vitals
---
# Built-in Components (Script, Link, Image)

## What's the Actual Use?
Next.js provides specialized components that automatically optimize your application's performance. `Image` handles lazy loading and resizing, `Link` enables fast pre-fetching for navigation, and `Script` manages how third-party scripts (like Analytics) are loaded without slowing down the page.

## Other Common Use Cases
- **Image:** Automatically converting PNGs/JPGs to WebP for smaller file sizes.
- **Link:** Pre-loading the "About" page while the user is still on the "Home" page.
- **Script:** Loading a Google Ads script only after the main page is interactive.

## Documentation & Code
These components replace standard HTML tags (`<img>`, `<a>`, `<script>`).

```jsx
import Image from 'next/image';
import Link from 'next/link';
import Script from 'next/script';

export default function Home() {
  return (
    <>
      {/* 1. Optimized Image (Prevents layout shift, handles resizing) */}
      <Image 
        src="/profile.jpg" 
        alt="Profile" 
        width={500} 
        height={500} 
        priority // Load this immediately
      />

      {/* 2. Optimized Link (Pre-fetches the page for instant navigation) */}
      <Link href="/dashboard">Go to Dashboard</Link>

      {/* 3. Optimized Script (Loads strategy like 'afterInteractive') */}
      <Script 
        src="https://example.com/analytics.js" 
        strategy="afterInteractive" 
      />
    </>
  );
}
```