from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    address_street = Column(String(255), nullable=True)
    address_number = Column(String(50), nullable=True)
    address_neighborhood = Column(String(100), nullable=True)
    address_city = Column(String(100), nullable=False)
    address_state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False, server_default="BRA")
    rooms = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
