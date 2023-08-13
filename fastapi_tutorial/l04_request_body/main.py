from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post('/items/')
async def create_item(item: Item) -> dict:
    item_dict = item.model_dump()

    if item_dict.get('tax'):
        item_dict.update(
            price_with_tax=(item_dict['price'] * item_dict['tax']))

    return item_dict


@app.put('/items/{item_id}')
async def update_item(item_id: str, item: Item, q: str | None = None) -> dict:
    result = item.model_dump()
    if q:
        result.update(q=q)

    return {'item_id': item_id, **result}
