---
type: lit-note
title: "EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series"
authors: [Seunghan Lee, Jaehoon Lee, Jun Seo, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, Junhyeok Kang, Sangjun Han, Soonyoung Lee, Wonbin Ahn]
year: 2026
venue: arXiv (LG AI Research technical report)
source_url: https://arxiv.org/abs/2609.04239
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.8]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, pretraining-objective]
---
# Lee 2026 EXAONE Finance Attention-Free TSFM (Lee et al., 2026)

**Takeaway:** A financial TSFM pretrained only on synthetic series (generated to have fat tails, volatility clustering, jumps, regime switches and cross-asset factors) with a direct multi-horizon quantile loss and input-masking augmentation ranked first on all three tiers of the FinVerse benchmark; synthetic-only pretraining also means no real test-period data can leak into pretraining.

## Problem
Building a financial TSFM that is cheap on long, many-channel, gappy panels and matches financial dynamics.

## Data and period
Pretraining: KernelSynth plus a synthetic financial generator (Table 4); no real market data (§5.1). Evaluation: FinVerse (diverse asset classes, from 2020), the benchmark described in [[Lee 2026 FinVerse Financial TSFM Benchmark]].

## Method
Attention-free encoder (causal 1D convolution over time, group-aware pooling MLP over variates). Instance normalisation plus arcsinh transform for heavy tails. Masked-context augmentation hides a contiguous 25% input span as known-missing and excludes it from the loss: it is a robustness device, not a reconstruction objective (§4.5). Pinball loss over 21 quantiles; all horizon steps decoded in one pass, no autoregressive rollout (§4.6–4.7).

## Baselines and validation
43 zero-shot TSFMs on FinVerse tiers: point accuracy, cross-sectional ranking, portfolio profitability; average ranks and pairwise win rates (§5.3–5.4).

## Results (with page or section references)
- #1 on all three tiers, rank sum 3 vs 14 for the next best (Chronos-2 Synthetic) (Table 7).
- Wins head-to-head against every baseline; win rate 0.51 against TiRex models (Fig. 7).
- No ablation of the loss or of the synthetic generator appears in the pages read; the report does not separate the objective's effect from architecture and data.

## Limits and risks to validity
_My assessment:_ vendor technical report evaluated on a benchmark built by overlapping authors (Jaehoon Lee, Jun Seo, Seunghan Lee and Wonbin Ahn are on both papers); no significance tests; FinVerse lacks GBT, GARCH or HAR baselines. Its value for RQ4.8 is a design data point: direct multi-horizon quantile training plus synthetic-only pretraining as a leakage-free route.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Zero-shot on a held-out benchmark |
| Baselines | 1 | 43 TSFMs; benchmark has persistence/naive baselines; no GBT or HAR |
| Point-in-time and leakage controls | 2 | Synthetic-only pretraining rules out real-data contamination |
| Costs and realism | 0 | Portfolio tier cost treatment not checked in pages read |
| Sample breadth | 1 | Many asset classes, one period from 2020 |
| Statistical testing | 0 | Ranks only |
| Reproducibility | 2 | Model weights and code released |
| **Total** | 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "EXAONE Finance therefore sees no real market data at any point during pretraining" (§5.1)
