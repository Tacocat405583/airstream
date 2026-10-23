"""OpenSky Network API client.

Implementation order:
  1. fetch_token()  - OAuth2 client-credentials token from the auth server
  2. get_states()   - hit /states/all with a BoundingBox
  3. study the raw response (scripts/explore_opensky.py), then parse into FlightState
"""

from __future__ import annotations

from typing import Any

import httpx

from airstream.config import Settings
from airstream.models import BoundingBox, FlightState


class OpenSkyAuthError(RuntimeError):
    """Raised when a token cannot be obtained."""


class OpenSkyClient:
    def __init__(self, settings: Settings, http: httpx.Client | None = None) -> None:
        self._settings = settings
        self._http = http or httpx.Client(timeout=10.0)
        self._token: str | None = None
        self._token_expires_at: float = 0.0

    def fetch_token(self) -> str:
        """Request an access token using client_id / client_secret.

        TODO:
          - POST to settings.opensky_token_url with grant_type=client_credentials
          - store access_token and compute expiry from expires_in
          - raise OpenSkyAuthError on non-2xx
        """
        raise NotImplementedError

    def _auth_headers(self) -> dict[str, str]:
        """TODO: refresh the token if missing/expired, return the Bearer header."""
        raise NotImplementedError

    def get_states_raw(self, bbox: BoundingBox | None = None) -> dict[str, Any]:
        """GET /states/all, optionally limited to a bounding box. Returns raw JSON.

        TODO: call f"{settings.opensky_api_url}/states/all" with bbox.as_params()
        """
        raise NotImplementedError

    def get_states(self, bbox: BoundingBox | None = None) -> list[FlightState]:
        """TODO: parse get_states_raw()["states"] into FlightState objects."""
        raise NotImplementedError

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> OpenSkyClient:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
