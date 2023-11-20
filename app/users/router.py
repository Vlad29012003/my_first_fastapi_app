from fastapi import APIRouter , HTTPException , status , Response
# ИМПОРТИРУЕМ СО SCHEMAS SUserRegister для 
from app.users.schemas import SUserAuth
from app.users.auth import get_password_hash
from app.users.service import UserService
from app.users.auth import auntificate_users , create_access_token

router = APIRouter(
    prefix = '/auth',
    tags= ['Аунтефикация']
)
# СОЗЛАЕМ ЭНДПОИНТ REGISTER ДЛЯ РЕГИСТРАЦИИ ПОЛЬЗОВАТЕЛЯ 
@router.post('/register')
async def register_user(user_data:SUserAuth):
    # ПРОВЕРЯЕТ ЕСТЬ ЛИ СУЩЕСВУЮЩИЙ ЮЗЕР
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    # если такой пользователь существует то дай ему ошибку 
    if existing_user:
        raise HTTPException(status_code=500)
# ПОЛЬЗОВАТЕЛЯ НЕТ ХЭШИРУЕМ ПАРОЛЬ И ДОБАВЛЯЕМ В БАЗУ ДАННЫХ 
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(email =user_data.email, hashed_password=hashed_password)


# СОЗДАЕМ ЭНДПОИНТ ДЛЯ ЛОГИНА ПОЛЬЗОВАТЕЛЯ 
@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await auntificate_users(user_data.email, user_data.password)
    # В СЛУЧАЕ ОТРАБАТЫВАНИЯ NONE В AUTH.PY 
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    # СОЗДАЕМ ТОКЕН ДОСТУПА 
    access_token = create_access_token({'sub':user.id})
    # httpponly = True означает что не получится взять токен через javascript
    response.set_cookie('booking_access_token', access_token, httponly= True)
    return {'access_token': access_token}
    