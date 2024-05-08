from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

class ToDo(BaseModel):
    task: str
    isDone: bool
    # finishDate: Optional[date] 2024-02-02

tasks = []

@app.post('/register')
def createTask(todo: ToDo):
    try:
        tasks.append(todo)
        return {'status': 'success'}
    except:
        return {'status': 'error'}
    
@app.post('/gettasks')
def getTasks(option: int):
    if option == 0 or option > 2:
        return tasks
    elif option == 1:
        return list(filter(lambda x: x.isDone == False, tasks))
    elif option == 2:
        return list(filter(lambda x: x.isDone == True, tasks))
    
@app.get('/task/{id}')
def findTaskById(id: int):
    try:
        return tasks[id]
    except:
        return {'message': 'Task not found'}