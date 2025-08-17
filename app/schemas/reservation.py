from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date
from decimal import Decimal

class ReservationBase(BaseModel):
    client_name: str
    client_email: EmailStr
    start_date: date
    end_date: date
    guests_quantity: int
    property_id: int

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    pass

class ReservationOut(ReservationBase):
    id: int
    total_price: Decimal

    class Config:
        pass

model_config = ConfigDict(from_attributes = True)