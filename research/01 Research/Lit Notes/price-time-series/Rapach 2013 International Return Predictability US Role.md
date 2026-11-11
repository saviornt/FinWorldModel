---
type: lit-note
title: "International Stock Return Predictability: What Is the Role of the United States?"
authors: [David E. Rapach, Jack K. Strauss, Guofu Zhou]
year: 2013
venue: Journal of Finance
source_url: https://rpc.cfainstitute.org/research/cfa-digest/2013/11/international-stock-return-predictability-what-is-the-role-of-the-united-states-digest-summary
doi: 10.1111/jofi.12041
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12, RQ1.15]
family: [price-time-series]
evidence: Moderate
score: 9
tags: [lit-note, family/price-time-series, information-diffusion, world-model]
---
# International Stock Return Predictability: What Is the Role of the United States? (Rapach, 2013)

**Basis:** the JF article is paywalled. Read: the JF abstract (EconPapers / SUFE index), the CFA Institute Digest summary (Nov 2013), and the exact replication in [[Siliverstovs 2015 US Role International Predictability Recessions]], which reproduces the paper's whole-sample out-of-sample results from the authors' posted data and code. Numbers below come from the replication unless marked.

**Takeaway:** Lagged monthly US market returns predict returns in most other industrialised markets out of sample (US Granger-causes 9 of 10), but not the reverse; a news-diffusion model attributes this to US shocks reaching other markets with a lag, i.e. an information friction.

## Problem
Are there lead-lag relationships among country stock returns, and does the US lead?

## Data and period
Monthly excess returns for the US and 10 other industrialised countries, 1980–2010 (replication data); returns adjusted for differences in closing times (abstract-level description).

## Method
Predictive regressions and pairwise Granger tests controlling for each country's own lag; multi-country specifications; an empirical news-diffusion model; out-of-sample forecasts with recursive windows against the historical mean, evaluated by R²OS and the Clark-West test (CFA Digest; replication).

## Baselines and validation
Historical-mean benchmark; own lagged return; out-of-sample recursive evaluation from 1985.

## Results (with page or section references)
- US returns Granger-cause returns in 9 of 10 non-US countries; lagged non-US returns have limited power for US returns (abstract; CFA Digest).
- News-diffusion model: US return shocks fully reflected abroad only with a lag (abstract).
- Out-of-sample R²OS of lagged US returns from −0.7% (Australia) to 3.8% (Netherlands); 9 of 10 significant at 10%; six above 1% (replication, Table 1, p. 8).

## Limits and risks to validity
_My assessment:_ monthly horizon only; gains concentrate in US recessions and are near zero in expansions ([[Siliverstovs 2015 US Role International Predictability Recessions]]); time-varying per later work (Aye, Balcilar & Gupta 2017, abstract only). No trading costs. Original text not opened.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 2 | Recursive expanding-window forecasts |
| Baselines | 1 | Historical mean, own lag; no strong ML |
| Point-in-time and leakage controls | 1 | Closing-time adjustment |
| Costs and realism | N/A | No trading claim |
| Sample breadth | 2 | 11 countries, 30 years incl. 2008 |
| Statistical testing | 1 | Clark-West; no multiple-testing correction |
| Reproducibility | 1 | Data and code posted by the authors |
| **Total** | **8/12 → 9/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (original not opened).
