import FastAPI as FastAPI

from db_service.src.db_actions import Database

app = FastAPI()

@app.post("/offers")
async def get_offers(**kwargs) -> dict[str, str]:
    """
    Checks if given number is a prime number
    :param number: number to check
    :return: True if number is prime, otherwise False. In case of any error raises BaseError.
    """
    db = Database()
    return db.get_from_db(kwargs)
