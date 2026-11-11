---
type: lit-note
title: "CRSP December 2017 Annual Release Notes (data edits)"
authors: [Center for Research in Security Prices]
year: 2017
venue: CRSP release notes
source_url: https://crsp.org/crsp_pdf/december-2017-annual-release-notes-0
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.8, RQ3.1]
family: [data-sources]
evidence: Primary documentation
tags: [lit-note, family/data-sources, entity-identity, bitemporal]
---
# CRSP December 2017 Annual Release Notes

**Basis:** release-notes PDF read through a summarising page fetch on 2026-11-08 (plus search-result excerpt).

**Takeaway:** Each CRSP release rewrites history: values are changed "for entire history" (e.g. PERMNO 17039 shares outstanding), trading start dates shift, records move between PERMNOs (89613's data after 2007-08-15 moved to 16852), and some 2010 reorganisations were re-coded with new PERMNOs/PERMCOs instead of name and CUSIP changes; the notes list old and new values but do not say earlier versions stay available, so a CRSP extract is a valid-time view as known at the release date, not a bitemporal record.

## Problem
What changes between CRSP releases?

## Data and period
Release edits up to December 2017.

## Method
Vendor change log.

## Baselines and validation
N/A.

## Results (with page or section references)
- Share-code, SIC and header-CUSIP changes applied to entire histories (search excerpt).
- 15 securities given new PERMNOs/PERMCOs from 2010-06-01 (fetch summary).
- Data transferred between PERMNOs after a delisting correction (fetch summary).

## Limits and risks to validity
One release; read via summary; whether CRSP keeps prior vintages for users is not stated.

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
