---
type: lit-note
title: "Supervised Autoencoder MLP for Financial Time Series Forecasting"
authors: [Bartosz Bieganowski, Robert Ślepaczuk]
year: 2024
venue: arXiv (q-fin.TR), v2
source_url: https://arxiv.org/abs/2404.01866
doi: 10.48550/arXiv.2404.01866
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.5]
family: [cleaning]
evidence: Moderate
score: 7
tags: [lit-note, family/cleaning, labels, triple-barrier]
---
# Supervised Autoencoder MLP with Triple-Barrier Labels (Bieganowski, 2024)

**Basis:** arXiv 2404.01866v2 read via alphaXiv PDF query on 2026-11-08 (pp. 1–27).

**Takeaway:** On S&P 500, EUR/USD and BTC/USD intraday bars (walk-forward, out-of-sample 2020–April 2022), triple-barrier labels beat simple direction labels at 15- and 30-minute bars but not at 5-minute bars, and results swing strongly with barrier width and holding time; no slippage is modelled.

## Problem
Do triple-barrier labels improve a classifier-driven strategy over direction labels?

## Data and period
One-minute data aggregated to 5/15/30-minute bars; 2016 (abstract says 2010) to 30 April 2022; out-of-sample 1 January 2020 – 30 April 2022 (pp. 1–2, 18).

## Method
Four approaches: regression (1), direction classifier (2), plus supervised-autoencoder denoising (3), plus triple-barrier labels with symmetric barrier λ and a custom metric (4) (Table 4, p. 17). Walk-forward with Bayesian hyperparameter search.

## Baselines and validation
Buy-and-hold; Diebold–Mariano and information-ratio t-tests at α = 0.01 (p. 24).

## Results (with page or section references)
- Approach 4 (TBL) beats 1–3 at 15- and 30-minute bars; at 5-minute bars it is worse than Approach 3 (p. 27).
- 30-minute equal-weight portfolio: IR 1.60 vs buy-and-hold 1.11 (Table 16, p. 24).
- Information ratio rises with barrier width up to ~0.18–0.21% then falls; best holding time ~15–20 minutes (sensitivity, p. 25).
- Limits stated: no slippage; barrier exits assumed filled exactly (p. 27).

## Limits and risks to validity
Three assets; one test period; heavy tuning (barrier, noise, bottleneck) on the same out-of-sample period invites selection bias; inconsistent sample-start dates in the text.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Walk-forward |
| Baselines | 1 | Buy-and-hold and simpler labels |
| Point-in-time and leakage controls | 1 | Walk-forward; barrier sensitivity on test period |
| Costs and realism | 1 | No slippage; perfect barrier fills |
| Sample breadth | 1 | Three assets, 2020–2022 test |
| Statistical testing | 1 | DM and IR tests, no multiple-testing correction |
| Reproducibility | 0 | No code |
| **Total** | 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "triple barrier labeling may not be the best choice for high-frequency trading" (p. 27)
