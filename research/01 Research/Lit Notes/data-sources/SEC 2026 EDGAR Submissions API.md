---
type: lit-note
title: "EDGAR Application Programming Interfaces (submissions API)"
authors: [U.S. Securities and Exchange Commission]
year: 2026
venue: SEC.gov documentation
source_url: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.8]
family: [data-sources]
evidence: Primary documentation
tags: [lit-note, family/data-sources, entity-identity, edgar]
---
# EDGAR Submissions API (SEC, 2026)

**Basis:** SEC API page read via page fetch on 2026-11-08.

**Takeaway:** The free submissions endpoint (data.sec.gov/submissions/CIK##########.json) returns, per 10-digit CIK, the current name, former names, and current exchanges and tickers; the page does not state that CIKs are permanent or that former names carry dates, so EDGAR gives a filer-level identity key but not a full dated security history.

## Problem / Data / Method
SEC documentation of EDGAR JSON APIs.

## Results (with page or section references)
- Submissions metadata: current name, former name, exchanges and tickers.
- CIK is a 10-digit number with leading zeros.

## Limits and risks to validity
Field-level JSON schema not shown on the page; dates on former names unconfirmed. See also [[SEC 2026 Accessing EDGAR Data]].

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
