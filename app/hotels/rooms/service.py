from app.services.base import BaseService
from app.hotels.rooms.models import Rooms
from app.database import asynch_session_maker
from app.services.base import BaseService



class RoomsService(BaseService):
    model = Rooms



