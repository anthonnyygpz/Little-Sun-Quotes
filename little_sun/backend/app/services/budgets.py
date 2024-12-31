from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from little_sun.backend.app.schemas.budgets import CreateBudgetsSchemas
from ..crud.crud_budgets import BudgetsDB


@dataclass
class BudgetsRepositories:
    db: Session

    def upload_budgets_repositories(self, budget: CreateBudgetsSchemas):
        try:
            return BudgetsDB(self.db).upload_budgets_db(budget)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
