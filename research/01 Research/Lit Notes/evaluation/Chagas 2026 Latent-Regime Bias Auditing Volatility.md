---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- metrics
title: Latent-Regime Bias Auditing for Volatility Forecasting
authors:
- Arthur Chagas
- Pedro Bento
- Yan Aquino
- Arthur Buzelin
- Wagner Meira Jr.
- Cristiano Arbex Valle
year: 2026
venue: arXiv (cs.LG) 2608.01599
source_url: https://arxiv.org/abs/2608.01599
doi: ''
research_questions:
- RQ4.3
evidence: Moderate
score: 8
---
# Latent-Regime Bias Auditing for Volatility Forecasting (Chagas et al., 2026)

**Basis:** Full text (8 pages) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** Volatility models with near-identical aggregate RMSE (0.025–0.027) can carry significant bias in particular calm, intermediate or stress regimes and rank differently under tail-weighted asymmetric loss; HAR-RV variants move up and Transformer models (PatchTST, iTransformer) move down when underprediction in high-volatility outcomes is penalised.

## Problem
Aggregate RMSE/MAE hide where volatility forecasts fail (§I).

## Data and period
Daily BTC, ETH, SPY, QQQ, IWM, GLD, USO, 25 May 2021 – 7 Mar 2026; chronological 70/15/15 split per asset; horizons 1, 5, 10, 21 days, main h = 5 (§IV.B).

## Method
TS2Vec-style embeddings with an asset adversary; within-asset K-means regimes (K = 3) fit on training data only and ordered by a training-period stress score; regime-conditional bias, tail underprediction, asymmetric loss; block-bootstrap CIs (§III).

## Baselines and validation
16 models incl. historical RV, HAR-RV, HAR-IV variants, ridge, ElasticNet, random forest, ExtraTrees, LSTM, GRU, TCN, PatchTST, iTransformer (Table V).

## Results (with page or section references)
- RMSE at h = 5 spans 0.025–0.027 for the top 12 models, but hidden regime bias (RBA_stable) ranges 0.734–1.374 among them (Table V).
- LSTM's worst-regime bias −0.006 [−0.010, −0.001] excludes zero; iTransformer and PatchTST show calm-regime bias 0.014 (Table VI).
- RMSE rank, conditional-reliability rank and tail-loss rank differ; HAR-RV models rise under economic loss (Fig. 2, §V.D).
- PatchTST and iTransformer have the highest RMSE (0.034–0.036) and tail asymmetric loss (0.020–0.021) (Table V).

## Limits and risks to validity
_My assessment:_ one chronological split; regimes are sample-dependent audit partitions (authors say so, §VI); short sample (2021–2026). Code released.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 2 | HAR family, linear and tree models |
| Point-in-time and leakage controls | 1 | Regimes and scalers fit on training only |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Seven assets, 2021–2026 |
| Statistical testing | 1 | Block-bootstrap CIs |
| Reproducibility | 1 | Code on GitHub; data from public APIs |
| **Total** | 7/12 → **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "aggregate accuracy can mask substantial regime-dependent failures" (§VI)
