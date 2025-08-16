from pydantic import BaseModel
from typing import Optional

class PropertyBase(BaseModel):
    title: str
    address_street: Optional[str] = None
    address_number: Optional[str] = None
    address_neighborhood: Optional[str] = None
    address_city: str
    address_state: str
    country: str = "Brazil"
    rooms: int
    capacity: int
    price_per_night: float


class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(PropertyBase):
    pass

class PropertyOut(PropertyBase):
    id: int

    class Config:
        from_attributes = True