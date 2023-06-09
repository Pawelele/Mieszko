import schedule
import time
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from price_prediction import predict_price
import requests
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

def job():
    response = requests.get('http://localhost:8069/get_offers')  # replace with your endpoint
    data = response.json()

    data_important = json()
    for apartment in data:
        data_important[apartment["id"]]["price"] = apartment["price"]
        data_important[apartment["id"]]["area"] = apartment["area"]
        data_important[apartment["id"]]["rooms_amount"] = apartment["rooms_amount"]
    with open('ml_data.json', 'w') as f:
        json.dump(data_important.data, f)

schedule.every(6).hours.do(job)

def run_scheduler():
    job()
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.on_event("startup")
async def startup_event():
    task = BackgroundTasks()
    task.add_task(run_scheduler)

@app.get("/price_prediction")
async def get_price_prediction(predict_data: PredictData):
    try:
        price = predict_price('ml_data.json', predict_data.rooms, predict_data.area)
        return {"predicted_price": price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))