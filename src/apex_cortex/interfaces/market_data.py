
from typing import Protocol
import pandas as pd
from datetime import datetime

class MarketData(Protocol):
    def bars(self, symbol: str, start: datetime, end: datetime, interval: str) -> pd.DataFrame: ...
