---
type: lit-note
title: "Event Study Testing with Cross-Sectional Correlation of Abnormal Returns"
authors: [James W. Kolari, Seppo Pynnönen]
year: 2010
venue: Review of Financial Studies 23(11), 3996–4025
source_url: https://papers.ssrn.com/abstract=1830364
doi: 10.1093/rfs/hhq072
accessed: 2026-11-08
papers: ["[[RP4 Training and Evaluation]]"]
research_questions: [RQ4.5]
family: [evaluation]
evidence: Weak
score: 5
tags: [lit-note, family/evaluation, event-study]
---
# Event Study Testing with Cross-Sectional Correlation (Kolari & Pynnönen, 2010)

**Basis:** Abstract only (SSRN abstract page and bibliographic records, opened 2026-11-08); journal full text is paywalled. Scored Weak for that reason and cited for direction only.

**Takeaway:** When events cluster on the same dates, even low cross-correlation among abnormal returns makes standard event-study tests over-reject the null of zero abnormal return; an adjusted Boehmer–Musumeci–Poulsen (BMP) t-statistic that accounts for cross-correlation performs well, and the portfolio approach is less powerful.

## Problem
Cross-sectional correlation of abnormal returns under event-date clustering (abstract).

## Data and period
Not in the part read (bibliographic subject tags list USA, 1990–2005).

## Method
Adjusts the BMP standardised t-statistic for average cross-correlation and event-induced variance; usable for multi-day CARs (abstract).

## Baselines and validation
Compared with other tests including the portfolio approach (abstract).

## Results (with page or section references)
- Event-date clustering plus "even relatively low cross-correlation" leads to serious over-rejection (abstract).
- The adjusted BMP statistic performs well; the portfolio approach is less powerful (abstract).
- A later paper citing it reports that a correlation of 0.05 can already bias tests towards over-rejection (Kolari–Pynnönen follow-up, J. Risk Financial Manag. 2022, p. 4; secondary source).

## Limits and risks to validity
_My assessment:_ abstract only; numbers not checked. Relevant because market-wide shocks hit all assets on the same date (complete clustering), the worst case for naive tests. Implemented in the R EventStudy package as `KolariPynnonenTest` (rdrr.io documentation, seen in search).

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | N/A | Test-statistic study |
| Baselines | 1 | Competing tests incl. portfolio approach |
| Point-in-time and leakage controls | N/A |  |
| Costs and realism | N/A |  |
| Sample breadth | 1 | Not verified (abstract only) |
| Statistical testing | 2 | Size and power comparisons |
| Reproducibility | 0 | Not known |
| **Total** | 4/8 → 7/14 → **Weak (abstract only)** | Recorded as 5 to match the abstract-only convention |

## Quotes worth keeping (each under 15 words, with page)
- "even relatively low cross-correlation among abnormal returns is serious" (abstract)
