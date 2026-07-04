---
tags: [ui, page, auth, clerk, user, frontend]
---

# Page: Sign Up / Register

This page wraps the Clerk Authentication Sign-Up component, located at `src/app/sign-up/[[...sign-up]]/page.tsx` and mapped to `/sign-up`.

- **File Link**: [page.tsx](file:///d:/02_CODE/04_TEST/Routine/src/app/sign-up/[[...sign-up]]/page.tsx)
- **Backlinks**: [[index]], [[layout]], [[proxy_middleware]]

---

## Technical Details

It is a basic layout container that renders the standard Clerk dynamic registration card. It is styled to center aligned dynamically on viewports.

### Source Code

```tsx
import { SignUp } from '@clerk/nextjs';

export default function SignUpPage() {
  return (
    <div className="auth-page-container">
      <SignUp />
    </div>
  );
}
```
