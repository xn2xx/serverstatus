#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : hsx
from enum import Enum

import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    alexent = 'alexnet'
    resnet = 'resnet'
    lenet = 'lnet'


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexent:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == '__main__':
    uvicorn.run(app="test:app", port=8080, host="0.0.0.0")
