---
type: lit-note
title: "Implementation Risk in Portfolio Backtesting: A Previously Unquantified Source of Error"
authors: [Don Yin, Takeshi Miki, Vladislav Lesnichenko, Vasyl Gural]
year: 2026
venue: arXiv (q-fin.PM) 2603.20319
source_url: https://arxiv.org/abs/2603.20319
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.6, RQ4.7]
family: [evaluation]
evidence: Strong
score: 10
tags: [lit-note, family/evaluation, reproducibility, transaction-costs, backtesting]
---
# Implementation Risk in Portfolio Backtesting (Yin et al., 2026)

**Basis:** Full text (pp. 1–9, 11–12, 14, 22, 27–28, 35–41) via the alphaXiv PDF reader, read 2026-11-09.

**Takeaway:** Running 15 strategies through five backtesting engines on identical data gives identical results at zero cost, but cost-model differences make results diverge in proportion to turnover (up to 3.71 percentage points of total return for rotation strategies at 60 bps), and cross-checking engines exposed seven undocumented engine defects, including one that silently cut commissions 100-fold.

## Problem
Whether the choice of backtest engine changes reported results for the same strategy, data and cost specification ("implementation risk") (pp. 1–2).

## Data and period
30 stratified buckets from 180 S&P 500 constituents, 2020–2024 (incl. COVID drawdown and the 2022 rate cycle); costs 0, 18, 36 and 60 bps (pp. 1, 3).

## Method
15 benchmark strategies (equal weight, buy-and-hold, inverse volatility, momentum, four ML signal families, rotation strategies, zero-cost control) through a reference implementation and four open-source engines (bt, vectorbt, Backtrader, cvxportfolio). Metrics: engine spread, implementation uncertainty interval, divergence amplification factor, Sharpe sign-flip indicator (pp. 3–4, 9–12).

## Baselines and validation
Zero-cost run as causal isolation; reference engine is a direct translation of the cost specification (pp. 3, 22). Spearman correlation, cluster bootstrap over buckets, Lin's concordance (p. 22).

## Results (with page or section references)
- At zero cost all five engines agree exactly (0.0000% total-return difference) (p. 22).
- Divergence rises with cost intensity (Spearman ρ = 0.93, p < 0.001); below 0.75 pp for 12 of 15 strategies, up to 3.71% for high-turnover rotation at the heaviest cost (p. 1).
- Rotation strategies amplify divergence 2.3–6.2× relative to monthly equal weight (p. 28). No Sharpe sign reversal in the sample (p. 28).
- Seven engine defects found, e.g. Backtrader default dividing the commission rate by 100 (p. 1); recommend at least two independent validators and an audit of each engine's cost model (pp. 38–39).
- Cites Pérignon et al. (2024): only 52% of 1,000 reproduction tests of six published papers gave the same conclusion (p. 7).

## Limits and risks to validity
_My assessment:_ proportional costs and market-on-close orders only; constituents appear to be current S&P 500 members (survivorship not addressed, but it does not affect the engine comparison). Strong for the narrow claim that cost-model implementation is a measurable error source that grows with turnover.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Engine comparison, not a forecast test |
| Baselines | N/A | Reference implementation serves as ground truth |
| Point-in-time and leakage controls | 0 | Constituent selection not addressed |
| Costs and realism | 2 | Four cost regimes; turnover-driven analysis |
| Sample breadth | 2 | 30 buckets, 2020–2024 incl. stress |
| Statistical testing | 1 | Rank correlation, cluster bootstrap |
| Reproducibility | 2 | Code, reference engine and benchmark suite released |
| **Total** | 7/10 → **10/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "multi-engine comparison is the most effective diagnostic for detecting it." (p. 2)
