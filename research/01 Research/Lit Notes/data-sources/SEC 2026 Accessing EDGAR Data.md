---
type: lit-note
title: 'SEC: Accessing EDGAR Data'
authors:
- U.S. Securities and Exchange Commission
year: 2026
venue: Official documentation
source_url: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data
doi: ''
accessed: '2026-11-08'
papers:
- '[[RP2 Data Sources and Storage]]'
- '[[RP3 Cleaning and Labelling]]'
research_questions:
- RQ2.2
- RQ2.6
- RQ3.2
family:
- data-sources
evidence: Primary documentation
tags:
- lit-note
- family/data-sources
- primary-documentation
---
# SEC: Accessing EDGAR Data (SEC, 2026)

**Basis:** official page opened 2026-11-08.

**Takeaway:** EDGAR filings are free, with a fair-access cap of 10 requests per second and a declared User-Agent; filings are accepted 6:00 a.m.–10:00 p.m. ET but those submitted after 5:30 p.m. ET are disseminated the next business day (Forms 3/4/5: 10:00 p.m. cutoff), so acceptance time and public time can differ by a day.

## Problem
How to get filings, at what cost and limits, and what the timestamps mean.

## Data and period
All public EDGAR filings; daily and full indexes; feed archives per filing day; JSON submission and XBRL APIs on data.sec.gov; monthly XBRL RSS archives from April 2005.

## Method
Rules: "Current max request rate: 10 requests/second"; SEC may lower limits; scripts must declare a user agent (company name and contact email). Indexes for the current day update nightly from about 10:00 p.m. ET. The fee-based EDGAR Public Dissemination Service (PDS) is separate.

## Baselines and validation
Not applicable.

## Results (with page or section references)
- Free and bulk-downloadable; a fetch-once design can mirror daily feed archives rather than call per filing.
- Timestamp rule: after-5:30 p.m. submissions are disseminated next business day, so a filing's acceptance timestamp is not when the public could see it (relevant to RQ3.2 and look-ahead).

## Limits and risks to validity
The page does not describe bulk ZIPs (submissions.zip, companyfacts.zip) or full-text search history. PDS subscribers historically received some filings before the public website ([[Rogers 2017 Run EDGAR Run SEC Dissemination]]).

## Rubric scores
Primary documentation (vendor documentation and pricing pages): not scored, per the guide's rubric. Facts below are what the vendor states, not independently checked.

## Quotes worth keeping (each under 15 words, with page)
- "Current max request rate: 10 requests/second." (Accessing EDGAR Data)
- "Anyone can access and download this information for free." (Accessing EDGAR Data)
