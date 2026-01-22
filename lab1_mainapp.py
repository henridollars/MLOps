from typing import Union
from fastapi import FastAPI
import scoring

# Initialize the web application
app = FastAPI()

@app.get("/")
async def index():
    """Service health check and greeting."""
    return {"message": "Welcome to the Apartment Scoring API!"}

@app.get("/calculate-score")
def get_rating(address: str, surface: float, number_rooms: int):
    result = scoring(address, surface, number_rooms)
    
    return {
        "address_queried": address,
        "calculated_score": result
    }
