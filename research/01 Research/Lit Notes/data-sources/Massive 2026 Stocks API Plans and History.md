---
type: lit-note
title: 'Massive (formerly Polygon.io) Stocks API: plans, tickers and aggregates'
authors:
- Massive
year: 2026
venue: Vendor documentation
source_url: https://massive.com/docs/rest/stocks/aggregates/custom-bars
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
# Massive (formerly Polygon.io) Stocks API: plans, tickers and aggregates (Massive, 2026)

**Basis:** pages opened 2026-11-08: [Custom bars](https://massive.com/docs/rest/stocks/aggregates/custom-bars), [All tickers](https://massive.com/docs/rest/stocks/tickers/all-tickers), [pricing](https://massive.com/pricing) (partly rendered), and Massive's own [Massive vs Databento](https://massive.com/compare/massive-vs-databento.md) page (vendor comparison, used only for Massive's own claims).

**Takeaway:** Records from 2003-09-10, delisted tickers queryable with `active=false` and a `delisted_utc` field, split-adjusted bars by default (dividends not mentioned); history and latency scale with plan: free 2 years EOD, $29 5 years 15-min delayed, $79 10 years, $199 all history real-time; stock plans are "Individual use only".

## Problem
History, delisting coverage, adjustment and cost of Massive's US stocks API.

## Data and period
"Records date back to September 10, 2003" (All tickers; Custom bars).

## Method
Plan table on the Custom bars page: Basic free, 2 years, end-of-day; Starter $29/month, 5 years, 15-minute delayed; Developer $79/month, 10 years, 15-minute delayed; Advanced $199/month, all history, real-time. Pricing page: Stocks Advanced described as "20+ years of history", individual use only; business pricing separate; 20% off annually.

Tickers endpoint: `active` defaults to true; false returns delisted assets; `delisted_utc` = last trading date; `date` parameter returns tickers available on a past date (point-in-time universe).

Aggregates: `adjusted` "Whether or not the results are adjusted for splits", default true; max 50,000 base aggregates per query.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Point-in-time ticker universe with delisting dates (All tickers).
- Only split adjustment documented for bars; total-return series would need the dividends endpoint (not opened).
- Massive's comparison page claims trades and quotes back to 2003 and trades from 2010 in Stocks Advanced: vendor claim, unverified.

## Limits and risks to validity
Pricing page rendered only partly. Flat-file (bulk) access and per-plan call limits not confirmed. A third-party skill page reports that some vendors, Polygon among them, can map delisted tickers to successor entities ([survivorship-bias skill page](https://skills.cat/skills/jefrnc/quant-llm-skills/survivorship-bias), unsourced, not counted as evidence).

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "False means the asset has been delisted." (All tickers)
