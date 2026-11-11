---
type: lit-note
title: 'AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation'
authors:
- Sandeep Neela
year: 2025
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2512.16103
doi: ''
accessed: 2026-11-07
papers:
- '[[RP1 ML Methods]]'
- '[[RP4 Training and Evaluation]]'
research_questions:
- RQ1.5
- RQ1.11
- RQ4.3
family:
- novelty-detection
- fusion
evidence: Weak
score: 4
tags:
- lit-note
- family/novelty-detection
- family/fusion
---
# AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation (Neela, 2025)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1, 12, 15, 17–23, 28, 32, 37).

**Takeaway:** A heuristic Reddit-plus-price "manipulation risk score" flagged GME about 22 days before the January 2021 peak at a relaxed threshold, but the social features are **synthetic** (Reddit history unavailable), only 3 positive events exist, weights were tuned with hindsight on GME, and a price-only anomaly rule discriminated better (AUC 0.863 vs 0.647).

## Problem
Can fused social-media coordination, bot and sentiment features plus market data warn of social-media-driven manipulation before it shows in prices?

## Data and period
AIMM-GT: 33 labelled ticker-days across eight equities (3 positive events: GME, AMC, BB, Jan–Jun 2021). Market data real (Yahoo Finance); social features are "calibrated synthetic" features because of Reddit API limits (pp. 1, 21–22).

## Method
Weighted average of component scores (social volume, bot-likeness, near-duplicate coordination, FinBERT/VADER sentiment, market anomalies) with expanding-window normalisation (p. 28). Lead time = trading days from first above-threshold alert to labelled event start (p. 12). Threat model covers botnets, brigades, influencers, microcaps (p. 20).

## Baselines and validation
Forward-walk evaluation on the 33 days; four rule baselines on the GME window (social volume threshold, sentiment threshold, combined, market anomaly) (pp. 12, 19).

## Results (with page or section references)
- At default threshold 0.5: TP 0, FP 0, TN 30, FN 3; ROC-AUC 0.99, PR-AUC 0.83 (Table 1, p. 12).
- At 0.20: 3/3 detected, 0 false positives, which the author calls "suspiciously good" (Table 2, p. 15).
- One of three events detected pre-event; median lead time a few trading days (p. 18).
- GME window: AIMM AUC 0.647, lead 9 days; market-anomaly rule AUC 0.863, lead 0; social volume alone AUC 0.558; sentiment alone fires 5 days late (Table 3, p. 20).
- Statistical power about 15% with n = 3 (p. 22).

## Limits and risks to validity
_My assessment:_ not empirical evidence on real social data. Synthetic features "matching documented event characteristics" encode the answer. Hindsight-tuned weights and labelled windows. Useful only for its lead-time definition and the observation that social signals may lead, while price anomalies discriminate better once the event is under way. Code promised "upon acceptance".

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Forward walk over 33 days |
| Baselines | 1 | Simple rule baselines |
| Point-in-time and leakage controls | 1 | Expanding normalisation; hindsight weights and synthetic social data |
| Costs and realism | N/A | No trading |
| Sample breadth | 0 | 3 events, 2021 only |
| Statistical testing | 0 | Underpowered, none |
| Reproducibility | 0 | Code and data promised, not released |
| **Total** | **3/12 → 4/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "we employ calibrated synthetic social features matching documented event characteristics" (p. 1)
