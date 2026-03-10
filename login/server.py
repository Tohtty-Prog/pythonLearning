from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    username: str
    password: str

def load_users():
    with open("users.json", 'r') as f:
        return json.load(f)["users"]

@app.post("/login")
def login(data: LoginData):
    users = load_users()
    for user in users:
        if user["username"] == data.username and user["password"] == data.password:
            return {"message": "login onnistui"}
    return {"succeess": False, "message": "Väärä username tai password"}
