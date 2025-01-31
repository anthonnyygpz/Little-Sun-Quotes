from sqlalchemy import Column, Integer, String

from little_sun.backend.app.db.base import Base
from sqlalchemy.orm import relationship


class Design(Base):
    __tablename__ = "designs"

    design_id = Column(Integer, primary_key=True, autoincrement=True)
    design_name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)

    quotes = relationship("Quote", secondary="quote_designs", back_populates="designs")
