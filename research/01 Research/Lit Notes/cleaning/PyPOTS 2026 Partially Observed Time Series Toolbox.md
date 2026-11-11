---
type: lit-note
title: "PyPOTS: a Python toolbox for machine learning on partially-observed time series"
authors: [Wenjie Du]
year: 2026
venue: PyPI project page (version 1.5)
source_url: https://pypi.org/project/pypots
doi: ''
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Primary documentation
tags: [lit-note, family/cleaning, imputation]
---
# PyPOTS toolbox (PyPI page, 2026)

**Basis:** PyPI page read via page fetch on 2026-11-08 (summarised by the fetch tool; no page numbers).

**Takeaway:** PyPOTS 1.5 (5 May 2026, BSD licence) catalogues about 45 learned imputation models plus naive baselines (linear interpolation, LOCF/NOCB, mean, median) and evaluates imputation by masking held-out values and scoring MAE; it says nothing about look-ahead or financial data, so its default evaluation measures reconstruction error, not downstream forecasting value.

## Problem
Catalogue of methods for missing-value multivariate time series (guide seed for RQ3.4).

## Data and period
Examples use PhysioNet 2012 (healthcare).

## Method
Imputation, forecasting, classification, clustering and anomaly detection models (e.g. SAITS, BRITS, GRU-D, CSDI, TimesNet).

## Baselines and validation
Masked-value MAE on validation and test sets.

## Results (with page or section references)
- About 45 learned imputers; four naive baselines.
- Note: LOCF/NOCB means "last observation carried forward / next observation carried backward"; NOCB and bidirectional models use future values.

## Limits and risks to validity
Documentation, not evidence of benefit.

## Rubric scores
Primary documentation (not scored).

## Quotes worth keeping (each under 15 words, with page)
- None.
