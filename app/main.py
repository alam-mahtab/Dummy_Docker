from fastapi import FastAPI, Request, Depends, File
from fastapi.middleware.cors import CORSMiddleware
from module1.database import database
import time
import requests
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def add_process_time_header(request : Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    response.headers['X-Process-Time'] = str(process_time)

    return response


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/')
async def read_root():
    return {"message" : "Hello world"}

from module1 import controller 
app.include_router(controller.router, prefix="/demo", tags=["Demo using query method"])

from module2 import controller 
app.include_router(controller.router, prefix="/body", tags=["Demo using Body method"])

from api import ping
app.include_router(ping.router)
