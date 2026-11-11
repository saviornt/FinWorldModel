---
type: lit-note
title: A note on the validity of cross-validation for evaluating autoregressive time series prediction
authors:
- Christoph Bergmeir
- Rob J Hyndman
- Bonsoo Koo
year: 2018
venue: Computational Statistics & Data Analysis 120, 70–83
source_url: https://robjhyndman.com/papers/cv-wp.pdf
doi: 10.1016/j.csda.2017.11.003
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
# Validity of Cross-Validation for Autoregressive Prediction (Bergmeir, Hyndman & Koo, 2018)

**Basis:** Authors' preprint (submitted to Elsevier July 2017) read through a summarising page fetch on 2026-11-08; journal version and page numbers not opened.

**Takeaway:** For purely autoregressive models whose errors are uncorrelated, standard k-fold cross-validation is valid and estimates error more precisely than a single out-of-sample split (MAPAE about 0.09 vs 0.16 on AR(3) data), but it under-estimates error when the model is underfitted and its residuals are serially correlated.

## Problem
Is ordinary k-fold CV valid for time series models?

## Data and period
Monte Carlo: 1,000 trials of length-200 series (140 in, 60 out) from AR(3), MA(1) and seasonal AR(12) processes; yearly sunspot data as an example.

## Method
Proof of CV consistency for purely autoregressive models with martingale-difference errors; simulations compare 5-fold CV, non-dependent CV and a last-block out-of-sample estimate for AR(1)–AR(5) and an MLP.

## Baselines and validation
Out-of-sample (last block) estimate.

## Results (with page or section references)
- AR(3) DGP: 5-fold CV error of the error estimate about 0.09 vs 0.16 for out-of-sample.
- MA(1) DGP: about 0.10–0.11 vs 0.17–0.19.
- Seasonal AR(12) (models underfitted): CV's advantage nearly disappears and CV is more biased than out-of-sample.
- Non-dependent CV (removing neighbours) did poorly because it throws away too much training data.
- Advice: check residual autocorrelation (e.g. Ljung–Box) before trusting CV.

## Limits and risks to validity
_My assessment:_ stationary, correctly specified, short series; no overlapping labels, no non-stationarity, no selection among many models. Lusompa (2025) argues the unbiasedness claim does not hold in finite samples even with martingale-difference errors. Cerqueira et al. (2020) find the result does not carry to non-stationary real series.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Estimates compared with a true out-set loss |
| Baselines | 1 | CV variants vs out-of-sample |
| Point-in-time and leakage controls | 1 | Dependence handled analytically; no purging |
| Costs and realism | N/A |  |
| Sample breadth | 0 | Synthetic AR/MA series plus sunspots |
| Statistical testing | N/A | Simulation averages |
| Reproducibility | 0 | Not stated in the version read |
| **Total** | 4/10 → **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None kept (read through a summary).

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
