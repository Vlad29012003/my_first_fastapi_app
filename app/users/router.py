from fastapi import APIRouter , HTTPException
# ИМПОРТИРУЕМ СО SCHEMAS SUserRegister для 
from app.users.schemas import SUserRegister
from app.users.auth import get_password_hash
from app.users.service import UserService

router = APIRouter(
    prefix = '/auth',
    tags= ['Аунтефикация']
)
# СОЗЛАЕМ ЭНДПОИНТ REGISTER ДЛЯ РЕГИСТРАЦИИ ПОЛЬЗОВАТЕЛЯ 
@router.post('/register')
async def register_user(user_data: SUserRegister):
    # ПРОВЕРЯЕТ ЕСТЬ ЛИ СУЩЕСВУЮЩИЙ ЮЗЕР
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    # если такой пользователь существует то дай ему ошибку 
    if existing_user:
        raise HTTPException(status_code=500)
# ПОЛЬЗОВАТЕЛЯ НЕТ ХЭШИРУЕМ ПАРОЛЬ И ДОБАВЛЯЕМ В БАЗУ ДАННЫХ 
    hashed_password = get_password_hash(user_data.password)

    await UserService.add(email =user_data.email, hashed_password=hashed_password)
    


