---
type: lit-note
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
family:
- evaluation
tags:
- lit-note
- family/evaluation
- multiple-testing
title: … and the Cross-Section of Expected Returns
authors:
- Campbell R. Harvey
- Yan Liu
- Heqing Zhu
year: 2016
venue: Review of Financial Studies 29(1), 5–68; NBER WP 20592 (2014)
source_url: http://www.nber.org/papers/w20592.pdf
doi: 10.1093/rfs/hhv059
research_questions:
- RQ4.2
evidence: Strong
score: 12
---
# … and the Cross-Section of Expected Returns (Harvey, Liu & Zhu, 2016)

**Basis:** NBER Working Paper 20592 (2014) PDF, read 2026-11-08 through a summarising page fetch covering the first 100,000 of 112,458 characters (main text; part of the appendix not covered). RFS version not opened.

**Takeaway:** After 316 published factors, a new return predictor needs a t-statistic above about 3.0 (FDR or FWER control, adjusted for correlation and unreported tests) rather than 2.0; most claimed findings in financial economics are likely false.

## Problem
Which significance hurdle accounts for decades of data mining over the cross-section of returns (p. 1–2).

## Data and period
316 factors from 313 published works and 63 working papers, 1967–2012, projected to 2032 (pp. 3–4).

## Method
Bonferroni and Holm (familywise error rate) and BHY (false discovery rate under arbitrary dependence) applied to reported t-statistics over time; scenario for unreported ("hidden") tests; structural model for correlation among tests (§4–§5).

## Baselines and validation
Single-test cut-off of 1.96 as the reference (§4).

## Results (with page or section references)
- Bonferroni hurdle rises from 1.96 to 3.78 by 2012; BHY at 1% FDR stabilises at 3.39 after 2010; at 5% FDR the minimum is about 2.8 (§4.6, pp. 20–22).
- If about 71% of tried factors are unreported, hurdles rise to 4.01 (Bonferroni), 3.96 (Holm), 3.68 (BHY 1%) and 3.18 (BHY 5%) (§4.7.2, p. 25).
- With correlation modelled, about 3.9 is needed for 5% FWER and 3.0 for 1% FDR (§5, p. 32).
- About 70% of the statistically "true" factors have Sharpe ratios below 0.5 (p. 34).
- Theory-motivated factors may face a lower hurdle, but 2.0 is still too low (p. 2).

## Limits and risks to validity
_My assessment:_ the hurdles are calibrated to published cross-sectional factor research, not to one researcher's model search; for this project the lesson is the method (count every trial, control FDR or FWER), not the exact 3.0. Read via summarising fetch.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Meta-study of reported results |
| Baselines | N/A |  |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 2 | 316 factors, 1967–2012 |
| Statistical testing | 2 | Multiple-testing correction is the subject |
| Reproducibility | 1 | Factor list published; no code |
| **Total** | 5/6 → **12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "most claimed research findings in financial economics are likely false" (abstract, p. 1)
