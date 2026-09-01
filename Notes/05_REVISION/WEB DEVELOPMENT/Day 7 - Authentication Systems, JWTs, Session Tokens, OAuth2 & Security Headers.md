tags:

- backend

- auth

- security

- jwt

- oauth2

- express

- nextjs date: 2026-08-07

# Day 7 - Authentication Systems, JWTs, Session Tokens, OAuth2 & Security Headers

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Stateful Sessions vs JSON Web Tokens (JWT)

Choosing an authentication architecture impacts system statefulness and horizontal scalability.

- **Stateful Session Authentication**:

  - Server generates a random Session ID stored in a server-side cache (Redis / Database).

  - Client stores Session ID in an HttpOnly cookie.

  - *Advantage*: Instant session revocation capability.

  - *Disadvantage*: Requires database lookups per request.

- **Stateless JWT Authentication**:

  - Server signs a payload using a secret key (HS256) or private key (RS256).

  - JWT contains Header, Payload, and Cryptographic Signature (base64Url(Header).base64Url(Payload).Signature).

  - *Advantage*: No database lookup required for authentication verification.

  - *Disadvantage*: Cannot revoke tokens prior to expiration unless a token blacklist/whitelist is maintained in Redis.

### 2. Attack Vectors & Secure Token Storage Strategy

Storing tokens in browser storage determines vulnerability to attack vectors:

- **XSS (Cross-Site Scripting)**: Storing JWTs in localStorage or sessionStorage exposes them to malicious scripts (window.localStorage).

- **CSRF (Cross-Site Request Forgery)**: Automatically sending cookies on cross-origin requests.

#### Production Dual-Token Security Pattern:

1.  **Short-Lived Access Token (15 mins)**: Kept in **In-Memory JavaScript State** (React Context/Zustand). Sent via Authorization: Bearer \<JWT\> header.

2.  **Long-Lived Refresh Token (7 days)**: Stored in an **HttpOnly, Secure, SameSite=Strict Cookie**.

3.  **Refresh Token Rotation**: Each refresh request invalidates the previous refresh token and issues a new pair. If a revoked refresh token is reused, all tokens in the user\'s family tree are immediately revoked (replay attack detection).

// Express Production Secure Auth Handler with Token Rotation

import { Request, Response } from \'express\';

import jwt from \'jsonwebtoken\';

const ACCESS_SECRET = process.env.ACCESS_TOKEN_SECRET!;

const REFRESH_SECRET = process.env.REFRESH_TOKEN_SECRET!;

export async function handleRefreshToken(req: Request, res: Response) {

const refreshToken = req.cookies?.refreshToken;

if (!refreshToken) return res.status(401).json({ error: \"Unauthorized\" });

try {

const payload = jwt.verify(refreshToken, REFRESH_SECRET) as { userId: string };

// Generate new Access + Refresh Token Pair (Rotation)

const newAccessToken = jwt.sign({ userId: payload.userId }, ACCESS_SECRET, { expiresIn: \'15m\' });

const newRefreshToken = jwt.sign({ userId: payload.userId }, REFRESH_SECRET, { expiresIn: \'7d\' });

// Set HttpOnly, Secure Cookie

res.cookie(\'refreshToken\', newRefreshToken, {

httpOnly: true,

secure: process.env.NODE_ENV === \'production\',

sameSite: \'strict\',

maxAge: 7 \* 24 \* 60 \* 60 \* 1000

});

return res.json({ accessToken: newAccessToken });

} catch (err) {

res.clearCookie(\'refreshToken\');

return res.status(403).json({ error: \"Invalid refresh token\" });

}

}

### 3. OAuth 2.0 & OpenID Connect (OIDC) with PKCE

OAuth 2.0 is an authorization framework allowing third-party applications to access user resources without exposing credentials.

#### Authorization Code Flow with PKCE (Proof Key for Code Exchange):

1.  **Client** generates code_verifier and computes code_challenge = Base64URL(SHA256(code_verifier)).

2.  **Client** redirects user to OAuth Provider with code_challenge.

3.  **Provider** redirects back with an authorization code.

4.  **Client** swaps code + original code_verifier for tokens at the token endpoint.

5.  **Provider** verifies hash before issuing tokens (prevents authorization code interception attacks).

## SECTION 2: DOCUMENTATION CHEAT SHEET

  -----------------------------------------------------------------------------------------------------------------------------------------------
  **Header / Config**             **Value / Syntax**                              **Purpose**
  ------------------------------- ----------------------------------------------- ---------------------------------------------------------------
  **HttpOnly Cookie**             res.cookie(\'name\', val, { httpOnly: true })   Prevents JavaScript (document.cookie) access (XSS mitigation)

  **SameSite Cookie**             sameSite: \'strict\' or \'lax\'                 Prevents cross-site cookie transmission (CSRF mitigation)

  **Strict-Transport-Security**   max-age=31536000; includeSubDomains             Forces HTTPS communication (HSTS)

  **Content-Security-Policy**     default-src \'self\'                            Restricts sources for scripts, styles, and frames

  **JWT Verification**            jwt.verify(token, secret)                       Verifies token signature and expiration
  -----------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Multi-Tenant OAuth2 & Session Revocation Architecture)

Design an authentication subsystem for an enterprise multi-tenant application supporting **OAuth2 SSO (Google/GitHub)** and **Instant Device Session Invalidation**.

**Requirements**:

1.  Diagram the token exchange flow between Next.js frontend, API Gateway, and OAuth Provider.

2.  Design a Redis-backed session revocation schema to support \"Log out of all devices\" without forcing SQL DB queries on every authenticated request.

3.  Architect an RBAC (Role-Based Access Control) claims model embedded within JWT payloads.

### Problem 2: End-to-End Code Implementation Challenge

Build a complete **Express.js Auth Middleware Guard & Token Rotation Router**.

**Requirements**:

1.  Implement POST /api/v1/auth/login, POST /api/v1/auth/refresh, and POST /api/v1/auth/logout endpoints.

2.  Build an authenticateJWT middleware that verifies Authorization: Bearer \<token\>, extracts claims, and populates req.user.

3.  Implement Refresh Token Rotation with automatic reuse detection (revoking all user sessions if a compromised refresh token is reused).

4.  Provide unit tests covering invalid token, expired token, and successful rotation scenarios.
