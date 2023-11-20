# ОСНОВНОЙ ФАЙЛ ДЛЯ ЗАПУСКА ПРИЛОЖЕНИЯ. СЮДА ИМПОРТИРУЮТСЯ ВСЕ ЭНДПОИНТЫ,СУЩНОСТИ 
import uvicorn
from fastapi import FastAPI , Query , Depends
from datetime import date
#ДЛЯ ГЕНЕРАЦИИ ТЕЛА ЗАПРОСА (request body)
from pydantic import BaseModel
from app.booking.router import router as router_bookings
from app.booking.schemas import Sbooking
from app.users.router import router as router_users
from typing import List

app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)  

class Shotel(BaseModel):
    address:str
    name:str
    stars:int

#логика 'рычаг', endpoint
@app.get('/hotels',response_model=List[Shotel])
def get_hotels(
    location:str,
    date_from:date,
    date_to:date,
#опциональные параметры 
    has_spa:bool = None,
    stars: int = Query(None,ge=1,le=5),
)-> List[Shotel]:
    
    hotels = [
        {
            'address':'ул Горькое, 6,Бищкук',
            'name':'International',
            'stars':3,
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date 

app.post('/bookings')
def add_bookings(booking: Sbooking):
    pass
