from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: list[str] | None = Query(default=None)) -> dict:
    """ It should be called as .../items/?q=foo&q=bar """
    query_items = {'q': q}

    return query_items
