from pathlib import Path
import pandas as pd


def append_prediction_log(log_path: Path, prediction_record: dict) -> None:
    if log_path.exists():
        log_df = pd.read_csv(log_path)
    else:
        log_df = pd.DataFrame()

    updated_df = pd.concat([log_df, pd.DataFrame([prediction_record])], ignore_index=True)
    updated_df.to_csv(log_path, index=False)

    