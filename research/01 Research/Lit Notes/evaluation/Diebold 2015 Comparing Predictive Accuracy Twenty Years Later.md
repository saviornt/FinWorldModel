---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- forecast-comparison
title: 'Comparing Predictive Accuracy, Twenty Years Later: A Personal Perspective on the Use and Abuse of Diebold–Mariano Tests'
authors:
- Francis X. Diebold
year: 2015
venue: Journal of Business & Economic Statistics 33(1); NBER WP 18391 (2012)
source_url: https://www.nber.org/papers/w18391.pdf
doi: 10.1080/07350015.2014.983236
research_questions:
- RQ4.2
evidence: Weak
score: 2
---
# Comparing Predictive Accuracy, Twenty Years Later (Diebold, 2015)

**Basis:** NBER Working Paper 18391 (2012) PDF, read 2026-11-08 through a summarising page fetch; the JBES version was not opened.

**Takeaway:** The DM test compares forecasts, not models; its only assumption is a covariance-stationary loss differential; for comparing models, full-sample methods (F/LR tests, information criteria, Bayes factors, MCS) are more efficient, and pseudo-out-of-sample splits are not a reliable guard against overfitting, though they remain useful for studying historical episodes with real-time vintages.

## Problem
Widespread use of DM-type tests to compare models in pseudo-out-of-sample (PSOS) designs (abstract, §1).

## Data and period
None: methodological essay.

## Method
Argument from the statistics of DM, West (1996) and Clark–McCracken frameworks, and classical model selection (§2–§4).

## Baselines and validation
Not applicable.

## Results (with page or section references)
- DM is an asymptotic z-test on the mean loss differential with a HAC standard error; Assumption DM is covariance stationarity of the differential, checkable in data (§2, pp. 2–4).
- Comparing models through forecasts needs model-specific assumptions; parameter estimation can make the differential non-stationary (§3, pp. 4–6).
- For nested models the full-sample F-test is uniformly most powerful, so out-of-sample procedures are suboptimal (p. 6).
- AIC/SIC guard against overfitting by penalising fit, not by splitting; choosing the split point adds data-mining risk (pp. 8–11).
- Recommends DM for forecasts, full-sample procedures incl. MCS for models, PSOS for episode analysis with real-time vintages (§4.2, §5, pp. 12–13).

## Limits and risks to validity
_My assessment:_ an expert perspective, not empirical evidence. Its case for full-sample model comparison assumes a fixed, correctly treated sample; it does not address the large flexible ML model searches and look-ahead problems this project faces, where an untouched causal test is the practical safeguard (see [[RP3 Cleaning and Labelling]]). Read via a summarising fetch.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Essay |
| Baselines | 0 | None |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 0 | No data |
| Statistical testing | 1 | Discusses test theory, no tests run |
| Reproducibility | 0 | None |
| **Total** | 1/8 → **2/14** | Weak (expert perspective; cited for definitions and scope) |

## Quotes worth keeping (each under 15 words, with page)
- "DM is a test for comparing forecasts, not models." (§2, p. 2)
