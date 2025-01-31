from dataclasses import dataclass
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.nail_sizes_models import NailSizes


@dataclass
class NailSizesDB:
    db: Session

    def get_nail_sizes_db(self):
        try:
            db_query = self.db.query(NailSizes).all()
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
