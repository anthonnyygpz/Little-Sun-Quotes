from sqlalchemy import Column, Integer, ForeignKey

from little_sun.backend.app.db.base import Base


class QuoteService(Base):
    __tablename__ = "quote_services"

    quote_id = Column(Integer, ForeignKey("quotes.quote_id"), primary_key=True)
    service_id = Column(Integer, ForeignKey("services.service_id"), primary_key=True)
