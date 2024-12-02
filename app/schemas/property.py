from pydantic import BaseModel

class PropertyBase(BaseModel):
    property_type: str
    address_full: str
    price: float
    area: float
    bedrooms: int
    bathrooms: int
    parking: int

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int

    class Config:
        orm_mode = True

class PropertyCoordinatesDescription(BaseModel):
    latitude: float
    longitude: float
    description: str

    class Config:
        orm_mode = True