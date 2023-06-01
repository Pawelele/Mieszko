from typing import Optional

from fastapi import FastAPI

from src.db_actions import Database

app = FastAPI()


@app.get("/get_offers/{city}")
async def get_offers(city: str = ""):
	offers = Database().get_offers(city)
	return {"offers": offers}
