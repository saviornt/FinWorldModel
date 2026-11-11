---
type: lit-note
title: 'X API: pricing and post search'
authors:
- X Corp.
year: 2026
venue: Official documentation
source_url: https://docs.x.com/x-api/getting-started/pricing
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.2
- RQ2.6
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# X API: pricing and post search (X, 2026)

**Basis:** opened 2026-11-08: [pricing](https://docs.x.com/x-api/getting-started/pricing) and [search introduction](https://docs.x.com/x-api/posts/search/introduction). This replaces the guide's seed (PostProxy summary) with X's own pages. Developer agreement (storage, training terms) not opened.

**Takeaway:** X now sells API access pay-per-use with no subscriptions: $0.005 per post read, capped at 3 million post reads a month (above that, Enterprise); full-archive search back to March 2006 is open to pay-per-use customers, up to 500 posts per request.

## Problem
Cost and history of X data for research.

## Data and period
Recent search: last 7 days. Full-archive search: "back to March 2006".

## Method
Credits bought upfront; spending caps available. Reads: $0.005/post, $0.010/user, $0.001/like. Writes $0.015/post. Query length 512 (recent) or 1,024 (full archive) characters; 100 or 500 posts per request.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Cost scales linearly with posts read: 3 million posts (the monthly cap) ≈ $15,000 (arithmetic from the listed rate).
- Historical cashtag studies are possible without Enterprise, within the cap.

## Limits and risks to validity
Storage, deletion-compliance and model-training terms are in the developer agreement, not read here. Timestamp precision not stated on these pages.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "The X API uses pay-per-usage pricing with no subscriptions." (pricing)
