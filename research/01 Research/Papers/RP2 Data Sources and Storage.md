---
type: research-paper
paper_id: RP2
title: "Financial Data Sources and Fetch-Once Storage"
status: final
research_questions: [RQ2.1, RQ2.2, RQ2.3, RQ2.4, RQ2.5, RQ2.6, RQ2.7, RQ2.8, RQ2.9]
sources_count: 80
evidence_strong: 1
evidence_moderate: 8
evidence_weak: 6
evidence_primary_documentation: 65
created: 2026-11-08
updated: 2026-11-08
related: ["[[Research Questions]]", "[[Evidence Register]]", "[[Search Log]]", "[[RP1 ML Methods]]"]
tags: [research-paper]
---
# RP2 – Financial Data Sources and Fetch-Once Storage

## Abstract

Affordable US price data come in three groups: long survivorship-free daily data (CRSP, Norgate), bulk intraday or tick archives (Tick Data, FirstRate), and subscription APIs with shorter history (RQ2.1). On the evidence read, the API shortlist is Alpaca, Databento and EODHD, but each needs a survivorship-free daily reference beside it. Massive is the only API whose pages document delisted coverage, and it bans model training (RQ2.7). The ranking has Low confidence: the margins are narrow and several cells are guesses where vendors are silent. Text sources range from free and permissive (EDGAR, GDELT, arXiv metadata) to restrictive (X, StockTwits, licensed news) (RQ2.2). Free macro vintages exist, but FRED/ALFRED terms forbid AI training, which leaves BLS originals and the Philadelphia Fed files as candidates (RQ2.3). On the terms read, vendor contracts rather than copyright set the tightest limits: several vendors ban training and several more stay silent on it (RQ2.6; a reading of terms, not legal advice). Fetch-once ingestion converges on an append-only raw layer, cursor-based loads, a request ledger, HTTP caching and client-side rate limits (RQ2.4). No storage engine read covers both knowledge time and valid time out of the box. Version-per-write stores, bitemporal tables and as-of joins each fill one part, and speed evidence is thin (RQ2.5). Free sources cover identifiers, ownership filings and insiders, while customer-supplier and board data are paid, incomplete and valid-time only (RQ2.8). USGS earthquake feeds are free and update every minute, but NOAA storm records lag by months; GDELT is fast but opaque, ACLED bans training, and AIS is free only for US waters with a lag of months (RQ2.9).

## Research questions

- **RQ2.1** – Which providers offer US stock and ETF prices, and how do they compare on history length, bar and tick resolution, delisted names, corporate-action handling and cost?
- **RQ2.2** – Which text sources exist (licensed news, GDELT, X, Reddit, StockTwits, EDGAR filings, OpenAlex, arXiv)? How good are their timestamps, and what do they cost and allow?
- **RQ2.3** – Which macro and alternative sources provide point-in-time vintages?
- **RQ2.4** – How do practitioners design fetch-once ingestion: append-only raw zones, request ledgers, idempotent incremental loads, watermarks, HTTP caching, rate limiting?
- **RQ2.5** – How do storage engines compare for a solo researcher on versioning, point-in-time reads, speed and upkeep? Candidates: ArcticDB, Parquet with DuckDB, TimescaleDB, QuestDB, Postgres with pgvector, LanceDB, MongoDB, SurrealDB, RocksDB, graph databases versus edge tables
- **RQ2.6** – What do licences and terms allow for storing raw data, deriving features, training models and redistributing results? What fair-access rules apply?
- **RQ2.7** – Which market data API should the project use? Compare the Alpaca Market Data API, Alpha Vantage and other candidates found (for example Databento, Massive (formerly Polygon.io), Tiingo, Twelve Data, EODHD). Criteria: asset coverage, history depth, bar and tick resolution, adjusted and unadjusted prices, delisted symbols, real-time versus delayed data, rate limits, cost per tier, bulk download, SDK quality, licence terms (storage, derived data, model training), and documented data-quality problems and outages
- **RQ2.8** – Which sources describe the structure of the financial world (ownership, subsidiaries, executives and boards, customers and suppliers, stable entity identifiers)? How point-in-time, costly and restricted are they?
- **RQ2.9** – Which sources cover geopolitical, natural-hazard, infrastructure and shipping events (for example GDELT, ACLED, USGS, NOAA, AIS ship tracking)? Compare timestamp quality, latency, history, cost and licence

## Method

Search 2026-11-08 (sessions 17–18). RQ2.1–RQ2.4 used built-in web search and page fetch on vendor and documentation pages; RQ2.5–RQ2.9 used alphaXiv first for papers, then web search and page fetch (Exa not connected in either session). The RQ2.7 scorecard was built with the decision-matrix skill. 80 sources kept (recounted from lit-note properties): 65 primary documentation, 15 scored (1 Strong, 8 Moderate, 6 Weak), including Cohen 2008 and Barrot 2016 reused from RP1. For systems and data-quality studies, rubric checks that do not apply (out-of-sample, point-in-time, costs) were marked N/A and the total scaled to 14. Evidence for RP2 is mostly official documentation, pricing pages and licence terms (guide: "For RP2: official documentation, pricing pages and licence terms"), plus engineering write-ups and the few peer-reviewed data papers. Documentation, pricing and licence pages are marked **Primary documentation** and not scored (guide rubric); research papers are scored 0–14 as in RP1. Queries are in the [[Search Log]]. Screening: keep official vendor pages for facts about coverage, price and limits; drop marketing comparisons and unsourced "best API" lists except as pointers to official pages. No accounts were opened and no data was downloaded.

## Findings

### RQ2.1 – Which providers offer US stock and ETF prices, and how do they compare on history length, bar and tick resolution, delisted names, corporate-action handling and cost?

**Answer.** No single affordable provider gives long history, tick resolution and documented delisted coverage together; the providers split into three groups. (1) **Long survivorship-free daily history:** CRSP (about 100 years, permanent PERMNO/PERMCO identifiers, institutional licence only) and Norgate ($630–$788 a year for listed and delisted stocks back to 1990 or 1950, with historical index constituents, end-of-day only, no REST API). (2) **Long intraday or tick history, bought in bulk:** Tick Data (consolidated ticks since 1993, inactive symbols included, price on request) and FirstRate Data (1-minute bars since 2000 including over 7,000 delisted tickers, upstream source not stated). (3) **Subscription APIs with shorter or plan-limited history:** Massive ($199/month for all history from September 2003, delisted tickers queryable point-in-time, split-adjusted bars); Databento (exchange-direct order-book data with nanosecond timestamps, but tick history only from 2018; Standard $199/month includes 12 months of L1); Alpaca (consolidated SIP bars from 2016 at 1-minute minimum, raw or split/dividend/spin-off adjusted, $99/month); Alpha Vantage (1-minute intraday back to 2000 by month, adjusted or raw, $49.99+/month); EODHD (1-minute US from 2004 at $29.99/month, ticks from 2008 as an add-on); Tiingo (30+ years daily at $30/month, but intraday from IEX only). Delisted-name coverage is documented only by CRSP, Norgate, Tick Data, FirstRate and Massive; for Alpaca, Alpha Vantage, EODHD, Tiingo and Databento it was not confirmed on the pages read. Corporate actions are handled at query time (Alpaca, Alpha Vantage, Massive split-only), as separate files (Tick Data, Databento), or pre-built adjusted and unadjusted series (FirstRate, Norgate). Independent evidence on vendor accuracy is thin and old: even CRSP has documented price errors, biased daily equal-weighted index returns and missing delisting returns (about 13% of delistings still missing in 2017), so delistings and adjustments need cross-checking whichever vendor is used.

**Confidence:** Medium. High for the stated prices, limits and history (read on official pages on 2026-11-08); Low for data quality, which only one independent review addresses and none for the retail APIs.

| Provider | History (US stocks) | Finest resolution | Delisted names | Corporate actions | Cost (list, 2026-11-08) | Source |
| --- | --- | --- | --- | --- | --- | --- |
| CRSP | ~100 years | Daily | Yes (PERMNO) | Included | Institutional licence, no public price | [[CRSP 2026 US Stock Databases]] |
| Norgate | 1990 (Platinum) / 1950 (Diamond) | Daily | Yes, 25,222 (1950–Sep 2022) | Adjusted series (method not read) | $630 / $787.50 a year | [[Norgate 2026 US Stocks Packages and Delisted Data]] |
| Tick Data | 1993 (trades, quotes); 2004 (NBBO) | Tick | Yes | Files + ticker mapping | On request | [[Tick Data 2026 US Equities Historical]] |
| FirstRate Data | 2000 | 1 minute | Yes, 7,000+ | Adjusted + unadjusted | Bundle price not shown; updates $59.95/month | [[FirstRate Data 2026 Complete Intraday Stocks]] |
| Massive | 2003-09-10 | Bars from docs; trades/quotes claimed | Yes (`active=false`, `delisted_utc`) | Split-adjusted by default | Free (2 y EOD) / $29 / $79 / $199 a month | [[Massive 2026 Stocks API Plans and History]] |
| Databento | Ticks 2018; daily backfill toward 2010 in progress | Order book (MBO), ns timestamps | Not confirmed | Separate datasets | Usage per GB; $199 / $1,750 / $4,500 a month | [[Databento 2026 US Equities Data and Pricing]] |
| Alpaca | 2016 | 1-minute bars (ticks not checked) | Not stated; `asof` follows renames | Query-time (raw, split, dividend, spin-off) | Free (IEX; SIP history >15 min old) / $99 a month | [[Alpaca 2026 Market Data API Stocks]] |
| Alpha Vantage | Intraday 2000-01; daily 25+ years | 1 minute | Not confirmed (LISTING_STATUS unread) | Query-time adjusted/raw | Free 25/day; $49.99–$249.99 a month | [[Alpha Vantage 2026 Premium Plans and Time Series]] |
| EODHD | EOD 1972; 1-minute 2004; ticks 2008 | Tick (add-on) | Not stated on pricing page | Not stated | $19.99–$99.99 a month; ticks +$9.99 | [[EODHD 2026 Pricing and Data Coverage]] |
| Tiingo | 30+ years daily | IEX-only intraday | Not stated | Not stated | Free / $30 a month (personal); $50 commercial | [[Tiingo 2026 Pricing and IEX API]] |

Evidence on data quality: [[Liu 2020 Data Quality Problems Finance Databases]] (Moderate, 7).

