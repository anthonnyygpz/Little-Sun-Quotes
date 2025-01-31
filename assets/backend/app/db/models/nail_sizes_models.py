from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from ..database import Base


class NailSizes(Base):
    __tablename__ = "nail_sizes"

    size_id = Column(
        Integer(), nullable=False, primary_key=True, autoincrement=True
    )
    size_name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    base_price = Column(Numeric(), nullable=True)

    quotes = relationship("Quotes", back_populates="nail_size")
