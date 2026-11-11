---
type: lit-note
title: "Documentation Link Table: crsp_20181231.csv (CRSP PERMCO – RSSD ID link)"
authors: [Federal Reserve Bank of New York]
year: 2018
venue: FRBNY banking research data documentation
source_url: https://www.newyorkfed.org/medialibrary/media/research/banking_research/data/documentation_20181219.pdf?la=en
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.8]
family: [data-sources]
evidence: Primary documentation
tags: [lit-note, family/data-sources, entity-identity]
---
# NY Fed CRSP–RSSD Link Table Documentation (2018)

**Basis:** PDF read through a summarising page fetch on 2026-11-08 (plus search excerpt).

**Takeaway:** A worked example of a dated cross-database identity map (bank regulatory IDs to CRSP PERMCOs, 1986–2018): tickers are "reassigned and not unique", PERMNO identifies a security and PERMCO the company, PERMCO usually survives mergers but changes in some reorganisations (bank → holding company, acquisition by a private firm), so each link carries a date range and was matched partly by hand.

## Problem / Data / Method
Linking Federal Reserve RSSD IDs to CRSP PERMCOs, with start and end dates; manual matching via CRSP lookup and STOCKNAMES.

## Baselines and validation
N/A.

## Results (with page or section references)
- Tickers reassigned; first six CUSIP digits identify the issuer.
- PERMCO persists through most M&A; listed exceptions change IDs and date ranges.
- STOCKNAMES gives start/end dates of PERMCO–name links.

## Limits and risks to validity
Bank-specific; summary read.

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- "reassigned and not unique" (on tickers)
