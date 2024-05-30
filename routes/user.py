from fastapi import APIRouter
from bson import ObjectId
from models.user import User
from schemas.user import serializeDict, serializeList
from  config.database import con

user = APIRouter()

@user.get('/')
async def find_all_users():
    return serializeList(con.FastApi.user.find())

@user.get('/{id}')
async def get_user(id,user: User):
    return serializeDict(con.FastApi.user.find_one({"_id":ObjectId(id)}))


@user.post('/')
async def create_users(user: User):
    con.FastApi.user.insert_one(dict(user))
    return serializeList(con.FastApi.user.find())

@user.put('/{id}')
async def update_user(id,user: User):
    con.FastApi.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return serializeDict(con.FastApi.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(con.FastApi.user.find_one_and_delete({"_id":ObjectId(id)}))





