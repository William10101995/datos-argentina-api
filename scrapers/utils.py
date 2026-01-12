from pathlib import Path
from datetime import date
import json


def save_dataset_json(dataset: str, data, versioned: bool = True):
    """
    Guarda data/<dataset>/latest.json
    y opcionalmente data/<dataset>/YYYY-MM-DD.json
    """

    base_dir = Path(__file__).resolve().parents[1]
    out_dir = base_dir / "data" / dataset
    out_dir.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()

    if versioned:
        dated_file = out_dir / f"{today}.json"
        with dated_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    latest_file = out_dir / "latest.json"
    with latest_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"📁 Dataset '{dataset}' guardado en {out_dir}")
