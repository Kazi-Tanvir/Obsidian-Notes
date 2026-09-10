---
tags:
  - devops
  - observability
  - opentelemetry
  - tracing
  - prometheus
  - logging
  - monitoring
  - backend
date: 2026-09-02
---

# Day 33 - Observability & Telemetry: OpenTelemetry, Distributed Tracing, Prometheus Metrics & Structured Logging

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The 3 Pillars of Observability & The OpenTelemetry (OTel) Standard

In a modern distributed architecture containing dozens of microservices, serverless functions, and databases, debugging production failures requires correlated telemetry across:

1. **Logs (What happened?)**: Structured, immutable, timestamped JSON event records.
2. **Metrics (What is the health/volume?)**: Aggregable numerical time-series data measuring system behavior (CPU, request rates, latency distributions).
3. **Traces (Where was time spent?)**: Request lifecycle propagation tracking a single user operation as it traverses across distributed network boundaries.

**OpenTelemetry (OTel)** is the vendor-neutral CNCF standard providing unified APIs, SDKs, and tooling to generate and export telemetry data to backends like Prometheus, Jaeger, Grafana Tempo, and Datadog.

┌────────────────────────────────────── Distributed Context Propagation ──────────────────────────────────┐

│                                                                                                        │

│  User Browser / Mobile Client                                                                          │

│  └────► HTTP Request (Header: traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01)    │

│           │                                                                                            │

│           ▼                                                                                            │

│  ┌───────────────────────────────── API Gateway (Kong / Envoy) ───────────────────────────────────┐  │

│  │ Root Span: "HTTP POST /checkout" [TraceID: 4bf92f..., SpanID: 00f067...]                        │  │

│  └────────┬────────────────────────────────────────────────────────────────────────────────────────┘  │

│           │                                                                                            │

│           │ HTTP Forward (Propagates same TraceID, New Parent SpanID)                                  │

│           ▼                                                                                            │

│  ┌───────────────────────────────── Order Microservice (Fastify) ─────────────────────────────────┐  │

│  │ Child Span: "process\_order" [TraceID: 4bf92f..., SpanID: 5a8e1b...]                             │  │

│  │  • Sub-Span: "db.query SELECT * FROM inventory" ──► PostgreSQL (SpanID: c3d2e1...)              │  │

│  │  • Sub-Span: "gRPC PaymentService/Charge" ──► Payment Service (SpanID: f7a6b5...)               │  │

│  └─────────────────────────────────────────────────────────────────────────────────────────────────┘  │

│                                                                                                        │

└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

#### The W3C Trace Context Standard (`traceparent`):

OpenTelemetry propagates context across HTTP headers using the W3C `traceparent` specification: `traceparent: {version}-{trace_id}-{parent_id}-{trace_flags}`

- `version`: `00` (Current standard version)
- `trace_id`: 32 hex characters representing the global request transaction.
- `parent_id`: 16 hex characters identifying the caller's span.
- `trace_flags`: `01` (Indicates sampled trace recording).

---

### 2. High-Performance Structured Logging with Pino

Traditional `console.log()` is synchronous in Node.js when writing to terminals or redirected pipes, blocking the event loop during high traffic.

**Pino** is an ultra-fast, zero-overhead JSON logger that formats logs asynchronously, integrates trace IDs for context correlation, and automatically redacts Personally Identifiable Information (PII).

import pino from 'pino';

export const logger \= pino({

  level: process.env.LOG\_LEVEL || 'info',

  // Redact sensitive security fields from logs automatically

  redact: {

    paths: ['req.headers.authorization', 'req.body.password', 'req.body.creditCard'],

    censor: '[REDACTED]',

  },

  // Base fields attached to every log record

  base: {

    service: 'order-service',

    env: process.env.NODE\_ENV,

  },

  timestamp: pino.stdTimeFunctions.isoTime,

});

// Correlated child logger bound to current request trace context

export function createRequestLogger(traceId: string, spanId: string) {

  return logger.child({ traceId, spanId });

}

---

### 3. Application Metrics & The RED Method in Prometheus

The **RED Method** is the gold standard for monitoring microservice architectures:

