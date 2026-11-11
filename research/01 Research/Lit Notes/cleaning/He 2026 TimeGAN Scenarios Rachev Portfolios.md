---
type: lit-note
title: "Rachev-Ratio Portfolio Optimization with TimeGAN Scenarios: Replacement versus Supplementation"
authors: [Yifan He]
year: 2026
venue: arXiv (preprint, Texas Tech University)
source_url: https://arxiv.org/abs/2610.24544
doi: 10.48550/arXiv.2610.24544
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ3.4]
family: [cleaning]
evidence: Moderate
score: 9
tags: [lit-note, family/cleaning, synthetic-data, tail-risk]
---
# Rachev-Ratio Portfolios with TimeGAN Scenarios (He, 2026)

**Basis:** arXiv 2610.24544 full text read via alphaXiv on 2026-11-08.

**Takeaway:** TimeGAN scenarios for 12 ETFs understate daily volatility by about 0.5 percentage points and 5% tail losses by about 1.5 points and get cross-asset correlations badly wrong (mean absolute error ≈ 0.57, some signs flipped); longer training improves reconstruction loss but not correlations, and no replacement or hybrid policy beats historical scenarios with intervals excluding zero.

## Problem
Are generated scenarios reliable inputs for a tail-sensitive portfolio criterion?

## Data and period
12 ETFs, daily split- and distribution-adjusted closes, April 2007 – December 2025; out-of-sample 3,955 returns from April 2010 (§3).

## Method
Rachev-ratio allocation on historical, TimeGAN-replacement and hybrid scenario sets; five seeds; delayed execution; 10 bp costs; comparison with IID and moving-block resampling controls.

## Baselines and validation
Historical scenarios and resampling controls; rolling decisions on 198 dates.

## Results (with page or section references)
- Generated scenarios: volatility −0.50 pp/day, 5% tail loss understated by ≈1.50 pp, correlation MAE ≈0.571 regardless of draw count (§5, Fig. 7).
- Longer training lowers reconstruction loss without improving correlation accuracy (abstract).
- All paired return, Sharpe and realised-tail-ratio intervals include zero; replacement raises turnover (§8.3).

## Limits and risks to validity
One generator design; 12 ETFs; flat costs.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Rolling decisions with delayed execution |
| Baselines | 1 | Historical and resampling controls |
| Point-in-time and leakage controls | 2 | Delayed execution; fixed protocol |
| Costs and realism | 1 | Flat 10 bp |
| Sample breadth | 1 | 12 ETFs, 2007–2025 incl. 2008 and 2020 |
| Statistical testing | 1 | Intervals; no multiple-testing correction |
| Reproducibility | 1 | Code and reproducibility file described |
| **Total** | 9/14 | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Generated scenarios understate volatility and tail losses and distort dependence." (abstract)
