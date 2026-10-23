"""Poll APIs and publish records to Kafka."""

from __future__ import annotations

from airstream.config import Settings
from airstream.models import BoundingBox


def run_flight_producer(settings: Settings, bbox: BoundingBox) -> None:
    """TODO: loop: OpenSkyClient.get_states(bbox) -> produce to settings.kafka_flights_topic."""
    raise NotImplementedError


def run_weather_producer(settings: Settings, stations: list[str]) -> None:
    """TODO: loop: NWSClient.get_latest_observation -> produce to settings.kafka_weather_topic."""
    raise NotImplementedError
