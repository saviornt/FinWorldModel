---
type: lit-note
title: "Missing Data in Asset Pricing Panels"
authors: [Joachim Freyberger, Björn Höppner, Andreas Neuhierl, Michael Weber]
year: 2025
venue: Review of Financial Studies 38(3), 760–802
source_url: https://bfi.uchicago.edu/wp-content/uploads/2023/01/BFI_WP_2022-168.pdf
doi: 10.1093/rfs/hhae003
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Moderate
score: 8
tags: [lit-note, family/cleaning, imputation]
---
# Missing Data in Asset Pricing Panels (Freyberger, 2025)

**Basis:** BFI working paper 2022-168 (December 2022) read via alphaXiv PDF query on 2026-11-08; the RFS 2025 version (pp. 760–802) was not opened.

**Takeaway:** In 82 CRSP/Compustat characteristics (1978–2021) the complete-case sample keeps only about 10% of firm-months; conditional-mean imputation (with GMM weighting) lets all firms with returns be used and gives valid inference, while unconditional mean imputation biases coefficients and shrinks standard errors. Most of the out-of-sample Sharpe gain over complete cases comes from using the full universe, not from the imputation method itself.

## Problem
How to handle missing return predictors in cross-sectional asset pricing without discarding data or biasing inference.

## Data and period
CRSP monthly + Compustat; Chen & Zimmermann (2021) characteristics; 82 covariates, 1978–2021; 2,406,042 firm-months after requiring 13 always-observed characteristics (pp. 8–10).

## Method
Conditional mean imputation from observed characteristics (optionally with the lagged value), down-weighting imputed observations in a GMM/weighted least squares framework. Assumes missingness may depend on observed but not on the missing characteristic itself (MAR, p. 4). Accounting variables lagged 6 (annual) / 4 (quarterly) months (p. 8). Imputation models estimated on the current and 59 previous months; the first 60 months imputed jointly (p. 41).

## Baselines and validation
Complete case, unconditional (cross-sectional) mean imputation; rolling 60-month estimation, one-month-ahead predictions, out-of-sample 1990–2021 (p. 42). Masking test: 1% of complete-case entries deleted and re-imputed (Table 5).

## Results (with page or section references)
- Complete case keeps 238,198 of 2,408,182 firm-months (about 10%) (p. 9).
- Masking RMSPE: unconditional mean 0.288, conditional mean 0.204, conditional mean with lags 0.177 (Table 5, p. 42).
- Linear model, 100-long/100-short: Sharpe 1.19 (complete case) vs 1.66 (unconditional mean) vs 1.79 (conditional mean) (Table 6, p. 43); nonlinear: 1.29 vs 2.44 vs 2.82. The gap between the two imputation methods is small relative to the gap from widening the universe; rankings matter, not levels (p. 44).
- Unconditional mean imputation is inconsistent unless covariates are independent or the imputed covariates have zero coefficients, and understates standard errors (p. 3).

## Limits and risks to validity
No transaction costs; the full-universe portfolios load on small, hard-to-trade stocks (mean returns of 50–90% a year are not realistic). The first 60 months are imputed jointly, a small look-ahead window. MAR assumption cannot be tested.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling 60-month window, 1990–2021 |
| Baselines | 1 | Complete case and mean imputation; no other ML imputation |
| Point-in-time and leakage controls | 1 | Reporting lags; imputation on trailing window except first 60 months |
| Costs and realism | 0 | No costs |
| Sample breadth | 2 | Full US cross-section, 1978–2021 |
| Statistical testing | 1 | GMM-based inference, no multiple-testing correction |
| Reproducibility | 1 | Public characteristic data; code not checked |
| **Total** | 8/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "thou shall not throw data away" (p. 3, quoting Zhang et al. 2005)
