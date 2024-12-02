from sqlalchemy.orm import Session
from app.repositories.property_repository import PropertyRepository
from app.schemas.property import PropertyCreate, PropertyUpdate
from app.external.generate_description import generate_description
#from aiocache import cached // estou com problema com assincronicidade
from functools import lru_cache

class PropertyService:
    def __init__(self, db: Session):
        self.property_repository = PropertyRepository(db)

    def create_property(self, property: PropertyCreate):
        return self.property_repository.create(property)

    def update_property(self, property_id: int, property: PropertyUpdate):
        return self.property_repository.update(property_id, property)

    def delete_property(self, property_id: int):
        return self.property_repository.delete(property_id)

    def get_property(self, property_id: int):
        return self.property_repository.get(property_id)


    @lru_cache(maxsize=128)
    def get_all_properties(self):
        return self.property_repository.get_all()

    async def get_property_coordinates_description(self, property_id: int):
        property = self.property_repository.get(property_id)
        if property is None:
            return None
        property_details = {
            "property_type": property.property_type,
            "address_full": property.address_full,
            "price": property.price,
            "area": property.area,
            "bedrooms": property.bedrooms,
            "bathrooms": property.bathrooms,
            "parking": property.parking
        }
        description = await generate_description(property_details)
        return {
            "latitude": property.latitude,
            "longitude": property.longitude,
            "description": description
        }