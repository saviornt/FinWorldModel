---
type: lit-note
title: "Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction"
authors: [Dehao Dai, Ding Ma, Dou Liu, Kerui Geng, Yiqing Wang]
year: 2026
venue: arXiv 2603.11408
source_url: https://arxiv.org/abs/2603.11408
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.14]
family: [sentiment]
evidence: Weak
score: 2
tags: [lit-note, family/sentiment]
---
# Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures (Dai, 2026)

**Basis:** v2 (16 Mar 2026), page excerpts via alphaXiv (pp. 1, 3, 5–21).

**Takeaway:** For weekly WTI direction (2020–2025, 314 weeks), five prompted dimensions (relevance, polarity, intensity, uncertainty, forwardness) from GPT-4o plus FinBERT polarity gave the best AUC (0.652 vs 0.569 for the vendor polarity score), with intensity, uncertainty change and FinBERT polarity dispersion as the top SHAP features; but the sample is tiny, there is no price-only baseline, and GPT-4o's training data covers most of the test period.

## Problem
Do dimensions beyond polarity add predictive content for a commodity's weekly return direction?

## Data and period
Alpha Vantage News API, energy topic, 29,153 articles 2020–2025; 20% stratified sample (8,639) scored; WTI front-month weekly returns (pp. 6–7).

## Method
GPT-4o and Llama-3.2-3B prompted for five continuous dimensions; FinBERT polarity and intensity; Alpha Vantage score; relevance-weighted weekly means, within-week dispersion, week-on-week changes; 31 features; LightGBM with Optuna (pp. 7–10, App. A–B).

## Baselines and validation
Alpha Vantage score only; FinBERT + AV. Five-fold time-series CV (p. 15). No price features, no random walk, no costs, no tests.

## Results (with page or section references)
- AUC / IC: AV 0.569 / 0.091; AV + FinBERT 0.620 / 0.157; GPT-4o 0.634 / 0.249; Llama-3.2-3B 0.589 / 0.115; GPT + FinBERT 0.652 / 0.228 (Table 4, p. 15).
- Top SHAP: GPT intensity mean, FinBERT polarity standard deviation, GPT uncertainty momentum; article counts negligible (p. 16).
- Polarity correlations across scorers only 0.47–0.68 (p. 13).

## Limits and risks to validity
_My assessment:_ ~60 test weeks per fold, std of AUC across folds 0.05–0.10, so differences between feature sets are within noise; GPT-4o pre-cutoff for 2020–2023 with no memorisation control; single source and asset. The dispersion finding agrees with [[Zhang 2025 GDELT FinBERT Macro Alpha]].

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Time-series CV |
| Baselines | 0 | Vendor sentiment only; no price baseline |
| Point-in-time and leakage controls | 0 | LLM pre-cutoff |
| Costs and realism | 0 | None |
| Sample breadth | 0 | One asset, 6 years |
| Statistical testing | 0 | Fold std only |
| Reproducibility | 0 | Prompt only |
| **Total** | **2/14 → capped Weak** | Rubric cap: LLM used on events before its cutoff |

## Quotes worth keeping (each under 15 words, with page)
- "article volume alone adds little incremental predictive content" (p. 17)
