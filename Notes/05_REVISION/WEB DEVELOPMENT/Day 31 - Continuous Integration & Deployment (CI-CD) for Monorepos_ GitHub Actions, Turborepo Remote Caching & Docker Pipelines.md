---
tags:
- devops
- ci-cd
- github-actions
- turborepo
- monorepo
- docker
- automation
- cloud
date: 2026-08-31
---

# Day 31 - Continuous Integration & Deployment (CI/CD) for Monorepos: GitHub Actions, Turborepo Remote Caching & Docker Pipelines

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Monorepo CI/CD Problem Space

In a large monorepo with multiple applications (apps/web, apps/api, apps/admin) and shared packages (packages/ui, packages/db, packages/utils), running test and build suites sequentially across all workspaces on every Pull Request leads to 45+ minute CI bottlenecks.

┌────────────────────────────────────── Monorepo CI/CD Optimization ──────────────────────────────────────┐

│ │

│ Naive Approach: Build Everything on Every Commit ──► 45 min build time ($$$ CI compute waste) │

│ │

│ Optimized Approach: │

│ 1. Affected Package Graph Filtering: turbo run build --filter=...[origin/main] │

│ 2. Remote Caching (Turborepo + S3 / Vercel): Replays build outputs if source code hasn't changed │

│ 3. Docker Pruning (turbo prune): Isolates only target app dependencies for minimal container layers │

│ │

│ Result: ──► 3 min build time (93% reduction!) │

│ │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Turborepo Remote Caching Architecture

Turborepo calculates a cryptographic SHA hash of all inputs (source files, dependencies, environment variables) for each task in turbo.json.

- **Cache Hit**: If the input hash matches a previously completed build stored in the Remote Cache (AWS S3, Vercel, or custom HTTP cache), Turborepo downloads the output artifacts (dist/, .next/) and replays the terminal output in milliseconds.

- **Cache Miss**: Executes the build step, uploads the artifacts and logs to the remote bucket, and signs the payload with TURBO_SIGNATURE_KEY.

┌─────────────────┐ 1. Hash Task Inputs (src, env, deps) ┌──────────────────────┐

│ GitHub Actions │ ────────────────────────────────────────────────► │ Turborepo Engine │

│ Runner (CI) │ ◄──────────────────────────────────────────────── │ (Local Hash Match?) │

└────────┬────────┘ 2. Cache HIT: Download artifacts & logs └──────────┬───────────┘

│ │

│ 3. Cache MISS: Build & Upload Artifacts │

└───────────────────────────────────────────────────────────────────────┴──────────┐

▼

┌─────────────────────┐

│ Remote Cache Server │

│ (AWS S3 / Vercel) │

└─────────────────────┘

### 3. Production GitHub Actions Matrix Pipeline for Monorepos

# .github/workflows/ci.yml

name: Monorepo CI/CD Pipeline

on:

push:

branches: [main]

pull_request:

branches: [main]

concurrency:

group: ${{ github.workflow }}-${{ github.ref }}

cancel-in-progress: true

jobs:

validate:

name: Lint, Typecheck & Test

runs-on: ubuntu-latest

env:

TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}

TURBO_TEAM: ${{ vars.TURBO_TEAM }}

steps:

- name: Checkout Codebase

uses: actions/checkout@v4

with:

fetch-depth: 2 # Required for git diff comparisons against previous commit

- name: Setup pnpm Package Manager

uses: pnpm/action-setup@v3

with:

version: 9

- name: Setup Node.js Environment

uses: actions/setup-node@v4

with:

node-version: 20

cache: 'pnpm'

- name: Install Monorepo Dependencies

run: pnpm install --frozen-lockfile

- name: Run Quality Checks on Affected Packages Only

run: pnpm turbo run lint typecheck test --filter=...[origin/main]

### 4. Docker Microservice Containerization with turbo prune

