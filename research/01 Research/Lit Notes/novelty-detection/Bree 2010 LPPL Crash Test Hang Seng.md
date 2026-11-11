---
type: lit-note
title: "Testing for financial crashes using the Log Periodic Power Law model"
authors: [David S. Brée, Nathan Lael Joseph]
year: 2010
venue: arXiv (q-fin.ST), v2 2013
source_url: https://arxiv.org/abs/1002.1010
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.8]
family: [novelty-detection]
evidence: Weak
score: 4
tags: [lit-note, family/novelty-detection]
---
# Testing for financial crashes using the LPPL model (Brée, 2010)

**Basis:** arXiv v2 (13 Apr 2013) read through alphaXiv page excerpts (pp. 1, 3–6, 10–13, 16, 19, 21–24). Authors from the arXiv abstract page; journal version not identified.

**Takeaway:** Re-fitting the log-periodic power law (LPPL) bubble model to 11 Hang Seng crashes (1970–2008), the best fits fall inside the "crash" parameter ranges for only 7 of 11; two of the three crashes not used to set those ranges fail; the fit is very sensitive to one parameter (ω); and the model's claimed martingale mechanism is contradicted by its own fits — so LPPL crash-timing claims are, at best, partly supported.

## Problem
Do LPPL fits to pre-crash bubbles have parameters in fixed ranges that identify coming crashes, and is the stated mechanism (imitation plus a martingale condition) consistent with the fits (pp. 1, 5–6)?

## Data and period
Hang Seng daily index, 1 Jan 1970–31 Dec 2008, 10,152 daily changes (p. 13); 11 crashes identified by a stated peak rule (pp. 13, 22).

## Method
Seven-parameter LPPL fit by grid search plus Nelder–Mead (pp. 10–11); comparison with the Johansen–Sornette (JS) fits; test that the fitted hazard rate stays positive (expected price always rising) (p. 10); RMSE sensitivity to each parameter (p. 19).

## Baselines and validation
None against other crash predictors. Crashes after the JS studies (2000, 2007) act as a post-hoc test of the parameter ranges (p. 16).

## Results (with page or section references)
- In the earlier JS fits, the LPPL slopes downward at times in 18 of 30 cases, which rejects the martingale mechanism (p. 12).
- Forcing a positive hazard rate on Dow Jones windows (1912–2000) predicted a crash within a year in only 65 of 229 windows that were followed by one (cited from Graf v. Bothmer & Meister, p. 10).
- Best fits within the crash ranges for 7 of 11 bubbles; 1973 and 2000 have no fit in range; 1981 needs β > 1 to be ruled out (p. 24).
- The 2007 bubble's best fit predicted the crash on the day it happened (p. 23).
- RMSE is highly sensitive to small changes in ω, so the search is unreliable (pp. 19, 24).
- Bubble start dates were moved "by eye" in half the JS data sets (p. 24); earlier ex-ante predictions were right once and wrong once (Laloux et al., cited p. 4).

## Limits and risks to validity
_My assessment:_ one market, one model family, no false-alarm test (bubbles that did not crash are not fitted). It is a replication critique rather than a forecasting study, but it is the clearest evidence read that the best-known "crash timing" model is fragile.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Post-hoc test on 2000 and 2007 only |
| Baselines | 0 | None |
| Point-in-time and leakage controls | 1 | Discusses real-time trough choice; JS start dates chosen ex post |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | One index, 1970–2008, 11 crashes |
| Statistical testing | 0 | No goodness-of-fit or significance tests |
| Reproducibility | 0 | Datastream data; no code noted |
| **Total** | **3/12 → 4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "the RMSE is highly sensitive to small fluctuations in the value chosen for ω" (p. 19)
