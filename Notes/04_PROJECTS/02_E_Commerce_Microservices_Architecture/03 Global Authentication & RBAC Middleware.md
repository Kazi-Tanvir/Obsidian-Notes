---
tags:
  - architecture
  - security
  - authentication
  - clerk
  - jwt
  - middleware
  - rbac
---

## 🧠 Core Concept: Decentralized Zero-Trust Auth

In a monolithic app, user sessions are usually stored in the database or server memory (stateful authentication). If a user makes a request, the server just checks its own memory to see if they are logged in.

In a microservices architecture, the `product-services` and `order-services` are completely isolated. They do not share memory. Therefore, we must use **Stateless Authentication via JWTs (JSON Web Tokens)**.

**The Zero-Trust Flow:**

1. Next.js does not verify permissions. It simply passes the user's Token to the backend.
2. The backend server _never_ trusts the client. It intercepts the request, cracks open the token, and cryptographically verifies its signature using Clerk's public keys before allowing the code to proceed.

---

## 🔐 1. The Clerk Strategy

Instead of building custom password hashing and JWT issuance logic (which is a massive security liability), the architecture outsources identity management to **Clerk**.

- **Frontend:** Clerk provides the Next.js `<SignIn />` and `<SignUp />` components, handling MFA, social logins, and session management out of the box.
- **Token Issuance:** When a user logs in, Clerk generates a cryptographically signed JWT containing their user ID and metadata.
- **The `Authorization` Header:** For every protected API call the Next.js client makes to your Express/Fastify servers, it attaches this token as a Bearer token: `Headers: { Authorization: "Bearer eyJhbGci..." }`

---

## 👑 2. Role-Based Access Control (RBAC) Setup

Not all authenticated users are equal. A regular customer can view products, but only an **Admin** can create or delete them.

**Using Clerk's Public Metadata:** Clerk allows us to attach custom JSON data to a user object. To create our admin, we go into the Clerk Dashboard and manually attach this to our specific user profile:

JSON

```json
{
  "role": "admin"
}
```

Because this is attached to the user in Clerk, it gets baked directly into the JWT payload. When the backend opens the token, it instantly knows if the user is an admin without needing to query a database.

---

## 🛡️ 3. The Custom Middleware Implementation

Since our backend servers (Express/Fastify) do not have Next.js magic, we must write a custom middleware function to manually verify the Clerk token.

### The Express Middleware (`authMiddleware.ts`)

This function acts as a bouncer at the door of our API. It sits _between_ the incoming request and the actual controller logic.

TypeScript

```ts
// apps/product-services/src/middleware/authMiddleware.ts
import { Request, Response, NextFunction } from "express";
import { verifyToken } from "@clerk/backend"; // Clerk's Node.js SDK

export const requireAdmin = async (req: Request, res: Response, next: NextFunction) => {
  try {
    // 1. Extract the token from the request headers
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return res.status(401).json({ message: "Unauthorized: No token provided" });
    }
    const token = authHeader.split(" ")[1];

    // 2. Cryptographically verify the token using your Clerk Secret Key
    const verifiedToken = await verifyToken(token, {
      secretKey: process.env.CLERK_SECRET_KEY,
    });

    // 3. Check for the Admin Role in the public metadata
    const role = verifiedToken.metadata?.role;
    if (role !== "admin") {
      return res.status(403).json({ message: "Forbidden: Admin access required" });
    }

    // 4. Attach the userId to the request for the controller to use
    req.userId = verifiedToken.sub;

    // 5. Allow the request to proceed to the controller!
    next(); 
    
  } catch (error) {
    return res.status(401).json({ message: "Unauthorized: Invalid token" });
  }
};
```

---

## 🚦 4. Protecting the Routes

With the middleware built, we apply it _only_ to the routes that modify the database. Reading data remains completely public.

TypeScript

```ts
// apps/product-services/src/routes/product.route.ts
import { Router } from "express";
import { getProducts, createProduct } from "../controllers/product.controller";
import { requireAdmin } from "../middleware/authMiddleware";

const router = Router();

// PUBLIC ROUTE: Anyone can view the catalog (No middleware)
router.get("/", getProducts);

// PROTECTED ROUTE: Only admins can add inventory (Middleware intercepts)
router.post("/", requireAdmin, createProduct);

export default router;
```

**The Security Guarantee:** If a malicious user opens Postman and tries to send a `POST` request to create a product, the `requireAdmin` middleware will instantly reject them with a `401 Unauthorized` or `403 Forbidden` before the Prisma database code even knows a request happened.