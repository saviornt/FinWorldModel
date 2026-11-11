---
type: lit-note
title: Norgate Data US stock packages and data content
authors:
- Norgate Data
year: 2026
venue: Vendor documentation
source_url: https://norgatedata.com/stockmarketpackages.php
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
# Norgate Data US stock packages and data content (Norgate Data, 2026)

**Basis:** opened 2026-11-08: [stock market packages](https://norgatedata.com/stockmarketpackages.php) and [data content tables](https://norgatedata.com/data-content-tables.php) (first 100,000 characters). The pricing page failed to load.

**Takeaway:** The cheapest survivorship-bias-free daily US source read: Platinum ($630/year) has listed and delisted stocks back to 1990 with historical index constituents; Diamond ($787.50/year) goes back to 1950 with 25,222 delisted securities to Sep 2022; end-of-day only, delivered through a Windows updater.

## Problem
Survivorship-free daily US stock history and its cost.

## Data and period
Packages: Silver last 10 years ($270/year), Gold last 20 years ($360/year), Platinum back to 1990 incl. delisted and historical index constituents ($630/year; $346.50 per 6 months), Diamond back to 1950 ($787.50/year; $433.13 per 6 months). Delisted database: "25222 delisted securities" from the start of 1950 to Sep 2022, with "no claim" of completeness, especially for the 1950s and early 1960s; OTC-only delistings excluded; delisted symbols carry a date suffix (e.g. ALOG-201806).

## Method
Close is the listing exchange's closing-auction price (or last price); open is first price on any venue (data content tables).

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Point-in-time index membership and delistings in one package (packages table).
- Daily resolution only (no intraday product found on the pages read).

## Limits and risks to validity
Adjustment-method sections not in the part of the page read. Delisted figure is to Sep 2022 (page may be stale). Delivery needs Norgate's updater; no REST API, which matters for a fetch-once pipeline.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "no claim that the database for Delisted is complete" (data content tables)
