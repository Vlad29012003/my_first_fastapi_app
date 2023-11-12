from fastapi import FastAPI , Query
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.booking.router import router as router_bookings

app = FastAPI()
app.include_router(router_bookings)  

class Shotel(BaseModel):
    address:str
    name:str
    stars:int

@app.get('/hotels')
def get_hotels(
    location: str,
    date_from: date,
    date_to: date):

    return Shotel