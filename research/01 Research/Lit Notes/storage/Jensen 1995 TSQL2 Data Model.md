---
type: lit-note
title: The TSQL2 Data Model
authors:
- Christian S. Jensen
- Richard T. Snodgrass
- Michael D. Soo
year: 1995
venue: In R. T. Snodgrass (ed.), The TSQL2 Temporal Query Language, Kluwer
source_url: https://homes.cs.aau.dk/~csj/Thesis/pdf/chapter12.pdf
doi: 10.1007/978-1-4615-2289-8_10
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
- '[[RP5 Vault Review]]'
research_questions:
- RQ2.5
- RQ3.8
family:
- storage
evidence: Primary documentation
tags:
- lit-note
- family/storage
- primary-documentation
---
# The TSQL2 Data Model (Christian S. Jensen, 1995)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** Standard reference defining valid time (when a fact is true in reality) and transaction time (when the database stored it) as orthogonal dimensions, combined in the bitemporal conceptual data model.

## Problem
Agreeing definitions for temporal databases after some two dozen incompatible proposals.

## Data and period
Not applicable.

## Method
Survey and comparison of 23 temporal data models; definition of the bitemporal conceptual data model (BCDM), where each tuple carries a set of bitemporal chronons in valid-time x transaction-time space.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Valid time can be past or future; transaction time is bounded by database creation and now.
- The two dimensions vary independently; they coincide only in 'degenerate' databases where facts are recorded the moment they become true.

## Limits and risks to validity
Conceptual, not empirical; treated as a standard reference and marked Primary documentation (see RP2 Assumptions). Book venue inferred from the chapter's page range (pp. 361-395).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Valid time concerns the time when a fact is true in reality."
