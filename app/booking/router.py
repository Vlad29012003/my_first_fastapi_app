# C ЭНДПОИНТАМИ ВОТ СДЕСЬ 
from fastapi import APIRouter , Request , Depends
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.booking.service import BookingService
from app.booking.schemas import Sbooking
from typing import List

router = APIRouter(
    prefix='/bookings',
    tags= ['бронирование'],
)

# ВОЗВРАЩЯЕТ ЖУРНАЛ ЗАПИСЕЙ ДЛЯ ЗАРЕГЕСТРИРОВАННОГО ПОЛЬЗОВАТЕЛЯ 
#принимаем пользователя 
@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)): #-> List[Sbooking]:
    return await BookingService.find_all(user_id= user.id)
    # return await BookingService.find_all()




