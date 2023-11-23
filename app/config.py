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
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')

# URL БАЗЫ ДАННЫХ ЧТОБЫ ПОМОЧЬ АЛХИМИИ НАЙТИ ГДЕ НАХОДИТСЯ БАЗА ДАННЫХ 
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


# ГЕНЕРАЦИЯ СЕКРЕТНОГО КЛЮЧА В ТЕРМИНАЛЕ 
# python3.8 
# from secrets import token_bytes
# from base64 import b64encode 
# print (b64encode (token_bytes(32)).decode())