**What would change the answer:** an independent comparison of retail-API prices and delistings against CRSP; vendor confirmation of delisted coverage for Alpaca, Alpha Vantage, EODHD, Tiingo and Databento; Databento finishing its pre-2018 daily backfill; the bulk prices of Tick Data and FirstRate.

**Stop rule:** 11 sources kept (10 primary documentation, 1 scored). The last three vendor pages (EODHD, Tick Data, FirstRate) each added a provider row but no new pattern beyond the three groups above.

### RQ2.2 – Which text sources exist (licensed news, GDELT, X, Reddit, StockTwits, EDGAR filings, OpenAlex, arXiv)? How good are their timestamps, and what do they cost and allow?

**Answer.** The free sources are the best documented and the most permissive: **EDGAR** (free, 10 requests/s, bulk daily archives), **GDELT** (free for any use including commercial, redistributable with citation, 15-minute files back to 2013/2015 with a reduced event set from 1979), **arXiv metadata** (CC0, one request per 3 s) and **OpenAlex** (free key, 30 requests/s; paid plans above that). Their limits are on full text and timing semantics rather than cost: arXiv full texts keep per-paper licences, and EDGAR's acceptance time is not its public time (filings begun after 5:30 p.m. ET, or 10 p.m. for Forms 3, 4 and 5, go out the next business day; in 2012–13 paying PDS subscribers saw just over half of Form 4 filings seconds before the public site). **Social sources** are costly or closed: X is pay-per-use at $0.005 per post read with a 3-million-post monthly cap and full-archive search back to 2006 (about $15,000 for a full month's cap); Reddit gives 100 queries/minute free with commercial and research use by approval (terms page unreadable this session); StockTwits bans scraping and licenses derived products itself, with no public data offer found. **Licensed news** (Benzinga, RavenPack/Dow Jones) has the best timestamp precision (RavenPack: milliseconds over 20+ years; Benzinga: created and updated fields) but no public prices, and their storage and training rights were not stated on the pages read. Timestamp quality is documented as a rule only for EDGAR and GDELT; no independent study of news-vendor timestamp accuracy was found this session.

**Confidence:** Medium for access, cost and licence of the free sources (official pages); Low for licensed news (prices and training rights unpublished) and for timestamp accuracy outside EDGAR.

| Source | Modality | History | Timestamp | Cost | Storage / redistribution | Training rights | Lit note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SEC EDGAR | Filings | Full EDGAR; XBRL RSS from 2005 | Acceptance time; after the 5:30 p.m. cutoff (10 p.m. for Forms 3/4/5) public next business day | Free; 10 req/s | Public data | Not restricted on page | [[SEC 2026 Accessing EDGAR Data]], [[Rogers 2017 Run EDGAR Run SEC Dissemination]] |
| GDELT | News events, GKG | 1979 (reduced events); GKG 2013 | 15-minute files | Free | Redistribute with citation | Any use, no fee | [[GDELT 2026 Data and Terms of Use]] |
| X | Social posts | March 2006 | Not stated on pages read | $0.005/post read; 3M/month cap | Allowed with 24-hour deletion duty; no redistribution (RQ2.6) | No for foundation or frontier models (RQ2.6) | [[X 2026 API Pricing and Search]], [[X 2026 Developer Agreement]] |
| Reddit | Social posts | Not stated | Not stated | Free 100 QPM; commercial by approval | Terms blocked | Terms blocked | [[Reddit 2026 Data API Wiki]] |
| StockTwits | Social posts | Not stated | Not stated | No public offer | Scraping banned | Not mentioned | [[StockTwits 2026 Terms of Service]] |
| Benzinga | Licensed news | Not stated | created/updated (HH:MM:SS, UNIX) | On request | Display allowed | Not stated | [[Benzinga 2026 Stock News API]] |
| RavenPack | Licensed news analytics | 20+ years | Millisecond | Institutional | Not stated | Not stated | [[RavenPack 2026 News Analytics Library Guide]] |
| Alpaca news | News (feed in `source`) | Not stated | created_at | Not stated | Not stated | Not stated | [[Alpaca 2026 Historical News API]] |
| arXiv | Papers | All | Submission dates in metadata | Free; 1 req/3 s | Metadata CC0; full text per paper | Not addressed | [[arXiv 2026 API Terms of Use]] |
| OpenAlex | Paper metadata | Not stated on page | Not stated | Free key; paid above | Not read | Not read | [[OpenAlex 2026 API Authentication and Limits]] |

**What would change the answer:** the X Developer Policy (the Developer Agreement was read under RQ2.6) and Reddit Data API Terms (storage, deletion, training); Benzinga and RavenPack quotes; an independent study of news-feed timestamp accuracy (also RQ3.2).

**Stop rule:** 11 sources (10 primary documentation, 1 scored, Weak). Not fully met for licensed news and timestamp accuracy: top-up list for a later session: X Developer Policy; Reddit Data API Terms (blocked here); OpenAlex pricing and snapshot pages; Dow Jones/Factiva or Refinitiv news licensing; the Bartlett & McCrary (2016) SIP latency paper (NBER w22551, seen in search) for price-feed timestamps.

### RQ2.3 – Which macro and alternative sources provide point-in-time vintages?

**Answer.** For US macro data three free vintage sources exist: **ALFRED** (over 350,000 series; the FRED API returns data as known on any past date through `realtime_start`/`realtime_end`), the **Philadelphia Fed Real-Time Data Set** (headline macro variables, vintages added monthly, first/second/third releases) and **FRED-MD/FRED-QD** (ready-made forecasting panels with monthly vintages from 1999-08 and 2018-05). Vintages matter: revisions are large (2008Q4 real GDP growth went from −3.8% to −6.2%), and real-time evaluation weakens or reverses several published forecasting results. The main finding is a licence one: **FRED's terms, which cover ALFRED, prohibit using FRED content to develop or train machine-learning or AI systems and prohibit storing, caching or archiving it through the API**, even for personal use. The public-domain originals (BLS states everything it publishes is public domain) are not bound by those terms, so a compliant route is the Philadelphia Fed files (licence to confirm) and the agencies' own release archives, with vintages kept by the project. For company fundamentals, point-in-time data matters even more: Compustat's common files are re-standardised in place, and in its Snapshot point-in-time files the sign of earnings changes flips in about 9–10% of firm-quarters across updates (Table 8; about 14% for sales changes). Commercial point-in-time fundamentals exist (Compustat Snapshot/Point-in-Time, LSEG and FactSet point-in-time, Sharadar as-reported; seen in search, not opened), all paid. No alternative-data (non-macro, non-fundamental) vintage source was found; the evidence there is thin.

**Confidence:** High that vintages matter and that ALFRED/RTDSM/FRED-MD provide them; Medium on the licence reading (terms read through a summarising fetch tool, not legal advice); Low on alternative-data vintages.

| Source | Content | Vintages | Cost | Storage / training terms | Lit note |
| --- | --- | --- | --- | --- | --- |
| ALFRED / FRED API | 350,000+ series | Every release, as-of queries | Free | Storage via API and AI training prohibited | [[ALFRED 2026 Real-Time Vintages and FRED API]], [[FRED 2026 Legal Terms of Use]] |
| Philadelphia Fed RTDSM | Headline US macro | Monthly; first–third releases | Free (no price stated) | Not stated | [[Philadelphia Fed 2026 Real-Time Data Set]] |
| FRED-MD / FRED-QD | Macro forecasting panels | Monthly from 1999-08 / 2018-05 | Free | Not stated; built from FRED | [[McCracken 2026 FRED-MD FRED-QD Databases]] |
| BLS (original releases) | Labour, prices | Project must archive releases | Free | Public domain | [[BLS 2026 Copyright Information]] |
| Compustat Snapshot (fundamentals) | Firm financials | Point-in-time updates 1986–2023 | Institutional | Licensed | [[Lyle 2024 Re-Standardized Financial Statement Data]] |

Evidence that vintages matter: [[Croushore 2011 Frontiers of Real-Time Data Analysis]] (Strong, 12, survey), [[Lyle 2024 Re-Standardized Financial Statement Data]] (Moderate, 7).

**What would change the answer:** the Philadelphia Fed and FRED-MD licence terms; St. Louis Fed confirming whether research downloads of FRED-MD fall under the AI-training prohibition; an alternative-data vintage source.

**Stop rule:** 7 sources (5 primary documentation, 2 scored). Stopped at 7: the last three (FRED-MD, BLS, Lyle) each added something (panel vintages, public-domain route, fundamentals restatement size), so the rule is not fully met. Top-up list: BEA and Census terms; ALFRED help on vintage coverage per series; Compustat Point-in-Time and LSEG point-in-time product pages; Croushore & Stark (2001) original RTDSM paper.

### RQ2.4 – How do practitioners design fetch-once ingestion: append-only raw zones, request ledgers, idempotent incremental loads, watermarks, HTTP caching, rate limiting?

**Answer.** The documented practice converges on five layers. (1) An **append-only raw (bronze) layer** that keeps source data as-is, with provenance columns and loose types so schema changes never drop data, and from which everything else can be rebuilt (Databricks). (2) **Incremental loads driven by a cursor (watermark) and a primary key**, writing an append-only history and a deduplicated current table (dlt, Airbyte); delivery is at-least-once, so duplicates are normal, coarse cursors need re-reads, and records that change without moving the cursor are silently missed. (3) **Idempotency keyed on a request identity**: AWS's pattern records a unique request token with its parameters atomically with the work and returns the same result on repeat; on the client side the same idea is a request ledger keyed by endpoint plus parameters (this transfer is the project's reading, not a documented market-data practice). (4) **HTTP caching**: RFC 9111 conditional requests (ETag, Last-Modified, 304) avoid re-downloading unchanged resources, and Python caches (hishel, requests-cache) can keep closed historical periods indefinitely with per-URL expiry for recent data. (5) **Client-side rate limiting** set to the vendor's published limits, honouring `Retry-After`; standard `RateLimit` headers are still an IETF draft and do not guarantee service. No source read describes a request ledger for market-data APIs specifically, or measures any of these patterns; the evidence is design documentation.

**Confidence:** Medium. Patterns are consistent across independent sources, but all are engineering documentation with no measured comparison.

**Fetch-once design patterns and trade-offs**

