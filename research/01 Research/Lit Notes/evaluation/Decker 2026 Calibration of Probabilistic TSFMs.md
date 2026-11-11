---
type: lit-note
title: "Evaluating Uncertainty Calibration in Probabilistic Time Series Foundation Models"
authors: [Thomas Decker, Volker Tresp]
year: 2026
venue: NeurIPS 2026 (Evaluations and Datasets)
source_url: https://arxiv.org/abs/2611.03592
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.13, RQ1.6]
family: [evaluation]
evidence: Moderate
score: 7
tags: [lit-note, family/evaluation, calibration, foundation-models]
---
# Evaluating Uncertainty Calibration in Probabilistic TSFMs (Decker, 2026)

**Basis:** alphaXiv PDF pages 1, 4–5, 8, 10–11, 18, 22, 27–28 (v1). Siemens AG, LMU Munich.

**Takeaway:** Across 14 zero-shot TSFMs on 55 GIFT-Eval configurations, the token-based, autoregressively sampled Chronos-T5 and the flow-matching Sundial are the worst calibrated (pooled error ~2× parametric and quantile-head models), stay badly miscalibrated in the tails, and miscalibration grows with horizon; post-hoc recalibration fixes average coverage but not conditional errors.

## Problem
How well calibrated are TSFM probabilistic forecasts, and does that depend on how uncertainty is represented? (p. 1)

## Data and period
GIFT-Eval short-term task, 55 dataset configurations (energy, traffic, weather, finance, health, sales, cloud); 42 with ≥50 windows for recalibration; medium/long tasks for horizon analysis (App. B.2, p. 18).

## Method
Taxonomy: (1) parametric density, (2) discretized distribution (Chronos-T5: autoregressive categorical sampling over 4,096 bins), (3) direct quantile, (4) implicit generative (Table 1, p. 5). Metrics: pooled, horizon-averaged and quantile-conditioned calibration errors at τ = 0.1…0.9; 100 sample paths for sampling models (App. B.1, p. 18).

## Baselines and validation
14 TSFMs compared on the same windows; isotonic, KDE and Platt-style recalibration fitted on earlier windows (chronological split) (p. 10). Significance tests for the horizon and conditioning gaps.

## Results (with page or section references)
- PCE_pool: Chronos-T5-Base 0.1024, Small 0.1035, Sundial 0.1467 vs Moirai-Large 0.0484, TiRex 0.0502, Chronos-Bolt-Base 0.0505, Chronos-2 0.0641 (Table 2, p. 8).
- Sundial's nominal 80% interval covers only 40% of outcomes (p. 8).
- Tails: at τ=0.01 Chronos-T5 and Sundial coverage errors exceed ten times the nominal tail probability (0.133 and 0.154) vs 0.010 for Moirai-Base and Chronos-2 (Table 13, p. 27). Not a Monte Carlo artefact (stable from S≈100) (p. 27).
- Horizon: worst-horizon error more than doubles from short to long tasks (PCE_max 0.130 → 0.297) (Table 15, p. 28).
- Recalibration cuts Chronos-T5 PCE_pool by ~60% but QCE_avg by only ~31% (Table 3, p. 10).

## Limits and risks to validity
_Authors:_ horizon-wise marginal calibration only; no joint (path) calibration; simple recalibrators (p. 10).
_My assessment:_ few finance series; no stress-period split. The Chronos-T5 result is the clearest evidence that sampled token paths, as implemented there, are poorly calibrated, but the cause (binning vs sampling vs training) is not isolated.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Zero-shot; chronological recalibration split |
| Baselines | 1 | 14 TSFMs; no classical density models |
| Point-in-time and leakage controls | N/A | Not a market study |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 55 configurations, little finance |
| Statistical testing | 1 | Resampling tests per pair; no multiple-testing correction |
| Reproducibility | 1 | Code released |
| **Total** | **5/10 → 7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Sundial's nominal 80% interval, for instance, covers only 40% of the outcomes." (p. 8)
