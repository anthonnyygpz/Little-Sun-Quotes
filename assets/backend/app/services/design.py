from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..crud.crud_design import DesignDB 


@dataclass
class DesignRepositories:
    db: Session

    def get_design_repositories(self):
        try:
            return DesignDB(self.db).get_design_db() 
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
