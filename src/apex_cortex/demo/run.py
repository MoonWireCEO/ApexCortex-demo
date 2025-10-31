
from .data import synthetic_bars
from .pipeline import train_and_validate
from .governance import evaluate
from .artifacts import write
import pandas as pd

def main():
    df = synthetic_bars(seed=42, n_days=5, freq="5min")
    metrics, bundle = train_and_validate(df)
    decision = evaluate(metrics)
    write(bundle, metrics, decision)
    print(pd.DataFrame([metrics]).to_string(index=False))

if __name__ == "__main__":
    main()
