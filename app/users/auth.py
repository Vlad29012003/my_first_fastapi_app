from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='autho')

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verity_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password ,hashed_password)
 




