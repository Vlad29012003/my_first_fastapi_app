# C ЭНДПОИНТАМИ ВОТ СДЕСЬ 
from fastapi import APIRouter ,Depends
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.booking.service import BookingService
from datetime import datetime, date, time
from app.exeptions import RoomCannotBeBooked

from typing import List

router = APIRouter(
    prefix='/bookings',
    tags= ['бронирование'],
)

# ВОЗВРАЩЯЕТ ЖУРНАЛ ЗАПИСЕЙ ДЛЯ ЗАРЕГЕСТРИРОВАННОГО ПОЛЬЗОВАТЕЛЯ 
#принимаем пользователя 
@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)): #-> List[Sbooking]:
    return await BookingService.find_all(user_id=1)
    # return await BookingService.find_all()

@router.get('')
async def add_booking(
    user:Users = Depends(get_current_user),
):
    await BookingService.add(user_id = user.id)



@router.post('')
async def add_booking(
    room_id: int, date_from: date, date_to:date,
    user:Users = Depends(get_current_user),
):
   booking =  await BookingService.add(user.id, room_id,date_from,date_to)
   if not booking:
       raise RoomCannotBeBooked