"""Shared data models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


@dataclass(frozen=True)
class BoundingBox:
    """Geographic box in WGS84 degrees."""

    lamin: float
    lomin: float
    lamax: float
    lomax: float

    def __post_init__(self) -> None:
        if not (-90 <= self.lamin < self.lamax <= 90):
            raise ValueError(f"invalid latitude range: {self.lamin}..{self.lamax}")
        if not (-180 <= self.lomin < self.lomax <= 180):
            raise ValueError(f"invalid longitude range: {self.lomin}..{self.lomax}")

    def as_params(self) -> dict[str, float]:
        """Query params in the shape OpenSky's /states/all expects."""
        return {"lamin": self.lamin, "lomin": self.lomin, "lamax": self.lamax, "lomax": self.lomax}


class FlightState(BaseModel):
    """One aircraft state vector from OpenSky.

    Fields will be filled in once the raw response has been studied
    (see scripts/explore_opensky.py).
    """

    icao24: str
    # TODO: add fields (callsign, lat/lon, altitude, velocity, ...) after studying the response

    @classmethod
    def from_state_vector(cls, raw: list[Any]) -> FlightState:
        # TODO: map the positional state-vector list to named fields
        raise NotImplementedError


class WeatherObservation(BaseModel):
    """A point weather observation from NWS."""

    station_id: str
    # TODO: add fields (timestamp, temperature, wind, visibility, ...)
