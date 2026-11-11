---
type: lit-note
title: "Deep Reinforcement Learning for Equity Trading: Benchmarking Actor-Critic Methods with Forward Retraining"
authors: [Bicheng Wang, Xinyi Zhang]
year: 2026
venue: arXiv (cs.LG); manuscript dated 2021-06-08
source_url: https://arxiv.org/abs/2609.31870
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.9]
family: [rl-planning]
evidence: Weak
score: 3
tags: [lit-note, family/rl-planning]
---
# DRL Actor-Critic Benchmark with Forward Retraining (Wang, 2026)

**Basis:** Full PDF read through alphaXiv, pp. 1–8. A Stanford course project (CS230) posted in 2026; the manuscript is dated June 2021.

**Takeaway:** On 20 surviving S&P 500 mega-caps in 2019–2020, five actor-critic DRL agents earned higher returns than an LSTM-forecast rule but with market betas of 0.83–1.24 and drawdowns of 23–34%, and retraining before each test slice cut DDPG's return from 55.5% to 29.8%; the gains look like leveraged market exposure, not skill.

## Problem
Compare end-to-end DRL trading (A2C, PPO, DDPG, TD3, SAC) with a forecast-then-trade LSTM, trained once versus retrained walk-forward (pp. 1, 5).

## Data and period
Daily Yahoo Finance OHLCV for the 20 largest S&P 500 stocks with full 2000–2020 histories; train 2000–2018, test 2019–2020 (p. 2).

## Method
MDP with cash, prices, holdings and 14 technical indicators; reward = change in portfolio value; Stable-Baselines3 agents (pp. 4–5). Forward retraining: expanding-window retraining before each test slice (p. 5).

## Baselines and validation
S&P 500 index for alpha/beta; LSTM with a long-or-cash rule (p. 4, Table 4). One chronological split plus a walk-forward variant.

## Results (with page or section references)
- Annual return / Sharpe / max drawdown / beta: DDPG 55.5% / 1.38 / −33.5% / 1.24; TD3 42.0% / 1.37 / −25.2% / 0.89; SAC 39.0% / 1.33 / −24.2% / 0.90; LSTM 17.0% / 1.19 / −9.6% / 0.31 (Table 4, p. 6).
- Forward retraining: DDPG 55.5% → 29.8%; TD3 unchanged (42.0% → 41.9%); A2C, PPO, SAC improved (p. 6).
- Authors note survivorship bias, a two-year test, and no variability across seeds (p. 7).

## Limits and risks to validity
_My assessment:_ survivorship-biased universe of 2019–2020 winners; no transaction costs stated; no buy-and-hold of the same 20 stocks reported, so DRL returns cannot be separated from simply holding them; single seed; the large drop for DDPG under retraining shows how much one tuned run can flatter a result.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One split; walk-forward variant on the same 2 years |
| Baselines | 1 | Index and LSTM rule; no equal-weight of the universe |
| Point-in-time and leakage controls | 0 | Survivorship bias acknowledged, not controlled |
| Costs and realism | 0 | No costs stated |
| Sample breadth | 1 | 20 stocks, 2 years incl. COVID crash |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code or data link |
| **Total** | **3/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "we do not report variability across runs" (p. 7)
