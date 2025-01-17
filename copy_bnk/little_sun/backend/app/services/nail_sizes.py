from dataclasses import dataclass
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..crud.crud_nail_sizes import NailSizesDB

@dataclass
class NailSizesRepositories:
    db: Session

    def get_nail_sizes(self):
        try:
            return NailSizesDB(self.db).get_nail_sizes_db() 
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
                      
