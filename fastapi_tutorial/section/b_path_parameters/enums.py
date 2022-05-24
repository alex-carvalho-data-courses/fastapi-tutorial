from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = 'AlexNet'
    resnet = 'ResNet'
    lenet = 'LeNet'


app = FastAPI()


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName) -> dict:
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Leraning FTW!'}

    if model_name.value == 'LeNet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}
