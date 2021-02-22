from typing import Optional
from pydantic import BaseModel
import datetime

class DummyBase(BaseModel):
    name :str
    desc:str
    phone:str
    email:str
    
class DummyList(DummyBase):
    created_date: Optional[datetime.datetime]
   