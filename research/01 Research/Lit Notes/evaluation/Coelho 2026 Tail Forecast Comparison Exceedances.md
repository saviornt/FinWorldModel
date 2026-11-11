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
- forecast-comparison
title: 'Comparing tail forecasts: the number of exceedances is the sample size'
authors:
- Raphael Coelho
year: 2026
venue: arXiv (q-fin.MF) 2610.40366
source_url: https://arxiv.org/abs/2610.40366
doi: ''
research_questions:
- RQ4.2
- RQ4.3
evidence: Strong
score: 11
---
# Comparing tail forecasts: the number of exceedances is the sample size (Coelho, 2026)

**Basis:** Full text via alphaXiv (v1), read 2026-11-08: abstract, §1, Discussion, data and code statement. Proof appendix skimmed only.

**Takeaway:** When two tail forecasts (high-coverage intervals, extreme quantiles, ES) are compared with a consistent score, only exceedance days carry information, so the effective sample size is the number of exceedances; with few exceedances the Diebold–Mariano test systematically favours the less conservative forecaster, and a block bootstrap-t version or an anytime-valid confidence sequence should be used instead.

## Problem
How much data a tail-forecast comparison needs, and why DM tests mislead when exceedances are scarce (§1).

## Data and period
Theory; simulations; six online conformal methods on seven forecasting data sets at 80%–99% coverage; six (VaR, ES) models on seven stock indices in 250-day windows at 97.5% (abstract, §1, Sections 8–9).

## Method
Shows score differences are known in advance except on exceedance days (Lemma 1); lower bounds on required misses; empirical-Bernstein confidence sequence valid at all sample sizes; analysis of DM and its small-sample corrections (§1).

## Baselines and validation
DM with normal critical values, Harvey–Leybourne–Newbold and Coroneo–Iacone corrections, bootstrap-t DM, Hoeffding-type procedures (Discussion).

## Results (with page or section references)
- Required observations grow like 1/α for intervals at miscoverage α; the required number of exceedances does not (abstract).
- With scarce exceedances, DM declares the less conservative forecaster better with probability at least that of observing no exceedance, whichever is actually better (abstract, §1).
- A 250-day window at 97.5% holds about six exceedances if VaR is calibrated (§1).
- In simulations DM error in favour of the narrower interval exceeded twice nominal in every design with fewer than 25 expected misses; HLN and Coroneo–Iacone corrections did not fix it; block bootstrap-t kept error near nominal in all but the smallest design (Discussion).
- Seven stock indices, 250-day windows, 97.5%: 18.4% of significant DM results favouring the less conservative model contradict the ranking on the remaining days, vs 6.9% for those favouring the more conservative one (abstract).
- A less conservative ES can be shown worse without assumptions but never better without an assumption on the loss tail (abstract).
- Recommendations: report the number of informative rounds; no normal critical values when it is small; confidence sequences when a finite-sample, monitorable guarantee is needed, at 2–3× the rounds DM needs (Discussion).

## Limits and risks to validity
_My assessment:_ single-author preprint, not yet peer reviewed; equity application uses Yahoo Finance index closes only. Strong theory and full reproducibility package.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Rolling 250-day windows in the applications |
| Baselines | 1 | Standard DM and corrections compared |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 2 | Seven indices plus seven non-financial data sets |
| Statistical testing | 2 | Error control is the subject; anytime-valid inference |
| Reproducibility | 2 | Code and data archived (Zenodo, GitHub) |
| **Total** | 8/10 → **11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "In tail forecast comparisons the effective sample size is the number of exceedances." (Discussion)
