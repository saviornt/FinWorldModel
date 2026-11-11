---
type: lit-note
title: "Can AI weather models predict out-of-distribution gray swan tropical cyclones?"
authors: [Y. Qiang Sun, Pedram Hassanzadeh, Mohsen Zand, Ashesh Chattopadhyay, Jonathan Weare, Dorian S. Abbot]
year: 2024
venue: arXiv (physics.ao-ph), v3 May 2025
source_url: https://arxiv.org/abs/2410.14932
doi: 10.1073/pnas.2420914122
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.8, RQ3.4, RQ4.5]
family: [novelty-detection]
evidence: Moderate
score: 7
tags: [lit-note, family/novelty-detection]
---
# Can AI weather models predict gray swan tropical cyclones? (Sun, 2024)

**Basis:** arXiv v3 (15 May 2025) read through alphaXiv page excerpts (pp. 1–3, 5–9, 13, 15–20, 23). Not a finance paper; kept because it is the cleanest controlled test read of whether a deep model can forecast events stronger than any in its training data (guide step 4: transfers).

**Takeaway:** A FourCastNet trained with all Category 3–5 cyclones removed matches the full model on ordinary weather but cannot forecast Category 5 storms — it predicts moderate storms instead (false negatives with no sign of error); it does extrapolate if similar storms were seen in another ocean basin, and standard skill metrics hide the failure.

## Problem
Can AI models extrapolate from weaker training events to stronger, unseen "gray swan" extremes (p. 1)?

## Data and period
ERA5 reanalysis, train 1979–2015, test 2018–2023; 20 Category 5 tropical cyclones in the test set (pp. 1, 8).

## Method
Five training sets: Full; noTC (samples with tropical mslp below 988 hPa removed); Rand (same size as noTC, removed at random); noWP and noNA (strong storms removed in one basin) — 5 seeds each, 25 models; 51-member perturbed initial-condition ensembles (pp. 3, 5).

## Baselines and validation
Full and Rand act as controls for data removal and training-set size (p. 7). Out-of-sample test years.

## Results (with page or section references)
- noTC performs much worse on Hurricane Lee and stays above 980 hPa; its forecasts are false negatives (p. 6).
- Across all 20 Cat-5 storms, noTC underpredicts intensity; when started in the strong phase it predicts weakening, relaxing toward intensities seen in training (p. 7).
- A 25% smaller training set (Rand) does not reduce skill, so data removal size is not the cause (p. 7).
- noTC has similar global, tropical and Cat 1–2 skill (ACC, RMSE), so "common metrics can obscure poor performance" (pp. 7, 15).
- Strong extratropical cyclones in training do not help, because the dynamics differ (p. 9); strong storms in another basin do help (pp. 9, 15).
- Weighted losses cannot help with events absent from training; generated synthetic extremes are not shown to be realistic beyond the generator's training data (p. 18).

## Limits and risks to validity
_My assessment:_ one model, one event type, physical system with stable dynamics — markets are reflexive and non-stationary, which can only make extrapolation harder. The transferable lessons: (1) a deep forecaster trained on calm and moderate periods should not be expected to forecast a larger-than-seen shock; (2) "unprecedented" should be judged against all analogous events in the pooled training data (other markets, other eras), not local history; (3) evaluate on held-out extremes, not average error.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Held-out years plus controlled removal, 5 seeds × 51 ICs |
| Baselines | 1 | Full and Rand controls; no non-AI model compared |
| Point-in-time and leakage controls | N/A | Physical reanalysis; removal is the design |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | 20 Cat-5 storms, one model |
| Statistical testing | 1 | Ensemble spread and "significantly better" basin tests; no formal multiple-testing |
| Reproducibility | 0 | Code not noted in pages read |
| **Total** | **5/10 → 7/14** | Moderate (as transfer evidence) |

## Quotes worth keeping (each under 15 words, with page)
- "the burden of proof is on anyone who claims it" (p. 20)
