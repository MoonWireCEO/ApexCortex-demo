
from typing import Protocol, Dict, Any
import pandas as pd

class Validator(Protocol):
    def walk_forward(self, data: pd.DataFrame, config: Dict[str, Any]) -> Dict[str, float]: ...
