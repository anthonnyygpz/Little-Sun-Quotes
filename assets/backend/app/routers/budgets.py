from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from little_sun.backend.app.schemas.budgets import CreateBudgetsSchemas
from ..dependencies import get_db
from ..services.budgets import BudgetsRepositories

router = APIRouter(
    prefix="/api",
    tags=["Budgets"],
    responses={400: {"description": "Not found"}},
)


@router.post("/upload_budgets")
async def upload_budgets(
    budget: CreateBudgetsSchemas, db: Session = Depends(get_db)
):
    return BudgetsRepositories(db).upload_budgets_repositories(budget)
