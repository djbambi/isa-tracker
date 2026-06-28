from datetime import datetime

from iss_tracker.domain.models import ScreenData


def test_screen_data_fields() -> None:

    my_position = ScreenData(
        latitude=54.8698,
        longitude=-1.4833,
        region="North Sea",
        next_visible=datetime(2026, 6, 28, 0, 0, 0),
        timestamp=datetime(2026, 6, 27, 0, 0, 0),
    )

    assert my_position.latitude == 54.8698
    assert my_position.longitude == -1.4833
    assert my_position.region == "North Sea"
    assert my_position.next_visible == datetime(2026, 6, 28, 0, 0, 0)
    assert my_position.timestamp == datetime(2026, 6, 27, 0, 0, 0)


def test_screen_data_equality() -> None:

    my_position = ScreenData(
        latitude=54.8698,
        longitude=-1.4833,
        region="North Sea",
        next_visible=datetime(2026, 6, 28, 0, 0, 0),
        timestamp=datetime(2026, 6, 27, 0, 0, 0),
    )

    my_position_2 = ScreenData(
        latitude=54.8698,
        longitude=-1.4833,
        region="North Sea",
        next_visible=datetime(2026, 6, 28, 0, 0, 0),
        timestamp=datetime(2026, 6, 27, 0, 0, 0),
    )
    assert my_position == my_position_2
