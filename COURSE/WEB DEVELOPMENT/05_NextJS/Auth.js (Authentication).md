---
tags:
- nextjs
- auth
- security
---
# Auth.js (Authentication)

## What's the Actual Use?
Auth.js (formerly NextAuth.js) is a complete open-source authentication solution for Next.js. It handles the complex and risky parts of security, allowing users to sign in via OAuth providers (Google, GitHub), magic links, or traditional email/password credentials.

## Real-Life Analogy
Building your own authentication is like building your own bank vault—it's very easy to make a small mistake that lets thieves in. Using Auth.js is like hiring a professional security firm. They provide the armored trucks, the background checks, and the locks, so you can focus on running your business.

## Other Common Use Cases
- Adding "Sign in with Google" or "Sign in with GitHub" to an app
- Managing user sessions across the server and client
- Protecting routes and API endpoints based on user roles

## Documentation & Code
Setup usually involves configuring a handler in your API routes and using hooks to access the session.

```javascript
// app/api/auth/[...nextauth]/route.js (Simplified Example)
import NextAuth from "next-auth";
import GitHubProvider from "next-auth/providers/github";

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    GitHubProvider({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
    }),
  ],
});

// Accessing session in a Server Component
import { auth } from "@/auth";

export default async function ProfilePage() {
  const session = await auth();
  
  if (!session) return <p>Not logged in</p>;
  return <div>Welcome, {session.user.name}</div>;
}
```