import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.api.deps import get_db, SessionLocal
from app.schemas.user import UserCreate

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)



@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def token(client: TestClient):
    # Cria um usuário de teste
    user_data = {"fantasy_name": "Test User", "cnpj": "12345678901234", "email": "test@example.com", "password": "password123"}
    client.post("/api/v1/users/", json=user_data)
    
    # Autentica o usuário de teste
    response = client.post("/api/v1/token", data={"username": user_data["email"], "password": user_data["password"]})
    assert response.status_code == 200
    return response.json()["access_token"]

@pytest.fixture(scope="module")
def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="function")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)