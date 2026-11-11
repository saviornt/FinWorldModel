---
type: lit-note
title: "Taming Tail Risk in Financial Markets: Conformal Calibration for Nonstationary Portfolio VaR"
authors: [Marc Schmitt]
year: 2026
venue: arXiv (q-fin.RM), v3
source_url: https://arxiv.org/abs/2602.03903
doi: ""
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.6, RQ4.3]
family: [tail-risk]
evidence: Strong
score: 13
tags: [lit-note, family/tail-risk]
---
# Taming Tail Risk in Financial Markets: Conformal Calibration for Nonstationary Portfolio VaR (Schmitt, 2026)

**Basis:** full text of arXiv v3 (3 Aug 2026), pp. 1–7, via the alphaXiv PDF reader.

**Takeaway:** Every uncalibrated base VaR model (historical simulation, GARCH-t, LightGBM quantile regression) over-exceeds its 1% target on the CRSP index in 2018–2024; conformal wrappers restore average coverage, but feedback methods (ACI, DtACI, PID) concentrate their misses in the stress quintile, while recency- and regime-weighted calibration keeps stress exceedances near target at a capital cost; no buffer rescues a base model that cannot adapt.

## Problem
Which calibration layer keeps one-sided VaR exceedance rates near target within calm and stress regimes separately, not just on average, and at what capital cost (p. 1)?

## Data and period
CRSP value-weighted index (WRDS) and 16 CRSP-derived Ken French portfolios (10 industries, 6 size/BM), daily, 1990-03-30 to 2024-12-31 (8,755 days). Train to 2011-01-31, validation 2011-02-01 to 2018-01-16, test 2018-01-17 to 2024-12-31 (N = 1,751, covering the 2018 spike, COVID crash, 2022 tightening) (pp. 3–4).

## Method
Regime-weighted conformal calibration (RWC): additive buffer = weighted conformal quantile of past one-sided scores, with weights = exponential time decay × Gaussian kernel on regime features (21-day realised volatility, 5-day mean absolute return, all through t−1); TWC is the kernel-free special case; effective-sample-size safeguard (pp. 2–3). Coverage-gap bound for arbitrary heuristic weights (Theorem 1, p. 3).

## Baselines and validation
Base forecasters: 500-day HS, GARCH(1,1)-t refit every 21 days, LightGBM quantile regression refit every 21 days. Calibrators: sliding window, ACI, DtACI, conformal PID, TWC, RWC. Hyperparameters tuned on validation, frozen for the 16 portfolios. Metrics: exceedance with 63-day block-bootstrap CIs, average VaR (capital), exceedance by volatility quintile, Kupiec, Christoffersen, Engle–Manganelli DQ (p. 4).

## Results (with page or section references)
- Uncalibrated 99% VaR exceedances: GBDT 4.05%, GARCH-t 1.94%, HS 1.83% vs 1% target, all rejected by Kupiec and DQ (p. 4, Table 1).
- All conformal wrappers bring exceedance near target; DtACI overshoots at 99% (1.54–1.88%) (p. 4).
- Stress quintile (Q5), HS base, 99%: ACI 2.29%, DtACI 2.00%, PID 1.71%, TWC 1.14%, RWC 0.86% (p. 4, Table 2). Feedback methods "widen only after a run of violations" (p. 5).
- GARCH-t base: all methods keep Q5 at or below target (0.29–0.57%); regime weighting unnecessary (p. 5).
- No calibrator rescues the HS base from DQ rejection: violations cluster because the base cannot adapt within regimes (pp. 4–5).
- 16 portfolios, HS base: mean Q5 exceedance RWC 0.82% vs ACI 1.64%, SWC 2.36%, at higher capital (627 vs 554 bps for TWC); GARCH-t base passes DQ on 13–14 of 16 portfolios with SWC/TWC/RWC/ACI (p. 5, Table 3).
- Single-index bootstrap CIs are wide ([0.17, 0.80]% for RWC vs [0.69, 1.37]% for ACI, GARCH-t base) (p. 4).

## Limits and risks to validity
_My assessment:_ one-day horizon, liquid US equity portfolios only; regime features are price-based, so an exogenous news shock is still seen only after the first large move. Coverage guarantees rely on smoothness and conditional-independence assumptions (p. 6). Strong design: chronological split, frozen hyperparameters, cross-sectional replication, regime-stratified metrics.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Chronological train/validation/test with rolling refits |
| Baselines | 2 | HS, GARCH-t, GBDT plus four conformal methods |
| Point-in-time and leakage controls | 2 | All features through t−1; tuning on validation only |
| Costs and realism | N/A | Risk calibration, not trading |
| Sample breadth | 2 | Index + 16 portfolios; test includes COVID and 2022 |
| Statistical testing | 1 | Kupiec, Christoffersen, DQ, bootstrap CIs; no multiple-testing correction |
| Reproducibility | 1 | Portfolio data public; CRSP proprietary; code not stated |
| **Total** | **11/12 → 13/14** | Strong |

## Quotes worth keeping (each under 15 words, with page)
- "A conformal layer complements a conditional risk model; it does not substitute for one." (p. 5)
