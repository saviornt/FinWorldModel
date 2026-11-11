---
type: lit-note
title: Comparison of Common Crawl News & GDELT
authors:
- Ameir El Ouadi
- David Beskow
year: 2026
venue: arXiv (cs.IR)
source_url: https://arxiv.org/abs/2610.00587
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.9
- RQ2.2
family:
- data-sources
evidence: Weak
score: 4
tags:
- lit-note
- family/data-sources
---
# Comparison of Common Crawl News & GDELT (Ameir El Ouadi et al., 2026)

**Takeaway:** Over January–June 2023, GDELT (96.4M articles, 63,325 domains) and Common Crawl News (103.9M articles, 27,032 domains) shared only 4,626 domains (5.4%), so the two 'global news' sources see largely different parts of the world's media.

## Problem
How GDELT's news coverage compares with Common Crawl News.

## Data and period
GDELT and CC-News, 2023-01-01 to 2023-06-30.

## Method
Counts of articles, domains, shared URLs and domains, languages.

## Baselines and validation
Each dataset as the other's comparison.

## Results (with page or section references)
- 96.4M GDELT vs 103.9M CC-News articles; 63,325 vs 27,032 domains; 4,626 shared (sec. III).
- Only 7.31% of GDELT domains indexed in CC-News; 17.11% the other way.
- 46% of GDELT from domains with 10 or fewer articles; GDELT stores metadata, not text (URLs must be re-fetched).
- 36% of GDELT articles in English.

## Limits and risks to validity
Six months only; descriptive; no measure of event accuracy or timeliness; no code or data release.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Descriptive |
| Baselines | 1 | Two datasets compared |
| Point-in-time and leakage controls | N/A | – |
| Costs and realism | N/A | – |
| Sample breadth | 1 | Six months |
| Statistical testing | 0 | None |
| Reproducibility | 0 | None released |
| **Total** | **4/14** | 2 of 8 on applicable checks, scaled (3.5) |

## Quotes worth keeping (each under 15 words, with page)
- "only 5.4% of news sources are shared" (sec. III)
