# C ЭНДПОИНТАМИ ВОТ СДЕСЬ 
from fastapi import APIRouter
from app.booking.service import BookingService
from app.booking.schemas import Sbooking
from typing import List

router = APIRouter(
    prefix='/bookings',
    tags= ['бронирование'],
)

# ВОЗВРАЩЯЕТ ЖУРНАЛ ЗАПИСЕЙ ДЛЯ ЗАРЕГЕСТРИРОВАННОГО ПОЛЬЗОВАТЕЛЯ 
@router.get('')
async def get_bookings() -> List[Sbooking]:
    return await BookingService.find_all()




