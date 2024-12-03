import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.schemas.user import UserCreate



@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def token(client: TestClient):
    # Cria um usuário de teste
    user_data = {"fantasy_name": "auth", "cnpj": "1111111111111111", "email": "admin@admin.com", "password": "1111111111111111111111111"}
    client.post("/api/v1/users/", json=user_data)
    
    # Autentica o usuário de teste
    response = client.post("/api/v1/token", data={"username": user_data["email"], "password": user_data["password"]})
    assert response.status_code == 200
    return response.json()["access_token"]

@pytest.fixture(scope="module")
def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}

