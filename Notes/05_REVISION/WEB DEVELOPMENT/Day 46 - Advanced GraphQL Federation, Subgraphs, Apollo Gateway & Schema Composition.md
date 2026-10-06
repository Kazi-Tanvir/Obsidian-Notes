---
tags:
  - backend
  - graphql
  - federation
  - apollo
  - microservices
  - schema-stitching
  - distributed-systems
  - architecture
date: 2026-09-15
---

# Day 46 - Advanced GraphQL Federation, Subgraphs, Apollo Gateway & Schema Composition

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Monolithic GraphQL Bottleneck & Apollo Federation 2

When organizations transition from REST to GraphQL, they frequently construct a monolithic schema. As the engineering organization expands to dozens of teams, the monolith creates massive organizational friction:

- Merge conflicts across multiple teams modifying a shared schema.graphql file.

- Single point of failure: a syntax or type error introduced by Team A blocks deployments for Team B.

- Tight coupling across service boundaries.

**Apollo Federation 2** decomposes the monolithic schema into autonomous, independently deployable **Subgraphs** owned by individual microservice teams, unified by an **Apollo Router / Gateway** into a single cohesive **Supergraph**:

```text
┌────────────────────────────────────── Apollo Federation 2 Architecture ──────────────────────────────────────┐
│                                                                                                              │
│   Client Application (Mobile / Browser / Web)                                                                │
│        │                                                                                                     │
│        ▼ HTTP POST (Single Unified GraphQL Supergraph Query)                                                 │
│   [ Apollo Router (Rust Engine) ]                                                                            │
│   • Validates incoming query against composed Supergraph Schema                                              │
│   • Compiles optimized Query Plan (Parallel DAG execution across subgraphs)                                  │
│        │                                                                                                     │
│        ├───────────────────────────────┬──────────────────────────────────┬──────────────────────────────────┤
│        ▼                               ▼                                  ▼                                  ▼
│   [ Subgraph: Users ]          [ Subgraph: Products ]     [ Subgraph: Inventory ]    [ Subgraph: Reviews ]   │
│   • Owns `User` entity         • Owns `Product` entity    • Extends `Product`        • Extends `Product`     │
│   • Resolves profile, auth     • Resolves SKU, title      • Resolves stock, shipping • Resolves ratings      │
│   • Service A (Node.js/Prisma) • Service B (Fastify/SQL)  • Service C (Go/gRPC)      • Service D (Python)    │
│                                                                                                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. Core Federation 2 Directives

#### 1. Entity Definition (@key):

An entity is a type that can be referenced and extended across subgraphs:

# products-subgraph.graphql

type Product \@key(fields: "id") {

id: ID!

title: String!

price: Float!

}

#### 2. Cross-Subgraph Entity Extension & Dependencies (@requires):

Another subgraph can extend Product and compute fields that depend on properties resolved by other subgraphs:

# inventory-subgraph.graphql

extend type Product \@key(fields: "id") {

id: ID! \@external

weight: Float! \@external # Defined in Products subgraph

# Computes shipping cost based on weight from Products subgraph!

shippingEstimate: Float! \@requires(fields: "weight")

inStock: Boolean!

}

#### 3. Field Sharing (@shareable):

Allows multiple subgraphs to calculate or return the exact same field value without schema composition conflicts:

type User \@key(fields: "id") {

id: ID!

role: String! \@shareable # Both Auth Subgraph and Users Subgraph can resolve role

}

### 3. Resolving Entities in Subgraphs (__resolveReference)

When the Apollo Router executes a Query Plan requiring fields across subgraphs, it calls the entity reference resolver:

// inventory-subgraph/resolvers.ts

export const resolvers = {

Product: {

// Apollo Router invokes this when hydrating a Product from another subgraph!

__resolveReference: async (reference: { id: string; weight?: number }, { dataSources }: any) => {

const stock = await dataSources.inventoryDb.getStockByProductId(reference.id);

return {

id: reference.id,

weight: reference.weight, // Provided by Router via \@requires!

inStock: stock > 0,

};

},

shippingEstimate: (product: { weight: number }) => {

// Direct access to required field from external subgraph

return product.weight * 1.75 + 5.00;

},

},

};

### 4. Mitigating Subgraph N+1 Network Cascades

If a client queries 100 products and their inventory status, naive Federation would fire 100 HTTP requests to the Inventory subgraph.

- **Subgraph DataLoader Batching**: Every subgraph must implement batching on __resolveReference using **DataLoader** over _entities queries to ensure 100 items are resolved in a single batch request over HTTP/2 or gRPC.

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Apollo Federation 2 Directives Reference:

----------------------------------------------------------------------- **Directive**           **Applied To**          **Purpose** ----------------------- ----------------------- ----------------------- \@key(fields: "\...") Object / Interface      Identifies unique primary key(s) of an entity.

\@shareable             Field / Object          Permits multiple subgraphs to resolve the exact same field.

\@external              Field                   Marks a field as owned by a different subgraph.

\@requires(fields:      Field                   Declares external "\...")                                       fields required to compute this field.

\@provides(fields:      Field                   Pre-resolves nested "\...")                                       entity fields to eliminate subgraph hops.

\@override(from:        Field                   Migrates field "\...")                                       ownership incrementally between subgraphs. -----------------------------------------------------------------------

### Supergraph Composition Command (rover):

```bash
```bash
# Validate and compose subgraphs into supergraph schema
rover supergraph compose --config ./supergraph.yaml > supergraph.graphql
SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS
```
SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS
```

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Retail Federated Supergraph Architecture

Design a high-scale Federated GraphQL Supergraph for a global retailer processing 30,000 requests/second across 4 subgraphs (Users, Catalog, Orders, Recommendations):

**Requirements**:

1.  **Zero-Downtime Schema Composition (CI/CD)**:

    - Automated Apollo Studio / Rover checks in GitHub Actions that validate pull request schema changes against production client query traffic (Schema Checks) to eliminate breaking changes.

2.  **Query Plan Optimization & Latency Guards**:

    - Architect routing rules to ensure no client query generates more than 3 sequential subgraph hops.

3.  **Subgraph Authentication Context Passing**:

    - Forward authenticated JWT claims (User ID, Role, Tenant ID) securely from the Apollo Router down to subgraphs via custom internal headers (x-user-id, x-user-role).

### Problem 2: Complete Apollo Federation 2 Subgraph Service in TypeScript

Build an Enterprise **Apollo Federation 2 Inventory Subgraph Service** in TypeScript using \@apollo/subgraph:

**Requirements**:

1.  **Schema Definition**:

    - Extends the Product entity (@key(fields: "id")).

    - Requires dimensions { weight, height } from the Catalog subgraph using \@requires.

    - Resolves shippingTier (enum: STANDARD, OVERSIZED, FREIGHT).

2.  **Batch Entity Reference Resolver with DataLoader**:

    - Implements Product.__resolveReference using DataLoader to batch multiple entity hydration requests into a single database query.

3.  **Health & Introspection**:

    - Exposes standard healthcheck /healthz and federated schema inspection endpoints compliant with Apollo Federation 2 specification.
