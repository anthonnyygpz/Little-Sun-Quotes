from dataclasses import dataclass
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.designs_model import Designs


@dataclass
class DesignDB:
    db: Session

    def get_design_db(self):
        try:
            db_query = self.db.query(Designs).all()  
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
