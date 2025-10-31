
import json, os, time, pickle

def write(bundle: dict, metrics: dict, decision: dict, out_dir: str = "artifacts"):
    os.makedirs(out_dir, exist_ok=True)
    ts = int(time.time())
    with open(os.path.join(out_dir, f"model_{ts}.pkl"), "wb") as f:
        pickle.dump(bundle["model"], f)
    with open(os.path.join(out_dir, f"manifest_{ts}.json"), "w") as f:
        json.dump({"features": bundle["features"]}, f, indent=2)
    with open(os.path.join(out_dir, f"metrics_{ts}.json"), "w") as f:
        json.dump(metrics, f, indent=2)
    with open(os.path.join(out_dir, f"decision_{ts}.json"), "w") as f:
        json.dump(decision, f, indent=2)
