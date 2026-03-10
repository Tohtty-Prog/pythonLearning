from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        convert_to_number = int(message)
        convert_to_number += 1
        await websocket.send_text(f"Server: {convert_to_number}")
