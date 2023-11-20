from pydantic import BaseModel ,  EmailStr

class SUserRegister(BaseModel):
    # УКАЗЫВАЕМ ТИП ДАННЫХ EmailStr из pydantic
    email: EmailStr
    password: str