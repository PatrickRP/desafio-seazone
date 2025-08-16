from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    guests_quantity = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)

    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"), nullable=False)
    property = relationship("Property")
