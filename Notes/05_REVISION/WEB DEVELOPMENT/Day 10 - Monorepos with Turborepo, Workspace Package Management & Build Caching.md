tags:

- devops

- monorepo

- turborepo

- pnpm

- build-system

- architecture date: 2026-08-10

# Day 10 - Monorepos with Turborepo, Workspace Package Management & Build Caching

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Monorepo Architecture & pnpm Workspaces

A **Monorepo** consolidates multiple applications (e.g. Next.js Web App, Next.js Admin, Express API) and shared libraries (e.g. UI component library, database schema, TypeScript configs) into a single Git repository.

#### Why pnpm Workspaces?

- **Hard Links & Symlinks**: pnpm uses a global content-addressable store and symlinks node_modules, saving gigabytes of disk space and preventing duplicate dependencies.

- **Workspace Protocol (workspace:\*)**: Ensures internal packages (@repo/ui, \@repo/database) reference local workspace source code directly without npm registry publishes.

\# pnpm-workspace.yaml

packages:

\- \'apps/\*\'

\- \'packages/\*\'

### 2. Turborepo Task Pipeline (turbo.json)

Turborepo is a high-performance build system for JavaScript/TypeScript monorepos. It creates an internal **Directed Acyclic Graph (DAG)** of tasks and caches outputs (build artifacts, dist folders) based on source file hashes.

// turbo.json

{

\"\$schema\": \"https://turbo.build/schema.json\",

\"globalEnv\": \[\"NODE_ENV\", \"DATABASE_URL\"\],

\"tasks\": {

\"build\": {

\"dependsOn\": \[\"\^build\"\], // Build dependencies in packages/ before building apps/

\"inputs\": \[\"\$TURBO_DEFAULT\$\", \".env\*\"\],

\"outputs\": \[\".next/\*\*\", \"!-next/cache/\*\*\", \"dist/\*\*\"\]

},

\"lint\": {

\"dependsOn\": \[\]

},

\"dev\": {

\"cache\": false, // Disable caching for persistent dev servers

\"persistent\": true

}

}

}

### 3. Remote Caching & CI/CD Optimization

Turborepo calculates a hash for each task input (source code + dependencies + env variables + turbo.json).

- **Local Cache**: Saved in node_modules/.cache/turbo. If files haven\'t changed, turbo run build completes in milliseconds (**FULL TURBO**).

- **Remote Cache**: Shares build artifacts across team members and CI/CD pipelines (Vercel / S3 custom cache server).

- **Pruning Workspaces (turbo prune)**: Extracts a scoped slice of the monorepo for Docker container builds, minimizing Docker context size.

## SECTION 2: DOCUMENTATION CHEAT SHEET

  -----------------------------------------------------------------------------------------------------------------------
  **CLI / Configuration**   **Command / File**                   **Purpose**
  ------------------------- ------------------------------------ --------------------------------------------------------
  **pnpm-workspace.yaml**   Root configuration file              Defines workspace directories (apps/\*, packages/\*)

  **Workspace Protocol**    \"@repo/ui\": \"workspace:\*\"       Adds internal package dependency in package.json

  **Run Monorepo Task**     pnpm turbo run build                 Executes pipeline graph concurrently across workspaces

  **Filter Execution**      pnpm turbo run build \--filter=web   Runs build target strictly for web app

  **Docker Prune**          npx turbo prune \--scope=web         Creates isolated sparse build tree in out/
  -----------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Enterprise Monorepo Architecture)

Design a production-grade full-stack Turborepo monorepo structure for an enterprise SaaS platform.

**Requirements**:

1.  Define the folder structure featuring 3 apps (apps/web, apps/admin, apps/api) and 4 shared packages (packages/ui, packages/db, packages/tsconfig, packages/eslint-config).

2.  Write the complete turbo.json task dependency pipeline for build, test, lint, and type-check.

3.  Explain how to prevent the \@repo/db package (Prisma schema) from rebuilding when only a CSS file in \@repo/ui changes.

### Problem 2: End-to-End Code Implementation Challenge

Set up a shared database package \@repo/db in a pnpm + Turborepo monorepo.

**Requirements**:

1.  Create packages/db/package.json with workspace protocol exports (exports: { \".\": \"./src/index.ts\" }).

2.  Implement packages/db/src/index.ts exporting a singleton Prisma Client instance (prisma).

3.  Configure apps/web/package.json to depend on \"@repo/db\": \"workspace:\*\" and import prisma directly inside a Next.js Server Component page (apps/web/app/users/page.tsx).

4.  Ensure pnpm turbo run build executes prisma generate in \@repo/db before building apps/web.
