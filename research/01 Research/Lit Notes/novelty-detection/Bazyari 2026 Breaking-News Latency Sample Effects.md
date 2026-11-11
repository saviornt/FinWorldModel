---
type: lit-note
title: 'Same Pipeline, Opposite Conclusions: Sample-Surface Effects in Breaking-News Latency'
authors:
- Farhad Bazyari
- Xianghang Liu
- Sean Moran
year: 2026
venue: arXiv 2605.21521
source_url: https://arxiv.org/abs/2605.21521
doi: ''
accessed: 2026-11-08
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ1.12
- RQ3.2
family:
- novelty-detection
evidence: Weak
score: 2
tags:
- lit-note
- family/novelty-detection
- information-diffusion
---
# Same Pipeline, Opposite Conclusions: Sample-Surface Effects in Breaking-News Latency (Bazyari, 2026)

**Basis:** v1 (18 May 2026), full text via alphaXiv (pp. 1–5).

**Takeaway:** Whether X or news outlets report breaking events first depends on which events are sampled: news led X by a median 21.6 minutes on encyclopedic events (n = 6 paired) but the two were tied within seconds on prediction-market events (n = 16), and a third of earliest reports came from other platforms (Bluesky, Facebook, YouTube).

## Problem
Which channel reports breaking news first in 2026?

## Data and period
Sample A: 50 Wikipedia Current Events items (Apr–May 2026); Sample B: 109 Polymarket events (Feb–May 2026) with news time pinned to the largest 1-hour volume spike; mentions from one commercial social-listening provider across nine channels; X times decoded from tweet IDs (pp. 2–3).

## Method
Same pipeline for both samples: LLM-drafted boolean queries, provider pulls, on-topic verification (p. 3).

## Baselines and validation
Descriptive cross-sample comparison; tiny paired cells.

## Results (with page or section references)
- Sample A: news before X in all 6 paired events, median 21.6 min (IQR 10–33) (Table 3).
- Sample B: median −0.02 min; 8 of 16 within 0.2 min; X first in 38% (Table 4).
- Earliest-channel share: news 53% vs 27%; X 16% vs 38%; other social channels 32–34% (Table 2).
- 24% of pageview-ranked US events had no on-topic evidence in the provider's index (p. 3).

## Limits and risks to validity
_My assessment:_ not about markets; very small paired samples; one provider with redacted fields. Useful as a measurement warning: "first report" timing depends on sampling and on vendor coverage gaps.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Descriptive |
| Baselines | 0 | None |
| Point-in-time and leakage controls | 1 | Millisecond X timestamps from IDs |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 159 events, 3 months |
| Statistical testing | 0 | None |
| Reproducibility | 0 | Commercial provider |
| **Total** | **2/12 → 2/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- "The X-vs-news direction depends on the sample." (p. 1)
