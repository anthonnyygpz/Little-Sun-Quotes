from sqlalchemy import Column, Integer
from ..database import Base


class QuoteServices(Base):
    __tablename__ = "quote_services"

    quote_id = Column(Integer(), nullable=False, primary_key=True)
    service_id = Column(Integer(), nullable=False)
