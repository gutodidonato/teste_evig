from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self, user: UserCreate):
        user.password = get_password_hash(user.password)
        return self.user_repository.create(user)

    def update_user(self, user_id: int, user: UserUpdate):
        user.password = get_password_hash(user.password)
        return self.user_repository.update(user_id, user)

    def delete_user(self, user_id: int):
        return self.user_repository.delete(user_id)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_by_email(email)

    def get_all_users(self):
        return self.user_repository.get_all()