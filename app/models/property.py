from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

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
    latitude = Column(Float, default=0.0)
    longitude = Column(Float, default=0.0)
    description = Column(String, default="")