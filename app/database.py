# ФАЙЛ СО ВСЕМИ ОСНОВНЫМИ НАСТРОЙКАМИ БАЗЫ ДАННЫХ, ЗДЕСЬ ПРОИСХОДИТ ПОДКЛЮЧЕНИЕ К БД И СОЗДАНИЕ НЕКОТОРЫХ СЕССИЙ 
# ДЛЯ РАБОТЫ С БД, ЧТОБЫ ИХ НЕ НУЖНО БЫЛО СОЗДАВАТЬ В ДРУГИЗ МЕСТАХ 


from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker
from .config import DATABASE_URL

# URL БАЗЫ ДАННЫХ ЧТОБЫ ПОМОЧЬ АЛХИМИИ НАЙТИ ГДЕ НАХОДИТСЯ БАЗА ДАННЫХ 
# DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# ДВИЖОК ДЛЯ ПЕРЕДАЧИ АЛХИМИИ 
engine = create_async_engine(DATABASE_URL)

# ГЕНЕРАТОР СЕСИИ (ТРАНЗАКЦИЙ В БД)
#ПЕРЕМЕННАЯ РАБОТЫ С БД 
asynch_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# ИСПОЛЬЗУЕТСЯ ДЛЯ МИГРАЦИЙ И СРАВНЕНИЙ С BACKEND TO DB THROUGHT ALEMBIC 
class Base(DeclarativeBase):
    pass



