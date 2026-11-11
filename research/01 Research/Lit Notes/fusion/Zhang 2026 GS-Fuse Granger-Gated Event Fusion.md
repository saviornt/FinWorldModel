---
type: lit-note
title: "GS-Fuse: Granger-Supervised Gated Fusion and Multi-Granularity Alignment for Event-Driven Financial Forecasting"
authors: [Yang Zhang, En Chun, Ziyun Mao, Yulu Wu, Jun Wang]
year: 2026
venue: "KDD 2026 (arXiv cs.AI)"
source_url: https://arxiv.org/abs/2605.28520
doi: 10.1145/3770855.3817927
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.7, RQ1.12]
family: [fusion]
evidence: Weak
score: 5
tags: [lit-note, family/fusion]
---
# GS-Fuse: Granger-Supervised Gated Fusion for Event-Driven Financial Forecasting (Zhang et al., 2026)

**Basis:** KDD 2026 paper, arXiv v1 (27 May 2026), pp. 1, 3, 7–9, 12, via the alphaXiv PDF reader.

**Takeaway:** For 5-minute paths of US indices and Treasury yields after macro releases (FOMC, CPI/PPI, jobs, GDP), a gate trained to open only when event text adds predictive value beyond prices improved on its own price-only branch by just 1.5–3.8% MSE (14.4% MAE on 1-month yields), with the gate opening ~52% of the time on equity indices and ~61% on short yields; the much larger gains over external baselines mix architecture and training differences.

## Problem
Fuse event text and pre-event prices asymmetrically, letting text in only when it is incrementally predictive (pp. 1, 3).

## Data and period
CAMEF macro-announcement dataset (six event categories) enriched with FNSPID news by embedding similarity; 5-minute S&P 500, Dow, Nasdaq, 1-month and 5-year Treasury yields; chronological 6/2/2 split; horizons of half, one and two trading days (p. 7).

## Method
Frozen LLM text encoder (LLaMA-3B or Phi-3B) and frozen TS foundation model (MOMENT or Kronos); Granger-supervised soft gate; instance- and token-level alignment; staged training (pp. 3, 7–8).

## Baselines and validation
ARIMA, DLinear, Autoformer, iTransformer, FEDformer, TimesFM, Chronos, MOMENT, Kronos, GPT4MTS, TEST, TimeCMA; MSE, MAE, directional hit rate, Sharpe (p. 7, Table 2).

## Results (with page or section references)
- Internal comparison, TS-only branch vs full model MSE (×1e-4): INDU 18.53 vs 18.16 (+2.0%), S&P 500 6.70 vs 6.60 (+1.5%), USGG1M 3.99 vs 3.84 (+3.8%; MAE +14.4%) (p. 8, Table 4).
- Average text-gate openness 52.9% (INDU), 51.6% (S&P), 60.7% (USGG1M) (p. 8).
- Directional hit rates for GS-Fuse 53–61% on equity indices; Sharpe reported without costs (p. 7, Table 2).

## Limits and risks to validity
_My assessment:_ external unimodal baselines were trained on continuous sliding windows while GS-Fuse is trained on event-aligned windows, so the headline gap over them is not a modality effect; the internal ablation is the fair comparison and shows small gains. LLaMA-3B reads pre-cutoff event text (memorisation not controlled; rubric cap). No significance tests; Sharpe without costs. Code and data public.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split |
| Baselines | 1 | ARIMA, DLinear, TSFMs, multimodal; no random walk |
| Point-in-time and leakage controls | 0 | Pre-cutoff LLM; not addressed |
| Costs and realism | 0 | Sharpe without costs |
| Sample breadth | 1 | Five assets, macro events |
| Statistical testing | 0 | None |
| Reproducibility | 2 | Code and public datasets |
| **Total** | **5/14, capped** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "learns to open toward event text only when it provides incremental predictive value" (p. 1)
