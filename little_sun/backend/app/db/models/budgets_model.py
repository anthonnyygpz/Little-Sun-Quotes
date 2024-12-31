from sqlalchemy import Column, Integer, Numeric
from ..database import Base


class Budgets(Base):
    __tablename__ = "budgets"

    budget_id = Column(
        Integer(), nullable=False, primary_key=True, autoincrement=True
    )
    id_client = Column(Integer(), nullable=False)
    id_nail_service = Column(Integer(), nullable=False)
    id_design = Column(Integer(), nullable=False)
    id_nail_size = Column(Integer(), nullable=False)
    total_budget = Column(Numeric(), nullable=False)
