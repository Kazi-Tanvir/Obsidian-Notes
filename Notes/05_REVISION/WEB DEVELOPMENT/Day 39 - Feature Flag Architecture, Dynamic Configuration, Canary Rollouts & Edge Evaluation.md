tags:

- devops

- feature-flags

- architecture

- system-design

- canary-deployment

- edge-computing

- launchdarkly

- backend date: 2026-09-08

# Day 39 - Feature Flag Architecture, Dynamic Configuration, Canary Rollouts & Edge Evaluation

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Decoupling Deployment from Release

In modern continuous delivery (CD), **Deployment** (shipping code to
production infrastructure) and **Release** (exposing functionality to
users) are separate events. Static environment variables
(process.env.FEATURE_ENABLED) require full application rebuilds and
redeployments, creating deployment bottlenecks.

**Feature Flags (Feature Toggles)** provide dynamic, runtime control
over application behavior without code modifications.

┌────────────────────────────────────── Feature Flag Evaluation
Topologies ──────────────────────────────────────┐

│ │

│ Antipattern: Synchronous Remote API Polling │

│ Client / Server ───────► HTTP GET /api/flags/my-flag ───────► Flag
Server (Adds 80ms latency per request! 🐢)│

│ │

│ Enterprise Architecture: In-Memory Local Evaluation with Streaming
Sync │

│ │

│ ┌───────────────────────┐ Streaming Deltas (SSE / gRPC)
┌───────────────────────────────────┐ │

│ │ Central Flag Server │ ────────────────────────────────────────────►
│ Application Server (Node.js/Next) │ │

│ │ • Rules Management UI │ │ • In-Memory Evaluation Engine │ │

│ │ • Postgres DB │ │ • Sub-microsecond evaluations (\<1μs)│

│ └───────────────────────┘ │ • Zero Network Hops on request! ⚡ │

│ └───────────────────────────────────┘ │

│ ▲ │

│ │ Local Hash Check │

│ Inbound User Request │

│ │

└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Deterministic Percentage Rollouts (Consistent Hashing)

To perform a canary release (e.g. expose a new checkout flow to exactly
10% of users), the system must guarantee:

1.  **Consistency**: The same user must always receive the same
    variation across multiple requests and devices without storing user
    states in a database.

2.  **Uniform Distribution**: Bucketing must distribute users evenly
    from 0% to 100%.

3.  **Flag Independence**: A user in the 10% bucket for Feature A must
    not automatically be in the 10% bucket for Feature B.

#### The Mathematical MurmurHash3 Bucket Formula:

\$\$\\text{Hash Value} = \\text{MurmurHash3}(\\text{User ID} +
\\text{\":\"} + \\text{Flag Key})\$\$ \$\$\\text{Bucket Number} =
(\\text{Hash Value} \\pmod{100}) + 1\$\$ \$\$\\text{Is Enabled} =
\\text{Bucket Number} \\le \\text{Rollout Percentage}\$\$

// Example: Deterministic In-Memory Hashing

import murmurhash from \'murmurhash\';

function evaluatePercentageRollout(userId: string, flagKey: string,
rolloutPercentage: number): boolean {

const seed = 0;

const hash = murmurhash.v3(\`\${userId}:\${flagKey}\`, seed);

const bucket = (Math.abs(hash) % 100) + 1; // Scale 1 to 100

return bucket \<= rolloutPercentage;

}

console.log(evaluatePercentageRollout(\'usr_9812\', \'new-checkout-v2\',
10)); // Deterministic boolean

### 3. Edge Flag Evaluation (Vercel Edge / Cloudflare Workers)

Evaluating feature flags inside Next.js Edge Middleware allows
zero-latency A/B routing and HTML streaming before SSR execution:

// middleware.ts (Next.js Edge Middleware)

import { NextRequest, NextResponse } from \'next/server\';

export async function middleware(req: NextRequest) {

const userId = req.cookies.get(\'user_id\')?.value \|\|
crypto.randomUUID();

const res = NextResponse.next();

// Edge in-memory deterministic flag evaluation:

const isV2Enabled = evaluatePercentageRollout(userId, \'checkout-v2\',
25);

if (isV2Enabled) {

// Zero-redirect URL rewrite to V2 variant at the edge:

return NextResponse.rewrite(new URL(\'/checkout/v2\', req.url));

}

return res;

}

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Feature Flag Types & Lifecycle Matrix:

  ---------------------------------------------------------------------------
  **Flag         **Longevity**   **Target       **Primary      **Cleanup
  Category**                     Audience**     Purpose**      Urgency**
  -------------- --------------- -------------- -------------- --------------
  **Release      1 - 4 Weeks     Canary % /     Safe phased    **High** (Tech
  Toggle**                       Internal       rollout        debt if kept)

  **Experiment   2 - 8 Weeks     Random Cohorts Statistical    High (Remove
  Toggle**                       (A/B)          hypothesis     on test end)
                                                testing        

  **Ops Kill     Permanent       Global /       Graceful       Low (Permanent
  Switch**                       Critical Paths system         safety net)
                                                degradation    

  **Permission   Permanent       Entitled /     SaaS feature   Low (Core
  Toggle**                       Paying Tiers   gating &       business
                                                licensing      logic)
  ---------------------------------------------------------------------------

### Flag Evaluation Rules Engine Schema (JSON):

{

\"flagKey\": \"ai-summary-generation\",

\"defaultVariant\": false,

\"rules\": \[

{ \"attribute\": \"email\", \"operator\": \"ends_with\", \"value\":
\"@company.com\", \"variant\": true },

{ \"attribute\": \"tier\", \"operator\": \"equals\", \"value\":
\"enterprise\", \"variant\": true },

{ \"rolloutPercentage\": 20, \"variant\": true }

\]

}

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Real-Time Feature Flagging System at Scale

Architect an enterprise-scale Feature Flag & Configuration Platform
supporting 500,000 evaluations/sec:

**Requirements**:

1.  **Sub-5-Second Propagation with Sub-Millisecond Evaluation**:

    - Updates made by product managers in an Admin UI must push to 500
      microservice nodes worldwide within 5 seconds using Server-Sent
      Events (SSE) or Redis Pub/Sub.

    - Flag evaluations must happen locally in memory in \$\<
      5\\mu\\text{s}\$ with zero network round-trips per request.

2.  **Offline Resilience & Crash Safety**:

    - If the central flag server goes offline, client SDKs must continue
      operating using local disk-persisted snapshot configurations.

3.  **Telemetry & Exposure Analytics**:

    - Collects aggregated flag exposure counts without degrading API
      throughput or creating telemetry lock contention.

### Problem 2: In-Memory Feature Flag Engine in TypeScript

Build a production-grade **In-Memory Feature Flag Evaluation Engine** in
TypeScript:

**Requirements**:

1.  **Multi-Attribute Rule Evaluator**:

    - Supports targeting rules with operators: equals, in_list,
      semver_gte (for mobile app versions), and percentage_rollout.

2.  **Consistent MurmurHash3 User Bucketing**:

    - Guarantees deterministic, uniformly distributed percentage
      allocation per flag.

3.  **Background SSE Stream Client with Local Cache**:

    - Connects to an SSE stream endpoint to receive live flag delta
      events (FLAG_UPDATED, FLAG_DELETED).

    - Automatically maintains an internal in-memory rule cache and
      dispatches change listeners.
