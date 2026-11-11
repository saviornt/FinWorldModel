---
type: lit-note
title: 'Agreement Between Reconstructed and Native GDELT GKG Records: A Field-Level
  Baseline'
authors:
- Nikita A. Klimin
year: 2026
venue: arXiv (cs.CL)
source_url: https://arxiv.org/abs/2610.35358
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.9
- RQ2.2
family:
- data-sources
evidence: Moderate
score: 9
tags:
- lit-note
- family/data-sources
---
# Agreement Between Reconstructed and Native GDELT GKG Records: A Field-Level Baseline (Nikita A. Klimin, 2026)

**Takeaway:** GDELT's GKG software is not public; an open reconstruction matched native English tone only moderately (MAE 1.79 points, CCC 0.75) and entities partly (F1 0.42–0.65), and 11 of 432 sampled 15-minute archives (2.5%) were missing, so GKG fields cannot be regenerated for one's own articles.

## Problem
Whether GDELT GKG records can be reproduced for self-collected news.

## Data and period
193,550 English articles from 8,729 publishers (2020–2025) and 2,500 in five other languages, sampled from 15-minute GKG archives; pages re-fetched in October 2026.

## Method
Open-source reconstruction (gdelt-regkg) compared field by field with native GKG records.

## Baselines and validation
Native GDELT records as reference.

## Results (with page or section references)
- 421 of 432 scheduled archives available; 11 missing (sec. III).
- English tone MAE 1.79, CCC 0.75; persons F1 0.65, organisations 0.42, locations 0.65; dates 0.42; quotations 0.07.
- Translated non-English tone worse (MAE 2.10–2.64).
- Agreement did not improve for more recent records (sec. VIII).

## Limits and risks to validity
Re-fetched pages may differ from what GDELT processed (9 months to 7 years later); single author; measures agreement, not truth.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Measurement study |
| Baselines | 1 | Native records as reference |
| Point-in-time and leakage controls | N/A | – |
| Costs and realism | N/A | – |
| Sample breadth | 2 | Six years, 8,729 publishers, six languages |
| Statistical testing | 0 | Descriptive agreement metrics only |
| Reproducibility | 2 | Code on GitHub/PyPI; native records public |
| **Total** | **9/14** | 5 of 8 on applicable checks, scaled (8.75) |

## Quotes worth keeping (each under 15 words, with page)
- "the software that produces the records is not public" (abstract)
