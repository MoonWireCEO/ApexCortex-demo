
import numpy as np, pandas as pd

def synthetic_bars(seed: int = 42, n_days: int = 5, freq: str = "5min") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    periods = n_days * (24 * (60 // 5)) if freq == "5min" else n_days * 24
    idx = pd.date_range("2024-01-01", periods=periods, freq=freq)
    rets = rng.normal(0, 0.001, len(idx))
    price = 100 * (1 + pd.Series(rets, index=idx)).cumprod()
    df = pd.DataFrame(index=idx)
    df["close"] = price
    df["open"] = df["close"].shift(1).fillna(df["close"])
    df["high"] = df[["open","close"]].max(axis=1) * (1 + np.abs(rng.normal(0.0002, 0.0005, len(df))))
    df["low"]  = df[["open","close"]].min(axis=1) * (1 - np.abs(rng.normal(0.0002, 0.0005, len(df))))
    df["volume"] = rng.uniform(100, 200, len(df))
    return df
