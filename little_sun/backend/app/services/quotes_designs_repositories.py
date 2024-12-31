from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..crud.crud_quotes_designs_db import QuotesDeginsDB


@dataclass
class QuoteDesignsRepositories:
    db: Session

    def create_quotes_designs_repositories(self):
        try:
            return QuotesDeginsDB(self.db)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
