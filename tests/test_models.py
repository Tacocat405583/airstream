import pytest

from airstream.models import BoundingBox


def test_bbox_as_params():
    bbox = BoundingBox(24.5, -125.0, 49.5, -66.9)
    assert bbox.as_params() == {"lamin": 24.5, "lomin": -125.0, "lamax": 49.5, "lomax": -66.9}


@pytest.mark.parametrize(
    "args",
    [
        (50, -125, 40, -66),  # lamin > lamax
        (-100, -125, 40, -66),  # lat out of range
        (24, -66, 49, -125),  # lomin > lomax
        (24, -200, 49, -66),  # lon out of range
    ],
)
def test_bbox_rejects_invalid(args):
    with pytest.raises(ValueError):
        BoundingBox(*args)
