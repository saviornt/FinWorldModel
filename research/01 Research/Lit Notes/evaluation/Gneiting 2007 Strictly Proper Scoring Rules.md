---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- metrics
title: Strictly Proper Scoring Rules, Prediction, and Estimation
authors:
- Tilmann Gneiting
- Adrian E. Raftery
year: 2007
venue: Journal of the American Statistical Association 102(477), 359–378; UW Statistics TR (2004–2005)
source_url: https://apps.dtic.mil/sti/pdfs/ADA459827.pdf
doi: 10.1198/016214506000001437
research_questions:
- RQ4.3
evidence: Weak
score: 4
---
# Strictly Proper Scoring Rules, Prediction, and Estimation (Gneiting & Raftery, 2007)

**Basis:** University of Washington technical report version (DTIC copy), read 2026-11-08 through a summarising page fetch; sections cited. JASA version not opened.

**Takeaway:** Probabilistic forecasts must be scored with strictly proper rules — log score, CRPS (which reduces to absolute error for a point forecast), quantile (pinball) and interval scores — because improper scores reward dishonest or wrongly dispersed forecasts; the aim is sharpness subject to calibration.

## Problem
Which scores reward honest, well-calibrated probabilistic forecasts (§1).

## Data and period
Theory; case study of sea-level pressure ensemble forecasts in the North American Pacific Northwest (§7.1).

## Method
Characterisation of proper scoring rules on general spaces (Theorem 2.1); examples for densities, CDFs, quantiles and intervals (§2–§5).

## Baselines and validation
Proper vs improper scores on the same forecasts (§7.1).

## Results (with page or section references)
- CRPS generalises absolute error and allows direct comparison of point and probabilistic forecasts (§4.2).
- Log score is strictly proper but highly sensitive to extreme low-probability events (§4.1, §7.1).
- Interval score rewards narrow intervals and penalises misses in proportion to their distance (§5.2).
- In the weather case, improper linear and probability scores peaked at near-deterministic forecasts (r = 0.05, 0.02), contradicting the known underdispersion; proper scores peaked at r > 1 (§7.1, Table 2).

## Limits and risks to validity
_My assessment:_ foundational theory, not finance evidence; the rubric scores it low by design. Cited for which scores to use on sampled token paths and quantile outputs.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Theory |
| Baselines | 1 | Proper vs improper scores |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 0 | One weather case study |
| Statistical testing | 1 | Score comparisons |
| Reproducibility | 0 | No code |
| **Total** | 2/8 → **4/14** | Weak (foundational reference) |

## Quotes worth keeping (each under 15 words, with page)
- "Propriety is essential in scientific and operational forecast evaluation" (§1)
