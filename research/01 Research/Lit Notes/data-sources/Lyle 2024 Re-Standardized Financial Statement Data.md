---
type: lit-note
title: Re-Standardized Financial Statement Data
authors:
- Matthew Lyle
- Federico Siano
- Teri Lombardi Yohn
year: 2024
venue: Working paper (Yale SOM hosted PDF)
source_url: https://som.yale.edu/sites/default/files/2024-07/Re-Standardized%20Financial%20Statement%20Data.pdf
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.3
- RQ3.1
family:
- data-sources
evidence: Moderate
score: 7
tags:
- lit-note
- family/data-sources
---
# Re-Standardized Financial Statement Data (Lyle, 2024)

**Basis:** working paper PDF (July 2024) opened 2026-11-08; Tables 1–11 summarised via the page-fetch tool.

**Takeaway:** Compustat silently re-standardises past figures in its common files: in Snapshot point-in-time data (1986–2023), the sign of earnings changes flips in about 9–10% of firm-quarters across updates (Table 8: 9.34% net income, 10.42% income before extraordinary items; 14.27% is for sales; checked 2026-11-08) and earnings-surprise hedge returns differ by about 25–31 points across collection dates, so fundamentals must come from point-in-time snapshots.

## Problem
How much do "historical" fundamentals change after the fact?

## Data and period
Compustat Snapshot quarterly and annual, 1986–2023; ~8.5 million quarterly datapoints, ~39,783 firms (Table 1).

## Method
Measure change frequency and size across update dates (Tables 2–8); re-run ERC regressions, earnings-surprise and accrual hedge portfolios on fixed samples at different collection dates (Tables 9–11).

## Baselines and validation
Fixed-sample comparison across vintages; no held-out validation.

## Results (with page or section references)
- Mean absolute change for numeric updates ~65% (Table 2).
- Earnings sign flips 9.3–14.3% across measures; accruals ~8% (p. 3, Table 8).
- 1995 ERC ranges 8.19–9.75 across collection dates (Table 9).
- Earnings hedge returns differ by ~25–31 pp; accrual spread up to ~30% (Tables 10–11).
- Snapshot "unrestated" values are first entries and may be preliminary (pp. 11–12).

## Limits and risks to validity
Working paper; inconsistent figures across sections (flagged by the paper's own text); in-sample; no multiple-testing correction. Compustat Snapshot is an institutional product.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample, fixed samples |
| Baselines | N/A | Measurement study |
| Point-in-time and leakage controls | 2 | The subject |
| Costs and realism | N/A | Not a trading claim |
| Sample breadth | 2 | ~40k firms, 1986–2023 |
| Statistical testing | 1 | Significance, no correction |
| Reproducibility | 0 | Licensed data, no code |
| **Total** | 5/10 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- None needed.
