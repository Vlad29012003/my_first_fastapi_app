from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='auto')

# ФУНКЦИЯ ХЭШИРОВАНИЯ ПАРОЛЯ 
def get_password_hash(password: str):
    return pwd_context.hash(password)

# ДЛЯ ВЕРИФИКАЦИИ ХЭЩИРОВАННОЙ ВЕРСИИ (ЧТО ПАРОЛЬ ДЕЙСТВИТЕЛЬНО СООТВЕТСТВУЕТ ХЭШИРОВАННОЙ ВЕРСИИ)
def verity_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password ,hashed_password)
 




