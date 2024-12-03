from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api.v1 import auth, user, property
from app.db.session import engine, get_db
from app.db.base import Base
from app.core.security import create_access_token, verify_password
from app.services.user_service import UserService
from app.schemas.token import Token
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")



app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(property.router, prefix="/api/v1/properties", tags=["properties"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])

