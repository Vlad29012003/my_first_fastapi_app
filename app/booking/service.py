

from app.database import asynch_session_maker
from sqlalchemy import select , delete , insert , func , and_ , or_
from app.booking.models import Booking
from app.services.base import BaseService
from datetime import datetime, date, time


class BookingService(BaseService):
    model = Booking

    @classmethod
    async def add(
        cls,
        room_id: int,
        date_from: date,
        date_to: date,
    ):
        """
        WITH booked_rooms AS (
            SELECT * FROM bookings
            WHERE room_id = 1 AND
            (date_from >= '2023-05-15' AND date_from <= '2023-06-20) OR
            (date_from <= '2023-05-15' AND date_to > '2023-06-20')
        )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """
        booked_rooms = select(Booking).where(
            and_(
                Booking.room_id == 1,
                or_(
                    and_(
                        Booking.date_from >= date_from,
                        Booking.date_from <= date_to
                    ),
                    and_(
                        Booking.date_from <= date_from,
                        Booking.date_to > date_from,
                    ),
                )
            )
        ).cte('booked_rooms')

        """
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """

        rooms_left = select(Rooms.quantity - COUNT(booked_rooms.room_id)).select_from(room_id)

    