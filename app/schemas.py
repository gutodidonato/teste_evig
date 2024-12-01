from pydantic import BaseModel

class UserBase(BaseModel):
    fantasy_name: str
    cnpj: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

class UserLogin(BaseModel):
    email: str
    password: str

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
    latitude: float
    longitude: float
    description: str

    class Config:
        orm_mode = True