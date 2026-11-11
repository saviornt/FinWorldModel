---
type: lit-note
title: 'requests-cache: expiration'
authors:
- requests-cache maintainers
year: 2026
venue: Engineering documentation
source_url: https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.4
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# requests-cache: expiration (requests-cache, 2026)

**Basis:** user guide page opened 2026-11-08.

**Takeaway:** A Python cache that by default stores responses indefinitely, with per-URL expiry rules and `stale_if_error` fallback, so historical (immutable) endpoints can be cached forever while recent data expires.

## Problem
Cache control for API clients whose servers send no useful headers.

## Data and period
Not applicable.

## Method
Default: store indefinitely; `NEVER_EXPIRE`; `urls_expire_after` {pattern: expiry}; Cache-Control headers honoured if enabled; `stale_if_error`.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Per-URL rules match the fetch-once need: closed historical periods never expire; the current day expires quickly.

## Limits and risks to validity
A cache is not a ledger: it does not by itself record request purpose, licence or knowledge time.

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "By default, cached responses will be stored indefinitely." (expiration guide)
