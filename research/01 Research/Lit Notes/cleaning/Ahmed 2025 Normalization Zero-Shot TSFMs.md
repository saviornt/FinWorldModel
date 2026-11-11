---
type: lit-note
title: "A Comparative Study on How Data Normalization Affects Zero-Shot Generalization in Time Series Foundation Models"
authors: [Ihab Ahmed, Denis Krompaß, Cheng Feng, Volker Tresp]
year: 2025
venue: arXiv
source_url: https://arxiv.org/abs/2512.02833
doi: 10.48550/arXiv.2512.02833
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6]
family: [cleaning]
evidence: Weak
score: 5
tags: [lit-note, family/cleaning, normalisation, foundation-model]
---
# Normalization and Zero-Shot Generalization in TSFMs (Ahmed, 2025)

**Basis:** arXiv 2512.02833v2 full PDF (pp. 1–5) read via alphaXiv on 2026-11-08.

**Takeaway:** Pretraining four small time-series foundation models seven ways, mean/standard-deviation normalisation (instance RevIN, dataset standardisation or both) cut zero-shot MASE by about 89% versus raw inputs and about 44% versus min-max, max-abs and mean-abs; for the token-based Chronos, any normalisation helped and the choice among them barely mattered.

## Problem
Which input normalisation helps foundation models generalise to unseen domains?

## Data and period
Weather, Electricity, ETTh/ETTm, Traffic, Turkey Power (Table 2, p. 3); leave-one-dataset-out zero-shot tests. No financial data.

## Method
Moirai, Chronos, GTT, LightGTS (smallest sizes), each pretrained with RevIN, MeanAbs, Hybrid (standardise → RevIN), Standardisation, MinMax, MaxAbs and raw; at inference only context-window statistics are used (pp. 2–3).

## Baselines and validation
Raw inputs; three leave-one-out runs; MASE mean ± s.d. No significance tests.

## Results (with page or section references)
- Average zero-shot MASE: RevIN 1.02, Hybrid 1.05, Standardisation 1.06, MinMax 1.22, MeanAbs 1.79, MaxAbs 2.58, raw 9.38 (Table 3, p. 4).
- Chronos (cross-entropy on tokens): choice among methods varied by ±0.07 MASE (p. 4).
- Clipping normalised horizon values for scale-sensitive losses cut MASE 16.5–36.4% (Table 4, p. 4).

## Limits and risks to validity
Smallest model variants; non-financial data; no tests; no code.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Leave-one-dataset-out |
| Baselines | 1 | Raw and alternatives |
| Point-in-time and leakage controls | 1 | Context-only statistics at inference |
| Costs and realism | N/A | |
| Sample breadth | 1 | Seven non-financial datasets |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code |
| **Total** | 4/12 → 5/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
