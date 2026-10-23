"""Record-level data quality checks.

Each check returns a list of human-readable problems (empty list = record is clean).
"""

from __future__ import annotations

from airstream.models import FlightState, WeatherObservation


def check_flight(state: FlightState) -> list[str]:
    """TODO: e.g. lat/lon in range, non-negative altitude, stale timestamp, missing callsign."""
    raise NotImplementedError


def check_weather(obs: WeatherObservation) -> list[str]:
    """TODO: e.g. plausible temperature range, null-heavy observations, stale timestamp."""
    raise NotImplementedError
