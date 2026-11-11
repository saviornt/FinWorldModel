---
type: lit-note
title: "Do Cryptocurrency Markets Differentiate Infrastructure from Regulatory Shocks? A Multi-Moment Event Study with Dependence-Robust Inference"
authors: [Murad Farzulla]
year: 2026
venue: Digital Finance (forthcoming); arXiv (q-fin.ST) 2602.07046 v5
source_url: https://arxiv.org/abs/2602.07046
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.5]
family: [evaluation]
evidence: Moderate
score: 8
tags: [lit-note, family/evaluation, event-study, negative-result]
---
# Crypto Shocks Event Study with Dependence-Robust Inference (Farzulla, 2026)

**Basis:** Full text (pp. 1–7, 9, 28) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** The author's own earlier "5.7×, p ≈ 0.001" finding that crypto variance reacts more to infrastructure than regulatory shocks does not survive: treating six correlated assets as independent was pseudoreplication (a naive test rejects 35.1% of true nulls at 5%), and the effect shrinks from 3.49× under curated, high-salience event selection to about 0.5–1.6× under a mechanical screen.

## Problem
Whether markets process infrastructure and regulatory shocks differently, and how event selection and dependence change the inference (§1).

## Data and period
50 events (26 infrastructure, 24 regulatory), six cryptocurrencies, January 2019–August 2025; events dated by the UTC day the information became public, verified against primary sources (one dating error caught) (§3.1).

## Method
Constant-mean CARs over [−5, +30] with event-level block bootstrap; GJR-GARCH-X variance responses with a Student-t-copula bootstrap; "inference ladder" of seven procedures; Monte-Carlo calibration; inclusion-rule sensitivity over a reconstructed candidate pool (§3, §6).

## Baselines and validation
Market model on BTC as robustness; event-level Welch test; BH-FDR across 18 weekly Granger tests (§3.2, §3.4).

## Results (with page or section references)
- First moment: CAR difference +8.69 pp, bootstrap p = 0.202; minimum detectable effect ≈ 19 pp at 80% power (p. 2).
- Second moment: 3.49× multiplier, t-copula bootstrap p = 0.389; recursive sensitivity one-sided p = 0.025–0.041 (pp. 2–3).
- Naive i.i.d. rule rejects 35.1% of true-null panels at 5%; copula rule 4.6% (p. 3).
- Curated events: 3.49×; mechanical impact screen on a broad pool: ≈0.5–1.6×; 13 of the curated 50 fail the strict screen (pp. 3, 6).
- Asset correlations 0.54–0.83, effective sample size of the six contrasts 1.33–2.35 (pp. 1, 3).

## Limits and risks to validity
_My assessment:_ small, crypto-only sample; single author; a self-correction, which makes it unusually candid. Key lessons for shock studies: event inclusion is a researcher degree of freedom that must be fixed by a mechanical rule; correlated assets sharing event dates are not independent replications; date events by first public information.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Event study, not a forecast |
| Baselines | 1 | Constant-mean and market models |
| Point-in-time and leakage controls | 2 | UTC first-public dating checked against primary sources |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Six assets, 50 events |
| Statistical testing | 2 | Dependence-aware bootstraps, FDR, calibration study |
| Reproducibility | 0 | Code release not stated in pages read |
| **Total** | 6/10 → **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "treating event inclusion as an explicit design parameter" (p. 1)
