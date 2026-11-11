---
type: lit-note
title: CRSP US Stock Databases (product page)
authors:
- CRSP (Morningstar)
year: 2026
venue: Vendor product page
source_url: https://indexes.morningstar.com/research-data-products/crsp-us-stock-databases
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.1
- RQ2.8
- RQ3.3
- RQ3.8
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# CRSP US Stock Databases (CRSP / Morningstar, 2026)

**Basis:** opened 2026-11-08: [product page](https://indexes.morningstar.com/research-data-products/crsp-us-stock-databases) (crsp.org redirects here). Coverage details for 1925/1926 come from the LUISS library page seen in search (CRSP 1925 US Stock Database) and from [[Liu 2020 Data Quality Problems Finance Databases]]; the product page itself does not state a start date.

**Takeaway:** The academic reference: daily and monthly US stock data with corporate actions and permanent identifiers (PERMNO for securities, PERMCO for companies) for "over 100 years", licensed to academic, government and practitioner licensees; no public price.

## Problem
Reference-quality, survivorship-free US stock history with stable identifiers.

## Data and period
"Over 100 Years" (headline). Daily and monthly market data and corporate actions.

## Method
PERMNO is "a proprietary, permanent identifier" that tracks US-listed equities over time; PERMCO identifies the company.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Permanent identifiers solve ticker reuse and renames (product page), relevant to RQ3.8.
- Access is by institutional licence (WRDS is the usual route but is not named on the page).

## Limits and risks to validity
No price, no intraday. Known CRSP data-quality issues (missing delisting returns, adjustment-factor pitfalls) are in [[Liu 2020 Data Quality Problems Finance Databases]]. A solo, non-academic researcher may not be able to license it.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "a proprietary, permanent identifier used to track US-listed equities over time" (product page)
