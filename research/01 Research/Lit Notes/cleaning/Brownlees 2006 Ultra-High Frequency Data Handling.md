---
type: lit-note
title: 'Financial Econometric Analysis at Ultra-High Frequency: Data Handling Concerns'
authors:
- Christian T. Brownlees
- Giampiero M. Gallo
year: 2006
venue: Computational Statistics & Data Analysis 51(4), 2232–2245
source_url: https://labdisia.disia.unifi.it/area01/pubblicazioni_DS/wp/2006/wp2006_03.pdf
doi: 10.1016/j.csda.2006.09.030
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.3
family:
- cleaning
evidence: Weak
score: 2
tags:
- lit-note
- family/cleaning
- high-frequency
---
# Financial Econometric Analysis at Ultra-High Frequency: Data Handling Concerns (Brownlees & Gallo, 2006)

**Basis:** working paper 2006/03 (University of Florence), read through a summarising page fetch on 2026-11-08; the journal version was not opened.

**Takeaway:** Removing a tiny share of bad ticks changes models a lot: on one stock-month, an outlier filter (trimmed-mean window of 60 ticks, 3 SD plus a USD 0.02 granularity) removed 0.18% of trades, yet left unfiltered the bad ticks shortened mean durations from about 9.4 to 7 minutes and moved every ACD coefficient; differences between dirty and clean data exceed differences between filter settings.

## Problem
How do TAQ handling choices affect high-frequency econometrics?

## Data and period
General Electric trades, April 2002 (22 days, about 363,000 trades) (pp. 22, 24).

## Method
Drop corrected and delayed trades; keep 9:30–16:05; outlier filter; median price for same-time ticks; price-change durations; ACD(1,1).

## Baselines and validation
Dirty vs cleaned series; filters with k ∈ {40, 60, 80}, γ ∈ {0.02, 0.04, 0.06}.

## Results (with page or section references)
- Filter removed 647 ticks (0.18%); out-of-hours 1,499 (0.41%) (p. 24, Table 6).
- ACD β 0.903 (dirty) vs 0.846 (clean); α 0.091 vs 0.140; lag-1 autocorrelation of durations 0.139 vs 0.240 (Tables 8–9).

## Limits and risks to validity
One stock, one month; the paper's own tables disagree slightly on counts (Table 6 vs text). Centred neighbour windows use future ticks (fine for cleaning history, not for live features).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Method paper |
| Baselines | N/A | |
| Point-in-time and leakage controls | N/A | |
| Costs and realism | N/A | |
| Sample breadth | 0 | One stock-month |
| Statistical testing | 1 | Model estimates compared |
| Reproducibility | 0 | Licensed data, no code |
| **Total** | 1/6 → **2/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
