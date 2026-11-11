---
type: lit-note
title: "Learning the Context of Errors: Black-Box Online Adaptation of Time Series Foundation Models"
authors: [Xilin Dai, Yiding Liu, Hongjie Xia, Yifan Hu, Zewei Dong, Jiang-Ming Yang, Qiang Xu]
year: 2026
venue: NeurIPS 2026
source_url: https://arxiv.org/abs/2606.14222
doi: ""
accessed: 2026-11-09
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.9]
family: [price-time-series]
evidence: Moderate
score: 8
tags: [lit-note, family/price-time-series, adaptation, foundation-models, non-finance]
---
# ORCA: Black-Box Online Adaptation of TSFMs (Dai et al., NeurIPS 2026)

**Basis:** alphaXiv PDF pages 1–4, 8–10, 16, 18, 23 (v2, 3 Oct 2026). Ant International / CUHK. Code: github.com/Fifthky/ORCA.

**Takeaway:** A frozen foundation model can be corrected online, without touching its weights, by a small linear adapter that predicts its residual from the input window plus the model's own forecast, mixed in by a router that trusts whichever of the two has had lower recent error; this cuts MSE by about 6.3% on average across five TSFMs and eight datasets, while white-box/grey-box adapters ported to the same setting made errors worse — but on the exchange-rate (financial) series the gain was 0%.

## Problem
How to adapt a closed, API-only TSFM to streaming data under drift (§1).

## Data and period
ETTh1/2, ETTm1/2, Exchange, Weather, Electricity, Traffic; chronological 7:1:2 split; horizons 30/96/336 (App. A).

## Method
Linear adapter with trend/seasonal decomposition and channel mixing on [X_t, Ŷ_base]; FIFO replay buffer with forgetting decay; predictive-space Bayesian loss; Boltzmann router weighting base vs adapted forecast by exponentially averaged past errors (§3).

## Baselines and validation
Zero-shot Chronos-2, Moirai-2, TiRex, TimesFM-2.5, Sundial; black-box ELF and δ-Adapter (Ada-Y); SOLID, TAFAS, DSOF ported to black-box; Ridge and ETS residual correctors (§4.3, App. C.3). Labels enter the buffer only at t + H, when the full horizon is observed (App. A.1). Three seeds (App. D.1).

## Results (with page or section references)
- Average MSE drop vs zero-shot: ORCA 6.29%, δ-Adapter 0.79%, ELF 0.47%, TAFAS −1.00%, DSOF −1.85%, SOLID −3.61% (Fig. 4).
- Learning from past errors alone hurts (−0.7%); conditioning on input and base prediction gives 6.5%; adding past errors to that lowers it to 6.1% (Fig. 5, §4.4).
- Without the router, ~80% of the gain remains (§4.5).
- Exchange-rate rows at H=30: 0.00% change for all five TSFMs (Table 4).
- ETS residual smoothing raises error (dataset-average score 126%); context-conditioned Ridge 69% (App. C.3).

## Limits and risks to validity
_Authors (§5):_ relies on a reasonable base forecast; abrupt structural shifts and probabilistic metrics untested.
_My assessment:_ no persistence/random-walk baseline; the only financial series shows no gain; no significance tests.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Streaming, labels delayed to t + H |
| Baselines | 1 | Zero-shot TSFMs, published adapters, Ridge/ETS; no naive forecast |
| Point-in-time and leakage controls | 2 | Explicit delayed-label buffer |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 1 | Eight datasets, one financial |
| Statistical testing | 0 | Three seeds, no tests |
| Reproducibility | 1 | Code released |
| **Total** | 7/12 → **8/14** | Moderate (non-finance) |

## Quotes worth keeping (each under 15 words, with page)
- "richer inputs do not monotonically improve performance" (§4.4, p. 8)
