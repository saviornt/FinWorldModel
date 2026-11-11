---
type: lit-note
title: "HIST: A Graph-based Framework for Stock Trend Forecasting via Mining Concept-Oriented Shared Information"
authors: [Wentao Xu, Weiqing Liu, Lewen Wang, Yingce Xia, Jiang Bian, Jian Yin, Tie-Yan Liu]
year: 2021
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2110.13716
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.4]
family: [graph]
evidence: Moderate
score: 8
tags: [lit-note, family/graph]
---
# HIST: Concept-Oriented Shared Information (Xu, 2021)

**Basis:** pp. 1, 3–4, 6–8, 10 read through alphaXiv page excerpts.

**Takeaway:** On China's CSI 300 (test 2017–2020), a plain GAT on concept graphs is no better than a GRU without a graph (IC 0.111 vs 0.113); only HIST's learned "hidden concept" plus predefined concept modules lift IC to 0.131.

## Problem
Can shared information from predefined stock concepts (industry, main business) and learned hidden concepts improve daily return forecasts?

## Data and period
CSI 100 and CSI 300 constituents, Qlib Alpha360 features (60 days of OHLCV + VWAP), 2007–2020; train 2007–2014, validate 2015–2016, test 2017–2020; concepts from Tushare (p. 6).

## Method
GRU encoder; predefined-concept module (market-cap-weighted concept embeddings, corrected by similarity); hidden-concept module; individual module; doubly residual sum; MSE on next-day return (pp. 3–6).

## Baselines and validation
MLP, LSTM, GRU, SFM, GATs on concept graph, ALSTM, Transformer, ALSTM+TRA; 10 seeds each (p. 7). No GBT/LightGBM baseline in the tables read.

## Results (with page or section references)
- CSI 300 IC: MLP 0.082, GRU 0.113, GATs 0.111, ALSTM 0.115, ALSTM+TRA 0.119, HIST 0.131 (Table 1, p. 7).
- Ablation (CSI 300): predefined concepts only 0.101–0.112; hidden only 0.110; predefined + hidden 0.120; full 0.131 (Table 2, p. 8).
- Top-30 backtest with 0.05% buy / 0.15% sell costs: over 120% cumulative 2017–2020 vs CSI 300 index about 50% (p. 8).

## Limits and risks to validity
_My assessment:_ one test split in one market; no significance tests; concept data are taken from a current vendor snapshot as far as the text shows (dates of concept assignments not stated); Chinese A-share predictability is higher than US.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 1 | Many deep baselines, no GBT |
| Point-in-time and leakage controls | 1 | Index membership changes handled; concept dates unclear |
| Costs and realism | 1 | Flat buy/sell costs |
| Sample breadth | 1 | CSI 300, 2017–2020 incl. 2018 fall |
| Statistical testing | 1 | 10 seeds, mean ± SD |
| Reproducibility | 2 | Code and Qlib data |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None recorded.
