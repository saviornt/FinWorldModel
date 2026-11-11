---
type: lit-note
title: "Contrastive Learning of Asset Embeddings from Financial Time Series"
authors: [Rian Dolphin, Barry Smyth, Ruihai Dong]
year: 2024
venue: arXiv
source_url: https://arxiv.org/abs/2407.18645
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.8]
family: [graph]
evidence: Moderate
score: 6
tags: [lit-note, family/graph, pretraining-objective]
---
# Dolphin 2024 Contrastive Asset Embeddings (Dolphin, Smyth & Dong, 2024)

**Takeaway:** A contrastive relation objective (pull together stocks whose returns co-move in many monthly windows more often than chance) produced embeddings that classified sectors better and chose better out-of-sample hedges than raw correlation (average hedged-pair volatility 19.1% vs 23.8%), but the best loss for one task was the worst for the other.

## Problem
Learning asset embeddings that capture relations between stocks from returns alone.

## Data and period
611 US stocks, daily returns 2000–2018, GICS sectors (§4.1). Hedging test: embeddings learned on 2000–2012, evaluated 2013–2018 (§4.3).

## Method
Co-occurrence of each pair among the top-5 most correlated in 22-day windows (stride 5); a proportions test sets positive (p < 0.05) and negative (p > 0.3) sampling distributions; three contrastive losses (individual sigmoid, aggregate sigmoid, sigmoid-softmax); 16-dimensional embeddings (§3).

## Baselines and validation
Sector classification: 5-fold CV over stocks with an SVM, against time-series classifiers and earlier embedding methods. Hedging: equal-weight two-asset portfolios using the most dissimilar asset, 100 random draws, Tukey HSD vs Pearson (§4.2–4.3).

## Results (with page or section references)
- Sector classification F1: sigmoid-softmax 0.69, individual sigmoid 0.68, best prior embedding 0.66, best classic classifier 0.53 (Table 1).
- Hedging out-of-sample volatility: individual sigmoid 19.1%, aggregate sigmoid 20.3%, Pearson 23.8%, sigmoid-softmax 26.1% (worse than Pearson) (Table 4).
- The authors conclude the best loss "may depend on the specific downstream task" (§4.3).

## Limits and risks to validity
_My assessment:_ the stock list is fixed over 2000–2018, so it holds survivors only; sector CV is across stocks, not time; no return-forecasting test; no costs. Useful as evidence that relation (contrastive) objectives encode co-movement structure, not that they improve forecasts.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One time split for hedging; sector CV not temporal |
| Baselines | 1 | Pearson and prior embeddings |
| Point-in-time and leakage controls | 0 | Survivor-only universe |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 1 | 611 US stocks, 18 years |
| Statistical testing | 1 | Tukey HSD |
| Reproducibility | 1 | Data on GitHub |
| **Total** | 5/12 → 6/14 | Moderate (borderline) |

## Quotes worth keeping (each under 15 words, with page)
- "the optimal choice of loss function may depend on the specific downstream task" (§4.3)
