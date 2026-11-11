---
type: lit-note
title: "DPAL: A Test-Time Adaptation Loss for Financial Time Series Forecasting"
authors: [Wuzhou Lian, Haochun Wang, Yuefan Deng]
year: 2026
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2610.14376
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.9]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, adaptation, test-time-adaptation]
---
# DPAL: Test-Time Adaptation Loss for Financial Forecasting (Lian, Wang & Deng, 2026)

**Basis:** alphaXiv full text (v1, 9 Oct 2026); setup, Tables 1–2, appendices A–B (splits, Wilcoxon test) and conclusions read. University of Michigan / Stony Brook.

**Takeaway:** Adding direction and compounded-price terms to the adaptation loss of two test-time adapters (TAFAS, PETSA) lowers reconstructed-price MSE on eight hand-picked US equity panels in 2023–2025 in most settings, under a matured-ground-truth protocol; but there is no random-walk baseline, one test window, and the frozen deep backbones it improves on are often very poor.

## Problem
Test-time adaptation objectives fit pointwise returns; financial use also needs the right sign and a price path that does not drift when returns compound (§1).

## Data and period
Eight panels built for the study: Magnificent 7, 20 S&P 500 names, 20 Russell 2000 names, sector panels (technology, consumer, energy…) and a cross-asset market-level set. Daily; train 2012-05 to 2021-11, validation to 2023-04, test 2023-04 to 2025-12 (Russell: from 2013/2022/2023) (§4.1.1, Table B.2).

## Method
DPAL = MSE + directional penalty + price-calibration loss over the first k forecast steps; plugged into TAFAS (gated calibration modules) and PETSA (low-rank calibration) without changing the frozen source model. Five backbones (PatchTST, iTransformer, DLinear, OLS, FreTS), look-back 60 days, horizons 60/90/120 days (§3, §4.1).

## Baselines and validation
Frozen backbone, original TAFAS and PETSA objectives. Adapters update only on matured windows (whole target observed before the current prediction) (§1, §4.1.2). One chronological split; coefficients fixed across settings, sensitivity checked (§4.3). Dataset-level one-sided Wilcoxon signed-rank test, Bonferroni for two frameworks (App. A.3).

## Results (with page or section references)
- DPAL lowers reconstructed-price MSE in most of the 120 dataset × backbone × horizon combinations per framework; e.g. Magnificent 7, iTransformer, H=60: frozen 1.617, TAFAS 1.137, TAFAS+DPAL 0.547 (Table 1).
- All eight dataset-level log-ratios favour DPAL in both frameworks (W⁺ = 0, p = 0.0039, survives Bonferroni) (App. A.3.1).
- Coefficients robust: the common setting is within 5% of the best MSE in 84.2% of cases (§4.3).
- Original TAFAS/PETSA sometimes do worse than the frozen model (e.g. PETSA on FreTS, Magnificent 7, H=60: 0.578 vs 0.530) (Table 2).

## Limits and risks to validity
_Authors (§5):_ limited markets and periods; simple directional and price terms.
_My assessment:_ no random-walk or persistence baseline, so it is unknown whether any adapted model beats a naive price forecast; hand-picked current constituents (survivorship); one test regime (2023–2025 bull market); metric is price MSE, no trading test; code not found.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split; matured-label adaptation |
| Baselines | 0 | Frozen and original adapters only; no random walk |
| Point-in-time and leakage controls | 1 | Matured ground truth; current-constituent tickers |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | ~130 series, one regime |
| Statistical testing | 2 | Wilcoxon with Bonferroni |
| Reproducibility | 0 | No code or data release found |
| **Total** | 5/12 → **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "a past forecast window is eligible for adaptation only when its entire target span has been observed" (§1)
