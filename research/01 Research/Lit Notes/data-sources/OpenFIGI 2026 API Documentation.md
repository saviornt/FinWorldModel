---
type: lit-note
title: OpenFIGI API documentation
authors:
- OpenFIGI (Bloomberg)
year: 2026
venue: Official documentation
source_url: https://www.openfigi.com/api/documentation
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.8
- RQ3.8
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# OpenFIGI API documentation (OpenFIGI (Bloomberg), 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** OpenFIGI maps tickers, ISINs and CUSIPs to FIGIs (exchange, composite and share-class levels) through a free API (25 mapping requests a minute without a key, 250 with one); delisted equities are included only on request.

## Problem
A free security identifier and mapping service.

## Data and period
Not applicable.

## Method
API documentation: /v3/mapping, /v3/search, /v3/filter; rate limits per key or IP.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Free and public; key raises limits (mapping 25 → 250 requests/min; search 5 → 20).
- Composite FIGI links venue-level FIGIs in one country; share-class FIGI spans countries.
- Only listed equities returned unless `includeUnlistedEquities` is true (adds unlisted and delisted).
- History depth not stated.

## Limits and risks to validity
Terms of Service not opened; FIGI maps current identifiers, not a dated history of ticker changes (project reading). Results capped at 15,000.

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "free and open to the public"
