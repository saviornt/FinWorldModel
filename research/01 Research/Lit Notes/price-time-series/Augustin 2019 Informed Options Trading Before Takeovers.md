---
type: lit-note
title: "Informed Options Trading prior to Takeover Announcements: Insider Trading?"
authors: [Patrick Augustin, Menachem Brenner, Marti G. Subrahmanyam]
year: 2019
venue: Management Science
source_url: https://pages.stern.nyu.edu/~mbrenner/research/brenner-patrick-subrahmanyam-informed-trading.pdf
doi: 10.1287/mnsc.2018.3122
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Moderate
score: 9
tags: [lit-note, family/price-time-series, information-diffusion, options]
---
# Informed Options Trading prior to Takeover Announcements (Augustin, 2019)

**Basis:** November 2017 author version, read through a page-fetch summary (first 100k of 107k characters).

**Takeaway:** About 25% of 1,859 US takeovers (1996–2012) show significant abnormal target-option volume in the 30 days before announcement, mainly in short-dated out-of-the-money calls and concentrated 5–10 days before; public news or rumours explain only ~9% of these cases and the SEC litigated ~8% of deals.

## Problem
How common is informed (pre-announcement) options trading before M&A news, and can public information explain it?

## Data and period
1,859 US takeovers, Jan 1996–Dec 2012, with target stock and option data (pp. 1, 8–9).

## Method
Market model of option volume with controls (lagged volume, market option volume, VIX, returns); estimation window −90 to −30 days, event window −30 to −1; matched control firms; Barras–Scaillet–Wermers multiple-testing adjustment; RavenPack news; logits for volume and litigation (pp. 11–14, 19–33).

## Baselines and validation
Matched controls and random dates; news, insider-filing, 13D and stock-leakage checks.

## Results (with page or section references)
- 467 deals (≈25%) with abnormal call volume at 5%; 304 for puts; OTM calls highest (p. 12).
- Most activity 5–10 days before announcement; litigated trades median 11 days before (pp. 3–4, 30).
- RavenPack news linked to 40 of 467 flagged deals (≈9%); abnormal volume similar with and without news (pp. 22–23).
- ≈44% of deals show excess implied volatility (p. 3); SEC litigates ≈8% of deals, unrelated to abnormal volume (pp. 3–4, 33).

## Limits and risks to validity
_My assessment:_ event study, not a forecast; M&A targets only. Shows options can price corporate news days before any public report.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Event study |
| Baselines | 2 | Matched controls, random dates |
| Point-in-time and leakage controls | 2 | Pre-event windows, news timing checked |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | 1,859 deals, 17 years incl. 2000–02, 2008 |
| Statistical testing | 2 | Multiple-testing adjustment |
| Reproducibility | 0 | Licensed data |
| **Total** | **8/12 → 9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).
