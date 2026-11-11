---
type: lit-note
title: 'DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion'
authors:
- Xuan Yao
- Shuping Li
- Yang Dai
- Yi Zhou
- Ke-Wei Huang
year: 2026
venue: arXiv
source_url: https://arxiv.org/abs/2608.22770
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ3.3
- RQ3.8
family:
- cleaning
evidence: Moderate
score: 9
tags:
- lit-note
- family/cleaning
- delisting
- corporate-actions
---
# DelistBench: Search-Enabled LLMs for Corporate-Event Database Completion (Yao et al., 2026)

**Basis:** arXiv 2608.22770v2 read in full via alphaXiv on 2026-11-08 (pp. 1–10).

**Takeaway:** Auditing vendor delisting records from public sources is feasible for *whether* a delisting happened (best web system 97% status accuracy on 1,200 records) but not yet for *when*: exact announcement dates were right for at most 46% of true delistings, and the main errors were confusing warning, decision, last-trading and effective dates and projecting later events back across the cutoff.

## Problem
How can an institution check its purchased corporate-event history (missing, stale or misdated delistings) independently?

## Data and period
1,200 security-level records from 59 countries (38% US/Canada), cutoff 2020-12-31 with 180-day buffers; strata: 400 delisted before cutoff, 400 delisted only after cutoff, 400 still listed (§3.2).

## Method
Five LLM systems, closed-book vs web-enabled, return status, announcement date, reason and evidence; risk-based triage to human review.

## Baselines and validation
Closed-book vs web per model; issuer-family-disjoint train/calibration/locked-test splits; human and model evidence audits.

## Results (with page or section references)
- Web raises date-within-7-days accuracy by 34–48 points; best overall joint accuracy 81.5% (abstract, Table 3).
- Exact-date accuracy on true delistings ≤46%; status accuracy minus exact-date accuracy is 51–56 points for every model (Table 3, §4.1).
- Error inventory: date mismatch 41%, missed announcement 20%, date + reason 19%, future projection 8% (Table 4).
- Defines the canonical date as the first qualifying public disclosure, not the effective or last-trading date (§3.1).

## Limits and risks to validity
Balanced benchmark (not real prevalence); history reconstructed from today's web, not a sealed archive; LLM-based, so the project's use would be audit, not data. Candidate events came from a licensed vendor.

## Rubric scores
| Check | Score | Note |
| --- | --- | --- |
| Out-of-sample design | 1 | Locked test split |
| Baselines | 1 | Closed-book vs web |
| Point-in-time and leakage controls | 2 | Cutoff-aware, future-event negatives |
| Costs and realism | N/A | |
| Sample breadth | 2 | 59 countries |
| Statistical testing | 0 | No tests |
| Reproducibility | 2 | Benchmark, prompts, outputs, code released |
| **Total** | 8/12 → **9/14** | Moderate |

## Quotes worth keeping (each under 15 words, with page)
- "the canonical date is the first qualifying public disclosure" (§3.1)
