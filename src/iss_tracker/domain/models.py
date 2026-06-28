from dataclasses import dataclass
from datetime import datetime


@dataclass
class ScreenData:
    latitude: float
    longitude: float
    region: str  # land/water mass
    next_visible: datetime
    timestamp: datetime  # when this data was fetched
