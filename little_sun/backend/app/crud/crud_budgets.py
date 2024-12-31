from dataclasses import dataclass

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..db.models.budgets_model import Budgets
from ..schemas.budgets import CreateBudgetsSchemas


@dataclass
class BudgetsDB:
    db: Session

    def upload_budgets_db(self, budget: CreateBudgetsSchemas):
        try:
            pass
            db_query = Budgets(**budget.model_dump())
            self.db.add(db_query)
            self.db.commit()
            self.db.refresh(db_query)
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
