import httpx
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: schemas.UserCreate):
    # Verificar se o email já existe
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        fantasy_name=user.fantasy_name,
        cnpj=user.cnpj,
        email=user.email,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db_user.fantasy_name = user.fantasy_name
    db_user.cnpj = user.cnpj
    db_user.email = user.email
    db_user.password = get_password_hash(user.password)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_coordinates(address: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    response = httpx.get(url, params=params)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return float(data["lat"]), float(data["lon"])
    return 0.0, 0.0

def create_property(db: Session, property: schemas.PropertyCreate):
    latitude, longitude = get_coordinates(property.address_full)
    db_property = models.Property(**property.dict(), latitude=latitude, longitude=longitude)
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def update_property(db: Session, property_id: int, property: schemas.PropertyUpdate):
    db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
    if db_property is None:
        return None
    for key, value in property.dict().items():
        setattr(db_property, key, value)
    db_property.latitude, db_property.longitude = get_coordinates(property.address_full)
    db.commit()
    db.refresh(db_property)
    return db_property

def read_property(db: Session, property_id: int):
    db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
    if db_property is None:
        return None
    return db_property

def read_all_properties(db: Session):
    return db.query(models.Property).all()

def delete_property(db: Session, property_id: int):
    db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
    if db_property is None:
        return None
    db.delete(db_property)
    db.commit()
    return db_property