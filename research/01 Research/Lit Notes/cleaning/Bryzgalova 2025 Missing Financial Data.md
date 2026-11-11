---
type: lit-note
title: "Missing Financial Data"
authors: [Svetlana Bryzgalova, Sven Lerner, Martin Lettau, Markus Pelger]
year: 2025
venue: Review of Financial Studies 38(3), 803–882
source_url: https://conference.nber.org/conf_papers/f175917.pdf
doi: 10.1093/rfs/hhae036
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.4, RQ3.1]
family: [cleaning]
evidence: Moderate
score: 9
tags: [lit-note, family/cleaning, imputation]
---
# Missing Financial Data (Bryzgalova, 2025)

**Basis:** NBER conference draft of 7 January 2023 read via alphaXiv PDF query on 2026-11-08; the RFS 2025 version was not opened (paywalled).

**Takeaway:** Firm fundamentals are not missing at random (more than 70% of firms, about half of market cap, miss at least one of 45 characteristics); a cross-sectional factor model plus each firm's own past (local B-XS) imputes with about half the error of the cross-sectional median and without look-ahead, while using future values (BF-XS) is only slightly more accurate and leaks.

## Problem
How widespread and how structured is missing firm-characteristic data, and how should it be imputed for asset pricing without look-ahead?

## Data and period
CRSP/Compustat, January 1967 – December 2020 (648 months), 22,630 stocks, 45 characteristics as centred ranks in [−0.5, 0.5] (p. 8).

## Method
Six-factor cross-sectional model of characteristics combined with time-series information: backward (B-XS: previous value + factors), backward-forward (BF-XS: also next value), local (one month) or global (full panel) estimation; compared with previous value, AR(1), cross-sectional and industry median (Table 3, §3.2).

## Baselines and validation
Out-of-sample masking of 10% of fully observed entries: missing at random, 12-month blocks, and a logit model of real missingness (Table 4).

## Results (with page or section references)
- Facts: 1967–1981 over 25% of observations missing, 1990–2020 about 10%; a fully observed panel of 45 characteristics omits over 70% of firms (pp. 2–3). Small firms and extreme characteristic values are more often missing (p. 4).
- Block-missing RMSE: XS-median 0.29, previous value 0.17, local B-XS 0.14, global BF-XS 0.10 (Table 4, p. 34). Logit masking R²: local B-XS 0.87, global BF-XS 0.93 (p. 35).
- §3.4.1: the most-information model without look-ahead is local B-XS; BF-XS "peeks" into the future; random masking for training would bias imputations because data are not MAR (p. 24).
- Stale values between quarterly updates are themselves imputation and create "mechanical trivial predictability" (p. 9, fn. 4).
- Selection: mean returns differ between stocks with and without a characteristic by up to 8.1% a year (sales-to-price) (p. 43); requiring all characteristics lowers Sharpe ratios of decile sorts (e.g. 25% lower for one OL decile, p. 50); imputed full-universe sorts match single-characteristic sorts (p. 48).

## Limits and risks to validity
Imputation accuracy is evaluated by masking, not by a downstream forecast; portfolio results are univariate sorts without costs.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Masked hold-out, not walk-forward |
| Baselines | 1 | Median, previous value, AR(1) |
| Point-in-time and leakage controls | 2 | Look-ahead-free vs future-using models compared explicitly; 6-month lag in pricing tests |
| Costs and realism | N/A | Imputation study |
| Sample breadth | 2 | Full US cross-section 1967–2020 |
| Statistical testing | 1 | Some tests; no multiple-testing correction |
| Reproducibility | 1 | Standard data; code not checked |
| **Total** | 8/12 → 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "firm fundamentals are not missing-at-random" (abstract, p. 1)
