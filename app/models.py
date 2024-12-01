from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fantasy_name = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
