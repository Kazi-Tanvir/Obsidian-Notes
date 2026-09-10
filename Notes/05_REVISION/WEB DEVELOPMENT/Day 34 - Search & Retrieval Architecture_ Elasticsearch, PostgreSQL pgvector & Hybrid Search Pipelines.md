---
tags:
  - database
  - search
  - elasticsearch
  - pgvector
  - embeddings
  - rag
  - backend
  - system-design
date: 2026-09-03
---

# Day 34 - Search & Retrieval Architecture: Elasticsearch, PostgreSQL pgvector & Hybrid Search Pipelines

---

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. The Search Paradigm: Lexical BM25 vs. Semantic Vector Retrieval

Modern application search has evolved past basic SQL `LIKE '%keyword%'` queries:

- **Lexical Search (BM25 / Inverted Index)**: Breaks text into normalized tokens (stemming, stop-words, lowercase) and indexes document frequency. Unbeatable for exact keyword matches, SKU numbers, product models, and legal names, but blind to synonyms or user intent.
- **Semantic Vector Search (Embeddings / ANN)**: Encodes text into high-dimensional vector representations (e.g. 1536-dimensional float arrays from OpenAI `text-embedding-3-small` or Cohere). Matches conceptual similarity (e.g. "comfy winter clothing" matches "wool sweater"), but struggles with exact SKU numbers or rare keywords.
- **Hybrid Search**: Fuses sparse lexical scores (BM25) with dense semantic vector distances using algorithms like **Reciprocal Rank Fusion (RRF)**.

┌────────────────────────────────────── Hybrid Search Architecture ──────────────────────────────────────┐

│                                                                                                        │

│  User Search Query: "lightweight waterproof hiking jacket"                                             │

│  ┌───────────────────────────────────────────────┬──────────────────────────────────────────────────┐  │

│  │                                               │                                                  │  │

│  ▼                                               ▼                                                  ▼  │

│  Lexical Pipeline (Elasticsearch / BM25)         Vector Pipeline (pgvector / HNSW)                     │  │

│  • Tokenization & Stemming: ["lightweight", ...] • Generate Embedding (1536d Float32 Array)        │  │

│  • Matches exact product specs and keywords      • Approximate Nearest Neighbor (ANN) Cosine Search │  │

│  │                                               │                                                  │  │

│  └───────────────────────┬───────────────────────┴──────────────────────────┬───────────────────────┘  │

│                          │ Top 50 Ranked Lexical Results                    │ Top 50 Ranked Vector Results     │

│                          ▼                                                  ▼                                  │

│                 ┌────────────────────────────────────────────────────────────────────┐                         │

│                 │ Reciprocal Rank Fusion (RRF) Scorer: RRF(d) \= Σ 1 / (60 \+ rank(d)) │                         │

│                 └─────────────────────────────────┬──────────────────────────────────┘                         │

│                                                   ▼                                                            │

│                                       Unified Final Ranked Top 20                                              │

│                                                                                                        │

└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

---

### 2. High-Performance Vector Search with PostgreSQL `pgvector`

`pgvector` turns standard PostgreSQL into a vector database, eliminating the operational complexity of running separate vector stores like Pinecone or Milvus.

#### Indexing Algorithms: IVFFlat vs. HNSW

- **IVFFlat (Inverted File Flat)**: Partitions vector space into Voronoi cells. Fast build times, low memory, but lower query recall during dataset mutations.
- **HNSW (Hierarchical Navigable Small World)**: Builds a multi-layer proximity graph. Superior query latency (sub-10ms) and high recall ($> 98%$), but requires significantly higher RAM.

-- PostgreSQL pgvector Configuration & Schema

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE products (

  id UUID PRIMARY KEY DEFAULT gen\_random\_uuid(),

  title TEXT NOT NULL,

  description TEXT NOT NULL,

  category TEXT NOT NULL,

  price NUMERIC(10, 2\) NOT NULL,

  -- Full-Text Lexical Search Vector

  tsv\_content TSVECTOR GENERATED ALWAYS AS (

    to\_tsvector('english', title || ' ' || description)

  ) STORED,

  -- 1536-Dimensional Semantic Embedding Vector

  embedding VECTOR(1536) NOT NULL

);

-- 1. Create Inverted Index for Lexical Full-Text Search

CREATE INDEX idx\_products\_tsv ON products USING GIN (tsv\_content);

-- 2. Create HNSW Vector Index for Semantic Cosine Similarity

-- m: Max connections per element, ef\_construction: Build search depth

CREATE INDEX idx\_products\_hnsw ON products USING hnsw (embedding vector\_cosine\_ops)

WITH (m \= 16, ef\_construction \= 64);

#### Vector Distance Operators in `pgvector`:

- `<=>`: Cosine Distance ($1 - \\text{cosine\_similarity}$) — standard for text embeddings.
- `<->`: L2 / Euclidean Distance — standard for computer vision image embeddings.
- `<#>`: Negative Inner Product — standard for normalized dot-product embeddings.

---

### 3. Reciprocal Rank Fusion (RRF) Hybrid Algorithm

