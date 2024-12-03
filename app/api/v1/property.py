from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.property import Property, PropertyCreate, PropertyUpdate, PropertyCoordinatesDescription
from app.services.property_service import PropertyService
from app.api.deps import get_current_user
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Property)
def create_property(property: PropertyCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    property_service = PropertyService(db)
    return property_service.create_property(property)

@router.put("/{property_id}", response_model=Property)
def update_property(property_id: int, property: PropertyUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    property_service = PropertyService(db)
    db_property = property_service.update_property(property_id, property)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@router.get("/{property_id}", response_model=Property)
def read_property(property_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    property_service = PropertyService(db)
    db_property = property_service.get_property(property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@router.get("/{property_id}/coordinates", response_model=PropertyCoordinatesDescription)
async def read_property_coordinates(property_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    property_service = PropertyService(db)
    result = await property_service.get_property_coordinates_description(property_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return result

@router.get("/", response_model=list[Property])
def read_all_properties(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    property_service = PropertyService(db)
    return property_service.get_all_properties()


@router.delete("/{property_id}", response_model=Property)
def delete_property(property_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    property_service = PropertyService(db)
    db_property = property_service.delete_property(property_id)
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property