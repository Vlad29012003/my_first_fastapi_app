from app.database import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String 

class Users(Base):
    __tablename__= 'users'

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False)
    hashed_password = Column(String,nullable=False)

