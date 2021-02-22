from sqlalchemy import  Column, Integer, String,DateTime
import datetime
from module1.database import Base
class Create(Base):
    __tablename__ = "creates"

    id = Column(String, primary_key=True,unique=True)
    created_at = Column(DateTime,default=datetime.datetime.utcnow)
    username = Column(String,unique=True)
    email = Column(String,unique=True)
    phone = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    status = Column(String)
    
