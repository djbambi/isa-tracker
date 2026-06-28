from datetime import datetime

from iss_tracker.domain.models import ScreenData


def get_screen_data() -> ScreenData:
    return ScreenData(
        latitude=-43.19,
        longitude=-84.50,
        region="South America",
        next_visible=datetime(2026, 6, 29, 2, 39, 0),
        timestamp=datetime(2026, 6, 28, 19, 42, 0),
    )
