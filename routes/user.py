from fastapi import APIRouter

from models.user import User
from schemas.user import userEntity, usersEntity
from  config.database import con

user = APIRouter()

@user.get('/')
async def find_all_users():
    # return con.FastApi.user.find()
    print(con.FastApi.user.find())
    print(usersEntity(con.FastApi.user.find()))
    return usersEntity(con.FastApi.user.find())


@user.post('/')
async def create_users(user: User):
    con.FastApi.user.insert_one(dict(user))
    return usersEntity(con.FastApi.user.find())



