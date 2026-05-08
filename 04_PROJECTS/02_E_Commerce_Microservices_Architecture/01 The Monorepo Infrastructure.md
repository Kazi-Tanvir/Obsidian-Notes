---
tags:
  - architecture
  - microservices
  - monorepo
  - turborepo
---
# [[01 The Monorepo Infrastructure]]


**Up Link:** [[E-Commerce Microservices MoC]] **Time Reference:** `0:00 - 1:30`

## 🧠 Core Concept: Why a Monorepo?

In a standard architecture, a frontend, a product backend, and an order backend would live in three completely separate GitHub repositories. This creates a nightmare for code sharing (e.g., sharing TypeScript interfaces or UI components requires publishing them to NPM).

A **Monorepo** (Monolithic Repository) solves this. It places multiple distinct projects into a single repository, keeping them logically isolated but physically close.

**The Enterprise Benefit:**

- **Single source of truth:** One Git commit can update the frontend and the backend simultaneously.
- **Instant code sharing:** Apps can import local packages without publishing to the internet.
- **Unified tooling:** One ESLint and TypeScript configuration rules them all.
---

## 🏗️ 1. The Directory Structure

The architecture relies on a strict separation of concerns, divided into two main folders:

- `apps/`: Contains the actual deployable servers and clients. (e.g., `order-services`, `product-services`, `client`, `admin`).
    
- `packages/`: Contains internal libraries and shared configuration. These are _never_ deployed on their own; they are imported by the apps. (e.g., `product-db`, `eslint-config`, `typescript-config`).
    

---

## 📦 2. Package Management with `pnpm` Workspaces

We use `pnpm` instead of `npm` or `yarn` because of its advanced workspace features and speed. It uses a hidden `.pnpm-store` to magically symlink dependencies, saving massive amounts of disk space.

**The `pnpm-workspace.yaml` File:** This file sits at the root of the project and tells `pnpm` where the isolated projects live.

YAML

```json
packages:
  - "apps/*"
  - "packages/*"
```

**The Workspace Link Syntax:** To share code, we don't install from the internet. We tell a package's `package.json` to look inside the local workspace using the `workspace:*` command.

JSON

```json
// Inside apps/product-services/package.json
"devDependencies": {
  "@repo/typescript-config": "workspace:*"
}
```

---

## 🛠️ 3. DRY Configuration (Shared Packages)

To adhere to the **DRY (Don't Repeat Yourself)** principle, we extract global settings into the `packages/` folder.

### The TypeScript Config (`@repo/typescript-config`)

Instead of having 5 different `tsconfig.json` files with conflicting strictness rules, we create one master config.

1. Create `packages/typescript-config/base.json`.
2. Inside an app (like `product-services`), extend it:

JSON

```json
// apps/product-services/tsconfig.json
{
  "extends": "@repo/typescript-config/base.json",
  "compilerOptions": {
    "outDir": "dist"
  }
}
```

---

## 🚀 4. Turborepo (The Task Runner)

Running `pnpm dev` in 5 different folders manually is tedious. **Turborepo** acts as the supreme orchestrator for the monorepo.

### The Two Superpowers of Turbo:

1. **Parallel Execution:** It looks at the dependency graph and runs scripts concurrently across all apps.
2. **Aggressive Caching:** If you run `turbo build`, it fingerprints your files. If you run it again without changing anything, it takes `15ms` instead of `2 minutes` because it just pulls the result from the cache.

### The `turbo.json` Pipeline

This file sits at the root and defines the rules of execution.

JSON

```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      // "A package's build command depends on its dependencies building first"
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "dev": {
      // Dev doesn't cache, it runs forever
      "cache": false,
      "persistent": true
    }
  }
}
```

**Execution:** Running `npx turbo dev` at the root will instantly boot up the Next.js frontend, the Express backend, and the Fastify backend all at the exact same time.