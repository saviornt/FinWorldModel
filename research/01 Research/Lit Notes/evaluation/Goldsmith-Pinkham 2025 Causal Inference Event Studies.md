---
type: lit-note
title: "Causal Inference in Financial Event Studies"
authors: [Paul Goldsmith-Pinkham, Tianshu Lyu]
year: 2025
venue: arXiv (econ.EM) 2511.15123
source_url: https://arxiv.org/abs/2511.15123
doi: ""
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.5]
family: [evaluation]
evidence: Strong
score: 11
tags: [lit-note, family/evaluation, event-study]
---
# Causal Inference in Financial Event Studies (Goldsmith-Pinkham & Lyu, 2025)

**Basis:** Full text (pp. 1–5, 12, 18, 25, 29, 32–37, 41, 43–44) via the alphaXiv PDF reader, read 2026-11-08.

**Takeaway:** Factor-model abnormal returns are inconsistent for causal effects when the factor model is misspecified; the bias is small for short windows with randomly timed events but large in volatile periods, over long horizons and when event timing correlates with market conditions — synthetic-control counterfactuals remove much of it.

## Problem
Whether the standard market/factor-model event study identifies causal effects of information events (§1).

## Data and period
Four applications: Geithner nomination (Nov 2008, financial firms, Datastream); S&P 500 inclusions 1976–2020 (CRSP); long-run acquirer returns; close merger contests with losing bidders as controls (§4).

## Method
Potential-outcomes framework; asymptotic bias expressions for abnormal-return, difference-in-means and synthetic-control/gsynth estimators; simulations; empirical comparisons (§2–4).

## Baselines and validation
Market-adjusted, CAPM, Fama–French 3-factor, synthetic control, gsynth, and a quasi-experimental benchmark (contest losers) (§4.4).

## Results (with page or section references)
- Short-horizon, randomly timed events (S&P inclusions): announcement-day effects agree across estimators within about 0.2 percentage points per decade (Table 5, p. 33).
- Geithner window had daily market moves above 6%; a 0.60 beta gap between treated and control banks implies about 4.1% bias on the event day alone; effects disappear under synthetic methods (p. 28).
- Pre-inclusion drift largely disappears once unobserved factor exposure is matched (gsynth, propensity matching) (pp. 33–36).
- Long-horizon merger results are highly sensitive to model choice; most model-based estimates disagree with the contest-loser benchmark (pp. 40–43).
- Buy-and-hold abnormal returns against a lower-variance index are biased by volatility drag even with no effect (p. 3).

## Limits and risks to validity
_My assessment:_ assumes a time-invariant latent factor model for the treated cohort (p. 2). Directly relevant to shock studies: shocks happen in volatile periods and are not randomly timed, which is exactly where standard abnormal returns fail; use short windows, matched or synthetic counterfactuals, and quasi-experimental controls where possible.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Separate training and post-event windows for counterfactuals |
| Baselines | 2 | Several estimators plus a design-based benchmark |
| Point-in-time and leakage controls | 1 | Estimation windows exclude the pre-announcement period |
| Costs and realism | N/A |  |
| Sample breadth | 2 | Four settings, 1976–2020, incl. 2008 crisis |
| Statistical testing | 2 | Theory, simulations, inference |
| Reproducibility | 1 | Replication data from original authors; own code not stated |
| **Total** | 9/12 → **11/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "misspecification bias compounds over longer horizons" (p. 42)
