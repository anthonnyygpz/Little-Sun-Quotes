from sqlalchemy import Column, Integer, ForeignKey
from ..database import Base


class QuoteDesigns(Base):
    __tablename__ = "quote_designs"

    quote_id = Column(
        Integer(), ForeignKey("quotes.quote_id"), primary_key=True
    )
    design_id = Column(
        Integer(), ForeignKey("designs.design_id"), primary_key=True
    )
