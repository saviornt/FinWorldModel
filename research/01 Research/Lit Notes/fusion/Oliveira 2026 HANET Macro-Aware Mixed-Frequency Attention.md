---
type: lit-note
title: "Macro-aware time series forecasting via hierarchical mixed-frequency attention models"
authors: [Daniel Cunha Oliveira, Kieran Wood, Stefan Zohren, Mihai Cucuringu, André Fujita]
year: 2026
venue: "arXiv q-fin.ST"
source_url: https://arxiv.org/abs/2606.00624
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15, RQ1.7]
family: [fusion]
evidence: Moderate
score: 8
tags: [lit-note, family/fusion, world-model]
---
# HANET: Macro-Aware Forecasting via Hierarchical Mixed-Frequency Attention (Oliveira et al., 2026)

**Basis:** arXiv v1 (30 May 2026), pp. 1, 3, 10–11, 14–15, 18, 21, 25 (Tables 2, 3, 5, 6, 11), via the alphaXiv PDF reader.

**Takeaway:** For time-series momentum on 55 liquid futures (2005–2024 out of sample), letting monthly point-in-time macro factors select historical regimes through cross-attention lifted gross Sharpe from 1.19 (macro-free LSTM) to 1.99, but concatenating the same five macro PCs to the daily inputs collapsed Sharpe to 0.06 and shuffling the macro history cut it to 0.81; the gain is gone by 5 bps per trade.

## Problem
Use scarce, low-frequency macro regimes to condition daily trading signals without discarding daily detail (pp. 1, 3).

## Data and period
55 Pinnacle futures (commodities, bonds, FX, equity indices), ratio-adjusted continuous series; FRED-MD (127 variables after excluding rates and FX) in point-in-time vintages with publication lags, December 1959–January 2023; PCA loadings fit on training data only (pp. 10–11).

## Method
LSTM encoder for daily returns; monthly macro queries/keys attend over all past macro months, weights expanded to the daily grid and applied to daily values; LSTM decoder to positions; Sharpe-loss training; 100 seeds, top 10% ensembled (pp. 10, 25, Table 11).

## Baselines and validation
Expanding walk-forward: initial 15-year in-sample window, 5-year steps; benchmarks: macro-free LSTM (Deep Momentum Network style), Lag(264), MACD(8,96), buy-and-hold; ablations: LSTM + concatenated macro PCs, HANET with shuffled macro history (pp. 14–15, 25).

## Results (with page or section references)
- Momentum, gross, 10% vol target: LSTM SR 1.19 (MDD −14.2%); LSTM + macro PCs 0.06 (MDD −25.8%); HANET 1.99 (MDD −15.9%); HANET shuffled macro 0.81 (p. 15, Table 2).
- Carry: LSTM 0.76; LSTM + macro PCs −0.17 (MDD −52.2%); HANET 0.91; shuffled 0.12 (p. 18, Table 5).
- Costs, momentum (4,622 trades): net SR 1.60 at 1 bp, 1.24 at 2 bps, 0.17 at 5 bps, −1.61 at 10 bps; carry keeps 0.60 at 10 bps (pp. 15, 18, Tables 3, 6).
- Attention up-weighted 2008 during COVID and Volcker-era months in 2022 (p. 21).

## Limits and risks to validity
_My assessment:_ the macro-free LSTM baseline is fixed while HANET adds architecture, so part of the gain is capacity (the shuffled-macro variant, 0.81, is the fairer control; it is still below the LSTM's 1.19, which means HANET's architecture without real macro hurts). No GBT or linear macro-timing baseline; no significance tests; Sharpe is gross in the headline tables. Authors list stricter walk-forward and cost-aware objectives as future work (p. 21). Code availability not stated in the pages read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward, 5-year steps |
| Baselines | 1 | LSTM, classical trend signals; no GBT, no linear macro model |
| Point-in-time and leakage controls | 2 | FRED-MD vintages with publication lags; train-only PCA |
| Costs and realism | 1 | Flat per-trade cost sensitivity |
| Sample breadth | 2 | 55 futures, 4 asset classes, 2005–2024 incl. GFC, COVID, 2022 |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Code not stated; licensed Pinnacle data |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "gains rely on structured macro conditioning rather than naive feature augmentation" (p. 1)
