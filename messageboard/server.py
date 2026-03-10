from fastapi import FastAPI
from pydantic import BaseModel

datas = []

app = FastAPI()

class Message(BaseModel):
    username: str
    text: str

@app.get("/messages")
def get_messages():
    return datas
    
@app.post("/messages")
def send_messages(msg:Message):
    data = msg.model_dump()
    if not datas:
        new_id = 1
    else:
        new_id = datas[-1]["id"] + 1
    data["id"] = new_id

    datas.append(data)
    return data

@app.delete("/messages/{id}")
def delete_message(id: int):
    for data in datas:
        if data["id"] == id:
            datas.remove(data)
            return {"status": "deleted"}
    return {"status": "not found"}
