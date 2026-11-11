---
type: lit-note
title: 'Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks'
authors:
- Alessio Brini
year: 2026
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2607.05291
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ1.1
- RQ4.3
family:
- price-time-series
evidence: Strong
score: 12
tags:
- lit-note
- family/price-time-series
---
# Forecasting Realized Volatility with Time Series Foundation Models (Brini, 2026)

**Basis:** full text via alphaXiv (§1–6, §8 limitations, data availability).

**Takeaway:** Across 50 assets, only one of nine zero-shot TSFMs (TTM, <1M parameters) beats a Log-HAR benchmark on average, by about 1.3–1.8%; the econometric models stay in the Model Confidence Set.

## Problem
Whether zero-shot TSFMs improve on HAR-family models for realised volatility (§1).

## Data and period
VOLARE 5-minute realised measures: 40 US equities (2015-01-02 to 2026-01-30), 5 FX pairs and 5 futures (from Sept 2009). Balanced equity panel, so survivors only (§3).

## Method
Nine TSFMs zero-shot (Chronos-Bolt S/B, Moirai 2.0, Moirai-MoE, Lag-Llama, TimesFM 2.5, Toto, Sundial, TTM), context 1,000 days, horizons 1, 5, 22 (§4.2).

## Baselines and validation
Eight econometric models (HAR, Log-HAR, HAR-J, HAR-RS, HARQ, ARFIMA, ARMA, MEM) re-estimated at every rolling origin (§4.1.2). QLIKE and MSE; DM tests, MCS, Mincer–Zarnowitz, Giacomini–Rossi; Benjamini–Hochberg check on DM win rates (§6, fn. 10). Pretraining contamination assessed in §4.3 (Table 3).

## Results (with page or section references)
- Pooled losses favour TSFMs, but this is driven by a few outlier assets (Abstract; §1).
- Equal-weighted loss ratios: only TTM beats Log-HAR at every horizon, margin about 1.3–1.8% (§1, p. 3).
- Equities, QLIKE at h = 22: TTM 0.521, Log-HAR 0.538, TimesFM-2.5 0.724, Chronos-Bolt-S 0.710 (Table 4, p. 15).
- Mincer–Zarnowitz recalibration: short-horizon edge is mostly better scaling; a real informational gain remains only at the monthly horizon (Abstract).
- Equal-weight average of TTM and Log-HAR enters the MCS for 98–100% of assets (Abstract).
- Choice of TSFM architecture matters more than TSFM versus econometric (Abstract).

## Limits and risks to validity
Zero-shot only; point forecasts only; undisclosed pretraining corpora for three models (§8). _My assessment:_ survivor-only equity panel; VOLARE data are licensed. Strong design overall.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling origins, econometric models refit each origin |
| Baselines | 2 | Full HAR family, ARFIMA, MEM |
| Point-in-time and leakage controls | 1 | Contamination assessed but cannot be ruled out |
| Costs and realism | N/A | No trading claims |
| Sample breadth | 2 | 50 assets, 3 asset classes, includes 2020 |
| Statistical testing | 2 | DM, MCS, BH correction |
| Reproducibility | 1 | Code public; data licensed |
| **Total** | **10/12 → 12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "Foundation models do not deliver a uniform gain." (Abstract, p. 1)
