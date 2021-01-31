from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


@app.get('/')
async def hello():
    return {"Hello": "world"}

# Basic About Parameters (Path Parameters)


@app.get('/component/{component_id}')  # {} means paramtres
# :int means param should only be integer
async def get_component(component_id: int):
    return {"component_id": component_id}


# Basic About Parameters (Query Parameters)
@app.get('/component/')  # query parameters
async def read_component(number: int, text: Optional[str]): #Optional means without value of text it will respond 
    return {"number": number, "text": text}

