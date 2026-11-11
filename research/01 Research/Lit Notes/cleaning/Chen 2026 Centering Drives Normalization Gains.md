---
type: lit-note
title: "Centering Drives Normalization Gains: Price-Offset Nuisances in Cross-Sectional Return Prediction"
authors: [Mingju Chen, Qianhui Liu, Yui Lo, Yuanhang Liu]
year: 2026
venue: arXiv (cs.CE)
source_url: https://arxiv.org/abs/2609.07122
doi: 10.48550/arXiv.2609.07122
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.6]
family: [cleaning]
evidence: Moderate
score: 9
tags: [lit-note, family/cleaning, normalisation]
---
# Centering Drives Normalization Gains (Chen, 2026)

**Basis:** arXiv 2609.07122v2 full PDF (pp. 1–5) read via alphaXiv on 2026-11-08.

**Takeaway:** On a point-in-time CSI 300 five-minute panel, per-window instance normalisation raises next-day rank IC for all eight parameter-matched encoders (+0.014 to +0.057), and the gain comes from removing each stock's price-level offset (centering, last-value or differencing), not from rescaling; normalisation matters more than the choice of encoder.

## Problem
Is the gain from instance normalisation (RevIN) in cross-sectional return ranking due to offset removal, scale removal or the encoder?

## Data and period
CSI 300 five-minute bars, Qlib 2019–2022 plus Baostock 2023–2025; point-in-time constituents; unadjusted inputs, adjusted labels (p. 3). Train 2019–2023, validate 2024, test 2025 (242 days), two-day embargo.

## Method
Input: 240 five-minute bars × 6 fields after training-only global log(1+x) and z-score. Eight encoders matched to ~234k parameters (GRU, LSTM, TCN, Transformer, PatchTST, Mamba, MLP, SSM), with and without RevIN; a parameter-free ladder (identity, scale only, centre, last value, difference, standardise) and channel-scope ablations (pp. 2–3). Statistics of each window come only from that backward-looking window.

## Baselines and validation
No-normalisation arms; two hand-crafted short-term reversal factors (raw IC 0.055 and 0.048); style residualisation. Moving-block bootstrap, Holm correction, TOST equivalence with a pre-set margin; contrasts set before the test year was inspected (p. 3).

## Results (with page or section references)
- RevIN raises rank IC for all eight encoders, e.g. GRU 0.036 → 0.088, LSTM 0.037 → 0.094 (Table 1, p. 3); all survive Holm correction.
- Gains among six strong encoders (0.038–0.057) exceed the spread between encoders after normalisation (0.011) (p. 1, p. 3).
- Scale-only normalisation does not help (−0.010 linear, −0.003 GRU); centering gives +0.029 / +0.052 (Table 2, p. 4).
- Price-only standardisation keeps 93–101% of the gain; volume/amount-only adds nothing significant (Table 3, p. 4).
- Gains not explained by short-term reversal (p. 4).

## Limits and risks to validity
One market, one bar frequency, one test year, three seeds; no trading or costs; no industry controls (public panel). Code not stated.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | One chronological split with embargo |
| Baselines | 1 | Reversal factors, no-norm arms; no GBT |
| Point-in-time and leakage controls | 2 | PIT constituents, training-only global stats, backward-only windows, embargo |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | One index, one stress-free test year |
| Statistical testing | 2 | Block bootstrap + Holm + TOST |
| Reproducibility | 1 | Public data; code not stated |
| **Total** | 8/12 → 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Centering drives the reliable effect, while scale-only normalization does not help." (p. 1)
