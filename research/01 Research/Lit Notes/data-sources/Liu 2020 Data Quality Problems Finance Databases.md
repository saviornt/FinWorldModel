---
type: lit-note
title: 'Data Quality Problems Troubling Business and Financial Researchers: A Literature Review and Synthetic Analysis'
authors:
- Guoying Liu
year: 2020
venue: Journal of Business & Finance Librarianship
source_url: https://core.ac.uk/download/386127028.pdf
doi: 10.1080/08963568.2020.1847555
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.1
- RQ3.1
- RQ3.3
- RQ2.7
family:
- data-sources
evidence: Moderate
score: 7
tags:
- lit-note
- family/data-sources
---
# Data Quality Problems Troubling Business and Financial Researchers (Liu, 2020)

**Basis:** author's accepted manuscript via CORE (opened 2026-11-08); abstract and CRSP section (pp. 1, 6–9) read; recommendations section beyond the first 100,000 characters not read.

**Takeaway:** Even CRSP, the reference database, has documented errors (price-relative discrepancies near 3% in 1963–68; about 1 in 10,000 monthly returns later), biased daily equal-weighted index returns (about 6% a year) and missing delisting returns (about 13% of delistings still missing in 2017), so every vendor's prices and delistings need checking.

## Problem
Which data-quality problems affect the main finance databases.

## Data and period
Review of published studies on CRSP, Compustat, Capital IQ, I/B/E/S, Datastream, Worldscope, SDC and Orbis.

## Method
Literature review; problems sorted into 11 categories (missing values, errors, discrepancies, biases, inconsistencies, static header data, standardisation, changes in historic data, lack of transparency, reporting-time issues, misuse).

## Baselines and validation
Not applicable (review).

## Results (with page or section references)
- Rosenberg & Houglet (1974): ~3% (industrial) and ~2.4% (utility) price-relative discrepancies, 1963–68 (p. 6).
- Bennin (1980): CRSP error rate ~1/10,000 monthly returns vs 1/1,000 for Compustat (p. 6).
- Canina et al. (1998): daily equal-weighted index upward bias ≈0.43% a month (p. 8).
- Shumway (1997): thousands of missing delisting returns; Shumway & Warther (1999): poor-outcome delistings missed more often; Tobek & Hronec (2018): 2,742 of 20,680 (~13%) still missing as of 2017 (p. 8).
- Kahle & Walkling (1996): SIC codes disagree between CRSP and Compustat for ~36% of firms at two digits (p. 7).
- Francis et al.: prices adjusted with CRSP factors are wrong around property dividends, spin-offs and rights offerings (p. 9).

## Limits and risks to validity
Secondary review; figures are from cited studies (not rechecked), several decades old. Covers academic databases, not the retail APIs in RQ2.1. Read as manuscript, not the journal version.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Review |
| Baselines | N/A | Review |
| Point-in-time and leakage controls | 1 | Covers delisting, backfill and history-change biases |
| Costs and realism | N/A | Not a trading study |
| Sample breadth | 2 | Eight databases, decades of studies |
| Statistical testing | N/A | Review |
| Reproducibility | 0 | No data or code |
| **Total** | 3/6 → **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "Omitted delisting returns introduce a bias into studies that use the CRSP data." (Shumway, quoted p. 8)
