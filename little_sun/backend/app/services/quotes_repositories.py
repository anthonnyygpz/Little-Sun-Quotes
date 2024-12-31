from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..crud.crud_quotes_db import QuotesDB
from ..schemas.quote_schema import CreateQuotesSchema


@dataclass
class QuotesRepositories:
    db: Session

    def create_quotes_repositories(self, quote: CreateQuotesSchema):
        try:
            return QuotesDB(self.db).create_quotes_db(quote)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def create_quotes_designs_repositories(self):
        try:
            return QuotesDB(self.db).create_quotes_designs_db()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
