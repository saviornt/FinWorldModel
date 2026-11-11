---
type: lit-note
title: "Market Efficiency in Real Time"
authors: [Jeffrey A. Busse, T. Clifton Green]
year: 2002
venue: Journal of Financial Economics
source_url: https://academicnewsletter.sufe.edu.cn/info/357816
doi: 10.1016/S0304-405X(02)00148-4
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Weak
score: 5
tags: [lit-note, family/price-time-series, information-diffusion]
---
# Market Efficiency in Real Time (Busse, 2002)

**Basis:** abstract only. No open full text found (JFE paywalled). Read: the JFE abstract (SUFE academic index, which gives the DOI) and the SSRN preprint abstract (Scilit, doi:10.2139/ssrn.270958). Sample size from a secondary summary (Alpha Architect, 2011), not verified against the paper.

**Takeaway:** When CNBC's intraday Morning Call and Midday Call segments mention a stock, prices respond within seconds; positive reports are fully priced within one minute, negative reports adjust gradually over about 15 minutes, and only traders executing within 15 seconds make small profits.

## Problem
How fast do prices absorb widely broadcast, intraday information?

## Data and period
CNBC Morning Call and Midday Call stock reports broadcast during trading hours; 322 reports over 84 trading days, June–October 2000 (secondary summary).

## Method
Second-by-second event study of prices and signed trades around the first mention of a stock.

## Baselines and validation
Pre-mention prices; in-sample event study.

## Results (with page or section references)
- Prices respond within seconds; positive reports fully incorporated within one minute (JFE abstract; SSRN abstract).
- Negative reports: gradual impact lasting about 15 minutes (SSRN abstract).
- Trading intensity doubles in the first minute, with buyer- (seller-) initiated trades after positive (negative) reports (JFE abstract).
- Executing within 15 seconds of the mention earns small but significant profits on positive Midday Call reports (JFE abstract).

## Limits and risks to validity
_My assessment:_ four months in 2000; one broadcast source; mostly positive reports; costs and market impact of the 15-second strategy unclear from the abstract; pre-decimal market.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Event study |
| Baselines | 1 | Pre-mention prices |
| Point-in-time and leakage controls | 2 | Broadcast timed to the second |
| Costs and realism | 1 | Execution-delay profits; costs not verifiable |
| Sample breadth | 0 | 322 reports, four months |
| Statistical testing | 1 | Significance tests |
| Reproducibility | 0 | Hand-collected video data |
| **Total** | **5/14 → Weak** | |

## Quotes worth keeping (each under 15 words, with page)
- None recorded (abstract-only read).
