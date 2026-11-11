---
type: lit-note
title: 'RFC 9111: HTTP Caching'
authors:
- R. Fielding
- M. Nottingham
- J. Reschke
year: 2022
venue: IETF RFC (Standards Track, STD 98)
source_url: https://www.rfc-editor.org/rfc/rfc9111.html
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
# RFC 9111: HTTP Caching (Fielding, Nottingham and Reschke, 2022)

**Basis:** RFC text opened 2026-11-08. Note year is 2022 (publication) though the file name follows the vault convention of first-author/year: the standard is from June 2022.

**Takeaway:** The HTTP caching standard: freshness from `max-age`/`Expires`, revalidation with `ETag`/`If-None-Match` or `Last-Modified`/`If-Modified-Since` returning 304, and `no-store` forbidding storage; a fetch-once client can use conditional requests to avoid re-downloading unchanged data.

## Problem
Standard rules for storing and reusing HTTP responses.

## Data and period
Not applicable.

## Method
s. 4.2 freshness; s. 4.3 validation and 304; s. 5.2.2.5 no-store; s. 5.2.2.7 private.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- A 304 "indicates that the stored response can be updated and reused" (s. 4.3.3).
- Market-data APIs often send no validators; a research cache then has to rely on its own expiry rules (assumption, not from the RFC).

## Limits and risks to validity
Standards text; says nothing about licence limits on caching (those come from vendor terms, RQ2.6).

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "the stored response can be updated and reused" (s. 4.3.3)
