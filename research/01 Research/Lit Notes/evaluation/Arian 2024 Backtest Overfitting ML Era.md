---
type: lit-note
title: 'Backtest overfitting in the machine learning era: A comparison of out-of-sample testing methods in a synthetic controlled environment'
authors:
- Hamid Arian
- Daniel Norouzi Mobarekeh
- Luis Seco
year: 2024
venue: Knowledge-Based Systems (2024)
source_url: https://doi.org/10.1016/j.knosys.2024.112477
doi: 10.1016/j.knosys.2024.112477
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ4.1
family:
- evaluation
evidence: Weak
score: 5
tags:
- lit-note
- family/evaluation
- cross-validation
- guide-seed
---
# Backtest Overfitting in the Machine Learning Era (Arian, Norouzi & Seco, 2024)

**Basis:** Abstract only, read 2026-11-08 through web-search records of the paper (an index page carrying the Knowledge-Based Systems abstract and DOI, and a copy of the SSRN preprint first page). The DOI landing page, ScienceDirect and SSRN (abstract 4778909) refused the fetch. No numbers could be read; guide seed source.

**Takeaway:** In synthetic markets (Heston, Merton jumps, drift bursts, regime switching) CPCV gave lower probability of backtest overfitting and better deflated Sharpe statistics than k-fold, purged k-fold and especially walk-forward; purged k-fold and k-fold performed about the same.

## Problem
Which out-of-sample testing method best prevents false discoveries in backtests of ML strategies?

## Data and period
Synthetic controlled environment combining Heston stochastic volatility, Merton jump diffusion, the drift-burst hypothesis and regime switching; historical S&P 500 for an empirical check (abstract).

## Method
Compares walk-forward, k-fold, purged k-fold and CPCV, and proposes Bagged CPCV and Adaptive CPCV; judged by PBO and the deflated Sharpe ratio test statistic (abstract).

## Baselines and validation
The four standard schemes against each other.

## Results (with page or section references)
- CPCV: lowest PBO and best DSR statistic; walk-forward worst at preventing false discoveries, with more temporal variability (abstract).
- Purged k-fold vs k-fold: comparable; the authors urge caution in choosing between them (abstract).
- S&P 500 data said to confirm the synthetic ranking (abstract). Sizes not read.

## Limits and risks to validity
_My assessment:_ full text not opened, so magnitudes, the number of simulations, the strategy class and how PBO was computed for walk-forward (a single path) are unknown. The comparison favours methods that produce many paths by construction of the metrics. Conflicts in part with Li 2026, which ranks walk-forward as the only strictly causal scheme. Code said to be on the RiskLab GitHub (not opened).

## Rubric scores
Not scored item by item: only the abstract was read. Capped at **Weak (5/14)** until the full text is opened; provisional reading: out-of-sample design 2, baselines 1, sample breadth 1, statistical testing 1 (PBO, DSR), reproducibility 1 (code claimed), leakage controls and costs unknown.

## Quotes worth keeping (each under 15 words, with page)
- None kept (abstract only).
