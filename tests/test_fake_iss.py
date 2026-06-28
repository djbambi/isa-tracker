from datetime import datetime

from iss_tracker.adapters.fake_iss import get_screen_data
from iss_tracker.domain.models import ScreenData


def test_fake_iss() -> None:
    screen_data = get_screen_data()
    assert isinstance(screen_data, ScreenData)

def test_fake_value() -> None:
    screen_data = get_screen_data()
    assert screen_data.latitude == -43.19
    assert screen_data.longitude == -84.5
    assert screen_data.region == "South America"
    assert screen_data.next_visible == datetime(2026, 6, 29, 2, 39, 0)
    assert screen_data.timestamp == datetime(2026, 6, 28, 19, 42, 0)
