---
type: lit-note
title: ALFRED and the FRED API real-time period
authors:
- Federal Reserve Bank of St. Louis
year: 2026
venue: Official documentation
source_url: https://alfred.stlouisfed.org/
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.3
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# ALFRED and the FRED API real-time period (Federal Reserve Bank of St. Louis, 2026)

**Basis:** opened 2026-11-08: [ALFRED home](https://alfred.stlouisfed.org/) and [FRED API real-time periods](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html). Use terms are in [[FRED 2026 Legal Terms of Use]].

**Takeaway:** ALFRED stores every release (vintage) of over 350,000 series, and the FRED API returns data "as known" on any past date by setting `realtime_start` and `realtime_end`; the default is today's values, so a naive pull is a look-ahead leak.

## Problem
Point-in-time macro data.

## Data and period
"Over 350,000 real-time economic time series"; tagline "Economic data time travel since 2006" (service start, not the vintage start).

## Method
Every source, release, series and observation has a real-time period (closed interval). Default real-time period is today ("FRED mode"); set both bounds to a past date to get what was known then.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Point-in-time reads are a parameter, not a separate product (real-time periods page).
- Vintage coverage per series and per-request limits are not stated on these pages.

## Limits and risks to validity
Terms of use restrict storage and AI training ([[FRED 2026 Legal Terms of Use]]), which may rule ALFRED out as a stored training source even though it is the best-designed vintage interface.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "observation data values can be revised" (real-time periods page)
