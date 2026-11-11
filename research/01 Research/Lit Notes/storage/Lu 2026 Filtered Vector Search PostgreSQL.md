---
type: lit-note
title: An In-Depth Study of Filter-Agnostic Vector Search on a PostgreSQL Database
  System
authors:
- Duo Lu
- Helena Caminal
- Manos Chatzakis
- Yannis Papakonstantinou
- Yannis Chronis
- Vaibhav Jain
- Fatma Özcan
year: 2026
venue: arXiv (cs.DB)
source_url: https://arxiv.org/abs/2603.23710
doi: 10.1145/3802011
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.5
family:
- storage
evidence: Moderate
score: 7
tags:
- lit-note
- family/storage
---
# An In-Depth Study of Filter-Agnostic Vector Search on a PostgreSQL Database System (Duo Lu et al., 2026)

**Takeaway:** Inside a PostgreSQL-compatible system with pgvector HNSW, page access and tuple handling, not distance computation, dominate filtered vector search time; latency can be up to 10x a standalone library, and the best method depends on filter selectivity and correlation.

## Problem
Whether vector-library benchmarks transfer to vector search inside Postgres.

## Data and period
Four public embedding sets: sift10M, openai5M (1536-d), cohere10M (768-d), text2image10M; 4,500 queries each over 9 selectivities and 5 correlation settings.

## Method
pgvector HNSW with filter-first (NaviX, ACORN) and traversal-first (sweeping, iterative scan) strategies vs a clustering index (ScaNN extension) in a commercial PostgreSQL-compatible system; QPS at 95% recall@10; CPU-cycle breakdowns.

## Baselines and validation
Five methods compared against each other across datasets and filter settings; data pre-warmed in memory.

## Results (with page or section references)
- System overheads (page access, buffer, tuple retrieval) take most query time: e.g. 55.9-84.4% of CPU cycles single-threaded (sec. 5.7 summary).
- Clustering index 2-3x faster than HNSW on low-dimensional data; advantage shrinks for high-dimensional vectors (sec. 5.1).
- Iterative scan loses up to 89% QPS when filters are negatively correlated with similarity (sec. 5.6).
- 16 threads raise CPU cycles per query by 48-68% (sec. 5.7).

## Limits and risks to validity
Commercial Postgres-compatible system (Google), custom ScaNN extension; in-memory only (no disk I/O); read from alphaXiv's structured report, not the full text.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Systems benchmark, not a forecast |
| Baselines | 2 | Several index and filter strategies |
| Point-in-time and leakage controls | N/A | Not a forecasting study |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 2 | Four datasets, wide selectivity/correlation grid |
| Statistical testing | 0 | None reported |
| Reproducibility | 0 | Commercial system; code release not found |
| **Total** | **7/14** | 4 of 8 on applicable checks, scaled |

## Quotes worth keeping (each under 15 words, with page)
- Not kept (read from the structured report; no page-referenced quote).
