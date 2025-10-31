
from typing import Protocol, Dict, Any

class Governance(Protocol):
    def evaluate(self, metrics: Dict[str, float]) -> Dict[str, Any]: ...
