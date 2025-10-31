
import numpy as np
import pandas as pd

def profit_factor(pnl: pd.Series) -> float:
    gains = pnl[pnl > 0].sum()
    losses = -pnl[pnl < 0].sum()
    if losses == 0:
        return float('inf') if gains > 0 else 1.0
    return float(gains / losses)

def win_rate(pnl: pd.Series) -> float:
    return float((pnl > 0).mean()) if len(pnl) else 0.0

def max_drawdown(equity: pd.Series) -> float:
    roll_max = equity.cummax()
    dd = (equity - roll_max) / roll_max
    return float(dd.min()) if len(dd) else 0.0
