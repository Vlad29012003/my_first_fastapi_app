from fastapi import Request , HTTPException , Depends , status
from jose import jwt , JWTError
from app.config import SECRET_KEY,ALGORITHM
from datetime import datetime 
from app.users.service import UserService



#Получение Cokie
def get_token(request : Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token 


# из Cokie мы достаем юзера 
async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY,ALGORITHM
        )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get('exp')  
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id: str = payload.get('sub')
    if not user_id:
        raise HTTPException (status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UserService.find_by_id(int(user_id))   
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return user 
