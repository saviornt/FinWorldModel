---
type: lit-note
title: "Training on the Future: A Delay-Aware Audit of Test-Time Adaptation for Time-Series Forecasting"
authors: [Mohamed Readh Fentazi, Mazene Ameur, Adlen Ksentini]
year: 2026
venue: arXiv (cs.LG)
source_url: https://arxiv.org/abs/2610.12232
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ4.9]
family: [evaluation]
evidence: Strong
score: 12
tags: [lit-note, family/evaluation, adaptation, leakage, negative-result, non-finance]
---
# Training on the Future: Delay-Aware Audit of Test-Time Adaptation (Fentazi, Ameur & Ksentini, 2026)

**Basis:** alphaXiv full text (v1, 8 Oct 2026), sections 1–7 and appendices read for setup, results and limitations. EURECOM. Non-finance benchmarks; cited for evaluation method.

**Takeaway:** When an H-step forecast's label is released for adaptation only after it exists (delay d ≥ H), four published test-time adapters (TAFAS, COSA, PETSA, DynaTTA) rarely beat their own frozen model by more than 0.5%, are sometimes significantly worse, and lose to a 30-line closed-form recursive-least-squares corrector on most streams; leaky next-step updates inflate simple adapters' gains by up to 110%.

## Problem
Is the published gain of test-time adaptation (TTA) for forecasting real once labels are only used after they mature, and with realistic pipeline delay on top? (§1)

## Data and period
Five standard non-financial streams: ETTm1, ETTh2, Weather, Electricity, Traffic (§1, §5).

## Method
A harness that releases the label of forecast origin s for updates only at step s + d, with d = H (minimum causal delay), d > H (pipeline latency) and d = 1 (legacy leaky reference). Delay is enforced by logged patches inside each method's own released code and checkpoints (PatchTST backbone). References: a bank of RLS filters over forgetting factors combined by per-coordinate median (no tuned hyperparameters; 56 µs per step), and an ELF-style linear corrector (§1, §4).

## Baselines and validation
Frozen checkpoint, persistence, bias-EMA, best gradient adapter (oracle learning rate), RLS bank, ELF-style corrector; three checkpoint seeds on ETT streams; block-bootstrap significance (§5).

## Results (with page or section references)
- On ETTm1 all four methods adapt, but the RLS bank beats three of four at every delay; only DynaTTA beats it, at d = H only, at ~2,500× the per-update cost; the ELF-style corrector beats all four (abstract, §1).
- On the other four datasets the largest significant gain of any published method over its frozen checkpoint is 0.5%; on each, at least one method is significantly worse than frozen at d = H (abstract).
- On drift-heavy ETTh2, longer delays make every adapter that separates from frozen significantly harmful (abstract).
- Leaky d = 1 updates inflate bias-EMA's apparent gain: causal MSE exceeds leaky MSE by 83% (ETTh2/DLinear) and 110% (ETTh2/PatchTST); under leakage simple adapters "beat" persistence, under causal updates none does (§5.1, Fig. 1).
- The backbone training recipe moves frozen online error by up to 25×, more than any adaptation effect (§1, §7).
- Gradient adapters are fragile: 3–11 of 12 learning-rate configurations diverge per cell; Electricity diverges for all plain-SGD settings (§5).
- Recommendations: delay-aware protocol, closed-form correctors as mandatory baselines, report adaptation cost and the backbone recipe (§7).

## Limits and risks to validity
_Authors (§7):_ one deep architecture (PatchTST); reduced method sets and single checkpoints on the wide streams; ELF-style corrector limited to ≤21 channels.
_My assessment:_ non-financial data, so no evidence on market regimes; but the protocol failures it measures (label leakage, missing closed-form baselines) apply directly to any adaptive market model. No multiple-testing correction across the many cells.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Causal streaming with explicit label delay |
| Baselines | 2 | Frozen, persistence, closed-form RLS and ELF correctors |
| Point-in-time and leakage controls | 2 | Delay enforced inside each method's code; leaky arm measured |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 1 | Five non-finance streams |
| Statistical testing | 1 | Block bootstrap; no multiplicity correction |
| Reproducibility | 2 | Harness, patches and cached runs released |
| **Total** | 10/12 → **12/14** | Strong (non-finance; method point only) |

## Quotes worth keeping (each under 15 words, with page)
- "what separates methods is evaluation practice, not adaptation machinery." (§7)
