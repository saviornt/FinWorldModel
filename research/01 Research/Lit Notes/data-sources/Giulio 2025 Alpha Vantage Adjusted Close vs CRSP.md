---
type: lit-note
title: Download historical data using Alpha Vantage (comparison with CRSP)
authors:
- Giulio (surname not stated; Sant'Anna School of Advanced Studies)
year: 2025
venue: Personal academic web page
source_url: https://www.cafed.santannapisa.it/~giulio/other/alpha_vantage/index.html
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.7
- RQ3.3
family:
- data-sources
evidence: Weak
score: 4
tags:
- lit-note
- family/data-sources
---
# Download historical data using Alpha Vantage (comparison with CRSP) (Giulio (surname not stated; Sant'Anna School of Advanced Studies), 2025)

**Takeaway:** A Sant'Anna School researcher's check of Alpha Vantage against CRSP for Microsoft found raw closes matched CRSP but the adjusted-close column behaved inconsistently (sometimes adjusted, sometimes not), and advises building adjustment factors from the split coefficient instead.

## Problem
Whether Alpha Vantage adjusted prices can be trusted.

## Data and period
Microsoft (MSFT) daily prices around its split; Alpha Vantage snapshots from Oct 2019, Jan 2020 and Jan 2021; page created 2025-11-19.

## Method
Plot of Alpha Vantage close and adjusted close against CRSP close and adjusted close; download script shown.

## Baselines and validation
CRSP used as reference.

## Results (with page or section references)
- Raw close matches CRSP.
- Adjusted close stays below CRSP's adjusted series after the split.
- Other stocks: Alpha Vantage price columns sometimes matched CRSP adjusted values.
- Advice: do not use the adjusted-close column; build factors from the split coefficient.

## Limits and risks to validity
One stock, informal, snapshots from 2019-2021 (may be fixed since); author's surname not shown on the page. Consistent with forum reports (e.g. a 2020 Stack Overflow report of a random adjusted close of 766,464) not opened as sources.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Data check, not a forecast |
| Baselines | 1 | CRSP reference |
| Point-in-time and leakage controls | N/A | – |
| Costs and realism | N/A | – |
| Sample breadth | 0 | One stock |
| Statistical testing | 0 | None |
| Reproducibility | 1 | Script shown; data not shared |
| **Total** | **4/14** | 2 of 8 on applicable checks, scaled (3.5) |

## Quotes worth keeping (each under 15 words, with page)
- "seems to return un-adjusted quantities, sometimes the adjusted ones"
