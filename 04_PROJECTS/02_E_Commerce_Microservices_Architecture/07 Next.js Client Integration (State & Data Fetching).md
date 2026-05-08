---
tags:
  - architecture
  - frontend
  - nextjs
  - react-query
  - zustand
  - state-management
---

## 🧠 Core Concept: The API Gateway & State Illusion

To the end user, your application feels like a single website. In reality, the Next.js frontend is acting as a router, juggling requests across entirely different backend ports (Products on `:8000`, Orders on `:8001`, Payments on `:8002`).

**The Enterprise Benefit:**

- **Decoupled UI:** The frontend doesn't care _how_ the products are stored in Postgres or _how_ Kafka handles events. It only cares about the JSON it receives.
- **Optimized Client State:** By using modern tools like React Query and Zustand, the client handles caching and local state (like the shopping cart) without aggressively spamming the backend servers.

---

## 🌐 1. Environment Variable Management

Because the Next.js app needs to talk to multiple microservices, its `.env.local` file acts as the directory. Notice the `NEXT_PUBLIC_` prefix, which exposes these URLs to the browser.

Code snippet

```python
# apps/client/.env.local
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
NEXT_PUBLIC_PRODUCT_SERVICE_URL=http://localhost:8000
NEXT_PUBLIC_ORDER_SERVICE_URL=http://localhost:8001
NEXT_PUBLIC_PAYMENT_SERVICE_URL=http://localhost:8002
```

---

## 🎣 2. Data Fetching with TanStack (React) Query

In modern React, using `useEffect` to fetch data is considered an anti-pattern due to race conditions and lack of caching. Instead, the architecture utilizes **React Query**.

### Why React Query?

If a user navigates from the Homepage to a Product page and back to the Homepage, React Query pulls the products from its local cache instantly instead of asking the `product-services` backend for the same data twice.

TypeScript

```ts
// apps/client/src/hooks/useProducts.ts
import { useQuery } from "@tanstack/react-query";
import axios from "axios";

export const useProducts = (categorySlug?: string) => {
  return useQuery({
    // The queryKey tells React Query when to re-fetch (e.g., if the category changes)
    queryKey: ["products", categorySlug],
    queryFn: async () => {
      const url = categorySlug 
        ? `${process.env.NEXT_PUBLIC_PRODUCT_SERVICE_URL}/products?category=${categorySlug}`
        : `${process.env.NEXT_PUBLIC_PRODUCT_SERVICE_URL}/products`;
        
      const response = await axios.get(url);
      return response.data;
    },
    staleTime: 1000 * 60 * 5, // Cache the data for 5 minutes
  });
};
```

---

## 🛒 3. Global Cart State with Zustand

The Shopping Cart is a complex piece of state. It needs to be accessible from the Navbar, the Product Page, and the Checkout Page. It also needs to survive page refreshes.

Instead of Redux (which requires massive boilerplate) or React Context (which causes unnecessary re-renders), the tutorial uses **Zustand**.

### The Cart Store

Zustand allows you to create a global hook that persists directly to the browser's `localStorage`.

TypeScript

```ts
// apps/client/src/store/useCartStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface CartItem {
  id: number;
  name: string;
  price: number;
  quantity: number;
  image: string;
}

interface CartState {
  items: CartItem[];
  addToCart: (item: CartItem) => void;
  removeFromCart: (id: number) => void;
  clearCart: () => void;
  getTotalPrice: () => number;
}

export const useCartStore = create<CartState>()(
  // The 'persist' middleware automatically saves the cart to Local Storage
  persist(
    (set, get) => ({
      items: [],
      addToCart: (newItem) => set((state) => {
        const existingItem = state.items.find(item => item.id === newItem.id);
        if (existingItem) {
          // Increase quantity if it already exists
          return {
            items: state.items.map(item => 
              item.id === newItem.id ? { ...item, quantity: item.quantity + 1 } : item
            )
          };
        }
        return { items: [...state.items, { ...newItem, quantity: 1 }] };
      }),
      removeFromCart: (id) => set((state) => ({
        items: state.items.filter(item => item.id !== id)
      })),
      clearCart: () => set({ items: [] }),
      getTotalPrice: () => get().items.reduce((total, item) => total + (item.price * item.quantity), 0),
    }),
    { name: 'ecommerce-cart' }
  )
);
```

---

## 💳 4. The Checkout Orchestration

This is where the frontend bridges the gap between the user's local cart, the Order backend, and the Payment backend.

When the user clicks "Pay Now", the Next.js client executes this flow:

TypeScript

```ts
// apps/client/src/components/CheckoutButton.tsx
import { useCartStore } from "../store/useCartStore";
import { useAuth } from "@clerk/nextjs";
import axios from "axios";

export const CheckoutButton = () => {
  const { items, getTotalPrice } = useCartStore();
  const { getToken, userId } = useAuth(); // Clerk Auth

  const handleCheckout = async () => {
    try {
      const token = await getToken();

      // 1. Create the Order in the Fastify Service
      const orderRes = await axios.post(
        `${process.env.NEXT_PUBLIC_ORDER_SERVICE_URL}/orders`,
        {
          userId,
          amount: getTotalPrice(),
          status: "pending",
          products: items,
        },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      // 2. Send the newly created Order ID to the Hono Payment Service
      const paymentRes = await axios.post(
        `${process.env.NEXT_PUBLIC_PAYMENT_SERVICE_URL}/create-checkout-session`,
        {
          orderId: orderRes.data._id,
          products: items,
        },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      // 3. Redirect the user to the Stripe Checkout URL
      window.location.href = paymentRes.data.url;

    } catch (error) {
      console.error("Checkout failed", error);
    }
  };

  return <button onClick={handleCheckout}>Pay Now</button>;
};
```

---