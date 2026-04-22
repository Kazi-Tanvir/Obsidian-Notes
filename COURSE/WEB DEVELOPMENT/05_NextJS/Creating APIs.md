---
tags:
- nextjs
- api
- backend
---
# Creating APIs

## What's the Actual Use?
Next.js allows you to build a full backend within the same project using Route Handlers. You can create API endpoints (like `/api/users`) that handle GET, POST, PUT, and DELETE requests, effectively replacing the need for a separate Express.js server for many projects.

## Real-Life Analogy
If your website is a restaurant dining room, the API is the kitchen window. The customer (frontend) sends an order (request) through the window, and the chef (Next.js Route Handler) processes the food (data) and sends it back out as a finished dish (JSON response).

## Other Common Use Cases
- Handling form submissions and saving them to a database
- Creating webhooks for payment processors like Stripe
- Building a proxy to fetch data from a 3rd party API while hiding your secret keys

## Documentation & Code
Route Handlers are defined in `route.js` files.

```javascript
// app/api/hello/route.js
import { NextResponse } from 'next/server';

// Handle GET requests to /api/hello
export async function GET() {
  return NextResponse.json({ message: "Hello from the Server!" });
}

// Handle POST requests to /api/hello
export async function POST(request) {
  const data = await request.json(); // Parse incoming JSON body
  
  return NextResponse.json({ 
    received: data,
    status: "Success" 
  }, { status: 201 });
}
```