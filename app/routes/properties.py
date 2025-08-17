from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import property as property_schema
from app import models
from app.models.property import Property
from app.models.reservation import Reservation
from datetime import date

router = APIRouter(prefix="/properties", tags=["Properties"])

@router.post("/", response_model=property_schema.PropertyOut)
async def create_property(payload: property_schema.PropertyCreate, db: Session = Depends(get_db)):
    new_property = models.property.Property(**payload.model_dump())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

@router.get("/", response_model=List[property_schema.PropertyOut])
async def list_properties(
    ciy: str | None = None,
    state: str | None = None,
    capacity: int | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.property.Property)
    
    if ciy:
        query = query.filter(models.property.Property.address_city == ciy)
    if state:
        query = query.filter(models.property.Property.address_state == state)
    if capacity:
        query = query.filter(models.property.Property.capacity >= capacity)
    if max_price:
        query = query.filter(models.property.Property.price_per_night <= max_price)

    properties = query.all()
    
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found")
    
    return properties

@router.get("/availability")
def check_availability(
    property_id: int,
    start_date: date,
    end_date: date,
    guests_quantity: int,
    db: Session = Depends(get_db)
):
    # 1. Verifica se a propriedade existe
    prop = db.query(Property).filter(Property.id == property_id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")

    # 2. Verifica capacidade
    if guests_quantity > prop.capacity:
        return {"available": False, "reason": "Exceeds property capacity"}

    # 3. Verifica sobreposição de datas
    overlapping = db.query(Reservation).filter(
        Reservation.property_id == property_id,
        Reservation.start_date < end_date,
        Reservation.end_date > start_date
    ).first()

    if overlapping:
        return {"available": False, "reason": "Property already reserved in this period"}

    return {"available": True, "reason": "Property available"}

@router.get("/{property_id}", response_model=property_schema.PropertyOut)
def get_property(property_id: int, db: Session = Depends(get_db)):
    prop = db.query(models.property.Property).filter(models.property.Property.id == property_id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    return prop

@router.put("/{property_id}", response_model=property_schema.PropertyOut)
def update_property(property_id: int, payload: property_schema.PropertyUpdate, db: Session = Depends(get_db)):
    prop = db.query(models.property.Property).filter(models.property.Property.id == property_id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(prop, key, value)
    db.commit()
    db.refresh(prop)
    return prop


@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    prop = db.query(models.property.Property).filter(models.property.Property.id == property_id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    db.delete(prop)
    db.commit()
    return {"detail": "Property deleted"}