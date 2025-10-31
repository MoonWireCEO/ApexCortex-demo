
from typing import Protocol
import pandas as pd

class FeatureGen(Protocol):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame: ...
