---
type: lit-note
title: "(Mis)Understanding Benign Overfitting in Equity Return Prediction"
authors: [Hui Guo, Jiawei Huang, Runze Li, Yan Yu]
year: 2026
venue: arXiv (stat.ML) 2608.23761
source_url: https://arxiv.org/abs/2608.23761
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.4]
family: [evaluation]
evidence: Strong
score: 11
tags: [lit-note, family/evaluation, training, regularisation, negative-result]
---
# (Mis)Understanding Benign Overfitting in Equity Return Prediction (Guo et al., 2026)

**Basis:** Full text (pp. 1–6, 12–15, 21–27, 33, 35) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** Re-running the "virtue of complexity" random-Fourier-feature ridge models on market returns, the optimally (cross-validated) regularised model shrinks to the historical average, ridgeless models give slightly negative R²oos, and any alpha vanishes once the historical-average portfolio is controlled for: when the signal is weak, the best-regularised large model is the simplest forecast.

## Problem
Whether benign overfitting and double descent imply that bigger models extract more return signal ("virtue of complexity", Kelly, Malamud & Zhou 2024) (§1).

## Data and period
US equity market excess returns, monthly, 1931–2020 (sub-periods 1931–1974, 1975–2020); 15 Goyal–Welch predictors expanded into up to 12,000 random Fourier features; rolling 12-, 60- and 120-month windows plus an expanding window (§3, Tables 1, A1, A2).

## Method
Ridge and ridgeless regression on RFFs with an unpenalised intercept; theory under the null of zero slopes (optimal penalty diverges, model collapses to the intercept); ridge penalty chosen by one-step rolling CV inside each training window; forecasts averaged over 100 RFF draws (§2, §3.2).

## Baselines and validation
Historical average (intercept-only), linear model on the 15 predictors, buy-and-hold market; R²oos (Campbell–Thompson), Sharpe, CAPM alpha and alpha controlling for the historical-average portfolio; Newey–West t-statistics; block bootstrap with resampled covariates pooled across window lengths (§3.1, §3.4–3.5).

## Results (with page or section references)
- Ridgeless RFF R²oos −0.02 (1931–1974), −0.01 (1975–2020), −0.01 (full); correlation with the historical-average portfolio 0.82–0.91 (p. 13, Table 1).
- CAPM alpha t = 3.59 (Panel A) falls to 1.49 once the historical-average portfolio is added; at KMZ's preferred z = 10³, controlled t = 1.32, 0.04, 1.16 (pp. 13–15).
- Cross-validation picks the maximum penalty 10⁹ in 47.68% of months (12-month window); 44.26% and 41.79% for 60 and 120 months (p. 15).
- Pooled bootstrap: the actual t(α₂) = 1.90 sits at the 62nd percentile of the null distribution (p. 21).
- KMZ's results come from a no-intercept, non-centred specification; with centred predictors the timing power vanishes (§3.6, p. 23).

## Limits and risks to validity
_My assessment:_ aggregate market timing at monthly frequency, not cross-sectional or high-frequency; theory assumes i.i.d. errors (footnote 2). Directly relevant to RQ4.4: tune regularisation causally inside each window, benchmark against the shrinkage target, and read double-descent curves as shrinkage, not signal. Part of an ongoing debate (Kelly & Malamud 2025 reply not opened).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling windows, causal CV per origin |
| Baselines | 2 | Historical average, linear model, market |
| Point-in-time and leakage controls | 2 | Penalty from training data only; flags KMZ full-sample z |
| Costs and realism | 0 | Market-timing Sharpe without costs |
| Sample breadth | 1 | One asset, many regimes (1931–2020) |
| Statistical testing | 2 | Newey–West; pooled bootstrap across window choices |
| Reproducibility | 2 | Code on GitHub; public predictors |
| **Total** | **11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "no model can identify a signal that does not exist in the data" (p. 4)
