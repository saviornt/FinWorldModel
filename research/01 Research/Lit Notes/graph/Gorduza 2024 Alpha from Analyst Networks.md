---
type: lit-note
title: "Extracting Alpha from Financial Analyst Networks"
authors: [Dragos Gorduza, Yaxuan Kong, Xiaowen Dong, Stefan Zohren]
year: 2024
venue: arXiv (q-fin.CP)
source_url: https://arxiv.org/abs/2410.20597
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.4]
family: [graph]
evidence: Moderate
score: 6
tags: [lit-note, family/graph]
---
# Extracting Alpha from Financial Analyst Networks (Gorduza, 2024)

**Basis:** pp. 1–5 and 8 read through alphaXiv page excerpts (turnover section pp. 6–7 not returned).

**Takeaway:** A GAT over the shared-analyst-coverage network of 495 S&P 500 firms reports a gross long–short Sharpe of 4.07 (2006–2022), against 1.75 for a feed-forward net without the graph and 0.07 for a simple neighbour-momentum average; the size of the gap and the lack of costs make the headline doubtful.

## Problem
Can graph machine learning on the analyst co-coverage network learn momentum spillovers better than simple neighbour averages?

## Data and period
495 S&P 500 firms, CRSP/Compustat prices and IBES analyst estimates, 2006–2022. Edge weight = number of analysts covering both firms in the past 252 days, rebuilt daily (pp. 2–3).

## Method
Eight momentum and MACD features per firm; 2-layer GAT predicts whether the next-21-day return beats the cross-sectional mean; long top 25%, short bottom 25% (p. 3).

## Baselines and validation
Retrained every month: 10 daily samples train, 10 validate, test on the next (p. 4). Baselines: equal-weight market, MACD momentum, the "Analyst Matrix" (1-hop neighbour momentum average), a 2-layer feed-forward net. Ablations swap the analyst graph for correlation or GICS-industry graphs, delete 60% of edges, or use a GCN (p. 4).

## Results (with page or section references)
- Gross: market Sharpe 0.41; neighbour-momentum average 0.07; MACD 0.67; feed-forward NN 1.75; GAT on analyst graph 4.07 (29.4% a year, volatility 7.1%) (Table 2, p. 5).
- Ablations: GAT on correlation graph 3.76; on industry graph 2.25; with 60% of edges deleted 2.27; GCN 2.21 (Table 3, p. 5).
- High-attention edges are mostly cross-industry and absent from the top-decile correlation graph (p. 8).

## Limits and risks to validity
_My assessment:_ returns are gross; monthly-horizon labels sampled daily with 10-day training windows give heavily overlapping targets; a Sharpe above 4 for a monthly long–short equity strategy is far outside published anomaly evidence and calls for replication; no significance tests; the S&P 500 list is likely the current one (survivorship). The Analyst Matrix baseline is much weaker here than [[Ali 2020 Shared Analyst Coverage Momentum Spillover]] report for connected-firm momentum.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Monthly walk-forward retraining |
| Baselines | 1 | Neighbour average, NN, momentum; no GBT |
| Point-in-time and leakage controls | 1 | Trailing 252-day network; universe likely survivorship-biased |
| Costs and realism | 0 | Gross returns |
| Sample breadth | 2 | 495 firms, 2006–2022 incl. 2008 and 2020 |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code stated; licensed data |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the neighbourhood momentum indicator ... may be too weak on its own" (p. 1)
