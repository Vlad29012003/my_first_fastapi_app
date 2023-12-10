from fastapi import HTTPException , status

class UserException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь уже существует'


class IncorrectEmailOrPasswordException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail = 'Неверная почта или пароль'


class TokenExpiredException(UserException): 
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='токен истек ('

class TokenAppcentException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='токен отсуцтвует'

class IncorrentTokenFormatException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail='Некоректный формат токена'

class UserIsNotPresentException(UserException):
    status_code=status.HTTP_401_UNAUTHORIZED

RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='не осталось свободных номеров'
)