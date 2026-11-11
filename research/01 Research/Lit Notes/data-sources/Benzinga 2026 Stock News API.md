---
type: lit-note
title: Benzinga Stock News API
authors:
- Benzinga
year: 2026
venue: Vendor product page
source_url: https://www.benzinga.com/apis/en-ca/cloud-product/stock-news-api/
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.2
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# Benzinga Stock News API (Benzinga, 2026)

**Basis:** opened 2026-11-08: product page. Benzinga's API home page ([benzinga.com/apis](https://benzinga.com/apis)) was seen in search results only (claims an 84 TB archive and sub-0.1 s latency; not opened, not used as fact).

**Takeaway:** A licensed, display-rights news feed covering the Wilshire 5000, TSX and 1,000 other tickers (130–160 articles and 600–900 headlines a day), not delayed, with `created`/`updated` timestamps; no public price or archive start date.

## Problem
A licensed US equity newswire for a solo project.

## Data and period
Archive start not stated on the page.

## Method
Delivered by REST pull or TCP push; full story, headline and image may be displayed.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Has both `created` and `updated` fields, so stories edited after release can be detected (timestamps in HH:MM:SS; `updated` also UNIX).
- Pricing on request.

## Limits and risks to validity
Training and storage rights not stated. Alpaca's news API draws on one or more feeds ([[Alpaca 2026 Historical News API]]; its news page does not name Benzinga), so a Benzinga-derived feed may be available more cheaply through a broker: unconfirmed.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Benzinga Stock News API is not delayed." (product page)
