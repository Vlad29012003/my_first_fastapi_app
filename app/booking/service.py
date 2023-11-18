

from app.database import asynch_session_maker
from sqlalchemy import select
from app.booking.models import Booking
from app.services.base import BaseService

class BookingService(BaseService):
    model = Booking

    