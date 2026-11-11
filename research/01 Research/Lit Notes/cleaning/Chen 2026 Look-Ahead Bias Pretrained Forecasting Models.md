---
type: lit-note
title: Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models
authors:
- Haiqiang Chen
- Li Chen
- Yunlong Chen
- Difang Huang
- Bo Zhang
year: 2026
venue: arXiv (econ.GN)
source_url: https://arxiv.org/abs/2609.20554
doi: ''
accessed: '2026-11-08'
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]"]
research_questions: [RQ3.1, RQ4.5]
family:
- cleaning
evidence: Moderate
score: 9
tags:
- lit-note
- family/cleaning
- leakage
- model-memory
---
# Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models (Chen et al., 2026)

**Basis:** full text via alphaXiv, opened 2026-11-08 (abstract, introduction, evaluation design §3; result tables skimmed, not read in full: the text is 320k characters).

**Takeaway:** For financial time-series foundation models trained in annual vintages, models that have seen post-origin data revise forecasts materially but usually make them *worse* (higher MSFE in 18 of 20 US model-horizon cases; certainty-equivalent returns −1.77 points a year in the US, −2.14 internationally), so temporal exposure is an information-set violation, not automatic inflation.

## Problem
Does training a numeric forecaster on data after the forecast origin inflate measured accuracy and economic value, as it does for LLMs reading text?

## Data and period
Five sets of financial TSFMs, each a sequence of independently trained annual vintages under US, global and factor-augmented training data; 14 equity markets; four horizons (monthly).

## Method
Rolling comparisons vary the vintage for a fixed forecast; fixed-vintage comparisons move the target window across the training cutoff. Each exposed forecast is paired with an origin-aligned point-in-time (PIT) forecast using the same inputs and inference.

## Baselines and validation
Expanding historical-average forecast (out-of-sample R²), Diebold–Mariano style loss differentials, Clark–West statistic, HAC and block-bootstrap intervals; a constrained allocation rule for economic value.

## Results (with page or section references)
- US training: post-origin vintages raise MSFE in 18 of 20 pooled model-set–horizon cases (abstract).
- Median exposed-minus-PIT certainty-equivalent return: −1.77 points (US), −2.14 (international) (abstract).
- Global and factor-augmented training give mixed effects (abstract).
- Decomposition: a revision helps only when its error-correcting part exceeds its squared size (abstract, §3).

## Limits and risks to validity
Monthly equity-premium forecasting only; no intraday or cross-sectional stock selection. The models are the authors' own vintages, not public checkpoints. Result tables not fully read. Contrasts with Yan 2026 (DatedGPT), which found a positive look-ahead premium for a text model.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling, origin-aligned |
| Baselines | 1 | Historical average and PIT model; no tree model |
| Point-in-time and leakage controls | 2 | The subject of the paper |
| Costs and realism | 1 | Constrained allocation; costs not detailed |
| Sample breadth | 2 | 14 markets, decades |
| Statistical testing | 1 | DM/CW, HAC, bootstrap; no multiple-testing correction |
| Reproducibility | 0 | No code or data found |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Temporal exposure therefore establishes an information-set violation" (abstract)
