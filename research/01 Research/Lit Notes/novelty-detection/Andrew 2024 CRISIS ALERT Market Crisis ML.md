---
type: lit-note
title: "CRISIS ALERT: Forecasting Stock Market Crisis Events Using Machine Learning Methods"
authors: [Xingyi Andrew, Yue Chen, Salintip Supasanya]
year: 2024
venue: arXiv
source_url: https://arxiv.org/abs/2401.06172
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ1.5, RQ1.8, RQ3.5]
family: [novelty-detection]
evidence: Weak
score: 2
tags: [lit-note, family/novelty-detection]
---
# CRISIS ALERT: Forecasting Stock Market Crisis Events Using Machine Learning Methods (Andrew, 2024)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1–14, full paper). A class project that follows Chatzis et al. (2018, Expert Systems with Applications), which was not opened.

**Takeaway:** Price- and macro-only random forest and XGBoost models predicting next-day 1st-percentile index drops (2014–2022 test) catch 18/19 crisis days with 110 false alarms (RF) or 12/19 with 4 (XGBoost); lagged VIX is the top feature, but a backward-fill step leaks future values.

## Problem
Can tree ensembles on market variables forecast one-day-ahead US stock market crisis days?

## Data and period
Bloomberg daily, Jan 2000–Feb 2022 (5,775 days): US indices, sector ETFs, FX, VIX, gold, oil, rates (19 variables, 75 features) (pp. 1–2).

## Method
Crisis day = index log return below the 1st percentile of the expanding empirical distribution (1.16% of days); label shifted one day ahead; LASSO feature selection (25 features); RF and XGBoost tuned by 5-fold CV; decision threshold 1/21 (false negatives weighted 20×) (pp. 3–6).

## Baselines and validation
Train 2000–2013, test 2014–Feb 2022 (one split). No naive baseline (e.g. VIX level rule or persistence). k-fold CV for tuning ignores time order. Missing values filled **backward then forward**, which uses future data (p. 2).

## Results (with page or section references)
- RF: 18 of 19 crisis days caught, 110 false alarms; XGBoost: 12 of 19, 4 false alarms (Table 2, p. 7).
- AUC RF 0.981, XGBoost 0.963; balanced accuracy 0.57 vs 0.87 (Table 3, p. 7).
- Lagged VIX (2–3 days) is the most important feature in both models; crises are persistent (pp. 5–6).

## Limits and risks to validity
_My assessment:_ leakage from backward filling and shuffled CV; one split; one-day horizon means "warning" is mostly volatility clustering after a crisis has begun. Useful only as a reminder that a VIX-persistence baseline is hard to beat for near-term crash days, and that any text-based warning should be compared with it.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split |
| Baselines | 0 | Two models compared with each other only |
| Point-in-time and leakage controls | 0 | Backward fill and shuffled CV leak future data |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | US market 2000–2022 incl. stress |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Bloomberg data, no code |
| **Total** | **2/12 → 2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "we use the backward first to fill in the gaps" (p. 2)
