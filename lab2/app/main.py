from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.scoring import score_apartment

app = FastAPI(title="Lab 2 - Apartment Scoring API")

class ApartmentIn(BaseModel):
    size_m2: float = Field(..., gt=0)
    rooms: int = Field(..., ge=0)
    distance_center_km: float = Field(..., ge=0)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score")
def score(apartment: ApartmentIn):
    s = score_apartment(
        size_m2=apartment.size_m2,
        rooms=apartment.rooms,
        distance_center_km=apartment.distance_center_km,
    )
    return {"score": s}
