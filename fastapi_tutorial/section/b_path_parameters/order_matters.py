from fastapi import FastAPI

app = FastAPI()


@app.get('/users/me')
async def rear_user_me():
    return {'user_id': "It's me, Mario!"}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


@app.get('/users/unreachable')
async def read_unreachable():
    return {'user_id': 'impossible to reach, because "/users/{user_id} will intercept it first"'}
