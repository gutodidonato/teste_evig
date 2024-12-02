from fastapi import FastAPI
from app.api.v1 import auth, user, property

app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(property.router, prefix="/api/v1/properties", tags=["properties"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])