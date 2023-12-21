from pydantic import BaseModel


class Shotel(BaseModel):
    id:int
    name:str
    location:str
    service:list
    rooms_quantity:str
    image_id:int




    

    