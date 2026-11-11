---
type: lit-note
title: USGS real-time earthquake GeoJSON feeds and copyright policy
authors:
- U.S. Geological Survey
year: 2026
venue: Official documentation
source_url: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
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
# USGS real-time earthquake GeoJSON feeds and copyright policy (U.S. Geological Survey, 2026)

**Basis:** official documentation opened 2026-11-08.

**Takeaway:** USGS publishes earthquake feeds (past hour to past 30 days, by magnitude) updated every minute, each event carrying `time` and `updated` fields under a feed life-cycle policy; USGS-authored data are US public domain (credit requested).

## Problem
A free, fast natural-hazard event source.

## Data and period
Not applicable.

## Method
GeoJSON feed summary page and the USGS Copyrights and Credits page.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Feeds updated every minute; windows past hour, day, 7 days, 30 days; significant, M4.5+, M2.5+, M1.0+, all.
- Each event has `time` and `updated` (revisions tracked; life-cycle policy not read).
- USGS-authored data are "U.S. Public Domain"; credit line requested.

## Limits and risks to validity
Real-time feeds hold only the last 30 days; the historical catalogue and revision history were not read. `updated` shows revisions happen, so an archive must keep each version to stay point-in-time (project reading).

## Rubric scores
Primary documentation: not scored, per the guide's rubric. Facts are what the vendor or project states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Updated every minute." (feed page)
