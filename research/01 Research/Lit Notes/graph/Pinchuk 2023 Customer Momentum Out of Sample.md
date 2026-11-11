---
type: lit-note
title: "Customer Momentum"
authors: [Mykola Pinchuk]
year: 2023
venue: arXiv (q-fin.PR)
source_url: https://arxiv.org/abs/2301.11394
doi: 10.48550/arXiv.2301.11394
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.4]
family: [graph]
evidence: Moderate
score: 7
tags: [lit-note, family/graph]
---
# Customer Momentum (Pinchuk, 2023)

**Basis:** pp. 1–4, 6–7, 11–12, 16–17, 21 and Tables 1, 2, 8, 9, 32, 39 read through alphaXiv page excerpts. Paper dated December 2018, posted 2023.

**Takeaway:** Customer momentum replicates for 1978–2004 (equal-weighted long–short 1.52%/month) but roughly halves after publication (0.62% EW, 0.62% VW insignificant, 2005–2018), and much of it looks like a large-customer-to-small-supplier lead–lag.

## Problem
Does Cohen–Frazzini customer momentum survive out of sample, and is it distinct from price momentum, earnings momentum and size lead–lag?

## Data and period
CRSP/Compustat with Compustat segment customer links, 1978–2018; 145,489 firm-months, 3,266 firms; 6-month lag on links; coverage 1–16% of market cap (pp. 6–7, Table 1).

## Method
Monthly decile sorts on past customer returns at several lags; factor alphas; Fama–MacBeth with SUE and price momentum; splits by relative customer/supplier size; attention via supplier volume on customer earnings days (pp. 11–17).

## Baselines and validation
Factor models (CAPM to FF5 + UMD), price and earnings momentum. The 2005–2018 period is a genuine post-discovery holdout (p. 11).

## Results (with page or section references)
- Full sample 1-1 lag: EW long–short 1.22% (t 5.17), VW 1.06% (t 3.34) (Table 2).
- 1978–2004 EW 1.52% (t 4.74), VW 1.30%; 2005–2018 EW 0.62% (t 2.12), VW 0.62% (t 1.54); 2005–2018 FF5 alpha 0.59% (t 1.91); the CMOM factor return is negative after 2005 (Tables 8–9, pp. 4, 11).
- Lags beyond one month are absorbed by price and earnings momentum (p. 3).
- Long–short returns rise from about 0.2% to 1.3% across quintiles of customer-to-supplier size; an interaction term flips the customer-return coefficient's sign (pp. 16–17).
- Attention evidence is mixed: stronger for low-attention links only in equal-weighted portfolios (p. 4).

## Limits and risks to validity
Author states small sample from poor link data (p. 4). _My assessment:_ no costs; the post-2004 test has low power.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Post-publication holdout |
| Baselines | 1 | Factor and momentum controls |
| Point-in-time and leakage controls | 2 | 6-month link lag |
| Costs and realism | 0 | Not addressed |
| Sample breadth | 2 | 1978–2018 incl. 2008 |
| Statistical testing | 1 | Newey–West t-stats |
| Reproducibility | 0 | Licensed data |
| **Total** | **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "customer momentum has a smaller magnitude and loses statistical significance" (p. 1)
