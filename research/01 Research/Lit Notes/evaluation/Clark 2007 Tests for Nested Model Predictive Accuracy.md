---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- forecast-comparison
title: Approximately normal tests for equal predictive accuracy in nested models
authors:
- Todd E. Clark
- Kenneth D. West
year: 2007
venue: Journal of Econometrics 138(1), 291–311; NBER Technical WP 326 (2006)
source_url: https://www.nber.org/system/files/working_papers/t0326/t0326.pdf
doi: 10.1016/j.jeconom.2006.05.023
research_questions:
- RQ4.2
evidence: Moderate
score: 7
---
# Approximately normal tests for equal predictive accuracy in nested models (Clark & West, 2007)

**Basis:** NBER Technical Working Paper 326 (2006) PDF, read 2026-11-08 through a summarising page fetch; journal version not opened. DOI from OpenAlex lookup (see citation check).

**Takeaway:** When a larger model nests a parsimonious one (any model vs a random walk or zero forecast), the plain DM/MSPE test is badly undersized and has little power because the larger model's estimation noise inflates its MSPE; the MSPE-adjusted (Clark–West) statistic with one-sided normal critical values fixes most of this.

## Problem
Comparing a parsimonious null model with a larger nesting model by MSPE (pp. 1–2).

## Data and period
Monte Carlo over 48 settings; DGP 1 mimics weakly predictable asset returns (pp. 15–19).

## Method
Adjusted loss differential f = e1² − [e2² − (ŷ1 − ŷ2)²], regressed on a constant; one-sided t-test with critical values 1.282 (10%) or 1.645 (5%), HAC errors for multistep (pp. 4–5).

## Baselines and validation
Compared with MSPE-normal (DM), Chao–Corradi–Swanson, simulated critical values, bootstrap (pp. 15–19).

## Results (with page or section references)
- Raw MSPE differences averaged about −0.24 under the null; adjusted about 0.01–0.02 (p. 16).
- Median size at nominal 10%: MSPE-adjusted 0.080, MSPE-normal 0.008; at 5%: 0.041 vs 0.003 (p. 18).
- Power for return-like DGP 1 (R = 120, P = 360): MSPE-adjusted 0.190 vs MSPE-normal 0.031; low because predictability is small (p. 18).
- Do not use raw MSPE-normal with normal critical values for nested comparisons (p. 16).

## Limits and risks to validity
_My assessment:_ simulation evidence and asymptotics for linear nested models; guarantees less clear for multistep or heteroskedastic cases (pp. 11–12). Read via summarising fetch.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Recursive and rolling pseudo-OOS in simulations |
| Baselines | 2 | Random-walk/parsimonious null vs larger model |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 1 | 48 simulated settings |
| Statistical testing | 1 | Size and power study, no multiplicity |
| Reproducibility | 0 | No code in the part read |
| **Total** | 5/10 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- (none kept; read via summary)
