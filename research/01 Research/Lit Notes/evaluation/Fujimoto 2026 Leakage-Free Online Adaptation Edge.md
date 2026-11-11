---
type: lit-note
title: "When Does Online Adaptation Pay on the Edge? A Leakage-Free Evaluation of Warmup, Learning-Rate Selection, and Resource Trade-offs for Time-Series Forecasting"
authors: [Takumi Fujimoto, Hiroaki Nishi]
year: 2026
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2609.01126
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.9]
family: [evaluation]
evidence: Moderate
score: 9
tags: [lit-note, family/evaluation, adaptation, leakage, non-finance]
---
# When Does Online Adaptation Pay? Leakage-Free Evaluation (Fujimoto & Nishi, 2026)

**Basis:** alphaXiv PDF pages 1–6, 9 (v1, 1 Sep 2026). Keio University. Code, data and numbers: github.com/keiotakmin/tsf-edge-adaptation.

**Takeaway:** Even with leakage-free streaming, the measured benefit of online adaptation moves by 3–19 points depending only on how long the static baseline was trained, and an optimizer comparison flips depending on a shared default learning rate; choosing both on a held-out slice of the latest pre-drift data fixes most of this without touching test data.

## Problem
Which evaluation choices, beyond target leakage, bias the measured benefit of online adaptation? (§I)

## Data and period
ETTh1, ETTh2, ETTm1, ETTm2, UCI Appliances, Building Data Genome 2 smart meters; first half warmup, second half streamed test; z-scores from warmup only (§III).

## Method
Non-overlapping windows at stride H; each target scored before it can enter a gradient. Static vs full, head-only and calibration adaptation with SGD+momentum or Adam; periodic and drift-triggered schedules (§III).

## Baselines and validation
Static (no adaptation) model; delayed-adaptation control to verify the protocol; 3–5 seeds; dispersion descriptive only (§III).

## Results (with page or section references)
- Target leakage inflates the reported benefit by +11.3 to +39.8 pp and flips its sign on ETTh2/PatchTST (+24.2% leaky vs −15.6% delayed) (§III).
- Baseline warmup effect is U-shaped: under- and over-trained static baselines both inflate adaptation benefit (by up to +26.0 and +21.9 pp); within a practical 1,000–20,000-step range the benefit still moves 3.0–18.8 pp (Table I, §IV-A).
- Validation early-stopping on the latest 20% of pre-drift data lands within +3.4 pp of the test-selected oracle (§IV-A).
- At a shared rate 10⁻³, Adam is worse than static in 174/360 cells (SGD+m 29/360); with rates rehearsed on the validation slice, Adam wins 310/360 and is below static in 4 (Table II, §IV-B).
- Parameter-efficient (head/calibration) variants are non-dominated on adaptation memory (§IV-C).
- Smart-meter gains depend on meter-selection rules (abstract).

## Limits and risks to validity
_Authors:_ device latency and energy not measured on target hardware.
_My assessment:_ non-financial; no naive forecast baseline; no significance tests. The two biases it isolates (baseline training budget, shared hyperparameters) apply to any adaptive market model.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Leakage-free streaming, verified against a control |
| Baselines | 1 | Validation-tuned static model; no naive forecast |
| Point-in-time and leakage controls | 2 | Score-before-update by construction; warmup-only scaling |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Six non-finance streams |
| Statistical testing | 0 | Descriptive standard deviations only |
| Reproducibility | 2 | Code, data and all numbers released |
| **Total** | 8/12 → **9/14** | Moderate (non-finance) |

## Quotes worth keeping (each under 15 words, with page)
- "it does not certify stability under drift." (§IV-B, p. 6)
