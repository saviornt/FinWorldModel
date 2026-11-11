---
type: lit-note
title: Making retries safe with idempotent APIs
authors:
- Malcolm Featonby
year: 2026
venue: Engineering documentation
source_url: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/
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
# Making retries safe with idempotent APIs (Featonby, AWS Builders' Library)

**Basis:** article opened 2026-11-08 (no publication date shown; page metadata updated 2026-11-05).

**Takeaway:** Make every request carry a caller-chosen unique token, record the token with its parameters atomically with the work, return the same result for a repeat, and reject a repeat token with different parameters; this is the server-side analogue of a client request ledger.

## Problem
Retries without duplicate side effects.

## Data and period
Not applicable.

## Method
Client request identifier (EC2 "ClientToken"); server records it keyed by customer and token; atomic record-and-act; same semantic response for a repeat within a retention interval; parameter mismatch returns a validation error.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- A request ledger keyed by a deterministic request identity (endpoint + parameters) gives the same guarantees on the client side: a repeated fetch returns the stored response instead of a new call (inference for this project, not a claim of the article).

## Limits and risks to validity
Written for AWS service design; the client-ledger transfer is the project's reading.

## Rubric scores
Primary documentation (engineering documentation and standards): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "an operation can be retried without any side effects" (article)
