---
type: lit-note
title: "TAC-Time: Texts as Channels For Multimodal Time Series Forecasting"
authors: [Jiayi Liang, Xiaotian Gu, Xinyu Xie, Yuanbin Wu, Xiaoling Wang]
year: 2026
venue: arXiv 2609.24156
source_url: https://arxiv.org/abs/2609.24156
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.14]
family: [fusion]
evidence: Weak
score: 2
tags: [lit-note, family/fusion]
---
# TAC-Time: Texts as Channels for Multimodal Time Series Forecasting (Liang, 2026)

**Basis:** v1 (21 Sep 2026), page excerpts via alphaXiv (pp. 1–4, 7–8, 10).

**Takeaway:** Encoding each time step's text with a mostly frozen GPT-2, compressing it with a sparse autoencoder and adding it as extra channels to an iTransformer beat other multimodal methods on nine Time-MMD-style datasets, yet shuffling the text across timestamps changed MSE by ≤1% on Agriculture, Economy and Energy (e.g. Economy 0.202 → 0.204), so on most series the text content did little.

## Problem
Can text be represented as low-dimensional time-series channels instead of tokens or cross-attended embeddings?

## Data and period
Nine multimodal benchmarks (Agriculture, Climate, Economy, Energy, Environment, Health, Security, Social Good, Traffic); no market price data (Table III, p. 7).

## Method
GPT-2 embedding (attention/FFN frozen; LayerNorm and position embeddings trained), learnable token compression, sparse autoencoder, orthogonality penalty, projection to d channels concatenated with the numeric series; FFT trend/season split; iTransformer backbone (pp. 2–4).

## Baselines and validation
Unimodal (iTransformer, TimeMixer, TimeXer…), fusion and LLM methods; ablations with shuffled text, mean pooling, no SAE, no frequency decomposition (Table III, p. 7). Benchmark splits; no tests.

## Results (with page or section references)
- Shuffled text vs real text MSE: Agriculture 0.371 vs 0.370; Economy 0.204 vs 0.202; Energy 0.226 vs 0.223; larger effects on Environment (0.260 vs 0.205), Health, Social Good, Traffic (Table III, p. 7).
- Gains over unimodal models of ~3–6% rise with the spectral correlation between text and numeric channels (Fig. 5, p. 8).
- Cost: 1.93 GB, 13.4M trainable parameters, 422 s training vs 8.4 s for iTransformer; far below Time-LLM (Table IV, p. 7).

## Limits and risks to validity
_My assessment:_ not financial data; benchmark texts are often reports that summarise the same series (risk of target information in text). Useful only for the design point that text can enter as a few dense channels at low cost, and for the shuffled-text control, which agrees with [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Benchmark train/test splits |
| Baselines | 1 | Unimodal deep models; no naive |
| Point-in-time and leakage controls | 0 | Not addressed |
| Costs and realism | N/A | No trading |
| Sample breadth | 0 | No financial series |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Not stated |
| **Total** | **2/12 → 2/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- "we translate texts into time series" (p. 2)
