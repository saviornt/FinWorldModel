---
type: lit-note
title: 'Alpaca Market Data API: About and Historical Stock Bars'
authors:
- Alpaca
year: 2026
venue: Vendor documentation
source_url: https://docs.alpaca.markets/docs/about-market-data-api
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.1
- RQ2.7
- RQ3.3
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# Alpaca Market Data API: About and Historical Stock Bars (Alpaca, 2026)

**Basis:** two official pages opened 2026-11-08: [About Market Data API](https://docs.alpaca.markets/docs/about-market-data-api) and the [Historical bars reference](https://docs.alpaca.markets/reference/stockbars).

**Takeaway:** Consolidated SIP US equities from 2016 only, 1-minute minimum bars, raw prices by default with split/dividend/spin-off adjustment on request and symbol mapping through name changes; free tier is IEX real-time and blocks the latest 15 minutes of SIP history; $99/month removes limits.

## Problem
What history, resolution, adjustments and limits the Alpaca stock data API gives.

## Data and period
Equities fed by CTA and UTP (the page says together "100% of market volume"); options via OPRA. Equity history "since 2016" on both plans. Options and crypto start dates not stated.

## Method
Plans: Basic (free): real-time IEX only, 30 WebSocket symbols, historical SIP data restricted to before the latest 15 minutes, 200 historical calls/min. Algo Trader Plus ($99/month): all US exchanges, unlimited WebSocket symbols, no restriction, 10,000 calls/min. Broker API tiers $500–$2,000/month for higher limits.

Bars endpoint: timeframes from `1Min` to `12Month` (no second or tick bars from this endpoint); `adjustment` = raw (default), split, dividend, spin-off or all; `feed` = sip (default), iex, boats (overnight), otc; `asof` maps a symbol to its underlying entity so renames are followed (example: META also returns FB history); `limit` up to 10,000 data points per page, paginated.

## Baselines and validation
Not applicable (documentation).

## Results (with page or section references)
- History depth is short for a long-horizon study: 2016 onwards (About page, plan table).
- Corporate actions handled at query time through `adjustment` (Bars reference, "adjustment").
- Name-change mapping through `asof` (Bars reference). Delisted-symbol coverage is **not stated** on either page.

## Limits and risks to validity
Vendor statement only. No word on delisted names, survivorship, or data-quality incidents. Trade and quote endpoints (tick resolution) not opened in this session.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Our data sources are directly fed by the CTA" (About page)
