from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..schemas.quote_designs_schemas import CreateQuoteDesignsSchema

from ..crud.crud_quote_designs_db import QuoteDeginsDB


@dataclass
class QuoteDesignsRepositories:
    db: Session

    def create_quotes_designs_repositories(
        self, quote_design: CreateQuoteDesignsSchema
    ):
        try:
            return QuoteDeginsDB(self.db).create_quote_designs_db(quote_design)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
