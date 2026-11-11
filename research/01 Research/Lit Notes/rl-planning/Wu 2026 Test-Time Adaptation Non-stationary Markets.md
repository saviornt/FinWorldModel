---
type: lit-note
title: "Test-Time Adaptation for Non-stationary Time Series: From Synthetic Regime Shifts to Financial Markets"
authors: [Yurui Wu, Qingying Deng, Wonou Chung, Mairui Li]
year: 2026
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2602.00073
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ4.9]
family: [rl-planning]
evidence: Moderate
score: 6
tags: [lit-note, family/rl-planning, adaptation]
---
# Test-Time Adaptation for Non-stationary Markets (Wu, 2026)

**Basis:** Full PDF read through alphaXiv, pp. 1–14.

**Takeaway:** On SPY, QQQ and EUR/USD daily direction (test 2020–2025), the cheapest adaptation — refreshing batch-normalisation statistics on recent unlabeled windows — gave small, DM-significant gains, while gradient updates of normalisation parameters overfit and were significantly worse than no adaptation on SPY and QQQ; direction accuracy stayed near 50% throughout.

## Problem
When does small-footprint, causal test-time adaptation (TTA) of a frozen forecaster help under regime shift (p. 1)?

## Data and period
Synthetic shifts on ETT benchmarks; SPY, QQQ, EUR/USD daily OHLCV features; train 2000–2016, validation 2017–2019, test 2020–2025 split into pandemic, high-inflation and recovery regimes; scalers fit on training only (pp. 3–5).

## Method
Frozen TCN backbone; options: no adaptation, BN-statistics refresh, or norm-only updates of BN affine parameters by entropy + consistency (classification) or augmentation-variance + EMA-teacher (regression); quadratic drift penalty; uncertainty-triggered fallback to BN refresh at the 80th validation percentile (pp. 3–4).

## Baselines and validation
Frozen model; Diebold–Mariano tests with HAC variance; simple directional backtest with Newey–West t-stats (pp. 5–8).

## Results (with page or section references)
- Direction accuracy: SPY 0.504 / 0.498 / 0.512; QQQ 0.503 / 0.525 / 0.463; EUR/USD 0.516 / 0.520 / 0.516 for no-TTA / BN-stats / norm-only (Table 2, p. 7).
- DM: BN-stats beats no-TTA on SPY (p = 0.005) and QQQ (p = 0.022); norm-only is worse than no-TTA on SPY and QQQ (p < 0.001) (Table 3, p. 8).
- On synthetic data, norm-only helps gradual drift; structural switches defeat all variants (R² −20.8) (Table 1, p. 6).
- Authors' recommendation: BN refresh as default; norm-only only when diagnostics support it (p. 8).

## Limits and risks to validity
_My assessment:_ the EUR/USD row reports DM +4.35 as "significantly better" although positive values mean worse under the stated convention (Table 3) — an internal inconsistency; backtest tables mix return, volatility and NW-t in an unclear way; no costs, no buy-and-hold baseline; three series. The qualitative lesson (light, gradient-free adaptation is safer than gradient updates on noisy markets) agrees with [[Nguyen 2026 Volatility-Clustering Adaptation]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split; adaptation causal |
| Baselines | 1 | Frozen model only; no random walk or buy-and-hold |
| Point-in-time and leakage controls | 1 | Training-only scalers and causal augmentations, stated not checked |
| Costs and realism | 0 | None |
| Sample breadth | 1 | 3 series, 2020–2025 incl. stress |
| Statistical testing | 1 | DM + Newey–West; no multiple-testing correction |
| Reproducibility | 1 | Code on Google Drive |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "more aggressive norm-only adaptation can even hurt" (p. 1)
