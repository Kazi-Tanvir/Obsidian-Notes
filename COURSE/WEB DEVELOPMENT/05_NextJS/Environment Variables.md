---
tags:
- nextjs
- config
- security
---
# Environment Variables

## What's the Actual Use?
Environment variables allow you to store sensitive information (like API keys, database passwords, and secrets) separately from your code. This prevents private data from being leaked when you share your code or push it to GitHub.

## Real-Life Analogy
Environment variables are like a safe in your office. Your instruction manual (the code) might say "use the key from the safe to open the door," but the manual doesn't actually contain the key itself. If someone steals the manual, they still don't have the key.

## Other Common Use Cases
- Storing database connection strings (`DATABASE_URL`)
- Storing 3rd party API keys (Stripe, OpenAI, Google Maps)
- Switching between "Development" and "Production" API endpoints

## Documentation & Code
Create a `.env.local` file in your root directory. Next.js automatically loads these.

```text
# .env.local
DATABASE_URL=mongodb+srv://user:pass@cluster.mongodb.net/
STRIPE_SECRET_KEY=sk_test_51Mz...
# Prefix with NEXT_PUBLIC_ to make it accessible in the browser
NEXT_PUBLIC_ANALYTICS_ID=UA-12345-6
```

```javascript
// Using variables in a Server Component or API Route
export async function GET() {
  const apiKey = process.env.STRIPE_SECRET_KEY; // Securely accessed on server
  console.log(apiKey);
}

// Using variables in a Client Component (requires NEXT_PUBLIC_ prefix)
"use client";
export function Analytics() {
  return <div>Tracking ID: {process.env.NEXT_PUBLIC_ANALYTICS_ID}</div>;
}
```