---
type: lit-note
title: "DIVINE: Simple Cross-Market Stock Pretraining via Diverse Indicator Reconstruction"
authors: [Kuan-Yu Chen, Shu-Cheng Zheng, Yu-Chen Den, Wei-Cheng Liao, Tien-Hao Chang]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2610.02866
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.8]
family: [price-time-series]
evidence: Moderate
score: 7
tags: [lit-note, family/price-time-series, pretraining-objective]
---
# Chen 2026 DIVINE Indicator Reconstruction Pretraining (Chen et al., 2026)

**Takeaway:** Pretraining a tiny encoder to reconstruct 77 technical-indicator targets from raw OHLCV, pooled across six equity markets, beat masked-reconstruction, contrastive and autoregressive pretraining in a 2021–2024 top-k ranking test (average long-only Sharpe 1.40 vs 1.01 for PatchTST and 1.26 for Kronos-small), and the largest single gain came from cross-market data, not from the objective itself.

## Problem
Which pretraining supervision transfers to cross-sectional stock ranking. The authors argue masked price reconstruction and future-return targets inherit stochastic noise, while contrastive pairs are hard to define in markets.

## Data and period
CSI300, CSI500, Nikkei 225, S&P 500, FTSE 100, TWSE300; 2008–2019 train, 2020 validation, 2021–2024 test (§5.1). Fixed stock universes shared by all methods.

## Method
A GRU encoder (0.05M parameters; Transformer and Mamba variants also tested) reconstructs 77 indicator-period targets from 16 standard indicators (RSV, stochastics, moving averages, etc.), computed only from past OHLCV. Targets clipped at median ± 10 IQR and standardised with training-split statistics. The reconstruction head is discarded; the encoder is transferred with a small MLP trained with a ranking loss (§4).

## Baselines and validation
From-scratch financial models (RankLSTM, FinGAT, MASTER, AlphaMix, StockMixer, DHMoE), general pretraining (TS2Vec, PatchTST, TimesURL), financial pretraining (CI-STHPAN, MERA, SSPT, FASCL), and released foundation models (Kronos mini/small/base, FinCast) as external references. One chronological split; 25 seed × start-offset runs per setting (§5.1). No random walk, gradient-boosted trees or market benchmark.

## Results (with page or section references)
- Average SR/CR: DIVINE-GRU 1.396/1.790; PatchTST 1.007/1.202; TS2Vec 0.983; TimesURL 0.914; best financial pretraining (MERA) 0.962; Kronos-small 1.256; FinCast (991M parameters) 0.754, below several from-scratch models (Table 1, §5.2).
- "None of the compared financial pretraining methods surpasses PatchTST on average" (§5.2).
- Ablation (Table 2): indicators as inputs 1.173; single-market indicator reconstruction 1.183; cross-market reconstruction 1.396. The cross-market step is the largest gain.
- Using only 10% of the corpus still beats all pretraining baselines (§5.4).
- Under ten horizon × long-only/long-short settings DIVINE has the best mean rank (1.6) but MERA, PatchTST and Kronos-small lead in some settings (Table 3).
- Paired t-test over 25 seed–offset runs: improvement over Kronos-small significant at p < 0.05 (Table 1 note).
- Exception: FTSE 100 (smallest universe), where relation-aware methods match or beat it (§5.2).

## Limits and risks to validity
_My assessment:_ the authors note fixed universes "may introduce survivorship effects" and that results are a controlled comparison, not an investable backtest (§5.1). Costs excluded from main tables (fees only in App. F.4). One test window; no random-walk or GBT baseline; Sharpe ratios are long-only and not reported against the market. Foundation models were pretrained on different corpora, so the Kronos comparison is not controlled. Good evidence on the relative ranking of objectives under one protocol; weak on absolute value.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split, 25 seed–offset runs |
| Baselines | 1 | Many deep and pretraining baselines; no random walk, GBT or market benchmark |
| Point-in-time and leakage controls | 1 | Train-only normalisation; survivorship acknowledged, not fixed |
| Costs and realism | 1 | Fees in an appendix; no slippage or turnover in main results |
| Sample breadth | 2 | Six markets, 2021–2024 test incl. 2022 drawdown |
| Statistical testing | 1 | Paired t-test, no multiple-testing correction |
| Reproducibility | 0 | Code release not stated |
| **Total** | 7/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "performance does not scale with model size" (§5.2)
