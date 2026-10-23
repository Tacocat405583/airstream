"""OpenSky client tests. Un-skip each one as you implement the matching method.

Use respx to mock httpx calls, e.g.:
    @respx.mock
    def test_...(settings):
        respx.post(settings.opensky_token_url).mock(return_value=httpx.Response(200, json={...}))
"""

import pytest

pytestmark = pytest.mark.skip(reason="OpenSky client not implemented yet")


def test_fetch_token_success(settings):
    # TODO: mock token endpoint, assert token is returned and cached
    ...


def test_fetch_token_failure_raises(settings):
    # TODO: mock 401, assert OpenSkyAuthError
    ...


def test_get_states_raw_sends_bbox_params(settings):
    # TODO: mock /states/all, assert lamin/lomin/lamax/lomax in request query
    ...


def test_get_states_parses_state_vectors(settings):
    # TODO: use a saved fixture from data/raw to assert FlightState parsing
    ...
