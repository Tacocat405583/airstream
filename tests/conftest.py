import pytest

from airstream.config import Settings


@pytest.fixture
def settings() -> Settings:
    return Settings(opensky_client_id="test-id", opensky_client_secret="test-secret")
