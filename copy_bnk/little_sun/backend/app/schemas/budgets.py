from decimal import Decimal
from pydantic import BaseModel


class BudgetBase(BaseModel):
    pass


class CreateBudgetsSchemas(BudgetBase):
    id_client: int
    id_nail_service: int
    id_design: int
    id_nail_size: int
    total_budget: Decimal
