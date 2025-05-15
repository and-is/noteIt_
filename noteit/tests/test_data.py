import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes", json={
        "title": "Test Note",
        "content": "This is a test note."
    })
    assert response.status_code in [200, 201]
    data = response.json()
    
    # Adjust if the API returns: { "note": { "id": ..., "title": ..., "content": ... } }
    note = data.get("note", data)  # fallback if no 'note' key
    
    assert note["title"] == "Test Note"
    assert note["content"] == "This is a test note."

def test_get_all_notes():
    response = client.get("/notes")
    assert response.status_code == 200
    data = response.json()
    notes = data.get("notes", data)  # allow both list or wrapped dict
    assert isinstance(notes, list)

def test_get_note_by_id():
    create_response = client.post("/notes", json={
        "title": "Fetch Me",
        "content": "Content to fetch"
    })
    note = create_response.json().get("note", create_response.json())
    note_id = note["id"]

    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    data = response.json()
    note = data.get("note", data)
    assert note["title"] == "Fetch Me"
    assert note["content"] == "Content to fetch"

def test_delete_note():
    create_response = client.post("/notes", json={
        "title": "Delete Me",
        "content": "Temporary content"
    })
    note = create_response.json().get("note", create_response.json())
    note_id = note["id"]

    delete_response = client.delete(f"/notes/{note_id}")
    assert delete_response.status_code in [200, 204]

    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 404
