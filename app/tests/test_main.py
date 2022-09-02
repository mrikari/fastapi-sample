from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "It works!"}


def test_get_info():
    response = client.get("/info")
    assert response.status_code == 200

    res_json = response.json()
    assert "app_name" in res_json
    assert "app_version" in res_json
