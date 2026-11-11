---
type: lit-note
title: 'The Impossible Trinity of Time-Series Validation: A Conservation Law among Training Sufficiency, Test Coverage, and Temporal Causality'
authors:
- Jiayu Li
year: 2026
venue: arXiv (cs.LG) 2609.29530
source_url: https://arxiv.org/abs/2609.29530
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ4.1
family:
- evaluation
evidence: Moderate
score: 6
tags:
- lit-note
- family/evaluation
- cross-validation
---
# The Impossible Trinity of Time-Series Validation (Li, 2026)

**Basis:** Full text via alphaXiv (v1), read 2026-11-08: Sections 1–2, 5 (Table 2, 5.2, 5.3), 6 and 7.

**Takeaway:** No validation scheme can give large training sets, full test coverage and strict causality at once; expanding walk-forward is the causal frontier, purged k-fold with an embargo trades causality for distance and is cheap only when the process forgets quickly, and on pure noise shuffled 5-fold reports IC +0.32 while contiguous and purged folds report about 0.

## Problem
Why every time-series validation scheme fails one of three demands (training sufficiency, test coverage, causality), and what each failure costs.

## Data and period
Theory, plus one numerical illustration: T = 3,000 i.i.d. Gaussian returns, label = 20-day forward return (true predictability zero), four EMA features, 1-NN model, 8 seeds (§5.3).

## Method
Defines worst-fold training fraction α, coverage β, anti-causal mass Λ and margin δ; proves α + β ≤ 1 + Λ and α + min{β, δ/T} ≤ 1, with leakage bias bounded by the mixing coefficient at distance δ (Theorem 1). Places hold-out, walk-forward, k-fold (contiguous, shuffled), purged k-fold + embargo and CPCV in these coordinates (Table 2).

## Baselines and validation
Schemes compared with each other on a null where the true IC is 0.

## Results (with page or section references)
- Pure noise, reported IC: shuffled 5-fold +0.318, contiguous 5-fold +0.004, purged 5-fold (gap = H) +0.000, walk-forward (gap = H) +0.017, last-20% hold-out +0.044 with the largest standard error (§5.3).
- Spurious IC falls with distance to the nearest training point: +0.340 at gap 0, +0.040 at gap 6, about 0 from gap 16 (H = 20) (§5.3): proximity of future data, not its amount, causes leakage.
- CPCV keeps leakage controlled and turns one estimate into a distribution of paths, at the cost of smaller training sets and more compute (§5.1).
- Tuning over N configurations inflates the best result by about ς√(2 ln N); tuning must be nested, with an outer strictly causal segment untouched by selection; deflate the winner or use DSR/PBO (§5.2).
- Guidance: purged k-fold/CPCV when stationarity is credible and the goal is model comparison; expanding walk-forward when non-stationarity is feared or live performance is to be quoted; gaps sized at H + 2–3 × the dependence half-life (§6).

## Limits and risks to validity
_My assessment:_ mostly theory; the only experiment is a synthetic stationary null with one model, so it says nothing about real-data drift (which the paper says purging cannot repair). Single author, no code. Ranks schemes by leakage, not by how often they lead to false discoveries in real research.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Study of validation schemes, not a forecaster |
| Baselines | 1 | Schemes compared on a known null |
| Point-in-time and leakage controls | 2 | The subject of the paper |
| Costs and realism | N/A |  |
| Sample breadth | 0 | One synthetic stationary process |
| Statistical testing | 1 | Standard errors over 8 seeds |
| Reproducibility | 0 | No code or data released |
| **Total** | 4/10 → **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "volume is harmless, proximity is harmful" (§5.3)