| Pattern | What it does | Trade-off / failure mode | Sources |
| --- | --- | --- | --- |
| Append-only raw zone | Store every response as received, with source, request and ingestion metadata | Storage grows; needs a separate cleaned layer; licence may limit how long raw data can be kept (RQ2.6) | [[Databricks 2026 Medallion Architecture]] |
| Request ledger (client-side idempotency) | Record each request's identity, parameters, time, status and response location before reuse | Extra bookkeeping; identity must be deterministic (normalised parameters); not documented for market data | [[Featonby 2026 Idempotent APIs Builders Library]] |
| Cursor / watermark incremental load | Fetch only records after the last cursor value | Misses updates that do not move the cursor; ties and coarse cursors cause duplicates or gaps; needs lookback window | [[dltHub 2026 Incremental Loading]], [[Airbyte 2026 Incremental Append Deduped]] |
| History table + deduplicated current table | Keep every version, serve latest by key | Two tables to keep consistent; "latest" overwrites knowledge-time unless versions are kept (RQ3.8) | [[Airbyte 2026 Incremental Append Deduped]] |
| HTTP conditional requests | Revalidate with ETag / Last-Modified; 304 means reuse | Many data APIs send no validators | [[IETF 2022 RFC 9111 HTTP Caching]], [[Hishel 2026 HTTP Caching Library]] |
| Forced cache with per-URL expiry | Cache closed periods forever, recent periods briefly | Can serve stale data if a vendor revises history; vendor terms may forbid caching (e.g. FRED API) | [[requests-cache 2026 Expiration Guide]], [[FRED 2026 Legal Terms of Use]] |
| Client-side rate limiter + back-off | Token bucket at published limits; obey Retry-After | Published limits change; server headers not standard yet | [[IETF 2026 RateLimit Header Fields Draft]] |

**What would change the answer:** an engineering write-up or study of market-data ingestion that measures re-fetch rates, data loss or vendor revisions under these patterns.

**Stop rule:** 8 sources (all primary documentation). The last three (requests-cache, hishel, RateLimit draft) added detail but no new pattern. Evidence on measured outcomes is thin (none found).

### RQ2.5 – How do storage engines compare for a solo researcher on versioning, point-in-time reads, speed and upkeep? Candidates: ArcticDB, Parquet with DuckDB, TimescaleDB, QuestDB, Postgres with pgvector, LanceDB, MongoDB, SurrealDB, RocksDB, graph databases versus edge tables

**Answer.** No engine read covers both knowledge time and valid time for every data type, so the comparison is about which layer each one fills. (1) **Point-in-time reads come in three kinds.** *Version-per-write* stores (ArcticDB, LanceDB, SurrealDB on SurrealKV) let you read a table as it was stored at a past version or snapshot. That is knowledge time only, and versions can be pruned: LanceDB drops untagged versions after 7 days by default. *Bitemporal* stores (XTDB, SQL:2011 temporal clauses) keep both system (knowledge) time and valid time and answer "what did we know then" directly, which is the property a look-ahead-free backtest needs (Jensen 1995 definitions). *As-of joins* (QuestDB `ASOF JOIN`, also in DuckDB) attach the latest value at or before each timestamp, but on their own they do not keep corrected history. QuestDB deduplication, for example, overwrites on the last write. (2) **Speed evidence is thin and mostly vendor-reported.** The one finance-specific benchmark (Barez 2023, Weak: one month of crypto, single thread) found kdb+ fastest, InfluxDB most compact and TimescaleDB slowest on most queries. A broader workload benchmark (Mostafa 2026, Moderate) found TimescaleDB stalling beyond moderate parallelism with heavy disk amplification, and read/write contention dominating mixed workloads. QuestDB's own figures are 8.59M rows/s against TimescaleDB's 1.08M on TSBS, but they are vendor-run. No independent benchmark of ArcticDB, DuckDB-on-Parquet, LanceDB, SurrealDB or QuestDB on market data was found. (3) **Upkeep and licence separate the embedded options from the servers.** ArcticDB, DuckDB/Parquet, LanceDB and RocksDB need no server. TimescaleDB, QuestDB, MongoDB, SurrealDB (server mode) and XTDB do. ArcticDB is BSL 1.1: free to use, but production use needs a paid licence. TimescaleDB's compression and continuous aggregates sit under the Timescale License, which is free to self-host. QuestDB is Apache 2.0. (4) **Embeddings:** pgvector keeps vectors next to relational data, but approximate indexes filter after the scan, and inside Postgres, page access rather than distance maths dominates query time (Lu 2026). Indexed `vector` columns are limited to 2,000 dimensions. (5) **Graphs:** on one synthetic benchmark by an interested vendor (Nguyen 2026, Weak), edge tables in a columnar SQL engine beat native graph engines on scans, joins and top-k, and lost only on bounded neighbourhood walks. Bulk-load speed varied about 860× and dominated total cost. (6) **MongoDB time series collections** restrict updates to the metaField and forbid writes in transactions, so corrections need their own design. **RocksDB** is a key-value library with no query or time-series layer, so it is relevant as the engine under other systems rather than as a research store.

**Confidence:** Medium on features, licences and point-in-time semantics (primary documentation, consistent). Low on speed (two independent benchmarks, neither on equity bars at research scale, plus vendor claims).

**Storage-engine comparison**

| Engine | Kind / deployment | Versioning and point-in-time reads | Speed evidence | Upkeep | Licence | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| ArcticDB | Embedded Python DataFrame store on LMDB or S3-type object storage | Version per write and named snapshots: knowledge-time reads by version or snapshot; old versions prunable | Vendor claims only (no figures) | No server; last writer wins; one writer per symbol | BSL 1.1: free to use, production use needs a paid licence; each version converts to Apache 2.0 after a set date | [[ArcticDB 2026 FAQ and Licence]] |
| Parquet + DuckDB | Files plus an embedded SQL engine | None built in; history kept by writing new dated files or partitions (project reading); as-of joins in SQL | Column and filter pushdown with zonemaps (docs); no independent finance benchmark read | No server; files are portable | DuckDB licence not read this session | [[DuckDB 2026 Parquet Read and Write]] |
| TimescaleDB | Postgres extension (server) | No built-in versioning; ordinary Postgres history tables possible | Slowest on most queries in one finance benchmark; stalls beyond moderate parallelism, disk amplification | Postgres server administration | Apache 2 core; compression and continuous aggregates under the Timescale License (free to self-host, cannot be sold as a service) | [[Tiger Data 2026 TimescaleDB Editions]], [[Barez 2023 Benchmarking Databases High-frequency Data]], [[Mostafa 2026 Six Dimensions Benchmarking TSDBs]] |
| QuestDB | Time-series SQL server | ASOF JOIN; upsert-key deduplication with last write wins (keeps no versions) | Vendor TSBS: 8.59M rows/s vs TimescaleDB 1.08M (one instance) | Server | Apache 2.0; Enterprise adds replication and tiering | [[QuestDB 2026 ASOF Join and Deduplication]] |
| Postgres + pgvector | Relational server with vector types | Postgres history tables possible; no vector versioning | Filtered approximate search: page access dominates; library benchmarks overstate speed (up to 10×) | Postgres server; index tuning | pgvector licence not confirmed this session | [[pgvector 2026 Postgres Vector Search]], [[Lu 2026 Filtered Vector Search PostgreSQL]] |
| LanceDB | Embedded columnar vector store | Version per write; checkout, restore, tags; untagged versions pruned after 7 days by default | None read | No server; compaction invalidates parts of ANN indexes | Not confirmed this session | [[LanceDB 2026 Table Versioning and Time Travel]] |
| MongoDB (time series) | Document server, bucketed time series | No as-of reads; updates only on metaField; no writes in transactions | None read | Server | Not read this session | [[MongoDB 2026 Time Series Collection Limitations]] |
| SurrealDB | Multi-model (document, graph, vector) on a KV layer; embedded or server | `SELECT ... VERSION` time travel on SurrealKV only | None read | Engine line-up changed in 4.0 | Not confirmed this session | [[SurrealDB 2026 Architecture and Versioned Queries]] |
| RocksDB | Embedded KV library | Snapshots, lost on restart; no as-of layer | None read | Compaction and cache tuning; everything above KV is user code | Not read this session | [[RocksDB 2026 Overview]] |
| XTDB (bitemporal reference) | Bitemporal SQL server | System time and valid time; `FOR SYSTEM_TIME AS OF` / `FOR VALID_TIME AS OF`; nothing erased | None read | Server; smaller ecosystem | Not read this session | [[XTDB 2026 Time in XTDB Bitemporal]], [[Jensen 1995 TSQL2 Data Model]] |
| Graph DB vs edge tables | Native graph engines (Neo4j, Memgraph, Ladybug) vs edge tables in a columnar SQL engine | Engine-dependent | Edge tables won scans, joins and top-k; native won bounded paths; ingest varied about 860× | Graph servers add a second system | Varies | [[Nguyen 2026 Graph Database Engines Cost]] |

| Source | Evidence | Finding |
| --- | --- | --- |
| [[Barez 2023 Benchmarking Databases High-frequency Data]] | Weak (4) | kdb+ fastest; TimescaleDB highest query latency; one month of crypto, single thread |
| [[Mostafa 2026 Six Dimensions Benchmarking TSDBs]] | Moderate (7) | Single-axis benchmarks hide bottlenecks; TimescaleDB stalls under parallel load |
| [[Nguyen 2026 Graph Database Engines Cost]] | Weak (5) | No engine fastest on all shapes; ingest cost dominates; vendor-authored |
| [[Lu 2026 Filtered Vector Search PostgreSQL]] | Moderate (7) | In Postgres, system overhead dominates filtered vector search |
| 11 documentation and reference notes | Primary documentation | Features, versioning semantics, licences (table above) |

**What would change the answer:** an independent benchmark of DuckDB/Parquet, ArcticDB, QuestDB and LanceDB on equity bars at research scale (for example 20 years of 1-minute bars for about 5,000 symbols); the DuckDB, pgvector, LanceDB, SurrealDB and XTDB licence texts; a documented case of a market-data research store built on bitemporal tables.

**Stop rule:** met at the 15-source cap (11 primary documentation, 4 scored: 0 Strong, 2 Moderate, 2 Weak). Speed evidence is thin: only two independent benchmarks were found, and neither tests the embedded engines.

### RQ2.6 – What do licences and terms allow for storing raw data, deriving features, training models and redistributing results? What fair-access rules apply?

