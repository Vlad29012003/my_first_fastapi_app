from fastapi import HTTPException , status

class UserException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

# Исключение ошибки Пользователь уже существует
class UserAlreadyExistsException(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь уже существует'

# Исключение ошибки Неверная почта или пароль
class IncorrectEmailOrPasswordException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail = 'Неверная почта или пароль'

# Исключение ошибки токен истек
class TokenExpiredException(UserException): 
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='токен истек ('

# Исключение ошибки токен отсуцтвует
class TokenAppcentException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='токен отсуцтвует'

 # Исключение ошибки Некоректный формат токена
class IncorrentTokenFormatException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Некоректный формат токена'

# Исключение ошибки не авторизован 
class UserIsNotPresentException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED

# Исключение ошибки не осталось свободных номеров
RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='не осталось свободных номеров'
)