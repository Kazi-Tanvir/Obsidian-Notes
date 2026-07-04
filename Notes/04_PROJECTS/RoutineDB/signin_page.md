---
tags: [ui, page, auth, clerk, user, frontend]
---

# Page: Sign In

This page wraps the Clerk Authentication Sign-In component, located at `src/app/sign-in/[[...sign-in]]/page.tsx` and mapped to `/sign-in`.

- **File Link**: [page.tsx](file:///d:/02_CODE/04_TEST/Routine/src/app/sign-in/[[...sign-in]]/page.tsx)
- **Backlinks**: [[index]], [[layout]], [[proxy_middleware]]

---

## Technical Details

The page uses standard Clerk SDK routing configurations and wraps the component inside an `.auth-page-container` block to center it horizontally and vertically.

### Source Code

```tsx
import { SignIn } from '@clerk/nextjs';

export default function SignInPage() {
  return (
    <div className="auth-page-container">
      <SignIn />
    </div>
  );
}
```
