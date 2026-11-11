---
type: lit-note
title: 'Survivorship Bias in Emerging Market Small-Cap Indices: Evidence from India''s NIFTY Smallcap 250'
authors:
- Harjot Singh Ranse
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2603.19380
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.1
- RQ3.3
family:
- cleaning
evidence: Moderate
score: 7
tags:
- lit-note
- family/cleaning
- survivorship
---
# Survivorship Bias in Emerging Market Small-Cap Indices (Ranse, 2026)

**Basis:** full text via alphaXiv, opened 2026-11-08 (executive summary, data and methods, results on bias size and significance).

**Takeaway:** Backtesting today's 252 NIFTY Smallcap 250 members over 2016–2025 overstates annual return by 4.94 points (26.17% vs 21.23%) and Sharpe by 0.097, because 82.5% of stocks ever in the index left it (16.1% delisted, 33.1% graduated, 33.2% demoted).

## Problem
How large is survivorship bias in an emerging-market small-cap index, and can history be reconstructed without official constituent lists?

## Data and period
NSE bhavcopy daily files (which keep delisted securities), September 2016 – 2025, 1,437 stocks, 2,459 trading days.

## Method
Rebuild quarterly index membership by market-cap ranking (about 85–90% historical accuracy claimed); compare equal-weight portfolios of current members against all historical members.

## Baselines and validation
Comparison of two universes; bootstrap of complete-portfolio returns.

## Results (with page or section references)
- Return bias 4.94 points a year (23.3% relative); Sharpe 1.160 vs 1.063 (executive summary, §4).
- All exit categories, not only delistings, contribute (abstract).

## Limits and risks to validity
Single author, one index, one nine-year period. Membership is reconstructed, not official. The significance claim is inconsistent: the survivor return "exceeds 97.8% of resamples" yet p < 0.001 is reported. Use the size, not the test.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Bias measurement |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | Explicit universe reconstruction |
| Costs and realism | N/A | |
| Sample breadth | 1 | One index, 2016–2025 (includes 2020) |
| Statistical testing | 0 | Reported p-value inconsistent with its own bootstrap |
| Reproducibility | 1 | Public exchange data; no code found |
| **Total** | 4/8 → **7/14** | Moderate (low end) |

## Quotes worth keeping (each under 15 words, with page)
- "Current index constituent lists create systematic upward bias." (executive summary)
