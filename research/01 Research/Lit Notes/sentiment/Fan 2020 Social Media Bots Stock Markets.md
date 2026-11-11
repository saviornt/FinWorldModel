---
type: lit-note
title: "Social media bots and stock markets"
authors: [Rui Fan, Oleksandr Talavera, Vu Tran]
year: 2020
venue: European Financial Management
source_url: https://cronfa.swansea.ac.uk/Record/cronfa51887/Download/51887__15304__febafe4026154617a0363a2e105de2e4.pdf
doi: 10.1111/eufm.12245
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.11]
family: [sentiment]
evidence: Weak
score: 5
tags: [lit-note, family/sentiment, bots]
---
# Social media bots and stock markets (Fan, 2020)

**Basis:** accepted manuscript (21 Aug 2019, Swansea repository), read through a page-fetch summary; Table 8 only partly visible. Numbers to check against the EFM version.

**Takeaway:** For 55 FTSE 100 firms, bot tweets (~5% of volume) were linked to volatility and volume like human tweets but more weakly, carried no reliable return information, and positive bot spikes were followed by negative returns the next week; separating bot from human tweets changes what the volume signal means.

## Problem
Do tweets from automated accounts relate to returns, volatility and trading volume differently from human tweets?

## Data and period
~69.8M tweets naming 55 FTSE 100 firms, Aug 2015–Jul 2018; 37,674 firm-days and 1.41M five-minute intervals (pp. 10–11, Table 2).

## Method
Rule-based bot labels (≥5 tweets 0:00–6:00, >10 tweets a day, or the same tweet ≥3 times, on >50% of active days), checked with Botometer (pp. 11–12); fixed-effects panel regressions at daily and 5-minute frequency; event study of abnormal tweet spikes (Sec. 5.3).

## Baselines and validation
In-sample regressions with controls (traditional news, pre-trading hours, lagged tweets); no out-of-sample test (pp. 23–25).

## Results (with page or section references)
- Daily volatility: human message volume 0.264 vs bot 0.094; bot positiveness −0.035 (Table 4).
- Returns: human and bot positiveness both small positive; bot volume not significant (Table 4); intraday bot returns not significant (Table 7).
- Event study: negative tweet spikes −0.38% on the day, recovered over days 1–5; positive bot spikes followed by significant negative returns next week (Sec. 5.3, Table 9).
- The 2018 working-paper version reports the intraday bot effect on returns vanishing within 30 minutes (EconPapers abstract, WP 2018-30).

## Limits and risks to validity
_My assessment:_ in-sample; simple heuristic bot rules; 55 large UK firms; no test of whether removing bots improves a forecast.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample |
| Baselines | 1 | Controls for news and lags |
| Point-in-time and leakage controls | 1 | Pre-trading hours and lags checked |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 55 firms, 3 years |
| Statistical testing | 1 | Panel significance |
| Reproducibility | 0 | No code or data |
| **Total** | **4/12 → 5/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).
