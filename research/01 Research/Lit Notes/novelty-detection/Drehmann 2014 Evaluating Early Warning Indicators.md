---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- novelty-detection
tags:
- lit-note
- family/novelty-detection
- early-warning
title: 'Evaluating early warning indicators of banking crises: Satisfying policy requirements'
authors:
- Mathias Drehmann
- Mikael Juselius
year: 2014
venue: International Journal of Forecasting 30(3), 759–780; BIS WP 421 (2013); draft 2012
source_url: https://www.frbsf.org/drehmann.pdf
doi: 10.1016/j.ijforecast.2013.10.002
research_questions:
- RQ4.3
- RQ4.5
evidence: Moderate
score: 7
---
# Evaluating early warning indicators of banking crises (Drehmann & Juselius, 2014)

**Basis:** August 2012 conference draft ("Improving EWIs for banking crises – satisfying policy requirements", FRBSF copy), read 2026-11-08 through a summarising page fetch; the BIS WP 421 PDF returned only its abstract page and the IJF version was not opened. Numbers below are from the draft and may differ from the published paper.

**Takeaway:** Early warning indicators should be judged by AUROC (no assumed policy loss), by timing (signal at least one year and at most five years ahead), by persistence of the signal, and with the two years after a crisis start removed; on this basis the credit-to-GDP gap and the debt service ratio reach AUROC above 0.9.

## Problem
Turning the macroprudential policy maker's needs (unknown costs, timing, stability) into statistical criteria for EWIs (abstract; draft pp. 1–2).

## Data and period
Quarterly data for 27 economies, mostly from 1980, 25 systemic banking crises (draft p. 2).

## Method
AUROC over a five-year signalling window, plus quarter-by-quarter AUROC for timing and persistence; post-crisis exclusion (draft pp. 7–9, 14–17).

## Baselines and validation
Several candidate indicators compared; AUROC 0.5 as the uninformative benchmark; confidence intervals (draft p. 7, Table 2).

## Results (with page or section references)
- AUROC preferred to noise-to-signal ratios and log scores because it does not assume a policy loss function (draft p. 2).
- Signals should come at least one year ahead and within five years, and persist rather than flip (draft p. 8).
- Signals in the two years after a crisis begins are excluded to avoid post-crisis bias (draft pp. 9, 11).
- Five-year horizon: DSR 0.91 (95% CI 0.83–0.97), credit-to-GDP gap 0.93 (0.89–0.96) (draft Table 2, p. 15).
- Published abstract: the gap is best at longer horizons and the DSR at shorter ones.

## Limits and risks to validity
_My assessment:_ evaluates indicators largely in sample over few crises (25); AUROC over long windows can look high for slow fragility gauges; read from an early draft. Pairs with [[Beutel 2019 ML vs Logit Banking Crisis Warning]] for real-time evaluation.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Indicators use one-sided (real-time) filters; no fitted-model hold-out in the part read |
| Baselines | 1 | Several indicators vs uninformative AUROC |
| Point-in-time and leakage controls | 1 | Post-crisis exclusion; one-sided gap |
| Costs and realism | N/A |  |
| Sample breadth | 2 | 27 economies, 25 crises |
| Statistical testing | 1 | AUROC confidence intervals |
| Reproducibility | 0 | No code |
| **Total** | 6/12 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- (none kept; read via summary)
