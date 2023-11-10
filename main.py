from fastapi import APIRouter
from dotenv import load_dotenv
from os import environ
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uvicorn

class User(BaseModel):
    name:str
    email:str
    password:str
    phone:Optional[str]
    data_joined: datetime=datetime.now()

users = [
    User(name="Richard",email="a",password="123",phone="111"),
    User(name="Ivan",email="b",password="321",phone="222"),
    User(name="Johny",email="c",password="213",phone="333"),
    User(name="Peter",email="d",password="312",phone="444"),
    User(name="Andy",email="e",password="132",phone="555")
]
load_dotenv()

router = APIRouter()

API_KEY = environ.get("SECRET_KEY")

@router.get("/")
async def get_users_name(apikey:str):
    if apikey == API_KEY:
        ls=[]
        for i in users:
            ls.append(i.name())
        return ls
    return {"error":"no access to this page"}
@router.post("/")
async def add_users(users:User,apikey:str):
    if apikey == API_KEY:
        users.append(users)
        return {users:"added"}
    return {"error":"no access to this page"}
@router.delete("/delete")
async def delete_users(name:str,apikey:str):
    if apikey == API_KEY:
        for n in users:
            if n.name() == name:
                users.remove(n)
                return {name:"delete"}
        return {"error":"not find"}
    return {"error": "no access to this page"}
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router,prefix="/user")

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)
