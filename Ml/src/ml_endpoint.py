from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from price_prediction import predict_price
import json

class MLData(BaseModel):
    file_path: str
    data: dict

class PredictData(BaseModel):
    rooms: int
    area: float

app = FastAPI()

origins = [
  "http://localhost",
  "http://localhost:8080",
  "http://localhost:8000",
  "http://127.0.0.1",
  "http://127.0.0.1:8080",
  "http://127.0.0.1:8000",
  "http://localhost:3000",
  "http://127.0.0.1:3000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.post(" ")
async def save_learning_data(ml_data: MLData):
    # Save JSON data to a file
    with open(ml_data.file_path, 'w') as f:
        json.dump(ml_data.data, f)
    return {"message": "Data saved successfully"}

@app.get("/price_prediction")
async def get_price_prediction(predict_data: PredictData):
    try:
        price = predict_price('ml_data.json', predict_data.rooms, predict_data.area)
        return {"predicted_price": price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))