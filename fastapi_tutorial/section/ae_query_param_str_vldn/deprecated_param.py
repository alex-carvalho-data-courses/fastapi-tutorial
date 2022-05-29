from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str | None = Query(default=None,
                                           alias='item-query',
                                           title='Query string',
                                           description='Query string for the items to search in the database that have '
                                                       'a good match',
                                           min_length=3,
                                           max_length=50,
                                           regex='^[a-zA-Z]',
                                           deprecated=True)) -> dict:
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}

    if q:
        results.update({'q': q})

    return results
