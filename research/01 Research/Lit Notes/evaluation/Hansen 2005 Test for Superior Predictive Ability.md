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
- multiple-testing
title: A Test for Superior Predictive Ability
authors:
- Peter Reinhard Hansen
year: 2005
venue: Journal of Business & Economic Statistics 23(4), 365–380
source_url: https://scispace.com/pdf/a-test-for-superior-predictive-ability-1fbgz05jht.pdf
doi: 10.1198/073500105000000063
research_questions:
- RQ4.2
evidence: Moderate
score: 7
---
# A Test for Superior Predictive Ability (Hansen, 2005)

**Basis:** Journal article PDF (SciSpace open copy), read 2026-11-08 through a summarising page fetch; the text had no page numbers, so sections and tables are cited.

**Takeaway:** Hansen's SPA test keeps White's Reality Check question (does any of m alternatives beat the benchmark?) but studentises each comparison and recentres the null to ignore clearly worse models; this makes it far more powerful and stops irrelevant alternatives from hiding a real improvement.

## Problem
White's (2000) Reality Check loses power and can be manipulated by adding poor or irrelevant models (§2.3).

## Data and period
Monte Carlo (m up to 1,000, n = 200–1,000); annual US inflation forecasts, 160 quarters, rolling 32-quarter windows, random-walk benchmark (§4–§5).

## Method
Studentised max statistic; sample-dependent null that recentres alternatives with t below −√(2 log log n); stationary bootstrap (§2).

## Baselines and validation
Random-walk forecast as benchmark; RC, recentred RC and SPA variants compared (§4–§5).

## Results (with page or section references)
- In a two-model example studentisation raises 5% power from about 15% to about 53% (§2.2).
- m = 100, n = 200: power RC about 5.5%, SPAc about 99.7% (§4, Figure 4); dropping both modifications is about like discarding 84% of the sample (§4).
- SPAc slight over-rejection (~1 point) at m = 100, n = 200, gone by n = 1,000 (§4).
- Inflation: 3,304 subset regressions, SPAc p = .741 (no model beats the random walk); 352 ridge regressions, p = .048; combined 3,656 models, SPAc p = .100 vs RC p = .963 (§5, Table 6).

## Limits and risks to validity
_My assessment:_ tests only whether the benchmark is beaten, not which model is best (MCS or Romano–Wolf stepwise do that); finite-variance assumption (see [[Frederiksen 2026 Heavy Tails Predictive Ability Testing]]). Read via summarising fetch.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Rolling-window pseudo-OOS forecasts |
| Baselines | 2 | Random walk vs thousands of models |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A |  |
| Sample breadth | 1 | One macro series, simulations |
| Statistical testing | 2 | Data-snooping correction is the subject |
| Reproducibility | 0 | No code in the part read |
| **Total** | 6/12 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the RC is easy to manipulate by including irrelevant alternative models" (§2.3)
