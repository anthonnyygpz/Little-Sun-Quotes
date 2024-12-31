from sqlalchemy import Column, Integer, String
from ..database import Base


class Designs(Base):
    __tablename__ = "designs"

    design_id = Column(
        Integer(), nullable=False, primary_key=True, autoincrement=True
    )
    design_name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    price = Column(Integer(), nullable=False)
