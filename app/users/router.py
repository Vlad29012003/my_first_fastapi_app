from fastapi import APIRouter , HTTPException
from app.users.schemas import SUserRegister
from app.users.auth import get_password_hash
from app.users.service import UserService

router = APIRouter(
    prefix = 'auth',
    tags= ['Аунтефикация']
)

@router.post('register')
async def register_user(user_data: SUserRegister):
    # ПРОВЕРЯЕТ ЕСТЬ ЛИ СУЩЕСВУЮЩИЙ ЮЗЕР
    existing_user = await UserService.find_one_or_none(email = user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    
    hashed_password = get_password_hash(user_data.password)
