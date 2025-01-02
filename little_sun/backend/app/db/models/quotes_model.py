from sqlalchemy import Column, DateTime, Integer, Numeric, String, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import relationship
from ..database import Base


class Quotes(Base):
    __tablename__ = "quotes"

    quote_id = Column(Integer(), primary_key=True, autoincrement=True)
    client_id = Column(
        Integer(), ForeignKey("clients.client_id"), nullable=True
    )
    nail_size_id = Column(
        Integer(), ForeignKey("nail_sizes.size_id"), nullable=True
    )
    total_amount = Column(Numeric(10, 2), nullable=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now()
    )
    status = Column(String(), nullable=True, default="pending")

    client = relationship("Clients", back_populates="quotes")
    nail_size = relationship("NailSizes", back_populates="quotes")
    services = relationship(
        "Services", secondary="quote_services", back_populates="quotes"
    )
    designs = relationship(
        "Designs", secondary="quote_designs", back_populates="quotes"
    )
