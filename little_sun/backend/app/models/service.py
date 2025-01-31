from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from little_sun.backend.app.db.base import Base


class Service(Base):
    __tablename__ = "services"

    service_id = Column(Integer, primary_key=True, autoincrement=True)
    service_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)

    quotes = relationship(
        "Quote", secondary="quote_services", back_populates="services"
    )
