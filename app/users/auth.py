from passlib.context import CryptContext
from pydantic import EmailStr 
from app.users.service import UserService
from fastapi import HTTPException 
from datetime import datetime , timedelta
from jose import jwt
from app.config import SECRET_KEY , ALGORITHM



pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='auto')

# ФУНКЦИЯ ХЭШИРОВАНИЯ ПАРОЛЯ 
def get_password_hash(password: str):
    return pwd_context.hash(password)

# ДЛЯ ВЕРИФИКАЦИИ ХЭЩИРОВАННОЙ ВЕРСИИ (ЧТО ПАРОЛЬ ДЕЙСТВИТЕЛЬНО СООТВЕТСТВУЕТ ХЭШИРОВАННОЙ ВЕРСИИ)
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password ,hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire =datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY , ALGORITHM
    )
    return encoded_jwt

# ФУНКЦИЯ ПРОВЕРКИ ПОЛЬЗОВАТЕЛЯ (ЕСТЬ ЛИ ПОЛЬЗОВАТЕЛЬ С ТАКИМ ЕМЕЙЛОМ )
async def auntificate_users(email:EmailStr ,password:str):
    user = await UserService.find_one_or_none(email=email)
    # ЕСЛИ ЕСТЬ ТО ПРОВЕРЯЕМ ЕГО ПАРОЛЬ 
    if not user and not verify_password(password, user.password):
    # ЕСЛИ НЕ СОВПАДАЕТ ВЕРНИ NONE
        return None
    # ЕСЛИ ВСЕ ХОРОШО ВЕРНИ ПОЛЬЗОВАТЕЛЯ 
    return(user)





