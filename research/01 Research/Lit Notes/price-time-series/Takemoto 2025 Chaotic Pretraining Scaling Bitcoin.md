---
type: lit-note
title: "Scaling Law for Large-Scale Pre-Training Using Chaotic Time Series and Predictability in Financial Time Series"
authors: [Yuki Takemoto]
year: 2025
venue: arXiv
source_url: https://arxiv.org/abs/2509.04921
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.13]
family: [price-time-series]
evidence: Weak
score: 2
tags: [lit-note, family/price-time-series, autoregressive, scaling, synthetic-pretraining]
---
# Scaling Law for Large-Scale Pre-Training Using Chaotic Time Series (Takemoto, 2025)

**Basis:** alphaXiv PDF pages 1–6, 9–19 (v1). HAY Co., Ltd.; preprint, "patent pending".

**Takeaway:** A small decoder transformer pretrained on 10B resampled Lorenz-system samples shows that the samples needed to reach a fixed correlation grow exponentially with horizon, loss stops improving beyond ~1M parameters, and zero-shot one-step Bitcoin signals beat a lag-1 autocorrelation rule only at ≤15-second bars, before costs.

## Problem
Can synthetic chaotic series stand in for financial training data, and does predictive horizon scale with training samples? (pp. 1–4)

## Data and period
Training: Lorenz system with perturbed parameters, resampled at intervals 100–1,000, context 512, 10B samples per horizon (§2.1, p. 6). Test: Bybit BTCUSDT perpetual futures, Jan–Feb 2025, 5–60 s bars of order flow, price change and volume; scaling coefficients fit on the first 10,000 of 100,000 sequences (§2.4, pp. 9–10).

## Method
Decoder-type transformer with causal masks and a scalar linear output head (continuous output, MSE loss); 0.1M, 1M, 10M parameter variants; single epoch on one A100 (Table 1, §2.3, p. 9).

## Baselines and validation
Only an "autocorrelation model" (last price change as predictor); top/bottom 5% long-short rule; no costs (p. 15).

## Results (with page or section references)
- Loss curves for 1M and 10M are "nearly identical"; improvement plateaus around 1M; no scaling with model parameters (pp. 13–14).
- Samples to reach correlation 0.1 rise roughly exponentially with horizon; the 1,000-unit horizon did not reach 0.1 within 10B samples (p. 14).
- Zero-shot: excess returns over the autocorrelation rule positive at 5–20 s bars (e.g. 15 s, horizon 1,000: return 0.246 vs 0.017), negative at 60 s for all horizons (Table 2, p. 17).
- Author notes that costs would make profitability "significantly more difficult" at sub-minute bars (p. 15).

## Limits and risks to validity
_My assessment:_ one asset over two months, one weak baseline, no costs or tests, continuous-output model (so not a token model). Cited only as a data point on scaling: model size saturates early; horizon reach needs exponentially more data.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Zero-shot on later data; scaling fit on first 10% |
| Baselines | 0 | Lag-1 autocorrelation rule only |
| Point-in-time and leakage controls | 1 | Scalers fit on held-back first sequences |
| Costs and realism | 0 | Ignored |
| Sample breadth | 0 | One asset, two months |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code or data |
| **Total** | **2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "no such scaling law was observed with respect to model parameters." (p. 14)
