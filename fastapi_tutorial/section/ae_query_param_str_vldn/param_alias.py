from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str | None = Query(default=None, alias='item-query')) -> dict:
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}

    if q:
        results.update({'q': q})

    return results
