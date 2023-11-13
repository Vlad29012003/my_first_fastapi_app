# ВСЕ ДАННЫЕ О ПОДКЛЮЧЕНИИ К БД К REDIS К ПОЧТЕ ИТД

from dotenv import load_dotenv
import os

#ДЛЯ АКТИВАЦИИ ФАЙЛА .ENV
load_dotenv()

# ВЗГЛЯД ДАННЫХ ИЗ .ENV 
DB_HOST= os.environ.get('DB_HOST')
DB_PORT= os.environ.get('DB_PORT')
DB_USER= os.environ.get('DB_USER')
DB_PASS= os.environ.get('DB_PASS')
DB_NAME= os.environ.get('DB_NAME')

# URL БАЗЫ ДАННЫХ ЧТОБЫ ПОМОЧЬ АЛХИМИИ НАЙТИ ГДЕ НАХОДИТСЯ БАЗА ДАННЫХ 
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'