**Answer.** Three layers of rules apply, and the strictest one decides. (1) **Contract terms** with the vendor or platform are the binding layer, and they are often stricter than copyright. Massive bans using its data "to train, fine-tune or distill" AI or ML models and requires deletion within 30 days after the licence ends. X bans training a "foundation or frontier model" on its content and requires removed posts to be deleted within 24 hours of a request. FRED (which includes ALFRED) bans ML/AI development and training, and API caching. (2) **Exchange pass-through agreements** sit under the retail APIs. Nasdaq's subscriber agreement limits non-professionals to personal use and professionals to internal use, forbids giving anyone else access, and defines the licensed Information to include data "as used or processed". So features derived from the data probably stay under the licence (project reading). Massive's terms allow keeping only your own analyses that cannot recreate the data. (3) **Copyright** covers text, not facts. The US Copyright Office's non-binding 2025 report says that collecting and training on copyrighted works implicates the reproduction right, that fair use is fact-specific, and (per a law-firm summary) that research or non-substitutive training on factual works leans toward fair use. Contract terms still apply on top. **Silence is common.** Alpaca, Alpha Vantage and EODHD license data for personal, non-commercial use and do not mention model training at all. EODHD explicitly allows private storage and analysis. Alpaca's terms forbid copying and redistribution. **Freely usable sources** are SEC EDGAR (public data; fair access at 10 requests per second with a declared User-Agent), BLS originals (public domain), GDELT (free for any use, redistribution with citation) and arXiv metadata (full texts keep per-paper licences). Databento passes through each publisher's terms; most historical data older than 24 hours can be redistributed. **Redistributing results** is safest as aggregate outputs that cannot recreate the source data (forecasts, metrics, code). Raw or near-raw data is barred by every commercial vendor read.

**Confidence:** Medium on what the terms say (official pages, read 2026-11-08). Low on how they apply to this project: several terms are silent, "production use" and "foundation model" are not defined, and this is a reading of terms, not legal advice.

**Rights by source (as read 2026-11-08)**

| Source | Store raw | Derive features | Train models | Redistribute | Fair-access / limits | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| Massive | Yes, personal use; delete within 30 days of licence end | Own analyses that cannot recreate data | **No** (s. 5(g)) without express permission | No | Plan limits; CME purge on end | [[Massive 2025 Market Data Terms of Service]] |
| Alpaca | Not addressed; "no copying" clause | Not addressed | Not mentioned | No, without written consent | Plan limits; Pro plan adds Nasdaq/NYSE terms | [[Alpaca 2026 Terms and Conditions Market Data]], [[Nasdaq 2026 Global Subscriber Agreement]] |
| Alpha Vantage | Not addressed | Not addressed | Not mentioned; macro and commodity APIs fall under FRED terms | No (counts as commercial use) | 25 requests/day free; premium per minute | [[Alpha Vantage 2026 Terms of Service]] |
| EODHD | Yes for non-professionals (private) | Private analysis allowed | Not mentioned | No | Plan limits | [[EODHD 2026 Terms and Conditions]] |
| Databento | Per publisher terms | Per publisher terms | Not stated | Historical data older than 24 h mostly allowed, subject to publisher | Usage-based per GB | [[Databento 2026 US Equities Data and Pricing]] |
| Nasdaq (pass-through) | Not addressed | Processed data is still Information | Not addressed | No access for others; limited professional excerpts | Audit and inspection rights | [[Nasdaq 2026 Global Subscriber Agreement]] |
| FRED / ALFRED | API storing/caching forbidden | – | **No** (any ML/AI training) | Not checked here | API key limits | [[FRED 2026 Legal Terms of Use]] |
| BLS | Yes (public domain) | Yes | Yes | Yes (citation requested) | – | [[BLS 2026 Copyright Information]] |
| SEC EDGAR | Yes (public) | Yes | Yes (public records; copyright in exhibits not checked) | Yes | 10 requests/s; declared User-Agent | [[SEC 2026 Accessing EDGAR Data]] |
| GDELT | Yes | Yes | Yes (free for any use) | Yes, with citation and link | – | [[GDELT 2026 Data and Terms of Use]] |
| X | Yes, with security and 24-hour deletion duty; delete all at termination | Analysis as approved by X | **No** for foundation or frontier models | No (post IDs count as X Content) | Paid tiers | [[X 2026 Developer Agreement]], [[X 2026 API Pricing and Search]] |
| StockTwits | Scraping banned | – | Not mentioned | No | Licensed products only | [[StockTwits 2026 Terms of Service]] |
| Reddit | Not confirmed (Data API Terms blocked) | – | Not confirmed | – | Rate limit; commercial and research use need approval | [[Reddit 2026 Data API Wiki]] |
| arXiv | Metadata yes | Yes | Full text: per-paper licence | Full text: per-paper licence | 1 request per 3 s | [[arXiv 2026 API Terms of Use]] |
| Copyright layer (US) | – | – | Fact-specific fair use; research and non-substitutive use favoured (non-binding) | – | – | [[US Copyright Office 2025 Generative AI Training Report]] |

**What would change the answer:** written answers from Alpaca, Alpha Vantage, Massive, EODHD and the St. Louis Fed on research model training (vendor-quote list); X's Developer Policy and Reddit's Data API Terms; a court decision or the final Copyright Office report on training for non-generative, non-substitutive models.

**Stop rule:** met at 15 sources (7 new primary documentation, plus 8 earlier RP2 notes reused and tagged RQ2.6). The last three new sources (EODHD, the Nasdaq agreement, the Copyright Office report) refined the picture but did not change the pattern above. No peer-reviewed study of data-licence terms for ML was found (thin).

### RQ2.7 – Which market data API should the project use? Compare the Alpaca Market Data API, Alpha Vantage and other candidates found (for example Databento, Massive (formerly Polygon.io), Tiingo, Twelve Data, EODHD). Criteria: asset coverage, history depth, bar and tick resolution, adjusted and unadjusted prices, delisted symbols, real-time versus delayed data, rate limits, cost per tier, bulk download, SDK quality, licence terms (storage, derived data, model training), and documented data-quality problems and outages

**Answer.** On the evidence read, the ranked shortlist is **(1) Alpaca, (2) Databento, (3) EODHD**, and the margins are narrow (112, 109 and 106 of a possible 170). Massive scores second on the criteria (111) and is the only API with documented delisted-ticker coverage, but its terms ban model training, so it is out unless it grants written permission. Three caveats outweigh the ranking. (a) None of the three shortlisted APIs documents delisted-symbol coverage, so each would need a survivorship-free reference beside it, such as Norgate or CRSP daily data from RQ2.1. (b) None of their terms mentions model training. Alpaca and EODHD license data for personal, non-commercial use, and Databento passes through each publisher's terms. Silence is not permission, so written confirmation is on the vendor-quote list. (c) Independent data-quality evidence is almost absent. The only check found is one informal comparison of Alpha Vantage with CRSP, which found its adjusted close inconsistent. No outage history could be read (Alpaca's status pages load dynamically). Many "not stated" cells are scored 2 as a guess, which favours vendors whose documentation is fuller.

**Confidence:** Low. The ranking depends on guessed scores for undocumented items and on weights proposed by this session; one weight change reorders the top three (see sensitivity).

**Decision frame.** Which API to shortlist for US stock and ETF prices for the build phase. Not decided here: buying anything, the final vendor (the methodology plan decides), and macro or text sources (RQ2.2, RQ2.3). Dealbreaker, applied outside the weights: an explicit ban on training models with the data (Massive s. 5(g)). Weights are this session's proposal; the user can change any of them and the matrix can be rescored.

**Market data API scorecard** (scores 1–5; *g* = guess where the vendor page is silent; weights in the header)

| Provider                          | History (4)                                                | Resolution (3)                          | Adjusted + raw (4)                                      | Delisted (5)                      | Limits + bulk (3)                            | Cost (3)                                                  | SDK (2)                                              | Licence: storage, derived, training (5)                                                         | Quality / outages (3)                                  | Coverage (1)                               | Real-time (1)             | **Total /170** |
| --------------------------------- | ---------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------- | --------------------------------- | -------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------ | ------------------------- | -------------- |
| Alpaca                            | 3: SIP bars from 2016                                      | 3: 1-minute bars (ticks not checked)    | 5: query-time raw, split, dividend, spin-off            | 2: not stated                     | 3*g*: limits not read; no flat files seen    | 5: free (IEX; SIP history older than 15 min) or $99/month | 5: official alpaca-py, Apache 2.0, ~1.6k stars       | 2: personal non-commercial; no copying or redistribution; training not mentioned                | 3*g*: no independent check; status history unreadable  | 4: stocks, options, crypto                 | 4: real-time on paid plan | **112**        |
| Databento                         | 2: ticks from 2018; daily backfill toward 2010 in progress | 5: full order book (MBO), ns timestamps | 3: corporate actions as separate, priced datasets       | 2: not confirmed                  | 5: batch flat-file downloads; billed per GB  | 2: per-GB billing plus $199+/month plans                  | 5: official Python, C++ and Rust clients, Apache 2.0 | 3: publisher pass-through; most history older than 24 h redistributable; training not stated    | 3*g*: exchange-direct; no independent check            | 4: equities, futures, options              | 5: live feeds             | **109**        |
| EODHD                             | 4: EOD from 1972; 1-minute from 2004                       | 4: ticks from 2008 (add-on)             | 2: not stated                                           | 2: not stated on pricing page     | 3*g*: per-plan limits not read               | 5: $19.99–$99.99/month                                    | 2*g*: SDK not checked                                | 3: non-professionals may store and analyse privately; no redistribution; training not mentioned | 3*g*: no evidence                                      | 5: global                                  | 3: varies by plan         | **106**        |
| *Massive (excluded: dealbreaker)* | 4: from 2003-09                                            | 4: bars; trades and quotes claimed      | 2: split-adjusted only, no dividends                    | 5: point-in-time delisted queries | 4: flat files (access per plan unconfirmed)  | 3: $199/month for all history                             | 3*g*: not checked                                    | 1: **bans AI/ML training**; delete within 30 days of licence end                                | 3*g*: no evidence                                      | 5: stocks, options, indices, forex, crypto | 4                         | *111*          |
| Alpha Vantage                     | 5: intraday from 2000, by month                            | 3: 1 minute                             | 3: query-time, but adjusted close reported inconsistent | 2: LISTING_STATUS not read        | 2: 25/day free; 75–1,200/min paid; no bulk   | 4: $49.99–$249.99/month                                   | 2*g*: no official SDK checked                        | 2: personal non-commercial; silent on training; macro APIs under FRED terms                     | 2: one informal CRSP check found adjusted-close errors | 4                                          | 3: premium only           | **96**         |
| Tiingo                            | 2: 30+ years daily; intraday from IEX only                 | 2: IEX intraday                         | 2: not stated                                           | 2: not stated                     | 3*g*                                         | 5: $30/month personal                                     | 2*g*                                                 | 2: terms page failed to load                                                                    | 3*g*                                                   | 3                                          | 3                         | **85**         |
| Twelve Data                       | 2: not stated                                              | 2: not stated                           | 2: not stated                                           | 2: not stated                     | 3: 8/min free; unlimited daily on paid plans | 3: $79–$999/month                                         | 2*g*                                                 | 2: "internal non-display" labels; terms not read                                                | 3*g*                                                   | 4                                          | 4                         | **81**         |

