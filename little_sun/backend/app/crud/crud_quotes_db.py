from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..db.models.quotes_model import Quotes
from ..schemas.quote_schema import CreateQuotesSchema


@dataclass
class QuotesDB:
    db: Session

    def create_quotes_db(self, quote: CreateQuotesSchema):
        try:
            db_query = Quotes(**quote.model_dump())
            self.db.add(db_query)
            self.db.commit()
            self.db.refresh(db_query)
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def create_quotes_designs_db(self):
        try:
            pass
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
