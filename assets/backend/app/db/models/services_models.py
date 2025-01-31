from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..database import Base


class Services(Base):
    __tablename__ = "services"

    service_id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    service_name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    price = Column(Integer(), nullable=False)

    quotes = relationship(
        "Quote", secondary="quote_services", back_populates="services"
    )
