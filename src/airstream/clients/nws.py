"""National Weather Service (api.weather.gov) client.

No API key needed, but NWS requires a User-Agent header with contact info.
Typical flow: /points/{lat},{lon} -> observation stations -> latest observation.
"""

from __future__ import annotations

from typing import Any

import httpx

from airstream.config import Settings
from airstream.models import WeatherObservation


class NWSClient:
    def __init__(self, settings: Settings, http: httpx.Client | None = None) -> None:
        self._settings = settings
        self._http = http or httpx.Client(
            timeout=10.0,
            headers={"User-Agent": settings.nws_user_agent, "Accept": "application/geo+json"},
        )

    def get_point(self, lat: float, lon: float) -> dict[str, Any]:
        """TODO: GET /points/{lat},{lon}"""
        raise NotImplementedError

    def get_latest_observation(self, station_id: str) -> WeatherObservation:
        """TODO: GET /stations/{station_id}/observations/latest and parse."""
        raise NotImplementedError

    def close(self) -> None:
        self._http.close()
