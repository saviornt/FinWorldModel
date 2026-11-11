---
type: lit-note
title: Alpha Vantage premium plans and time-series documentation
authors:
- Alpha Vantage
year: 2026
venue: Vendor documentation
source_url: https://www.alphavantage.co/premium/
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
# Alpha Vantage premium plans and time-series documentation (Alpha Vantage, 2026)

**Basis:** opened 2026-11-08: [Premium](https://www.alphavantage.co/premium/) and [API documentation](https://www.alphavantage.co/documentation/) (time-series sections). The LISTING_STATUS (delisting) section could not be retrieved: the fetch tool truncated before it at both offsets tried.

**Takeaway:** Confirms the guide's seed figures: free key 25 requests/day; premium $49.99–$249.99/month for 75–1,200 requests/min (a second band $499–$2,499 is also listed); intraday back to 2000-01 by month with adjusted/raw choice, but intraday, full daily history and adjusted daily are premium, and real-time or 15-min-delayed US data needs an entitlement.

## Problem
Cost, limits and history of Alpha Vantage stock data.

## Data and period
TIME_SERIES_INTRADAY: "current and 25+ years of historical intraday" bars; `month` parameter accepts any month since 2000-01. TIME_SERIES_DAILY and DAILY_ADJUSTED: "25+ years".

## Method
Intraday: `adjusted` default true (split/dividend), false for raw; `extended_hours` default true; `entitlement` = realtime or delayed; premium endpoint. Daily: raw only; "full" output premium. Daily adjusted: adjusted close plus split/dividend events; premium. Premium page: realtime, 15-min delayed, realtime options or historical index data need a "data entitlement process" for personal use (cost not stated). "No daily limits" on premium.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Seed figures confirmed (Premium page table; free limit sentence).
- Intraday history to 2000 at 1-minute (Documentation, TIME_SERIES_INTRADAY) is long for the price, but delivered one month per call.
- Delisted coverage **not confirmed** (LISTING_STATUS section unread).

## Limits and risks to validity
No statement on data sources (SIP vs exchange), data-quality controls or licence for derived data on the pages read. The second price band (to $2,499) has no tier names; assumed to be higher-volume or business tiers.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Any month in the last 25+ years since 2000-01 (January 2000) is supported." (Documentation)
