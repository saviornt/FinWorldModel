---
type: lit-note
title: "The social signal"
authors: [J. A. Cookson, R. Lu, W. Mullins, M. Niessner]
year: 2024
venue: Journal of Financial Economics 158, 103870
source_url: https://tony91782.github.io/hkust-ai-and-workflows/demos/Social%20Signal%20Demo/the_social_signal.pdf
doi: 10.1016/j.jfineco.2024.103870
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.3, RQ1.5]
family: [sentiment]
evidence: Strong
score: 11
tags: [lit-note, family/sentiment]
---
# The Social Signal (Cookson, 2024)

**Basis:** published JFE PDF hosted by the first author, read through page fetch up to p. 18 (later pages not covered).

**Takeaway:** Across Twitter, StockTwits and Seeking Alpha, the common sentiment factor predicts positive next-day abnormal returns (≈ 6 bp per SD) that do not reverse over 20 days, while the common attention factor predicts negative next-day returns (≈ −13 bp per SD) that partly reverse; WSB attention, not WSB sentiment, carries signal.

## Problem
Is social-media sentiment and attention common across platforms, and what does each predict for returns once news and disclosures are controlled?

## Data and period
Twitter (Social Market Analytics), StockTwits (all single-firm messages) and Seeking Alpha (RavenPack); top 1,500 StockTwits firms, 2012–2021, ~815,000 firm-days (pp. 4–6, Table 1).

## Method
PCA of sentiment and of attention across platforms, also conditional on Dow Jones news, 8-Ks and earnings; next-day abnormal return regressions with firm and date FE, ten lags, news controls, Google ASVI; cumulative returns to t+20 (pp. 7–12).

## Baselines and validation
Dow Jones news sentiment and attention as the news benchmark; rolling 1-year PCA to rule out look-ahead (p. 13). No trading strategy or costs in the pages read.

## Results (with page or section references)
- Sentiment PC1 explains ~39% of cross-platform variation (33% if independent); attention PC1 ~67% (pp. 7–8).
- Next-day abnormal return: sentiment PC1 +0.061 (≈ 6 bp/SD), attention PC1 −0.131 (≈ −13 bp/SD); DJ news sentiment ≈ 8 bp/SD (Table 6, pp. 10–11).
- Sentiment effect persists to t+20 without reversal; attention's same-day gain partly reverses over 10–20 days (Fig. 3, Table 7, pp. 11–12).
- WSB attention predicts positive next-day returns; WSB sentiment does not (p. 13).
- After the Jan 2021 GameStop episode, sentiment's next-day power dropped by ~12.5 bp/SD, mainly among new users (Table 9, pp. 17–18).

## Limits and risks to validity
_My assessment:_ predictive panel regressions, not a costed strategy; effects of a few bp per day are small next to trading costs for many names. Pages after 18 not read.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Predictive regressions; rolling PCA check |
| Baselines | 1 | News sentiment/attention and rich controls; no ML baseline |
| Point-in-time and leakage controls | 2 | Explicit look-ahead check, disclosure controls |
| Costs and realism | N/A | No strategy reported in pages read |
| Sample breadth | 2 | 1,500 firms, 2012–2021 incl. 2020 |
| Statistical testing | 1 | Clustered SEs, no correction |
| Reproducibility | 2 | Code and data released |
| **Total** | **9/12 → 11/14** | Strong (10.5 rounded up) |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (page fetch summary only).
