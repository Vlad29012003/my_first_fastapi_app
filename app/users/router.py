from fastapi import APIRouter  , Response , Depends
# ИМПОРТИРУЕМ СО SCHEMAS SUserRegister для 
from app.exeptions import UserAlreadyExistsException , IncorrectEmailOrPasswordException
from app.users.schemas import SUserAuth
from app.users.auth import get_password_hash
from app.users.service import UserService
from app.users.auth import auntificate_users , create_access_token
from app.users.models import Users
from app.users.dependencies import get_current_user

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
        raise UserAlreadyExistsException
# ПОЛЬЗОВАТЕЛЯ НЕТ ХЭШИРУЕМ ПАРОЛЬ И ДОБАВЛЯЕМ В БАЗУ ДАННЫХ 
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(email =user_data.email, hashed_password=hashed_password)


# СОЗДАЕМ ЭНДПОИНТ ДЛЯ ЛОГИНА ПОЛЬЗОВАТЕЛЯ 
@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await auntificate_users(user_data.email, user_data.password)
    # В СЛУЧАЕ ОТРАБАТЫВАНИЯ NONE В AUTH.PY 
    if not user:
        raise IncorrectEmailOrPasswordException
    # СОЗДАЕМ ТОКЕН ДОСТУПА 
    access_token = create_access_token({'sub':str (user.id)})
    # httpponly = True означает что не получится взять токен через javascript
    response.set_cookie('booking_access_token', access_token, httponly= True)
    return {'access_token': access_token}
    

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('booking_access_token')


@router.get('/me')
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user

