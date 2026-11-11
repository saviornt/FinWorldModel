---
type: lit-note
title: "Rethinking Synthetic Scenario Realism: Compatibility, Not Fidelity, Drives Hedging Performance"
authors: [Ryuji Hashimoto, Ryota Ozaki, Kentaro Imajo, Masanori Hirano]
year: 2026
venue: arXiv (preprint, University of Tokyo / Preferred Networks)
source_url: https://arxiv.org/abs/2608.20842
doi: 10.48550/arXiv.2608.20842
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Weak
score: 4
tags: [lit-note, family/cleaning, synthetic-data]
---
# Compatibility, Not Fidelity, Drives Hedging Performance (Hashimoto, 2026)

**Basis:** arXiv 2608.20842 full text read via alphaXiv on 2026-11-08.

**Takeaway:** Statistical realism of a scenario generator (eight distribution and autocorrelation distances) does not consistently predict how well a deep hedger trained on it performs on real data, and generator rankings change with the hedger class and task: synthetic data must be judged on the downstream task, not on how real it looks.

## Problem
Does a more realistic generator give a better hedging policy?

## Data and period
Generators calibrated on daily Nikkei 225, 2018–2022; hedgers tested January 2023 – February 2026 (§5.3).

## Method
GBM, Merton jump, Heston and VAE generators; linear, MLP and no-transaction-band hedgers; European and lookback calls with two cost levels; entropic risk and CVaR. A bound links hedging degradation to learning error plus a "compatibility gap".

## Baselines and validation
Generators ranked against each other; single train/test split.

## Results (with page or section references)
- Realism does not consistently predict hedging performance; rankings depend on hedger class and task (§7).

## Limits and risks to validity
One index; compatibility is not directly measurable; no significance tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One split |
| Baselines | 1 | Classical generators |
| Point-in-time and leakage controls | N/A | |
| Costs and realism | 1 | Two flat cost levels |
| Sample breadth | 0 | One index |
| Statistical testing | 0 | None |
| Reproducibility | 0 | No code found |
| **Total** | 3/12 → 4/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- "higher statistical realism does not consistently improve hedging performance" (§7)
