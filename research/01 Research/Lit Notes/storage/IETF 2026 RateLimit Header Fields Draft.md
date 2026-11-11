---
type: lit-note
title: RateLimit header fields for HTTP (Internet-Draft -11)
authors:
- IETF httpapi working group
year: 2026
venue: IETF Internet-Draft
source_url: https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
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
# RateLimit header fields for HTTP (IETF draft -11, 2026)

**Basis:** Datatracker page opened 2026-11-08 (draft -11, updated 2026-05-23, expires 2026-11-24).

**Takeaway:** A not-yet-standard way for servers to advertise quota (`RateLimit`: remaining `r`, window `t`; `RateLimit-Policy`: quota `q`, window `w`); `Retry-After` takes precedence, and a positive quota does not guarantee service, so clients still need their own limiter and back-off.

## Problem
How clients learn and respect rate limits.

## Data and period
Not applicable.

## Method
Header semantics; relation to Retry-After and 429.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- "Retry-After field MUST take precedence" when both are present.
- Draft status: Internet-Draft, not an RFC; early review of -10 "Not ready".

## Limits and risks to validity
Few market-data vendors are documented as sending these headers (not checked); a client-side token bucket set to the vendor's published limits is the safer default (project inference).

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Clients MUST NOT assume that a positive available quota is a guarantee" (draft)
