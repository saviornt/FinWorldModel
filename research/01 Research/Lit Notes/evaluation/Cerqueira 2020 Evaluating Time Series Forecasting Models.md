---
type: lit-note
title: 'Evaluating time series forecasting models: An empirical study on performance estimation methods'
authors:
- Vitor Cerqueira
- Luis Torgo
- Igor Mozetič
year: 2020
venue: Machine Learning 109 (2020); arXiv 1905.11744
source_url: https://arxiv.org/abs/1905.11744
doi: 10.1007/s10994-020-05910-7
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ4.1
family:
- evaluation
evidence: Moderate
score: 9
tags:
- lit-note
- family/evaluation
- cross-validation
---
# Evaluating Time Series Forecasting Models (Cerqueira, Torgo & Mozetič, 2020)

**Basis:** Full text via alphaXiv (arXiv v1, 2019), pp. 1–24, read 2026-11-08. Journal version (Machine Learning) not opened; DOI not recorded.

**Takeaway:** On 62 real-world series, out-of-sample methods that keep time order (repeated hold-out, hold-out) estimated true future error best, and cross-validation variants were optimistic; on stationary series cross-validation was competitive, on non-stationary ones it was among the worst.

## Problem
Which performance-estimation method best approximates the error a forecaster will incur on future data?

## Data and period
62 real-world univariate series (half-hourly to daily, several domains, 31 stationary, 31 not by a wavelet test) and three synthetic stationary processes of 200 points (§3.2, pp. 9–13).

## Method
Each series split into an estimation set (first 70%) and a later validation set (30%) that gives the true loss; 11 estimators compared: CV, blocked CV, modified CV, hv-blocked CV, hold-out, repeated hold-out, and five prequential variants (§3.4, pp. 13–14).

## Baselines and validation
Estimators compared against the true later loss; Bayes sign test with a ±2.5% region of practical equivalence (p. 18).

## Results (with page or section references)
- Synthetic stationary data: CV variants and prequential blocks estimate well; matches Bergmeir et al. (pp. 16–17).
- Real series: repeated hold-out and hold-out rank best; blocked CV best among CV variants (Fig. 13, p. 18).
- CV variants tend to under-estimate error (optimistic); out-of-sample and prequential methods over-estimate it (Fig. 14, p. 18).
- Stationary subset: plain CV best, then repeated hold-out; non-stationary subset: hold-out and repeated hold-out best, CV among the worst (Figs 16–17, pp. 19–20).
- Varying series length from 100 to 3,000 had no noticeable effect (p. 23).

## Limits and risks to validity
_My assessment:_ not financial data and one-step-ahead univariate autoregression only; judged by estimation accuracy, not by false discoveries or selection among many models. No purging or embargo variants beyond hv-blocking. Transfers to finance as a mechanism (non-stationarity favours time-ordered evaluation).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Estimates checked against a later untouched period |
| Baselines | 1 | Eleven estimators compared; no external baseline needed |
| Point-in-time and leakage controls | 1 | Time order and gaps studied, no purging of labels |
| Costs and realism | N/A |  |
| Sample breadth | 1 | 62 series, several domains, not financial |
| Statistical testing | 1 | Bayes sign test |
| Reproducibility | 2 | Code and data on GitHub |
| **Total** | 8/12 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the most accurate estimates are produced by out-of-sample methods" (p. 1)

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
