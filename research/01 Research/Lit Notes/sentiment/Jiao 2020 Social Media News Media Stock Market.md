---
type: lit-note
title: "Social media, news media and the stock market"
authors: [Peiran Jiao, André Veiga, Ansgar Walther]
year: 2020
venue: Journal of Economic Behavior & Organization 176, 63–90
source_url: https://core.ac.uk/download/288394514.pdf
doi: 10.1016/j.jebo.2020.03.002
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.3, RQ1.12]
family: [sentiment]
evidence: Weak
score: 5
tags: [lit-note, family/sentiment]
---
# Social Media, News Media and the Stock Market (Jiao, 2020)

**Basis:** author version dated 21 Feb 2020 (CORE PDF), read through page fetch.

**Takeaway:** Heavy news coverage of a stock is followed by lower idiosyncratic volatility and turnover next month; heavy social-media coverage by higher volatility and turnover, consistent with social networks echoing stale news.

## Problem
Do news and social media coverage affect later volatility and trading in the same way?

## Data and period
Thomson Reuters MarketPsych Indices (news and social buzz and sentiment), balanced panel of 1,848 NYSE/AMEX/NASDAQ stocks, monthly, Jan 2009–Dec 2014 (Sec. 2, p. 7).

## Method
Next-month idiosyncratic volatility (FF3 residuals) and turnover regressed on this month's relative news and social buzz, with stock and month fixed effects and controls including sentiment; panel VAR (pp. 9–11, Tables 6–7, 15–16).

## Baselines and validation
Lagged dependent variable and firm controls; robustness to unbalanced panel, other volatility measures, dropping industries or size quartiles; market-level GJR-GARCH. All in-sample.

## Results (with page or section references)
- Volatility: news buzz −0.052, social buzz +0.037 (both 1%) (Table 6, p. 32).
- Turnover: news −0.065, social +0.042 (Table 7, p. 33).
- Going from 0 to 0.5% buzz: social raises volatility ~54% and turnover ~30%; news lowers them ~68% and ~47% (pp. 10–11).
- News buzz Granger-causes social buzz, not clearly the reverse (p = 0.054) (Tables 15–16).
- Does not test whether sentiment predicts returns.

## Limits and risks to validity
_Authors:_ associations, not causal. _My assessment:_ in-sample, one bull-market regime, vendor indices; relevant for volatility and turnover targets, not returns.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | In-sample panel (predictive timing only) |
| Baselines | 1 | Lagged DV and controls |
| Point-in-time and leakage controls | 1 | Next-month timing; vendor indices |
| Costs and realism | N/A | No trading |
| Sample breadth | 1 | 1,848 stocks, 2009–2014 |
| Statistical testing | 1 | Clustered SEs |
| Reproducibility | 0 | Proprietary data |
| **Total** | **4/12 → 5/14** | Weak |

## Quotes worth keeping (each under 15 words, with page)
- None recorded.
