from fastapi import FastAPI, Depends, HTTPException

from pydantic import BaseModel
import sqlite3

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config import APP_NAME, PORT, ENV, DEBUG

from sqlalchemy.orm import Session
from sqlalchemy import text 
from app.deps import get_db

class NoteCreate(BaseModel):
    id: int | None = None
    title: str
    content: str | None = None

app = FastAPI(title=APP_NAME, debug=DEBUG)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/notes")
def read_notes(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM notes"))
    notes = result.mappings().all()
    return {"notes": notes}

@app.get("/notes/{note_id}")
def read_note(note_id: int, db: Session = Depends(get_db)):
    query = text("SELECT * FROM notes WHERE id = :id")
    result = db.execute(query, {"id": note_id})
    note = result.mappings().first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    result = db.execute(text("INSERT INTO notes (title, content) VALUES (:title, :content)"), {"title": note.title, "content": note.content})
    db.commit()
    id = result.lastrowid
    note.id = id
    return {"message": "Note created successfully", "note": note}

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    query = text("DELETE FROM notes WHERE id = :id")
    result = db.execute(query, {"id": note_id})
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}

