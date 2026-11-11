---
type: lit-note
title: 'The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality'
authors:
- David H. Bailey
- Marcos López de Prado
year: 2014
venue: Journal of Portfolio Management 40(5), 94–107
source_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
doi: 10.3905/jpm.2014.40.5.094
accessed: '2026-11-08'
papers:
- '[[RP4 Training and Evaluation]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ4.1
- RQ4.2
family:
- evaluation
evidence: Weak
score: 5
tags:
- lit-note
- family/evaluation
- backtest-overfitting
- multiple-testing
---
# The Deflated Sharpe Ratio (Bailey & López de Prado, 2014)

**Basis:** SSRN abstract page (2460551) read through a summarising page fetch on 2026-11-08; full text not opened. The DOI recorded is the SSRN one; the journal DOI was not seen.

**Takeaway:** The deflated Sharpe ratio tests whether a backtest's Sharpe ratio is significant after allowing for the number of strategies tried and for non-normal returns, so a reported Sharpe ratio must come with the number of trials behind it.

## Problem
Selection bias under multiple testing and non-normal returns inflate reported Sharpe ratios.

## Data and period
Not read.

## Method
DSR: a probabilistic Sharpe ratio test with the benchmark set to the expected maximum Sharpe ratio across the trials run (abstract; details not read). Keywords include minimum track record length and minimum backtest length.

## Baselines and validation
Not read.

## Results (with page or section references)
- Corrects for the number of trials and for skewness and kurtosis of returns (abstract).
- No numbers read.

## Limits and risks to validity
_My assessment:_ only the abstract was read; widely used, but its effective-number-of-trials input is hard to know when searches are adaptive (Nikolopoulos 2026). Scored Weak because the full text was not opened, not because the method is weak.

## Rubric scores
Not scored item by item: only the abstract was read. Provisional **Weak (5/14)**: statistical testing 2 (multiple-testing correction is the subject), other checks not assessable.

## Quotes worth keeping (each under 15 words, with page)
- None kept (abstract only).

*DOI added 2026-11-09 from an OpenAlex lookup during the RP4 citation check (published version; the note was written from the version cited in `source_url`).*