RRF combines ranking orders from disparate algorithms without requiring score normalization:

$$\\text{RRF Score}(d) \= \\sum\_{m \\in M} \\frac{1}{k \+ r\_m(d)}$$

Where $k$ is a smoothing constant (typically $60$) and $r\_m(d)$ is the 1-based ranking position of document $d$ in system $m$.

// Hybrid Reciprocal Rank Fusion Implementation in TypeScript

interface SearchResult {

  id: string;

  title: string;

}

export function reciprocalRankFusion(

  lexicalResults: SearchResult[],

  vectorResults: SearchResult[],

  k: number \= 60

): (SearchResult & { score: number })[] {

  const scores \= new Map<string, { doc: SearchResult; score: number }>();

  // 1. Process Lexical Rankings

  lexicalResults.forEach((doc, rank) \=> {

    const rrfWeight \= 1 / (k \+ (rank \+ 1));

    scores.set(doc.id, { doc, score: rrfWeight });

  });

  // 2. Process Vector Rankings and Accumulate

  vectorResults.forEach((doc, rank) \=> {

    const rrfWeight \= 1 / (k \+ (rank \+ 1));

    if (scores.has(doc.id)) {

      scores.get(doc.id)!.score \+= rrfWeight;

    } else {

      scores.set(doc.id, { doc, score: rrfWeight });

    }

  });

  // 3. Sort Descending by Fused RRF Score

  return Array.from(scores.values())

    .sort((a, b) \=> b.score - a.score)

    .map(({ doc, score }) \=> ({ ...doc, score }));

}

---

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Vector Index Tuning Reference (`pgvector`):

| Parameter | Default | Tradeoff | Description |
| :---- | :---- | :---- | :---- |
| `m` (HNSW) | 16 | Higher \= Better recall, higher RAM | Max bidirectional links per node in graph |
| `ef_construction` | 64 | Higher \= Slower index build, better recall | Size of candidate list during index graph construction |
| `hnsw.ef_search` | 40 | Higher \= Slower query latency, higher recall | Query-time search depth (`SET hnsw.ef_search = 100`) |

### Hybrid Search Query in PostgreSQL (`TSVector` \+ `pgvector`):

WITH lexical\_matches AS (

  SELECT id, title, ROW\_NUMBER() OVER (ORDER BY ts\_rank\_cd(tsv\_content, query) DESC) as rank

  FROM products, plainto\_tsquery('english', 'waterproof hiking') query

  WHERE tsv\_content @@ query

  LIMIT 50

),

vector\_matches AS (

  SELECT id, title, ROW\_NUMBER() OVER (ORDER BY embedding <=> '[0.012, -0.045, ...]'::vector) as rank

  FROM products

  ORDER BY embedding <=> '[0.012, -0.045, ...]'::vector

  LIMIT 50

)

SELECT COALESCE(l.id, v.id) AS id, COALESCE(l.title, v.title) AS title,

       COALESCE(1.0 / (60 \+ l.rank), 0.0) \+ COALESCE(1.0 / (60 \+ v.rank), 0.0) AS rrf\_score

FROM lexical\_matches l

FULL OUTER JOIN vector\_matches v ON l.id \= v.id

ORDER BY rrf\_score DESC

LIMIT 20;

---

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Global E-Commerce Hybrid Search Architecture

Design a multi-tenant enterprise search engine supporting 50 million products, 50,000 queries per second, and sub-50ms p99 response times:

**Requirements**:

1. **Real-Time Data Synchronization Pipeline**:
   - Eliminates database/search dual-write bugs by utilizing **Change Data Capture (CDC)** via Debezium and Apache Kafka from PostgreSQL to Elasticsearch.
   - Asynchronous worker pool that generates 1536-dimensional vector embeddings on product creation/update with automated batching.
2. **Multi-Stage Query & Reranking Pipeline**:
   - Fast retrieval phase: Top 100 candidates fetched in parallel from Elasticsearch (BM25) and PostgreSQL `pgvector` (HNSW).
   - Reciprocal Rank Fusion blending.
   - Cross-Encoder AI Reranker (e.g. Cohere Rerank / BGE-Reranker) scoring the top 30 items for precision relevance.

---

### Problem 2: Complete Hybrid Search Service in TypeScript

Build a production-grade **Hybrid Search Service Module** in TypeScript using Prisma and Raw SQL:

**Requirements**:

1. **Embedding Generator & Cache (`getOrGenerateEmbedding`)**:
   - Computes SHA-256 hash of search query string.
   - Checks Redis cache; on miss, calls embedding model, caches vector with 24-hour TTL.
2. **Parallel Hybrid Query Executor (`executeHybridSearch`)**:
   - Simultaneously queries PostgreSQL for full-text lexical ranking (`ts_rank_cd`) and vector semantic distance (`<=>`).
   - Merges results using Reciprocal Rank Fusion (RRF with $k \= 60$).
3. **Faceted Filtering Guard**:
   - Supports metadata filtering (`price_range`, `category`, `in_stock`) in both lexical and vector stages without causing HNSW post-filtering graph disconnects.

