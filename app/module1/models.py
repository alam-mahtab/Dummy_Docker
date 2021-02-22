from sqlalchemy import  Column, Integer, String,DateTime

import datetime
from .database import Base

class Dummy(Base):
    __tablename__ = "dummys"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    name = Column(String)
    desc = Column(String)
    phone = Column(String)
    email = Column(String)
    


   