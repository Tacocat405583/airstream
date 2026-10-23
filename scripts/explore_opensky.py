"""Hit OpenSky once and dump the raw response so you can study its shape.

Usage:
    python scripts/explore_opensky.py --bbox 24.5 -125 49.5 -66.9
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from airstream.clients.opensky import OpenSkyClient
from airstream.config import get_settings
from airstream.models import BoundingBox


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bbox", nargs=4, type=float, metavar=("LAMIN", "LOMIN", "LAMAX", "LOMAX"))
    parser.add_argument("--out", type=Path, default=Path("data/raw/opensky_states.json"))
    args = parser.parse_args()

    bbox = BoundingBox(*args.bbox) if args.bbox else None
    with OpenSkyClient(get_settings()) as client:
        raw = client.get_states_raw(bbox)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(raw, indent=2))
    print(f"time={raw.get('time')} states={len(raw.get('states') or [])} -> {args.out}")


if __name__ == "__main__":
    main()
