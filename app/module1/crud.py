
from sqlalchemy.orm import Session
from . import models, schemas, database
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from random import randint

def create_dummy(db: Session,name:str,desc:str,phone:str,email:str,id:int):
    gid=randint(10,100)
    db_dummy = models.Dummy(name=name,desc=desc,phone=phone,email=email,id=gid)
    db.add(db_dummy)
    db.commit()
    #db.refresh(db_dummy)
    return db_dummy


def get_dummy(db, id: int):
    return db.query(models.Dummy).filter(models.Dummy.id== id).first()

def dummy_list(db):
    return db.query(models.Dummy).all()

async def delete(db: Session,id: int)-> bool:
   sym1 =models.Dummy.__table__
   sym = sym1.delete().where(models.Dummy.id== id)
   print(sym)
   result = db.execute(sym)
   db.commit()
   return True
# async def update_dummy(db:Session,name:str,desc:str,phone:str,email:str,id:int):
#     query = models.Dummy.__table__.update(
#         models.Dummy.name = name
#     )


