import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.schemas.property import PropertyCreate, PropertyUpdate
from app.api.deps import get_db
from app.main import app

@pytest.fixture
def db() -> Session:
    return next(get_db())

def test_create_property(client: TestClient, db: Session, auth_headers: dict):
    response = client.post(
        "/api/v1/properties/",
        json={"property_type": "HOUSE", "address_full": "0000 Avenida Brigadeiro Faria Lima, São Paulo - SP - Brasil", "price": 500000.00, "area": 150, "bedrooms": 3, "bathrooms": 2, "parking": 1},
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["property_type"] == "HOUSE"
    assert "id" in data

def test_update_property(client: TestClient, db: Session, auth_headers: dict):
    response = client.post(
        "/api/v1/properties/",
        json={"property_type": "HOUSE", "address_full": "0000 Avenida Brigadeiro Faria Lima, São Paulo - SP - Brasil", "price": 500000.00, "area": 150, "bedrooms": 3, "bathrooms": 2, "parking": 1},
        headers=auth_headers
    )
    assert response.status_code == 200
    property_id = response.json()["id"]
    response = client.put(
        f"/api/v1/properties/{property_id}",
        json={"property_type": "APARTMENT", "address_full": "0000 Avenida Paulista, São Paulo - SP - Brasil", "price": 600000.00, "area": 120, "bedrooms": 2, "bathrooms": 2, "parking": 1},
        headers=auth_headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["property_type"] == "APARTMENT"

def test_delete_property(client: TestClient, db: Session, auth_headers: dict):
    response = client.post(
        "/api/v1/properties/",
        json={"property_type": "HOUSE", "address_full": "0000 Avenida Brigadeiro Faria Lima, São Paulo - SP - Brasil", "price": 500000.00, "area": 150, "bedrooms": 3, "bathrooms": 2, "parking": 1},
        headers=auth_headers
    )
    assert response.status_code == 200
    property_id = response.json()["id"]
    response = client.delete(f"/api/v1/properties/{property_id}", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == property_id

def test_read_properties(client: TestClient, db: Session, auth_headers: dict):
    response = client.get("/api/v1/properties/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)