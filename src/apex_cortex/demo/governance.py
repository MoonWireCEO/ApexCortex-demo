
def evaluate(metrics: dict) -> dict:
    promote = (metrics.get("pf", 1.0) >= 1.05) and (metrics.get("max_dd", 0.0) >= -0.30)
    return {"action": "PROMOTE" if promote else "REJECT",
            "criteria": {"pf_min": 1.05, "max_dd_min": -0.30}}
