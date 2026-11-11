---
type: lit-note
title: "End-to-End Parametric Portfolio Policies for Cross-Asset Futures Timing: When Do AI Models Beat Simple Rules?"
authors: [Austin Pollok, Kevin Robik]
year: 2026
venue: arXiv (q-fin.ST)
source_url: https://arxiv.org/abs/2607.00475
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP4 Training and Evaluation]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.9, RQ1.7, RQ4.6]
family: [rl-planning]
evidence: Strong
score: 12
tags: [lit-note, family/rl-planning]
---
# End-to-End Portfolio Policies vs Simple Rules on Liquid Futures (Pollok, 2026)

**Basis:** Full PDF read through alphaXiv, pp. 1–8.

**Takeaway:** A transformer policy trained directly on a differentiable Sharpe loss (a policy-function approximation, the non-RL cousin of policy-gradient trading) only matches equal weighting on 16 liquid CME futures out of sample (net Sharpe 0.54 vs 0.52; bootstrap P(better) = 0.59), and its one significant result (equities) is mostly market beta; mixture-of-experts, more features and ensembles did not help.

## Problem
When does a policy that maps market states straight to portfolio weights beat the rules a practitioner would run (1/N, risk parity, time-series momentum) (pp. 1–2)?

## Data and period
16 most liquid CME futures across six asset classes, daily 2000–2024 (Barchart continuous contracts); cross-asset out-of-sample period 2011–2024 (pp. 2, 4).

## Method
Transformer (Time2Vec, 4 encoder/decoder layers, causal mask) and LSTM policies with a signed-softmax weight layer, trained on negative Sharpe; optional turnover penalty; three-seed averaging (pp. 3, 7). Expanding-window walk-forward: first 40% for training, re-fit in ~4-year blocks with a chronological 90/10 train/validation split (p. 4). All features use trailing data only (p. 2).

## Baselines and validation
1/N, 60-day inverse-volatility risk parity, 12-month TSMOM; Bonferroni-adjusted Sharpe t-tests across seven universes; stationary bootstrap on Sharpe differences; Newey–West alpha/beta decomposition (pp. 4–7).

## Results (with page or section references)
- Cross-asset Sharpe (gross / net 2 bp): 1/N 0.52 / 0.52; TSMOM 0.37 / 0.35; LSTM 0.50 / 0.33; transformer 0.55 / 0.54 (Table II, p. 5).
- Bootstrap probability the transformer beats 1/N is 0.59, risk parity 0.99, TSMOM 0.68 (p. 4).
- At 10 bp the LSTM falls to −0.38 while the transformer stays ~0.50; LSTM turnover 0.17/day vs 0.02 (Table III, p. 6).
- TSMOM wins rates and FX; 1/N wins energy; only equity-index learned Sharpes survive Bonferroni (t ≈ 3), and for the transformer that is mostly beta (alpha +0.8%, n.s.) (pp. 4, 7; Table IV).
- Engineered regime features helped in-sample but not out of sample; MoE, per-class tuning and cross-model ensembles did not improve net results; seed averaging was the only reliable gain (pp. 3–4, 7).

## Limits and risks to validity
Seed-sensitive; recipe tuned mainly on the LSTM; one daily frequency and two architectures; no code (p. 8). _My assessment:_ the strongest-designed paper found for RQ1.9; its negative-leaning result is credible because the baselines are the right ones.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Expanding walk-forward, 2011–2024 |
| Baselines | 2 | 1/N, risk parity, TSMOM (the strong simple rules for allocation) |
| Point-in-time and leakage controls | 2 | Trailing-only features, causal mask, stated explicitly |
| Costs and realism | 2 | 2 bp with 0–10 bp sensitivity and turnover |
| Sample breadth | 2 | 16 contracts, 6 classes, 14 years incl. 2020 |
| Statistical testing | 2 | Bonferroni plus bootstrap and HAC |
| Reproducibility | 0 | No code or data |
| **Total** | **12/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "Added complexity also does not automatically help." (p. 2)
