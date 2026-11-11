---
type: lit-note
title: An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts
authors:
- Sotirios D. Nikolopoulos
year: 2025
venue: arXiv (stat.ME)
source_url: https://arxiv.org/abs/2512.00916
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ1.8
- RQ4.3
- RQ3.5
family:
- evaluation
evidence: Weak
score: 5
tags:
- lit-note
- family/evaluation
---
# An Imbalance-Robust Evaluation Framework for Extreme Risk Forecasts (Nikolopoulos, 2025)

**Basis:** arXiv v1 (30 Nov 2025) read through alphaXiv page excerpts (pp. 1–3, 5–6, 9–11, 14–15, 19).

**Takeaway:** As event prevalence falls, F1, MCC and accuracy push their optimal alarm thresholds to the boundaries (towards "never alarm") and AUC saturates near 1, so model rankings are driven by prevalence rather than tail skill; the paper proposes "rare-event-stable" metrics with a fixed false-positive/false-negative tolerance α that keep thresholds interior, shown in simulation (π down to 10⁻⁶) and on one credit-default dataset.

## Problem
Standard classification metrics behave inconsistently as rare-event prevalence declines (p. 1).

## Data and period
Simulations with prevalence 10⁻² to 10⁻⁶, 2,000 replications, two signal strengths (AUC ≈ 0.90 and > 0.99) (pp. 10–11). One consumer credit-default dataset; LightGBM on a 70/30 split; prevalence down-sampled from 6.64% to 0.1% (p. 14).

## Method
Decision-theoretic analysis of the threshold each metric implies; RES metrics are those whose penalty ratio B(π)/A(π) stays finite as π → 0 (pp. 6, 9). Bootstrap (500) of optimal thresholds (p. 14).

## Baselines and validation
Compares F1, MCC, balanced accuracy, AUC and RES metrics on the same fixed forecasts (pp. 11, 14).

## Results (with page or section references)
- Simulation, moderate signal: F1-optimal threshold ranges 0.552–0.992 and MCC 0.532–0.992 across prevalence; AUC range 0.996–1.000 for strong signal (Table 1, p. 11); all drifts significant (p < 0.001) (Table 2, p. 11).
- Credit data: F1 threshold range 0.55, MCC 0.64 across prevalence regimes (Table 5, p. 15); RES metrics give stable 4–9% default cutoffs (abstract, p. 1).
- MCC drives towards a never-alarm rule as π → 0 (p. 10).
- Recommends pairing a tail-weighted proper scoring rule (model choice) with an RES metric (alarm threshold) (p. 19).

## Limits and risks to validity
_My assessment:_ single author, one real dataset (not market shocks), no out-of-sample test of whether RES-chosen alarms give better outcomes. Cited for the evaluation idea (fix the cost ratio α in advance; do not judge shock detectors by F1/AUC alone), which bears on RQ4.3.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One 70/30 split |
| Baselines | 1 | Compared with standard metrics |
| Point-in-time and leakage controls | N/A | Metric study |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 0 | Simulation plus one credit dataset |
| Statistical testing | 1 | Spearman tests, bootstrap |
| Reproducibility | 0 | Code not noted in pages read |
| **Total** | **3/8 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "standard metrics collapse as event prevalence declines" (p. 1)
