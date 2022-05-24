from enum import Enum
from fastapi import FastAPI


app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id: int) -> dict:
    return {'item_id': item_id}
