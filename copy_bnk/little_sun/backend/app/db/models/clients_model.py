from sqlalchemy import Column, DateTime, Integer, String, func
from ..database import Base
from sqlalchemy.orm import relationship


class Clients(Base):
    __tablename__ = "clients"

    client_id = Column(
        Integer(), nullable=False, primary_key=True, autoincrement=True
    )
    name = Column(String(), nullable=False)
    phone_number = Column(Integer(), nullable=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now()
    )
    quotes = relationship("Quotes", back_populates="client")
