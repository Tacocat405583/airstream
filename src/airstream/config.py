"""Runtime settings loaded from environment variables / .env."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="AIRSTREAM_", extra="ignore")

    # OpenSky (OAuth2 client credentials)
    opensky_client_id: str = ""
    opensky_client_secret: str = ""
    opensky_token_url: str = (
        "https://auth.opensky-network.org/auth/realms/opensky-network"
        "/protocol/openid-connect/token"
    )
    opensky_api_url: str = "https://opensky-network.org/api"

    # NWS requires a descriptive User-Agent with contact info
    nws_api_url: str = "https://api.weather.gov"
    nws_user_agent: str = "airstream (you@example.com)"

    poll_interval_seconds: int = 15


def get_settings() -> Settings:
    return Settings()
