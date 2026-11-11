---
type: lit-note
title: 'Firm-level production networks: what do we (really) know?'
authors:
- Andrea Bacilieri
- András Borsos
- Pablo Astudillo-Estevez
- François Lafond
year: 2023
venue: INET Oxford Working Paper 2023-08 (2025 revision; JEDC 2026)
source_url: https://oms-inet.files.svdcdn.com/staging/files/Firm-level-production-networks-what-do-we-really-know.pdf
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.8
- RQ3.7
family:
- data-sources
evidence: Moderate
score: 7
tags:
- lit-note
- family/data-sources
---
# Firm-level production networks: what do we (really) know? (Andrea Bacilieri et al., 2023)

**Takeaway:** Against complete administrative networks (Ecuador, Hungary), FactSet's supply-chain data misses most links (mean degree under 10 vs about 40) and biases degree, supplier-only shares and path lengths, though it covers firms producing 43% of US gross output; Compustat holds only about a thousand links a year because of the 10% customer rule.

## Problem
How good the available firm-level production-network data are.

## Data and period
Administrative VAT-based networks for Ecuador and Hungary (no reporting threshold) compared with FactSet and published national datasets (Belgium, Spain, Japan and others).

## Method
Network statistics (degree distributions, assortativity, reciprocity, clustering, path length) computed on each dataset; synthesis of published results.

## Baselines and validation
Complete administrative networks serve as the benchmark.

## Results (with page or section references)
- FactSet: firms with sales data cover 43% of US and 29% of world gross output (sec. 2, p. 6).
- Compustat: about a thousand firms and links per year; 10%-of-revenue customer rule "skews the type of relations observed" (sec. 2, pp. 5-6).
- Mean degree around 40 in complete data vs under 10 in incomplete data including FactSet (p. 2, sec. 3.1).
- FactSet: 41.5% supplier-only and 44.2% customer-only firms; reciprocity about 3% vs 5% (Tables 4; sec. 3.3.1).
- Weighted quantities much less affected than binary ones (Table 10, p. 22).

## Limits and risks to validity
Read the May 2023 working paper (journal version, JEDC 2026, cited by Fukada 2026, not opened). Administrative data are confidential, so results cannot be reproduced.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Descriptive data comparison |
| Baselines | 2 | Complete administrative networks as benchmark |
| Point-in-time and leakage controls | N/A | – |
| Costs and realism | N/A | – |
| Sample breadth | 2 | Several countries and datasets |
| Statistical testing | 0 | Not reported in parts read |
| Reproducibility | 0 | Confidential data |
| **Total** | **7/14** | 4 of 8 on applicable checks, scaled |

## Quotes worth keeping (each under 15 words, with page)
- "skews the type of relations observed" (sec. 2, p. 6)