Arithmetic (Alpaca): 4×3 + 3×3 + 4×5 + 5×2 + 3×3 + 3×5 + 2×5 + 5×2 + 3×3 + 1×4 + 1×4 = 112. The other rows use the same weights.

**Evidence behind the deciding scores.** Delisted coverage: RQ2.1 vendor notes; only Massive documents it ([[Massive 2026 Stocks API Plans and History]]). Licence: [[Massive 2025 Market Data Terms of Service]], [[Alpaca 2026 Terms and Conditions Market Data]], [[EODHD 2026 Terms and Conditions]], [[Alpha Vantage 2026 Terms of Service]], [[Databento 2026 US Equities Data and Pricing]]. Adjustments and history: [[Alpaca 2026 Market Data API Stocks]], [[Databento 2026 US Equities Data and Pricing]], [[EODHD 2026 Pricing and Data Coverage]], [[Alpha Vantage 2026 Premium Plans and Time Series]], [[Tiingo 2026 Pricing and IEX API]], [[Twelve Data 2026 Pricing]]. SDKs: [[Alpaca 2026 alpaca-py SDK]], [[Databento 2026 Python Client]]. Data quality: [[Giulio 2025 Alpha Vantage Adjusted Close vs CRSP]] (Weak, 4), [[Liu 2020 Data Quality Problems Finance Databases]] (Moderate, 7; CRSP errors, so any vendor needs cross-checks).

**Sensitivity.** Lowering the cost weight to 1, or raising the resolution weight to 5, puts Databento first. Lowering the delisted weight to 1 leaves the order Alpaca, Databento, EODHD. If Massive gave written permission to train (licence score 1 → 3 or more), it would rank first or tie for first (121 or more), because it is the only API with documented delisted coverage. A single confirmed fact, such as Alpaca or EODHD documenting delisted symbols, would move that vendor clearly ahead.

**Recommendation (for the methodology plan; not a decision).** Shortlist Alpaca and Databento, with EODHD as the low-cost alternate, each paired with a survivorship-free daily reference (Norgate or CRSP). The reversible first step is to send the written questions on the vendor-quote list (delisted coverage, storage after cancellation, model training) to Alpaca, Databento, EODHD and Massive before any subscription. Three findings would change the recommendation: Massive permitting training; a shortlisted vendor stating that it bans training; or an independent accuracy check of the shortlisted vendors against CRSP.

**Stop rule:** 15 sources: 4 new (2 SDK repositories, 1 pricing page, 1 data check scored Weak) plus 11 reused from RQ2.1 and RQ2.6. Evidence on data quality and outages is thin (one informal check; no outage history readable).

### RQ2.8 – Which sources describe the structure of the financial world (ownership, subsidiaries, executives and boards, customers and suppliers, stable entity identifiers)? How point-in-time, costly and restricted are they?

**Answer.** Free sources cover identifiers, ownership filings and insiders well. Customer-supplier links and boards are thin unless paid for, and none of the sources read records when a relationship became known, as distinct from when it was true. (1) **Identifiers.** OpenFIGI maps tickers, ISINs and CUSIPs to FIGIs for free (25 to 250 mapping requests a minute). Delisted equities are returned only on request, and it gives current mappings, not a dated history. GLEIF LEIs carry direct and ultimate accounting parents and are free, with website data under CC0. Parent data exist only from May 2017 and only for entities that hold an LEI. CRSP PERMNO/PERMCO remain the standard permanent US security identifiers, under institutional licence (RQ2.1). (2) **Ownership and insiders.** The SEC publishes as-filed 13F holdings (from 2013 Q2) and Forms 3/4/5 insider filings (from 2006 Q1) as free quarterly extracts. Being as-filed, they carry filing dates, so knowledge time can be rebuilt (project reading). FactSet Ownership is the paid alternative. (3) **Customers and suppliers.** Compustat Historical Segments (from 1976) lists only customers above 10% of revenue: about a thousand links a year, with customer names as free text. FactSet Revere (from 2003) has relationship start and end dates and weekly updates, but against complete administrative networks it misses most links (mean degree under 10, against about 40) and biases binary network statistics (Bacilieri 2023, Moderate). Weighted quantities are much less affected. LLM extraction from web text can add many links (9.3 times more than a disclosure database in China), but its precision is unmeasured (Fukada 2026, Weak). (4) **Boards.** BoardEx (from 1999, more than 20,000 North American firms) is paid and academic-only through WRDS. SEC insider filings are a partial free substitute. (5) **Subsidiaries.** 10-K Exhibit 21 lists subsidiaries through EDGAR, but the rule text (Regulation S-K Item 601(b)(21)) could not be opened, so its omission rules are unconfirmed. **Restrictions.** Every paid source read (Compustat, FactSet, BoardEx through WRDS) is licensed for academic, non-commercial research only.

**Confidence:** Medium on what exists, its cost and its licences. Medium on coverage bias, which rests on one strong comparison (Bacilieri 2023). Low on point-in-time quality: no source documents knowledge time for relationship records.

| Source | What | History | Point-in-time? | Cost / licence | Sources |
| --- | --- | --- | --- | --- | --- |
| OpenFIGI | Security identifiers and mapping | Not stated | Current mappings; delisted on request | Free API | [[OpenFIGI 2026 API Documentation]] |
| GLEIF LEI Level 2 | Legal entities, direct and ultimate parents | Parents from May 2017 | Golden copy and delta files (history depth not read) | Free; website data CC0 | [[GLEIF 2026 Level 2 Who Owns Whom]] |
| CRSP | Permanent security and company IDs (PERMNO, PERMCO) | About 100 years | Dated identifier history | Institutional licence | [[CRSP 2026 US Stock Databases]] |
| SEC 13F data sets | Institutional holdings | 2013 Q2 onward | As-filed (filing dates) | Free | [[SEC 2026 Form 13F Data Sets]] |
| SEC insider data sets | Insider and 10% holder transactions | 2006 Q1 onward | As-filed | Free | [[SEC 2026 Insider Transactions Data Sets]] |
| Compustat Historical Segments | Major customers (10% rule), segments | 1976 onward | Fiscal-year disclosures; names need matching | Academic, through WRDS | [[Compustat 2026 Historical Segments Customers]], [[Cohen 2008 Economic Links Predictable Returns]], [[Barrot 2016 Input Specificity Shock Propagation]] |
| FactSet Revere | Customers, suppliers, partners, competitors | 2003 onward | Start and end dates (valid time); knowledge time not stated | Subscription; academic copies non-commercial | [[FactSet 2026 Revere Supply Chain Relationships]], [[Bacilieri 2023 Firm-level Production Networks]] |
| BoardEx | Directors, executives, networks | 1999 onward | Not stated | Subscription; academic copies non-commercial | [[BoardEx 2026 North America Data Guide]] |
| Web extraction (LLM) | Supplier-customer links from web text | Single snapshot | Retrieval timestamps only | Search API and LLM cost | [[Fukada 2026 Snippet-Driven Supply Chain Discovery]] |

**What would change the answer:** the Item 601(b)(21) text and an Exhibit 21 dataset; FactSet or BoardEx documentation of when each record was entered; a precision study of LLM-extracted supply-chain links against filings; LSEG, Orbis, Wikidata or OpenCorporates terms and coverage.

**Stop rule:** 13 sources (7 primary documentation, 2 scored: 1 Moderate, 1 Weak; plus Cohen 2008, Barrot 2016, CRSP and the SEC EDGAR note reused). Not fully met: the last three sources (BoardEx, Bacilieri, Fukada) each added something. Top-up list: Item 601(b)(21); Ellis, Fee & Thomas (2012) on withheld customer names; Orbis; Wikidata; OpenCorporates; Bloomberg SPLC.

### RQ2.9 – Which sources cover geopolitical, natural-hazard, infrastructure and shipping events (for example GDELT, ACLED, USGS, NOAA, AIS ship tracking)? Compare timestamp quality, latency, history, cost and licence

**Answer.** The free, fast sources are the government ones. GDELT is also free and fast, but it is opaque, and ACLED forbids training on its data. (1) **Natural hazards.** USGS earthquake feeds update every minute, and each event carries `time` and `updated` fields. Events are revised after publication, so an archive must keep every version to stay point-in-time (project reading). The data are US public domain. NOAA's Storm Events Database reaches back to 1950, but its event types change by period (tornadoes only until 1954; 48 types from 1996). At access it ran only to May 2026, a lag of about five to six months, so it suits backtests but not early warning. (2) **Geopolitics and news events.** GDELT 2.0 publishes events and the Global Knowledge Graph every 15 minutes, free for any use with citation (RQ2.2). Two independent checks qualify it. Its coding software is not public, a reconstruction matched its tone and entity fields only moderately, and 11 of 432 sampled 15-minute archives (2.5%) were missing (Klimin 2026, Moderate). Its news sources overlap little with Common Crawl News (5.4% of domains shared), so "global news" coverage depends on the collector (El Ouadi 2026, Weak). ACLED requires a corporate licence for commercial users, bans use as "training data, embeddings, or knowledge-base input" without written consent, and requires deletion at termination. (3) **Shipping.** MarineCadastre publishes US Coast Guard AIS positions for US waters from 2009 under CC0, with daily point files and monthly tracks, released months after the fact. Global or near-real-time AIS needs commercial providers (Spire, Kpler, MarineTraffic) whose terms were not read. (4) **Infrastructure.** No dedicated source (power grid, ports, cables, cloud outages) was read this session. Evidence on infrastructure events is thin.

**Confidence:** Medium on history, cost and licence (official pages). Low on timestamp quality and latency: only USGS gives a stated update cadence, and none of the sources publishes measured latency from event to record.

