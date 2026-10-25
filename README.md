# Airstream

A real-time pipeline that streams weather data from the National Weather Service API and
live flight data from OpenSky, runs data quality checks, and feeds a live map that shows
flights over current conditions.

> Status: early development. Building the OpenSky client first.

## Architecture

```
OpenSky /states/all ─┐
                     ├─> producers ─> Kafka ─> consumers ─> quality checks ─> live map
NWS observations ────┘
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
cp .env.example .env           # then fill in your OpenSky client credentials
```

OpenSky uses OAuth2 client credentials. Create an API client on your OpenSky account page
to get a `client_id` and `client_secret`.

## Development

```bash
pytest          # run tests
ruff check .    # lint
```

## Roadmap

- [ ] OpenSky client: token auth, bounding-box queries, state-vector parsing
- [ ] NWS client: point lookup, latest station observations
- [ ] Kafka streaming layer
- [ ] Data quality checks
- [ ] Live map
- [ ] Extension: wildfire smoke segmentation on GOES imagery (NOAA HMS smoke polygons +
      NASA FIRMS hotspots as labels)
