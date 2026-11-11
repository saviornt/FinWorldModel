---
type: lit-note
title: "Deep Reinforcement Learning for Cryptocurrency Trading: Practical Approach to Address Backtest Overfitting"
authors: [Berend Jelmer Dirk Gort, Xiao-Yang Liu, Jiechao Gao, Shuaiyu Chen, Christina Dan Wang]
year: 2022
venue: arXiv (AAAI 2023 workshop version)
source_url: https://arxiv.org/abs/2209.05559
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ4.1]
family: [rl-planning]
evidence: Weak
score: 5
tags: [lit-note, family/rl-planning]
---
# DRL for Crypto Trading: Addressing Backtest Overfitting (Gort, 2022)

**Basis:** Full PDF (v6) read through alphaXiv, pp. 1–8. Guide seed source.

**Takeaway:** Using combinatorial cross-validation and the probability of backtest overfitting (PBO) to reject over-tuned DRL agents picks a PPO agent that lost less than baselines in a two-month 2022 crypto crash (−35% vs −48% equal weight and −51% index), but every strategy lost money, so the paper shows how to screen out overfitted agents, not that DRL trades profitably.

## Problem
DRL trading papers report optimistic backtests that may be false positives from hyperparameter sensitivity and single walk-forward validation; can overfitted agents be detected and rejected (pp. 1–2)?

## Data and period
10 high-volume cryptocurrencies, 5-minute bars; training 2022-02-02 to 2022-04-30, test 2022-05-01 to 2022-06-27, which contains two market crashes (p. 5).

## Method
Trading as an MDP (cash, holdings, prices, 6 decorrelated technical features); reward = change in portfolio value minus 0.3% fees; long-only; a CVIX risk switch sells everything above a threshold (p. 3). Combinatorial CV (N = 5, k = 2, 10 splits) inside the training period; H = 50 hyperparameter trials per agent; PBO via the Bailey et al. logit of the out-of-sample rank of the in-sample best trial; reject agents with PBO ≥ α = 10% (pp. 4–6). PPO, TD3, SAC compared; also PPO with walk-forward and K-fold CV.

## Baselines and validation
Equal-weight buy-and-hold and the S&P Broad Digital Market index (p. 6). One test window of 58 days.

## Results (with page or section references)
- PBO: PPO walk-forward 17.5% (rejected), PPO K-fold 7.9%, PPO with combinatorial CV 8.0%, TD3 9.6%, SAC 21.3% (rejected) (p. 6; Table 3, p. 8).
- Test cumulative return: index −50.78%, equal weight −47.78%, PPO WF −49.39%, PPO KCV −55.54%, PPO (proposed) −34.96%, TD3 −59.08%, SAC −59.48% (Table 3, p. 8).
- Lower PBO did not rank agents consistently: TD3 passed the test (9.6%) yet lost more than equal weight.

## Limits and risks to validity
_My assessment:_ one 58-day crash window; the CVIX threshold (90.1) is the *average CVIX during the test-period crashes*, i.e. set with test data (p. 5), a direct look-ahead that likely explains much of the PPO advantage. No slippage, no seeds, no significance test on returns. The PBO screening idea is sound and useful for RP4; the trading evidence is not.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | CPCV for selection, but one short test split |
| Baselines | 1 | Equal weight and index; no simple trend rule |
| Point-in-time and leakage controls | 0 | Risk-switch threshold set from the test period |
| Costs and realism | 1 | Flat 0.3%, no slippage |
| Sample breadth | 0 | 10 coins, 2 months, one regime |
| Statistical testing | 1 | PBO test; no test on return differences |
| Reproducibility | 1 | Built on open-source FinRL/ElegantRL; code not linked in the paper |
| **Total** | **5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "A researcher may get 'lucky' during the backtest process" (p. 1)
