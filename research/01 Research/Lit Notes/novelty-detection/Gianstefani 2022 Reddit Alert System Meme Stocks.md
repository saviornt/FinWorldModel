---
type: lit-note
title: "The echo chamber effect resounds on financial markets: a social media alert system for meme stocks"
authors: [Ilaria Gianstefani, Luigi Longo, Massimo Riccaboni]
year: 2022
venue: arXiv (q-fin.TR)
source_url: https://arxiv.org/abs/2203.13790
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.5, RQ1.11]
family: [novelty-detection, sentiment]
evidence: Weak
score: 2
tags: [lit-note, family/novelty-detection, family/sentiment]
---
# The echo chamber effect resounds on financial markets: a social media alert system for meme stocks (Gianstefani, 2022)

**Basis:** arXiv v1 read through alphaXiv page excerpts (pp. 1, 7–15, 18–19, 22–27, 31–36, 40–41).

**Takeaway:** A two-stage Reddit alert (unusual ticker activity, then a recurring influencer at the hub of the thread network) fired 21 times for GME and 4 for AMC over nine months and was followed by positive abnormal returns for meme stocks only; it is a retrospective event study on four stocks with no false-alarm rate or lead-time statistics.

## Problem
Can unusual, coordinated activity on r/WallStreetBets give an early warning of destabilising price moves?

## Data and period
r/WallStreetBets posts and comment trees mentioning GME, AMC, AAPL, MSFT, Oct 2020–Jun 2021, via PRAW; moderator bots excluded; daily prices and volume (pp. 6–7).

## Method
Stage 1: at least four of six activity variables (ticker share of posts and users, absolute counts, day-on-day change) exceed a threshold of the 10-day mean plus one mean absolute deviation, or doubling for the change variables (pp. 11–12). Stage 2: a top in-degree author of the day is also in the PageRank top 20 over the previous 20 days (p. 14). Market-model event study, estimation window [−21, −11], event window [−10, 10]; HAC regressions (pp. 14, 17, 21).

## Baselines and validation
Non-meme stocks (AAPL, MSFT) act as controls. No out-of-sample period, no baseline signal (e.g. volume or price spikes alone), no hit or false-alarm rates.

## Results (with page or section references)
- Alerts: GME 21, AMC 4, AAPL 2, MSFT 1 (Table 1, p. 18); 8/4/2/1 events after imposing 10-day spacing (p. 17).
- Significant abnormal returns after alerts for GME and AMC only; non-meme alerts give no clear trend (pp. 18, 22).
- AMC price rose about sevenfold in ten days after the 19 May 2021 alert (p. 17).
- Predictive regression: lagged subreddit rank and Robinhood outage reports predict GME and AMC abnormal returns (adj. R² 0.24, 0.21; Table 6, p. 32).

## Limits and risks to validity
_My assessment:_ in-sample, four stocks, the most extreme meme episode in history; the event with the largest abnormal return is the one reported (p. 17), which selects on the outcome. Reddit data downloaded later may miss deleted posts. Lead time is not measured: many GME alerts fire during the squeeze rather than before it. Useful as a design idea (volume burst plus influencer-network test), not as evidence of early warning.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Retrospective event study, same period |
| Baselines | 0 | Control stocks only, no competing signal |
| Point-in-time and leakage controls | 1 | Thresholds use past 10/20 days; retrospective API pull |
| Costs and realism | N/A | No strategy |
| Sample breadth | 0 | Four stocks, nine months |
| Statistical testing | 1 | Event-study tests, HAC errors |
| Reproducibility | 0 | No code or data release seen |
| **Total** | **2/12 → 2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "we devise an early warning signal to detect suspicious users' social network activity" (p. 1)
