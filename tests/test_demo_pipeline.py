
from apex_cortex.demo.data import synthetic_bars
from apex_cortex.demo.pipeline import train_and_validate

def test_pipeline_runs():
    df = synthetic_bars(n_days=2)
    metrics, bundle = train_and_validate(df)
    assert "pf" in metrics and "wr" in metrics and "max_dd" in metrics
    assert isinstance(bundle.get("features"), list)
