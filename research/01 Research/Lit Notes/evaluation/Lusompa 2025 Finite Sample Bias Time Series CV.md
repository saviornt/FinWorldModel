---
type: lit-note
title: A Note on the Finite Sample Bias in Time Series Cross-Validation
authors:
- Amaze Lusompa
year: 2025
venue: arXiv (stat.ME) 2512.05900; Federal Reserve Bank of Kansas City
source_url: https://arxiv.org/abs/2512.05900
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ4.1
family:
- evaluation
evidence: Weak
score: 1
tags:
- lit-note
- family/evaluation
- cross-validation
---
# Finite Sample Bias in Time Series Cross-Validation (Lusompa, 2025)

**Basis:** Full text via alphaXiv (v1), pp. 1–7, read 2026-11-08.

**Takeaway:** Cross-validation for model selection on time series is biased in finite samples even when errors are martingale differences, because the left-out prediction and its error stay correlated through lagged regressors; the argument of Burman & Nolan (1992) and Bergmeir et al. (2018) covers only the variance term, so block CV is safer.

## Problem
Does the martingale-difference condition make CV unbiased for time series model selection?

## Data and period
None (analytical note with an AR(1) counterexample).

## Method
Decomposes the leave-one-out CV MSE and shows the cross term E[μ̃(−i)ε(i)] is generally non-zero for models with lagged dependent variables; the bias vanishes asymptotically (pp. 3–6).

## Baselines and validation
N/A.

## Results (with page or section references)
- Martingale-difference errors are not sufficient for unbiased CV in finite samples; strict exogeneity would be, and it rarely holds (pp. 5–6).
- The bias can differ across candidate models and so change which model CV selects (p. 6).
- Recommends block CV (Burman et al. 1994) or alternatives (p. 7).

## Limits and risks to validity
_My assessment:_ no simulation of how large the bias is in practice; a theoretical caution, not a measured effect. Cited as an idea.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | No empirical test |
| Baselines | 0 |  |
| Point-in-time and leakage controls | 1 | Bias mechanism analysed |
| Costs and realism | N/A |  |
| Sample breadth | 0 | No data |
| Statistical testing | 0 |  |
| Reproducibility | 0 |  |
| **Total** | 1/12 → **1/14** | Weak (theory note) |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
