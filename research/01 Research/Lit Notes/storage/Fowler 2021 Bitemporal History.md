---
type: lit-note
title: "Bitemporal History"
authors: [Martin Fowler]
year: 2021
venue: martinfowler.com
source_url: https://www.martinfowler.com/articles/bitemporal-history.html
doi: ""
accessed: 2026-11-08
papers: ["[[RP3 Cleaning and Labelling]]"]
research_questions: [RQ3.8]
family: [storage]
evidence: Primary documentation
tags: [lit-note, family/storage, bitemporal]
---
# Bitemporal History (Fowler, 2021)

**Basis:** article read via page fetch on 2026-11-08 (and search excerpt).

**Takeaway:** Keep two histories: actual history (what a value was, given perfect information), which may be corrected retroactively, and record history (what we believed when), which is append-only; bitemporality is needed when retroactive corrections matter to past decisions, and is costly enough to avoid when corrections can be forbidden or inputs stored with each decision.

## Problem / Method
Engineering pattern essay (payroll example).

## Results (with page or section references)
- Record history append-only; actual history mutable.
- Retroactive changes make earlier reports wrong; bitemporal records show what was believed when.
- Simpler alternatives: no retroactive changes, or store the inputs used with each action.

## Limits and risks to validity
Practitioner essay, not an empirical study. Formal definitions: [[Jensen 1995 TSQL2 Data Model]].

## Rubric scores
Primary documentation – not scored.

## Quotes worth keeping (each under 15 words, with page)
- None kept.
