from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..services.quotes_repositories import QuotesRepositories
from ..schemas.quote_schema import CreateQuotesSchema

router = APIRouter(
    prefix="/api",
    tags=["Quote"],
    responses={400: {"Description": "Not found"}},
)


@router.post("/create_quotes")
async def create_quotes(
    quote: CreateQuotesSchema, db: Session = Depends(get_db)
):
    return QuotesRepositories(db).create_quotes_repositories(quote)
