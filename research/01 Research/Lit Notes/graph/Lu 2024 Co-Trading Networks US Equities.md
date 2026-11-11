---
type: lit-note
title: "Co-trading networks for modeling dynamic interdependency structures and estimating high-dimensional covariances in US equity markets"
authors: [Yutong Lu, Gesine Reinert, Mihai Cucuringu]
year: 2024
venue: arXiv (q-fin.TR)
source_url: https://arxiv.org/abs/2302.09382
doi: 10.48550/arXiv.2302.09382
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.7]
family: [graph]
evidence: Weak
score: 5
tags: [lit-note, family/graph, time-valid-graph, co-movement]
---
# Co-trading Networks in US Equities (Lu, 2024)

**Basis:** arXiv 2302.09382v2 pages 1–7, 14, 24–25, 31 read via alphaXiv on 2026-11-08.

**Takeaway:** Daily networks built from how often two stocks trade within 500 microseconds of each other drift away from GICS sectors over 2017–2019 and show three regimes; they relate positively to realised covariance on 98.5% of days even after sector controls, and using daily co-trading clusters instead of fixed GICS blocks in a factor covariance estimator raised a mean-variance portfolio's Sharpe from 0.97 to 1.40 (no costs).

## Problem
Can trade timing build a dynamic stock network that tracks co-movement better than static sectors?

## Data and period
457 S&P 500 stocks, LOBSTER Nasdaq order books, 2017-01-03 to 2019-12-09 (p. 7).

## Method
Pairwise co-trading score = normalised count of trades within δ = 500 µs; daily matrices; spectral clustering; network regression on realised covariance; block-diagonal idiosyncratic covariance with daily clusters (pp. 5–7).

## Baselines and validation
GICS sector blocks; sample covariance; market portfolio.

## Results (with page or section references)
- Daily cluster–GICS agreement trends down 2017–2019; three regimes found (pp. 14).
- Positive, significant co-trading–covariance relation on 98.51% of days (p. 2).
- GMV Sharpe 1.40 with 20 co-trading clusters vs 0.97 GICS (10 factors) (Table 8, p. 31).
- Count-based networks more stable than volume-based (p. 24).

## Limits and risks to validity
Three calm years; fixed universe of survivors over the period (p. 25 notes this); no costs; commercial data; no code.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Rolling portfolio evaluation |
| Baselines | 1 | GICS blocks |
| Point-in-time and leakage controls | 1 | Daily networks; fixed survivor universe |
| Costs and realism | 0 | No costs |
| Sample breadth | 1 | 457 stocks, no stress period |
| Statistical testing | 1 | Daily regression tests |
| Reproducibility | 0 | Commercial data, no code |
| **Total** | 5/14 | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None kept.
