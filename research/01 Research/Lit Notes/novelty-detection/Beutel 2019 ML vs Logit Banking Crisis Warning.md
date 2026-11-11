---
type: lit-note
title: 'An Evaluation of Early Warning Models for Systemic Banking Crises: Does Machine Learning Improve Predictions?'
authors:
- Johannes Beutel
- Sophia List
- Gregor von Schweinitz
year: 2019
venue: IWH Discussion Paper 2/2019 (also Bundesbank DP 48/2018; published as "Does machine learning help us predict banking crises?", Journal of Financial Stability, 2019)
source_url: https://www.econstor.eu/bitstream/10419/191248/1/104687456X.pdf
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ1.8
- RQ4.5
- RQ4.3
family:
- novelty-detection
evidence: Moderate
score: 9
tags:
- lit-note
- family/novelty-detection
---
# An Evaluation of Early Warning Models for Systemic Banking Crises (Beutel, 2019)

**Basis:** IWH Discussion Paper 2/2019 read through alphaXiv page excerpts (pp. 4–5, 8, 17–18, 20–21, 26, and appendix tables pp. 48–49, 51). The Journal of Financial Stability version was not opened (its title and abstract were seen on the IWH page); its DOI was not shown and is left blank.

**Takeaway:** In recursive quasi-real-time forecasts (2005Q3–2016Q4) of systemic banking crises 5–12 quarters ahead in 15 advanced economies, random forests, kNN, SVMs and trees reach near-perfect in-sample fit but are beaten out of sample by a plain logit, often doing worse than a naive forecast; even the true model would miss crises, because crises can only be predicted in probability.

## Problem
Do machine learning methods improve early warning of systemic banking crises compared with a logit, once tested out of sample?

## Data and period
15 advanced economies, 1970–2016; ESCB/ESRB crisis database extended with Laeven & Valencia for the US and Japan (p. 26). Four predictor sets: credit/asset prices, macro, external imbalances, all (p. 17). Target: crisis starting in the next 5–12 quarters (p. 8).

## Method
Logit vs random forest, SVM, kNN, decision trees, all on the same pooled panel (pp. 4–5, 8). Hyperparameters by a cross-validation that respects cross-sectional and serial correlation and uses only pre-2005Q3 data; CV is not used for evaluation (p. 8). Recursive re-estimation each quarter from 2005Q3 to 2016Q4, about 300 out-of-sample observations including 60 pre-crisis periods (p. 18). Metrics: relative usefulness, AUC, Brier score; bootstrap significance (pp. 5, 17–18).

## Baselines and validation
Logit and a naive forecast; recursive out-of-sample; bootstrap confidence bands; robustness to preference parameter, transformation, sample length and crisis database (pp. 18, 20).

## Results (with page or section references)
- In sample, RF and kNN reach relative usefulness 0.69–1.00, logit 0.20–0.51 (Table 3, p. 17).
- Out of sample, logit is best on three of four sets: all variables logit 0.605 vs trees 0.126, kNN −0.062, RF −0.003, SVM −0.186 (Table 4, p. 18). On the macro set every method is negative, i.e. worse than a naive forecast (p. 18).
- ML performance on credit/asset, external and all-variable sets is significantly worse than logit on all three metrics (p. 18).
- With the Laeven–Valencia database, logit (all variables) keeps relative usefulness 0.527, AUC 0.770; RF 0.062, AUC 0.629 (Table C.6, p. 51).
- Even the true data-generating process misses crises: a DSGE simulation with true probabilities still misses about one third (p. 21).
- Restricting to statistically significant signals leaves five false positives and six false negatives out of sample (p. 26).
- Key predictors: credit expansions, asset price booms, external imbalances; a logit would have warned before 2007/08 in many countries (p. 26).

## Limits and risks to validity
_My assessment:_ the out-of-sample window is dominated by one global crisis, so the 60 "pre-crisis" observations are not independent. Macro data revisions and publication lags were not checked in the pages read. Deep networks were not tested (p. 8, footnote). The lesson transfers: with tens of events, flexible models overfit, and a simple, regularised model is hard to beat.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Recursive quarterly re-estimation; CV only pre-sample |
| Baselines | 2 | Logit and naive forecast vs four ML methods |
| Point-in-time and leakage controls | 1 | Strict time split; data vintages not addressed in pages read |
| Costs and realism | N/A | Policy warning, no trading claim |
| Sample breadth | 2 | 15 countries, 1970–2016, incl. GFC |
| Statistical testing | 1 | Bootstrap significance; no multiple-testing correction |
| Reproducibility | 0 | Code not mentioned in pages read |
| **Total** | **8/12 → 9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the logit approach is surprisingly hard to beat" (p. 26)
