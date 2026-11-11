---
type: lit-note
title: MarineCadastre AIS vessel traffic data
authors:
- NOAA Office for Coastal Management; BOEM
year: 2026
venue: Official documentation
source_url: https://marinecadastre.gov/ais
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
research_questions:
- RQ2.9
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# MarineCadastre AIS vessel traffic data (NOAA Office for Coastal Management; BOEM, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** US Coast Guard AIS vessel positions for US coastal waters are free from MarineCadastre (bulk files from 2009, daily point files and monthly tracks, GeoParquet for 2024–2025) under CC0, released with a delay of months; coverage stops at US waters.

## Problem
A free shipping-traffic source and its limits.

## Data and period
Not applicable.

## Method
MarineCadastre AIS page and the ocm-marinecadastre GitHub repository (last updated 2025-07-30).

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Collected by the US Coast Guard's national AIS receiver network; location, time, type, speed, size, draft.
- AIS page lists US coastal data for 2009–2023; GitHub adds 2024 daily points and 2024–2025 monthly tracks (GeoParquet, experimental).
- Licence: "CC0 1.0 Universal public domain dedication" (GitHub).

## Limits and risks to validity
US waters only; release lag of months (a 2023 US Army Corps technical note, seen as a search snippet, said several months; not opened). Global or real-time AIS needs commercial providers (Spire, Kpler, MarineTraffic) whose terms were not read.

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "All content is licensed under the CC0 1.0 Universal public domain dedication." (GitHub)
