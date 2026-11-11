---
type: lit-note
title: "Deep Learning in Asset Pricing"
authors: [Luyang Chen, Markus Pelger, Jason Zhu]
year: 2024
venue: "Management Science (arXiv q-fin.ST version read)"
source_url: https://arxiv.org/abs/1904.00745
doi: 10.1287/mnsc.2023.4695
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15, RQ1.1]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series, world-model]
---
# Deep Learning in Asset Pricing (Chen, Pelger & Zhu)

**Basis:** arXiv v6 (11 Aug 2021), pp. 1, 3, 13–20, 26–28, 34–36, 51–55 (Table I, Fig. 6, Table A.I), via the alphaXiv PDF reader. Year set to the journal year; the published version and its DOI were not opened, so `doi` is left empty.

**Takeaway:** In a no-arbitrage GAN for US individual stock returns, 178 macro series helped only after an LSTM compressed them into four state processes (out-of-sample SDF Sharpe 0.75 vs ~10% lower without macro); feeding the raw macro increments directly made out-of-sample Sharpe "completely collapse" for the linear, elastic-net, feedforward and GAN models alike, so the tuned linear and FFN benchmarks drop macro entirely.

## Problem
Estimate a flexible, time-varying SDF from many firm characteristics and macro series without overfitting (pp. 1, 3).

## Data and period
US stocks with firm characteristics and 178 FRED-style macro series (McCracken–Ng transformations); single train/validation/test split (years not in the pages read) (pp. 15, 26).

## Method
FFN SDF network, LSTM macro-state extractor (4 states), adversarial conditioning network for test assets; ensembles of nine fits; hyperparameters by validation Sharpe (pp. 13–20, 51).

## Baselines and validation
LS, elastic net and Gu–Kelly–Xiu-style FFN; Sharpe, explained variation and cross-sectional R² (pp. 19, 26).

## Results (with page or section references)
- Test SDF Sharpe: LS 0.42, EN 0.50, FFN 0.44, GAN 0.75; test EV 0.03–0.04 vs 0.08 (p. 26, Table I).
- Raw 178 macro inputs: test Sharpe collapses for all four models; GAN without macro ~10% lower than with LSTM states; unconditional-moment version ~20% lower (pp. 26–27, Fig. 6).
- Simulation: models given only the latest macro differences cannot infer cyclical states (p. 54, Table A.I).
- LSTM states peak in NBER recessions (p. 35, Fig. 13).

## Limits and risks to validity
_My assessment:_ single split; macro series appear to be final-revised data, not vintages (not addressed in pages read); no costs or significance tests in pages read; validation-Sharpe selection over 384 configurations. The ablation pattern (raw macro hurts, compressed dynamic state helps modestly) matches [[Oliveira 2026 HANET Macro-Aware Mixed-Frequency Attention]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single train/validation/test split |
| Baselines | 1 | LS, EN, FFN; no GBT |
| Point-in-time and leakage controls | 1 | Lagged macro; vintages not addressed |
| Costs and realism | 0 | Not in pages read |
| Sample breadth | 2 | US cross-section over decades incl. recessions |
| Statistical testing | 0 | Not in pages read |
| Reproducibility | 0 | Licensed stock data; code not stated |
| **Total** | **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "including the large number of irrelevant variables actually lowers the performance" (p. 26)

**Citation check (2026-11-08):** DOI 10.1287/mnsc.2023.4695 confirmed through OpenAlex by the reference-lookup tool.
