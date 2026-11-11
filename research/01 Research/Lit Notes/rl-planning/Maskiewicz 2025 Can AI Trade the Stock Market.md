---
type: lit-note
title: "Can Artificial Intelligence Trade the Stock Market?"
authors: [Jędrzej Maskiewicz, Paweł Sakowski]
year: 2025
venue: University of Warsaw working paper (arXiv q-fin)
source_url: https://arxiv.org/abs/2506.04658
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.9]
family: [rl-planning]
evidence: Moderate
score: 6
tags: [lit-note, family/rl-planning]
---
# Can AI Trade the Stock Market? DDQN and PPO (Maskiewicz, 2025)

**Basis:** Working-paper PDF read through alphaXiv excerpts (pp. 1, 25, 31–50, 56). Literature-review chapters not read.

**Takeaway:** In yearly walk-forward tests 2019–2023 on three FX pairs, the S&P 500 and Bitcoin, a PPO agent with a transformer network beat buy-and-hold on Sharpe in every asset (e.g. S&P 500 2.16 vs 0.83), but the same algorithm with a plain network was the worst model (S&P 500 Sharpe 0.18, Bitcoin −0.02), hyperparameters were hand-picked, and there are no seeds or significance tests, so the edge is fragile.

## Problem
Can DDQN and PPO, with fully connected or transformer networks, trade liquid assets profitably out of sample (p. 1)?

## Data and period
Daily EUR/JPY, EUR/USD, USD/JPY, S&P 500 and BTC; five one-year out-of-sample windows 2019–2023, each preceded by a one-year validation year (p. 25).

## Method
Long/short/flat whole-capital agents; 20-day state of returns, position, OHLC and indicators; γ = 0.75; costs 0.01% FX, 0.025% S&P 500, 0.1% BTC; no leverage or swaps (pp. 25, 31). Hyperparameters set "by expert knowledge", not by search, because each model took about a day to train (p. 31).

## Baselines and validation
Buy-and-hold and a hypothetical "perfect annual" strategy with yearly foresight (Tables 1–5). Rolling walk-forward.

## Results (with page or section references)
- S&P 500 Sharpe: PPO-T 2.16, DDQN-T 1.60, DDQN-NN 0.99, PPO-NN 0.18, buy-and-hold 0.83 (Table 4, p. 44).
- BTC: only PPO-T beat buy-and-hold on final balance; PPO-NN Sharpe −0.02 with −85% drawdown (Table 5, p. 47).
- EUR/USD buy-and-hold Sharpe −0.11; DDQN-NN 1.84 (Table 1, p. 35).
- The authors attribute BTC failure to a shorter training history (p. 50).

## Limits and risks to validity
_My assessment:_ the authors chose the architectures and parameters knowing the literature and, plausibly, early results; with four model variants per asset and no seeds, multiple-testing and selection risk is high; huge spread between PPO-T and PPO-NN signals instability. Few assets; no trend-following or GBT baseline.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Yearly walk-forward |
| Baselines | 1 | Buy-and-hold only (plus foresight benchmark) |
| Point-in-time and leakage controls | 1 | Stated, not checked |
| Costs and realism | 1 | Flat per-asset fees |
| Sample breadth | 1 | 5 assets, 5 years incl. 2020, 2022 |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code |
| **Total** | **6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "we relied on the expert knowledge of the authors to select" (p. 31)
