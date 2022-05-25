from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item_id}')
async def read_items(item_id: str, q: str | None = None, short: bool = False) -> dict:
    response = {'item_id': item_id}

    if q:
        response['q'] = q

    if not short:
        response.update({'description': 'This is an amazing item that has a long description'})

    return response


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str | None, q: str | None = None, short: bool = False) -> dict:
    item = {'item_id': item_id, 'owner_id': user_id}

    if q:
        item.update({'q': q})
    if not short:
        item.update({'description': 'This is an amazing item that has a long description.'})

    return item
