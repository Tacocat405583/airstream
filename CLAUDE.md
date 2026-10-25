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
  fix, or drop records. Validation happens at the Kafka stage, downstream:
  `client -> producer -> raw topic -> validator (consumer) -> clean topic | quarantine topic`

**Current stage:** OpenSky client only.

## Planned extension
Wildfire smoke segmentation on GOES satellite imagery, labeled with NOAA HMS smoke
polygons and NASA FIRMS hotspots.

## Goals
- Portfolio project aimed at data platform roles (e.g. Spectrum Data Platforms team).
- Priorities: tests, CI/CD, a clean README.

## Working agreements
- **The owner writes all source code, tests included.** That covers class design, module
  structure, naming, and library choices. Interviews focus on OOP, so the design must be theirs.
- Claude does NOT write code stubs, skeletons, class outlines, or suggested method names in
  the repo. Claude's role: review the owner's code, explain concepts, answer questions, and
  point out bugs. Don't hand over full implementations unless explicitly asked.
- Setup and tooling files (pyproject, CI, .gitignore, README, docs) are fine for Claude to
  maintain when asked.
- Runs locally in `.venv` for now; Docker comes when Kafka is added.
- Commit after every change.
- Keep `docs/decisions.md` up to date: tick off progress items and add an entry
  for each meaningful decision (newest at the top). It's the owner's project memory.
- Do NOT add Claude as a co-author or contributor in commits or PRs.

## Layout
- `src/airstream/` - source package (owner-designed)
- `tests/` - pytest suite (owner-written)
- `docs/decisions.md` - decision log and progress tracker

## Commands
- Install: `pip install -e ".[dev]"`
- Tests: `pytest`
- Lint: `ruff check .`
