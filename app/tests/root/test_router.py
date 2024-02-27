from fastapi.testclient import TestClient
from main import app

client = TestClient(app, backend="asyncio")


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "It works!"}


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200

    res_json = response.json()
    assert "name" in res_json
    assert "version" in res_json
