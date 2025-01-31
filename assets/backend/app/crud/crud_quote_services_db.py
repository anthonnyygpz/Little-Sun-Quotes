from dataclasses import dataclass
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.quote_services_model import QuoteServices

from ..schemas.quote_services_schema import CreateQuoteServicesSchema


@dataclass
class QuoteServicesDB:
    db: Session

    def create_quote_services_db(
        self, quote_services: CreateQuoteServicesSchema
    ):
        try:
            db_query = QuoteServices(**quote_services.model_dump())
            self.db.add(db_query)
            self.db.commit()
            self.db.refresh(db_query)
            return db_query
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
