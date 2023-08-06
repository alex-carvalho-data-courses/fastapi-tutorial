from enum import auto, StrEnum

from fastapi import FastAPI


class ModelName(StrEnum):
    ALEXNET = auto()
    RESNET = auto()
    LENET = auto()


app = FastAPI()


@app.get('/items/{item_id}')
async def read_item(item_id) -> dict:
    return {'item_id': item_id}


@app.get('/things/{thing_id}')
async def read_thing(thing_id: int) -> dict:
    return {'thing_id': thing_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName) -> dict:
    message = ''
    match model_name:
        case ModelName.ALEXNET:
            message = 'Depp learning FTW!'
        case ModelName.LENET:
            message = 'LeCNN all the images'
        case ModelName.RESNET:
            message = 'Have some residuals'

    return {'model': model_name, 'message': message}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str) -> dict:
    return {'file_path': file_path}
