---
type: lit-note
title: "ACT-Tensor: Tensor Completion Framework for Financial Dataset Imputation"
authors: [Junyi Mo, Jiayu Li, Duo Zhang, Elynn Chen]
year: 2025
venue: ACM ICAIF 2025; arXiv 2508.01861
source_url: https://arxiv.org/abs/2508.01861
doi: 10.1145/3768292.3770408
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Weak
score: 3
tags: [lit-note, family/cleaning, imputation, leakage]
---
# ACT-Tensor: Tensor Completion for Financial Dataset Imputation (Mo, 2025)

**Basis:** arXiv 2508.01861 full text read via alphaXiv on 2026-11-08.

**Takeaway:** A cluster-based tensor completion with a centred moving-average smoother beats Bryzgalova-style baselines on masked entries and doubles the long-short Sharpe ratio of the resulting factors, but the smoother averages future values and the panel is completed on the whole sample, so the asset-pricing gains are not look-ahead-free: an example of how an imputation method can manufacture performance.

## Problem
Impute a sparse firm × characteristic × time tensor.

## Data and period
CRSP/Compustat monthly, 22,630 US stocks, January 2016 – December 2020, 45 characteristics ranked to [−0.5, 0.5]; about 83% of entries missing; delisted stocks dropped (§5.1).

## Method
CP tensor completion per firm cluster, then temporal smoothing by centred moving average (window centred on t, so it uses t+1…t+m), EMA or Kalman filter (§3.3). Asset-pricing test with factors from double-sorted portfolios.

## Baselines and validation
Cross-sectional median, Global BF-XS and Local B-XS from [[Bryzgalova 2025 Missing Financial Data]]; 10% of observed cells masked under MAR, block and logit patterns.

## Results (with page or section references)
- Logit masking imputation R²: 0.88 (CMA) vs 0.46 (best baseline) (Table 2).
- Asset pricing: T–B Sharpe 1.13–1.32 vs 0.71–0.73 for B-XS/BF-XS (Table 3).
- CMA smoother best of the three; the causal EMA and Kalman variants are close in Sharpe (1.09–1.32).

## Limits and risks to validity
Centred smoothing and full-panel completion leak future information; dropping delisted stocks adds survivorship; five years only; no costs; no significance tests. The comparison with the look-ahead-free Local B-XS is therefore not like for like.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Masked cells only |
| Baselines | 1 | Strong imputation baselines |
| Point-in-time and leakage controls | 0 | Centred smoother; whole-panel fit; delisted dropped |
| Costs and realism | 0 | Sharpe without costs |
| Sample breadth | 1 | 2016–2020 only |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code found |
| **Total** | 3/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "Roughly 83% of the firm-characteristic entries are missing" (§5.1)
