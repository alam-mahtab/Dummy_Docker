from fastapi import APIRouter, HTTPException, Depends, Form
from sqlalchemy.orm.session import Session
from . import schemas, models
import uuid, datetime
from module1.database import database
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.paginator import paginate
#from .models import Create
router = APIRouter()

@router.post("/test/create", response_model = schemas.TestList)
async def create(user : schemas.CreateTest):
    gid = str(uuid.uuid1())
    gdate = datetime.datetime.now()
    query = models.Create.__table__.insert().values(
        id = gid,
        username = user.username,
        email = user.email,
        first_name = user.first_name,
        last_name = user.last_name,
        phone = user.phone,
        created_at = gdate,
        status = "1")

    await database.execute(query)
    return {
        **user.dict(),
        "id" :gid,
        "created_at" : gdate,
        "status" : "1",
    }

@router.put("/test/update",response_model = schemas.TestList)
async def update_test(test : schemas.TestUpdate):
    gDate = datetime.datetime.now()
    query = models.Create.__table__.update().\
        where(models.Create.username == test.username).\
            values(
                first_name = test.first_name,
                last_name = test.last_name,
                email = test.email,
                phone = test.phone,
                created_at = gDate
            )
    await database.execute(query)
    #return {"status" : True}
    return await find_test_by_username(test.username)

@router.get("/tests",response_model=Page[schemas.TestList],dependencies=[Depends(pagination_params)])
async def find_all_test(
):
    query = "Select * From Creates"
    test_all = await database.fetch_all(query=query, values={}) 
    return paginate(test_all)

@router.get("/tests/username", response_model= schemas.TestList)
async def find_test_by_username(username : str):
    query = models.Create.__table__.select().where(models.Create.username == username)
    return await database.fetch_one(query)

@router.delete("/tests/username")
async def delete_test_by_username(username: str):
    query = models.Create.__table__.delete().where(models.Create.username == username)
    await database.execute(query)
    return {
        "status" : True,
        "message" : "This Test Is been Deleted"}