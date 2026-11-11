---
type: lit-note
title: "Rent Seeking by Low-Latency Traders: Evidence from Trading on Macroeconomic Announcements"
authors: [Tarun Chordia, T. Clifton Green, Badrinath Kottimukkalur]
year: 2018
venue: Review of Financial Studies
source_url: https://www.unsw.edu.au/content/dam/pdfs/business/banking-finance/events/news-events/2021-10-busines-banking-finance-news-events-Low-Latency-Trading-on-Macroeconomic-Announcements.pdf
doi: 10.1093/rfs/hhy025
accessed: 2026-11-08
papers: ["[[RP1 ML Methods]]", "[[RP5 Vault Review]]"]
research_questions: [RQ1.12]
family: [price-time-series]
evidence: Moderate
score: 6
tags: [lit-note, family/price-time-series, information-diffusion]
---
# Rent Seeking by Low-Latency Traders (Chordia, 2018)

**Basis:** January 2016 working-paper version ("Low Latency Trading on Macroeconomic Announcements"), read through a page-fetch summary. Published as RFS 31(12), 4650–4687 (DOI from EconPapers). The published abstract reports a response "within five milliseconds"; the 2016 draft says within the first 100 ms. Use the journal numbers once checked.

**Takeaway:** SPY and E-mini prices respond to macro-announcement surprises within a tenth of a second and most of the move is done in 2 seconds; profits from trading fast are small (≈$19k per event SPY, ≈$50k ES, before data fees) and fell to almost nothing by 2014 as competition grew; paying for a 2-second head start did not raise profits.

## Problem
Do low-latency traders earn large rents from public macro news, and how fast is the information priced?

## Data and period
Millisecond Tick Data quotes and trades for SPY (2008–2014) and E-mini S&P 500 futures (July 2011–2014); 18 of 27 macro announcements with significant price impact (pp. 7, 9).

## Method
Event-time price response and trading intensity around release time; profits of a simple strategy trading in the surprise direction within 2 seconds and exiting after 1–5 minutes; trend in profits; difference-in-differences around Reuters ending early access to Consumer Sentiment (July 2013); state-space estimate of order-flow informativeness (pp. 11–29).

## Baselines and validation
Pre-release windows; non-treated announcements in the diff-in-diff. Event study, in-sample.

## Results (with page or section references)
- Response within the first 100 ms (2016 draft; journal: 5 ms); 2-second response = 78% (SPY) / 84% (ES) of the 10-second response (pp. 11–12).
- Trading intensity rises ten- to twenty-fold in the first quarter-second (pp. 4, 13; the two figures are not fully consistent).
- Profit per event ≈$19k SPY, ≈$50k ES (≈2 bp on ≈$80M notional); SPY profit fell from $38k (2011) to ≈0 (2014) (pp. 4–5).
- No significant change in profits after early access ended (p. 26). Order-flow price impact fell from 0.67 (2011) to ≈0 (2014): prices move on the news itself, not through trading (p. 29).

## Limits and risks to validity
_My assessment:_ two very liquid instruments; profits exclude commissions and data subscriptions (≈$10k/month quoted, p. 17); strategy not optimised; assumes exact release times.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 0 | Event study |
| Baselines | 1 | Pre-release windows, diff-in-diff control |
| Point-in-time and leakage controls | 2 | Millisecond timestamps vs release times |
| Costs and realism | 1 | Spreads in profit calc; no commissions or data fees |
| Sample breadth | 1 | Two instruments, 2008–2014 |
| Statistical testing | 1 | t-stats, clustered errors |
| Reproducibility | 0 | Licensed tick data |
| **Total** | **6/14 → Moderate** | |

## Quotes worth keeping (each under 15 words, with page)
- "does not account for commissions" (p. 4)
