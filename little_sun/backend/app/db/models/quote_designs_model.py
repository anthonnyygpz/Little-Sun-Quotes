from sqlalchemy import Column, Integer
from ..database import Base


class QuoteDesigns(Base):
    __tablename__ = "quote_designs"

    quote_id = Column(Integer(), nullable=False, primary_key=True)
    design_id = Column(Integer(), nullable=False, primary_key=True)
