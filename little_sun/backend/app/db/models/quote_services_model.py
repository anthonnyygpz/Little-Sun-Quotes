from sqlalchemy import Column, Integer, ForeignKey
from ..database import Base


class QuoteServices(Base):
    __tablename__ = "quote_services"

    quote_id = Column(
        Integer(), ForeignKey("quotes.quote_id"), primary_key=True
    )
    service_id = Column(
        Integer(), ForeignKey("services.service_id"), primary_key=True
    )