- **Rate**: Number of requests per second received by the service.
- **Errors**: Number of failing requests per second (HTTP 5xx).
- **Duration**: Amount of time requests take to process (p50, p95, p99 latency distributions).

// Prometheus Metrics Collection with prom-client

import client from 'prom-client';

// Initialize default Node.js runtime metrics (Event Loop lag, Memory, GC)

client.collectDefaultMetrics({ prefix: 'nodejs\_' });

// 1. Counter: Monotonically increasing counter for HTTP requests (Rate & Errors)

export const httpRequestsTotal \= new client.Counter({

  name: 'http\_requests\_total',

  help: 'Total number of incoming HTTP requests',

  labelNames: ['method', 'route', 'status\_code'],

});

// 2. Histogram: Measures request duration distributions (Duration)

export const httpRequestDurationSeconds \= new client.Histogram({

  name: 'http\_request\_duration\_seconds',

  help: 'HTTP request duration in seconds',

  labelNames: ['method', 'route', 'status\_code'],

  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5], // 10ms to 5s buckets

});

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### The 4 Prometheus Metric Types:

| Metric Type | Behavior | Best Use Case | PromQL Query Example |
| :---- | :---- | :---- | :---- |
| **Counter** | Cumulative metric that only increases or resets to zero | Request counts, error occurrences, task runs | `rate(http_requests_total[5m])` |
| **Gauge** | Value that can arbitrarily go up and down | Memory usage, active WebSocket connections | `avg_over_time(active_users[1m])` |
| **Histogram** | Samples observations into configurable buckets | HTTP latency, database query duration | `histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))` |
| **Summary** | Calculates client-side quantiles (p50, p99) over sliding window | High-precision latency when server aggregation is not needed | `http_duration_seconds{quantile="0.99"}` |

### PromQL Alerting Formulas:

# 1. Error Rate Percentage (> 1% triggers P1 Alert)

sum(rate(http\_requests\_total{status\_code=\~"5.."}[5m]))

/

sum(rate(http\_requests\_total[5m])) * 100 > 1.0

# 2. 99th Percentile Latency Exceeds 300ms

histogram\_quantile(0.99, sum(rate(http\_request\_duration\_seconds\_bucket[5m])) by (le)) > 0.3

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global Telemetry & Distributed Tracing Infrastructure Design

Design a high-throughput observability pipeline for an enterprise microservice architecture processing 150,000 requests per second across 25 services:

**Requirements**:

1. **Telemetry Pipeline Architecture**:
   - In-process OpenTelemetry SDK instrumentation with head-based vs. tail-based probabilistic sampling (100% of errors and slow requests $\\ge 500\\text{ms}$, 1% of normal 200 OK requests).
   - Deployment of OpenTelemetry Collectors as DaemonSets / sidecars to buffer, batch, and export metrics/traces without slowing app runtimes.
   - Storage backends: Prometheus / Mimir for metrics, Grafana Tempo / Jaeger for traces, Elasticsearch / Loki for logs.
2. **SLA / SLO Dashboarding**:
   - Define formal Service Level Objectives (e.g. 99.9% availability, 99% of requests $< 200\\text{ms}$) and Error Budget burn rate alerts.

---

### Problem 2: Complete Observability Suite Middleware in TypeScript

Build a production-grade **Observability & Telemetry Middleware for Fastify / Express**:

**Requirements**:

1. **Trace Context Interceptor (`traceContextMiddleware`)**:
   - Parses incoming W3C `traceparent` headers. If missing, generates a new 16-byte random trace ID and span ID.
   - Injects the trace context into the request object and sets the outgoing `traceparent` and `x-request-id` response headers.
2. **Prometheus Metrics Recorder**:
   - Automatically records every incoming request method, path template (e.g. `/users/:id` rather than raw `/users/123` to prevent metric cardinality explosion), and response status code.
   - Measures exact duration using high-resolution timers (`process.hrtime.bigint()`) and records into `http_requests_total` and `http_request_duration_seconds`.
3. **Structured Context Logging**:
   - Wraps every request with a child Pino logger pre-bound with `{ traceId, spanId, method, path }`.
   - Emits a standardized structured log line on request completion containing duration and status code.
4. Includes a dedicated `/metrics` endpoint that exposes Prometheus formatted scrape output.

