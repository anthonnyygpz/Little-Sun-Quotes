from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy import func
from ..database import Base


class Quotes(Base):
    __tablename__ = "quotes"

    quote_id = Column(
        Integer(), nullable=False, primary_key=True, autoincrement=True
    )
    client_id = Column(Integer(), nullable=True)
    nail_size_id = Column(Integer(), nullable=True)
    total_amount = Column(Numeric(10, 2), nullable=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, default=func.now()
    )
    status = Column(String(), nullable=True, default="pending")
