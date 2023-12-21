# ОСНОВНОЙ ФАЙЛ ДЛЯ ЗАПУСКА ПРИЛОЖЕНИЯ. СЮДА ИМПОРТИРУЮТСЯ ВСЕ ЭНДПОИНТЫ,СУЩНОСТИ 
import uvicorn
from fastapi import FastAPI , Query , Depends
from datetime import date
#ДЛЯ ГЕНЕРАЦИИ ТЕЛА ЗАПРОСА (request body)
from pydantic import BaseModel
from app.booking.router import router as router_bookings
from app.booking.schemas import Sbooking
from app.hotels.rooms.router import router as router_rooms
from app.users.router import router as router_users
from typing import List

app = FastAPI()
app.include_router(router_users)
app.include_router(router_bookings)  
app.include_router(router_rooms)

