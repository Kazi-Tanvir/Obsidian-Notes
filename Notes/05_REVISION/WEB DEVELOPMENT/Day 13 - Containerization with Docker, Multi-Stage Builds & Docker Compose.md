---
tags:
- devops
- docker
- containerization
- docker-compose
- backend
- infrastructure
date: 2026-08-13
---

# Day 13 - Containerization with Docker, Multi-Stage Builds & Docker Compose

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Containerization Fundamentals & Linux Primitives

Containerization isolates applications and their dependencies into portable execution units. Unlike Hypervisor Virtual Machines (which virtualize guest OS hardware), Docker containers share the host OS Linux kernel, providing sub-second startup times and near-zero CPU/memory overhead.

#### Underlying Linux Kernel Primitives:

- **Namespaces**: Provides process-level isolation (PID, NET, MNT, IPC, UTS, USER).

- **Control Groups (cgroups)**: Limits and monitors resource usage (CPU, Memory, Disk I/O).

- **Union File System (UnionFS / OverlayFS)**: Stackable read-only image layers merged with a thin writable container layer.

### 2. Dockerfile Optimization & Layer Caching Mechanics

Docker builds images sequentially from Dockerfile instructions. Each instruction (RUN, COPY, ADD) creates an immutable layer.

#### Optimization Tactics:

- **Order Operations by Change Frequency**: Copy package.json and install dependencies *before* copying application source code to maximize layer cache hits during code edits.

- **Security Principles**: Never execute processes as root. Specify USER node or create an unprivileged system user.

- **Minimizing Image Footprint**: Use Minimal Linux distributions (alpine or Google distroless).

### 3. Multi-Stage Builds for Node.js / Next.js

Multi-stage builds use multiple FROM instructions in a single Dockerfile. Dev dependencies, compilers, and build tools remain in intermediate build stages, producing a lightweight, minimal production image.

# Multi-Stage Dockerfile for Next.js App Router

# Stage 1: Base Dependencies

FROM node:20-alpine AS base

RUN apk add --no-cache libc6-compat

WORKDIR /app

# Stage 2: Install Dependencies

FROM base AS deps

COPY package.json pnpm-lock.yaml ./

RUN corepack enable pnpm && pnpm install --frozen-lockfile

# Stage 3: Builder Stage

FROM base AS builder

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules

COPY . .

ENV NEXT_TELEMETRY_DISABLED 1

RUN corepack enable pnpm && pnpm run build

# Stage 4: Production Runner Stage (Minimal Distroless Footprint)

FROM node:20-alpine AS runner

WORKDIR /app

ENV NODE_ENV production

ENV NEXT_TELEMETRY_DISABLED 1

# Security: Non-root execution

RUN addgroup --system --gid 1001 nodejs

RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./

COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT 3000

CMD ["node", "server.js"]

### 4. Local Orchestration with Docker Compose

Docker Compose defines and runs multi-container applications (Node API, PostgreSQL, Redis) via a declarative YAML configuration.

version: '3.8'

services:

app:

build:

context: .

target: runner

ports:

- "3000:3000"

environment:

- DATABASE_URL=postgresql://postgres:secret@db:5432/app_db

- REDIS_URL=redis://redis:6379

depends_on:

db:

condition: service_healthy

redis:

condition: service_started

networks:

- app-network

db:

image: postgres:16-alpine

environment:

POSTGRES_USER: postgres

POSTGRES_PASSWORD: secret

POSTGRES_DB: app_db

volumes:

- pgdata:/var/lib/postgresql/data

healthcheck:

test: ["CMD-SHELL", "pg_isready -U postgres"]

interval: 5s

timeout: 5s

retries: 5

networks:

- app-network

redis:

image: redis:7-alpine

networks:

- app-network

volumes:

pgdata:

networks:

app-network:

driver: bridge

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Directive / Command** | **Usage / Syntax** | **Purpose** |
| --- | --- | --- |
| **FROM <image> AS <stage>**   FRO | node:20-alpine AS builder              Def | nes named multi-stage build context |
| **COPY --from=<stage>**        CO | Y --from=builder /app/dist ./dist       Cop | es artifacts from previous build stage |
| **USER node** | USER node | Drops root privileges for security |
| **docker build -t app .** | docker build --target runner -t app:v1 . | uilds targeted production stage |
| **docker-compose up -d** | docker-compose up --build -d | pins up multi-container environment in background |
| **docker system prune -a** | docker system prune -a --volumes | leans up unused layers, images, and volumes |

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Production Monorepo Containerization Architecture)

Design a multi-stage Docker build and deployment strategy for a **pnpm Turborepo Monorepo** containing 2 Next.js apps (apps/web, apps/admin) and 1 Fastify API (apps/api).

**Requirements**:

1.  Detail how to use turbo prune --scope=web inside Docker to extract only necessary workspace packages.

2.  Formulate a Docker layer caching strategy to avoid re-installing pnpm dependencies when unrelated monorepo apps change.

3.  Design a Docker Compose development stack supporting live hot-reloading (COPY vs volume mounts).

### Problem 2: End-to-End Code Implementation Challenge

Build a production-ready **Docker Compose Environment with Nginx Reverse Proxy, Fastify API, Redis & PostgreSQL**.

**Requirements**:

1.  Write an optimized multi-stage Dockerfile for a Fastify API using TypeScript.

2.  Write a docker-compose.yml orchestrating Nginx (SSL termination & rate limiting proxy), Fastify API (3 replicas with load balancing), PostgreSQL (with healthchecks), and Redis.

3.  Ensure Nginx routes /api/* requests to the Fastify service replicas using bridge networking.

4.  Include startup verification tests validating healthcheck execution and zero-downtime container restarts.
