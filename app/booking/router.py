from fastapi import APIRouter
from app.booking.models import Booking
from sqlalchemy import select
from app.booking.service import BookingService
from app.database import asynch_session_maker

router = APIRouter(
    prefix='/bookings',
    tags= ['бронирование'],
)

@router.get('')
async def get_bookings():
    return await BookingService.find_one_or_none(room_id =2)