A common mistake is copying the entire monorepo into the Docker build context, invalidating Docker layer caches on unrelated package changes. turbo prune --scope=<app-name> --docker generates an isolated sub-monorepo containing **only** the target app and its transitive workspace dependencies.

# apps/api/Dockerfile

# Phase 1: Prune monorepo to isolate API dependencies

FROM node:20-alpine AS pruner

WORKDIR /app

RUN npm install -g turbo

COPY . .

RUN turbo prune --scope=@repo/api --docker

# Phase 2: Install dependencies with cached pnpm store

FROM node:20-alpine AS installer

WORKDIR /app

RUN npm install -g pnpm

# Copy package.json files from pruner (enables layer caching!)

COPY --from=pruner /app/out/json/ .

COPY --from=pruner /app/out/pnpm-lock.yaml ./pnpm-lock.yaml

RUN pnpm install --frozen-lockfile

# Copy full source code of pruned packages

COPY --from=pruner /app/out/full/ .

# Build application

RUN pnpm turbo run build --filter=@repo/api...

# Phase 3: Production Runner (Ultra-lean 90MB Distroless/Alpine image)

FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production

USER node

COPY --from=installer --chown=node:node /app/apps/api/dist ./dist

COPY --from=installer --chown=node:node /app/node_modules ./node_modules

EXPOSE 8080

CMD ["node", "dist/server.js"]

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Turborepo Filter Command Reference:

| **Filter Flag** | **Target Scope** |
| --- | --- |
| --filter=@repo/web | argets \@repo/web only |
| --filter=@repo/web...             T | rgets \@repo/web AND all its internal dependencies |
| --filter=...@repo/web             T | rgets \@repo/web AND all packages that depend on it |
| --filter=...[origin/main]       Tar | ets all packages changed in current branch vs. main |
| --filter=!@repo/docs | xplicitly excludes \@repo/docs from the execution |

### GitHub Actions Layer Caching with Buildx:

- name: Build and Push Docker Image with GHA Layer Cache

uses: docker/build-push-action@v5

with:

context: .

file: apps/api/Dockerfile

push: true

tags: ghcr.io/my-org/api:${{ github.sha }}

cache-from: type=gha

cache-to: type=gha,mode=max

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Enterprise Monorepo CI/CD & Deployment Architecture

Design a high-scale CI/CD and deployment pipeline for a financial trading organization operating 12 microservices, 3 Next.js applications, and 6 shared libraries in a Turborepo monorepo:

**Requirements**:

1.  **Pull Request Validation Pipeline**:

    - Parallel test shards (Unit, Integration, Playwright E2E) executed across GitHub Actions matrix runners.

    - S3-backed self-hosted Turborepo Remote Cache with signature verification.

    - Dynamic ephemeral preview environment deployments on Vercel and Railway for every PR.

2.  **Production Release Pipeline**:

    - Zero-Downtime **Canary Rollout** strategy (10% -> 50% -> 100%) on Kubernetes with automated Prometheus metrics verification (p99 latency $< 150\text{ms}$, HTTP 5xx error rate $< 0.1%$).

    - Automated rollback trigger if error budget thresholds are breached.

### Problem 2: End-to-End Docker Buildx CI Deployment Pipeline in TypeScript

Build an automated **CI/CD Deployment Controller Script** in TypeScript:

**Requirements**:

1.  **Affected Service Detector (detectChangedApps)**:

    - Executes git diff against base branch origin/main.

    - Uses turbo-graph to compute the list of deployable applications whose code or transitive dependencies have changed.

2.  **Container Image Builder (buildAndTagImages)**:

    - Triggers turbo prune for each changed app.

    - Invokes docker buildx with multi-stage caching flags (type=gha / inline).

3.  **Healthcheck & Automated Rollback Guard (deployAndVerify)**:

    - Deploys updated containers to target cluster.

    - Polls /healthz endpoints every 2 seconds for 30 seconds.

    - If any instance fails the liveness probe, issues immediate zero-loss rollback to PREVIOUS_STABLE_TAG.
