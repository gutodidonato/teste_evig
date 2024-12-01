from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import crud, models, schemas, database, auth

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if not user:
        return False
    if not crud.verify_password(password, user.password):
        return False
    return user

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db=db, user=user)
    except:
        raise HTTPException(status_code=400, detail="Email already exists")

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@app.get("/protected", response_model=str)
def read_protected(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    auth.verify_token(token, credentials_exception)
    return "ok"

@app.get("/debug/users/{user_id}", response_model=dict)
def read_user_passwords(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"email": db_user.email, "hashed_password": db_user.password}


# Rota para criar um imóvel
@app.post("/properties/", response_model=schemas.Property)
def create_property(property: schemas.PropertyCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = auth.verify_token(token, credentials_exception)
    user = crud.get_user_by_email(db, token_data.email)
    if user is None:
        raise credentials_exception
    return crud.create_property(db=db, property=property)

# Rota para atualizar um imóvel
@app.put("/properties/{property_id}", response_model=schemas.Property)
def update_property(property_id: int, property: schemas.PropertyUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    auth.verify_token(token, credentials_exception)
    db_property = crud.update_property(db=db, property_id=property_id, property=property)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

# Rota para ler um imóvel
@app.get("/properties/{property_id}", response_model=schemas.Property)
def read_property(property_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    auth.verify_token(token, credentials_exception)
    db_property = crud.read_property(db=db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

# Rota para ler todos os imóveis
@app.get("/properties/", response_model=list[schemas.Property])
def read_all_properties(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    auth.verify_token(token, credentials_exception)
    return crud.read_all_properties(db=db)

# Rota para deletar um imóvel
@app.delete("/properties/{property_id}", response_model=schemas.Property)
def delete_property(property_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    auth.verify_token(token, credentials_exception)
    db_property = crud.delete_property(db=db, property_id=property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property