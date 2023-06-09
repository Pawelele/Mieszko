import schedule
import time
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from price_prediction import predict_price
import requests
import json
import logging
import asyncio

# Create a logger object.
logger = logging.getLogger('my_logger')

# Set the level of the logger. This can be DEBUG, INFO, ERROR, etc.
logger.setLevel(logging.DEBUG)

# Create a file handler for outputting log messages to a file
log_handler = logging.FileHandler('my_logs.log')

# Format the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(log_handler)


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
  "http://localhost:8070"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)



def job():
    logger.debug("Fetching data batch")
    try:
        response = requests.get('http://db_service:8069/get_offers')  # replace with your endpoint
        data = response.json()
    except Exception as e:
        logger.debug(e)
        return 500
    
    if(response.status_code == 200):
        logger.debug("Data gathered correctly")
    
    logger.debug(data)

    data_important = {}
    for apartment in data['offers']:
        try:
            data_important[apartment[0]] = {
                "price": apartment[1],
                "area": apartment[3],
                "rooms_amount": apartment[4],
            }
        except Exception as e:
            logger.error(e)
    if data_important:
        with open('ml_data.json', 'w') as f:
            json.dump(data_important, f)
            print("JEST PLIK")
        logger.debug("Data saved correctly")
        return 200
    else:
        logger.error("No valid apartment data found")
        return 500

async def run_scheduler():
    while True:
        await asyncio.sleep(60)
        code = job()

@app.on_event("startup")
async def startup_event():
    logger.debug("Running scheduler")
    asyncio.create_task(run_scheduler())

@app.get("/price_prediction")
async def get_price_prediction(rooms: int, area: int):
    logger.debug(f"Begining price prediction process rooms: {rooms}, area: {area} ")
    price = predict_price('ml_data.json', rooms, area)
    logger.debug(f"PRICE: {price}")
    return {"predictedPrice": price}