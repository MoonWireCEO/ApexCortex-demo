
import numpy as np
import pandas as pd
from .metrics import profit_factor, win_rate, max_drawdown

def simple_walk_forward(df: pd.DataFrame, n_splits: int = 3) -> dict:
    n = len(df)
    folds = []
    for k in range(1, n_splits+1):
        cut = int(n * k / (n_splits+1))
        train = df.iloc[:cut]
        test  = df.iloc[cut:]
        if len(test) < 2 or len(train) < 2:
            continue
        pnl = test["signal"].shift(1).fillna(0) * test["ret"].fillna(0)
        eq  = (1 + pnl).cumprod()
        folds.append({"pf": profit_factor(pnl), "wr": win_rate(pnl), "mdd": max_drawdown(eq)})
    if not folds:
        return {"pf": 1.0, "wr": 0.5, "max_dd": 0.0}
    pf = float(np.mean([f["pf"] for f in folds]))
    wr = float(np.mean([f["wr"] for f in folds]))
    mdd = float(np.mean([f["mdd"] for f in folds]))
    return {"pf": pf, "wr": wr, "max_dd": mdd}
