---
type: lit-note
title: 'Graph Memory for LLM Agents: At What Cost? Query, Ingest and Update Performance
  Across Graph Database Engines'
authors:
- Donald Nguyen
- Gurbinder Gill
- Hadi Ahmadi
- Christopher J. Rossbach
year: 2026
venue: arXiv (cs.DB)
source_url: https://arxiv.org/abs/2609.23315
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.5
- RQ3.7
family:
- storage
evidence: Weak
score: 5
tags:
- lit-note
- family/storage
---
# Graph Memory for LLM Agents: At What Cost? Query, Ingest and Update Performance Across Graph Database Engines (Donald Nguyen et al., 2026)

**Takeaway:** On a synthetic 1M-node graph, no engine was fastest on every query: a native graph engine won bounded neighbourhood queries, but columnar SQL over edge tables won scans, joins and top-k, and bulk-ingest speed (5k to 4.3M rows/s) was the largest cost difference.

## Problem
Whether graph databases are needed for connected-data workloads or edge tables in a columnar engine suffice.

## Data and period
Synthetic biomedical-shaped property graph: 1.02M nodes, 5.34M node+edge rows, plus 1K and 10K scales (sec. 3.1).

## Method
Twenty query shapes (neighbourhood, paths, joins, aggregation, top-k, temporal filters) run natively on Corvic AI (authors' columnar engine), DuckPGQ (SQL/PGQ on DuckDB), LoraDB, Ladybug, Memgraph, Neo4j, HugeGraph, FalkorDB; latency geomean, correctness, ingest, update latency; simple total-cost model.

## Baselines and validation
Seven other engines; no statistical tests; single harness and hardware.

## Results (with page or section references)
- Geomean at 1.02M nodes: Corvic 2.19 ms, DuckPGQ 4.18, Memgraph 4.77, Neo4j 6.92, HugeGraph 61.8 (Table 1).
- Native graph engine (Ladybug) faster on bounded paths (1.76 vs 2.62 ms) but 4.6-10.9x slower on hash join, self join, top-k (sec. 5.4).
- DuckPGQ ties hand-written SQL on joins but is 2.26x slower on graph shapes due to plan choice (sec. 5.3).
- Bulk ingest varies about 860x across engines; dominates total cost below about 10^5 queries per refresh (sec. 5.5).
- Point updates: Memgraph/FalkorDB fastest (0.85-0.90 ms) (sec. 5.5).

## Limits and risks to validity
Authors' own product is the subject (conflict of interest, disclosed); synthetic data; Ladybug figures differ between Table 1 and Appendix A.1 (copy vs attach mode appear swapped); one harness, no repeated-run statistics.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Systems benchmark, not a forecast |
| Baselines | 1 | Seven engines |
| Point-in-time and leakage controls | N/A | Not a forecasting study |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | One synthetic graph, three scales |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Full table published; no code |
| **Total** | **5/14** | 3 of 8 on applicable checks, scaled (5.25) |

## Quotes worth keeping (each under 15 words, with page)
- "the shape of the query, not the label 'graph database,'" predicts the fastest engine (sec. 5.4; fragment)
