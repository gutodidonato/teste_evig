from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi import HTTPException, status

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate) -> User:
        # Verificar se o cnpj já existe
        db_user = self.db.query(User).filter(User.cnpj == user.cnpj).first()
        if db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CNPJ already registered")
        
        # Verificar se o email já existe
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        
        db_user = User(
            fantasy_name=user.fantasy_name,
            cnpj=user.cnpj,
            email=user.email,
            password=user.password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user: UserUpdate) -> User:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        db_user.fantasy_name = user.fantasy_name
        db_user.cnpj = user.cnpj
        db_user.email = user.email
        db_user.password = user.password
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> User:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_all(self) -> list[User]:
        return self.db.query(User).all()