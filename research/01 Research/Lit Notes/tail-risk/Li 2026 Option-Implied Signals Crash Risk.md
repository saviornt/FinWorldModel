---
type: lit-note
title: "Option-Implied Signals and Crash Risk: Predictability and Machine-Learning Evidence from U.S. Equity Options, 2015–2026"
authors: [Baichuan Li, Mengxiao Wang]
year: 2026
venue: arXiv 2608.26115 (q-fin.ST)
source_url: https://arxiv.org/abs/2608.26115
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12, RQ1.6]
family: [tail-risk]
evidence: Moderate
score: 8
tags: [lit-note, family/tail-risk, information-diffusion, options]
---
# Option-Implied Signals and Crash Risk, 2015–2026 (Li, 2026)

**Basis:** v1 (May 2026), pp. 1, 3–5, 7–8, 11–16, 23, 26–27 via alphaXiv.

**Takeaway:** On 12.36M firm-days (10,026 underlyings, 2015–2026) the classic option smirk stopped predicting returns after 2022, while the IV spread and risk-neutral skewness stayed significant in every regime; firm-level option features forecast 5-day crashes in calm markets (AUC 0.71) but not in the 2020–22 macro-shock regime (AUC 0.56).

## Problem
Do option-implied signals still reveal information before it shows in stock prices, and does that hold across regimes?

## Data and period
OPRA end-of-day records for all US equity options, Jan 2015–Apr 2026, standard screens; regimes fixed ex ante: 2015–19, 2020–22, 2023–26 (pp. 5–8).

## Method
Two-way fixed-effects panel regressions with double-clustered SEs; OLS, Elastic Net, XGBoost on 18 option/liquidity features with annual expanding-window OOS (train to T−2, validate T−1, test T); crash flag = 5-day return below −3.09σ√5 (pp. 9–11).

## Baselines and validation
OLS and Elastic Net vs XGBoost; logit vs XGBoost for crashes; replication of Xing et al. smirk on 2015–17 (Table 2).

## Results (with page or section references)
- Smirk coefficient (next month): −0.023 (t −5.5), −0.015 (t −4.2), −0.006 (t −1.5) by regime; +0.016 at 3 months in 2023–26 (Table 3, p. 2).
- IV spread and risk-neutral skewness significant in every regime and specification (|t| > 4) (Tables 3–4).
- Unsigned put–call volume ratio weak everywhere (Table 3).
- XGBoost beats linear only in 2023–26 (R²OOS 1.29% vs 0.07%), driven by 2025 (3.55%); worse than linear in 2020–22 (p. 2).
- Crash AUC: 0.706 calm, 0.561 high-volatility, 0.665 recent (p. 21).

## Limits and risks to validity
_My assessment:_ no stock-side controls (size, momentum) beyond liquidity; crash split chronological 80/20 within regime; pre-registered robustness deferred; data proprietary. Useful as evidence that options carry anticipation, but it is regime-dependent.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Annual expanding walk-forward |
| Baselines | 1 | Linear models; no factor controls |
| Point-in-time and leakage controls | 1 | End-of-day data; no explicit checks |
| Costs and realism | N/A | Predictability, not trading |
| Sample breadth | 2 | 10,026 names, three regimes incl. 2020 |
| Statistical testing | 1 | Clustered t-stats, no multiple-testing correction |
| Reproducibility | 0 | Data and code on request only |
| **Total** | **7/12 → 8/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "option-implied predictability is real but regime-conditional" (p. 1)
