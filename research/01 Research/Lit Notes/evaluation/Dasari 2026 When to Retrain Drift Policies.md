---
type: lit-note
title: "When to Retrain: An Empirical Study of Retraining Policies for Streaming ML Under Concept Drift, Budget, and Latency Constraints"
authors: [Sawan Dasari]
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2608.19488
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.9]
family: [evaluation]
evidence: Strong
score: 10
tags: [lit-note, family/evaluation, adaptation, drift-detection, retraining, non-finance]
---
# When to Retrain: Retraining Policies Under Drift, Budget and Latency (Dasari, 2026)

**Basis:** alphaXiv PDF pages 1–15 (v1, 19 Aug 2026). Single author. Code and artefacts: github.com/sa1dasari/Study-of-Drift-Triggered-Retraining-Policies-Under-Budget-and-Latency-Constraints.

**Takeaway:** Across 3,933 runs, periodic retraining beat error-threshold and ADWIN drift-triggered retraining under abrupt and gradual drift (by 8.6–16.0 points of post-drift accuracy), drift triggers won only under recurring drift (not significant after correction), and when the model also learned incrementally, no retraining policy beat never retraining.

## Problem
When should a deployed model be retrained, given a finite retraining budget and training-plus-deployment latency? (§1)

## Data and period
Synthetic 10,000-step streams with abrupt, gradual or recurring drift; LUFlow network-intrusion flows; LendingClub loans 2007–2018 (origination-time features, year cohorts across 2012–2016 policy changes). Three of five candidate real datasets rejected by a pre-registered drift-suitability check (§5.3).

## Method
Linear SGD classifier; policies: periodic, error-threshold, ADWIN on the error stream, no-retrain; budgets K ∈ {5,10,20}; five latency levels; with and without per-sample incremental updates (§2, §4–5).

## Baselines and validation
Prequential (predict-then-learn) streams; 10 seeds synthetic, 3 stream configurations per real dataset; paired t-test and Wilcoxon with Holm–Bonferroni, Cohen's d, pre-defined practical-significance rule (§5.5).

## Results (with page or section references)
- With incremental updates: 0 of 54 policy comparisons practically significant; on LendingClub no-retrain 0.715 vs periodic 0.702 (Table 3).
- Static model: periodic 0.658 / 0.844 / 0.704 vs no-retrain 0.505 / 0.287 / 0.489 (synthetic / LUFlow / LendingClub) (Table 4).
- Periodic beats error-threshold by 8.6 pp (abrupt) and 9.8 pp (gradual), and ADWIN by 9.0 and 16.0 pp, all Holm-corrected p ≤ 0.011 (Table 6).
- Error-threshold spends 66–77% of its budget before the drift on noise; ADWIN misses gradual drift (zero retrains in all 27 gradual configurations at 3 seeds) (§6.4).
- On a fraud dataset, ADWIN exhausted its budget on false alarms in 51 of 54 calibrations (§5.3).
- If retrain + deploy latency exceeds the retrain interval, the effective budget halves (§6.5).

## Limits and risks to validity
_Author (§7.5):_ linear learner only; labels assumed immediate (label delay untested); 3 configurations per real dataset limits power.
_My assessment:_ not market data; drift is mostly injected. The "simple schedule beats detector" result transfers as a baseline requirement, not as a magnitude.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Prequential streams |
| Baselines | 1 | No-retrain and periodic; one learner class |
| Point-in-time and leakage controls | 1 | Pre-drift scaler, origination-time features; immediate labels assumed |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Synthetic + two real streams |
| Statistical testing | 2 | Paired tests with Holm–Bonferroni |
| Reproducibility | 2 | Code, pipelines and per-run artefacts |
| **Total** | 9/12 → **10/14** | Strong (non-finance; method point only) |

## Quotes worth keeping (each under 15 words, with page)
- "Statistical rigor in detection does not equal decision quality." (§7.2, p. 14)
