# Airstream

Real-time data pipeline: flights (OpenSky) and weather (NWS API) streamed through Kafka,
validated by a data quality layer, stored, joined, and shown on a live map.

## End goal (context only - don't build ahead)
- Two sources, OpenSky (flights) and NWS (weather), polled on schedules.
- Producers push raw records into Kafka topics.
- **The data quality layer is the core of the project, not an add-on.** It validates every
  record for schema, value ranges, freshness, completeness, and duplicates. Bad records go to
  a quarantine topic rather than being dropped silently, and failure counts are tracked over time.
- Clean data is stored and joined: each flight is matched to current weather near it.
- A live map shows flights over current conditions.
- Keep ingestion, validation, and storage as separate layers in the code.
- **Never fold validation into ingestion.** Clients fetch and reshape only. They never filter,
  fix, or drop records. Every validation decision lives in the quality layer.

**Current stage:** OpenSky client only.

## Planned extension
Wildfire smoke segmentation on GOES satellite imagery, labeled with NOAA HMS smoke
polygons and NASA FIRMS hotspots.

## Goals
- Portfolio project aimed at data platform roles (e.g. Spectrum Data Platforms team).
- Priorities: tests, CI/CD, a clean README.

## Working agreements
- Keep scaffolding minimal and step by step. Scaffold only what the current stage needs,
  and don't overdo it.
- Claude does general scaffolding only. The owner writes the core logic, starting with the
  OpenSky API client: token auth, then bounding-box queries, then studying the response.
  Leave `TODO` stubs with `NotImplementedError` instead of implementing it.
- For core logic, the owner writes the code and Claude reviews: explain concepts, point out
  bugs, suggest fixes, but don't rewrite the owner's implementation unless asked.
- Runs locally in `.venv` for now; Docker comes when Kafka is added.
- The owner builds the streaming layer (Kafka producers/consumers, docker-compose) from
  scratch. Do not scaffold it.
- Commit after every change.
- Keep `docs/decisions.md` up to date: tick off progress items and add an entry
  for each meaningful decision (newest at the top). It's the owner's project memory.
- Do NOT add Claude as a co-author or contributor in commits or PRs.

## Layout
- `src/airstream/clients/` - API clients (OpenSky, NWS)
- `src/airstream/models.py` - shared data models
- `src/airstream/quality/` - data quality checks
- `docs/decisions.md` - decision log and progress tracker
- `scripts/` - exploration scripts for poking at raw API responses
- `tests/` - pytest suite

## Commands
- Install: `pip install -e ".[dev]"`
- Tests: `pytest`
- Lint: `ruff check .`