| Source | Events | History | Latency / update | Timestamp notes | Cost / licence | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| USGS earthquake feeds | Earthquakes worldwide | Feeds: last 30 days (catalogue not read) | Updated every minute | `time` plus `updated`; events revised | Free; US public domain | [[USGS 2026 Earthquake Feeds and Public Domain]] |
| NOAA Storm Events | US storms, 48 types from 1996 | 1950 onward | About 5–6 months behind (inferred) | Event types and procedures change by period | Free (terms not read) | [[NOAA 2026 Storm Events Database]] |
| GDELT 2.0 | Machine-coded news events (CAMEO), GKG | Events 1979 (1.0); GKG 2013 | 15-minute files; about 2.5% of archives missing | Publication and processing times; coding software closed | Free for any use, with citation | [[GDELT 2026 Data and Terms of Use]], [[Klimin 2026 Reconstructed vs Native GDELT GKG]], [[El Ouadi 2026 Common Crawl News vs GDELT]] |
| ACLED | Political violence and protest | Not read | Not read | Not read | Non-commercial; corporate licence for firms; **no model training** without consent | [[ACLED 2026 End User Licence Agreement]] |
| MarineCadastre AIS | Vessel positions, US waters | 2009 onward | Months behind; daily and monthly files | AIS broadcast times | Free; CC0 | [[MarineCadastre 2026 AIS Vessel Traffic]] |
| Commercial AIS (Spire, Kpler, MarineTraffic) | Global vessel positions | – | Near real time (claimed; not read) | – | Paid; terms not read | – |

**What would change the answer:** the USGS life-cycle (revision) policy and catalogue history; ACLED's update cadence and coverage pages; a measured event-to-record latency study for GDELT; commercial AIS terms; an infrastructure-outage source.

**Stop rule:** 7 sources (4 new primary documentation, 2 scored: 1 Moderate, 1 Weak; GDELT note reused). Not met: fewer than five scored or new sources per event type, so the evidence on infrastructure events and on latency is thin. Top-up list: USGS ComCat and life-cycle policy; ACLED coverage and FAQ; Ward et al. (2013) GDELT vs ICEWS; Kwak & An (2016) GDELT vs EventRegistry; Spire or Kpler AIS terms; GDACS; NOAA NCEI billion-dollar disasters.

## Cross-cutting observations

- **Licence terms decide more than price or quality.** Training is explicitly banned by FRED/ALFRED, Massive, X (for foundation models) and ACLED, and is not mentioned by Alpaca, Alpha Vantage or EODHD. The sources that clearly allow storage and training are government or open ones: EDGAR, BLS, USGS, GDELT, GLEIF and MarineCadastre AIS (RQ2.2, RQ2.3, RQ2.6, RQ2.8, RQ2.9).
- **Knowledge time is almost never recorded by the source.** Price vendors, FactSet relationships, Compustat customers, NOAA events and USGS revisions all describe when something was true, or show only the latest state. The fetch-once design (RQ2.4) therefore has to stamp its own retrieval time and keep every version (RQ2.5) if backtests are to be free of look-ahead. The as-filed SEC data sets are the exception (RQ2.8).
- **Independent quality evidence is scarce across every modality.** Data quality is documented independently only for CRSP (Liu 2020), Alpha Vantage adjusted prices (one informal check), FactSet supply chains (Bacilieri 2023) and GDELT (Klimin 2026; El Ouadi 2026). Everything else rests on vendor claims (RQ2.1, RQ2.7, RQ2.8, RQ2.9).
- **Coverage gaps bias network and event features in known directions.** FactSet and Compustat under-count links, and the 10% customer rule skews which links are seen. GDELT and Common Crawl see largely different outlets. Features built on these sources inherit those biases (RQ2.8, RQ2.9, RP1 RQ1.4).
- **Evidence by type.** 80 sources: 65 primary documentation, 15 scored (1 Strong, 8 Moderate, 6 Weak). The scored sources are mostly data-quality and systems benchmarks, not forecasting studies, so the rubric's out-of-sample, point-in-time and costs checks were mostly N/A.

## Contradictions and evidence gaps

- **Databento history:** the pricing page says 16+ years of L0, while the equities catalog says 8 years (RQ2.1; catalog taken).
- **Twelve Data credits:** its own pricing cards and comparison table disagree (RQ2.7).
- **Nguyen 2026 (graph engines):** Ladybug figures differ between Table 1 and Appendix A.1 (RQ2.5).
- **Rogers 2017 (EDGAR lead):** two summaries report different average lead times (RQ2.2).
- **Gaps:** independent benchmarks of embedded storage engines on market data (RQ2.5); retail-API accuracy against CRSP and outage histories (RQ2.7); Reddit, X Developer Policy, Tiingo and Databento licensing terms (RQ2.2, RQ2.6); Exhibit 21 rules (RQ2.8); infrastructure-event sources and measured event latency (RQ2.9); EU text-and-data-mining law (RQ2.6). The top-up lists are in each RQ's stop-rule line.

## Assumptions made during the research

