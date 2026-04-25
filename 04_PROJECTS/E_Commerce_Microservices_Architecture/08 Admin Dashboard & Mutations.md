---
tags:
  - architecture
  - admin
  - nextjs
  - mutations
  - react-query
  - cloudinary
---

## 🧠 Core Concept: Internal Tooling & Secure Mutations

While the client-facing store focuses on _Reading_ data (GET requests), the Admin Dashboard focuses heavily on _Mutating_ data (POST, PUT, DELETE).

Because this interface controls your business, it requires strict security at the frontend routing layer and efficient handling of complex data like image uploads.

**The Enterprise Benefit:**

- **Decoupled Asset Management:** By offloading image storage to a CDN (Cloudinary) instead of stuffing image blobs into your PostgreSQL database, your database remains lightning fast and cheap to host.
- **Optimistic UI Updates:** Using TanStack Query's mutation cache, the dashboard feels instantaneous when an admin adds a product, even if the backend takes a full second to respond.

---

## 🛡️ 1. Frontend Route Protection

It is not enough that your backend Express API is protected by the `requireAdmin` middleware. If a regular user navigates to `yourstore.com/admin`, they shouldn't even see the UI.

In Next.js (App Router), we protect entire route segments using Clerk.

TypeScript

```ts
// apps/client/src/app/admin/layout.tsx
import { auth } from "@clerk/nextjs/server";
import { redirect } from "next/navigation";

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  // 1. Grab the user's session token and metadata securely on the server
  const { sessionClaims } = auth();

  // 2. Check the RBAC metadata we set up in Part 3
  if (sessionClaims?.metadata?.role !== "admin") {
    // 3. Immediately kick unauthorized users back to the homepage
    redirect("/"); 
  }

  // 4. If they are an admin, render the dashboard
  return (
    <div className="admin-layout">
      <AdminSidebar />
      <main>{children}</main>
    </div>
  );
}
```

---

## 🖼️ 2. Media Management (Cloudinary)

Databases are meant for structured text, not 5MB JPEG files. When an admin creates a new Product, the image upload happens in two distinct steps.

**The Cloudinary Flow:**

1. The Next.js frontend uses `next-cloudinary` (an official widget) to pop open an upload modal.
2. The image goes straight from the admin's browser to Cloudinary's servers (bypassing your backend entirely, saving bandwidth).
3. Cloudinary returns a secure URL (e.g., `https://res.cloudinary.com/demo/image/...`).
4. We take that URL and send _it_ to our Express Backend to be saved in the Prisma database.

TypeScript

```ts
// Example Cloudinary Widget Implementation
import { CldUploadWidget } from 'next-cloudinary';

<CldUploadWidget 
  uploadPreset="ecommerce_admin" // Configured in Cloudinary dashboard
  onSuccess={(result) => {
    // result.info.secure_url is what we will save to our PostgreSQL DB!
    setImageUrl(result.info.secure_url);
  }}
>
  {({ open }) => <button onClick={() => open()}>Upload Product Image</button>}
</CldUploadWidget>
```

---

## ⚡ 3. React Query Mutations & Cache Invalidation

When an admin submits the "Add Product" form, we use TanStack Query's `useMutation` instead of `useQuery`.

The most powerful feature here is **Cache Invalidation**. When the mutation succeeds, we tell React Query: _"Hey, the data just changed. Throw away your cached list of products and fetch a fresh one from the server immediately."_

TypeScript

```ts
// apps/client/src/hooks/useCreateProduct.ts
import { useMutation, useQueryClient } from "@tanstack/react-query";
import axios from "axios";
import { useAuth } from "@clerk/nextjs";

export const useCreateProduct = () => {
  const queryClient = useQueryClient();
  const { getToken } = useAuth();

  return useMutation({
    mutationFn: async (newProductData) => {
      const token = await getToken();
      return axios.post(
        `${process.env.NEXT_PUBLIC_PRODUCT_SERVICE_URL}/products`, 
        newProductData,
        { headers: { Authorization: `Bearer ${token}` } }
      );
    },
    onSuccess: () => {
      // THE MAGIC: This forces the Admin table UI to re-render with the new item!
      queryClient.invalidateQueries({ queryKey: ["products"] });
      alert("Product created successfully!");
    },
  });
};
```

---

## 📊 4. Data Aggregation for Dashboards

To build the charts (like "Total Sales per Month"), the frontend shouldn't download 10,000 orders and do the math. The Fastify Order Service should do the heavy lifting using **Mongoose Aggregations**.

TypeScript

```ts
// apps/order-services/src/routes/analytics.ts
// Example: Getting total revenue by month
app.get("/revenue-stats", async (request, reply) => {
  const stats = await Order.aggregate([
    { $match: { status: "success" } }, // Only count successful orders
    { 
      $group: { 
        _id: { $month: "$createdAt" }, // Group by the month they were created
        totalRevenue: { $sum: "$amount" } // Add up all the amounts
      } 
    },
    { $sort: { _id: 1 } } // Sort by month (Jan -> Dec)
  ]);
  
  reply.send(stats);
});
```

The Next.js frontend then takes this clean `[{ month: 1, totalRevenue: 5000 }, ...]` array and passes it directly into a charting library like **Recharts**.