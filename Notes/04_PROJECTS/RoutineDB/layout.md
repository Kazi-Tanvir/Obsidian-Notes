---
tags: [ui, layout, nextjs, routing, clerk, frontend]
---

# Page: Root Layout

This page represents the entry point layout wrapper for all routes in the application, located at `src/app/layout.tsx`. It coordinates the HTML frame, global styles, and provides the authentication context.

- **File Link**: [layout.tsx](file:///d:/02_CODE/04_TEST/Routine/src/app/layout.tsx)
- **Backlink**: [[index]], [[DESIGN]]

---

## Technical Details

The Root Layout uses standard Next.js Server Component layout conventions, wrapping all dynamic child pages in the **Clerk Provider** to enable frontend session tokens.

### Configuration
1. **Metadata Definition**: Specifies the application title and description used for browser tabs and search engine optimization.
2. **Style Bootstrapping**: Imports `globals.css` directly, ensuring theme variables are initialized before page renders.
3. **Clerk Auth Wrapper**: Uses `<ClerkProvider>` to handle authentication state globally, shielding pages from loading without valid authentication credentials.

---

## Source Code

Here is the complete implementation of `src/app/layout.tsx`:

```tsx
import type { Metadata } from "next";
import { ClerkProvider } from '@clerk/nextjs';
import "./globals.css";

export const metadata: Metadata = {
  title: "Routine Planner | Multi-User Schedule & Attendance Tracker",
  description: "A paper-styled daily class routine planner and attendance tracker with multi-user authentication, admin-managed templates, and real-time scheduling.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <ClerkProvider>
          <main className="app-main">
            {children}
          </main>
        </ClerkProvider>
      </body>
    </html>
  );
}
```
