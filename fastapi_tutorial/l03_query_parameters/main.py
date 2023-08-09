from fastapi import FastAPI

app = FastAPI()

FAKE_DB = [{'item_name': 'foo'}, {'item_name': 'bar'}, {'item_name': 'baca'}, {'item_name': 'baz'}]


@app.get('/items/')
async def read_items(skip: int = 0, limit: int = 10) -> list[dict]:
    return FAKE_DB[skip:skip+limit]


@app.get('/elements/{element_id}')
async def read_element_optional(element_id: str, q: str | None = None) -> dict:
    if q:
        return {'element_id': element_id, 'q': q}

    return {'element_id': element_id}


@app.get('/members/{member_id}')
async def read_member_boolean(
        member_id: str,
        q: str | None = None,
        short: bool = False) -> dict:
    member = {'member_id': member_id}

    if q:
        member.update(q=q)

    if not short:
        member.update({'description': 'This is an amazing item that has a'
                                      ' long description (short == False)'})

    return member


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
        user_id: int,
        item_id: str,
        q: str | None = None,
        short: bool = False) -> dict:
    user_item = {'user_id': user_id, 'item_id': item_id}

    if q:
        user_item.update(q=q)

    if not short:
        user_item.update({'description': 'This is an amazing item that has a '
                                         'long description (short == False)'})

    return user_item


@app.get('/components/{component_id}')
async def read_component(component_id: int, needy: str) -> dict:
    return {'component_id': component_id, 'needy': needy}
