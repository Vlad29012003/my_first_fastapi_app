from fastapi import Request ,  Depends
from jose import jwt , JWTError
from app.config import SECRET_KEY,ALGORITHM
from datetime import datetime 
from app.users.service import UserService
from app.exeptions import TokenAppcentException , TokenExpiredException , IncorrentTokenFormatException , UserIsNotPresentException 

#Получение Cokie
def get_token(request : Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAppcentException
    return token 


# из Cokie мы достаем юзера 
async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY,ALGORITHM
        )
    except JWTError:
        raise IncorrentTokenFormatException
    expire: str = payload.get('exp')  
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id:str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentException
    user = await UserService.find_by_id(int(user_id))   
    if not user:
        raise UserIsNotPresentException
    
    return user 


