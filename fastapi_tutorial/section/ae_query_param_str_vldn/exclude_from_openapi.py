from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(hidden_query: str | None = Query(default=None, include_in_schema=False)) -> dict:
    if hidden_query:
        return {'hidden_query': hidden_query}

    return {'hidden_query': 'not found'}
