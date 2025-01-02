from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.services_models import Services


@dataclass
class ServicesDB:
    db: Session

    def get_nail_services_db(self):
        try:
            db_query = self.db.query(Services).all()

            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
