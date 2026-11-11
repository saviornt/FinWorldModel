---
type: lit-note
title: "Improving Machine Learning Performance with Synthetic Augmentation"
authors: [Charles Dezons, Sami Sellami, Oscar Ninou, Axel Pincon, Mel Sohm]
year: 2026
venue: arXiv (preprint, UC Berkeley)
source_url: https://arxiv.org/abs/2604.14498
doi: 10.48550/arXiv.2604.14498
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.4, RQ3.5]
family: [cleaning]
evidence: Moderate
score: 8
tags: [lit-note, family/cleaning, synthetic-data]
---
# Improving Machine Learning Performance with Synthetic Augmentation (Dezons, 2026)

**Basis:** arXiv 2604.14498 full text read via alphaXiv on 2026-11-08.

**Takeaway:** Synthetic training data (bootstrap, copulas, VAE, diffusion, TimeGAN) helps only where the target has persistent structure: it improves volatility forecasts slightly (ΔR² ≈ +0.011 for linear models, ≈ 0 for random forests) and hurts daily direction prediction for every generator, with deep generators (TimeGAN, VAE) the most harmful.

## Problem
When does adding synthetic samples improve out-of-sample financial prediction, once mechanical sample-size effects are removed?

## Data and period
Daily panel of AAPL, MSFT, GOOGL, IBM, NVDA (Databento), January 2020 – January 2024, 15 OHLCV features z-scored within each training window; an options tick tape (160.3M rows) (§3).

## Method
Mixed training distribution with synthetic share α ∈ {0.25…1}; size-matched null augmentation and block permutation test; 12 generators; tasks: next-day direction, next-day 5-day volatility, volatility spike (above the in-sample 95th percentile).

## Baselines and validation
Unaugmented and null-augmented training; non-overlapping expanding walk-forward, 5 folds; all preprocessing inside the training window (§4).

## Results (with page or section references)
- Direction: baseline AUC ≈ 0.518; every generator net negative on average; TimeGAN −12.5×10⁻³, VAE −8.2×10⁻³ (§7).
- Volatility: all generator–model pairs positive vs null (p < 0.001), but vs unaugmented ΔR² ≈ +0.011 (Gaussian copula + ridge, base 0.638) and −0.001 for RF (Table 6).
- Spikes: targeted oversampling raises average precision (DDPM + XGBoost +0.125) while unconditional permutation tests penalise it (§9).
- Conclusion: synthetic data is "a stress test of whether the signal was there" (§9).

## Limits and risks to validity
Five mega-cap stocks over four years; no costs (prediction only); the large null-relative gains overstate the practical gain.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward |
| Baselines | 1 | Unaugmented and null; no HAR baseline for volatility |
| Point-in-time and leakage controls | 2 | Preprocessing inside training windows |
| Costs and realism | N/A | Prediction only |
| Sample breadth | 1 | 5 stocks, 2020–2024 (incl. 2020) |
| Statistical testing | 1 | Permutation tests; no multiple-testing correction |
| Reproducibility | 0 | No code or data link found |
| **Total** | 7/12 → 8/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Synthetic data is not a shortcut to predictive power" (§9)
