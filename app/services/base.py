from app.database import asynch_session_maker
from sqlalchemy import select , insert 
from app.booking.models import Booking

#ДЛЯ ИЗБЕЖАНИЯ ПОВТОРНЫХ МЕТОДОВ 
class BaseService:
    #ПРИНИМАЕТ МОДЕЛИ 
    model = None

  #ДЛЯ ВОЗВРАТА СУЩНОСТИ ПО ID 
    @classmethod
    async def find_by_id(cls,model_id: int):
        #ОТКРЫВАЕМ СЕССИЮ С WITH, ЧТОБЫ В СЛУЧАЕ ЧЕГО СЕССИЯ ЗАКРЫВАЛАСЬ АВТОМАТИЧЕСКИ 
        async with asynch_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            #ИСПОЛЬЗУЕМ AWAIT ТАК КАК МЫ РАБОТАЕМ С АССИНХРОННОЙ ФУНКЦИЕЙ 
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls,**filter_by):
        async with asynch_session_maker() as sesion:
            query = select(cls.model).filter_by(**filter_by)
            result = await sesion.execute(query)
            return result.scalar_one_or_none()

  # ДЕДАЕТ ЗАПРОС К ПОЛУЧЕННОЙ МОДЕЛИ  
    @classmethod
    async def find_all(cls, **filter_by):
        async with asynch_session_maker() as session:
            # SELECT * FROM BOOKINGS.
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()
        

    @classmethod
    async def add(cls, **data):
        async with asynch_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            # ФИКСИРУЕТ ИЗМЕНЕНИЯ (INSERT , UPDATE , DELETE) В БАЗЕ ДАННЫХ 
            await session.commit()