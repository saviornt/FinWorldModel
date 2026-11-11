---
type: lit-note
title: "Price Drift before U.S. Macroeconomic News: Private Information about Public Announcements?"
authors: [Alexander Kurov, Alessio Sancetta, Georg Strasser, Marketa Halova Wolfe]
year: 2019
venue: Journal of Financial and Quantitative Analysis
source_url: https://www.skidmore.edu/economics/documents/KSSW2017-PriceDriftBeforeUSMacroeconomicNews.pdf
doi: 10.1017/S0022109018000625
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, information-diffusion]
---
# Price Drift before U.S. Macroeconomic News (Kurov, 2019)

**Basis:** November 2017 draft ("forthcoming in JFQA"), read through a page-fetch summary; DOI not confirmed, left empty; year assumed 2019 from the forthcoming note (to check).

**Takeaway:** For 9 of 20 market-moving US macro releases, E-mini S&P 500 and 10-year Treasury futures start moving in the correct direction about 30 minutes before the official release, accounting for about 49% (stocks) and 36% (bonds) of the total adjustment; drift is stronger where release procedures are less secure.

## Problem
Is some macro news priced before its scheduled public release, and why?

## Data and period
Second-by-second E-mini S&P 500 and 10-year T-note futures, Jan 2008–Mar 2014, 30 announcements; minute data back to 2003 (pp. 1–2, 5, 8–10).

## Method
Event-time returns in pre-announcement windows; comparison across release procedures (embargo, lock-up, pre-release) (pp. 4, 27–31).

## Baselines and validation
Post-announcement adjustment; earlier minute-data period; release-procedure comparison. In-sample.

## Results (with page or section references)
- 9 of 20 market-moving releases show drift (all 9 in bonds, 4 in stocks); starts ~30 min before release (pp. 1, 17).
- Pre-release share of total adjustment ≈49% stocks, 36% bonds (pp. 15, 36).
- Stronger drift for pre-released ("embargo-only") announcements and agencies outside federal release guidelines (pp. 4, 27–31).
- Drift weaker in the pre-2008 sample (p. 2).

## Limits and risks to validity
_My assessment:_ two contracts, six years; explanation (leakage vs superior forecasting) unresolved.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample |
| Baselines | 1 | Post-release adjustment, earlier period |
| Point-in-time and leakage controls | 2 | Second-level timestamps vs official release times |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Two futures, 2008–2014 |
| Statistical testing | 1 | Significance tests |
| Reproducibility | 0 | Licensed tick data |
| **Total** | **5/12 → 6/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).

**Citation check (2026-11-08):** DOI 10.1017/S0022109018000625 confirmed through OpenAlex by the reference-lookup tool.
