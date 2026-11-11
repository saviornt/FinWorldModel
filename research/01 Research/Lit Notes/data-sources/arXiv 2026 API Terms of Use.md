---
type: lit-note
title: arXiv API Terms of Use
authors:
- arXiv
year: 2026
venue: Official documentation
source_url: https://info.arxiv.org/help/api/tou.html
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
# arXiv API Terms of Use (arXiv, 2026)

**Basis:** opened 2026-11-08.

**Takeaway:** Metadata is CC0 and free at one request every three seconds, but full texts keep their authors' licences: serving or redistributing e-prints needs the copyright holder's permission unless the paper's own licence allows it.

## Problem
Can arXiv metadata and papers be harvested and stored?

## Data and period
All arXiv metadata; bulk downloads and OAI-PMH listed.

## Method
"make no more than one request every three seconds", one connection, across all your machines. Metadata under CC0 1.0.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Metadata (titles, abstracts, dates) is free to store and use.
- Full text: per-paper licence; only "a very small subset" permit redistribution.

## Limits and risks to validity
The page does not address training models on full text; it covers serving and redistribution.

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "make no more than one request every three seconds" (Terms of Use)
