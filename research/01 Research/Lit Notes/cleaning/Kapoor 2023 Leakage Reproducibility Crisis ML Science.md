---
type: lit-note
title: "Leakage and the Reproducibility Crisis in ML-based Science"
authors: [Sayash Kapoor, Arvind Narayanan]
year: 2023
venue: Patterns (arXiv 2207.07048)
source_url: https://arxiv.org/abs/2207.07048
doi: 10.1016/j.patter.2023.100804
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6, RQ3.1]
family: [cleaning]
evidence: Moderate
score: 8
tags: [lit-note, family/cleaning, leakage, preprocessing]
---
# Leakage and the Reproducibility Crisis in ML-based Science (Kapoor, 2023)

**Basis:** arXiv 2207.07048v1 pages 1–5, 8, 17, 29 read via alphaXiv on 2026-11-08. The journal DOI is the Patterns version as recorded by the authors' later work; the Patterns article itself was not opened.

**Takeaway:** A survey of 20 reviews across 17 fields found leakage in 329 papers and gave an eight-type taxonomy (preprocessing on train and test together, feature selection on all data, duplicates, illegitimate features, temporal leakage, non-independence, sampling bias); in civil-war prediction, every paper claiming complex ML beat logistic regression failed once imputation-on-all-data and temporal k-fold leakage were fixed.

## Problem
How common is data leakage in applied ML, and what forms does it take?

## Data and period
Literature survey (Table 1, p. 2); reproduction of 12 civil-war prediction papers with code and data, 2016–2021 (pp. 8, 17).

## Method
Taxonomy L1.1–L3.3 (p. 5); "model info sheets" as a reporting checklist (pp. 2, 29); re-analysis correcting each leak.

## Baselines and validation
Logistic regression as the baseline in the case study; corrected train/test separation.

## Results (with page or section references)
- 329 affected papers across 17 fields (p. 1).
- Muchlinski et al. imputed training and test data together, with 95% of the out-of-sample data missing (p. 3).
- Wang (2019): AUC gap between AdaBoost and logistic regression shrank from 0.14 to 0.01 after the fix (p. 8).
- Kaufman et al. (2019): k-fold on temporal data plus proxy features; after correction no model beat a previous-year baseline (p. 3).
- 9 of 12 papers reported no significance tests (p. 8).

## Limits and risks to validity
Survey is a lower bound, not systematic; case study is one non-financial field.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Corrected train/test splits |
| Baselines | 1 | Logistic regression, previous-year baseline |
| Point-in-time and leakage controls | 2 | The subject of the paper |
| Costs and realism | N/A | |
| Sample breadth | 1 | 17-field survey; one case-study field |
| Statistical testing | 0 | Not central |
| Reproducibility | 2 | Code and data released |
| **Total** | 7/12 → 8/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "data leakage is a pitfall in every single case" (p. 4)
