---
type: lit-note
title: 'Databento US Equities: catalog, pricing and history'
authors:
- Databento
year: 2026
venue: Vendor documentation
source_url: https://databento.com/catalog/us-equities
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.1
- RQ2.7
- RQ2.6
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# Databento US Equities: catalog, pricing and history (Databento, 2026)

**Basis:** pages opened 2026-11-08: [US equities catalog](https://databento.com/catalog/us-equities), [pricing](https://databento.com/pricing), [product roadmap](https://roadmap.databento.com/b/n0o5prm6/feature-ideas/cfe-book-depth), and the blog post [Introducing Databento US Equities](https://databento.com/blog/introducing-databento-us-equities) (2025-01-13). The corporate-actions documentation page was opened but did not contain the answer.

**Takeaway:** Exchange-direct, nanosecond-timestamped US equities from 45 venues down to full order book (MBO), but tick history starts in 2018 (Nasdaq ITCH from 2018-05-01) and daily backfill to about 2010 was "in progress"; $199/month Standard gives full L0 (OHLCV) history but only 12 months of L1 and 1 month of L2/L3.

## Problem
Coverage, resolution, history and cost of Databento's US equities service.

## Data and period
15 exchanges and 30 ATSs, 20,000+ symbols, 19 datasets in one service (catalog). Catalog header: "Available history 8 years". XNAS.ITCH available from 2018-05-01. Roadmap: tick history (L1 and finer) starts 2018; "backfill of daily/OHLCV/L0 data is in progress, which will bring daily history back to at least 2010"; no plan to backfill ticks.

## Method
Schemas grouped L0 (OHLCV, definitions, statistics), L1 (trades, top of book), L2 (MBP-10), L3 (MBO). Pricing page (general plan table): Usage-based pay-as-you-go priced per GB of uncompressed binary data; Standard $199/month (L0 16+ years, L1 last 12 months, L2/L3 last 1 month; "up to 2 devices", individuals and small teams); Plus $1,750/month and Unlimited $4,500/month, annual contract, aimed at firms. New users get $125 historical credits expiring after 6 months. Historical data for most datasets can be redistributed after 24 hours subject to publisher terms.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Finest resolution of any provider read (MBO, nanosecond timestamps; catalog).
- Shortest tick history of the institutional-grade options (2018; roadmap).
- Prices are raw exchange prices; adjustment factors and corporate actions are separate datasets (listed in docs navigation; their content and price **not confirmed** this session).

## Limits and risks to validity
The "16+ years" L0 figure on the pricing page and the "8 years" catalog header disagree; the pricing table is not equities-specific. Per-GB rates not shown on the pricing page. Delisted-symbol handling not confirmed (docs list a "Listings and delistings" page, not opened).

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "The earliest that our tick history (L1 and better) goes back to is 2018" (roadmap)
