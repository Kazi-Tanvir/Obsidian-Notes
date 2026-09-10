---
tags:
  - system-design
  - architecture
  - devops
  - database
  - search
  - nextjs
  - terraform
  - ci-cd
  - backend
date: 2026-09-04
---

# Day 35 - Week 5 Review: Edge Auth, Database Scaling, Monorepo CI-CD, IaC & Hybrid Search

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Week 5 Architectural Synthesis: The Production Cloud Platform

Week 5 synthesized production infrastructure, database scalability, automated delivery, and modern search into a cohesive cloud architecture:

┌──────────────────────────────────── Enterprise Full-Stack Cloud Topology ────────────────────────────────────┐

│                                                                                                              │

│  Global Edge Layer (Cloudflare / Route 53 \+ AWS CloudFront)                                                  │

│  • Edge Middleware: Geo-Routing, Subdomain Multi-Tenancy, DDoS Throttling                                   │

│  • Edge Authentication: JWT Verification & Cookie Validation                                                │

│         │                                                                                                    │

│         ▼                                                                                                    │

│  Application Layer (AWS ECS Fargate Container Mesh / Vercel Serverless)                                      │

│  • Next.js App Router (RSC, Server Actions, Partial Prerendering)                                            │

│  • Fastify / Express Microservices (OpenTelemetry Distributed Tracing & Pino Logging)                       │

│  • Observability Sidecars: OpenTelemetry Collector ──► Prometheus & Grafana Tempo                            │

│         │                                                                                                    │

│         ├─────────────────────────────────┬────────────────────────────────┬─────────────────────────────────┤

│         ▼                                 ▼                                ▼                                 ▼

│  Caching Layer                    Primary Database Cluster         Search & Retrieval Layer          CI/CD Automation

│  • Redis Cluster (Pub/Sub,        • PostgreSQL Master (Writes)     • Elasticsearch (BM25 Lexical)    • GitHub Actions

│    Sliding-Window Rate Limiting,  • Read Replicas (PgBouncer)      • pgvector (HNSW Semantic)        • Turborepo Remote Cache

│    Session Revocation Store)      • Declarative Table Partitioning • Reciprocal Rank Fusion (RRF)    • Docker Multi-Stage Builds

│                                                                                                              │

└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. Cross-Cutting Production Reliability Patterns

1. **Authentication & Multi-Factor Security**:
   - Universal session management using Auth.js (NextAuth.js v5) across Edge Middleware, Server Components, and API Route Handlers.
   - RFC 6238 Time-Based One-Time Passwords (TOTP) for multi-factor authentication with drift-tolerant verification windows.
   - Cookie Jar protection utilizing `__Host-` and `__Secure-` browser prefixes to eliminate subdomain cookie-tossing attacks.
2. **Database Scalability**:
   - **PgBouncer** connection pooling running in transaction mode to prevent PostgreSQL process exhaustion under high concurrent connection spikes.
   - Master-Replica WAL replication featuring causal consistency tracking (Read-Your-Own-Writes) via session write tokens.
   - Range and Hash table partitioning to maintain B-Tree index efficiency on multi-million row datasets.
3. **Hybrid Search Pipelines**:
   - Fusing sparse lexical queries (Elasticsearch BM25) and dense semantic vector distances (`pgvector` HNSW) using Reciprocal Rank Fusion (RRF).
   - Debezium Change Data Capture (CDC) streaming database mutations through Kafka into search indexes, eliminating dual-write inconsistencies.
4. **Automated Infrastructure & Continuous Delivery**:
   - Terraform managing immutable AWS VPC networks, ECS Fargate clusters, Application Load Balancers, and IAM task execution roles.
   - Turborepo Remote Caching in GitHub Actions delivering sub-2-minute monorepo pull request build validations using `turbo prune`.

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Production Architecture Component Comparison:

| Subsystem | Core Technology | Primary Function | Failure Mode / Mitigation |
| :---- | :---- | :---- | :---- |
| **Edge Compute** | V8 Isolates / Edge Middleware | Routing, Auth, Throttling | Memory/CPU limits (keep bundle $< 1\\text{MB}$) |
| **Container Compute** | AWS ECS Fargate | Microservices & background jobs | Task crash (ALB healthcheck automated restart) |
| **Relational DB** | PostgreSQL 16+ | ACID Source of Truth | Connection exhaustion (deploy PgBouncer pool) |
| **Vector Search** | `pgvector` (HNSW) | Semantic similarity | High RAM consumption (tune `m=16, ef=64`) |
| **Lexical Search** | Elasticsearch 8+ | Exact token/spec matching | Split-brain (multi-AZ dedicated master nodes) |
| **Observability** | OpenTelemetry \+ Prometheus | Traces & RED Metrics | Metric cardinality explosion (parameterize routes) |
| **IaC** | Terraform | Reproducible infrastructure | State lock drift (S3 backend \+ DynamoDB lock) |

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Full-Scale Architecture: Enterprise Knowledge & E-Commerce Search Platform

Architect an enterprise-scale global search and recommendation platform serving 20 million active users and 10 million products/documents:

**Requirements**:

1. **Edge & Compute Tier**:
   - Next.js App Router front-end deployed with Partial Prerendering (PPR) and edge auth validation.
   - Dockerized backend microservices deployed on AWS ECS Fargate managed via Terraform.
2. **Database & Hybrid Search Pipeline**:
   - PostgreSQL master database with monthly declarative table partitioning.
   - Debezium CDC pipeline publishing table changes to Kafka.
   - Parallel hybrid search retrieval (pgvector HNSW for embeddings \+ Elasticsearch BM25 for keyword search) merged using Reciprocal Rank Fusion (RRF).
3. **Observability & CI/CD**:
   - OpenTelemetry tracing propagating W3C `traceparent` headers across all service hops.
   - Prometheus scrape endpoints monitoring request duration histograms and error rates.
   - Turborepo \+ Docker CI/CD workflow in GitHub Actions with automated canary deployments.

---

### Problem 2: Observability-Instrumented Search & Query Gateway in TypeScript

Build a production-ready **Observability-Instrumented Hybrid Search Gateway Service** in TypeScript:

**Requirements**:

1. **OpenTelemetry Span Tracking**:
   - Generates an OpenTelemetry child span (`span.recordException()`, `span.end()`) measuring the total hybrid retrieval duration.
   - Propagates W3C trace context headers to downstream services.
2. **Prometheus Latency Metrics**:
   - Records request duration into a Prometheus Histogram with buckets for sub-100ms search SLA monitoring.
3. **Hybrid Search Execution**:
   - Executes parallel lexical keyword matching and vector cosine similarity queries against PostgreSQL.
   - Merges candidate results using the Reciprocal Rank Fusion (RRF) algorithm ($k \= 60$).
4. **Pino Structured Logging**:
   - Emits structured JSON logs containing `{ traceId, spanId, query, resultCount, durationMs }` on every search invocation.

