from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session


@dataclass
class QuoteDesignsRepositories:
    db: Session

    def create_quotes_designs_repositories(self):
        try:
            pass
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
