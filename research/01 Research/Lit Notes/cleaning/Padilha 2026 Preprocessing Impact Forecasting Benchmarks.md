---
type: lit-note
title: "Are We Really Benchmarking Forecasting Models? The Impact of Preprocessing on Time Series Performance"
authors: [Guilherme Afonso Galindo Padilha, Paulo S. G. de Mattos Neto, Rafael M. O. Cruz]
year: 2026
venue: arXiv (under review, ICLR 2027)
source_url: https://arxiv.org/abs/2610.09096
doi: 10.48550/arXiv.2610.09096
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6]
family: [cleaning]
evidence: Moderate
score: 9
tags: [lit-note, family/cleaning, normalisation, preprocessing]
---
# Are We Really Benchmarking Forecasting Models? (Padilha, 2026)

**Basis:** arXiv 2610.09096v2 PDF pages 1–2, 5–8, 13, 17, 20, 22 read via alphaXiv on 2026-11-08.

**Takeaway:** Across 11 models × 16 reversible pipelines (Box-Cox, differencing, seasonal differencing, z-score; all fitted on training windows only) on ~29,000 M4 series, choosing preprocessing per series improves MASE by about 27–87%, and changes model rankings; models without built-in normalisation (linear regression, XGBoost, MLP, Informer) gain most, mainly from first differencing.

## Problem
Do fixed preprocessing choices in benchmarks bias model comparisons?

## Data and period
M4 quarterly, weekly, daily and hourly subsets (~29,000 series, mixed domains incl. finance); M4 standard horizons (Table 2, p. 5).

## Method
Grid of variance stabilisation × unit-root differencing × seasonal differencing × z-score (16 pipelines); transformation parameters fitted on training windows only (p. 5). Models: ETS, ARIMA, Theta, linear regression, XGBoost, MLP, N-BEATS, TimesNet, PatchTST, Informer, Chronos-2 Synth (synthetic-only pretraining to avoid M4 contamination) (p. 6). Hyperparameters fixed.

## Baselines and validation
Statistical baselines (ETS, ARIMA, Theta); MASE scaled by the naive forecast; single M4 hold-out.

## Results (with page or section references)
- Raw MLP MASE 31.9 vs 3.1 differenced; Informer 106.8 raw vs 3.1 differenced (Table 3, p. 7).
- Stacked transforms (Box-Cox + differencing + seasonal differencing) can explode errors when the inverse transform amplifies noise (p. 6).
- Oracle per-series choice: models with internal normalisation gain ~35–55%, four of five without gain >50%, MLP and Informer >75% (p. 7).
- Under z-score only, models with built-in normalisation rank best; under oracle pipelines rankings shift (Table 4, p. 8).

## Limits and risks to validity
Univariate, fixed hyperparameters, no learned normalisation; oracle selection uses the test set (an upper bound, not a usable method); not finance-specific; no significance tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | M4 hold-out |
| Baselines | 2 | Naive-scaled MASE, ETS/ARIMA/Theta, XGBoost |
| Point-in-time and leakage controls | 2 | Transform parameters fitted on training windows only |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | Many series, not financial panels or stress periods |
| Statistical testing | 0 | Mean ranks only |
| Reproducibility | 2 | Code and data released |
| **Total** | 8/12 → 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Optimizing preprocessing per series yields gains of approximately 27% to 87%" (p. 1)
