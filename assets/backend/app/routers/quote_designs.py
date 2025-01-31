from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas.quote_designs_schemas import CreateQuoteDesignsSchema
from ..dependencies import get_db
from ..services.quote_designs_repositories import QuoteDesignsRepositories

router = APIRouter(
    prefix="/api",
    tags=["Quotes Designs"],
    responses={400: {"description": "Not found"}},
)


@router.post("/create_quote_designs")
def create_quote_designs(
    quote_designs: CreateQuoteDesignsSchema, db: Session = Depends(get_db)
):
    return QuoteDesignsRepositories(db).create_quotes_designs_repositories(
        quote_designs
    )
