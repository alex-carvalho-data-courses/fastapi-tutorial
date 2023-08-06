from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id) -> dict:
    return {'item_id': item_id}


@app.get('/things/{thing_id}')
async def read_thing(thing_id: int) -> dict:
    return {'thing_id': thing_id}
