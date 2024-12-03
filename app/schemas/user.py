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