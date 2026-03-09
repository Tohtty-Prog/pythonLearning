from fastapi import FastAPI
from pydantic import BaseModel
from storage import NoteStorage

storage_management: NoteStorage = NoteStorage("notes.json")

app = FastAPI()

class Note(BaseModel):
    content: str


@app.get("/")
def home():
    return {"message": "Notes API is running"}


@app.get("/notes")
def get_notes():
    return storage_management.get_notes()


@app.post("/notes")
def add_note(note: Note):
    saved_note = storage_management.add_note(note.model_dump())
    return {"status": "ok", "note": saved_note}