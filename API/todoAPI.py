from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    dueDate:str
    description: str

app = FastAPI(title="Todo API")

#CRUD

sample_db = []

@app.get('/')
async def default(): 
    return "Hello World"

@app.post("/todo/")
async def create_todo(todo:Todo):
    sample_db.append(todo)
    return todo

