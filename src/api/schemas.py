from pydantic import BaseModel
from typing import Optional


class PredictionRequest(BaseModel):
    text: str
    source_channel: Optional[str] = "unknown"


class PredictionResponse(BaseModel):
    request_id: str
    text: str
    source_channel: str
    request_timestamp: str
    predicted_label: str
    predicted_label_id: int
    model_name: str
    model_family: str
    inference_timestamp: str

    