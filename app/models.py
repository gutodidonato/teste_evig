from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fantasy_name = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    property_type = Column(String, index=True)
    address_full = Column(String, index=True)
    price = Column(Float)
    area = Column(Float)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    parking = Column(Integer)
    #Vamos ter que passar pelo endpoint de ia
    latitude = Column(Float, default=0.0)
    longitude = Column(Float, default=0.0)
    description = Column(String, default="Sem Descrição")
    