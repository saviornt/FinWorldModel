---
type: lit-note
title: "Financial Fine-tuning a Large Time Series Model"
authors: [Xinghong Fu, Masanori Hirano, Kentaro Imajo]
year: 2024
venue: arXiv (q-fin.CP)
source_url: https://arxiv.org/abs/2412.09880
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.13, RQ1.1]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, foundation-models, fine-tuning]
---
# Financial Fine-tuning a Large Time Series Model (Fu, 2024)

**Basis:** alphaXiv PDF pages 1, 3–8 (v1). MIT; Preferred Networks.

**Takeaway:** Continual pretraining of the decoder-only TimesFM on ~90M financial price points makes it beat the original TimesFM and a chance-rate model from 2023 on, but a simple AR(1) is about as good on S&P 500 (Sharpe 1.58 vs 1.68) and much better on currencies and crypto; results are cost-free.

## Problem
Can a time-series foundation model predict market prices, and does financial fine-tuning help? (p. 1)

## Data and period
>100K series, ~90M points: TOPIX500 and S&P500 stocks, currencies, Japanese investment trusts, commodities, indices, crypto; daily and hourly; Yahoo Finance and Binance. Test from 1 Jan 2023; train/validation 75/25 random split before 2023 (§IV.A, Table I, p. 3).

## Method
TimesFM continual pretraining (20 layers, 1,280 hidden, context 512, output 128) with MSE on log prices and random-start masking; 100 epochs, 8 V100s, ~1 hour (§III–IV.B, p. 3).

## Baselines and validation
Original TimesFM, chance-rate random model, AR(1). Accuracy and macro F1 by horizon; market-neutral mock trading at h=128 without costs, plus "neutral cost" (break-even cost) (§IV.C, pp. 4, 6).

## Results (with page or section references)
- Original TimesFM underperforms random chance on 4 of 7 horizons; fine-tuned beats it at all horizons (p. 5).
- Market-neutral S&P 500, h=128: annual Sharpe 1.679, annual return 3.6%, break-even cost 0.60% (Table III, p. 6).
- Sharpe across markets (fine-tuned / original / random / AR1): S&P500 1.68 / 0.42 / 0.03 / 1.58; TOPIX500 1.06 / −1.75 / 0.11 / −0.82; currencies 0.25 / −0.04 / −0.03 / 0.88; crypto daily 0.26 / −0.03 / 0.01 / 0.17 (Table IV, p. 7).
- Authors: "unable to ascertain consistently better performance over just a simple AR1 model" (p. 7).

## Limits and risks to validity
_Authors:_ train and validation sets are similar, inviting memorisation of seen patterns (p. 5); data dominated by hourly crypto and stocks (p. 7).
_My assessment:_ one test period, no significance tests despite the "statistical confidence" wording, no costs in PnL, likely survivorship in the S&P 500 list. [[Cheung 2026 Base-Rate-Honest TimesFM LoRA Equities]] cites this as the ~54% reference and finds no skill over the base rate under stricter tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single split; test from 2023 |
| Baselines | 1 | AR(1), chance, original; no GBT/GARCH |
| Point-in-time and leakage controls | 1 | Time split; random validation; survivorship not addressed |
| Costs and realism | 1 | Zero cost plus break-even cost |
| Sample breadth | 1 | Several markets, one period |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Code and weights released |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "unable to ascertain consistently better performance over just a simple AR1 model." (p. 7)
