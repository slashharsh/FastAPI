from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 


app = FastAPI()

class Package(BaseModel):
    name: str
    number: int
    description:Optional[str] = "Please provide if you want"


@app.get('/')
async def pydantic_demo():
    return {"This is a demo of PyDantic":"This is default Route"}

# Basic About BaseModel
@app.post('/details/')
async def get_details(detail:Package):
    return detail

# Basic About BaseModel with Query and Parameters
@app.post('/details/{parameter}')
async def get_details_parameters(parameter:int,detail:Package,flag:bool):
 return {"Parameter Passed":parameter,**detail.dict(),"Flag Passed":flag}