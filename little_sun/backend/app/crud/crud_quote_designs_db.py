from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..db.models.quote_designs_model import QuoteDesigns
from ..schemas.quote_designs_schemas import CreateQuoteDesignsSchema


@dataclass
class QuoteDeginsDB:
    db: Session

    def create_quote_designs_db(self, quote_designs: CreateQuoteDesignsSchema):
        try:
            db_query = QuoteDesigns(**quote_designs.model_dump())
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
