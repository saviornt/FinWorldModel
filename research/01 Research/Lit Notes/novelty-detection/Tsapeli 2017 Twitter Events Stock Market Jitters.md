---
type: lit-note
title: "Linking Twitter Events With Stock Market Jitters"
authors: [Fani Tsapeli, Nikolaos Bezirgiannidis, Peter Tino, Mirco Musolesi]
year: 2017
venue: arXiv (cs.SI)
source_url: https://arxiv.org/abs/1709.06519
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.5, RQ1.12]
family: [novelty-detection]
evidence: Moderate
score: 6
tags: [lit-note, family/novelty-detection]
---
# Linking Twitter Events With Stock Market Jitters (Tsapeli, 2017)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1–4, 9–10, 12–17).

**Takeaway:** Bursty-word Twitter events, filtered by a classifier trained on whether past events coincided with volatility jumps, detected intraday jitters in the Greek and Spanish indices in 2015 with F1 up to 0.74, versus about 0.25–0.33 for a general burst detector and 0.34–0.37 for sentiment-only events: raw bursts are mostly false alarms.

## Problem
Can event detection on Twitter flag events that will move a specific stock market, and is sentiment enough?

## Data and period
Tweets tracked by 158 European-debt-crisis keywords (extracted from the Wikipedia page on the crisis) mentioning Greece or Spain; ATHEX and IBEX 5-minute data, Mar–Nov 2015 (p. 10). 375 Greek and 349 Spanish Twitter events (p. 12).

## Method
Word arrival rates as inhomogeneous Poisson processes; burst when rate and slope exceed thresholds; event feature vectors (bursty words, polarity, geography, user profiles); feature selection and a classifier whose labels come from co-occurrence (within 1 hour) with a jump in volatility slope; classifier updated online once each true label is known (pp. 1–4, 9).

## Baselines and validation
First four months for parameters, remainder for evaluation with online updating (p. 10). Baselines: EDCoW general event detector (with its threshold tuned on test results, favouring it) and a sentiment-only detector (pp. 13–14).

## Results (with page or section references)
- FED precision / recall / F1: Greece 0.69 / 0.81 / 0.74; Spain 0.65 / 0.72 / 0.68 at the strictest jitter threshold (Table 3, p. 13).
- EDCoW F1 0.23–0.33; sentiment-only F1 0.34–0.37 with precision about 0.22 (Tables 4–5, pp. 14–15).
- All detected market events were flagged on Twitter before they appeared in the market, though not trained for it (p. 13); lead time is bounded by the 1-hour matching window and not quantified.
- Mutual information between FED events and jitters clearly exceeds the baselines' (p. 16).

## Limits and risks to validity
_My assessment:_ the keyword list was taken from a Wikipedia page written with hindsight about the crisis, which biases topic selection. One crisis year in two small markets. Lead time is minutes to an hour, not days. No volatility-persistence baseline (jitters cluster). Shows that burst counts and sentiment alone produce many false alarms; a learned filter on burst features is needed.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Train period then online walk-forward updating |
| Baselines | 1 | General burst and sentiment detectors; no volatility persistence |
| Point-in-time and leakage controls | 1 | Labels revealed after delay; hindsight keyword list |
| Costs and realism | N/A | Detection, no trading |
| Sample breadth | 1 | Two indices, 8 months, one crisis |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code or data |
| **Total** | **5/12 → 6/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "not feasible to detect Twitter events ... solely by searching for bursts" (p. 14)
