tags:

- frontend

- nextjs

- auth

- security

- oauth

- session-management

- mfa

- backend date: 2026-08-29

# Day 29 - Next.js Authentication Internals: Session Management, Auth.js / NextAuth, OAuth PKCE & Multi-Factor Auth

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Modern Next.js Authentication Landscape

Authentication in Next.js App Router spans both server-side React Server Components (RSC), Edge Middleware, Client Components, and asynchronous Server Actions.

┌─────────────────────────────────────── Next.js App Router Architecture ───────────────────────────────────────┐

│ │

│ \[ Edge Middleware \] ────────► \[ Server Components (RSC) \] ────────► \[ Server Actions / Route Handlers \] │

│ • Edge JWT verification • Universal auth() read • Mutating state with CSRF check │

│ • Fast URL redirect/rewrite • Zero bundle size on client • Set-Cookie chunked encryption │

│ │

└───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

#### Authentication Strategy Comparison:

- **Stateless JWT Sessions**: Compact encrypted/signed tokens stored in cookies. Eliminates database lookups on every page request, ideal for Edge Middleware. Drawback: Immediate server-side revocation requires distributed Redis blacklists.

- **Database-Backed Sessions**: Session tokens map to database rows (Session table). Supports instant revocation of compromised devices. Drawback: Requires database roundtrips on every authenticated render.

- **Hybrid Strategy**: Short-lived JWTs (15 min) for fast edge validation + Database Refresh Tokens (7 days) for session revocation and privilege checks.

### 2. Auth.js (NextAuth.js v5) Universal Architecture

Auth.js v5 introduces the **Universal auth() helper**, which functions consistently across all App Router boundaries:

// auth.ts - Central Configuration

import NextAuth from \'next-auth\';

import GitHub from \'next-auth/providers/github\';

import Credentials from \'next-auth/providers/credentials\';

import { PrismaAdapter } from \'@auth/prisma-adapter\';

import { prisma } from \'@/lib/prisma\';

import { z } from \'zod\';

export const { handlers, signIn, signOut, auth } = NextAuth({

adapter: PrismaAdapter(prisma),

session: { strategy: \'jwt\', maxAge: 30 \* 24 \* 60 \* 60 },

providers: \[

GitHub({

clientId: process.env.AUTH_GITHUB_ID,

clientSecret: process.env.AUTH_GITHUB_SECRET,

}),

Credentials({

async authorize(credentials) {

const parsed = z.object({ email: z.string().email(), password: z.string().min(8) }).safeParse(credentials);

if (!parsed.success) return null;

const user = await prisma.user.findUnique({ where: { email: parsed.data.email } });

if (!user \|\| !user.passwordHash) return null;

const isValid = await verifyPassword(parsed.data.password, user.passwordHash);

return isValid ? user : null;

},

}),

\],

callbacks: {

async jwt({ token, user }) {

if (user) {

token.id = user.id;

token.role = user.role;

}

return token;

},

async session({ session, token }) {

if (session.user) {

session.user.id = token.id as string;

session.user.role = token.role as string;

}

return session;

},

},

});

#### Usage Across Next.js App Router:

// 1. In Server Components (app/dashboard/page.tsx)

import { auth } from \'@/auth\';

import { redirect } from \'next/navigation\';

export default async function DashboardPage() {

const session = await auth();

if (!session) redirect(\'/api/auth/signin\');

return \<h1\>Welcome back, {session.user.name} ({session.user.role})\</h1\>;

}

// 2. In Server Actions (app/actions.ts)

\'use server\';

import { auth } from \'@/auth\';

export async function deleteProjectAction(projectId: string) {

const session = await auth();

if (!session \|\| session.user.role !== \'ADMIN\') {

throw new Error(\'Unauthorized\');

}

await prisma.project.delete({ where: { id: projectId } });

}

### 3. Secure Cookie Jar & Hardening Flags

Session cookies must be protected against tampering and cross-origin leaks:

- **HttpOnly**: Blocks client-side JavaScript from accessing session tokens via document.cookie (mitigates XSS token theft).

- **Secure**: Enforces transmission only over encrypted HTTPS channels.

- **SameSite=Lax / SameSite=Strict**: Protects against CSRF attacks.

- **\_\_Host- and \_\_Secure- Prefixes**: Browser cookie prefixes that enforce strict origin, path, and secure HTTPS requirements.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Next.js Authentication Reference:

  ------------------------------------------------------------------------------------------------------------------------------------------
  **Boundary**           **Method**                                      **Runtime**          **Performance**
  ---------------------- ----------------------------------------------- -------------------- ----------------------------------------------
  **Server Component**   const session = await auth()                    Node.js / Edge       Zero client bundle, runs on server

  **Server Action**      const session = await auth()                    Node.js Serverless   Validates caller identity before DB mutation

  **Route Handler**      export const { GET, POST } = handlers           Node.js / Edge       Manages OAuth redirects and API callbacks

  **Edge Middleware**    export { auth as middleware } from \'@/auth\'   Edge Runtime (V8)    Fast sub-5ms path protection before render

  **Client Component**   useSession() via \<SessionProvider\>            Browser DOM          Client-side reactive UI state
  ------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Enterprise Multi-Tenant SSO & Session Invalidation Architecture

Design a secure Enterprise authentication system in Next.js App Router for a B2B SaaS platform:

**Requirements**:

1.  Detail the integration of:

    - **Enterprise SAML / OIDC SSO** (Okta, Azure AD) with dynamic tenant discovery based on email domain (user@enterprise.com).

    - **Time-Based One-Time Password (TOTP MFA)** verification step (RFC 6238) using QR code setup and secret encryption.

    - **Instant Global Device Revocation**: Detail how stateless JWT sessions can be revoked immediately across all active browser sessions when a user clicks \"Log out of all devices\".

2.  Architect cookie chunking strategies for handling large JWT payloads that exceed browser 4096-byte cookie limits.

### Problem 2: End-to-End Code Implementation Challenge

Build a complete **Next.js TOTP MFA Verification Route & Server Action** in TypeScript:

**Requirements**:

1.  Implement a Server Action setupMfaAction():

    - Generates a cryptographically random 32-character base32 secret.

    - Computes an otpauth://totp/MyApp:user@email.com?secret=\... URI.

    - Encrypts and saves the unverified secret to the database.

2.  Implement a Server Action verifyAndEnableMfaAction(totpToken: string):

    - Verifies the 6-digit TOTP token against current time window (±1 step / 30s) using Web Crypto API.

    - Marks MFA as enabled on the user record.

    - Issues an updated secure session cookie containing mfa_verified: true.

3.  Include test cases validating:

    - Rejection of expired TOTP codes.

    - Acceptance of valid TOTP codes within clock drift tolerance.

    - Authorization guard blocking access to /dashboard if mfa_verified !== true.
