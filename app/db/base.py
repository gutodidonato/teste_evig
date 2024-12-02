from app.db.session import engine
from app.models import user, property
from app.db.database import Base

Base.metadata.create_all(bind=engine)