from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Annotated

FALSE_TOKEN_SECRET = 'coneofsilence'
ERROR_MSG_INVALID_TOKEN = 'Invalid X-Token header'
ERROR_MSG_EXISTENT_ITEM = 'Item already exists.'

fake_db = {
    'foo':
        {'id': 'foo', 'title': 'Foo', 'description': 'There goes my hero'},
    'bar':
        {'id': 'bar', 'title': 'Bar', 'description': 'The bartenders'}
}


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


app = FastAPI()


@app.get('/')
async def read_main() -> dict:
    return {'msg': 'Hello world!'}


@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: str, x_token: Annotated[str, Header()]) -> dict:
    if x_token != FALSE_TOKEN_SECRET:
        raise HTTPException(status_code=400, detail=ERROR_MSG_INVALID_TOKEN)

    if item_id not in fake_db:
        raise HTTPException(
            status_code=404, detail=f'No item with id: {item_id}')

    return fake_db[item_id]


@app.post('/items/', response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]) -> Item:
    if x_token != FALSE_TOKEN_SECRET:
        raise HTTPException(status_code=400, detail=ERROR_MSG_INVALID_TOKEN)

    if item.id in fake_db:
        raise HTTPException(status_code=400, detail=ERROR_MSG_EXISTENT_ITEM)

    fake_db[item.id] = item.model_dump()

    return item
