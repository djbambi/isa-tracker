import datetime

import requests

from iss_tracker.domain.models import ScreenData

iss_url = "http://api.open-notify.org/iss-now.json"



def get_screen_data() -> ScreenData:
    response = requests.get(iss_url)
    json_response = response.json()

    return ScreenData(
        latitude=float(json_response["iss_position"]["latitude"]),
        longitude=float(json_response["iss_position"]["longitude"]),
        region="unknown",
        next_visible=datetime.datetime.now(tz=datetime.UTC),
        timestamp=datetime.datetime.fromtimestamp(json_response["timestamp"], tz=datetime.UTC)
    )

