---
type: lit-note
title: When Can the Market Identify Old News?
authors:
- Anastassia Fedyk
- James Hodson
year: 2023
venue: Journal of Financial Economics
source_url: https://aeaweb.org/conference/2020/preliminary/paper/riRZrF43
doi: 10.1016/j.jfineco.2023.04.008
accessed: 2026-11-08
papers:
- '[[RP1 ML Methods]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ1.11
- RQ3.2
family:
- novelty-detection
evidence: Moderate
score: 6
tags:
- lit-note
- family/novelty-detection
- corroboration
---
# When Can the Market Identify Old News? (Fedyk, 2023)

**Basis:** August 2019 working-paper version (AEA 2020 conference PDF), read through a page-fetch summary; Table 8 coefficients not returned. DOI from OpenAlex. Check numbers against the JFE version before RP1 is final.

**Takeaway:** The market discounts straight reprints of one earlier story but over-reacts to recombinations that stitch together old facts from several earlier stories; those reactions are larger and then reverse, and the effect grew over 2001–2014.

## Problem
Which kinds of old news does the market fail to recognise as old?

## Data and period
~17 million Bloomberg terminal articles, Jan 2000–Dec 2014, US equities above $5, ≥70% relevance (pp. 2, 12–13). Each article compared to the five closest articles on the same firm in the prior 72 hours (pp. 13–14).

## Method
Novel: <60% of terms covered by prior articles. Old articles split into reprints (≥80% of stale content from the single closest prior article) and recombinations (stale content spread across several sources) (pp. 15–16, eqs. 4–5). Survey experiment with 36 finance professionals. Panel regressions of next-day absolute abnormal returns, volume, and following-week reversals.

## Baselines and validation
In-sample panel regressions with controls; 12 alternative constructions (p. 26); year-by-year estimates; no holdout or trading test.

## Results (with page or section references)
- Professionals rated novelty: novel 4.52, recombinations 3.03, reprints 2.61 of 7; recombination − reprint 0.42 (t = 2.05); 72% rated recombinations more novel (p. 10).
- Next-day absolute abnormal return ≈13 bp larger per 10% shift from reprints to recombinations (p. 20); overall old news ≈8 bp smaller per 10% more old content (p. 19).
- Reactions to old news reverse more in the following week; recombination-driven reversals larger still (p. 22).
- Old-news reaction declined 2001–2014 while the recombination effect rose (significant in 11 of 14 years; ≈18 bp in 2014) (p. 23).

## Limits and risks to validity
_My assessment:_ in-sample; Bloomberg-specific; lexical overlap measure; no costs. Key implication: deduplication that only removes near-copies leaves the most misleading repetition (recombination) in place.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample |
| Baselines | 1 | Controls, novel-news comparison |
| Point-in-time and leakage controls | 1 | Only prior 72 h used; terminal timestamps |
| Costs and realism | N/A | Not a trading claim |
| Sample breadth | 2 | All US equities, 15 years incl. 2008 |
| Statistical testing | 1 | Significance, many robustness variants |
| Reproducibility | 0 | Licensed data |
| **Total** | **5/12 → ≈6/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (summary-only read).
