---
type: lit-note
title: "Temporal Graph Benchmark for Machine Learning on Temporal Graphs"
authors: [Shenyang Huang, Farimah Poursafaei, Jacob Danovitch, Matthias Fey, Weihua Hu, Emanuele Rossi, Jure Leskovec, Michael Bronstein, Guillaume Rabusseau, Reihaneh Rabbany]
year: 2023
venue: NeurIPS 2023 Datasets and Benchmarks
source_url: https://arxiv.org/abs/2307.01026
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.4]
family: [graph]
evidence: Moderate
score: 9
tags: [lit-note, family/graph]
---
# Temporal Graph Benchmark (Huang, 2023)

**Basis:** pp. 1–3, 6–7, 9–10, 15, 18 (v2) read through alphaXiv page excerpts. Guide seed source.

**Takeaway:** On large temporal graphs (including stablecoin and token transaction networks spanning the Terra crash), persistence and moving-average heuristics beat temporal GNNs on every node-property task, and a memorisation heuristic is competitive on transaction link prediction.

## Problem
Provide realistic, large, time-split benchmarks for temporal graph learning and test whether models beat simple heuristics.

## Data and period
Nine datasets from five domains; financial-like ones: tgbl-coin (stablecoin ERC20 transfers, Apr–Nov 2022, 22.8 M edges), tgbn-token (user–token transactions, 72.9 M edges), tgbn-trade (UN agricultural trade 1986–2016) (pp. 6–7, Table 1).

## Method
Chronological 70/15/15 splits; link prediction as ranking against many historical and random negatives (MRR); node affinity prediction scored by NDCG@10 (pp. 2, 6).

## Baselines and validation
DyRep, TGN, CAWN, TCL, GraphMixer, TGAT, NAT vs EdgeBank (memorisation), persistence and moving average; 5 runs (p. 7).

## Results (with page or section references)
- Node affinity NDCG@10 (test): tgbn-token TGN 0.169 vs moving average 0.508 and persistence 0.430; tgbn-trade TGN 0.374 vs persistence 0.855 (Table 4, p. 10).
- tgbl-coin MRR: TGN 0.586 vs EdgeBank-tw 0.580; DyRep 0.452 (Table 3, p. 9).
- Large validation-to-test gaps on long datasets point to distribution shift (p. 9).

## Limits and risks to validity
_My assessment:_ not about stock returns; transfers as evidence that temporal GNNs must be checked against persistence and moving-average baselines on time-split data. 2023 results; leaderboard models may have improved since.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Strong heuristics; no GBT |
| Point-in-time and leakage controls | 1 | Time split; streaming setting allows test-time updates |
| Costs and realism | N/A | No trading |
| Sample breadth | 2 | 9 datasets, 5 domains, incl. a crash |
| Statistical testing | 1 | Mean ± SD over 5 runs |
| Reproducibility | 2 | Code, data and leaderboard |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "simple methods often achieve superior performance compared to existing temporal graph models" (p. 1)
