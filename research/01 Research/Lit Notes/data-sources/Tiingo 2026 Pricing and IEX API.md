---
type: lit-note
title: Tiingo pricing and IEX intraday API
authors:
- Tiingo
year: 2026
venue: Vendor documentation
source_url: https://www.tiingo.com/about/pricing
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.1
- RQ2.7
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# Tiingo pricing and IEX intraday API (Tiingo, 2026)

**Basis:** opened 2026-11-08: [pricing](https://www.tiingo.com/about/pricing) and [IEX API documentation](https://www.tiingo.com/documentation/iex).

**Takeaway:** Cheap long daily history ("30+ Years", Power $30/month, 10,000 requests/hour, 40 GB/month) but intraday comes from IEX only (IEX volume only), and the licence is personal internal use; commercial internal use is $50/month.

## Problem
Cost, limits, history and licence of Tiingo prices.

## Data and period
Price history "30+ Years"; 110,471 securities listed. Intraday: IEX feed; volume field is "The number of shares traded on IEX only." Intraday history start not stated.

## Method
Starter free: 500 unique symbols/month, 50 requests/hour, 1,000/day, 1 GB/month. Power $30/month or $300/year: 110,471 symbols, 10,000/hour, 100,000/day, 40 GB/month. Commercial internal use $50/month or $499/year. Licence: "Internal Use Only"; may not display or share data with another person or organisation.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Good value for daily bars; intraday is a single-venue (IEX) view, not the consolidated tape (IEX documentation).
- Delisted coverage and adjustment method not stated on the pages read.

## Limits and risks to validity
EOD documentation (adjustment fields) not opened. Single-venue intraday volume understates market volume; any intraday feature built from it would differ from SIP-based data.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "The number of shares traded on IEX only." (IEX documentation)
