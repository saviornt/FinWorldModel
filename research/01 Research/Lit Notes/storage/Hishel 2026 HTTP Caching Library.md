---
type: lit-note
title: 'Hishel: HTTP caching for Python'
authors:
- Hishel maintainers
year: 2026
venue: Engineering documentation
source_url: https://hishel.com/
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
# Hishel: HTTP caching for Python (Hishel, 2026)

**Basis:** project site opened 2026-11-08 (guide seed).

**Takeaway:** An RFC-compliant, streaming-friendly HTTP cache for HTTPX and Requests with SQLite and Redis storage; whether it can force-cache responses that headers mark uncacheable is not stated on the home page.

## Problem
A drop-in HTTP cache layer for API clients.

## Data and period
Not applicable.

## Method
Pure-Python caching state machine; integrations for HTTPX, Requests, ASGI, FastAPI; SQLite and Redis backends.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Standards-following cache: good for well-behaved APIs; for APIs without cache headers, a forced or ledger-based cache is needed.

## Limits and risks to validity
Version and licence not stated on the page read.

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "An elegant HTTP caching library for Python." (home page)
