---
type: lit-note
title: "Can AI Make Money in Crypto? Measuring the Gap from Backtests to Real Markets"
authors: [Xingtong Yu, Jiarun Zhou, Guanlin Ding, Wenkang Wei, Jiarui Liu, Chang Zhou, Fangzhou Ge, Chenyi Xu, Xikun Zhang, Renqiang Luo, Jie Zhang, Hong Cheng, Xinming Zhang, Hui Zhang, Yuan Fang]
year: 2026
venue: arXiv (cs.AI)
source_url: https://arxiv.org/abs/2609.34510
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ1.2, RQ4.6]
family: [rl-planning]
evidence: Strong
score: 10
tags: [lit-note, family/rl-planning, evaluation]
---
# AI Crypto Trading: Backtest vs Paper vs Live (Yu, 2026)

**Basis:** Full PDF read through alphaXiv, pp. 1–9 and Appendix Table 6.

**Takeaway:** Of 32 ML, RL, LLM and agent methods on ten large-cap cryptocurrencies, the 2025 backtest ranking nearly reversed in prospective paper trading (median selected-ML return 36.0% → −9.8%), and in four weeks of real-money trading none of the four survivors beat Bitcoin buy-and-hold (all negative alpha); both RL methods lost money in the 2025 backtest.

## Problem
How much of an AI trading method's backtest performance survives on unseen future data and real execution (pp. 1–2)?

## Data and period
OKX data; train 2021–2023, validation 2024, backtest test 2025; paper trading 2026-06-04 to 2026-09-21; live trading 2026-08-24 to 2026-09-21 (p. 4).

## Method
24 ML models (Qlib-style, Alpha52 factors, top-k long-only), 2 RL (MacroHFT, EarnHFT, long-only on one asset), 3 LLMs and 3 LLM agents; configurations selected on validation and frozen; OKX taker fees (0.10% spot, 0.05% perp) in all stages; fixed seed for non-LLM methods, three runs averaged for LLMs (pp. 3–4).

## Baselines and validation
Bitcoin buy-and-hold; linear, LightGBM, CatBoost, XGBoost among the ML set; staged prospective evaluation.

## Results (with page or section references)
- 2025 backtest: 23 of 24 ML methods profitable; none of the RL, LLM or agent methods were; MacroHFT −10.07%, EarnHFT −38.57% vs buy-and-hold −7.63% (Table 1, p. 5).
- Paper trading: only 2 of 8 selected ML methods profitable; all 6 non-ML selected methods positive; MacroHFT +38.1% vs buy-and-hold +30.4% over the same window (Table 2, pp. 6–7).
- Same-window backtest vs paper gaps average 6.25 pp in return and 0.62 in Sharpe; 10 of 14 methods did better in paper trading (p. 7).
- Live: one of four methods profitable, none beat buy-and-hold (+11.63%); live price slippage ~6× paper (1.86‰ vs 0.31‰) (Tables 4–5, pp. 8–9).

## Limits and risks to validity
Single crypto market; short paper (~3.5 months) and live (4 weeks) windows; a few methods per stage; one seed for non-LLM models; no significance tests. _My assessment:_ the selection-then-reversal pattern is exactly what selection on noise predicts; the main lesson is for evaluation (RP4), and for RQ1.9 it shows RL no better than other families once prospective.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Held-out year plus prospective paper and live trading |
| Baselines | 2 | Buy-and-hold, linear and GBT models |
| Point-in-time and leakage controls | 2 | Prospective stages cannot see the future |
| Costs and realism | 2 | Exchange fees; real execution measured |
| Sample breadth | 1 | Ten coins, one asset class |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Open-source code; exchange data |
| **Total** | **10/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "historical backtesting alone is insufficient for estimating prospective trading performance" (p. 9)