- Prices and limits are as shown on the vendors' public pages on the access date; they change often and are not quotes.
- Evidence for RP2 is mostly vendor documentation, which states what a vendor offers, not how well it works; data-quality claims are flagged as vendor claims unless an independent source confirms them.
- The Exa search tools were not connected in this session (session 17); built-in web search and page fetch were used instead, as the guide's fallback. No alphaXiv search was run for RQ2.1 because the evidence is vendor pages, not papers.
- RQ2.1: where a vendor page did not state delisted coverage, the provider is marked "not stated/confirmed", not "no". Alpha Vantage LISTING_STATUS could not be read (the page fetch truncated before that section).
- RQ2.1: Databento's pricing page gives "16+ years" for L0 history but the equities catalog says "8 years" and the roadmap says daily backfill to 2010 is in progress; the catalog and roadmap are taken as the equities-specific figures.
- Paper-critique (session 19) was run on the full draft. Fixes: source counts recounted from lit-note properties (80, not 78); three abstract claims narrowed (delisted coverage, licence vs copyright, hazard-feed speed) and the RQ2.7 confidence added; stale X rows updated from the Developer Agreement read under RQ2.6. Scorecard arithmetic and all four sensitivity claims were recomputed and hold.
- Citation check (session 19), using the reference-lookup tools (OpenAlex, arXiv) for the 17 scholarly entries and page fetch for a sample of vendor pages: 16 of 17 scholarly references verified (Lyle 2024 is not indexed in OpenAlex; its authors' PDF was opened and matches); two titles completed (Nguyen 2026, Lu 2026) and published DOIs added (Lu 2026, Fukada 2026, Jensen 1995). Support: Lyle 2024's sign-flip figure corrected (9–14% → about 9–10% for earnings changes; 14% was sales); EDGAR's next-day rule given its 10 p.m. Forms 3/4/5 cutoff. The six licence and limit pages behind the main claims (FRED, Massive, ACLED, X, GDELT, SEC EDGAR) were re-opened on 2026-11-08 and support the text. The other 59 primary-documentation pages were opened in sessions 17–18 (accessed dates in their lit notes) and were not re-fetched; no orphans either way (80 references, 80 linked lit notes).
- Decided unattended (session 19): the RQ2.2, RQ2.3, RQ2.8 and RQ2.9 top-up lists were not worked before final. They are evidence gaps (see each stop-rule line and Contradictions and evidence gaps), not blockers, following the RP1 precedent for flagged gaps.
- RQ2.1: Massive's "Massive vs Databento" page is a vendor comparison; only Massive's statements about itself were used, and its trades/quotes-from-2003 claim is marked unverified.

- RQ2.2: the Reddit Data API Terms page was blocked to the fetch tool; Reddit's training and deletion rules are marked unconfirmed rather than assumed.
- RQ2.2: the guide's seeds for X (PostProxy summary) and GDELT (Aalto DataHub) were replaced by the providers' own pages, which take precedence.
- RQ2.2: Rogers et al. (2017) was read from a university summary and the abstract (journal closed); the two summaries report different lead figures (18 s average vs 30 s vs 40 s means), both recorded.
- RQ2.3: the FRED/ALFRED AI-training and storage prohibitions are reported as read on 2026-11-08 through a summarising fetch tool (verbatim fragments checked twice); this is a reading of terms, not legal advice.
- RQ2.3: Croushore (2011) is a survey; it is scored on the rubric as written (Strong), but it is evidence that vintages matter, not a test of any method.
- RQ2.4: the "request ledger" pattern is the project's transfer of AWS's server-side idempotency design to a client; no source documents it for market-data APIs. A Microsoft data-lake-zones page was opened but held no zone guidance and was not kept.
- RQ2.5: the rubric is written for forecasting studies; for database benchmarks the out-of-sample, point-in-time and costs checks were marked N/A and the total scaled to 14 from the remaining checks.
- RQ2.5: Jensen, Snodgrass & Soo (1995) is a conceptual standard reference (definitions of valid and transaction time), so it is marked Primary documentation rather than scored.
- RQ2.5: Lu et al. (2026) was read from alphaXiv's structured report rather than the full text; Barez (2023), Mostafa (2026) and Nguyen (2026) were read in full text.
- RQ2.5: Nguyen et al. (2026) is written by the vendor of the system it tests, and its Ladybug figures differ between Table 1 and Appendix A.1. It is cited for the pattern (query shape matters more than the graph label; ingest cost dominates), not for its numbers.
- RQ2.5: licences for DuckDB, pgvector, LanceDB, SurrealDB, MongoDB, RocksDB and XTDB were not stated on the pages read and are marked "not confirmed" rather than filled in from memory.
- RQ2.6: licence terms were read through a summarising fetch tool; clause numbers and short quotes come from that reading and should be checked against the documents before any reliance. This is a reading of terms, not legal advice.
- RQ2.6: where terms are silent on model training (Alpaca, Alpha Vantage, EODHD), the answer is recorded as "not mentioned", not as permission.
- RQ2.6: the Copyright Office report's fair-use conclusions were read through a law-firm summary (Lowenstein Sandler), because the fetch tool stopped before that section of the report. The report's own pages 1-33 were opened.
- RQ2.6: the Alpaca Terms PDF shows no date and may not be the current version. Massive's Businesses Terms, X's Developer Policy, the Tiingo terms (the page failed to load) and Databento's licensing page (it failed to load) were not read.
- RQ2.6: only US law was considered (the user's location); EU text-and-data-mining rules were not read.
- RQ2.7: the scorecard weights were proposed by this session (unattended) from the project's needs (point-in-time research data, model training). Delisted coverage and licence carry the most weight; an explicit training ban is a dealbreaker. The user can change the weights and the matrix can be rescored.
- RQ2.7: where a vendor page was silent, the cell is scored 2 (or 3 for quality and outages, marked *g*) as a guess, not a finding. This favours vendors with fuller documentation.
- RQ2.7: Alpaca's status and uptime pages load their data dynamically, so no outage history could be read for any vendor. The author of the Alpha Vantage–CRSP check is named on the page only as "Giulio".
- RQ2.8: FactSet, Compustat Segments and BoardEx were described from university library and WRDS pages, not vendor manuals. Prices are not public.
- RQ2.8: the eCFR page for Regulation S-K Item 601 refused the fetch tool (robots), so Exhibit 21's omission rules are unconfirmed.
- RQ2.8: Bacilieri et al. was read in the 2023 INET working-paper version; the 2025 revision and the 2026 JEDC version were not opened.
- RQ2.9: NOAA Storm Events lag is inferred from the coverage end date shown at access (May 2026 on 2026-11-08), not from a stated policy.
- RQ2.9: the ACLED terms page only links to the EULA, which was opened; ACLED coverage and update pages were not read. The MarineCadastre AIS page lists 2009–2023, and the project's GitHub repository adds 2024–2025 files; both were read.
- RQ2.9: no infrastructure-event source was searched, because of session length. It is recorded as an evidence gap, not as "none exist".

## Open questions for the methodology plan

- Which request identity (endpoint + normalised parameters + vendor + licence) keys the request ledger, and how are vendor revisions to already-fetched history detected (re-fetch sample, checksums)? (RQ2.4)
- Given FRED's AI-training prohibition, where will macro vintages come from: the Philadelphia Fed files, agency release archives kept by the project, or written permission from the St. Louis Fed? (RQ2.3)
- Which layer gives knowledge-time (as-known) reads: a version-per-write store (ArcticDB, LanceDB), explicit bitemporal tables (XTDB-style or hand-built in Postgres/DuckDB), or dated Parquet partitions? (RQ2.5, RQ3.8)
- Does ArcticDB's BSL "production use" restriction apply to a solo research project, or should an Apache/MIT-licensed engine be preferred? (RQ2.5, RQ2.6)
- Embeddings: Postgres + pgvector beside the relational data, or a separate embedded store (LanceDB) with tagged versions? pgvector indexes `vector` columns only up to 2,000 dimensions, so the sentiment module's unreduced 3,080-value embedding could not be indexed there; its PCA-reduced 264 features could (project doc `sentiment-module-design.md`). (RQ2.5)
- If the main price vendor's terms ban or stay silent on model training, does the project seek written permission, switch vendor, or train only on sources that allow it (EDGAR, BLS, GDELT, own-collected data)? (RQ2.6)
- Is the planned model a "foundation or frontier model" under the X agreement, and can deletion duties be met in a point-in-time archive? (RQ2.6, RQ3.8)
- Which vendor goes first in a trial: Alpaca (cheapest, adjustment options) or Databento (tick depth, bulk files), and which survivorship-free daily reference sits beside it? (RQ2.7, RQ2.1)
- Relationship data (FactSet start/end dates, Compustat customers) give valid time only. How will knowledge time be assigned (filing date, or a lag rule) to avoid look-ahead? (RQ2.8, RQ3.7, RQ3.8)
- For shock detection, which event feeds are fast enough (USGS, GDELT) and which only label history (NOAA Storm Events, MarineCadastre AIS)? Does each event archive need to keep every revision? (RQ2.9, RQ3.8)

## Facts that need a vendor quote or a trial account

- Delisted-symbol coverage and history for Alpaca, Alpha Vantage (LISTING_STATUS), EODHD, Tiingo and Databento (RQ2.1).
- Bulk prices for Tick Data US equities and the FirstRate Data complete intraday bundle (RQ2.1).
- Databento per-GB rates for US equities L1/L0 history, and the price of its corporate-actions and adjustment-factor datasets (RQ2.1).
- Massive flat-file (bulk) access and per-plan call limits; whether Massive bars can be dividend-adjusted (RQ2.1).
- Tiingo IEX intraday history start (RQ2.1).
- Benzinga and RavenPack news: price, archive start, storage and model-training rights (RQ2.2).
- StockTwits historical data licence (RQ2.2).
- X: whether a private, non-generative forecasting model counts as a "foundation or frontier model" under the Developer Agreement, and the Developer Policy terms on storing posts (RQ2.2, RQ2.6).
- St. Louis Fed: whether FRED-MD/QD research files and ALFRED vintages may be stored and used to train a forecasting model (RQ2.3); Philadelphia Fed RTDSM licence (RQ2.3).
- ArcticDB: whether research-only use counts as "production use" under BSL 1.1, and the price of a commercial licence (RQ2.5).
- Alpaca, Alpha Vantage, EODHD and Massive: written confirmation of whether storing history and training a private research model is allowed, and at what tier (RQ2.6).
- Databento: the per-dataset licence terms for US equities history, and whether model training is restricted (RQ2.6).
- Alpaca, Databento and EODHD: delisted-symbol coverage, flat-file/bulk options, per-plan rate limits and outage history (RQ2.7).
- Massive: written permission to train a private research model (would change the RQ2.7 ranking).
- FactSet Revere and BoardEx: commercial (non-academic) price and whether each record carries an entry date (RQ2.8).
- ACLED: corporate licence price and whether training a private research model can be approved (RQ2.9).
- Commercial AIS (Spire, Kpler, MarineTraffic): history, latency, price and training rights (RQ2.9).

## References

- Alpaca (2026). Market Data API: About; Historical bars. https://docs.alpaca.markets/docs/about-market-data-api – [[Alpaca 2026 Market Data API Stocks]]
- Alpha Vantage (2026). Premium plans; API documentation. https://www.alphavantage.co/premium/ – [[Alpha Vantage 2026 Premium Plans and Time Series]]
- CRSP / Morningstar (2026). CRSP US Stock Databases. https://indexes.morningstar.com/research-data-products/crsp-us-stock-databases – [[CRSP 2026 US Stock Databases]]
- Databento (2026). US equities catalog; Pricing; Product roadmap. https://databento.com/catalog/us-equities – [[Databento 2026 US Equities Data and Pricing]]
- EODHD (2026). Pricing. https://eodhd.com/pricing – [[EODHD 2026 Pricing and Data Coverage]]
- FirstRate Data (2026). Complete historical intraday US stocks. https://firstratedata.com/b/22/stock-complete-historical-intraday – [[FirstRate Data 2026 Complete Intraday Stocks]]
- Liu, G. (2020). Data Quality Problems Troubling Business and Financial Researchers: A Literature Review and Synthetic Analysis. Journal of Business & Finance Librarianship. doi:10.1080/08963568.2020.1847555 – [[Liu 2020 Data Quality Problems Finance Databases]]
- Massive (2026). Stocks API: Custom bars; All tickers; Pricing. https://massive.com/docs/rest/stocks/aggregates/custom-bars – [[Massive 2026 Stocks API Plans and History]]
- Norgate Data (2026). Stock market packages; Data content tables. https://norgatedata.com/stockmarketpackages.php – [[Norgate 2026 US Stocks Packages and Delisted Data]]
- Tick Data LLC (2026). U.S. Equities. https://tickdata.com/product/us-equities – [[Tick Data 2026 US Equities Historical]]
- Tiingo (2026). Pricing; IEX API documentation. https://www.tiingo.com/about/pricing – [[Tiingo 2026 Pricing and IEX API]]
- Alpaca (2026). Historical news data. https://docs.alpaca.markets/docs/historical-news-data – [[Alpaca 2026 Historical News API]]
- arXiv (2026). API Terms of Use. https://info.arxiv.org/help/api/tou.html – [[arXiv 2026 API Terms of Use]]
- Benzinga (2026). Stock News API. https://www.benzinga.com/apis/en-ca/cloud-product/stock-news-api/ – [[Benzinga 2026 Stock News API]]
- GDELT Project (2026). Data; About. https://www.gdeltproject.org/data.html – [[GDELT 2026 Data and Terms of Use]]
- Imperial College London Library (2026). RavenPack News Analytics. https://www.imperial.ac.uk/admin-services/library/subject-support/business/ravenpack-news-analytics/ – [[RavenPack 2026 News Analytics Library Guide]]
- OpenAlex (2026). Authentication. https://help.openalex.org/api/authentication/ – [[OpenAlex 2026 API Authentication and Limits]]
- Reddit (2026). Reddit Data API Wiki. https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki – [[Reddit 2026 Data API Wiki]]
- Rogers, J. L., Skinner, D. J., & Zechman, S. L. C. (2017). Run EDGAR Run: SEC Dissemination in a High-Frequency World. Journal of Accounting Research 55(2), 459–505. doi:10.1111/1475-679X.12167 – [[Rogers 2017 Run EDGAR Run SEC Dissemination]]
- SEC (2026). Accessing EDGAR Data. https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data – [[SEC 2026 Accessing EDGAR Data]]
- StockTwits (2026). Terms of Service (revised 2026-07-10). https://www.stocktwits.com/about/legal/terms – [[StockTwits 2026 Terms of Service]]
- X Corp. (2026). X API pricing; Search Posts introduction. https://docs.x.com/x-api/getting-started/pricing – [[X 2026 API Pricing and Search]]
- BLS (2026). Copyright information. https://www.bls.gov/opub/copyright-information.htm – [[BLS 2026 Copyright Information]]
- Croushore, D. (2011). Frontiers of Real-Time Data Analysis. Journal of Economic Literature 49(1), 72–100. doi:10.1257/jel.49.1.72 – [[Croushore 2011 Frontiers of Real-Time Data Analysis]]
- Federal Reserve Bank of Philadelphia (2026). Real-Time Data Set for Macroeconomists. https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/real-time-data-set-for-macroeconomists – [[Philadelphia Fed 2026 Real-Time Data Set]]
- Federal Reserve Bank of St. Louis (2026). ALFRED; FRED API real-time periods. https://alfred.stlouisfed.org/ – [[ALFRED 2026 Real-Time Vintages and FRED API]]
- Federal Reserve Bank of St. Louis (2026). FRED Legal. https://fred.stlouisfed.org/legal/ – [[FRED 2026 Legal Terms of Use]]
- Lyle, M., Siano, F., & Yohn, T. L. (2024). Re-Standardized Financial Statement Data. Working paper. https://som.yale.edu/sites/default/files/2024-07/Re-Standardized%20Financial%20Statement%20Data.pdf – [[Lyle 2024 Re-Standardized Financial Statement Data]]
- McCracken, M. W. (2026). FRED-MD and FRED-QD. https://www.stlouisfed.org/research/economists/mccracken/fred-databases – [[McCracken 2026 FRED-MD FRED-QD Databases]]
- Airbyte (2026). Incremental sync – append + deduped. https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped – [[Airbyte 2026 Incremental Append Deduped]]
- Databricks (2026). What is the medallion lakehouse architecture? https://docs.databricks.com/aws/en/lakehouse/medallion – [[Databricks 2026 Medallion Architecture]]
- dltHub (2026). Incremental loading. https://dlthub.com/docs/general-usage/incremental-loading – [[dltHub 2026 Incremental Loading]]
- Featonby, M. (n.d., accessed 2026-11-08). Making retries safe with idempotent APIs. Amazon Builders' Library. https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/ – [[Featonby 2026 Idempotent APIs Builders Library]]
- Fielding, R., Nottingham, M., & Reschke, J. (2022). RFC 9111: HTTP Caching. IETF. https://www.rfc-editor.org/rfc/rfc9111.html – [[IETF 2022 RFC 9111 HTTP Caching]]
- Hishel (2026). Hishel. https://hishel.com/ – [[Hishel 2026 HTTP Caching Library]]
- IETF httpapi WG (2026). RateLimit header fields for HTTP, draft-ietf-httpapi-ratelimit-headers-11. https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ – [[IETF 2026 RateLimit Header Fields Draft]]
- requests-cache (2026). Expiration. https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html – [[requests-cache 2026 Expiration Guide]]
- Barez, F., Bilokon, P., & Xiong, R. (2023). Benchmarking Specialized Databases for High-frequency Data. arXiv:2301.12561. https://arxiv.org/abs/2301.12561 – [[Barez 2023 Benchmarking Databases High-frequency Data]]
- DuckDB Foundation (2026). Reading and Writing Parquet Files. https://duckdb.org/docs/2.0/data/parquet/overview.html – [[DuckDB 2026 Parquet Read and Write]]
- Jensen, C. S., Snodgrass, R. T., & Soo, M. D. (1995). The TSQL2 Data Model. In R. T. Snodgrass (Ed.), The TSQL2 Temporal Query Language (pp. 361–395). Kluwer. doi:10.1007/978-1-4615-2289-8_10. https://homes.cs.aau.dk/~csj/Thesis/pdf/chapter12.pdf – [[Jensen 1995 TSQL2 Data Model]]
- JUXT (2026). Time in XTDB. https://docs.xtdb.com/about/time-in-xtdb.html – [[XTDB 2026 Time in XTDB Bitemporal]]
- LanceDB (2026). Table management: versioning. https://docs.lancedb.com/management/table.md – [[LanceDB 2026 Table Versioning and Time Travel]]
- Lu, D., Caminal, H., Chatzakis, M., Papakonstantinou, Y., Chronis, Y., Jain, V., & Özcan, F. (2026). An In-Depth Study of Filter-Agnostic Vector Search on a PostgreSQL Database System [Experiments & Analysis]. arXiv:2603.23710; published version doi:10.1145/3802011. https://arxiv.org/abs/2603.23710 – [[Lu 2026 Filtered Vector Search PostgreSQL]]
- Man Group (2026). ArcticDB FAQ; Library API; GitHub README (licence). https://docs.arcticdb.io/latest/faq/ – [[ArcticDB 2026 FAQ and Licence]]
- Meta Platforms (2026). RocksDB Overview. https://github.com/facebook/rocksdb/wiki/RocksDB-Overview – [[RocksDB 2026 Overview]]
- MongoDB (2026). Time Series Collection Limitations. https://www.mongodb.com/docs/manual/core/timeseries/timeseries-limitations/ – [[MongoDB 2026 Time Series Collection Limitations]]
- Mostafa, J., Melissano, S., Tan Jerome, N., Chilingaryan, S., & Kopmann, A. (2026). Six Dimensions of Benchmarking Time-Series Databases. arXiv:2608.01459. https://arxiv.org/abs/2608.01459 – [[Mostafa 2026 Six Dimensions Benchmarking TSDBs]]
- Nguyen, D., Gill, G., Ahmadi, H., & Rossbach, C. J. (2026). Graph Memory for LLM Agents: At What Cost? A Comparative Evaluation of Query, Ingest, and Update Performance Across Graph Database Engines. arXiv:2609.23315. https://arxiv.org/abs/2609.23315 – [[Nguyen 2026 Graph Database Engines Cost]]
- pgvector contributors (2026). pgvector. https://github.com/pgvector/pgvector – [[pgvector 2026 Postgres Vector Search]]
- QuestDB (2026). ASOF JOIN; Deduplication; GitHub README. https://questdb.com/docs/reference/sql/asof-join/ – [[QuestDB 2026 ASOF Join and Deduplication]]
- SurrealDB (2026). Architecture; SELECT statement. https://surrealdb.com/docs/surrealdb/introduction/architecture – [[SurrealDB 2026 Architecture and Versioned Queries]]
- Tiger Data (2026). TimescaleDB editions. https://www.tigerdata.com/docs/get-started/choose-your-path/timescaledb-editions – [[Tiger Data 2026 TimescaleDB Editions]]
- AlpacaDB (2026). Terms and Conditions; Can I redistribute Alpaca API data? https://files.alpaca.markets/disclosures/library/TermsAndConditions.pdf – [[Alpaca 2026 Terms and Conditions Market Data]]
- Alpha Vantage (2026). Terms of Service. https://www.alphavantage.co/terms_of_service/ – [[Alpha Vantage 2026 Terms of Service]]
- EODHD (2026). Terms and Conditions. https://eodhd.com/financial-apis/terms-conditions – [[EODHD 2026 Terms and Conditions]]
- Massive.com (2025). Market Data Terms of Service (updated 2025-08-28). https://massive.com/legal/market-data-terms-of-service – [[Massive 2025 Market Data Terms of Service]]
- Nasdaq (2026). NASDAQ OMX Global Subscriber Agreement (copy hosted by Alpaca). https://files.alpaca.markets/disclosures/library/NASDAQ+OMX+Global+Subscriber+Agreement.pdf – [[Nasdaq 2026 Global Subscriber Agreement]]
- U.S. Copyright Office (2025). Copyright and Artificial Intelligence, Part 3: Generative AI Training (pre-publication version). https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf – [[US Copyright Office 2025 Generative AI Training Report]]
- X Corp. (2026). Developer Agreement. https://docs.x.com/developer-terms/agreement – [[X 2026 Developer Agreement]]
- AlpacaDB (2026). alpaca-py. https://github.com/alpacahq/alpaca-py – [[Alpaca 2026 alpaca-py SDK]]
- Databento (2026). databento-python. https://github.com/databento/databento-python – [[Databento 2026 Python Client]]
- Giulio (surname not stated) (2025). Download historical data using Alpha Vantage. Sant'Anna School of Advanced Studies. https://www.cafed.santannapisa.it/~giulio/other/alpha_vantage/index.html – [[Giulio 2025 Alpha Vantage Adjusted Close vs CRSP]]
- Twelve Data (2026). Pricing. https://twelvedata.com/pricing – [[Twelve Data 2026 Pricing]]
- Bacilieri, A., Borsos, A., Astudillo-Estevez, P., & Lafond, F. (2023). Firm-level production networks: what do we (really) know? INET Oxford Working Paper 2023-08. https://oms-inet.files.svdcdn.com/staging/files/Firm-level-production-networks-what-do-we-really-know.pdf – [[Bacilieri 2023 Firm-level Production Networks]]
- BoardEx (2026). BoardEx North America (Aalto University data hub). https://datahub.aalto.fi/en/data-sources/boardex-north-america – [[BoardEx 2026 North America Data Guide]]
- Cohen, L., & Frazzini, A. (2008). Economic Links and Predictable Returns. Journal of Finance 63(4), 1977–2011. doi:10.1111/j.1540-6261.2008.01379.x – [[Cohen 2008 Economic Links Predictable Returns]]
- Barrot, J.-N., & Sauvagnat, J. (2016). Input Specificity and the Propagation of Idiosyncratic Shocks in Production Networks. Quarterly Journal of Economics 131(3), 1543–1592. doi:10.1093/qje/qjw018 – [[Barrot 2016 Input Specificity Shock Propagation]]
- FactSet (2026). FactSet on WRDS; FactSet Supply Chain Relationships (Aalto data hub). https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/factset/ – [[FactSet 2026 Revere Supply Chain Relationships]]
- Fukada, H., & Mizuno, T. (2026). Snippet-Driven Supply Chain Discovery with LLMs: Scaling Visibility in China. arXiv:2605.27845; IEEE CIFEr 2026, doi:10.1109/CIFEr67845.2026.11692384. https://arxiv.org/abs/2605.27845 – [[Fukada 2026 Snippet-Driven Supply Chain Discovery]]
- GLEIF (2026). Level 2 data: who owns whom; Open data. https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-2-data-who-owns-whom – [[GLEIF 2026 Level 2 Who Owns Whom]]
- OpenFIGI (2026). API documentation. https://www.openfigi.com/api/documentation – [[OpenFIGI 2026 API Documentation]]
- S&P Global Market Intelligence (2026). Compustat (Aalto University data hub). https://datahub.aalto.fi/en/data-sources/compustat – [[Compustat 2026 Historical Segments Customers]]
- SEC (2026). Form 13F data sets. https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets – [[SEC 2026 Form 13F Data Sets]]
- SEC (2026). Insider transactions data sets. https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets – [[SEC 2026 Insider Transactions Data Sets]]
- ACLED (2026). End User Licence Agreement. https://acleddata.com/eula – [[ACLED 2026 End User Licence Agreement]]
- El Ouadi, A., & Beskow, D. (2026). Comparison of Common Crawl News & GDELT. arXiv:2610.00587. https://arxiv.org/abs/2610.00587 – [[El Ouadi 2026 Common Crawl News vs GDELT]]
- Klimin, N. A. (2026). Agreement Between Reconstructed and Native GDELT GKG Records: A Field-Level Baseline. arXiv:2610.35358. https://arxiv.org/abs/2610.35358 – [[Klimin 2026 Reconstructed vs Native GDELT GKG]]
- NOAA Office for Coastal Management & BOEM (2026). MarineCadastre AIS vessel traffic; ocm-marinecadastre/ais-vessel-traffic. https://marinecadastre.gov/ais – [[MarineCadastre 2026 AIS Vessel Traffic]]
- NOAA NCEI (2026). Storm Events Database: details. https://www.ncei.noaa.gov/stormevents/details.jsp – [[NOAA 2026 Storm Events Database]]
- U.S. Geological Survey (2026). Real-time earthquake GeoJSON feeds; Copyrights and credits. https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php – [[USGS 2026 Earthquake Feeds and Public Domain]]
