---
tags: [ui, page, admin, security, authorization, frontend]
---

# Page: Admin Gateway Controller

This page acts as the authorization gateway and container for the admin control center, located at `src/app/admin/page.tsx` and mapped to `/admin`.

- **File Link**: [page.tsx](file:///d:/02_CODE/04_TEST/Routine/src/app/admin/page.tsx)
- **Backlinks**: [[index]], [[lib_auth]], [[component_admin_panel]]

---

## 1. Authentication & Role Validation

The page uses a client-side gatekeeper mechanism:
1. When mounted, `checkAdminAccess` triggers a profile fetch from `GET /api/user`.
2. Evaluates `userData.role`. If the role is `"admin"`, the dashboard is unlocked.
3. If the role is not `"admin"` (or the server responds with a non-200 authentication code), the interface triggers a timed redirect:
   - Sets state to `denied`.
   - Displays a custom warning screen with a shrinking animation progress bar (2 seconds duration).
   - Uses Next.js `useRouter().push('/')` to bounce the user back to the primary dashboard.

---

## 2. Source Code

Here is the complete implementation of `src/app/admin/page.tsx`:

```tsx
'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { UserButton } from '@clerk/nextjs';
import { Loader2, ShieldOff } from 'lucide-react';
import AdminPanel from '@/components/AdminPanel';

export default function AdminPage() {
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [authState, setAuthState] = useState<'loading' | 'denied' | 'authorized'>('loading');

  useEffect(() => {
    checkAdminAccess();
  }, []);

  const checkAdminAccess = async () => {
    try {
      const res = await fetch('/api/user');
      if (res.ok) {
        const userData = await res.json();
        if (userData.role === 'admin') {
          setUser(userData);
          setAuthState('authorized');
        } else {
          setAuthState('denied');
          setTimeout(() => {
            router.push('/');
          }, 2000);
        }
      } else {
        setAuthState('denied');
        setTimeout(() => {
          router.push('/');
        }, 2000);
      }
    } catch (err) {
      console.error('Error checking admin access:', err);
      setAuthState('denied');
      setTimeout(() => {
        router.push('/');
      }, 2000);
    }
  };

  if (authState === 'loading') {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', width: '100vw', alignItems: 'center', justifyContent: 'center', background: 'var(--paper-white)' }}>
        <div className="wobbly-box" style={{ padding: '2.5rem', textAlign: 'center', background: '#ffffff' }}>
          <Loader2 className="animate-spin mb-4" size={40} style={{ color: 'var(--ink-charcoal)', display: 'inline-block' }} />
          <h2 className="sketchy-heading" style={{ fontSize: '1.4rem' }}>🛡️ Verifying Admin Access...</h2>
          <p className="handwritten" style={{ fontSize: '1.1rem', marginTop: '0.5rem', color: '#718096' }}>Checking your credentials.</p>
        </div>
      </div>
    );
  }

  if (authState === 'denied') {
    return (
      <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', width: '100vw', alignItems: 'center', justifyContent: 'center', background: 'var(--paper-white)' }}>
        <div className="wobbly-box" style={{ padding: '2.5rem', textAlign: 'center', background: '#ffffff', borderColor: '#c53030' }}>
          <ShieldOff size={48} style={{ color: '#c53030', display: 'inline-block', marginBottom: '1rem' }} />
          <h2 className="sketchy-heading" style={{ fontSize: '1.6rem', color: '#c53030' }}>🚫 Access Denied</h2>
          <p className="handwritten" style={{ fontSize: '1.1rem', marginTop: '0.5rem', color: '#718096' }}>
            You don&apos;t have admin privileges. Redirecting to home page...
          </p>
          <div style={{ marginTop: '1rem', height: '3px', background: 'linear-gradient(90deg, transparent, #c53030, transparent)', borderRadius: '2px' }}>
            <div style={{
              height: '100%',
              background: '#c53030',
              borderRadius: '2px',
              animation: 'shrinkBar 2s linear forwards'
            }} />
          </div>
        </div>
        <style jsx>{`
          @keyframes shrinkBar {
            from { width: 100%; }
            to { width: 0%; }
          }
        `}</style>
      </div>
    );
  }

  return (
    <div style={{ padding: '1rem', maxWidth: '1400px', width: '100%', margin: '0 auto' }}>
      <header className="app-header mb-6">
        <div className="header-brand-row">
          <span className="auth-brand handwritten" style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>
            🛡️ Admin Control Center
          </span>
          <div className="header-user-mobile">
            <UserButton
              appearance={{
                elements: {
                  avatarBox: { width: '2.2rem', height: '2.2rem' }
                }
              }}
            />
          </div>
        </div>

        <div className="header-tabs-container">
          <button onClick={() => router.push('/')} className="sketchy-btn">
            📒 Back to Routine
          </button>
        </div>

        <div className="header-user-desktop">
          <UserButton
            appearance={{
              elements: {
                avatarBox: { width: '2.2rem', height: '2.2rem' }
              }
            }}
          />
        </div>
      </header>

      <AdminPanel user={user} />
    </div>
  );
}
```
