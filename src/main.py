from fastapi import FastAPI
from typing import Union

app = FastAPI()


data = {
    '1': 'Миша',
    '2': 'Женя',
    '3': 'Маша'
}

@app.get("/hello")
async def hello():
    return {"Hello": "World"}


@app.get('/user/{user_id}')
async def get_user(user_id:str) -> str:
    return data[user_id]


@app.post('/user/{username}')
async def add_user(username:str) -> dict:
    max_key = max([int(i) for i in data.keys()])
    data[str(max_key+1)] = username
    return {
        'status': 201,
        'detail': 'success',
            }
