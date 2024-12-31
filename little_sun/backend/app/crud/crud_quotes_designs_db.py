from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session


@dataclass
class QuotesDeginsDB:
    db: Session

    def create_quotes_designs_db(self):
        try:
            pass
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
