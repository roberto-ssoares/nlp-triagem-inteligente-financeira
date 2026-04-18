from pathlib import Path
import json
from datetime import datetime
import uuid

import joblib
import pandas as pd
from fastapi import FastAPI

from src.api.schemas import PredictionRequest, PredictionResponse
from src.monitoring.logging_utils import append_prediction_log


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "baseline" / "tfidf_logreg_pipeline.joblib"
LABEL_MAPPING_PATH = PROJECT_ROOT / "data" / "03-gold" / "label_mapping.csv"
METADATA_PATH = PROJECT_ROOT / "models" / "baseline" / "baseline_metadata.json"
LOG_PATH = PROJECT_ROOT / "artifacts" / "logs" / "prediction_log.csv"

model = joblib.load(MODEL_PATH)
label_mapping_df = pd.read_csv(LABEL_MAPPING_PATH)

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

id_to_label = dict(zip(label_mapping_df["label_id"], label_mapping_df["category_final"]))

app = FastAPI(title="NLP Triagem Inteligente Financeira API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/model-info")
def model_info():
    return {
        "model_name": metadata["selected_model_name"],
        "model_family": metadata["model_family"],
        "label_count": len(id_to_label),
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest):
    request_id = str(uuid.uuid4())
    request_timestamp = datetime.utcnow().isoformat()
    inference_timestamp = datetime.utcnow().isoformat()

    text_prepared = str(payload.text).strip()
    pred_label_id = int(model.predict([text_prepared])[0])
    pred_label = id_to_label[pred_label_id]

    response = {
        "request_id": request_id,
        "text": text_prepared,
        "source_channel": payload.source_channel,
        "request_timestamp": request_timestamp,
        "predicted_label": pred_label,
        "predicted_label_id": pred_label_id,
        "model_name": metadata["selected_model_name"],
        "model_family": metadata["model_family"],
        "inference_timestamp": inference_timestamp,
    }

    append_prediction_log(LOG_PATH, response)
    return response

    