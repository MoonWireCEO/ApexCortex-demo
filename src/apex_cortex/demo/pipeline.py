
import pandas as pd
from .features import make_demo_features
from .model import train_logreg, to_signal
from ..validation.wf_cv import simple_walk_forward

def train_and_validate(df: pd.DataFrame):
    feats = make_demo_features(df)
    X = feats[["r_1","r_3","r_6","atr_14","sma_gap"]]
    y = (feats["y"] > 0).astype(int)
    model = train_logreg(X, y)
    proba = pd.Series(model.predict_proba(X)[:,1], index=feats.index, name="proba")
    feats = feats.join(proba)
    feats["signal"] = to_signal(feats["proba"], threshold=0.5)
    metrics = simple_walk_forward(feats, n_splits=3)
    bundle = {"model": model, "features": list(X.columns)}
    return metrics, bundle
