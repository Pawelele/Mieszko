from typing import Optional, List
from fastapi import FastAPI
from src.db_actions import Database
from fastapi.middleware.cors import CORSMiddleware

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



# @app.get("/get_offers/{city}")
# async def get_offers(city: str = ""):
# 	offers = Database().get_offers(city)
# 	return {"offers": offers}

@app.get("/get_offers")
async def get_offers(city: str = ""):
	offers = Database().get_offers(city)
	return {"offers": offers}

class Offer:
    def __init__(self, id: int, price: str, price_per_meter: str, area: str, rooms: int,
                 title: str, type: str, description: str, link: str, photo: str, city: str):
        self.id = id
        self.price = price
        self.price_per_meter = price_per_meter
        self.area = area
        self.rooms = rooms
        self.title = title
        self.type = type
        self.description = description
        self.link = link
        self.photo = photo
        self.city = city

@app.get("/get_offers2")
async def get_offers(city: str = ""):
    raw_offers = Database().get_offers(city)
    offers = []
    for raw_offer in raw_offers:
        offer = Offer(*raw_offer)
        offers.append(offer.__dict__)
    return {"offers": offers}
