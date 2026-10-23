# Airstream

Real-time pipeline that streams weather data (NWS API) and live flight data (OpenSky)
through Kafka, runs data quality checks, and feeds a live map that shows flights over
current conditions.

## Planned extension
Wildfire smoke segmentation on GOES satellite imagery, labeled with NOAA HMS smoke
polygons and NASA FIRMS hotspots.

## Goals
- Portfolio project aimed at data platform roles (e.g. Spectrum Data Platforms team).
- Priorities: tests, CI/CD, a clean README.

## Working agreements
- Claude does general scaffolding only. The owner writes the core logic, starting with the
  OpenSky API client: token auth, then bounding-box queries, then studying the response.
  Leave `TODO` stubs with `NotImplementedError` instead of implementing it.
- The owner builds the streaming layer (Kafka producers/consumers, docker-compose) from
  scratch. Do not scaffold it.
- Commit after every change.
- Do NOT add Claude as a co-author or contributor in commits or PRs.

## Layout
- `src/airstream/clients/` - API clients (OpenSky, NWS)
- `src/airstream/models.py` - shared data models
- `src/airstream/quality/` - data quality checks
- `scripts/` - exploration scripts for poking at raw API responses
- `tests/` - pytest suite

## Commands
- Install: `pip install -e ".[dev]"`
- Tests: `pytest`
- Lint: `ruff check .`
