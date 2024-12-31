from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..crud.crud_nail_services import NailServicesDB


@dataclass
class NailServicesRepositories:
    db: Session

    def get_nail_services_repositories(self):
        try:
            return NailServicesDB(self.db).get_nail_services_db()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
