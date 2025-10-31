
from typing import Protocol
import pandas as pd

class Regime(Protocol):
    def tag(self, df: pd.DataFrame) -> pd.Series: ...
