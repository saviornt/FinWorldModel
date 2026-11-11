---
type: lit-note
title: "Shared Analyst Coverage: Unifying Momentum Spillover Effects"
authors: [Usman Ali, David Hirshleifer]
year: 2020
venue: Journal of Financial Economics 136(3), 649–675
source_url: https://www.nber.org/system/files/working_papers/w25201/w25201.pdf
doi: 10.1016/j.jfineco.2019.10.007
accessed: 2026-11-07
papers: ["[[RP1 ML Methods]]", "[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ1.4, RQ3.7]
family: [graph]
evidence: Moderate
score: 7
tags: [lit-note, family/graph]
---
# Shared Analyst Coverage: Unifying Momentum Spillover Effects (Ali, 2020)

**Basis:** NBER WP 25201 (rev. Feb 2019) read through alphaXiv page excerpts: pp. 1–3, 5, 7, 9–13, 22, 24, 31–32 and Tables 1 and 5. The JFE version was not opened.

**Takeaway:** A simple neighbour-return feature over the shared-analyst-coverage graph (connected-stock momentum) earns a monthly alpha of 1.68% (t 9.67) and subsumes industry, geographic, customer, supply-chain-industry, segment and technology momentum; it holds in 10 of 11 developed markets.

## Problem
Are the many documented momentum spillovers one effect, and does analyst co-coverage measure firm relatedness better than other links?

## Data and period
All CRSP common stocks with price ≥ $5, 1984–2015; two firms are linked if one analyst issued an FY1/FY2 forecast for both in the past 12 months (IBES); about 86 connected stocks per firm, half overlapping earlier link types (pp. 10–11, Table 1). Customer links from Frazzini (lagged 6 months); BEA input–output lagged one year; patents lagged 6 months.

## Method
Connected-stock (CS) return = weighted average last-month return of analyst-linked firms; long–short sorts and five-factor alphas; spanning regressions; Fama–MacBeth with all other spillover variables; international replication; second-order links; analyst forecast revisions (pp. 5–12, 22–24).

## Baselines and validation
All earlier spillover measures as competitors; size, book-to-market, reversal and momentum controls. No train/test split; the international sample serves as an out-of-sample check (p. 5).

## Results (with page or section references)
- CS momentum factor alpha 1.68%/month (t 9.67); value- and equal-weighted five-factor alphas 1.19% and 2.10% (pp. 2, 31).
- Fama–MacBeth: CS return coefficient 0.18 (t 11.5); customer return 0.041 (t 4.0) falls to 0.022 with CS; supplier- and customer-industry returns become insignificant (Table 5, p. 42).
- Global ex-US: industry momentum alpha 0.92% falls to 0.20% after CS; CS keeps 0.78% (t 6.23) (p. 22).
- Analysts themselves update sluggishly: CS forecast revisions predict a firm's next revision (t 23.25) (p. 24). Effect stronger with more, and indirect, links (pp. 7, 24).
- Information ratio 1.71 after hedging factors (p. 32).

## Limits and risks to validity
_My assessment:_ monthly regressions without trading costs in the pages read; the sample ends in 2015, so post-publication decay is untested here; IBES is licensed.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Predictive regressions; international replication |
| Baselines | 1 | All competing spillover measures; no ML |
| Point-in-time and leakage controls | 2 | Trailing coverage; lagged link data |
| Costs and realism | 0 | Not in pages read |
| Sample breadth | 2 | US 1984–2015 plus 11 markets |
| Statistical testing | 1 | Large t-stats; no formal correction |
| Reproducibility | 0 | Licensed data, no code |
| **Total** | **7/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "there is really just a single momentum spillover effect" (p. 3)
