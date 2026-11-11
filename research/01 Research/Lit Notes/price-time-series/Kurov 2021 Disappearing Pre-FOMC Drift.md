---
type: lit-note
title: "The Disappearing Pre-FOMC Announcement Drift"
authors: [Alexander Kurov, Marketa Halova Wolfe, Thomas Gilbert]
year: 2021
venue: Finance Research Letters
source_url: https://www.skidmore.edu/economics/documents/KurovWolfeGilbert-TheDisappearingPre-FOMC-Announce-Drift-200914.pdf
doi: 10.1016/j.frl.2020.101781
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Moderate
score: 8
tags: [lit-note, family/price-time-series, information-diffusion, negative-result]
---
# The Disappearing Pre-FOMC Announcement Drift (Kurov, 2021)

**Basis:** accepted version (14 Sep 2020), read through a page-fetch summary; t-statistics computed by the summariser from reported standard errors.

**Takeaway:** Out of the original sample, the pre-FOMC drift ([[Lucca 2015 Pre-FOMC Announcement Drift]]) survived only for meetings with press conferences until 2015 (≈44.5 bp) and then shrank to ≈9 bp (insignificant) in 2016–2019; it was absent for meetings without press conferences; lower uncertainty (VIX) explains the decline.

## Problem
Did the pre-FOMC drift persist after its publication?

## Data and period
S&P 500 returns before scheduled FOMC announcements, Sept 1994–Dec 2019; post-sample Apr 2011–Dec 2019 (pp. 1, 3).

## Method
Mean pre-FOMC returns by period and press-conference status; regressions with VIX and TYVIX (Tables 2–3).

## Baselines and validation
Original sample replication; out-of-sample extension.

## Results (with page or section references)
- 1994–2011: ≈49.2 bp (t ≈ 4.6) (Table 1).
- With press conferences: ≈44.5 bp (t ≈ 3.3) 2011–15; ≈9.2 bp (t ≈ 1.3) 2016–19; without: ≈ −5.1 bp (Table 2).
- Post-liftoff dummy insignificant once VIX/TYVIX added (Table 3); authors reject a pure publication effect because the drift first persisted (p. 7).

## Limits and risks to validity
_My assessment:_ small post-sample; one index. Key negative result: a documented "priced-in-early" pattern can vanish within a few years.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Post-publication extension |
| Baselines | 1 | Original sample, uncertainty controls |
| Point-in-time and leakage controls | 2 | Intraday announcement timing |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | One index, 25 years |
| Statistical testing | 1 | Basic tests |
| Reproducibility | 1 | Public data |
| **Total** | **7/12 → 8/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "We discuss a possible explanation for this change: reduced uncertainty." (p. 1)
