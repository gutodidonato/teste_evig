from sqlalchemy.orm import Session
from app.models.property import Property
from app.schemas.property import PropertyCreate, PropertyUpdate

class PropertyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, property: PropertyCreate) -> Property:
        db_property = Property(**property.dict())
        self.db.add(db_property)
        self.db.commit()
        self.db.refresh(db_property)
        return db_property

    def update(self, property_id: int, property: PropertyUpdate) -> Property:
        db_property = self.db.query(Property).filter(Property.id == property_id).first()
        if db_property is None:
            return None
        for key, value in property.dict().items():
            setattr(db_property, key, value)
        self.db.commit()
        self.db.refresh(db_property)
        return db_property

    def delete(self, property_id: int) -> Property:
        db_property = self.db.query(Property).filter(Property.id == property_id).first()
        if db_property is None:
            return None
        self.db.delete(db_property)
        self.db.commit()
        return db_property

    def get(self, property_id: int) -> Property:
        return self.db.query(Property).filter(Property.id == property_id).first()

    def get_all(self) -> list[Property]:
        return self.db.query(Property).all()