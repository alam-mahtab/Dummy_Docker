from typing import List
from fastapi import Depends,File, UploadFile, APIRouter
from sqlalchemy.orm import Session
from . import crud, models
from .database import SessionLocal, engine
from .schemas import DummyBase, DummyList
from .models import Dummy
# Pagination
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.paginator import paginate
router = APIRouter()
from random import randint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/talents/")
def create_dummy(
    desc:str,name:str,phone:str,email:str,db: Session = Depends(get_db)
):
    
    return crud.create_dummy(db=db,name=name,desc=desc,phone=phone,email=email,id=id)

@router.put("/talents/")
def update_dummy(
    id:int,desc:str,name:str,phone:str,email:str,db: Session = Depends(get_db)
):
    subject =  crud.get_dummy(db,id)
    if not subject:
        raise HTTPException(status_code=404, detail="Course not found")
    #'select * from USERS where email='+"'"+str(username)+"'"+' and PASSWORD='+"'"+str(password)+"'"
    query = "UPDATE courses SET name='"+str(name)+"' , desc='"+str(desc)+"' , phone='"+str(phone)+"' , email='"+str(email)+"'  WHERE id='"+str(id)+"'"
    db.execute(query)
    db.commit()
    return {"Result" : "Course Updated Succesfully"}
@router.get("/talents/" ,dependencies=[Depends(pagination_params)])
def dummy_list(db: Session = Depends(get_db)):
    dummy_all =crud.dummy_list(db=db)
    return paginate(dummy_all)

@router.get("/talents/{talent_id}")
def dummy_detail(talent_id:int,db: Session = Depends(get_db)):
    return crud.get_dummy(db=db, id=talent_id)

@router.delete("/talents/{talent_id}")
async def delete(talent_id: int, db: Session = Depends(get_db)):
    deleted = await crud.delete(db, talent_id)
    return {"deleted": deleted}
