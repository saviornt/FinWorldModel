---
type: lit-note
title: 'Run EDGAR Run: SEC Dissemination in a High-Frequency World'
authors:
- Jonathan L. Rogers
- Douglas J. Skinner
- Sarah L. C. Zechman
year: 2017
venue: Journal of Accounting Research 55(2), 459–505
source_url: https://www.colorado.edu/business/faculty-research/2018/06/17/run-edgar-run-sec-dissemination-high-frequency-world
doi: 10.1111/1475-679X.12167
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.2
- RQ3.2
- RQ1.12
family:
- data-sources
evidence: Weak
score: 5
tags:
- lit-note
- family/data-sources
---
# Run EDGAR Run: SEC Dissemination in a High-Frequency World (Rogers, 2017)

**Basis:** journal full text is closed; read the University of Colorado research summary (opened 2026-11-08) and the journal abstract on [EconPapers](https://econpapers.repec.org/RePEc:bla:joares:v:55:y:2017:i:2:p:459-505) and an Alpha Architect summary (search-result text). Summary-only, so capped at Weak as in RP1 practice.

**Takeaway:** In 2012–13 just over half of Form 4 filings reached paying PDS subscribers before the EDGAR website (average lead about 18 s per the Colorado summary), and prices, volume and spreads moved about 30 s before public posting; the SEC then agreed to remove the advantage.

## Problem
Is "public" EDGAR dissemination simultaneous for all investors?

## Data and period
Form 4 insider filings, 2012–2013.

## Method
Compare PDS feed arrival times with EDGAR website posting times; event study of returns, volume and spreads in "EDGAR time".

## Baselines and validation
Event-study comparison of filings arriving before vs after website posting (abstract; Fig. 3 per summary).

## Results (with page or section references)
- "Just over half the filing were received in advance of the public posting, with an average 18 second advantage" (Colorado summary).
- Alpha Architect's summary reports 57% early, mean 30 s (PDS) vs 40 s (website) after acceptance (Table 4); the two summaries' figures differ and were not checked against the paper.
- Market response begins around 30 s before public posting (abstract).
- SEC Chair announced on 2014-12-19 that filings would reach the website before PDS subscribers.

## Limits and risks to validity
One filing type, two years, pre-2015 process. Not read in full.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Event study |
| Baselines | N/A | |
| Point-in-time and leakage controls | 2 | The paper is about timestamps |
| Costs and realism | N/A | |
| Sample breadth | 1 | Form 4 only, 2012–13 |
| Statistical testing | 1 | Event-study tests (per abstract) |
| Reproducibility | 0 | |
| **Total** | 4/8 → 7/14, **capped Weak (5)** | Summary-only read |

## Quotes worth keeping (each under 15 words, with page)
- "the meaning of publicly available information in capital markets is no longer simple" (abstract)
