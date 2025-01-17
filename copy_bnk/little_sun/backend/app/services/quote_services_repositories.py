from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas.quote_services_schema import CreateQuoteServicesSchema
from ..crud.crud_quote_services_db import QuoteServicesDB


@dataclass
class QuoteServiceRepositories:
    db: Session

    def create_quote_services_repositories(
        self, quote_services: CreateQuoteServicesSchema
    ):
        try:
            return QuoteServicesDB(self.db).create_quote_services_db(
                quote_services
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
