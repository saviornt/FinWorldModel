---
type: lit-note
title: "Forecasting Global Equity Volatility: Econometric Anchoring and Cross-Market Attention"
authors: [Xinlin Zhao, Haotian Qiao]
year: 2026
venue: "arXiv cs.CE"
source_url: https://arxiv.org/abs/2608.25369
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15, RQ1.4, RQ1.1]
family: [graph]
evidence: Moderate
score: 9
tags: [lit-note, family/graph, world-model]
---
# Forecasting Global Equity Volatility: Econometric Anchoring and Cross-Market Attention (Zhao & Qiao, 2026)

**Basis:** arXiv v3 (23 Oct 2026), pp. 1, 3, 7–13 (Tables 1–9, Fig. 3), via the alphaXiv PDF reader.

**Takeaway:** For daily range volatility of eight equity indices (test Sep 2022–Sep 2026), foreign-market information helped only as a bounded correction to each market's own HAR forecast (MSE −1.70% at 1 day, −1.13% at 22 days; significant vs HAR in 5 of 8 markets at 1 day after Holm correction); adding foreign regressors freely (VHAR) raised 22-day MSE by 33%, and unanchored graph and attention models were worse than HAR at every lead.

## Problem
Use cross-market information without letting unstable links swamp a strong local benchmark, on asynchronous trading calendars (pp. 1, 3).

## Data and period
Yahoo Finance daily OHLC for S&P 500, DAX, CAC 40, FTSE 100, OMX Stockholm, Nikkei 225, KOSPI, Hang Seng; Parkinson range volatility; 5 Mar 2013–28 Sep 2026 on a union calendar of 3,531 dates; missing values masked, not filled (p. 7, Table 1).

## Method
Frozen per-market HAR anchor plus a bounded attention correction; spatial attention guided by a rolling VAR(2) GFEVD predictive-connectedness graph from past data only; source masks for market closures (pp. 3, 7–8).

## Baselines and validation
Chronological 60/10/30 split, refit on the first 70% with the validated epoch count; five seeds ensembled. Primary pool: HAR, VHAR (200 coefficients), HAR-KS, GNN-HAR, DCRNN-HAR, Pure-ST-Transformer; six controlled ablations. HAC Diebold–Mariano with Holm adjustment; 90% Model Confidence Sets; VaR/ES and certainty-equivalent tests with 0–10 bps costs (pp. 7–9).

## Results (with page or section references)
- Equal-market MSE, h = 1 / 5 / 22: HAR 0.1615 / 0.2139 / 0.2480; VHAR 0.1647 / 0.2300 / 0.3306; GNN-HAR 0.1851 / 0.2470 / 0.2625; Pure-ST 0.1627 / 0.2242 / 0.2571; PGA-Trans-HAR 0.1588 / 0.2140 / 0.2452 (p. 10, Table 3).
- h = 1 MSE gains vs HAR significant in SPX, DAX, CAC, FTSE, OMX; at h = 5 essentially none; at h = 22 only HSI (p. 12, Table 6).
- Market-level gains are lead-dependent: FTSE +4.5% at h = 1 but −1.5% at h = 22 (p. 13, Table 8).
- Retained in 47 of 48 MSE MCS cells; seed SD of MSE 0.00057 vs 0.0373 for GNN-HAR (pp. 1, 12).
- Economic value: annual CER gain of 7.9–9.3 bps vs HAR (p. 1).

## Limits and risks to validity
_My assessment:_ gains are small and concentrated at the 1-day lead; one test period without a crash; range volatility from Yahoo data, not realised variance. The finding that cross-market information must be anchored and bounded is the transferable part. Code public.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Single chronological split with refit |
| Baselines | 2 | HAR, VHAR and graph/attention neural benchmarks |
| Point-in-time and leakage controls | 1 | Past-only graphs and masks; vendor data not checked |
| Costs and realism | 1 | Flat cost scenarios for an exposure rule |
| Sample breadth | 1 | Eight indices; test 2022–26, no crash |
| Statistical testing | 2 | HAC DM with Holm correction; MCS |
| Reproducibility | 1 | Code public; public data source |
| **Total** | **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Adding foreign-market predictors therefore does not automatically improve forecasts." (p. 9)
