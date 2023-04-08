from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/user")
async def create_user(user: User):
    return user
