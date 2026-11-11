---
type: lit-note
title: "Towards Financial World Modeling"
authors: [Humzah Merchant, Alec Guthrie, Simon Mahns, Randall Balestriero, Bradford Levy]
year: 2026
venue: "NeurIPS 2026 (arXiv cs.LG)"
source_url: https://arxiv.org/abs/2610.09048
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.15, RQ1.13, RQ1.1]
family: [price-time-series]
evidence: Strong
score: 12
tags: [lit-note, family/price-time-series, world-model]
---
# Towards Financial World Modeling (Merchant et al., 2026)

**Basis:** arXiv v2 (13 Oct 2026), pp. 1–10, 17–23 (Tables 2–5, Figs. 2, 5–7), via the alphaXiv PDF reader.

**Takeaway:** On Market-1T (1 Hz quotes and trades for all US-listed equities, 2008–2025), 18 encoders were compared as candidate "state representations" for a financial world model across 32 sampled months: a supervised multihead encoder gave the best 15-minute rank IC for returns (0.031) and volatility change (0.094), above Chronos-2, TimesFM 3.0, Kronos (0.017 return IC) and classical baselines, but most self-supervised objectives barely beat an untrained random ViT, the month explained 97–99.9% of the variance in results, and predictive skill was unrelated to how well a representation organises market structure (ρ = −0.19).

## Problem
What should the state layer of a financial world model preserve, and how should it be evaluated (pp. 1–3)?

## Data and period
Market-1T: ~1 trillion one-second aggregates of NBBO and trades, all US-traded equities 2008–2025, 11 features per observation (bid/ask price and size, OHLC, VWAP, volume, trade count). Benchmark universe recomputed monthly from the prior month only (common stock, VWAP > $5, ADV ≥ $20M, active > 20% of seconds), avoiding survivorship (pp. 4–5, 17).

## Method
ViT-S encoders trained with a supervised pairwise ranking loss (return, volatility, spread, multihead) or 14 self-supervised objectives (LeJEPA with five augmentations incl. cross-stock same-time views, DINO, BYOL, CPC, I-JEPA, MAE, TS2Vec, CoST, TF-C, TimeMAE); ridge probes on frozen embeddings; latent-structure probes (day, firm, industry clustering; factor-loading decoding) (pp. 3, 5–9, 18–19).

## Baselines and validation
Each of 32 evaluation months uses only the preceding six months for training; hyperparameters tuned on five separate months; 2-SE error bars adjusted for month variance. Baselines: mean reversion, AR, ARMA, HAR-RV, GARCH(1,1), ridge ARDL, ridge and GBM on the raw view, frozen Chronos-2, Kronos, TimesFM 3.0, and an untrained random ViT (pp. 5–7, 18, 21, Table 4).

## Results (with page or section references)
- 15-min rank IC (return / volatility / spread): multihead 0.0311 / 0.0941 / 0.2455; random ViT 0.0170 / 0.0694 / 0.1692; best LeJEPA (time warping) 0.0204 / 0.0721 / 0.1691; cross-stock augmentation 0.0169 / 0.0693 / 0.1667 (p. 6, Table 2).
- Baselines: AR(p) 0.0136 return; GARCH 0.0468 and HAR-RV 0.0639 volatility; GBM 0.0097 return; Chronos-2 0.0230 / 0.0928 / 0.1289; TimesFM 3.0 0.0232 / 0.0947 / 0.1362; Kronos 0.0171 / 0.0621 / 0.0560 (p. 21, Table 4).
- Month explains 97.2%, 98.9% and 99.9% of result variation (seed the rest) (p. 6, Fig. 5); rank IC swings widely across 2008–2025 (p. 2, Fig. 2).
- At fixed compute, ViT-Tiny (5.4M) beats ViT-Base (86M) on every task (p. 7, Fig. 6).
- Decay: return representations persist; volatility and spread skill fall by ~20% and ~10% of base IC over five years (p. 9, Fig. 7).
- Augmentation shapes the state: same-stock views cluster by firm (memorising bid/ask size), cross-stock views capture market-wide movement but do not raise predictive IC (pp. 3, 8–10, Table 3).
- Forecasting rank and organisation rank are unrelated (ρ = −0.19) (p. 10, Fig. 8).

## Limits and risks to validity
_My assessment:_ the "state" here is per-stock market microstructure only; no macro, text, graph or event inputs are tested, so it says nothing directly about whether broader world state helps. Horizon is 15 minutes; IC is the main metric (portfolio Sharpe explored over 2,448 implementations, p. 6, and Appendix D). TSFMs were not retrained per month. No multiple-testing correction across 18 encoders.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | 32 months, each trained on preceding 6 months only |
| Baselines | 2 | AR, GARCH, HAR, GBM, TSFMs, random encoder |
| Point-in-time and leakage controls | 2 | Monthly prior-month universe; train-only normalisation |
| Costs and realism | 1 | IC-centred; portfolio implementations varied, spread change as cost proxy |
| Sample breadth | 2 | All liquid US stocks, 2008–2025 incl. GFC and COVID |
| Statistical testing | 1 | Month-adjusted standard errors; no multiple-testing correction |
| Reproducibility | 2 | Data, models and code released |
| **Total** | **12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "encoders with similar predictive performance can organize market state very differently" (p. 1)
