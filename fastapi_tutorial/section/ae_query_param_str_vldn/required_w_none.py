""" Required with None """
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str | None = Query(default=..., min_length=3)) -> dict:
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}

    results.update({'q': q})

    return results
