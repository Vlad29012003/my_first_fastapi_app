from app.database import asynch_session_maker
from sqlalchemy import select
from app.booking.models import Booking


class BaseService:
    model = None

    @classmethod
    async def find_by_id(cls,model_id: int):
        async with asynch_session_maker() as session:
            query = select(cls.model).filter_by(id = model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls,**filter_by):
        async with asynch_session_maker() as sesion:
            query = select(cls.model).filter_by(**filter_by)
            result = await sesion.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with asynch_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()