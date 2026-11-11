---
type: lit-note
title: "Does Joint-Embedding Predictive Architecture Pretraining Help Time Series Forecasting?"
authors: [Yutong Feng, Bowen Liao, See Kiong Ng, Yuxuan Liang]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2609.31680
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.8]
family: [price-time-series]
evidence: Weak
score: 4
tags: [lit-note, family/price-time-series, pretraining-objective]
---
# Feng 2026 JEPA Pretraining Time Series Forecasting (Feng et al., 2026)

**Takeaway:** Latent-space prediction pretraining (LeJEPA) helped some forecasting backbones and consistently hurt others on the same datasets; the swing between best and worst effect exceeded 25 percentage points, so the effect of a pretraining objective has to be checked on the backbone actually used.

## Problem
Whether JEPA-style pretraining (predict target embeddings, no reconstruction, no negative pairs) is a reliable improvement for forecasting.

## Data and period
Five temporal benchmarks (ETTh1/h2/m1/m2, Weather) and six spatio-temporal traffic benchmarks (METR-LA, PEMS-BAY, PEMS03/04/07/08). No financial data. Standard splits (§3).

## Method
One JEPA instantiation (LeJEPA loss with SIGReg regulariser) applied to nine backbones. Context = input window, target = forecast window; encoder shared. Pretrain, then fine-tune with the same supervised loss; total epochs matched (§2–3).

## Baselines and validation
Same backbone trained from random initialisation on the supervised loss only; three seeds; MAE/RMSE (§3).

## Results (with page or section references)
- Crossformer and FEDformer improve on every temporal dataset (FEDformer up to 6.4% MAE on Weather); iTransformer degrades on four of five; Autoformer loses 15.5% MAE on Weather (Table 1, §4).
- Spatio-temporal: STGCN gains up to 8.3%; ASTGCN loses up to 10.4% (Table 2).
- Dense global-attention backbones tend to lose; structurally constrained ones tend to gain; the authors present this as an observation, not a mechanism (§5).
- The range of effects "exceeds 25 percentage points" and can change which model looks best (§5).

## Limits and risks to validity
_My assessment:_ not finance; one JEPA variant; three seeds with no significance tests; code release not stated. Cited only for the general point that a pretraining objective's effect is backbone-dependent.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Standard benchmark splits |
| Baselines | 1 | Matched from-scratch backbone; no simple statistical baselines |
| Point-in-time and leakage controls | N/A | Not financial |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | Eleven datasets, two task families, no finance |
| Statistical testing | 0 | Mean ± std over three seeds only |
| Reproducibility | 0 | Code not stated |
| **Total** | 3/10 → 4/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "JEPA does not work uniformly for time series self-supervised learning" (§5)
