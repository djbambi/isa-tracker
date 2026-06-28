from iss_tracker.adapters.fake_iss import get_screen_data
from iss_tracker.domain.models import ScreenData


def test_fake_iss() -> None:
    screen_data = get_screen_data()
    assert isinstance(screen_data, ScreenData)
