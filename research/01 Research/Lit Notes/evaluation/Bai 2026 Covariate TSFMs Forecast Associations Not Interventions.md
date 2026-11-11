---
type: lit-note
title: "Forecasting Associations, Not Interventions: A Preregistered Causal Audit of Covariate-Aware Time Series Foundation Models"
authors: [Zong-Han Bai]
year: 2026
venue: "arXiv cs.LG"
source_url: https://arxiv.org/abs/2610.31869
doi: ""
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.15]
family: [evaluation]
evidence: Weak
score: 5
tags: [lit-note, family/evaluation, world-model]
---
# Forecasting Associations, Not Interventions: A Causal Audit of Covariate-Aware TSFMs (Bai, 2026)

**Basis:** arXiv v1 (22 Oct 2026), pp. 1–2, 4–6, 9–10, 16 (Tables 1–2, Figs. 2–3, 7), via the alphaXiv PDF reader.

**Takeaway:** Asked "what if this covariate path were different?", Chronos-2, TiRex-2, TabPFN-TS and TimesFM-2.5 answer with the observational association, not the causal effect: on a preregistered synthetic grid their confounding gaps track the least-squares prediction (R² 0.90–1.00) at 1.3–1.8× its size, they report a spurious effect of 0.44–0.72 when the true effect is zero, and on real randomized physical systems they under-respond by 2–5×.

## Problem
Covariate-aware sequence models invite scenario queries; does their answer reflect intervention or association (pp. 1–2)?

## Data and period
Synthetic linear and nonlinear structural models with exact counterfactuals (L = 512, H = 64, 600 episodes per cell); DoTime benchmark; two Causal Chambers systems with randomized actuators (pp. 4, 16).

## Method
Confounding gap = effect estimate under observational minus randomized context; closed-form reference for in-context least squares; confounder hidden, past-only or known-future; linear probes; post-training repairs with replay and LoRA (pp. 2, 4–5, 9–10).

## Baselines and validation
In-context OLS control (slope 1.000, R² 1.000); preregistered thresholds with recorded amendments; 1,000-sample bootstrap CIs (pp. 4–5).

## Results (with page or section references)
- Impact slopes vs the OLS line: Chronos-2 1.64–1.78, TiRex-2 1.34–1.56, TabPFN-TS 1.00, TimesFM-2.5+XReg 1.26–1.62 (p. 5, Table 1).
- True effect 0: reported effects 0.47, 0.48, 0.44, 0.72 under observational context; 0.00 under randomized context (p. 6).
- Supplying the confounder's future removes only part of the gap (Chronos-2 to 58%; TiRex-2 107%) (p. 5).
- Synthetic interventional post-training with replay cut the gap 52–61% at +1–3% MASE (p. 9, Table 2).

## Limits and risks to validity
_My assessment:_ no financial data; single author; code not yet released. It matters for the world-model hypothesis because a market model conditioned on macro or event covariates trained on observational data will give associational, not causal, "what-if" answers unless trained otherwise.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Synthetic audit |
| Baselines | 1 | OLS reference |
| Point-in-time and leakage controls | N/A | — |
| Costs and realism | N/A | — |
| Sample breadth | 1 | Synthetic grid plus two physical systems |
| Statistical testing | 1 | Preregistration, bootstrap CIs |
| Reproducibility | 0 | Release promised, not yet available |
| **Total** | **3/8 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "should be used as an effect only on experimental context" (p. 10)
