from fastapi import FastAPI
from pydantic import BaseModel
import json

datas = []

app = FastAPI()

class Task(BaseModel):
    description: str
    completed: bool = False


@app.post("/tasks")
def set_new_task(task: Task):
    data = task.model_dump()
    if not datas:
        new_id = 1
    else:
        new_id = datas[-1]['id'] + 1

    data['id'] = new_id
    datas.append(data)
    return data


@app.get("/tasks")
def get_all_tasks():
    if datas:
        return datas
    else:
        return {"message": "ei tehtäviä", "tasks": datas}
    
@app.patch("/tasks/{id}")
def update_task_status(id: int):
    for data in datas:
        if data['id'] == id:
            data['completed'] = True
            return data
    return {"message": "Tehtävää ei löytynyt"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for data in datas:
        if data['id'] == id:
            datas.remove(data)
            return {"message": "Tehtävä on poistettu"}
    return {"message": "Tehtävää ei ole"}

@app.get("/tasks/{id}")
def get_task(id: int):
    for data in datas:
        if data['id'] == id:
            return data
    return{"message": "Tehtävää ei ole"}