
import numpy as np, pandas as pd

def make_demo_features(df: pd.DataFrame) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    out["ret"] = df["close"].pct_change().fillna(0.0)
    out["r_1"] = out["ret"].rolling(1).sum().fillna(0.0)
    out["r_3"] = out["ret"].rolling(3).sum().fillna(0.0)
    out["r_6"] = out["ret"].rolling(6).sum().fillna(0.0)
    tr = (df["high"] - df["low"]).abs()
    out["atr_14"] = tr.rolling(14).mean().fillna(tr.mean())
    out["sma_gap"] = (df["close"] / df["close"].rolling(20).mean() - 1.0).fillna(0.0)
    out["y"] = np.sign(out["ret"].shift(-1)).replace(0, 1).fillna(1.0)
    return out.dropna()
