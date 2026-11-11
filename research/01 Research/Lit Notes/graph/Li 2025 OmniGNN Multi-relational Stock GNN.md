---
type: lit-note
title: "Structure Over Signal: A Globalized Approach to Multi-relational GNNs for Stock Prediction"
authors: [Amber Li, Aruzhan Abil, Juno Marques Oda]
year: 2025
venue: arXiv
source_url: https://arxiv.org/abs/2510.10775
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.4]
family: [graph]
evidence: Weak
score: 4
tags: [lit-note, family/graph]
---
# Structure Over Signal: OmniGNN (Li, 2025)

**Basis:** full text (pp. 1–11) read through alphaXiv page excerpts.

**Takeaway:** A GAT–Transformer GNN with a sector "global node" beats a plain GAT and a Transformer on 10 US tech stocks (IC 0.067 vs 0.021–0.023), but the test has no non-deep baseline, no costs, no significance tests and a tiny universe, so it is an idea, not proof.

## Problem
Can a multi-relational dynamic GNN with an industry node propagate macro shocks faster than multi-hop message passing and predict next-day excess returns?

## Data and period
10 Information Technology stocks, daily, 2019-01-04 to 2022-12-15; Bloomberg and LSEG data; edges from GICS similarity, overlapping institutional holders, Capital IQ market share and ESG governance scores (pp. 3, 7).

## Method
Metapath-weighted GAT (stock–stock and stock–industry–stock paths) per daily snapshot, then a Transformer with ALiBi over snapshots; per-stock linear head predicting next-day excess return over the S&P 500 (pp. 2–6).

## Baselines and validation
Rolling windows: 6 months train, 2 validation, 2 test, advanced by the test length (p. 7). Baselines are a GAT and a Transformer only (p. 8). No random walk, linear, GBT or neighbour-average baseline.

## Results (with page or section references)
- OmniGNN IC 0.0673, IR 0.0767, cumulative return per 2-month window 0.0218, Precision@30% 0.527; GAT IC 0.0209; Transformer IC 0.0225 (Table 1, p. 8).
- COVID window (Mar–May 2020) ablation: adding the industry node raises IC from −0.0745 to −0.0465 (still negative) and IR from −0.057 to 0.082 (Table 2, p. 9).
- News sentiment comes from TextBlob, not a finance model (p. 9).

## Limits and risks to validity
_My assessment:_ 10 stocks and a 4-year window give very few independent cross-sections; Precision@K of 0.53 is near chance; no costs; edges such as current GICS codes and ESG scores are not shown to be point-in-time; hyperparameters partly missing ("x") in the text. Undergraduate summer project.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling walk-forward |
| Baselines | 0 | Only other deep models |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | 0 | Gross cumulative return only |
| Sample breadth | 1 | 10 stocks, one sector, includes COVID |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code released; data licensed |
| **Total** | **4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "a sector node acting as a global intermediary" (p. 1)
