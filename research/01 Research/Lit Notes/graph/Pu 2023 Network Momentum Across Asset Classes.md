---
type: lit-note
title: "Network Momentum across Asset Classes"
authors: [Xingyue (Stacy) Pu, Stephen Roberts, Xiaowen Dong, Stefan Zohren]
year: 2023
venue: arXiv (q-fin.PM)
source_url: https://arxiv.org/abs/2308.11294
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ1.4, RQ1.15, RQ3.7]
family: [graph]
evidence: Moderate
score: 9
tags: [lit-note, family/graph]
---
# Network Momentum across Asset Classes (Pu, 2023)

**Basis:** pp. 1–2, 6–12, 14–17, 25–26 read through alphaXiv page excerpts.

**Takeaway:** A graph learned from momentum features of 64 futures, used only to average neighbours' momentum into a linear regression, beats own-asset momentum (gross Sharpe 1.36 vs 0.95, 2000–2022), but both turn negative at 5 bps and the network strategy stays positive only up to about 3 bps.

## Problem
Does momentum spill over across assets and asset classes, and can a learned network turn that into a better trend signal?

## Data and period
64 continuous futures (commodities, equity indices, bonds, FX), Pinnacle CLC, 1990–2022; out-of-sample 2000–2022 (pp. 7, 12).

## Method
Convex graph learning (Laplacian smoothness) on stacked momentum features over 1–5-year lookbacks, ensembled and normalised; network momentum = edge-weighted neighbour average of 8 momentum features; pooled OLS predicts next-day volatility-scaled return; sign positions with volatility targeting (pp. 9–11).

## Baselines and validation
Long-only, MACD, and LinReg on the same 8 own-asset features. Expanding window retrained every 5 years; last 10% of training data for graph hyperparameters (pp. 11–12).

## Results (with page or section references)
- Gross Sharpe: GMOM 1.36 (1.51 after volatility scaling, 22% a year); LinReg 0.95 (p. 14, p. 17).
- GMOM and LinReg returns correlate about 0.65; combining both feature sets in one regression is slightly better than GMOM (p. 15).
- At 5 bps: LinReg −1.05, GMOM −0.67; GMOM positive up to 3 bps, above 0.5 up to 2 bps (p. 17).
- Network momentum shows its own reversal pattern by horizon (Table 4, pp. 25–26).

## Limits and risks to validity
_My assessment:_ daily rebalancing makes the signal cost-fragile; no significance test on Sharpe differences; the graph is learned from the same price features, so it is a co-movement graph, not an economic-link graph.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward |
| Baselines | 1 | Own-asset LinReg, MACD; no GBT |
| Point-in-time and leakage controls | 2 | Trailing-window graphs |
| Costs and realism | 1 | Cost sensitivity 0–5 bps with turnover |
| Sample breadth | 2 | 64 futures, 4 classes, incl. 2008 and 2020 |
| Statistical testing | 1 | Coefficient t-tests only |
| Reproducibility | 0 | Licensed data, no code stated |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "maintain a positive Sharpe ratio up to a cost of 3bps" (p. 17)
