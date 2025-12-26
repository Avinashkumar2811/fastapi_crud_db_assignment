from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create():
    res = client.post("/api/tasks/", json={"title": "Test"})
    assert res.status_code == 200

def test_read():
    res = client.get("/api/tasks/")
    assert res.status_code == 200
