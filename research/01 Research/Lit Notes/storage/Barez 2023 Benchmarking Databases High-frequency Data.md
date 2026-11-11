---
type: lit-note
title: Benchmarking Specialized Databases for High-frequency Data
authors:
- Fazl Barez
- Paul Bilokon
- Ruijie Xiong
year: 2023
venue: arXiv (cs.DB)
source_url: https://arxiv.org/abs/2301.12561
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.5
family:
- storage
evidence: Weak
score: 4
tags:
- lit-note
- family/storage
---
# Benchmarking Specialized Databases for High-frequency Data (Fazl Barez et al., 2023)

**Takeaway:** On one month of crypto trades and order-book data (about 25 GB), kdb+ was fastest at ingestion and most queries, InfluxDB stored data most compactly, TimescaleDB ingested fast but had the highest query latency, and ClickHouse ingested slowest; single-thread, single-client only.

## Problem
Which time-series database suits financial tick and order-book analysis.

## Data and period
About 25 GB of crypto exchange trades and order books collected over about one month in 2022 (about 20M trades, 33M order-book rows; sec. 4.3); random data for bulk-write tests.

## Method
Benchmark suite of ingestion, storage, read, compute-heavy and complex queries (VWAP, NBBO, order-book queries) in each database's native language; kdb+ (in-memory and on-disk), InfluxDB, TimescaleDB, ClickHouse community editions.

## Baselines and validation
Four databases compared against each other; no file-based baseline (Parquet/DuckDB); single machine, single thread, one client (sec. 7.1).

## Results (with page or section references)
- Ingestion: kdb+ fastest (47.35 MB/s from CSV, 1.6x TimescaleDB); InfluxDB 9.6x and ClickHouse 22.6x slower than kdb+ (sec. 6.1).
- Storage: InfluxDB most compact (sec. 6.6).
- Queries: kdb+ lowest latency overall; InfluxDB second, faster than kdb+ on long-window aggregations (2.7x on T-V2); TimescaleDB largest latency in most tests (sec. 6.2, 6.6).
- In-memory kdb+ 7x faster than on-disk on NBBO (sec. 6.2).

## Limits and risks to validity
One month, crypto only; single-threaded; latency is the only query metric; community editions only; kdb+ licence cost not discussed; no repeated-run statistics reported.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Systems benchmark, not a forecast |
| Baselines | 1 | Four engines; no simple file baseline |
| Point-in-time and leakage controls | N/A | Not a forecasting study |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | One month, crypto only |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code or data release found in the paper |
| **Total** | **4/14** | 2 of 8 on applicable checks, scaled to 14 (3.5, rounded) |

## Quotes worth keeping (each under 15 words, with page)
- "kdb+ has the overall best performance among the 4 databases" (sec. 7)
