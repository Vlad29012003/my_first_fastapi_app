from pydantic import BaseModel , EmailStr

class SUserAuth(BaseModel):
    # УКАЗЫВАЕМ ТИП ДАННЫХ EmailStr из pydantic
    email: EmailStr
    password: str