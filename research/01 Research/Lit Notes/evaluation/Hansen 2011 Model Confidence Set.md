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
title: The Model Confidence Set
authors:
- Peter R. Hansen
- Asger Lunde
- James M. Nason
year: 2011
venue: Econometrica 79(2), 453–497; FRB Atlanta WP 2005-7a (2009)
source_url: https://www.atlantafed.org/-/media/documents/research/publications/wp/2005/wp0507a.pdf
doi: 10.3982/ECTA5771
research_questions:
- RQ4.2
evidence: Moderate
score: 9
---
# The Model Confidence Set (Hansen, Lunde & Nason, 2011)

**Basis:** Federal Reserve Bank of Atlanta Working Paper 2005-7a (June 2009) PDF, read 2026-11-08 through a summarising page fetch; §6 empirical results were not in the text returned; Econometrica version not opened (abstract page only).

**Takeaway:** The MCS is a set of models that contains the best model with a stated confidence, built by repeated equal-predictive-ability tests that drop the worst model until no rejection; uninformative data give a large set, which makes it the natural tool for "which of many models can we not tell apart from the best".

## Problem
Selecting among many models without assuming any is true, while controlling error over sequential tests (pp. 1–2).

## Data and period
Simulations (2,500 replications, n = 250, m = 10/40/100, block bootstrap B = 1,000); applications: Stock–Watson (1999) inflation forecasts; 25 Taylor-rule regressions (pp. 4–5, 21–23).

## Method
Equivalence test of equal expected loss over the current set; elimination rule removes the model with the largest t-statistic; statistics T_max and T_R with bootstrap p-values; MCS p-values let any α be applied afterwards (pp. 6–12).

## Baselines and validation
Random walk ("no-change") forecasts among the inflation candidates (p. 4).

## Results (with page or section references)
- Asymptotically the MCS contains all best models with probability ≥ 1 − α; with one best model it converges to that model (Theorem 1, Corollary 2, p. 7).
- Stopping at the first non-rejection avoids accumulating type I error over the sequence (p. 7).
- Simulations: coverage mostly near or above 0.90 at α = 10%, a few cells about 0.84–0.85 at m = 100; average set size falls from 9.6 to 1.5 models as model differences grow (p. 22).
- Inflation: the no-change (month) forecast never enters the MCS; Taylor rules: only regressions with the lagged funds rate survive (pp. 4–5).

## Limits and risks to validity
_My assessment:_ relies on stationary loss differentials and block bootstrap, so heavy tails (see [[Frederiksen 2026 Heavy Tails Predictive Ability Testing]]) and rare tail events ([[Bauer 2025 DM and MCS Tail Risk Finite Sample]]) weaken it. Read via summarising fetch; empirical section not seen.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Pseudo-out-of-sample inflation forecasts |
| Baselines | 2 | Random walk among many models |
| Point-in-time and leakage controls | 0 | Not addressed in the part read |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Two macro applications, simulations |
| Statistical testing | 2 | Familywise error control is the subject |
| Reproducibility | 2 | Replication files published with the journal supplement |
| **Total** | 8/12 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "it acknowledges the limitations of the data" (p. 2)
