---
type: lit-note
title: "Which Leakage Types Matter? A Quantitative Landscape Across 2,047 Benchmark Datasets"
authors: [Simon Roth]
year: 2026
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2604.04199
doi: 10.48550/arXiv.2604.04199
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.6, RQ3.1]
family: [cleaning]
evidence: Moderate
score: 9
tags: [lit-note, family/cleaning, leakage, preprocessing]
---
# Which Leakage Types Matter? (Roth, 2026)

**Basis:** arXiv 2604.04199v2 pages 1–3, 7–10, 16–18, 23–24, 27, 34–36 read via alphaXiv on 2026-11-08.

**Takeaway:** On 2,047 iid tabular datasets, fitting scalers, PCA, encoders or outlier filters on the full data before cross-validation changed AUC by less than 0.005 (an O(p/n) effect), while choosing models or seeds by test score (+0.04), duplicates (up to +0.07) and using random instead of time-ordered folds on data with real drift (+0.023) mattered far more; feature selection on all data mattered only when features are many relative to rows (+0.018 at p/n > 0.1).

## Problem
Which kinds of leakage inflate scores, and by how much?

## Data and period
2,047 binary classification datasets (OpenML, PMLB); a boundary experiment on 129 temporal datasets (92 FOREX as null control, 14 genuine temporal) (pp. 1, 27).

## Method
Within-dataset counterfactuals: clean vs leaky 5-fold CV with the same folds and seed; 29 experiments in four classes (estimation, selection, memorisation, boundary) (pp. 7–8). Discovery/confirmation split of datasets; Benjamini–Hochberg correction (p. 8).

## Baselines and validation
Clean pipeline as the comparator; placebo (seed-only) noise floor of about 0.003 AUC (p. 9).

## Results (with page or section references)
- Normalisation on full data: ΔAUC 0.000 for LR and RF; chained scaling+encoding+PCA −0.007 (Table 1, p. 9).
- Test-set peeking +0.040, best-of-10 seeds +0.045 (p. 3); peeking still about +0.039 at n = 10,000 (Table 6, p. 17).
- Duplicates: up to d_z 1.38 for decision trees at 30% duplication (p. 1).
- Temporal: +0.023 on genuine temporal datasets, −0.006 on FOREX (p. 27).
- Feature selection on all data: +0.001 typical, +0.018 at p/n > 0.1 (p. 27).

## Limits and risks to validity
iid tabular classification; temporal part small (14 datasets) and non-financial; normalisation result may not hold for non-stationary series where full-sample statistics carry future level information; single author; LLM-assisted writing disclosed (p. 36).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | CV within datasets; confirmation split |
| Baselines | 1 | Clean pipeline |
| Point-in-time and leakage controls | 2 | The subject |
| Costs and realism | N/A | |
| Sample breadth | 1 | Very many datasets, few temporal, none financial panels |
| Statistical testing | 2 | FDR correction |
| Reproducibility | 1 | Code public; raw results not yet |
| **Total** | 8/12 → 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the leakage type most prominent in standard references (normalization) matters least" (p. 1)
