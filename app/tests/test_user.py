import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate
from app.api.deps import get_db
from app.main import app

@pytest.fixture
def db() -> Session:
    return next(get_db())

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

def test_create_user(client: TestClient, db: Session):
    response = client.post(
        "/api/v1/users/",
        json={"fantasy_name": "Test User", "cnpj": "12345678901234", "email": "test@example.com", "password": "aaaa"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

    # Delete the user after the test
    user_id = data["id"]
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200

def test_update_user(client: TestClient, db: Session):
    response = client.post(
        "/api/v1/users/",
        json={"fantasy_name": "Test User 2", "cnpj": "12345678901235", "email": "test2@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    user_id = response.json()["id"]
    response = client.put(
        f"/api/v1/users/{user_id}",
        json={"fantasy_name": "Updated User", "cnpj": "12345678901235", "email": "updated2@example.com", "password": "newpassword123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "updated2@example.com"

    # Delete the user after the test
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200

def test_delete_user(client: TestClient, db: Session):
    response = client.post(
        "/api/v1/users/",
        json={"fantasy_name": "Test User 3", "cnpj": "12345678901236", "email": "test3@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    user_id = response.json()["id"]
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

def test_read_users(client: TestClient, db: Session):
    response = client.post(
        "/api/v1/users/",
        json={"fantasy_name": "Test User 4", "cnpj": "12345678901237", "email": "test4@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    user_id = response.json()["id"]

    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # Delete the user after the test
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200