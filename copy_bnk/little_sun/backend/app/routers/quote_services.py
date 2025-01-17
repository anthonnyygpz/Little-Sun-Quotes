from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.quote_services_repositories import QuoteServiceRepositories
from ..dependencies import get_db
from ..schemas.quote_services_schema import CreateQuoteServicesSchema

router = APIRouter(
    prefix="/api",
    tags=["Quote Services"],
    responses={400: {"description": "Not found"}},
)


@router.post("/create_quote_services")
def create_quote_services(
    quote_services: CreateQuoteServicesSchema, db: Session = Depends(get_db)
):
    return QuoteServiceRepositories(db).create_quote_services_repositories(
        quote_services
    )
