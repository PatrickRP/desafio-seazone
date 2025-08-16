from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import reservation as reservation_schema
from app import models

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=reservation_schema.ReservationOut)
def create_reservation(payload: reservation_schema.ReservationCreate, db: Session = Depends(get_db)):
    # Valida se a propriedade existe
    prop = db.query(models.property.Property).filter(models.property.Property.id == payload.property_id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")

    # Valida capacidade
    if payload.guests_quantity > prop.capacity:
        raise HTTPException(status_code=400, detail="Exceeds property capacity")

    # Valida conflito de datas
    overlapping = db.query(models.reservation.Reservation).filter(
        models.reservation.Reservation.property_id == payload.property_id,
        models.reservation.Reservation.start_date < payload.end_date,
        models.reservation.Reservation.end_date > payload.start_date
    ).first()

    if overlapping:
        raise HTTPException(status_code=400, detail="Property not available for these dates")

    # Cálculo do número de noites
    nights = (payload.end_date - payload.start_date).days
    if nights <= 0:
        raise HTTPException(status_code=400, detail="End date must be after start date")

    total_price = nights * prop.price_per_night

    new_reservation = models.reservation.Reservation(**payload.dict(), total_price=total_price)
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


@router.get("/", response_model=List[reservation_schema.ReservationOut])
def list_reservations(
    client_email: str | None = None,
    property_id: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.reservation.Reservation)
    if client_email:
        query = query.filter(models.reservation.Reservation.client_email == client_email)
    if property_id:
        query = query.filter(models.reservation.Reservation.property_id == property_id)
    return query.all()


@router.delete("/{reservation_id}")
def cancel_reservation(reservation_id: int, db: Session = Depends(get_db)):
    res = db.query(models.reservation.Reservation).filter(models.reservation.Reservation.id == reservation_id).first()
    if not res:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(res)
    db.commit()
    return {"detail": "Reservation cancelled"}