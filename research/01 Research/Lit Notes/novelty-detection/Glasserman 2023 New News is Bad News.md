---
type: lit-note
title: "New News is Bad News"
authors: [Paul Glasserman, Harry Mamaysky, Jimmy Qin]
year: 2023
venue: arXiv (q-fin.GN)
source_url: https://arxiv.org/abs/2309.05560
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.5, RQ1.8]
family: [novelty-detection, llm-text]
evidence: Moderate
score: 9
tags: [lit-note, family/novelty-detection, family/llm-text]
---
# New News is Bad News (Glasserman, 2023)

**Basis:** arXiv v1 (Sep 2023) read through alphaXiv page excerpts (pp. 1–3, 5, 7, 9, 13–15, 18, 24–25, 27, 31, 43).

**Takeaway:** A rise in the novelty of aggregate news text (entropy under a language model retrained monthly on 1.6 million Reuters articles) forecasts lower S&P 500 returns and weaker macro data over the next 12 months, and was the best out-of-sample return predictor among a long list including VIX, EPU and CAPE, though out-of-sample R² stays below 10%.

## Problem
Does a change in the distribution of news language, rather than its sentiment, predict market and macroeconomic outcomes?

## Data and period
Thomson Reuters News Feed Direct, Jan 1996–Dec 2022, English articles about S&P 500 firms; rewrites of the same story removed using the PNAC code (keeps first article in a chain); machine-generated alerts excluded (p. 6). Monthly frequency; first observation July 1997 (p. 13).

## Method
LSTM language model (177,488 parameters) retrained each month on the previous six months; entropy of month t articles scored with the model trained only on earlier months, so the measure was available in real time (pp. 12–13). ENT = change in average entropy over 12 months; decomposed into a news-innovation part (ENT_NEWS) and a model-update part (p. 23). Extends the n-gram unusual-news measure of Glasserman & Mamaysky (2019), which forecast volatility (pp. 1, 4).

## Baselines and validation
Rolling out-of-sample univariate regressions with estimation windows of 12–24 months, compared with the historical mean; competing predictors include Welch–Goyal variables, CAPE, cay, EPU, VIX², news sentiment, trailing returns and factor returns (pp. 2, 17–18).

## Results (with page or section references)
- In sample: +1 s.d. ENT predicts about −3% cumulative S&P 500 return over 12 months, with many controls (p. 2).
- Out of sample: ENT R² positive in 4 of 5 windows (0.024–0.051); ENT_NEWS positive in all 5 (0.060–0.096); most other predictors negative in every window (p. 17).
- ENT forecasts higher unemployment and volatility and lower industrial production, earnings and rates 12 months ahead (p. 30).
- Low correlation with EPU (0.115) and news sentiment (−0.280) (p. 13).
- Entropy peaks in Jan 2007 (Fannie/Freddie risk language), Nov 2010 (Ireland "default") before the words became common (p. 14).
- ENT_NEWS predictive sign varies over time; average coefficient only marginally significant (p. 23).

## Limits and risks to validity
_My assessment:_ a slow (monthly, 12-month horizon) aggregate signal, not an early alarm for a specific shock; no lead-time or false-alarm statistics. One market and about 300 monthly observations with overlapping 12-month returns. Many predictors compared without a multiple-testing correction. Licensed Reuters data, no code. Look-ahead in the text model is controlled (rolling retraining), which is a design to copy.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling-window model and forecasts |
| Baselines | 2 | Historical mean plus a large set of standard predictors incl. VIX |
| Point-in-time and leakage controls | 2 | Text model retrained only on past months; duplicates removed |
| Costs and realism | N/A | No strategy |
| Sample breadth | 1 | One market, 1997–2022 incl. GFC and COVID |
| Statistical testing | 1 | Significance tests, no multiple-testing correction |
| Reproducibility | 0 | Licensed data, no code |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "entropy is the best forecaster of year-ahead market returns out of a large set" (p. 30)
