---
type: evidence-register
updated: 2026-11-09
tags: [evidence-register]
---
# Evidence Register

One row per source. A live view over lit-note properties is in [[Evidence Register.base]].

| Source | Paper | Family | Score | Finding |
| --- | --- | --- | --- | --- |
| [[Fentazi 2026 Delay-Aware Audit Test-Time Adaptation]] | RP4, RP5 | evaluation | Strong (12) | With labels released only after maturity, four published test-time adapters gain ≤0.5% over frozen on 4 of 5 streams; leaky updates inflate gains up to 110% (non-finance) |
| [[Dasari 2026 When to Retrain Drift Policies]] | RP4, RP5 | evaluation | Strong (10) | Periodic retraining beats error-threshold and ADWIN triggers by 8.6–16 pp under abrupt/gradual drift; with incremental updates no policy beats never retraining (non-finance) |
| [[Fujimoto 2026 Leakage-Free Online Adaptation Edge]] | RP4, RP5 | evaluation | Moderate (9) | Baseline warmup budget alone moves measured adaptation benefit 3–19 pp; validation-slice selection of warmup and learning rate fixes most of it (non-finance) |
| [[Zhao 2025 PROCEED Proactive Drift Adaptation]] | RP4 | price-time-series | Moderate (8) | Correct H-step label delay raises earlier online forecasters' MSE by 107% on average; drift-aware parameter shifts beat online GD (non-finance) |
| [[Dai 2026 ORCA Black-Box TSFM Adaptation]] | RP4 | price-time-series | Moderate (8) | Residual adapter on input + frozen TSFM forecast cuts MSE 6.3%; ported white/grey-box adapters worsen it; 0% gain on exchange rates |
| [[Lian 2026 DPAL Financial Test-Time Adaptation]] | RP4 | price-time-series | Moderate (6) | Direction and price-path terms in the TTA loss lower price MSE on US equity panels 2023–25; no random-walk baseline |
| [[Karaouli 2025 Catastrophic Forgetting TSFMs Continual]] | RP4 | price-time-series | Moderate (6) | Sequential fine-tuning always causes forgetting (larger TSFMs less); experience replay removes most of it (non-finance) |
| [[Capponi 2025 Nonstationarity-Complexity Tradeoff Returns]] | RP4 | price-time-series | Moderate (6) | Joint choice of model and training window on adaptive recent validation raises industry-return OOS R² 14–23%; short-window ridge wins in recessions |
| [[Chen 2026 DIVINE Indicator Reconstruction Pretraining]] | RP4, RP5 | price-time-series | Moderate (7) | Reconstructing indicators from OHLCV across six markets beats masked, contrastive and AR pretraining (Sharpe 1.40 vs 1.01 PatchTST) |
| [[Wang 2025 SSPT Stock-Customised Pretraining Tasks]] | RP4 | price-time-series | Moderate (6) | Masked moving-average target beats masked raw values (Sharpe 1.97 vs 1.54); pretext tasks conflict when combined |
| [[Feng 2026 JEPA Pretraining Time Series Forecasting]] | RP4 | price-time-series | Weak (4) | JEPA pretraining effect is backbone-dependent: −15% to +12% (non-finance) |
| [[Sungu Isiacik 2026 Random Initialization TSFM Baseline]] | RP4, RP5 | evaluation | Strong (11) | Pretrained TSFM weights add only 1.4–5.2 points over random-init twins; 1 of 7 significant after Holm (non-finance) |
| [[Wen 2026 Generic Transformer TSFM Baseline]] | RP4 | price-time-series | Strong (10) | Contiguous patch masking and data mix matter most; data beats model size; mask ratio robust (non-finance) |
| [[Yang 2026 LiMT Liquidity-Aware Multi-Task Stocks]] | RP4 | price-time-series | Moderate (7) | Volume/volatility auxiliary losses raise CSI300 IC 0.0543 → 0.0575, only with gating and small weights |
| [[Kirchdorfer 2024 Uncertainty-Based Loss Weighting MTL]] | RP4 | evaluation | Moderate (7) | Tuned fixed weights or inverse-loss softmax best; uncertainty weighting overfits; LR tuning matters most (vision) |
| [[Dolphin 2024 Contrastive Asset Embeddings]] | RP4 | graph | Moderate (6) | Contrastive co-movement embeddings beat correlation for sector and hedging; best loss flips by task |
| [[Lee 2026 EXAONE Finance Attention-Free TSFM]] | RP4 | price-time-series | Moderate (7) | Synthetic-only pretraining with direct multi-horizon quantile loss ranks #1 on FinVerse (same authors' benchmark) |
| [[Song 2026 Label Horizon Paradox]] | RP3, RP4 | cleaning | Moderate (6) | Best training label horizon can differ from target horizon; learned mix raises IC |
| [[Bieganowski 2024 Supervised Autoencoder Triple Barrier]] | RP3 | cleaning | Moderate (7) | Triple-barrier labels help at 15–30-min bars, not 5-min; sensitive to barriers |
| [[Kang 2025 Triple Barrier OHLCV Korean Stocks]] | RP3 | cleaning | Weak (5) | TB parameters tuned for class balance; LSTM = XGBoost F1 0.43 |
| [[Kili 2025 Adaptive Event-Driven Labeling]] | RP3 | cleaning | Weak (4) | FH, TB, trend scanning all ~0 Sharpe across 16 assets |
| [[Siswara 2024 Early Crash Detection ASEAN-5]] | RP3 | novelty-detection | Moderate (6) | VaR-quantile crash labels; no treatment → no alarms; SMOTE-ENN hit rate ~21% |
| [[Zhao 2025 Label Unbalance High-Frequency Trading]] | RP3 | cleaning | Weak (5) | Fee-aware labels ~80% no-trade; class weights beat resampling/focal loss |
| [[Freyberger 2025 Missing Data Asset Pricing Panels]] | RP3 | cleaning | Moderate (8) | Complete case keeps ~10% of rows; mean imputation biased; universe drives Sharpe gains |
| [[Bryzgalova 2025 Missing Financial Data]] | RP3, RP5 | cleaning | Moderate (9) | Fundamentals not MAR; local B-XS halves median-fill error without look-ahead |
| [[Blanchet 2023 Imputation Look-Ahead-Bias Variance Tradeoff]] | RP3, RP5 | cleaning | Moderate (7) | Full-panel imputation leaks test period; training-only is noisier; consensus best |
| [[Le Morvan 2024 Imputation for Prediction Diminishing Returns]] | RP3 | cleaning | Moderate (8) | Better imputation buys ~1/10 as much prediction; missingness indicators help |
| [[Mo 2025 ACT-Tensor Financial Panel Imputation]] | RP3 | cleaning | Weak (3) | Tensor imputation doubles factor Sharpe, but centred smoother and full-panel fit leak |
| [[Dezons 2026 Synthetic Augmentation Financial ML]] | RP3, RP5 | cleaning | Moderate (8) | Synthetic data: vol ΔR² +0.011 (linear); hurts direction for all generators |
| [[He 2026 TimeGAN Scenarios Rachev Portfolios]] | RP3, RP5 | cleaning | Moderate (9) | TimeGAN understates vol and tails, distorts correlations; no significant gain |
| [[Hashimoto 2026 Synthetic Scenario Compatibility Hedging]] | RP3 | cleaning | Weak (4) | Generator realism does not predict deep-hedging performance |
| [[Shumailov 2024 Model Collapse Training on Generated Data]] | RP3 | cleaning | Weak (5) | Training on generated data loses distribution tails first |
| [[Andersen 1998 Answering the Skeptics Volatility]] | RP3 | cleaning | Weak (4) | Daily returns are noisy volatility readings; daily range ≈ 2–3-hour information |
| [[PyPOTS 2026 Partially Observed Time Series Toolbox]] | RP3 | cleaning | Primary documentation | ~45 imputers; masked-MAE evaluation; no look-ahead check |
| [[Barndorff-Nielsen 2009 Realised Kernels in Practice]] | RP3 | cleaning | Weak (5) | Standard TAQ cleaning rules P1–P3, Q1–Q4, T1–T4; one stock |
| [[Brownlees 2006 Ultra-High Frequency Data Handling]] | RP3 | cleaning | Weak (2) | Removing 0.18% bad ticks changes every ACD coefficient |
| [[Audrino 2002 Synchronizing Multivariate Financial Time Series]] | RP3 | cleaning | Weak (5) | Synchronising closes raises DJIA–Nikkei correlation 0.19→0.33 |
| [[Muhammad 2026 Temporal Coverage Bias Panel Data]] | RP3, RP5 | cleaning | Moderate (9) | Back-filling before listing cuts volatility ~20%, GARCH variance ~26% |
| [[Yao 2026 DelistBench Corporate-Event Database Completion]] | RP3 | cleaning | Moderate (9) | Delisting status auditable (97%) but exact dates ≤46% correct |
| [[Bradley 2014 Analyst Recommendation Timestamp Delays]] | RP3 | cleaning | Moderate (7) | ~56–58% of matched daytime I/B/E/S and First Call times late by ~2.4 h |
| [[Berkman 2009 After-Hours Earnings Event Day 0]] | RP3 | cleaning | Weak (5) | >40% of earnings after hours; reaction one day after database date (abstract) |
| [[Gabrovsek 2017 Twitter Sentiment Earnings Announcements]] | RP3 | cleaning | Moderate (8) | Calendar-day tweet bins create spurious prediction for after-close earnings |
| [[Xue 2026 Temporal Leakage Financial News NLP]] | RP3, RP5 | cleaning | Strong (10) | Random splits inflate news-direction MCC 1.1–6.5×; chronological MCC ≤0.06 |
| [[Passonneau 2014 Company Mention Detection]] | RP3 | cleaning | Weak (5) | Coreference raises mention recall 57%→77%, precision 100%→90%; no forecast gain |
| [[Ding 2021 JEL Entity Linking JPMorgan]] | RP3 | cleaning | Weak (4) | Char n-gram + context linker beats string match; hard name pairs excluded |
| [[Zhang 2026 When Alpha Disappears Decision-Time Leakage]] | RP3, RP5 | cleaning | Moderate (9) | Centered features / same-bar execution add Sharpe 15–26; global normalisation ~0 |
| [[Chen 2026 Look-Ahead Bias Pretrained Forecasting Models]] | RP3, RP4 | cleaning | Moderate (9) | Post-origin training of numeric TSFMs usually worsens forecasts (18/20 US cases) |
| [[Ranse 2026 Survivorship Bias NIFTY Smallcap 250]] | RP3 | cleaning | Moderate (7) | Current members overstate Indian small-cap returns by 4.9 points a year |
| [[Daniel 2009 Look-Ahead Benchmark Bias]] | RP3 | cleaning | Moderate (9) | End-of-period index membership adds 1.5–7.2% a year (CRSP 1926–2006) |
| [[Fu 2014 Asset Growth Anomaly Delisting Bias]] | RP3 | cleaning | Moderate (9) | >90% of delistings lack monthly returns; ~4%/yr on extreme EW decile |
| [[Alfalah 2026 Point-in-Time Leakage Electricity Data]] | RP3 | cleaning | Moderate (7) | Issue-time selection picks unpublished runs on >99% of days (some feeds) |
| [[Klimin 2026 Reconstructed vs Native GDELT GKG]] | RP2 | data-sources | Moderate (9) | GKG software closed; reconstruction tone CCC 0.75; 2.5% of 15-min archives missing |
| [[El Ouadi 2026 Common Crawl News vs GDELT]] | RP2 | data-sources | Weak (4) | GDELT and CC-News share 5.4% of domains (H1 2023) |
| [[ACLED 2026 End User Licence Agreement]] | RP2 | data-sources | Primary documentation | Non-commercial; corporate licence for firms; no training/embeddings without consent |
| [[USGS 2026 Earthquake Feeds and Public Domain]] | RP2 | data-sources | Primary documentation | Feeds updated every minute; events revised (`updated`); public domain |
| [[NOAA 2026 Storm Events Database]] | RP2 | data-sources | Primary documentation | US storms from 1950; event types change by period; months of lag |
| [[MarineCadastre 2026 AIS Vessel Traffic]] | RP2 | data-sources | Primary documentation | USCG AIS for US waters from 2009; CC0; months of lag |
| [[Bacilieri 2023 Firm-level Production Networks]] | RP2, RP3  | data-sources | Moderate (7) | FactSet misses most links vs complete admin networks; binary stats biased; Compustat 10% rule |
| [[Fukada 2026 Snippet-Driven Supply Chain Discovery]] | RP2, RP3  | data-sources | Weak (4) | LLM on web snippets finds 9.3x CSMAR links in China; precision unmeasured |
| [[GLEIF 2026 Level 2 Who Owns Whom]] | RP2, RP3  | data-sources | Primary documentation | Free LEIs with direct/ultimate parents since 2017; CC0 website data |
| [[OpenFIGI 2026 API Documentation]] | RP2, RP3  | data-sources | Primary documentation | Free identifier mapping; delisted only on request |
| [[SEC 2026 Form 13F Data Sets]] | RP2 | data-sources | Primary documentation | Free as-filed 13F holdings from 2013 Q2 |
| [[SEC 2026 Insider Transactions Data Sets]] | RP2 | data-sources | Primary documentation | Free as-filed Forms 3/4/5 from 2006 Q1 |
| [[FactSet 2026 Revere Supply Chain Relationships]] | RP2, RP3  | data-sources | Primary documentation | Dated customer/supplier links from 2003; subscription; academic non-commercial |
| [[Compustat 2026 Historical Segments Customers]] | RP2, RP3  | data-sources | Primary documentation | Customer segments from 1976 (10% rule); academic via WRDS |
| [[BoardEx 2026 North America Data Guide]] | RP2 | data-sources | Primary documentation | Directors/executives of 20,000+ firms from 1999; academic via WRDS |
| [[Giulio 2025 Alpha Vantage Adjusted Close vs CRSP]] | RP2 | data-sources | Weak (4) | Alpha Vantage raw close matches CRSP; adjusted close inconsistent (one stock) |
| [[Twelve Data 2026 Pricing]] | RP2 | data-sources | Primary documentation | $0–$999/month personal plans; history and licence not stated on pricing page |
| [[Databento 2026 Python Client]] | RP2 | data-sources | Primary documentation | Official Apache-2.0 client; historical, live, batch; DBN; pandas |
| [[Alpaca 2026 alpaca-py SDK]] | RP2 | data-sources | Primary documentation | Official Apache-2.0 SDK; bars and streaming; ~1.6k stars |
| [[Massive 2025 Market Data Terms of Service]] | RP2 | data-sources | Primary documentation | Store for personal use; no AI/ML training (s. 5(g)); delete within 30 days of licence end |
| [[X 2026 Developer Agreement]] | RP2 | data-sources | Primary documentation | No training foundation/frontier models; delete removed posts within 24 h; IDs are X Content |
| [[Alpaca 2026 Terms and Conditions Market Data]] | RP2 | data-sources | Primary documentation | Personal non-commercial; no copying or redistribution; training not mentioned |
| [[Alpha Vantage 2026 Terms of Service]] | RP2 | data-sources | Primary documentation | Personal non-commercial; silent on storage/training; macro APIs under FRED terms |
| [[EODHD 2026 Terms and Conditions]] | RP2 | data-sources | Primary documentation | Non-professionals may store and analyse privately; no redistribution; training not mentioned |
| [[Nasdaq 2026 Global Subscriber Agreement]] | RP2 | data-sources | Primary documentation | Personal/internal use only; processed data still Information; audit rights |
| [[US Copyright Office 2025 Generative AI Training Report]] | RP2 | data-sources | Primary documentation | Training implicates reproduction; fair use fact-specific; research/non-substitutive favoured; non-binding |
| [[Barez 2023 Benchmarking Databases High-frequency Data]] | RP2 | storage | Weak (4) | kdb+ fastest; InfluxDB most compact; TimescaleDB highest query latency; 1 month crypto, single thread |
| [[Mostafa 2026 Six Dimensions Benchmarking TSDBs]] | RP2 | storage | Moderate (7) | Multi-axis TSDB benchmark: TimescaleDB stalls under parallel load; read/write contention dominates |
| [[Nguyen 2026 Graph Database Engines Cost]] | RP2 | storage | Weak (5) | Edge tables in columnar SQL beat native graph DBs except bounded walks; ingest cost dominates; vendor-authored |
| [[Lu 2026 Filtered Vector Search PostgreSQL]] | RP2 | storage | Moderate (7) | pgvector-in-Postgres filtered search dominated by page/tuple overhead, not distances |
| [[ArcticDB 2026 FAQ and Licence]] | RP2 | storage | Primary documentation | Embedded versioned DataFrame store; snapshots; BSL 1.1 (production use needs licence) |
| [[DuckDB 2026 Parquet Read and Write]] | RP2 | storage | Primary documentation | Query Parquet in place with pushdown; many files as one table; no built-in versioning |
| [[Tiger Data 2026 TimescaleDB Editions]] | RP2 | storage | Primary documentation | Compression and continuous aggregates only in TSL Community Edition; free to self-host |
| [[QuestDB 2026 ASOF Join and Deduplication]] | RP2 | storage | Primary documentation | ASOF JOIN; upsert-key dedup (last write wins); Apache 2.0; vendor TSBS figures |
| [[pgvector 2026 Postgres Vector Search]] | RP2 | storage | Primary documentation | HNSW/IVFFlat; post-filtering returns too few rows unless iterative scans; 2,000-dim index limit |
| [[LanceDB 2026 Table Versioning and Time Travel]] | RP2 | storage | Primary documentation | Version per write, checkout/restore/tags; untagged versions pruned after 7 days default |
| [[MongoDB 2026 Time Series Collection Limitations]] | RP2 | storage | Primary documentation | Updates only on metaField; no transactional writes; no unique indexes |
| [[SurrealDB 2026 Architecture and Versioned Queries]] | RP2 | storage | Primary documentation | Multi-model on one KV layer; SELECT VERSION only on SurrealKV |
| [[RocksDB 2026 Overview]] | RP2 | storage | Primary documentation | Embedded LSM KV library; snapshots not durable; no query or time-series layer |
| [[XTDB 2026 Time in XTDB Bitemporal]] | RP2, RP3  | storage | Primary documentation | Every table bitemporal; SYSTEM_TIME and VALID_TIME AS OF queries |
| [[Jensen 1995 TSQL2 Data Model]] | RP2, RP3, RP5 | storage | Primary documentation | Standard definitions: valid time vs transaction time are orthogonal |
| [[Databricks 2026 Medallion Architecture]] | RP2 | storage | Primary documentation | Bronze = raw, as-is, append-only with provenance; enables replay; schema evolution in silver |
| [[dltHub 2026 Incremental Loading]] | RP2 | storage | Primary documentation | Cursor state + append/replace/merge; failed extract leaves destination untouched |
| [[Airbyte 2026 Incremental Append Deduped]] | RP2 | storage | Primary documentation | Cursor + PK; history + deduped tables; at-least-once; misses changes without cursor bump |
| [[Featonby 2026 Idempotent APIs Builders Library]] | RP2 | storage | Primary documentation | Unique request token recorded atomically with work; same response on repeat; reject mismatches |
| [[IETF 2022 RFC 9111 HTTP Caching]] | RP2 | storage | Primary documentation | Freshness, ETag/Last-Modified revalidation, 304 reuse, no-store |
| [[Hishel 2026 HTTP Caching Library]] | RP2 | storage | Primary documentation | RFC-compliant Python cache for HTTPX/Requests; SQLite/Redis |
| [[requests-cache 2026 Expiration Guide]] | RP2 | storage | Primary documentation | Stores indefinitely by default; per-URL expiry; stale_if_error |
| [[IETF 2026 RateLimit Header Fields Draft]] | RP2 | storage | Primary documentation | RateLimit/-Policy headers still a draft; Retry-After takes precedence |
| [[ALFRED 2026 Real-Time Vintages and FRED API]] | RP2 | data-sources | Primary documentation | 350,000+ series with every vintage; as-of reads via realtime_start/end; default is today |
| [[FRED 2026 Legal Terms of Use]] | RP2 | data-sources | Primary documentation | FRED/ALFRED content may not be used to develop or train ML/AI; API storing/caching prohibited |
| [[Philadelphia Fed 2026 Real-Time Data Set]] | RP2 | data-sources | Primary documentation | Headline macro vintages, monthly, first–third releases; free files |
| [[McCracken 2026 FRED-MD FRED-QD Databases]] | RP2 | data-sources | Primary documentation | Monthly-vintage macro panels from 1999-08 (MD), 2018-05 (QD) |
| [[BLS 2026 Copyright Information]] | RP2 | data-sources | Primary documentation | All BLS publications public domain; citation requested |
| [[Croushore 2011 Frontiers of Real-Time Data Analysis]] | RP2 | data-sources | Strong (12) | Revisions large (2008Q4 GDP −3.8%→−6.2%); latest-vintage evaluation distorts forecast skill |
| [[Lyle 2024 Re-Standardized Financial Statement Data]] | RP2 | data-sources | Moderate (7) | Compustat re-standardises in place; earnings sign flips 9–14%; hedge returns shift ~25–31 pp |
| [[SEC 2026 Accessing EDGAR Data]] | RP2 | data-sources | Primary documentation | Free; 10 req/s with User-Agent; after-5:30 p.m. ET filings disseminated next business day |
| [[Rogers 2017 Run EDGAR Run SEC Dissemination]] | RP2 | data-sources | Weak (5) | 2012–13: just over half of Form 4s reached PDS subscribers before EDGAR site (~18 s); prices moved first |
| [[X 2026 API Pricing and Search]] | RP2 | data-sources | Primary documentation | Pay-per-use $0.005/post, 3M posts/month cap; full archive to 2006 |
| [[Reddit 2026 Data API Wiki]] | RP2 | data-sources | Primary documentation | 100 QPM free; commercial/research by approval; terms page blocked |
| [[StockTwits 2026 Terms of Service]] | RP2 | data-sources | Primary documentation | Scraping banned; StockTwits licenses derived products itself |
| [[GDELT 2026 Data and Terms of Use]] | RP2 | data-sources | Primary documentation | Free for any use, redistributable with citation; 15-min updates |
| [[OpenAlex 2026 API Authentication and Limits]] | RP2 | data-sources | Primary documentation | Free key: 30 req/s, 10× keyless budget; paid above |
| [[arXiv 2026 API Terms of Use]] | RP2 | data-sources | Primary documentation | Metadata CC0, 1 req/3 s; full text per-paper licence |
| [[Benzinga 2026 Stock News API]] | RP2 | data-sources | Primary documentation | Not delayed; created/updated stamps; price on request |
| [[RavenPack 2026 News Analytics Library Guide]] | RP2 | data-sources | Primary documentation | Dow Jones + 19,000 sources, ms timestamps, 20+ years; institutional |
| [[Alpaca 2026 Historical News API]] | RP2 | data-sources | Primary documentation | News with created_at and source field; history/terms not stated |
| [[Alpaca 2026 Market Data API Stocks]] | RP2 | data-sources | Primary documentation | SIP bars from 2016, 1-min minimum, query-time split/dividend/spin-off adjustment; free tier IEX; $99/month |
| [[Databento 2026 US Equities Data and Pricing]] | RP2 | data-sources | Primary documentation | 45 venues to MBO, ns timestamps; ticks only from 2018; Standard $199/month = 12 months L1 |
| [[Massive 2026 Stocks API Plans and History]] | RP2 | data-sources | Primary documentation | From 2003-09-10; delisted tickers point-in-time; split-adjusted bars; $199/month all history |
| [[Alpha Vantage 2026 Premium Plans and Time Series]] | RP2 | data-sources | Primary documentation | Free 25/day; $49.99–$249.99 for 75–1,200/min; 1-min intraday since 2000-01 (premium) |
| [[Tiingo 2026 Pricing and IEX API]] | RP2 | data-sources | Primary documentation | 30+ years daily at $30/month; intraday IEX-only; personal internal use |
| [[EODHD 2026 Pricing and Data Coverage]] | RP2 | data-sources | Primary documentation | $29.99/month EOD+intraday; 1-min US from 2004; ticks from 2008 add-on |
| [[Norgate 2026 US Stocks Packages and Delisted Data]] | RP2 | data-sources | Primary documentation | Delisted + index constituents back to 1990/1950 for $630/$788 a year; EOD only |
| [[CRSP 2026 US Stock Databases]] | RP2, RP3  | data-sources | Primary documentation | ~100 years daily/monthly, PERMNO/PERMCO identifiers; institutional licence |
| [[Tick Data 2026 US Equities Historical]] | RP2 | data-sources | Primary documentation | Consolidated ticks since 1993 incl. inactive symbols; price on request |
| [[FirstRate Data 2026 Complete Intraday Stocks]] | RP2 | data-sources | Primary documentation | 1-min bars since 2000 incl. 7,000+ delisted; source not stated |
| [[Liu 2020 Data Quality Problems Finance Databases]] | RP2 | data-sources | Moderate (7) | CRSP errors, biased daily EW index (~6%/yr), ~13% delisting returns still missing (2017) |
| [[Rapach 2013 International Return Predictability US Role]] | RP1 | price-time-series | Moderate (9) | Lagged US returns predict 9 of 10 non-US markets out of sample (monthly); not the reverse |
| [[Siliverstovs 2015 US Role International Predictability Recessions]] | RP1 | price-time-series | Moderate (9) | Exact replication: US-lead gain only in US recessions (R²OS 4–13%), none in expansions |
| [[Pan 2006 Option Volume Future Stock Prices]] | RP1, RP5 | price-time-series | Moderate (7) | Opening-volume put-call ratio predicts ≈42 bp/day; decays over 3 weeks, no reversal; non-public signal |
| [[Chordia 2018 Low-Latency Trading Macro Announcements]] | RP1, RP5 | price-time-series | Moderate (6) | SPY/E-mini priced within 0.1 s of macro surprises; fast-trading profits small, ≈0 by 2014 |
| [[Hong 2000 Bad News Travels Slowly]] | RP1 | price-time-series | Weak (5) | Momentum larger in small, low-coverage stocks, esp. losers: bad news diffuses slowly (summary read) |
| [[Busse 2002 Market Efficiency in Real Time]] | RP1 | price-time-series | Weak (5) | CNBC mentions priced in seconds; positive in 1 min, negative over ~15 min (abstract read) |
| [[Christensen 2026 Warp Speed Jumps After Earnings]] | RP1 | price-time-series | Moderate (9) | Prices jump after 91% of after-hours earnings releases; no profit after 2016 with spreads or 5 s delay |
| [[Lucca 2015 Pre-FOMC Announcement Drift]] | RP1, RP5 | price-time-series | Moderate (9) | S&P 500 +49 bp in 24 h before FOMC (1994–2011), no reversal; none before other releases |
| [[Augustin 2019 Informed Options Trading Before Takeovers]] | RP1 | price-time-series | Moderate (9) | Abnormal target option volume in ≈25% of 1,859 takeovers, OTM calls 5–10 days before; news explains ≈9% |
| [[Kurov 2021 Disappearing Pre-FOMC Drift]] | RP1 | price-time-series | Moderate (8) | Pre-FOMC drift ≈9 bp and insignificant 2016–19; decline tied to lower uncertainty |
| [[Li 2026 Option-Implied Signals Crash Risk]] | RP1 | tail-risk | Moderate (8) | IV spread, RN skew predict returns in all regimes 2015–26; smirk fades; crash AUC 0.71 calm vs 0.56 crisis |
| [[Kurov 2019 Price Drift Before Macro News]] | RP1 | price-time-series | Moderate (6) | Futures drift ~30 min before 9 of 20 macro releases; 36–49% of adjustment pre-release |
| [[Kargarzadeh 2026 When Is News Priced In]] | RP1 | novelty-detection | Weak (5) | 1.68M news events: move mostly by day 0; numbers drift, stories reverse; sentiment fade = background drift |
| [[Bazyari 2026 Breaking-News Latency Sample Effects]] | RP1 | novelty-detection | Weak (2) | X vs news first-report order flips with event sample; a third of first reports from other platforms |
| [[Lu 2026 Corroboration Illusion News Poisoning]] | RP1, RP5 | llm-text | Moderate (9) | 5 fabricated consistent articles flip 69–77% of RAG forecasts; publisher labels ignored; allow-list, aggregation and perplexity defenses bypassed |
| [[Kogan 2023 Social Media Financial News Manipulation]] | RP1, RP5 | sentiment | Moderate (7) | SEC-identified fake articles: volume +50%, small-cap spike then reversal; after revelation reaction to all articles falls (−35% small firms) |
| [[Tetlock 2011 Stale News Reprint]] | RP1 | novelty-detection | Moderate (6) | Stale (repeated) news moves prices less but reverses next week (−26 bp); individuals drive it |
| [[Fedyk 2023 When Market Identifies Old News]] | RP1 | novelty-detection | Moderate (6) | Reprints discounted, recombinations of old news over-reacted to then reversed; effect grew 2001–14 |
| [[Zhou 2025 Expert Opinion Social Media Stock Prediction]] | RP1 | sentiment | Moderate (6) | Track-record experts 72.8% vs crowd 47.6% direction accuracy; ~4% coverage; small IC gain inside strong model |
| [[Wang 2015 Crowds on Wall Street]] | RP1 | sentiment | Moderate (6) | Author reputation persists OOS on SeekingAlpha (corr ≈0.12), not StockTwits; aggregate sentiment ≈ useless |
| [[Fan 2020 Social Media Bots Stock Markets]] | RP1 | sentiment | Weak (5) | Bot tweets (~5%) weaker than human for volatility/volume, no return info; positive bot spikes then negative returns |
| [[Huang 2019 Trust Filters Twitter Stock Prediction]] | RP1 | sentiment | Weak (4) | Trust-weighted tweet sentiment ROI 4.26% vs 2.81% unweighted; 6 months, no costs |
| [[Bolz 2025 Real-Time Pump-and-Dump Detection]] | RP1 | novelty-detection | Weak (3) | Pump target top-5 of 51 in 56% at 20 s ahead, 19% at 1 min |
| [[Cresci 2018 Cashtag Piggybacking Bots]] | RP1 | sentiment | Weak (2) | 71% of accounts behind top cashtag bursts are bots; bursts 60% retweets pairing large caps with OTC tickers |
| [[Song 2026 When News Gets Old]] | RP1 | novelty-detection | Weak (8, capped) | News-age features or 8-week filter: no net-return gain beyond noise; market-only RL best |
| [[Merchant 2026 Towards Financial World Modeling]] | RP1, RP5 | price-time-series | Strong (12) | 18 state encoders on 1 Hz US equities 2008–25: supervised multihead best (return IC 0.031); most SSL ≈ random encoder; month explains 97–99.9% of variance |
| [[Zhao 2026 PGA-Trans-HAR Cross-Market Volatility]] | RP1 | graph | Moderate (9) | Cross-market info helps only as bounded correction to local HAR (MSE −1.7% at 1 day); VHAR +33% MSE at 22 days |
| [[Oliveira 2026 HANET Macro-Aware Mixed-Frequency Attention]] | RP1 | fusion | Moderate (8) | Point-in-time macro via regime attention: futures momentum SR 1.19 → 1.99; concatenated macro → 0.06; gone by 5 bps |
| [[Hu 2026 Exogenous Dropout Corruption-Robust Covariates]] | RP1, RP4 | fusion | Moderate (7) | Covariate models 24–62% worse than price-only floor when covariates corrupted; channel dropout restores robustness |
| [[Chen 2024 Deep Learning in Asset Pricing]] | RP1 | price-time-series | Weak (5) | Raw 178 macro series collapse OOS SDF Sharpe; LSTM macro states add ~10% |
| [[Das 2026 Chronos-2 Multivariate Financial Forecasting]] | RP1 | price-time-series | Weak (5) | Same-class multivariate context helps Chronos-2 levels; adding the other asset class slightly hurts |
| [[Liu 2026 World2TS Real-World Event Context]] | RP1 | fusion | Weak (5) | Hindsight-linked events help LLM forecasters in 49/54 pairs; can hurt; LLM cutoff uncontrolled |
| [[Bai 2026 Covariate TSFMs Forecast Associations Not Interventions]] | RP1 | evaluation | Weak (5) | Covariate-aware TSFMs answer what-if queries associationally (1.3–1.8× OLS confounding) |
| [[Zhu 2026 WorldTS Latent World Modeling Covariates]] | RP1 | fusion | Weak (4) | Latent-state world model with covariates beats baselines on non-financial sets; no-covariate ablation worse |
| [[Noguer i Alonso 2026 Pretrained TSFMs Return Forecasting]] | RP1, RP4, RP5 | price-time-series | Moderate (6) | Zero-shot TSFMs top rankings on 5 US stocks but beat random walk significantly in only 2/10 cases |
| [[Rahimikia 2025 ReVisiting TSFMs in Finance]] | RP1, RP5 | price-time-series | Strong (12) | Off-the-shelf TSFMs lose to CatBoost; finance-native pretraining narrows gap; all daily long–short strategies negative after 20 bps |
| [[Shi 2025 Kronos Financial Foundation Model]] | RP1, RP4, RP5 | price-time-series | Moderate (6) | Finance-only K-line FM beats generic TSFMs and GARCH in one post-2024 window; no significance tests; discrete tokens beat continuous AR variants in its ablation (RQ1.10) |
| [[Brini 2026 TSFMs vs Econometric Realized Volatility]] | RP1, RP4, RP5 | price-time-series | Strong (12) | Only 1 of 9 zero-shot TSFMs beats Log-HAR for realised vol, by ~1.5%; HAR models stay in MCS |
| [[Christensen 2023 Machine Learning Volatility Forecasting]] | RP1, RP5 | price-time-series | Moderate (7) | RF and NNs beat HAR family for DJIA realised variance; gains largest at monthly horizon and with extra predictors |
| [[Zhu 2026 AI Equity Crypto Limits Review]] | RP1, RP3, RP4 | evaluation | Weak (review) | Review: no general AI architecture shown to give persistent net alpha; points to look-ahead and memorisation failures |
| [[Gu 2020 Empirical Asset Pricing Machine Learning]] | RP1, RP3, RP4, RP5 | price-time-series | Moderate (8) | Trees and shallow NNs beat linear models for monthly US returns (R²oos ~0.4%); depth >3 layers adds nothing; no costs |
| [[Nguyen 2026 Volatility-Clustering Adaptation]] | RP1, RP4, RP5 | price-time-series | Weak (5) | Naive fine-tuning of Kronos can underperform the frozen model; HAR-RV beats frozen Kronos on variance at longer horizons (CSI300) |
| [[Fang 2026 Volatility Regimes Return Prediction China]] | RP1 | price-time-series | Moderate (9) | Regime probability improves HARQ in stress; XGBoost return signal only in low-vol regimes; not significant after SPA |
| [[Dewage 2026 Hybrid Correction Frozen TSFM]] | RP1, RP4 | price-time-series | Moderate (6) | Frozen TimesFM ≈ historical mean intraday; RF residual stage gives most of the correction gain (40-day test) |
| [[Saly-Kaufmann 2026 Deep Learning Financial Benchmark]] | RP1, RP4 | price-time-series | Moderate (8) | Sharpe-optimised multi-asset futures: gated recurrent/hybrid models beat linear; generic Transformers and SSMs no better than AR(1); ranking holds net of 0–5 bp |
| [[Mesfin 2026 LSTM vs Gradient Boosting MNQ]] | RP1 | price-time-series | Moderate (7) | Null result: GBT and LSTM at base rate on 944 days of intraday futures; small test sets give chance accuracies up to 61% |
| [[Lopez-Lira 2026 ChatGPT Forecast Stock Prices]] | RP1 | llm-text | Moderate (7) | GPT-4 calls initial reaction to post-cutoff headlines ~90% of days; drift Sharpe 2.97 gross, negative at 20 bps, decays 2021–24 |
| [[Lopez-Lira 2025 LLM Memorization Problem]] | RP1, RP3, RP4, RP5 | llm-text | Moderate (7) | GPT-4o recalls pre-cutoff index levels (MAPE 0.61%) vs 16.9% post; fake-cutoff prompts and masking fail |
| [[Glasserman 2023 Look-Ahead Bias GPT Sentiment]] | RP1, RP3 | llm-text | Moderate (6) | Anonymised headlines beat original in sample: GPT-3.5 distraction effect larger than look-ahead gain |
| [[Dehkordi 2026 OLIVIA LLM News Look-Ahead Test]] | RP1, RP3, RP4 | llm-text | Strong (10) | Pre-registered blinded test: news priced at the open; validated IC 0.065 → 0.020; no strategy survives costs; masking leaks identity |
| [[Guo 2026 Language Models Forecast Stock Prices]] | RP1 | llm-text | Weak (5) | Price-only agent benchmark: momentum beats 7/9 frontier LLMs; frontier scores collapse in later window |
| [[Yan 2026 DatedGPT Time-Aware Pretraining]] | RP1, RP3, RP4 | llm-text | Moderate (9) | Time-locked 1.3B LLMs keep headline signal (Sharpe 3.20 gross); biased vintages add a significant look-ahead premium |
| [[Foley 2026 NoLBERT News Topics Returns]] | RP1, RP5 | llm-text | Strong (10) | Point-in-time encoder topics ≈ LDA; best combo net Sharpe 1.12, not better than price-only; best validated pick loses |
| [[Li 2025 Structured Event Representation Returns]] | RP1 | llm-text | Weak (capped) | LLM event triplets beat FinBERT for returns (gross), but GPT-3.5 used on pre-cutoff news without controls |
| [[Chen 2026 Agentic AI Nowcasting Returns]] | RP1, RP4 | llm-text | Moderate (8) | Live web-search LLM, Russell 1000, 9 months: top-20 alpha 18.4 bp/day; no skill for losers |
| [[Tan 2024 Are LMs Useful for Time Series]] | RP1 | llm-text | Moderate (8) | Removing the LLM from LLM time-series forecasters does not hurt accuracy; ~1,000× less compute |
| [[Cookson 2024 The Social Signal]] | RP1, RP5 | sentiment | Strong (11) | Cross-platform social sentiment +6 bp/SD next day, no reversal; attention −13 bp/SD, reverses; WSB sentiment no signal |
| [[Aravinthakshan 2026 Human Agreement vs Return Association]] | RP1, RP5 | sentiment | Moderate (9) | Human-label agreement does not rank tools by return association; FinBERT best 1-day lead on X; volume no signal |
| [[Heston 2017 News vs Sentiment Returns]] | RP1, RP5 | sentiment | Moderate (6) | Daily news tone predicts 1–2 days; weekly tone up to 13 weeks, via negative news and next earnings |
| [[Kirtac 2024 Sentiment Trading with LLMs]] | RP1 | sentiment | Weak (capped) | OPT > BERT ≈ FinBERT >> LM dictionary (L-S Sharpe 3.05/2.07/1.23 at 10 bps), but random split and pre-cutoff LLM |
| [[Luo 2026 QLoRA Sentiment Return Predictability]] | RP1, RP5 | sentiment | Weak (capped) | QLoRA LLMs classify best, FinBERT has best 1-day IC; IC negative from day 2; nothing survives FDR |
| [[Bisharat 2026 Evaluating Financial Sentiment AI]] | RP1, RP4, RP5 | sentiment | Weak (capped) | 12 tools + Claude: accuracy 54–94%, none predicts next-day returns after earnings releases |
| [[Jiao 2020 Social Media News Media Stock Market]] | RP1 | sentiment | Weak (5) | News coverage lowers, social coverage raises next-month volatility and turnover (in-sample) |
| [[Kilian 2026 LLM vs Lexicon Meme Stocks]] | RP1, RP5 | sentiment | Weak (2) | VADER no signal on WSB meme stocks; LLM index asset-specific; weak tail-event warnings |
| [[Kmak 2025 ChatGPT Reddit Sentiment Prices]] | RP1 | sentiment | Weak (2) | WSB sentiment unrelated to GME/AMC prices; comment volume and Google Trends related |
| [[Li 2025 OmniGNN Multi-relational Stock GNN]] | RP1 | graph | Weak (4) | Multi-relational GNN IC 0.067 vs GAT 0.021 on 10 tech stocks; no non-deep baseline, no costs |
| [[Wade 2026 GNN Volatility Forecasts Portfolios]] | RP1, RP3  | graph | Moderate (7) | Correlation GNN barely beats HAR for weekly RV; sector/Granger graphs worse; macro features drive gains |
| [[Yilki 2026 Supply Chain Propagation Text Signals]] | RP1 | graph | Weak (5) | Neighbour-averaged 10-K embeddings predict returns (t −2.64, net Sharpe 0.67) on a 48-node manual graph |
| [[Gorduza 2024 Alpha from Analyst Networks]] | RP1 | graph | Moderate (6) | GAT on analyst co-coverage gross Sharpe 4.07 vs neighbour average 0.07; no costs or tests |
| [[Cohen 2008 Economic Links Predictable Returns]] | RP1, RP3, RP5 | graph | Moderate (8) | Customer momentum 1.55%/month 1980–2004; not explained by own, industry or cross-industry momentum |
| [[Ali 2020 Shared Analyst Coverage Momentum Spillover]] | RP1, RP3  | graph | Moderate (7) | Analyst-link neighbour return alpha 1.68%/month (t 9.67); subsumes other spillovers; holds in 10/11 markets |
| [[Barrot 2016 Input Specificity Shock Propagation]] | RP1, RP5 | graph | Moderate (8) | Supplier disaster cuts customer sales growth ~2 pp and value ~1% within 21 days; specific inputs only |
| [[Pinchuk 2023 Customer Momentum Out of Sample]] | RP1 | graph | Moderate (7) | Customer momentum halves after 2004 (VW insignificant); partly large-to-small lead–lag |
| [[Pu 2023 Network Momentum Across Asset Classes]] | RP1, RP3  | graph | Moderate (9) | Learned-graph network momentum Sharpe 1.36 vs 0.95 own momentum gross; negative at 5 bps |
| [[Xu 2021 HIST Concept Graph Stock Forecasting]] | RP1, RP5 | graph | Moderate (8) | Plain GAT ≈ GRU without graph on CSI 300 (IC 0.111 vs 0.113); HIST concept modules reach 0.131 |
| [[Zhou 2026 LENS LLM Priors News Graphs]] | RP1, RP3  | graph | Weak (5) | LLM-extracted relation graph beats GICS/WikiData inside same GNN; one bullish year, no costs |
| [[Fanshawe 2026 Transformer GNN Equity Correlations]] | RP1 | graph | Weak (5) | Transformer–GAT cuts 10-day correlation MAE vs persistence; prior ML trading gains not reproduced |
| [[Huang 2023 Temporal Graph Benchmark]] | RP1, RP5 | graph | Moderate (9) | Persistence and moving average beat temporal GNNs on all node tasks incl. token transactions |
| [[Garcia Seuma 2026 Crypto Cascade Early Warning]] | RP1, RP4, RP5 | novelty-detection | Strong (11) | No event-invariant crash precursor across 7 BTC cascades; sudden-news shocks show none in price |
| [[Glasserman 2023 New News is Bad News]] | RP1, RP5 | novelty-detection | Moderate (9) | Rise in news entropy predicts lower 12-month S&P 500 returns; OOS R² 0.024–0.051 |
| [[Manela 2017 News Implied Volatility Disasters]] | RP1 | novelty-detection | Moderate (7) | WSJ-text VIX proxy predicts returns and disasters (+2.5 pp/s.d.); missed March 2000 |
| [[Glasserman 2019 Unusual News Forecast Market Stress]] | RP1 | novelty-detection | Moderate (6) | Unusual negative news predicts volatility up to 6 months; in-sample |
| [[Qian 2026 Extreme Volatility Warning Anomaly Fusion]] | RP1, RP4 | novelty-detection | Moderate (6) | GDELT + Chinese news anomalies lift 1–3 day extreme-vol AUC 0.608 → 0.680; English news hurts |
| [[Tsapeli 2017 Twitter Events Stock Market Jitters]] | RP1 | novelty-detection | Moderate (6) | Learned filter on Twitter bursts F1 0.68–0.74 for intraday jitters; raw bursts ≤0.33 |
| [[Neela 2025 Systemic Risk Radar Crash Warning]] | RP1 | novelty-detection | Weak (5) | Correlation-graph GNN crash warner FPR 1.0; COVID AUROC 0.000 |
| [[Neela 2025 AIMM Social Media Manipulation Detection]] | RP1, RP4 | novelty-detection | Weak (4) | Synthetic social data; 1 of 3 events pre-alerted; price rule discriminates better |
| [[Gianstefani 2022 Reddit Alert System Meme Stocks]] | RP1 | novelty-detection | Weak (2) | Reddit activity + influencer alerts precede meme-stock abnormal returns; in-sample, 4 stocks |
| [[Andrew 2024 CRISIS ALERT Market Crisis ML]] | RP1 | novelty-detection | Weak (2) | Next-day crash days: lagged VIX top feature; backward-fill leakage |
| [[Schmitt 2026 Conformal Calibration Portfolio VaR]] | RP1 | tail-risk | Strong (13) | All base VaR models over-exceed 2018–24; recency/regime-weighted conformal halves stress-quintile misses vs ACI; no buffer fixes non-adaptive HS |
| [[Taylor 2025 Combining VaR and ES Forecasts]] | RP1, RP4 | tail-risk | Strong (11) | Combining 90 VaR/ES methods: trimmed mean, probability averaging, performance weights best; pool underestimates risk |
| [[Zhang 2026 ReSGA Large Tail Risk Model]] | RP1 | tail-risk | Strong (11) | Pooled VaR–ES model on 40k stocks beats GARCH/GAS (monthly 5%); gains from data, not parameters |
| [[McNeil 2000 Conditional EVT Tail Risk]] | RP1 | tail-risk | Moderate (9) | GARCH + GPD tail passes 95–99.5% VaR tests incl. 1987; GARCH-normal fails; normal useless for ES |
| [[Aich 2025 Temporal Conformal Prediction Risk]] | RP1, RP4 | tail-risk | Moderate (9) | Conformal TCP near-nominal overall, but only 80% coverage (95% target) in COVID window, like GARCH |
| [[Goel 2024 TimesFM Value-at-Risk Forecasting]] | RP1 | tail-risk | Moderate (9) | Fine-tuned TimesFM best violation ratios on 91 stocks, ≈ GAS on quantile loss; zero-shot worse |
| [[Michankow 2025 Deep Networks Return Distributions]] | RP1 | tail-risk | Moderate (9) | Skew-t LSTM/CNN VaR ≈ best GARCH on 6 indices; normal outputs fail 1% tests |
| [[Barunik 2024 Quantile Neural Networks Return Distributions]] | RP1 | tail-risk | Moderate (8) | Quantile NN beats GARCH, RF, GBRT on tail quantile loss (monthly, global); no VaR backtest |
| [[Li 2026 Adaptive Window Selection Risk]] | RP1, RP4 | tail-risk | Moderate (8) | Adaptive look-back windows cut VaR–ES loss, esp. GFC (3.25% vs 3.66% for 250-day) |
| [[Herrig 2025 LSTM Mixture Density VaR]] | RP1 | tail-risk | Moderate (6) | Negative: LSTM-MDN VaR no better than GARCH(1,1); seed-sensitive (MSc thesis) |
| [[Ye 2026 Regime-Gated Residual MoE Volatility]] | RP1, RP4, RP5 | fusion | Strong (11) | Regime info helps only via soft gate on residual experts; as inputs it hurts and collapses MLPs; gain small (IC 0.547 vs 0.542) |
| [[Sridhar 2026 Text Sensitivity Audit Multimodal TS]] | RP1, RP4, RP5 | fusion | Moderate (7) | Negative: swapping text moves MSE <0.5% in 3 fusion models; published lift came from a numeric column |
| [[Lee 2026 Constrained Fusion Text Time Series]] | RP1, RP4 | fusion | Moderate (7) | Naive add/concat fusion often below text-free model; gating/FiLM/low-rank adapter beat it (Time-MMD) |
| [[Zhou 2026 When Context Routing Helps Fusion]] | RP1, RP4 | fusion | Moderate (6) | Negative: no text information for daily returns of 50 S&P tickers; repeat-last-value beats 14.3B MoE |
| [[Zhang 2025 When Multimodality Helps TS Forecasting]] | RP1, RP5 | fusion | Moderate (6) | Negative: multimodal ≈ unimodal across 16 datasets (p=0.79); gains only for weak TS models |
| [[Koval 2025 Modality-Specific Experts Text and TS]] | RP1, RP4 | fusion | Weak (8, capped) | Separate TS experts + late cross-attention best; net Sharpe 1.51 vs 0.46 price-only (pre-cutoff LLM) |
| [[Zong 2024 MSGCA Gated Cross-Attention Fusion]] | RP1 | fusion | Weak (7, capped) | Adding text to ALSTM hurt on 3/4 datasets; price-led gated cross-attention gives small MCC gains |
| [[Khubiyev 2025 Multimodal Russian Stock Prediction]] | RP1 | fusion | Weak (6, capped) | News embeddings cut MAPE 55% but lowered direction accuracy (52.0% → ≤49.8%) |
| [[Guo 2025 Factors and Newsflow Fusion Returns]] | RP1 | fusion | Weak (4) | Concat fusion > attention; fusion helps NA/EU, hurts EM vs factors alone; mixture most robust |
| [[Zhang 2026 GS-Fuse Granger-Gated Event Fusion]] | RP1 | fusion | Weak (5, capped) | Granger-gated macro-event fusion only 1.5–3.8% MSE better than own price-only branch |
| [[Noseda 2026 Earnings Day Multimodal Direction]] | RP1 | fusion | Weak (5) | FinBERT sentiment adds small macro-F1 gain at earnings days; tiny test |
| [[Lee 2026 XForecast News-Grounded Challenge]] | RP1, RP4 | fusion | Weak (5) | Competition: top solutions ensembles with compact text features; metric weighted by hindsight |
| [[Pei 2025 Cross-Modal Temporal Fusion FTSE]] | RP1 | fusion | Weak (4, capped) | 5 FTSE stocks: F1 0.64 vs 0.61 driven by recall; precision ≈ chance |
| [[Ghali 2025 Commodity Price Shocks Fusion]] | RP1 | fusion | Weak (4, capped) | Negative example: AUC 0.94 from retrospective LLM-written news; hindsight leakage |
| [[Chen 2025 Limits to Machine Learning]] | RP1 | evaluation | Moderate (9) | Finite-sample bound: negative R²_OOS can coexist with ≥20% population R² for market returns |
| [[Yuan 2024 Limits Extreme Event Forecasting Chaos]] | RP1 | novelty-detection | Weak (0) | Model-independent minimum error for extreme-event forecasts; unobserved variables dominate (theory, simulated systems) |
| [[Beutel 2019 ML vs Logit Banking Crisis Warning]] | RP1, RP4 | novelty-detection | Moderate (9) | Logit beats RF/SVM/kNN/trees in recursive OOS banking-crisis warnings; ML overfits |
| [[Greenwood 2022 Predictable Financial Crises]] | RP1, RP4, RP5 | novelty-detection | Moderate (8) | Credit + price booms give ~40–45% 3-year crisis probability; OOS R² 0.9–4.5%; many misses and false alarms |
| [[Guttal 2016 No Critical Slowing Down Before Crashes]] | RP1 | novelty-detection | Moderate (8) | No critical slowing down before major crashes; rising variance precedes them but 7 false alarms in 115 years |
| [[Bree 2010 LPPL Crash Test Hang Seng]] | RP1 | novelty-detection | Weak (4) | LPPL crash parameters hold for 7/11 Hang Seng crashes; fits fragile; mechanism contradicted |
| [[Sun 2024 AI Weather Gray Swan Cyclones]] | RP1, RP4, RP5 | novelty-detection | Moderate (7) | Deep weather model cannot forecast extremes stronger than any in training; silent false negatives |
| [[Nikolopoulos 2025 Rare-Event-Stable Evaluation Metrics]] | RP1, RP4 | evaluation | Weak (5) | F1/MCC/AUC collapse as prevalence falls; fixed cost-ratio metrics keep thresholds stable |
| [[Pollok 2026 End-to-End Policies vs Simple Rules]] | RP1, RP4, RP5 | rl-planning | Strong (12) | Sharpe-trained transformer policy ≈ 1/N net of costs on 16 futures 2011–2024; equity result mostly beta; MoE/ensembles no help |
| [[Yu 2026 AI Crypto Backtest to Live Gap]] | RP1, RP4, RP5 | rl-planning | Strong (10) | 32 ML/RL/LLM methods: backtest ranking reverses in paper trading; none beat BTC buy-and-hold live; RL lost in backtest |
| [[Pan 2026 ReCAP Regime-Adaptive Continual Learning]] | RP1, RP4, RP5 | rl-planning | Moderate (8) | Fine-tune, replay, EWC ≈ plain retraining for RL portfolios; regime policy library adds ~15 pts (unconfirmed) |
| [[Go 2026 FinPILOT Inference-Time Planning RL]] | RP1, RP5 | rl-planning | Moderate (7) | Frozen PPO/SAC/A2C/TD3/DDPG below buy-and-hold on DJ30 2023–25; MPC-style planning with weak forecaster improves 27/30 |
| [[Maskiewicz 2025 Can AI Trade the Stock Market]] | RP1 | rl-planning | Moderate (6) | PPO-transformer beats buy-and-hold on 5 assets 2019–23; PPO-MLP worst; hand-picked settings, no tests |
| [[Wu 2026 Test-Time Adaptation Non-stationary Markets]] | RP1, RP4, RP5 | rl-planning | Moderate (6) | BN-statistics refresh small DM-significant gain; gradient norm-only adaptation hurts SPY/QQQ |
| [[Gort 2022 DRL Crypto Backtest Overfitting]] | RP1, RP4, RP5 | rl-planning | Weak (5) | PBO screening rejects over-tuned DRL agents; best agent still −35% in 2-month crash; risk switch set from test data |
| [[Wang 2023 Meta-Stock Sub-new Stock Meta-Learning]] | RP1, RP4, RP5 | rl-planning | Weak (5) | Reptile-style meta-learning gives small MCC gains on new listings; accuracy 51–57%; plain Reptile trading −79%/yr |
| [[Asaad 2026 Regime-Aware In-Context Volatility]] | RP1 | rl-planning | Weak (5) | Regime-selected LLM demonstrations cut high-vol MAE 27% vs GJR-GARCH; HAR best in calm; memorisation uncontrolled |
| [[Liu 2025 Robust Meta-Learning Zero-Shot Financial]] | RP1, RP4, RP5 | rl-planning | Weak (4) | MAML with GMM regime tasks lifts IC on unseen stocks in 2020 window; plain pre-training wins some cells |
| [[Maggiolo 2025 Deep Hedging Non-Convexity AlphaZero]] | RP1, RP5 | rl-planning | Weak (4) | AlphaZero search finds optimal hedge where gradient deep hedging fails, simulated non-convex markets only |
| [[Wang 2026 DRL Equity Actor-Critic Forward Retraining]] | RP1 | rl-planning | Weak (3) | DRL on 20 surviving mega-caps: high returns with beta 0.83–1.24; retraining halves DDPG return |
| [[Pippas 2025 RL in Quantitative Finance Survey]] | RP1, RP4, RP5 | rl-planning | Weak (review) | 167 RL papers usually beat own benchmarks, but with look-ahead, survivorship and unequal-information flaws |
| [[Ansari 2024 Chronos Language of Time Series]] | RP1 | price-time-series | Moderate (8) | Uniform-bin token model level with PatchTST/ETS zero-shot; worse than random walk on FX; bins cap range and lose precision |
| [[Ma 2026 VAIOM Continuous-Input Discrete-Output]] | RP1, RP5 | price-time-series | Moderate (7) | FX 1H: continuous input beats tokenized input with bucket output; beats LightGBM by 0.02–0.04 bits/event on 2025 test |
| [[Mai 2024 StockGPT Generative Stock Returns]] | RP1 | price-time-series | Moderate (7) | 50-bp return-token GPT trained to 2000: monthly L/S ~13%/yr, ~15% alpha 2001–23; daily result small-cap |
| [[Kim 2026 PRISM-VQ Discrete Latent Factors]] | RP1 | price-time-series | Moderate (8) | VQ codebook is the most important component for stock ranking; S&P 500 RankIC only 0.014 |
| [[Rabanser 2020 Effectiveness of Discretization Forecasting]] | RP1 | price-time-series | Weak (5) | Output binning helps WaveNet, hurts DeepAR; input binning matters less (non-finance) |
| [[Roger 2025 Small Vocabularies Tokenization TS]] | RP1 | price-time-series | Weak (2) | Bin design matters at small vocabularies; Chronos default worst at 512 tokens |
| [[Yu 2025 Implicit Biases TSFM Design Choices]] | RP1 | price-time-series | Weak (2) | Quantised vs continuous embeddings and CE vs quantile loss trade off outliers, scales, mean reversion (synthetic) |
| [[Goetz 2026 Byte Pair Encoding Time Series]] | RP1 | price-time-series | Weak (4) | BPE motif tokens beat per-value Chronos tokens and compress 2–23× (non-finance) |
| [[Talukder 2024 TOTEM Tokenized Time Series]] | RP1 | price-time-series | Weak (5) | VQ-VAE tokens beat continuous patches with a fixed forecaster (non-finance) |
| [[Montgomery 2026 Numeric Value Encoding Transformers]] | RP1 | price-time-series | Moderate (7) | In event sequences, hybrid binning is the robust default; continuous FiLM most precise (EHR, transfer) |
| [[Ansari 2026 Chronos-2 Multivariate Foundation Model]] | RP1 | price-time-series | Moderate (9) | Chronos family moved to continuous patches + quantile head; Chronos-2 leads fev-bench (not a matched ablation) |
| [[Acero 2026 What LOB Foundation Models Learn]] | RP1 | price-time-series | Weak (4) | Next-token LOB models reach Bayes optimum at ~10^5 params; regime diversity, not tokens, drives generalisation (synthetic) |
| [[Kawawa-Beaudan 2026 TradeFM Trade-Flow Foundation Model]] | RP1 | price-time-series | Moderate (6) | 524M token trade-flow model: 2–3× lower return-distribution error than Hawkes; loss power laws; realism only |
| [[Takemoto 2025 Chaotic Pretraining Scaling Bitcoin]] | RP1 | price-time-series | Weak (2) | Chaos-pretrained decoder plateaus at ~1M params; beats lag-1 rule only at ≤15 s BTC bars, pre-cost |
| [[Yao 2025 Neural Scaling Laws TSFMs]] | RP1 | price-time-series | Moderate (6) | TSFM power laws hold ID and OOD; token Chronos-T5 scales weakly (non-finance) |
| [[Lee 2026 FinVerse Financial TSFM Benchmark]] | RP1, RP4 | evaluation | Moderate (6) | 43 zero-shot TSFMs on 60K financial series: most ≈ persistence; generic rank ≠ financial rank |
| [[Decker 2026 Calibration of Probabilistic TSFMs]] | RP1, RP5 | evaluation | Moderate (7) | Token-sampling Chronos-T5 worst calibrated of 14 TSFMs; tails off >10×; worsens with horizon |
| [[Kim 2026 Dynamic Multi-Step Decoding TSFMs]] | RP1, RP4 | price-time-series | Moderate (6) | Full autoregressive rollout −3.1% MASE vs one-shot (−10.7% long horizons) (non-finance) |
| [[Cheung 2026 Base-Rate-Honest TimesFM LoRA Equities]] | RP1, RP4, RP5 | evaluation | Moderate (9) | LoRA/zero-shot TimesFM: no directional skill over always-up on S&P 500/NASDAQ-100 |
| [[Nagy 2025 LOB-Bench Generative LOB Benchmark]] | RP1 | price-time-series | Moderate (7) | Token-level LOB model best realism; all generators derail as rollouts lengthen |
| [[Fu 2024 Financial Fine-tuning TimesFM]] | RP1 | price-time-series | Moderate (6) | Finance-fine-tuned TimesFM beats original but ≈ AR(1) on S&P 500 and worse on FX |
| [[Kirtac 2026 MFAST News Trading Under Frictions]] | RP1, RP5 | sentiment | Strong (10) | Post-cutoff, net of costs: L–S Sharpe dictionary 0.68 < FinBERT 1.75 < LLaMA-3 2.85; FinBERT 13× faster |
| [[Lis 2026 ModernFinBERT News Volatility HAR]] | RP1, RP5 | sentiment | Moderate (9) | ModernFinBERT news variables beat HAR in 2/33 cells, not robust; naive lowest QLIKE |
| [[Zhang 2025 GDELT FinBERT Macro Alpha]] | RP1 | sentiment | Moderate (8) | GDELT + FinBERT aggregates: reported FX/bond Sharpe 4.6–5.9 (implausible); dispersion top feature |
| [[Jeong 2026 FinBERT Embeddings vs Scalar Sentiment]] | RP1, RP5 | sentiment | Weak (5) | Frozen FinBERT embeddings beat scalar score by 17% MSE; no directional skill |
| [[Zhu 2026 Beyond Sentiment Structured News Extraction]] | RP1 | sentiment | Weak (5) | LLM event-type/horizon fields add +0.019 F1 to FinBERT; AUROC 0.528; random splits |
| [[Paredes Amorin 2026 Conditional Sentiment Aluminum]] | RP1 | sentiment | Weak (4) | Occurred-event news Sharpe 0.62 vs forward-looking −0.01; source matters |
| [[Zhao 2026 DualCast Dual-Path Bimodal Forecasting]] | RP1 | fusion | Weak (3) | Price tokens in frozen Qwen3 + news reviser cut MAPE; 16× latency; LLM cutoff uncontrolled |
| [[Dai 2026 Multi-Dimensional Sentiment WTI]] | RP1 | sentiment | Weak (2) | GPT-4o dimensions + FinBERT AUC 0.652 vs 0.569 for WTI weekly; tiny sample |
| [[Liang 2026 TAC-Time Texts as Channels]] | RP1 | fusion | Weak (2) | Text as SAE channels; shuffled text ≤1% worse on most sets |
| [[Chen 2026 Centering Drives Normalization Gains]] | RP3 | cleaning | Moderate (9) | Per-window centering raises CSI 300 rank IC +0.014 to +0.057 for all 8 encoders; scale-only no gain |
| [[Padilha 2026 Preprocessing Impact Forecasting Benchmarks]] | RP3 | cleaning | Moderate (9) | Per-series preprocessing changes M4 MASE 27–87% and model rankings; differencing helps models without built-in normalisation |
| [[Vilhes 2026 Normalization Causal Large Time-Series Models]] | RP3 | cleaning | Moderate (8) | Whole-window stats leak in causal training; causal+arcsinh best at long contexts; no-norm worst |
| [[Ahmed 2025 Normalization Zero-Shot TSFMs]] | RP3 | cleaning | Weak (5) | Mean/s.d. normalisation cuts zero-shot MASE ~89% vs raw; token model insensitive to choice |
| [[Kapoor 2023 Leakage Reproducibility Crisis ML Science]] | RP3 | cleaning | Moderate (8) | Leakage in 329 papers/17 fields; train+test imputation and temporal k-fold overturned civil-war ML claims |
| [[Roth 2026 Which Leakage Types Matter]] | RP3, RP5 | cleaning | Moderate (9) | Full-data scaling ΔAUC <0.005; test-set selection +0.04; duplicates up to +0.07; temporal +0.023 |
| [[Passalis 2020 Deep Adaptive Input Normalization]] | RP3 | cleaning | Moderate (7) | Learned per-window normalisation lifts LOB κ 0.31 → 0.49; no normalisation fails |
| [[Stempien 2025 Fractional Differencing LSTM Indices]] | RP3 | cleaning | Moderate (6) | Fractional differences beat log returns on price-level RMSE for 4 indices; no naive baseline |
| [[purgedcv 2026 Purged Cross-Validation Library]] | RP3, RP4, RP5 | cleaning | Primary documentation | Shuffled k-fold invents R² 0.91 on unpredictable target; purged split removes it |
| [[Yang 2026 LLM Point-in-Time Economic Graphs]] | RP3 | graph | Moderate (7) | LLM 10-K graph stamped by filing date; 88% audited precision for strong edges; model-knowledge edges not point-in-time |
| [[Lu 2024 Co-Trading Networks US Equities]] | RP3 | graph | Weak (5) | Daily co-trading networks track covariance beyond GICS; GMV Sharpe 1.40 vs 0.97 (no costs) |
| [[Gopal 2021 Supply Chain Link Discovery GNN]] | RP3 | graph | Moderate (6) | GNN finds missing Bloomberg supply links; analysts confirm 21% of predictions |
| [[Onnela 2003 Dynamic Asset Trees Market Correlations]] | RP3 | graph | Weak (5) | Rolling correlation MSTs stable but reorganise at crashes; edge half-life ≈ 0.12 × window |
| [[Schwenkler 2020 Network of Firms Implied by News]] | RP3 | graph | Moderate (9) | Same-sentence news co-mentions give dated network of 2,961 firms; predicts volatility and spreads 1 month ahead |
| [[CRSP 2017 Annual Release Notes Data Edits]] | RP3 | data-sources | Primary documentation | CRSP rewrites values "for entire history", moves data between PERMNOs, re-codes reorganisations; no vintages stated |
| [[Stanford GSB 2026 CRSP Names File FAQ]] | RP3, RP5 | data-sources | Primary documentation | Names/tickers/CUSIPs as dated spells; ticker "S" reused 2005 and 2021 |
| [[NY Fed 2018 CRSP-FRB Link Documentation]] | RP3 | data-sources | Primary documentation | Dated PERMCO–RSSD links; PERMCO survives most M&A but not all reorganisations |
| [[SEC 2026 EDGAR Submissions API]] | RP3 | data-sources | Primary documentation | CIK with current and former names, tickers; former-name dates not documented |
| [[Fowler 2021 Bitemporal History]] | RP3 | storage | Primary documentation | Actual history mutable, record history append-only; use bitemporality when retroactive corrections matter |
| [[Qi 2026 Multilingual Company Entity Resolution]] | RP3 | cleaning | Moderate (7) | Better retrieval (54% → 77% recall) barely lifts cluster recall (33%); renamed/merged entities excluded |
| [[Li 2026 Impossible Trinity Time-Series Validation]] | RP4 | evaluation | Moderate (6) | No scheme has full training, coverage and causality; on noise shuffled 5-fold IC +0.32, purged 0.00; proximity of future data, not amount, leaks |
| [[Arian 2024 Backtest Overfitting ML Era]] | RP4 | evaluation | Weak (5) | Abstract only: CPCV lowest PBO and best DSR in synthetic markets; walk-forward worst; purged k-fold ≈ k-fold |
| [[Cerqueira 2020 Evaluating Time Series Forecasting Models]] | RP4 | evaluation | Moderate (9) | 62 real series: time-ordered hold-outs estimate future error best; CV optimistic, worst on non-stationary series |
| [[Bergmeir 2018 Validity of Cross-Validation Autoregressive]] | RP4 | evaluation | Moderate (6) | k-fold CV valid and more precise than hold-out for AR models with uncorrelated errors; fails when underfitted |
| [[Lusompa 2025 Finite Sample Bias Time Series CV]] | RP4 | evaluation | Weak (1) | Theory: CV model selection biased in finite samples even with martingale-difference errors; prefer block CV |
| [[Nikolopoulos 2026 Spurious Predictability Financial ML]] | RP4, RP5 | evaluation | Moderate (9) | Best of K grows like √(2 ln K) under null; falsify pipelines on synthetic nulls; measure IS–walk-forward gap |
| [[Bailey 2017 Probability of Backtest Overfitting]] | RP4, RP5 | evaluation | Moderate (7) | PBO via CSCV; hold-out ignores number of trials; example: all IS Sharpe positive, ~78% OOS negative |
| [[Bailey 2014 Deflated Sharpe Ratio]] | RP4, RP5 | evaluation | Weak (5) | Abstract only: DSR corrects Sharpe significance for number of trials and non-normal returns |
| [[skfolio 2026 Cross-Validation Model Selection]] | RP4 | evaluation | Primary documentation | Resampled walk-forward paths: OOS Sharpe 0.36 ± 0.38 vs 0.50 ± 0.32; single path hides spread |
| [[Albelali 2025 Hidden Leaks LSTM Validation]] | RP4 | evaluation | Moderate (6) | Windows built before splitting: unpurged 10-fold understates error up to 20.5%; chronological splits ≤5% |
| [[Bauer 2025 DM and MCS Tail Risk Finite Sample]] | RP4 | evaluation | Weak (5) | Simulation: DM and MCS have little power against tail-underestimating 1–2.5% VaR/ES models below ~2 years; type III errors; MCS can drop the true model |
| [[Coelho 2026 Tail Forecast Comparison Exceedances]] | RP4 | evaluation | Strong (11) | Effective sample in tail comparisons = exceedances; DM favours less conservative model when few; bootstrap-t DM or confidence sequences fix it |
| [[Frederiksen 2026 Heavy Tails Predictive Ability Testing]] | RP4 | evaluation | Moderate (7) | Infinite-variance loss differentials: nominal 5% DM rejects true null up to 70%; subsampling valid; overturns GARCH-dominance in FX |
| [[Diebold 2015 Comparing Predictive Accuracy Twenty Years Later]] | RP4 | evaluation | Weak (2) | Essay: DM compares forecasts, not models; full-sample procedures better for model comparison |
| [[Hansen 2011 Model Confidence Set]] | RP4 | evaluation | Moderate (9) | MCS keeps all models not separable from the best at a stated confidence; large set when data uninformative |
| [[Clark 2007 Tests for Nested Model Predictive Accuracy]] | RP4, RP5 | evaluation | Moderate (7) | Nested vs random walk: plain DM median size 0.008 at 10%; MSPE-adjusted 0.080 with better power |
| [[Harvey 2016 Cross-Section Expected Returns Multiple Testing]] | RP4, RP5 | evaluation | Strong (12) | 316 factors: new factor needs t > ~3.0 (FDR/FWER); hidden tests raise it to 3.18–4.01 |
| [[Hansen 2005 Test for Superior Predictive Ability]] | RP4 | evaluation | Moderate (7) | SPA studentised and recentred beats Reality Check: power 99.7% vs 5.5% in one design; RC easy to manipulate |
| [[Sullivan 1999 Data-Snooping Technical Trading Bootstrap]] | RP4 | evaluation | Moderate (9) | 7,846 rules: best rule OOS 1987–96 nominal p 0.004 → Reality Check p 0.341; futures RC p 0.908 |
| [[Nolde 2017 Elicitability and Backtesting]] | RP4 | evaluation | Moderate (8) | Traditional backtests cannot rank methods; comparative backtests with consistent (VaR, ES) scores; two-stage traffic-light scheme |
| [[Wang 2025 E-backtesting]] | RP4 | tail-risk | Moderate (7) | Model-free, anytime-valid ES backtest via e-values; detects before 2008 losses; less power than model-based tests |
| [[Tokajuk 2026 Loss Choice Crypto Volatility]] | RP4 | evaluation | Moderate (8) | Training-loss effect 2.9× model effect, mostly forecast level; alignment cuts it 77%; VaR breach range 1.3–6.3% → 3.5–3.6% |
| [[Chagas 2026 Latent-Regime Bias Auditing Volatility]] | RP4 | evaluation | Moderate (8) | Near-equal RMSE hides regime bias; rankings change under tail-weighted loss; HAR rises, Transformers fall |
| [[Patton 2011 Volatility Forecast Comparison Imperfect Proxies]] | RP4 | evaluation | Moderate (6) | Only robust family (MSE, QLIKE) ranks correctly with noisy proxies; MAE optimum ~0.45σ² with squared returns |
| [[Drehmann 2014 Evaluating Early Warning Indicators]] | RP4 | novelty-detection | Moderate (7) | EWI evaluation: AUROC, 1–5-year window, persistence, post-crisis exclusion; credit gap and DSR AUROC >0.9 (2012 draft) |
| [[Gneiting 2007 Strictly Proper Scoring Rules]] | RP4 | evaluation | Weak (4) | Use strictly proper scores (log, CRPS, quantile, interval); improper scores reward wrongly dispersed forecasts |
| [[Cortesi 2026 Optimizer as Implicit Prior]] | RP4, RP5 | evaluation | Strong (12) | S&P 500 volatility: 59/66 model pairs tied, none beat HAR; optimizer changes learned function and portfolio turnover (up to 58%) |
| [[Guo 2026 Benign Overfitting Equity Returns]] | RP4 | evaluation | Strong (11) | Causally tuned ridge on 12,000 RFFs collapses to the historical average; "virtue of complexity" alpha vanishes |
| [[Le Grice 2026 Cross-Regime Bayesian Optimisation]] | RP4 | evaluation | Moderate (6) | Cross-regime tuning, fixed objective weights; no tabular DL beats XGBoost; XGBoost+TabNet ensemble Sharpe 2.44 in one year (outlier) |
| [[Coolsaet 2026 Index Pre-Training Stock Transformers]] | RP4 | price-time-series | Weak (3) | Index pre-training rescues a stock transformer (BCE 0.694 → 0.640) but XGBoost wins on F1 and returns |
| [[Coakley 2026 Deep Learning Performance Distributions]] | RP4 | evaluation | Moderate (8) | 100 seeds per config: TS forecasters non-Gaussian, ~3× more underperforming outliers; early stopping best |
| [[Kim 2025 Deep Ensembles Portfolio DSL]] | RP4 | evaluation | Moderate (9) | Seed ensembles 1→64 raise median Sharpe and narrow spread; rolling universes only match EW/VW |
| [[Ye 2026 Hindcast Replaying Prediction Markets]] | RP4 | evaluation | Weak (9, capped) | Replay against immutable archive with per-event cutoff closes the retrieval leak; retrieval helps only where pre-event coverage exists |
| [[Goldsmith-Pinkham 2025 Causal Inference Event Studies]] | RP4 | evaluation | Strong (11) | Factor-model abnormal returns biased in volatile periods, long horizons, non-random timing; synthetic controls fix much of it |
| [[Farzulla 2026 Crypto Event Study Dependence-Robust]] | RP4 | evaluation | Moderate (8) | Curated vs mechanical event selection 3.49× vs 0.5–1.6×; naive test rejects 35.1% of true nulls |
| [[Kolari 2010 Event Study Cross-Sectional Correlation]] | RP4 | evaluation | Weak (5, abstract) | Event-date clustering with low cross-correlation causes over-rejection; adjusted BMP test |
| [[Zhang 2026 Deep TS Models Equity Portfolios]] | RP4, RP5 | evaluation | Strong (12) | Gross decile Sharpe up to 3.88; turnover decides 20 bps survival; all constrained portfolios net-negative |
| [[Bysik 2026 ML Bitcoin Trading Transaction Costs]] | RP4 | evaluation | Moderate (8) | Hourly BTC ML strategies lose 50–99%/yr at 10 bps; cost threshold filter restores some profit, not significant vs buy-and-hold |
| [[Smerlak 2026 Optimal Trading Filters Signal Value]] | RP4 | evaluation | Weak (2, theory) | With costs, equal-accuracy signals differ in value; value = friction-weighted forecast of future drift |
| [[Yin 2026 Implementation Risk Backtest Engines]] | RP4 | evaluation | Strong (10) | Five engines agree at zero cost; diverge with turnover up to 3.71 pp; seven engine defects found |
| [[Avramov 2023 ML vs Economic Restrictions]] | RP4 | evaluation | Weak (5, abstract) | ML profits concentrate in hard-to-arbitrage stocks; restrictions and costs attenuate them |
| [[Jensen 2026 ML Implementable Efficient Frontier]] | RP4, RP5 | evaluation | Moderate (9) | Cost-blind ML portfolios not implementable; cost-aware Portfolio-ML net Sharpe 1.38 vs 1.11–1.16 |
| [[Perignon 2024 Computational Reproducibility Finance]] | RP4 | evaluation | Weak (5, abstract) | Rerunning authors' code on same data reproduces exactly only 52% of 1,000+ finance results |
| [[Menkveld 2024 Nonstandard Errors]] | RP4 | evaluation | Moderate (9) | 164 teams, same data: estimate spread ≈ 2× standard error; peer feedback cuts it 47% |
| [[Zhou 2026 Determinism Financial AI Survey]] | RP4 | evaluation | Weak (5) | Seeds not enough: GPU/framework nondeterminism; 15.5–27.5% label flips across seeds on Elliptic |
