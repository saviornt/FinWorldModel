---
type: lit-note
title: "purgedcv: scikit-learn-compatible purged and combinatorial cross-validation"
authors: [E. S. Lazarev]
year: 2026
venue: GitHub / PyPI documentation
source_url: https://github.com/eslazarev/purged-cross-validation
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.6, RQ4.1]
family: [cleaning]
evidence: Primary documentation
tags: [lit-note, family/cleaning, cross-validation, leakage]
---
# purgedcv documentation (2026)

**Basis:** GitHub README read via page fetch on 2026-11-08 (summarised); PyPI page seen in search. Author name taken from the repository owner handle; full name not confirmed.

**Takeaway:** The guide's seed demo shows naive shuffled k-fold "finding" R² 0.83–0.91 on a target built to be unpredictable, falling below the mean baseline (−1.48 to −1.87) once overlapping labels are purged; on real smart-meter data, group-aware selection deployed better in all 30 partitions; the README gives no rule for fitting scalers inside folds.

## Problem
Show how overlapping labels and grouped rows make shuffled cross-validation report skill that does not exist.

## Data and period
Synthetic unpredictable target; UK Low Carbon London smart meters; daily BTC/USDT 2021–2023.

## Method
Purge, embargo, purged (group) k-fold, walk-forward, CPCV, probabilistic and deflated Sharpe ratios; scikit-learn splitter protocol, usable inside Pipeline.

## Baselines and validation
Predict-the-mean reference.

## Results (with page or section references)
- Synthetic: k-NN 0.83 / RandomForest 0.91 R² under shuffled k-fold vs −1.48 / −1.87 purged; 100% vs 0% label overlap (README).
- Smart meters: naive selection deployed at 2.638 kWh MAE vs 2.464 for purged-group selection (≈6.6% better), all 30 partitions.
- BTC: both selections lost money; naive pick Sharpe −0.77 vs −0.26.

## Limits and risks to validity
Vendor-style documentation by the library author; demos chosen to illustrate the point; read via summary.

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
