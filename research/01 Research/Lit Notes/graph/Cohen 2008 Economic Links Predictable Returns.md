---
type: lit-note
title: "Economic Links and Predictable Returns"
authors: [Lauren Cohen, Andrea Frazzini]
year: 2008
venue: Journal of Finance 63(4), 1977–2011
source_url: https://tevgeniou.github.io/EquityRiskFactors/bibliography/SuppyChainReturns.pdf
doi: 10.1111/j.1540-6261.2008.01379.x
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP2 Data Sources and Storage]]", "[[RP3 Cleaning and Labelling]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.4, RQ1.12, RQ2.8, RQ3.7]
family: [graph]
evidence: Moderate
score: 8
tags: [lit-note, family/graph]
---
# Economic Links and Predictable Returns (Cohen, 2008)

**Basis:** published JF PDF (hosted copy), pp. 1977–1981, 1983–1986, 1989, 1996–1997 and 2009 read through alphaXiv page excerpts. DOI not shown in the pages read; left empty (add from the journal page).

**Takeaway:** Supplier stocks under-react to news about their major customers: buying suppliers whose customers rose most last month and shorting those whose customers fell most earns about 1.55% a month (1980–2004), not explained by own, industry or cross-industry momentum.

## Problem
Do prices of linked firms adjust with a lag to news about their customers, as limited investor attention predicts?

## Data and period
Compustat segment files: customers above 10% of sales (SFAS 14/131), hand-matched to CRSP; 30,622 firm-year links, 11,484 unique pairs, 1980–2004; average customer takes 20% of supplier sales; 78% of links cross industries (pp. 1983–1984, Table I).

## Method
Monthly quintile sorts of suppliers on last month's customer-portfolio return; calendar-time alphas; Fama–MacBeth regressions hedging own reversal and momentum, industry momentum, cross-industry momentum and intra-industry lead–lag (pp. 1985–1986, 1996–1997).

## Baselines and validation
Factor models and the competing momentum effects above. Links are lagged 6 months after fiscal year-end so they are public before use (p. 1983). Predictive, not a trained model.

## Results (with page or section references)
- Long–short customer momentum: 1.55% a month (18.6% a year) value-weighted; equal-weighted alpha 1.3% (t 4.93) (pp. 1980, 1989).
- After hedging all controls in Fama–MacBeth, about 88 bp a month (p. 1997).
- Returns mostly come from slow diffusion of bad news (p. 1989); drift converges faster in large caps, lasts over a year in small caps (p. 1996).
- Predictability is stronger where few mutual funds hold both customer and supplier (p. 1980).

## Limits and risks to validity
_My assessment:_ the main sort uses only the customer's own past return, a simple neighbour feature; costs are not addressed in the pages read; customers are much larger than suppliers, so part of the effect may be a large-to-small lead–lag (see [[Pinchuk 2023 Customer Momentum Out of Sample]]). Post-2004 decay is reported elsewhere.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Predictive sorts, no holdout |
| Baselines | 1 | Factor and momentum controls |
| Point-in-time and leakage controls | 2 | 6-month lag on links |
| Costs and realism | 0 | Not in pages read |
| Sample breadth | 2 | All linked CRSP firms, 1980–2004 |
| Statistical testing | 1 | t-stats, no correction |
| Reproducibility | 1 | Link data posted by Frazzini (per [[Ali 2020 Shared Analyst Coverage Momentum Spillover]]) |
| **Total** | **8/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "stock prices do not incorporate news involving related firms" (p. 1977)

**Citation check (2026-11-08):** DOI 10.1111/j.1540-6261.2008.01379.x confirmed through OpenAlex by the reference-lookup tool.
