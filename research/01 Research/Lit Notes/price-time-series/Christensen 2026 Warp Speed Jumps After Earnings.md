---
type: lit-note
title: 'Warp Speed Price Moves: Jumps after Earnings Announcements'
authors:
- Kim Christensen
- Allan Timmermann
- Bezirgen Veliyev
year: 2026
venue: arXiv 2601.08962 (econ.EM); published in Journal of Financial Economics
source_url: https://arxiv.org/abs/2601.08962
doi: 10.1016/j.jfineco.2025.104010
accessed: 2026-11-08
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ1.12
- RQ3.2
family:
- price-time-series
evidence: Moderate
score: 9
tags:
- lit-note
- family/price-time-series
- information-diffusion
---
# Warp Speed Price Moves: Jumps after Earnings Announcements (Christensen, 2026)

**Basis:** v1 (Nov 2024 draft posted 13 Jan 2026), pp. 1–2, 4, 6, 11, 17–18, 23–24, 40, 97 via alphaXiv. Journal not stated in the pages read.

**Takeaway:** For the 50 US stocks with most after-hours trading (2008–2020), prices jumped after 91% of earnings announcements (96% after 2016), and a post-announcement trading rule stopped earning anything after 2016 once spreads or a few seconds' delay were charged: public scheduled news is absorbed in seconds.

## Problem
Do prices of liquid stocks absorb earnings news at once (jumps), and can anyone trade on the adjustment?

## Data and period
TAQ tick data, 50 S&P 500 stocks, Jun 2008–Dec 2020 (3,169 days; ~89.6B quotes, ~8.0B trades), after-hours to 6:30pm; close-to-open test on all S&P 500 members 2012–2023 (pp. 17–18, 96).

## Method
New microstructure-noise-robust pre-averaged bipower-variation jump test; Bonferroni-corrected family-wise error 1% (pp. 10, 23); trading rule after announcements with frictionless, midquote, actual-spread and delayed execution (p. 4).

## Baselines and validation
Non-announcement sessions; classical 5-minute jump test; Monte Carlo size/power; subsamples 2008–15 vs 2016–20.

## Results (with page or section references)
- Jump frequency: 2.95% regular session, 3.67% after-hours without announcements, 91.06% after-hours with announcements (87.5% before 2016, 95.8% after) (p. 23).
- Jumps carry >50% of announcement-day variation (p. 24).
- Trading rule: 1.50% per trade at midquote, 0.72% at actual spreads, 0.41% with a 5-second delay, insignificant beyond; after 2016 insignificant with spreads, negative with delays (p. 4).
- Announcements raise co-jump probability in non-announcing firms and the market, more for early announcers and close industry peers (p. 40).

## Limits and risks to validity
_My assessment:_ 50 of the most liquid names chosen by later index membership; speed for less liquid stocks is likely slower. Clean evidence that for scheduled numeric news the "priced-in" window is seconds.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Subsample split |
| Baselines | 1 | Non-announcement sessions, classic test |
| Point-in-time and leakage controls | 2 | Tick timestamps; delays tested |
| Costs and realism | 2 | Spreads and execution delays |
| Sample breadth | 1 | 50 stocks, 2008–2020 incl. stress |
| Statistical testing | 2 | Bonferroni-corrected tests |
| Reproducibility | 0 | Licensed TAQ data |
| **Total** | **9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "In markets where a minute can be an eternity" (p. 4)

**Citation check (2026-11-08):** DOI 10.1016/j.jfineco.2025.104010 confirmed through OpenAlex by the reference-lookup tool.
